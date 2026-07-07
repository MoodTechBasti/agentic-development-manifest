# ADM Review Validation

This document describes the advisory validation layer for completed ADM review artifacts.

## Scope

Reusable templates live in `templates/reviews/`.

Completed review artifacts live in `.ai/reviews/`.

The validator checks completed review artifacts only. It does not validate reusable templates as if they were completed reviews.

## Command

Strict local validation:

```bash
python scripts/validate_reviews.py --path .
```

Advisory validation:

```bash
python scripts/validate_reviews.py --path . --advisory
```

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

Example:

```text
REV-SEC-20260708-ai-routing
```

## CI mode

The GitHub workflow runs the validator in advisory mode. This surfaces malformed review artifacts without turning every feature branch into a hard review-gate branch.

A hard review gate can be added later when ADM defines which phases, branches, or release types require complete review sets.
