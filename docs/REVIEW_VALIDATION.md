# ADM Review Validation

This document describes the validation layer for completed ADM review artifacts.

## Scope

Reusable templates live in `templates/reviews/`.

Completed review artifacts live in `.ai/reviews/`.

The validator checks completed review artifacts only. It does not validate reusable templates as if they were completed reviews.

## Commands

- `python scripts/validate_reviews.py --path . --mode advisory`
- `python scripts/validate_reviews.py --path . --mode existing-strict`
- `python scripts/validate_reviews.py --path . --mode complete-set`
- `python scripts/validate_reviews.py --path . --mode complete-set --review-set-id RSV-20260708-review-set-scoping --target-ref PR-2 --target-commit <git-sha>`
- `python scripts/validate_reviews.py --path . --advisory` remains a compatibility alias for advisory mode.
- `python scripts/validate_reviews.py --dir .ai/reviews --strict --set-id RSV-20260708-review-set-scoping` remains a compatibility form for complete-set validation.

## Validation modes

| Mode | Blocks malformed existing reviews | Requires all 6 reviews | Intended use |
| --- | --- | --- | --- |
| `advisory` | No | No | Feature branches, local exploration, early agent work |
| `existing-strict` | Yes | No | PRs to `main` / `master`, strict syntax and metadata checks |
| `complete-set` | Yes | Yes, scoped | Release branches and manual release-readiness checks |

`complete-set` requires one passing, CI-ready review for every standard ADM review type: `architect`, `security`, `performance`, `cost`, `simplifier`, and `documentation`.

Each completed artifact in `complete-set` mode must use `review_status: PASSED` and `ci_ready: true`.

## Review set scoping

ADM v0.11 adds target binding to prevent stale reviews from satisfying new release gates.

Every completed review artifact must include:

- `review_set_id`, using the pattern `RSV-YYYYMMDD-feature-slug`
- `target_ref`, such as `PR-2`, `release/v1`, or a branch name
- `target_commit`, the 7 to 40 character hexadecimal git commit hash being reviewed

A complete set passes only when all six review types share the same `review_set_id`, `target_ref`, and `target_commit`.

Recommended runtime filenames use the review ID instead of static role names, for example:

- `.ai/reviews/REV-ARCH-20260708-review-set-scoping.md`
- `.ai/reviews/REV-SEC-20260708-review-set-scoping.md`

Do not write completed runtime reviews to static names such as `.ai/reviews/architect.md`, because that destroys review history.

## Validated fields

The validator checks YAML frontmatter at the beginning of each completed review file and validates:

- `template_id`
- `template_type`
- `review_type`
- `role`
- `version`
- `runtime_target`
- `review_id`
- `review_set_id`
- `target_ref`
- `target_commit`
- `review_status`
- `ci_ready`
- optional `confidence_score`

## Status rules

Allowed `review_status` values:

- `PENDING`
- `PASSED`
- `FAILED`
- `NEEDS_REVISION`

`ci_ready` must be `true` only when `review_status` is `PASSED`.

When `review_status` is `PASSED` or `ci_ready` is `true`, `review_set_id`, `target_ref`, and `target_commit` must be filled.

## Review ID rules

Review IDs must match their review type:

| Review type | Prefix |
| --- | --- |
| `architect` | `REV-ARCH` |
| `security` | `REV-SEC` |
| `performance` | `REV-PERF` |
| `cost` | `REV-COST` |
| `simplifier` | `REV-SIMP` |
| `documentation` | `REV-DOC` |

Example: `REV-SEC-20260708-ai-routing`

## CI mode

The GitHub workflow selects the review mode by branch context:

- feature branches and `dev`: `advisory`
- pull requests to `main` / `master`: `existing-strict`
- pushes to `main` / `master`: `existing-strict`
- `release/**` branches and pull requests targeting `release/**`: `complete-set`
- manual `workflow_dispatch`: selected by input, defaulting to `existing-strict`

For `complete-set`, the workflow passes `target_ref` and `target_commit` into the validator. Pull requests use `PR-<number>` and the PR head SHA. Pushes use the branch name and workflow SHA.

This prevents normal feature work from deadlocking while still letting release branches enforce complete review-set readiness for the exact code target being released.
