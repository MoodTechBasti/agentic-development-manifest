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
- `python scripts/validate_reviews.py --path . --advisory` remains a compatibility alias for advisory mode.

## Validation modes

| Mode | Blocks malformed existing reviews | Requires all 6 reviews | Intended use |
| --- | --- | --- | --- |
| `advisory` | No | No | Feature branches, local exploration, early agent work |
| `existing-strict` | Yes | No | PRs to `main` / `master`, strict syntax and metadata checks |
| `complete-set` | Yes | Yes | Release branches and manual release-readiness checks |

`complete-set` requires one passing, CI-ready review for every standard ADM review type: `architect`, `security`, `performance`, `cost`, `simplifier`, and `documentation`.

Each completed artifact in `complete-set` mode must use `review_status: PASSED` and `ci_ready: true`.

## Validated fields

The validator checks YAML frontmatter at the beginning of each completed review file and validates:

- `template_id`
- `template_type`
- `review_type`
- `role`
- `version`
- `runtime_target`
- `review_id`
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

This prevents normal feature work from deadlocking while still letting release branches enforce complete review-set readiness.
