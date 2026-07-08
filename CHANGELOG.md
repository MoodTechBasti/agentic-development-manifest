# Changelog

## [v0.20] — 2026-07-08

### AI Foundation Standard

- Added `docs/AI_FOUNDATION_STANDARD.md` as the Roadmap Phase 3 AI Foundation Standard.
- Added canonical AI vocabulary for provider abstraction, model capabilities, prompt registry, prompt versions, tool registry, evaluation, routing, fallback, caching, safety rules, AI cost tracking, observability, audit, and AI artifact lifecycle.
- Added `docs/decisions/ADR-20260708-ai-foundation-standard.md` to record the accepted Roadmap Phase 3 architecture decision.
- Clarified that Roadmap Phase 3 builds on Roadmap Phase 2 SaaS Foundation Standard instead of replacing user, tenant, permission, billing, quota, job, observability, or data-lifecycle boundaries.
- Synchronized `spec/ADM_v1_DRAFT.md`, `docs/OPERATING_SYSTEM.md`, `prompts/master_prompt.md`, `README.md`, and `ROADMAP.md`.
- Kept v0.20 documentation-only: no validator changes, workflow changes, schemas, runtime code, provider SDK integrations, prompt execution, tool execution, real model calls, or provider secrets.

## [v0.19] — 2026-07-08

### SaaS Foundation Standard

- Promoted `docs/SAAS_FOUNDATION_BLUEPRINT.md` from early blueprint to Roadmap Phase 2 SaaS Foundation Standard.
- Added canonical SaaS vocabulary for users, organizations, tenants, workspaces, memberships, roles, permissions, entitlements, quotas, jobs, workers, observability, admin diagnostics, and data lifecycle.
- Added `docs/decisions/ADR-20260708-saas-foundation-standard.md` to record the accepted Roadmap Phase 2 architecture decision.
- Clarified that Roadmap Phase 2 is distinct from Lifecycle Phase 2 — Architecture Competition in `spec/ADM_v1_DRAFT.md`.
- Synchronized `spec/ADM_v1_DRAFT.md`, `docs/OPERATING_SYSTEM.md`, `prompts/master_prompt.md`, `README.md`, and `ROADMAP.md`.
- Kept v0.19 documentation-only: no validator changes, workflow changes, schemas, runtime code, provider integrations, or real SaaS implementation.

## [v0.18] — 2026-07-08

### Handover Automation Architecture

- Added `docs/decisions/ADR-20260708-handover-automation.md` to define structured, repository-owned handover automation semantics.
- Defined which handover concepts may become machine-checkable, including session identity, agent role, changed files, checks, review status, risks, and next steps.
- Documented safety boundaries: automation may prefill, lint, and cross-check handovers, but must not invent checks, commits, CI results, review votes, roles, or approvals.
- Connected Handover Automation to Project-owned Memory and Agent Registry without adding validators, workflow changes, schemas, or real automation.
- Updated `templates/HANDOVER_TEMPLATE.md`, `docs/OPERATING_SYSTEM.md`, `spec/ADM_v1_DRAFT.md`, `prompts/master_prompt.md`, `README.md`, and `ROADMAP.md`.

## [v0.17] — 2026-07-08

### Agent Registry Architecture

- Added `docs/decisions/ADR-20260708-agent-registry.md` to define repository-owned agent roles, responsibility boundaries, initialization expectations, and handover routing.
- Added `.ai/agents/README.md` as the runtime policy for Agent Registry artifacts.
- Updated `spec/ADM_v1_DRAFT.md` with Agent Registry authority, role fields, and boundary rules.
- Updated `docs/OPERATING_SYSTEM.md` with Agent Registry purpose, required fields, and governance boundaries.
- Extended `.ai/README.md` to include `.ai/agents/` as versioned coordination metadata.
- Updated `prompts/master_prompt.md` so agents check the Agent Registry during initialization.
- Updated `README.md` and `ROADMAP.md` to reflect the v0.17 draft focus.

## [v0.16] — 2026-07-08

### Project-owned Memory Architecture

- Added `docs/decisions/ADR-20260708-project-owned-memory.md` to define repository-owned memory as an auditable, portable, model-neutral project layer.
- Updated `spec/ADM_v1_DRAFT.md` with project-owned memory authority, storage classes, and runtime artifact policy.
- Updated `docs/OPERATING_SYSTEM.md` with memory authority order, commit rules, and memory-file requirements.
- Extended `.ai/README.md` to clarify durable memory, knowledge, task, and decision artifact policies.
- Updated `prompts/master_prompt.md` so agents check curated `.ai/memory/` and `.ai/knowledge/` during initialization.
- Updated `README.md` and `ROADMAP.md` to reflect the v0.16 draft focus.

## [v0.15] — 2026-07-08

### Specification and Agent Compliance Alignment

- Canonically restructured `spec/ADM_v1_DRAFT.md` into a logical "canonical structured ADM specification" covering governance, release policy, and PR hygiene.
- Hardened `prompts/master_prompt.md` with mandatory validation scripts (`validate_reviews.py`), PR hygiene rules, and new documentation reading requirements.
- Synced `ROADMAP.md` by marking governance/release hardening as completed and refocusing Phase 1 on project-owned memory.
- Enforced strict PR hygiene: no placeholders, no empty fields, and verified checkboxes.
- Created a complete six-role ADM review set for the v0.15 specification alignment.

## [v0.14] — 2026-07-08

### Release Baseline Hardening

- Added optional `target_ref` input to the `workflow_dispatch` trigger in `.github/workflows/adm-quality-gate.yml` for explicit release-grade validation.
- Added `docs/RELEASE_RUNBOOK.md` to define the manual release validation process, parameter mapping, and tagging rules.
- Added `docs/decisions/ADR-20260708-release-baseline-validation.md` documenting the explicit target reference support for releases.
- Synchronized `docs/REPOSITORY_GOVERNANCE.md` and `docs/REVIEW_RUNBOOK.md` with the new release runbook and explicit `target_ref` logic.
- Created a complete six-role ADM review set for the v0.14 baseline hardening.

## [v0.13] — 2026-07-08

### Repository Governance and Release Gate Policy

- Added `docs/REPOSITORY_GOVERNANCE.md` documenting branch protection, PR-only merge flow, required reviews, required checks, and tag/release expectations.
- Added `.github/pull_request_template.md` with an ADM compliance checklist.
- Added `docs/REVIEW_RUNBOOK.md` describing how to run and evaluate multi-role reviews.
- Added `docs/REVIEW_VALIDATION.md` and `scripts/validate_reviews.py` to validate review frontmatter and structure.
- Added `scripts/test_validate_reviews.py` covering validator behavior.
- Added GitHub Actions workflow `.github/workflows/adm-quality-gate.yml` for line-limit and review validation.
- Added `.ai/reviews/README.md` as the runtime review artifact policy.
- Added `templates/reviews/*.md` accepted review templates for architect, security, performance, cost, simplifier, and documentation roles.
- Added a complete six-role review set for the repository governance baseline.
- Synchronized `spec/ADM_v1_DRAFT.md`, `prompts/master_prompt.md`, `README.md`, and `ROADMAP.md` with governance and release expectations.

## [v0.1] — Initial seed

- Repository initialized.
- Vision document added.
- Constitution added.
- First handover context added.
- Multi-Agent Parliament document added.
- SaaS Foundation Blueprint added.
- ADM v1 draft specification added.
- Legacy specification file converted to pointer.
