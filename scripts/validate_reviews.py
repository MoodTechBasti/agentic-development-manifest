#!/usr/bin/env python3
"""ADM review frontmatter validator.

Validates completed review artifacts in .ai/reviews/ without external dependencies.
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

REQUIRED_KEYS = {
    'template_id',
    'template_type',
    'review_type',
    'role',
    'version',
    'runtime_target',
    'review_id',
    'review_status',
    'ci_ready',
}

VALID_TYPES = {
    'architect': 'REV-ARCH',
    'security': 'REV-SEC',
    'performance': 'REV-PERF',
    'cost': 'REV-COST',
    'simplifier': 'REV-SIMP',
    'documentation': 'REV-DOC',
}

VALID_STATUSES = {'PENDING', 'PASSED', 'FAILED', 'NEEDS_REVISION'}
TRUE_VALUES = {'true', 'yes', '1'}
FALSE_VALUES = {'false', 'no', '0'}
FRONTMATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)


def repo_root(start: Path) -> Path:
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--show-toplevel'],
            cwd=start,
            text=True,
            capture_output=True,
            check=True,
        )
        return Path(result.stdout.strip()).resolve()
    except Exception:
        current = start.resolve()
        for parent in [current, *current.parents]:
            if (parent / '.git').exists() or (parent / '.ai').exists():
                return parent
        return current


def parse_frontmatter(path: Path) -> dict[str, str] | None:
    text = path.read_text(encoding='utf-8', errors='ignore')
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None

    metadata: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' not in line:
            continue
        key, value = line.split(':', 1)
        clean_value = value.strip().strip('"').strip("'")
        metadata[key.strip()] = clean_value
    return metadata


def bool_value(value: str) -> bool | None:
    normalized = value.strip().lower()
    if normalized in TRUE_VALUES:
        return True
    if normalized in FALSE_VALUES:
        return False
    return None


def validate_confidence(metadata: dict[str, str], errors: list[str]) -> None:
    value = metadata.get('confidence_score', '').strip().lower()
    if not value or value == 'null':
        return
    try:
        score = int(value)
    except ValueError:
        errors.append('confidence_score must be an integer from 1 to 10 or null')
        return
    if score < 1 or score > 10:
        errors.append('confidence_score must be between 1 and 10')


def validate_review(path: Path) -> list[str]:
    errors: list[str] = []
    metadata = parse_frontmatter(path)
    if metadata is None:
        return ['missing YAML frontmatter at file start']

    missing = sorted(REQUIRED_KEYS - set(metadata))
    if missing:
        errors.append('missing required keys: ' + ', '.join(missing))

    review_type = metadata.get('review_type', '')
    if review_type not in VALID_TYPES:
        errors.append('review_type must be one of: ' + ', '.join(sorted(VALID_TYPES)))

    if metadata.get('template_type') != 'review':
        errors.append("template_type must be 'review'")

    if metadata.get('runtime_target') != '.ai/reviews/':
        errors.append("runtime_target must be '.ai/reviews/'")

    status = metadata.get('review_status', '')
    if status not in VALID_STATUSES:
        errors.append('review_status must be one of: ' + ', '.join(sorted(VALID_STATUSES)))

    ci_ready = bool_value(metadata.get('ci_ready', ''))
    if ci_ready is None:
        errors.append('ci_ready must be true or false')
    elif status == 'PASSED' and not ci_ready:
        errors.append('ci_ready must be true when review_status is PASSED')
    elif status != 'PASSED' and ci_ready:
        errors.append('ci_ready cannot be true unless review_status is PASSED')

    review_id = metadata.get('review_id', '')
    if not review_id:
        errors.append('review_id must be filled')
    elif review_type in VALID_TYPES:
        prefix = VALID_TYPES[review_type]
        pattern = rf'^{prefix}-\d{{8}}-[a-z0-9][a-z0-9-]*$'
        if not re.match(pattern, review_id):
            errors.append(f'review_id must match {prefix}-YYYYMMDD-feature-slug')

    validate_confidence(metadata, errors)
    return errors


def review_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    ignored = {'readme.md', '.gitkeep'}
    return sorted(
        path for path in directory.glob('*.md')
        if path.name.lower() not in ignored
    )


def main() -> int:
    parser = argparse.ArgumentParser(description='Validate ADM review artifacts')
    parser.add_argument('--path', default='.', help='Repository path')
    parser.add_argument('--reviews-dir', default='.ai/reviews', help='Review artifact directory')
    parser.add_argument('--advisory', action='store_true', help='Report errors but exit 0')
    args = parser.parse_args()

    root = repo_root(Path(args.path))
    reviews_path = root / args.reviews_dir
    files = review_files(reviews_path)

    print('ADM review validator')
    print('Root:', root)
    print('Reviews:', reviews_path)
    print('Mode:', 'advisory' if args.advisory else 'strict')

    if not files:
        print('No completed review artifacts found. PASSED')
        return 0

    failed = False
    for path in files:
        rel_path = os.path.relpath(path, root)
        errors = validate_review(path)
        if not errors:
            print(f'PASSED: {rel_path}')
            continue
        failed = True
        print(f'FAILED: {rel_path}')
        for error in errors:
            print(f'  - {error}')

    if failed:
        print('Review validation completed with errors.')
        return 0 if args.advisory else 1

    print('All completed review artifacts are valid.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
