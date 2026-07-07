#!/usr/bin/env python3
"""ADM line-limit validator with Decision Record exemptions."""

import argparse
import os
import re
from pathlib import Path

EXCLUDE_DIRS = {'.git', '.ai', '.venv', 'venv', 'env', 'node_modules', 'dist', 'build', 'coverage', '__pycache__', 'docs', 'spec', 'research', 'templates'}
EXCLUDE_FILES = {'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', 'poetry.lock', 'Cargo.lock', 'go.sum', 'Pipfile.lock'}
EXTENSIONS = {'.py', '.go', '.rs', '.js', '.jsx', '.ts', '.tsx', '.java', '.c', '.h', '.cpp', '.cs', '.php', '.rb', '.sh', '.bash'}
DECISION_DIRS = ('adr', 'docs/adr', 'docs/decisions', '.ai/decisions')
EXEMPTION_RE = re.compile(r'(?:\*\*)?ADM-Exemption(?:\*\*)?:\s*`?([^`\s]+)`?\s*\(Max:\s*(\d+)\)', re.IGNORECASE)
STATUS_RE = re.compile(r'(?:^|\n)\s*(?:Status\s*:\s*|\|\s*Status\s*\|\s*)(ACCEPTED|APPROVED)', re.IGNORECASE)


def count_lines(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as handle:
        return sum(1 for _ in handle)


def normalize(path):
    return str(path).replace('\\', '/').strip().lstrip('./')


def accepted_decision(text):
    return bool(STATUS_RE.search(text))


def parse_exemptions(root):
    exemptions = {}
    ignored = []
    for rel_dir in DECISION_DIRS:
        decision_dir = root / rel_dir
        if not decision_dir.exists():
            continue
        for md_file in decision_dir.rglob('*.md'):
            text = md_file.read_text(encoding='utf-8', errors='ignore')
            matches = EXEMPTION_RE.findall(text)
            if not matches:
                continue
            if not accepted_decision(text):
                ignored.append(str(md_file.relative_to(root)))
                continue
            for file_path, max_lines in matches:
                exemptions[normalize(file_path)] = int(max_lines)
    return exemptions, ignored


def scan(root, max_lines, exemptions):
    violations = []
    scanned = 0
    for current_root, dirs, files in os.walk(root):
        dirs[:] = [name for name in dirs if name not in EXCLUDE_DIRS]
        for file_name in files:
            if file_name in EXCLUDE_FILES:
                continue
            path = Path(current_root) / file_name
            if path.suffix.lower() not in EXTENSIONS:
                continue
            scanned += 1
            rel_path = normalize(path.relative_to(root))
            lines = count_lines(path)
            allowed = exemptions.get(rel_path, max_lines)
            if lines > allowed:
                violations.append((rel_path, lines, allowed, rel_path in exemptions))
    return violations, scanned


def main():
    parser = argparse.ArgumentParser(description='ADM line-limit validator')
    parser.add_argument('--path', default='.')
    parser.add_argument('--max-lines', type=int, default=300)
    parser.add_argument('--exclude-dir', action='append', default=[])
    parser.add_argument('--exclude-file', action='append', default=[])
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.exists():
        print('Error: path does not exist:', root)
        return 1

    global EXCLUDE_DIRS, EXCLUDE_FILES
    EXCLUDE_DIRS = EXCLUDE_DIRS | set(args.exclude_dir)
    EXCLUDE_FILES = EXCLUDE_FILES | set(args.exclude_file)

    exemptions, ignored = parse_exemptions(root)
    violations, scanned = scan(root, args.max_lines, exemptions)

    print('ADM line-limit check')
    print('Root:', root)
    print('Default max lines:', args.max_lines)
    print('Scanned files:', scanned)
    print('Accepted exemptions:', len(exemptions))
    if ignored:
        print('Ignored exemption files without accepted status:', ', '.join(ignored))

    if not violations:
        print('PASSED')
        return 0

    print('FAILED:', len(violations), 'file(s) exceed their allowed line limit')
    print('File | Lines | Allowed')
    print('--- | --- | ---')
    for path, lines, allowed, exempted in sorted(violations, key=lambda item: item[1], reverse=True):
        suffix = ' ADR' if exempted else ''
        print(f'{path} | {lines} | {allowed}{suffix}')
    print('Exemptions require an accepted Decision Record containing: ADM-Exemption: path/to/file (Max: lines)')
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
