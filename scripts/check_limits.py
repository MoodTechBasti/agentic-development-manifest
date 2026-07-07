#!/usr/bin/env python3

import os
import argparse
from pathlib import Path

EXCLUDE_DIRS = {'.git', '.ai', '.venv', 'venv', 'node_modules', 'dist', 'build', 'coverage', '__pycache__', 'docs', 'spec', 'research', 'templates'}
EXCLUDE_FILES = {'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', 'poetry.lock', 'Cargo.lock', 'go.sum', 'Pipfile.lock'}
EXTENSIONS = {'.py', '.go', '.rs', '.js', '.jsx', '.ts', '.tsx', '.java', '.c', '.h', '.cpp', '.cs', '.php', '.rb', '.sh', '.bash'}

def count_lines(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as handle:
        return sum(1 for _ in handle)

def scan(root, max_lines):
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
            lines = count_lines(path)
            if lines > max_lines:
                violations.append((path.relative_to(root), lines))
    return violations, scanned

def main():
    parser = argparse.ArgumentParser(description='ADM line-limit validator')
    parser.add_argument('--path', default='.')
    parser.add_argument('--max-lines', type=int, default=300)
    args = parser.parse_args()
    root = Path(args.path).resolve()
    if not root.exists():
        print('Error: path does not exist:', root)
        return 1
    violations, scanned = scan(root, args.max_lines)
    print('ADM line-limit check: max', args.max_lines, 'lines')
    print('Scanned files:', scanned)
    if not violations:
        print('PASSED')
        return 0
    print('FAILED:', len(violations), 'file(s) exceed the limit')
    for path, lines in sorted(violations, key=lambda item: item[1], reverse=True):
        print(str(path), lines)
    print('Exceptions require a Decision Record in .ai/decisions/.')
    return 1

if __name__ == '__main__':
    raise SystemExit(main())
