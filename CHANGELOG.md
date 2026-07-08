# Changelog

## [v0.14] — 2026-07-08

### Release Baseline Hardening

- Added optional `target_ref` input to the `workflow_dispatch` trigger in `.github/workflows/adm-quality-gate.yml` for explicit release-grade validation.
- Added `docs/RELEASE_RUNBOOK.md` to define the manual release validation process, parameter mapping, and tagging rules.
- Added `docs/decisions/ADR-20260708-release-baseline-validation.md` documenting the explicit target reference support for releases.
- Synchronized `docs/REPOSITORY_GOVERNANCE.md` and `docs/REVIEW_RUNBOOK.md` with the new release runbook and explicit `target_ref` logic.
- Created a complete six-role ADM review set for the v0.14 baseline hardening.

## [v0.13] — 2026-07-08

### Repository Governance and Release Gate Policy

- Added `docs/REPOSITORY_GOVERNANCE.md` to document the required `main-protection` ruleset, default-branch target, empty bypass list, pull-request-only merge path, required `ADM Quality Gate` status check, force-push block, and deletion restriction.
- Added `docs/decisions/ADR-20260708-main-protection-ruleset.md` to record the accepted branch protection decision.
- Aligned the GitHub Actions job display name with the required `ADM Quality Gate` status check expected by the repository ruleset.
- Documented the release gate distinction between the normal PR gate and release-grade complete-set validation.
- Linked repository governance from `README.md`.
- Updated `docs/REVIEW_RUNBOOK.md` with the repository settings precondition for merge readiness.

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

## [v0.9] — 2026-07-08

### Advisory Review Validation

- Added `scripts/validate_reviews.py` for dependency-free frontmatter validation of completed review artifacts under `.ai/reviews/`.
- Updated all review templates with runtime frontmatter fields required by the validator.
- Added an advisory GitHub Actions step for review validation without making review completeness a hard merge gate.
- Added `docs/REVIEW_VALIDATION.md` and updated `docs/OPERATING_SYSTEM.md` with the validation workflow.
- Updated `spec/ADM_v1_DRAFT.md` to document advisory review validation.

## [v0.8] — 2026-07-08

### Review Template Governance

- Added reusable review templates under `templates/reviews/` for Architect, Security, Performance, Cost, Simplifier, and Documentation reviews.
- Added `templates/reviews/README.md` to document the separation between reusable templates and runtime review artifacts.
- Updated `docs/OPERATING_SYSTEM.md` to specify that templates live in `templates/reviews/` and completed reviews live in `.ai/reviews/`.
- Updated `spec/ADM_v1_DRAFT.md` to document review template governance and CI-readiness expectations.

## [v0.7] — 2026-07-07

### PR-Ready Agent Protocol

- Updated `prompts/master_prompt.md` with a strict PR-ready quality-gate protocol.
- Agents must run `scripts/check_limits.py` without proposed-exemption tolerance before marking work merge-ready.
- Handover output must now state CI-readiness status.

## [v0.6] — 2026-07-07

### Branch-Aware Local DX

- Added `scripts/bootstrap.sh` to initialize the local `.ai/` workspace structure and install a local pre-commit hook.
- Improved `scripts/check_limits.py` with an explicit `--allow-proposed-exemptions` mode for local feature work.
- Kept CI merge-readiness strict: accepted exemptions require ACCEPTED or APPROVED Decision Records.
- Updated the ADM specification to document local proposed exemptions, bootstrap behavior, and the strict CI distinction.

## [v0.5] — 2026-07-07

### ADR Exemptions and Agent Onboarding

- Upgraded `scripts/check_limits.py` with accepted Decision Record exemption parsing.
- Added machine-readable ADM exemption section to `templates/ADR_TEMPLATE.md`.
- Added `prompts/master_prompt.md` for model-neutral CLI-agent onboarding.

## [v0.4] — 2026-07-07

### CI Quality Gate MVP

- Added GitHub Actions workflow `.github/workflows/adm-quality-gate.yml`.
- The workflow runs on `push`, `pull_request`, and manual `workflow_dispatch`.
- The workflow executes `scripts/check_limits.py --path . --max-lines 300`.
- The ADM specification now documents the automated CI Quality Gate and clarifies that ADR-based technical exception validation is not implemented yet.

## [v0.3] — 2026-07-07

### Operational Templates and Checks

- Added ADR template for structured architecture decisions.
- Added session handover template for metric-based agent handoffs.
- Added source file line-limit validator script.

## [v0.2] — 2026-07-07

### Quality Hardening

- Added default performance budgets to the SaaS Foundation Blueprint.
- Added Data Lifecycle requirements: Upload or Import, Processing, Archive, Delete, Backup, Restore.
- Expanded Cost Engineering from usage counting to cost aggregation per user, workspace, tenant, feature, request, worker time, and model call.
- Added KI-specific threat modeling topics: Prompt Injection, Token Leakage, Cost Explosion, API misuse, Tenant Escape, and sensitive-data leakage.
- Added hard AI-Coding-Friendliness rules to the Constitution, including the 300-line source file limit and exception process.
- Added stricter Definition of Done and Quality Gates to the ADM specification.
- Expanded the Operating System handover protocol with metrics, budget violations, risks, and next-step requirements.

## [v0.1] — 2026-07-07

### Initial Draft

- Repository foundation started.
- README replaced with v0.1 draft overview.
- Vision document expanded.
- Constitution document expanded.
- Operating system document added.
- Multi-Agent Parliament document added.
- SaaS Foundation Blueprint added.
- ADM v1 draft specification added.
- Legacy specification file converted to pointer.
