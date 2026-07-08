# Changelog

## [v0.25] — 2026-07-08

### Foundation Consistency and Release Hygiene Baseline

- Added `docs/decisions/ADR-20260708-foundation-consistency-release-hygiene-baseline.md` to accept v0.25 as a consolidation baseline after v0.24.
- Synchronized version and status language across canonical ADM documents while preserving the origin version of earlier standards.
- Updated `docs/RELEASE_RUNBOOK.md` to replace the old v0.13-centered example with generic release inputs and final tag semantics.
- Clarified that governance-relevant releases require a manual external GitHub ruleset audit; source files alone do not prove active repository settings.
- Updated `docs/REPOSITORY_GOVERNANCE.md`, `docs/REVIEW_RUNBOOK.md`, `docs/OPERATING_SYSTEM.md`, foundation standards, prompt standards, adapter README, `spec/ADM_v1_DRAFT.md`, `README.md`, and `ROADMAP.md` for the v0.25 baseline.
- Kept v0.25 intentionally narrow: no Roadmap Phase 7 implementation, Handover linter, Handover Automation expansion, workflow hardening, release automation, runtime code, provider SDK integration, MCP integration, local tool profile, Gemini CLI adapter, Antigravity CLI adapter, branch-protection change, or v1 release-candidate claim.

## [v0.24] — 2026-07-08

### Review and Validation Hardening Baseline

- Added `docs/decisions/ADR-20260708-review-validation-hardening-baseline.md` to accept Roadmap Phase 6 as a controlled review and validation hardening baseline.
- Promoted the already implemented review validation mode and review-set scoping ADRs from stale `PROPOSED` status to accepted repository truth.
- Updated `docs/REVIEW_VALIDATION.md` and `docs/REVIEW_RUNBOOK.md` to document the v0.24 baseline guardrails, stale-review protection, and normal PR versus release-grade validation boundaries.
- Hardened `scripts/test_validate_reviews.py` with targeted scope-filtering regression coverage for review set IDs, target refs, and stale complete review sets.
- Marked Roadmap Phase 6 baseline work complete in `ROADMAP.md` and synchronized `spec/ADM_v1_DRAFT.md` and `README.md`.
- Kept v0.24 intentionally narrow: no workflow hardening, release automation, runtime code, provider SDK integration, MCP integration, local tool profile, Gemini CLI adapter, Antigravity CLI adapter, or provider secrets.

## [v0.23] — 2026-07-08

### Roadmap Continuation and v1 Readiness Plan

- Added Roadmap Phase 6 through Roadmap Phase 9 to `ROADMAP.md` as planned future blocks after Roadmap Phase 5.
- Added v1 Readiness Criteria to define the evidence required before ADM can be considered v1-ready.
- Added `docs/decisions/ADR-20260708-roadmap-continuation-v1-readiness.md` to record the accepted roadmap continuation and v1 readiness architecture decision.
- Clarified that Roadmap Phase 6 and later remain distinct from ADM lifecycle phases in `spec/ADM_v1_DRAFT.md`.
- Synchronized `spec/ADM_v1_DRAFT.md`, `README.md`, `ROADMAP.md`, and `CHANGELOG.md`.
- Kept v0.23 documentation-only: no validator change, workflow change, runtime code, provider SDK integration, MCP integration, local tool profile, release automation, Gemini CLI adapter, Antigravity CLI adapter, or provider secrets.

## [v0.22] — 2026-07-08

### Adapter Prompt Standard

- Added `docs/ADAPTER_PROMPT_STANDARD.md` as the Roadmap Phase 5 Adapter Prompt Standard.
- Added canonical Adapter vocabulary for adapter prompts, canonical prompt dependency, adapter boundaries, tool capabilities, and tool state.
- Added `docs/decisions/ADR-20260708-adapter-prompt-standard.md` to record the accepted Roadmap Phase 5 architecture decision.
- Added initial adapter prompts under `prompts/adapters/` for Claude Code CLI, Codex CLI, and Generic CLI Agent.
- Deferred Gemini CLI and Antigravity CLI adapters until their current tool behavior is explicitly verified.
- Synchronized `spec/ADM_v1_DRAFT.md`, `docs/OPERATING_SYSTEM.md`, `docs/MASTER_PROMPT_STANDARD.md`, `prompts/master_prompt.md`, `README.md`, and `ROADMAP.md`.
- Kept v0.22 documentation-only: no runtime code, provider SDK integration, real tool integration, local tool profile, MCP integration, schema, validator change, workflow change, release automation, release tag, Gemini CLI adapter, Antigravity CLI adapter, or provider secrets.

## [v0.21] — 2026-07-08

### Master Prompt Standard

- Added `docs/MASTER_PROMPT_STANDARD.md` as the Roadmap Phase 4 Master Prompt Standard.
- Added canonical Master Prompt vocabulary for authority order, agent onboarding, scope declaration, quality gate contract, handover contract, foundation triggers, and adapter prompt boundaries.
- Added `docs/decisions/ADR-20260708-master-prompt-standard.md` to record the accepted Roadmap Phase 4 architecture decision.
- Hardened `prompts/master_prompt.md` with explicit authority order, Roadmap Phase 4 context, scope rules, Master Prompt rules, proportional ADR guidance, and adapter-scope boundaries.
- Clarified that Roadmap Phase 4 Master Prompt is distinct from Lifecycle Phase 4 — Simplification.
- Synchronized `spec/ADM_v1_DRAFT.md`, `docs/OPERATING_SYSTEM.md`, `README.md`, and `ROADMAP.md`.
- Kept v0.21 documentation-only: no runtime code, provider SDK integration, tool integration, CLI-specific adapter prompt, local tool profile, MCP integration, schema, validator change, workflow change, release automation, or release tag.

## [v0.20] — 2026-07-08

### AI Foundation Standard

- Added `docs/AI_FOUNDATION_STANDARD.md` as the Roadmap Phase 3 AI Foundation Standard.
- Added canonical AI vocabulary for provider abstraction, model capabilities, prompt registry, prompt versions, tool registry, evaluation, routing, fallback, caching, safety rules, AI cost tracking, observability, audit, and AI artifact lifecycle.
- Added `docs/decisions/ADR-20260708-ai-foundation-standard.md` to record the accepted Roadmap Phase 3 architecture decision.
- Clarified that Roadmap Phase 3 builds on Roadmap Phase 2 SaaS Foundation Standard instead of replacing user, tenant, permission, billing, quota, job, observability, or data-lifecycle boundaries.
- Synchronized `spec/ADM_v1_DRAFT.md`, `docs/OPERATING_SYSTEM.md`, `docs/SAAS_FOUNDATION_BLUEPRINT.md`, `prompts/master_prompt.md`, `README.md`, and `ROADMAP.md`.
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
- Documented safety boundaries: automation may prefill, lint, and cross-check handovers, but must not invent checks, commits, CI results, review votes, or approvals.
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
