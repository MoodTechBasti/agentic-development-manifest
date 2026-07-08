# ADM Review Runbook

This runbook describes the operational happy path for creating and validating a complete ADM review set.

## 1. When to use a complete review set

Use a six-role complete review set for:

- release readiness
- phase transitions
- governance changes
- architecture-critical changes
- security-, cost-, or performance-sensitive changes

Do not require a complete review set for every small feature branch. Use `advisory` or `existing-strict` there.

## 2. Standard review roles

A complete ADM review set requires exactly one passing, CI-ready review for each role:

| Review type | Runtime prefix |
| --- | --- |
| `architect` | `REV-ARCH` |
| `security` | `REV-SEC` |
| `performance` | `REV-PERF` |
| `cost` | `REV-COST` |
| `simplifier` | `REV-SIMP` |
| `documentation` | `REV-DOC` |

## 3. Happy path

### Step 1: Commit the code under review

Finish the code, documentation, or governance change first.

Record the stable code-under-review SHA:

```bash
git rev-parse HEAD
```

This value becomes `target_commit`.

### Step 2: Choose review scope

Choose one set ID and one target reference.

Example:

```text
review_set_id: RSV-20260708-review-governance-v0111
target_ref: main
target_commit: 8afe6714a0ccfcee83a18e2c1fe746b1b160a630
```

Use `target_ref: main` when reviewing a stable main commit. Use `target_ref: PR-<number>` only when the PR head itself is the code under review.

### Step 3: Create runtime review files

Copy the six templates from `templates/reviews/` into `.ai/reviews/` and rename each file by its runtime `review_id`.

Example filenames:

```text
.ai/reviews/REV-ARCH-20260708-feature.md
.ai/reviews/REV-SEC-20260708-feature.md
.ai/reviews/REV-PERF-20260708-feature.md
.ai/reviews/REV-COST-20260708-feature.md
.ai/reviews/REV-SIMP-20260708-feature.md
.ai/reviews/REV-DOC-20260708-feature.md
```

Do not use static runtime names such as `.ai/reviews/architect.md`.

### Step 4: Fill required frontmatter

All six files must share the same:

- `review_set_id`
- `target_ref`
- `target_commit`

Each file must also have:

```yaml
review_status: PASSED
ci_ready: true
```

for release-grade complete-set validation.

### Step 5: Validate locally

Validate existing review artifacts:

```bash
python scripts/validate_reviews.py --path . --mode existing-strict
```

Validate a complete set:

```bash
python scripts/validate_reviews.py \
  --path . \
  --mode complete-set \
  --review-set-id RSV-20260708-review-governance-v0111 \
  --target-ref main \
  --target-commit 8afe6714a0ccfcee83a18e2c1fe746b1b160a630
```

### Step 6: Open the PR

The normal PR workflow runs `existing-strict`. It proves that existing runtime review artifacts are structurally valid.

### Step 7: Run release-grade validation manually

After merge, run the GitHub workflow manually:

1. Open **Actions**.
2. Select **ADM Quality Gate**.
3. Click **Run workflow**.
4. Select branch `main`.
5. Set `review_gate_mode` to `complete-set`.
6. Set `review_set_id` to the set ID.
7. Set `reviewed_commit` to the stable code-under-review SHA.
8. Run the workflow.

The workflow should print the selected mode, target ref, and reviewed code commit before running the validator.

## 4. Common failures

### Missing role

Cause: one of the six required review types is missing.

Fix: add the missing runtime review artifact.

### Duplicate role

Cause: two files in the same review set declare the same `review_type`.

Fix: keep exactly one file per role for the review set.

### Mismatched review_set_id

Cause: one file belongs to a different set.

Fix: align all six files to the same `review_set_id`.

### Mismatched target_commit

Cause: one review points to a different reviewed code commit.

Fix: verify the actual code-under-review SHA and align all six files.

### PASSED with ci_ready false

Cause: the review says it passed but is not CI-ready.

Fix: either set `ci_ready: true` after the review is complete, or change `review_status` to `PENDING`, `FAILED`, or `NEEDS_REVISION`.

### Invalid review_id

Cause: the review ID does not match the required prefix and date pattern.

Fix: use the correct prefix, date, and slug, for example `REV-SEC-20260708-auth-hardening`.

## 5. Validator fixture tests

Run the validator fixture test suite with:

```bash
python scripts/test_validate_reviews.py
```

The test suite covers both the happy path and expected failure modes for malformed or incomplete review sets.
