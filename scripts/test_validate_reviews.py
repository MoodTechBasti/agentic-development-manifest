#!/usr/bin/env python3
"""Fixture tests for the ADM review validator."""

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / 'scripts' / 'validate_reviews.py'
SET_ID = 'RSV-20260708-fixture'
TARGET_REF = 'main'
TARGET_COMMIT = 'abcdef1234567'
REVIEW_TYPES = {
    'architect': ('ADM-TMP-REV-ARCH', 'REV-ARCH', 'Principal Architect'),
    'security': ('ADM-TMP-REV-SEC', 'REV-SEC', 'Security Engineer'),
    'performance': ('ADM-TMP-REV-PERF', 'REV-PERF', 'SRE and Performance Lead'),
    'cost': ('ADM-TMP-REV-COST', 'REV-COST', 'Cost Engineer'),
    'simplifier': ('ADM-TMP-REV-SIMP', 'REV-SIMP', 'Simplifier'),
    'documentation': ('ADM-TMP-REV-DOC', 'REV-DOC', 'Documentation Reviewer'),
}


def review_text(review_type, **overrides):
    template_id, prefix, role = REVIEW_TYPES[review_type]
    metadata = {
        'template_id': template_id,
        'template_type': 'review',
        'review_type': review_type,
        'role': role,
        'version': '1.2.0',
        'runtime_target': '.ai/reviews/',
        'review_id': f'{prefix}-20260708-fixture',
        'review_set_id': SET_ID,
        'target_ref': TARGET_REF,
        'target_commit': TARGET_COMMIT,
        'review_status': 'PASSED',
        'ci_ready': 'true',
        'confidence_score': '9',
    }
    metadata.update(overrides)
    lines = ['---']
    for key, value in metadata.items():
        lines.append(f'{key}: {value}')
    lines.extend(['---', '', f'# {role} Fixture Review', '', '- Vote: APPROVED'])
    return '\n'.join(lines) + '\n'


def write_set(root, types=None, directory='.ai/reviews', slug='fixture', **overrides):
    review_dir = root / directory
    review_dir.mkdir(parents=True, exist_ok=True)
    selected = types or list(REVIEW_TYPES)
    for review_type in selected:
        _, prefix, _ = REVIEW_TYPES[review_type]
        review_id = f'{prefix}-20260708-{slug}'
        path = review_dir / f'{review_id}.md'
        path.write_text(review_text(review_type, review_id=review_id, **overrides), encoding='utf-8')
    return review_dir


def run_validator(root, *args):
    command = [sys.executable, str(VALIDATOR), '--path', str(root), *args]
    return subprocess.run(command, text=True, capture_output=True, check=False)


def assert_result(name, result, expected_code, expected_text):
    output = result.stdout + result.stderr
    if result.returncode != expected_code or expected_text not in output:
        print(f'FAILED: {name}')
        print('Expected code:', expected_code)
        print('Actual code:', result.returncode)
        print('Expected text:', expected_text)
        print(output)
        raise SystemExit(1)
    print('PASSED:', name)


def complete_set_args():
    return [
        '--mode', 'complete-set',
        '--review-set-id', SET_ID,
        '--target-ref', TARGET_REF,
        '--target-commit', TARGET_COMMIT,
    ]


def test_empty_modes():
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        (root / '.ai' / 'reviews').mkdir(parents=True)
        result = run_validator(root, '--mode', 'existing-strict')
        assert_result('empty existing-strict passes', result, 0, 'No completed review artifacts found. PASSED')
        result = run_validator(root, '--mode', 'complete-set')
        assert_result('empty complete-set fails', result, 1, 'no completed review artifacts found')


def test_valid_complete_set():
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        write_set(root)
        result = run_validator(root, *complete_set_args())
        assert_result('valid complete-set passes', result, 0, 'PASSED: review set')


def test_missing_role_fails():
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        write_set(root, types=['architect', 'security', 'performance', 'cost', 'simplifier'])
        result = run_validator(root, *complete_set_args())
        assert_result('missing role fails', result, 1, 'missing PASSED ci-ready review types')


def test_mismatched_scope_fails():
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        write_set(root)
        path = root / '.ai' / 'reviews' / 'REV-DOC-20260708-fixture.md'
        path.write_text(review_text('documentation', target_commit='bbbbbbb'), encoding='utf-8')
        result = run_validator(root, *complete_set_args())
        assert_result('mismatched target_commit fails', result, 1, 'missing PASSED ci-ready review types')


def test_wrong_review_set_filter_fails():
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        write_set(root, review_set_id='RSV-20260708-other-fixture')
        result = run_validator(root, *complete_set_args())
        assert_result('wrong review_set_id filter fails', result, 1, 'no review artifacts match the requested scope')


def test_wrong_target_ref_filter_fails():
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        write_set(root, target_ref='release/v1')
        result = run_validator(root, *complete_set_args())
        assert_result('wrong target_ref filter fails', result, 1, 'no review artifacts match the requested scope')


def test_stale_complete_set_does_not_satisfy_new_scope():
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        write_set(root, slug='old-fixture', review_set_id='RSV-20260708-old-fixture')
        write_set(root, slug='fixture', types=['architect'], review_set_id=SET_ID)
        result = run_validator(root, *complete_set_args())
        assert_result('stale complete set cannot satisfy new scope', result, 1, 'missing PASSED ci-ready review types')


def test_duplicate_role_fails():
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        review_dir = write_set(root)
        duplicate = review_text('architect', review_id='REV-ARCH-20260708-fixture-two')
        (review_dir / 'REV-ARCH-20260708-fixture-two.md').write_text(duplicate, encoding='utf-8')
        result = run_validator(root, *complete_set_args())
        assert_result('duplicate role fails', result, 1, 'duplicate review types')


def test_invalid_metadata_fails():
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        write_set(root)
        path = root / '.ai' / 'reviews' / 'REV-SEC-20260708-fixture.md'
        path.write_text(review_text('security', ci_ready='false'), encoding='utf-8')
        result = run_validator(root, *complete_set_args())
        assert_result('PASSED with ci_ready false fails', result, 1, 'ci_ready must be true')
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        write_set(root)
        path = root / '.ai' / 'reviews' / 'REV-COST-20260708-fixture.md'
        path.write_text(review_text('cost', review_id='BAD-ID'), encoding='utf-8')
        result = run_validator(root, *complete_set_args())
        assert_result('invalid review_id fails', result, 1, 'review_id must match')


def main():
    tests = [
        test_empty_modes,
        test_valid_complete_set,
        test_missing_role_fails,
        test_mismatched_scope_fails,
        test_wrong_review_set_filter_fails,
        test_wrong_target_ref_filter_fails,
        test_stale_complete_set_does_not_satisfy_new_scope,
        test_duplicate_role_fails,
        test_invalid_metadata_fails,
    ]
    for test in tests:
        test()
    print('All ADM review validator fixture tests passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
