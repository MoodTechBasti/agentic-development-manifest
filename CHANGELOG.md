# Changelog

## [v0.32] — 2026-07-08

### v1 Release Candidate Criteria

- Added `docs/decisions/ADR-20260708-v1-release-candidate-criteria.md` to accept Roadmap Phase 9 as the v1 Release Candidate Criteria baseline.
- Defined the evidence required before a future v1 release candidate can be tagged.
- Clarified that v1-RC readiness requires synchronized README, ROADMAP, CHANGELOG, specification, ADRs, governance documents, complete six-role review evidence, release-grade `complete-set` validation, and manual GitHub ruleset audit evidence where release-relevant.
- Clarified that a v1-RC review set must be fresh, explicitly scoped, and bound to the stable reviewed content commit.
- Clarified the active `.ai/reviews/` evidence boundary for a future v1-RC gate without moving or archiving review files in v0.32.
- Kept v0.32 intentionally narrow: no v1-RC claim, v1 tag, v1-RC tag, workflow change, release automation, new validator mode, recursive archive validation, review index generation, runtime code, provider SDK integration, MCP integration, adapter expansion, Handover linting, branch-protection change, or review archive migration.

## [v0.31] — 2026-07-08

### Foundation Hygiene Cleanup

- Added `docs/decisions/ADR-20260708-foundation-hygiene-cleanup.md` to accept v0.31 as a pre-Phase-9 foundation hygiene cleanup.
- Finalized stale review-evidence wording in the accepted v0.29 and v0.30 ADRs after their review sets and release tags already existed.
- Clarified `docs/RELEASE_RUNBOOK.md` so local terminal validation, GitHub PR quality gates, manual `workflow_dispatch` release-grade validation, and manual ruleset audits are recorded as distinct evidence paths.
- Strengthened `.github/pull_request_template.md` to require explicit validation evidence instead of mixing local and GitHub workflow claims.
- Improved `scripts/validate_reviews.py` complete-set output clarity without changing validator semantics, archive behavior, required roles, or scope binding.
- Added fixture coverage for the new complete-set scope-filtering message.
- Kept v0.31 intentionally narrow: no Roadmap Phase 9 implementation, v1 release-candidate claim, workflow change, release automation, new validator mode, recursive archive validation, review index generation, runtime code, provider SDK integration, MCP integration, adapter expansion, Handover linting, or branch-protection change.

## [v0.30] — 2026-07-08

### Review Archive Migration Batch 2

- Added `docs/decisions/ADR-20260708-review-archive-migration-batch-2.md` to accept v0.30 as Review Archive Migration Batch 2.
- Moved completed v0.26, v0.27, and v0.28 review sets from direct `.ai/reviews/*.md` files into `.ai/reviews/archive/<review_set_id>/`.
- Kept the v0.29 Tool Verification Discovery Baseline review set directly under `.ai/reviews/` as current active release evidence.
- Preserved original review file contents and metadata; no historical `review_set_id`, `target_ref`, `target_commit`, review vote, `review_status`, or `ci_ready` value is retargeted.
- Kept v0.30 intentionally narrow: no production validator logic change, workflow change, release automation, review index generation, Roadmap Phase 9 implementation, v1 release-candidate claim, runtime code, provider SDK integration, MCP integration, adapter expansion, Handover linting, or branch-protection change.

## [v0.29] — 2026-07-08

### Roadmap Phase 8 Tool Verification Discovery Baseline

- Added `docs/decisions/ADR-20260708-tool-verification-discovery-baseline.md` to accept Roadmap Phase 8 as a Tool Verification Discovery Baseline.
- Added `docs/TOOL_VERIFICATION.md` to define the discovery and governance evidence required before deferred or future adapter prompts can be proposed.
- Kept Gemini CLI and Antigravity CLI deferred; v0.29 accepts no new adapter prompts.
- Synchronized `ROADMAP.md`, `README.md`, `spec/ADM_v1_DRAFT.md`, `docs/OPERATING_SYSTEM.md`, `docs/ADAPTER_PROMPT_STANDARD.md`, `docs/MASTER_PROMPT_STANDARD.md`, `prompts/master_prompt.md`, and `prompts/adapters/README.md` for Tool Verification semantics.
- Kept v0.29 intentionally narrow: no Gemini CLI adapter, Antigravity CLI adapter, runtime code, provider SDK integration, MCP integration, local tool profile, workflow change, validator change, release automation, Handover linter, branch-protection change, Review Archive Migration, Phase 9 implementation, or v1 release-candidate claim.

## [v0.28] — 2026-07-08

### Roadmap Phase 7 Session Continuity Baseline

- Added `docs/decisions/ADR-20260708-session-continuity-baseline.md` to accept Roadmap Phase 7 as the Session Continuity Baseline.
- Added `.ai/handover/README.md` to define durable handover discovery, metadata, continuity status, evidence, and commit policy.
- Hardened `templates/HANDOVER_TEMPLATE.md` with continuity status, target ref, target commit, review set ID, and latest repository evidence fields.
- Synchronized `.ai/README.md`, `docs/OPERATING_SYSTEM.md`, `spec/ADM_v1_DRAFT.md`, `prompts/master_prompt.md`, `README.md`, and `ROADMAP.md` for repository-owned Session Continuity semantics.
- Kept v0.28 intentionally narrow: no runtime code, real automation, Handover linter, new validator mode, workflow change, release automation, provider SDK integration, MCP integration, local tool profile, Gemini CLI adapter, Antigravity CLI adapter, branch-protection change, review archive migration, Phase 8 work, or v1 release-candidate claim.

## [v0.27] — 2026-07-08

### Review Archive Migration Batch 1

- Added `docs/decisions/ADR-20260708-review-archive-migration-batch-1.md` to accept v0.27 as Review Archive Migration Batch 1.
- Moved completed historical review sets up to v0.25 from direct `.ai/reviews/*.md` files into `.ai/reviews/archive/<review_set_id>/`.
- Kept the v0.26 Review Archive Policy review set directly under `.ai/reviews/` as current active release evidence.
- Preserved original review file contents and metadata; no historical `review_set_id`, `target_ref`, `target_commit`, review vote, `review_status`, or `ci_ready` value is retargeted.
- Kept v0.27 intentionally narrow: no production validator logic change, workflow hardening, release automation, review index generation, Roadmap Phase 7 implementation, runtime code, provider SDK integration, MCP integration, Gemini CLI adapter, Antigravity CLI adapter, branch-protection change, or v1 release-candidate claim.

## [v0.26] — 2026-07-08

### Review Archive Policy

- Added `docs/decisions/ADR-20260708-review-archive-policy.md` to accept v0.26 as the Review Archive Policy baseline.
- Documented `.ai/reviews/archive/<review_set_id>/` as the future historical review-set archive path.
- Clarified that direct `.ai/reviews/*.md` files remain the active review validation area.
- Updated `.ai/README.md`, `docs/REVIEW_VALIDATION.md`, `docs/REVIEW_RUNBOOK.md`, `README.md`, and `ROADMAP.md` for archive-policy semantics.
- Added targeted fixture coverage in `scripts/test_validate_reviews.py` proving archive subdirectories are ignored by the standard validator path.
- Kept v0.26 intentionally narrow: no historical review migration, production validator logic change, workflow hardening, release automation, review index generation, Roadmap Phase 7 implementation, runtime code, provider SDK integration, MCP integration, Gemini CLI adapter, Antigravity CLI adapter, branch-protection change, or v1 release-candidate claim.

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
- Added canonical AI vocabulary for provider abstraction, model capabilities, prompt registry, tool registry, evaluation, AI cost tracking, routing, fallback, caching, safety rules, observability, audit, and AI artifact lifecycle.
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
- Defined which handover concepts may become machine-checkable, including session identity, agent role, changed files, checks, review status, and next steps.
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

### Review Validation Modes

- Added `docs/REVIEW_VALIDATION.md` to document ADM review validation behavior, modes, and metadata requirements.
- Extended `scripts/validate_reviews.py` with explicit `advisory`, `existing-strict`, and `complete-set` modes.
- Preserved backward-compatible `--advisory` and `--strict` flags.
- Updated `ADM Quality Gate` so feature branches use advisory validation, normal protected-branch paths use existing-strict validation, and release branches use complete-set validation.
- Added `docs/decisions/ADR-20260708-review-validation-modes.md`.

## [v0.9] — 2026-07-08

### ADR Review Metadata

- Added machine-readable metadata to all review templates:
  - `review_id`
  - `review_set_id`
  - `target_commit`
  - `review_status`
  - `ci_ready`
  - optional `confidence_score`
- Added `scripts/validate_reviews.py` to validate completed `.ai/reviews/*.md` frontmatter.
- Added `.ai/reviews/.gitkeep` so completed review output has a stable runtime target.
- Updated `docs/MULTI_AGENT_PARLIAMENT.md` and `prompts/master_prompt.md` to require completed review artifacts.
- Added `docs/decisions/ADR-20260708-review-metadata.md`.

## [v0.8] — 2026-07-08

### Review Template Standard

- Added six reusable review templates under `templates/reviews/`:
  - Architect
  - Security
  - Performance
  - Cost
  - Simplifier
  - Documentation
- Added `templates/reviews/README.md` to document template usage, runtime output location, and CI-readiness semantics.
- Added `docs/decisions/ADR-20260708-review-template-standard.md`.
- Updated `docs/MULTI_AGENT_PARLIAMENT.md`, `spec/ADM_v1_DRAFT.md`, and `prompts/master_prompt.md` to reference the review template standard.

## [v0.7] — 2026-07-08

### Governance and Release Hygiene

- Added `docs/decisions/ADR-20260708-governance-release-hygiene.md`.
- Added `scripts/check_limits.py` to enforce the 300-line file limit while excluding transient, vendor, and VCS directories.
- Added `.github/workflows/adm-quality-gate.yml` to run the line-limit check on pull requests and pushes.
- Updated `docs/OPERATING_SYSTEM.md`, `docs/CONSTITUTION.md`, `spec/ADM_v1_DRAFT.md`, `README.md`, and `prompts/master_prompt.md` with governance and release hygiene requirements.

## [v0.6] — 2026-07-08

### Master Prompt v0.1

- Added `prompts/master_prompt.md`, the first CLI-first model-neutral ADM master prompt.
- Added `docs/decisions/ADR-20260708-master-prompt-v0.md`.
- Updated `README.md` and `spec/ADM_v1_DRAFT.md`.

## [v0.5] — 2026-07-08

### ACP + Spezifikation v0.1

- Added `spec/ADM_v1_DRAFT.md` and `docs/ACP.md`.
- Added `docs/decisions/ADR-20260708-spec-and-acp.md`.
- Updated `README.md`.

## [v0.4] — 2026-07-08

### Decision Records

- Added `templates/ADR_TEMPLATE.md`.
- Added `docs/decisions/ADR-20260708-adopt-adr-process.md`.
- Updated `docs/OPERATING_SYSTEM.md` and `README.md` with ADR policy.

## [v0.3] — 2026-07-08

### Initial Documentation

- Added `docs/VISION.md`.
- Added `docs/CONSTITUTION.md`.
- Added `docs/OPERATING_SYSTEM.md`.
- Added `docs/MULTI_AGENT_PARLIAMENT.md`.
- Added `.ai/README.md`.

## [v0.2] — 2026-07-08

### Repository Foundation

- Added `.ai/`, `docs/`, `spec/`, and `templates/` structure.
- Added `.gitkeep` placeholders for initial ADM repository folders.

## [v0.1] — 2026-07-08

### Initial Baseline

- Added initial README and repository purpose.
