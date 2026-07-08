# ADM Review Templates

This directory contains reusable review templates for the ADM multi-agent review process.

## Template location vs runtime location

- Reusable templates live in `templates/reviews/`.
- Completed review artifacts live in `.ai/reviews/`.

Do not store empty templates in `.ai/reviews/`. That directory is runtime project memory and should contain concrete, dated review artifacts only.

Completed runtime reviews must not use static role filenames such as `.ai/reviews/architect.md`. Use the runtime review ID as the filename so historical reviews are not overwritten.

## Available templates

| Template | Role | Runtime ID prefix |
| --- | --- | --- |
| `architect.md` | Principal Architect | `REV-ARCH` |
| `security.md` | Security Engineer | `REV-SEC` |
| `performance.md` | SRE and Performance Lead | `REV-PERF` |
| `cost.md` | Cost Engineer | `REV-COST` |
| `simplifier.md` | Simplifier | `REV-SIMP` |
| `documentation.md` | Documentation Reviewer | `REV-DOC` |

## Required runtime scope

Every completed review must include:

- `review_set_id`, for example `RSV-20260708-review-set-scoping`
- `target_ref`, for example `PR-2` or `release/v1`
- `target_commit`, the git commit SHA being reviewed

All six reviews in one complete set must share the same scope values.

## Usage

Copy the relevant template into `.ai/reviews/`, rename it with the runtime review ID, and fill it before marking the related work CI-ready.

Example:

```bash
cp templates/reviews/security.md .ai/reviews/REV-SEC-20260708-ai-routing.md
```

The completed review must state a final vote, CI-readiness status, review-set scope, target reference, and target commit.
