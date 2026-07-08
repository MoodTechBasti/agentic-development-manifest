# Changelog

## [v0.12.1] — 2026-07-08

### Repository Hygiene and PR Template

- Added a targeted `.gitignore` for Python, Node, build output, local secrets, editor files, and transient ADM agent runtime data.
- Kept versioned ADM governance artifacts under `.ai/reviews/`, `.ai/decisions/`, and `.ai/handover/` intentionally visible.
- Added `.github/pull_request_template.md` with ADM compliance, quality gate, review-scope, and validation sections.
- Added `.ai/README.md` to document which `.ai/` artifacts may be committed and which local agent outputs must remain ignored.

## [v0.12] — 2026-07-08

### Validator Fixture Tests and Review Runbook

- Added `scripts/test_validate_reviews.py` with dependency-free fixture tests for the ADM review validator.
- Added positive complete-set coverage for a fully scoped six-role review set.
- Added negative fixture coverage for empty complete-set runs, missing roles, duplicate roles, mismatched target commits, invalid `ci_ready`, and invalid `review_id` metadata.
- Updated `.github/workflows/adm-quality-gate.yml` to run the validator fixture tests in CI.
- Added `docs/REVIEW_RUNBOOK.md` with the operational happy path and common failure modes for complete ADM review sets.

## [v0.11.1] — 2026-07-08

### Stable Reviewed-Code SHA

- Added `docs/decisions/ADR-20260708-stable-reviewed-code-sha.md` to document stable code-under-review commit handling.
- Updated `.github/workflows/adm-quality-gate.yml` so `complete-set` gates use a stable code-under-review SHA instead of blindly using the workflow commit SHA.
- Added full checkout history for review-gate runs so CI can resolve the latest commit outside `.ai/reviews/`.
- Added optional manual `reviewed_commit` workflow input for explicit release-readiness checks.
- Updated review validation, operating system, and ADM specification docs to clarify that `target_commit` means the reviewed code commit, not necessarily the commit containing review artifacts.

## [v0.11] — 2026-07-08

### Review Set Scoping

- Added `docs/decisions/ADR-20260708-review-set-scoping.md` to define review-set scoping and target binding.
- Extended `scripts/validate_reviews.py` with `review_set_id`, `target_ref`, and `target_commit` validation.
- Updated `complete-set` validation so six reviews must belong to the same set, target ref, and target commit.
- Updated the ADM quality gate workflow to pass target reference and target commit into release-grade complete-set validation.
- Updated all six review templates with v0.11 scope metadata fields.
- Updated review validation, operating system, and ADM specification docs for commit-bound review sets.

## [v0.10] — 2026-07-08

### Review Gate Modes

- Added `docs/decisions/ADR-20260708-review-validation-modes.md` to define explicit ADM review validation modes.
- Extended `scripts/validate_reviews.py` with `--mode advisory`, `--mode existing-strict`, and `--mode complete-set`.
- Kept `--advisory` as a backward-compatible alias for `--mode advisory`.
- Updated `.github/workflows/adm-quality-gate.yml` to select the review validation mode by branch context and manual workflow input.
- Updated review validation, operating system, and ADM specification docs to describe the three-stage gate model.
