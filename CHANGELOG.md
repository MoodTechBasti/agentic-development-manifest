# Changelog

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
