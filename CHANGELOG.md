# Changelog

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
