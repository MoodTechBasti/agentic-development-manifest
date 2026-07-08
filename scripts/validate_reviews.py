#!/usr/bin/env python3
"""ADM review frontmatter validator without external dependencies."""

import argparse
import os
import re
import subprocess
from collections import defaultdict
from pathlib import Path

VALID_TYPES = {
    'architect': 'REV-ARCH',
    'security': 'REV-SEC',
    'performance': 'REV-PERF',
    'cost': 'REV-COST',
    'simplifier': 'REV-SIMP',
    'documentation': 'REV-DOC',
}
REQUIRED_KEYS = {
    'template_id', 'template_type', 'review_type', 'role', 'version',
    'runtime_target', 'review_id', 'review_set_id', 'target_ref',
    'target_commit', 'review_status', 'ci_ready',
}
VALID_STATUSES = {'PENDING', 'PASSED', 'FAILED', 'NEEDS_REVISION'}
TRUE_VALUES = {'true', 'yes', '1'}
FALSE_VALUES = {'false', 'no', '0'}
FRONTMATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
REVIEW_SET_RE = re.compile(r'^RSV-\d{8}-[a-z0-9][a-z0-9-]*$')
TARGET_COMMIT_RE = re.compile(r'^[0-9a-fA-F]{7,40}$')


def repo_root(start: Path) -> Path:
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--show-toplevel'],
            cwd=start, text=True, capture_output=True, check=True,
        )
        return Path(result.stdout.strip()).resolve()
    except Exception:
        current = start.resolve()
        for parent in [current, *current.parents]:
            if (parent / '.git').exists() or (parent / '.ai').exists():
                return parent
        return current


def parse_frontmatter(path: Path) -> dict[str, str] | None:
    match = FRONTMATTER_RE.match(path.read_text(encoding='utf-8', errors='ignore'))
    if not match:
        return None
    metadata: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if line and not line.startswith('#') and ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip().strip('"').strip("'")
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


def validate_scope_fields(metadata: dict[str, str], errors: list[str]) -> None:
    status = metadata.get('review_status', '')
    ci_ready = bool_value(metadata.get('ci_ready', ''))
    review_set_id = metadata.get('review_set_id', '').strip()
    target_ref = metadata.get('target_ref', '').strip()
    target_commit = metadata.get('target_commit', '').strip()
    if review_set_id and not REVIEW_SET_RE.match(review_set_id):
        errors.append('review_set_id must match RSV-YYYYMMDD-feature-slug')
    if target_commit and not TARGET_COMMIT_RE.match(target_commit):
        errors.append('target_commit must be a 7 to 40 character hexadecimal git commit hash')
    if status == 'PASSED' or ci_ready is True:
        for key, value in (
            ('review_set_id', review_set_id),
            ('target_ref', target_ref),
            ('target_commit', target_commit),
        ):
            if not value:
                errors.append(f'{key} must be filled when review_status is PASSED or ci_ready is true')


def validate_review(path: Path) -> tuple[dict[str, str] | None, list[str]]:
    errors: list[str] = []
    metadata = parse_frontmatter(path)
    if metadata is None:
        return None, ['missing YAML frontmatter at file start']
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
    elif review_type in VALID_TYPES and not re.match(rf'^{VALID_TYPES[review_type]}-\d{{8}}-[a-z0-9][a-z0-9-]*$', review_id):
        errors.append(f'review_id must match {VALID_TYPES[review_type]}-YYYYMMDD-feature-slug')
    validate_scope_fields(metadata, errors)
    validate_confidence(metadata, errors)
    return metadata, errors


def review_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(
        path for path in directory.glob('*.md')
        if path.name.lower() not in {'readme.md', '.gitkeep'}
    )


def scoped_items(reviewed, review_set_id, target_ref, target_commit):
    items = [(p, m) for p, m, errors in reviewed if m is not None and not errors]
    if review_set_id:
        items = [(p, m) for p, m in items if m.get('review_set_id') == review_set_id]
    if target_ref:
        items = [(p, m) for p, m in items if m.get('target_ref') == target_ref]
    if target_commit:
        items = [(p, m) for p, m in items if m.get('target_commit', '').lower() == target_commit.lower()]
    return items


def validate_one_set(set_id: str, items, target_ref, target_commit, root: Path) -> bool:
    failed = False
    by_type: dict[str, list[tuple[Path, dict[str, str]]]] = defaultdict(list)
    for path, metadata in items:
        by_type[metadata.get('review_type', '')].append((path, metadata))
    duplicates = sorted(name for name, values in by_type.items() if name in VALID_TYPES and len(values) > 1)
    missing = sorted(set(VALID_TYPES) - set(by_type))
    target_refs = {metadata.get('target_ref', '') for _, metadata in items}
    target_commits = {metadata.get('target_commit', '').lower() for _, metadata in items}
    checks = [
        (duplicates, 'duplicate review types: ' + ', '.join(duplicates)),
        (missing, 'missing PASSED ci-ready review types: ' + ', '.join(missing)),
        (len(target_refs) != 1, 'target_ref values differ: ' + ', '.join(sorted(target_refs))),
        (len(target_commits) != 1, 'target_commit values differ: ' + ', '.join(sorted(target_commits))),
        (target_ref and target_refs != {target_ref}, f'target_ref must match requested scope {target_ref}'),
        (target_commit and target_commits != {target_commit.lower()}, f'target_commit must match requested scope {target_commit}'),
    ]
    for condition, message in checks:
        if condition:
            failed = True
            print(f'FAILED: review set {set_id}')
            print('  - ' + message)
    for path, metadata in items:
        status = metadata.get('review_status', '')
        ci_ready = bool_value(metadata.get('ci_ready', ''))
        if status != 'PASSED' or ci_ready is not True:
            failed = True
            print(f'FAILED: {os.path.relpath(path, root)}')
            print('  - complete-set mode requires review_status PASSED and ci_ready true')
    if not failed:
        print(f'PASSED: review set {set_id}')
    return failed


def validate_complete_set(reviewed, root, review_set_id=None, target_ref=None, target_commit=None) -> bool:
    items = scoped_items(reviewed, review_set_id, target_ref, target_commit)
    if not items:
        print('FAILED: complete review set')
        print('  - no review artifacts match the requested scope')
        return True
    sets: dict[str, list[tuple[Path, dict[str, str]]]] = defaultdict(list)
    for path, metadata in items:
        if metadata.get('review_set_id'):
            sets[metadata['review_set_id']].append((path, metadata))
    if not sets:
        print('FAILED: complete review set')
        print('  - no scoped review_set_id found')
        return True
    failed = False
    passing_sets = 0
    for set_id, set_items in sorted(sets.items()):
        set_failed = validate_one_set(set_id, set_items, target_ref, target_commit, root)
        passing_sets += 0 if set_failed else 1
        failed = failed or set_failed
    if passing_sets == 0:
        failed = True
        print('FAILED: complete review set')
        print('  - no complete scoped review set passed')
    return failed


def parse_args():
    parser = argparse.ArgumentParser(description='Validate ADM review artifacts')
    parser.add_argument('--path', default='.', help='Repository path')
    parser.add_argument('--reviews-dir', default='.ai/reviews', help='Review artifact directory')
    parser.add_argument('--dir', dest='reviews_dir_alias', help='Deprecated alias for --reviews-dir')
    parser.add_argument('--mode', choices=('advisory', 'existing-strict', 'complete-set'))
    parser.add_argument('--advisory', action='store_true', help='Deprecated alias for --mode advisory')
    parser.add_argument('--strict', action='store_true', help='Deprecated alias for --mode complete-set')
    parser.add_argument('--review-set-id', help='Require a specific review_set_id')
    parser.add_argument('--set-id', dest='set_id_alias', help='Deprecated alias for --review-set-id')
    parser.add_argument('--target-ref', help='Require a specific target_ref')
    parser.add_argument('--target-commit', help='Require a specific target_commit')
    return parser.parse_args()


def resolve_mode(args) -> str:
    if args.mode and (args.advisory or args.strict):
        raise SystemExit('error: --mode cannot be combined with --advisory or --strict')
    if args.advisory and args.strict:
        raise SystemExit('error: --advisory cannot be combined with --strict')
    if args.advisory:
        return 'advisory'
    if args.strict:
        return 'complete-set'
    return args.mode or 'existing-strict'


def main() -> int:
    args = parse_args()
    mode = resolve_mode(args)
    root = repo_root(Path(args.path))
    reviews_arg = args.reviews_dir_alias or args.reviews_dir
    reviews_path = Path(reviews_arg) if Path(reviews_arg).is_absolute() else root / reviews_arg
    review_set_id = args.review_set_id or args.set_id_alias
    print('ADM review validator')
    print('Root:', root)
    print('Reviews:', reviews_path)
    print('Mode:', mode)
    for label, value in (('Review set scope', review_set_id), ('Target ref scope', args.target_ref), ('Target commit scope', args.target_commit)):
        if value:
            print(f'{label}: {value}')
    if mode == 'complete-set':
        print('Complete-set scope filters are applied after structural validation.')
    files = review_files(reviews_path)
    if not files:
        if mode == 'complete-set':
            print('FAILED: complete review set')
            print('  - no completed review artifacts found')
            return 1
        print('No completed review artifacts found. PASSED')
        return 0
    failed = False
    reviewed = []
    for path in files:
        metadata, errors = validate_review(path)
        reviewed.append((path, metadata, errors))
        rel_path = os.path.relpath(path, root)
        if errors:
            failed = True
            print(f'FAILED: {rel_path}')
            for error in errors:
                print(f'  - {error}')
        else:
            print(f'PASSED: {rel_path}')
    if mode == 'complete-set':
        failed = validate_complete_set(reviewed, root, review_set_id, args.target_ref, args.target_commit) or failed
    if failed:
        print('Review validation completed with errors.')
        return 0 if mode == 'advisory' else 1
    if mode == 'complete-set':
        print('All required completed review artifacts are valid, scoped, PASSED, and CI-ready.')
    else:
        print('All completed review artifacts are valid.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
