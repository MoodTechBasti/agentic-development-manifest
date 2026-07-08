# Roadmap

Roadmap phases describe the ADM standard roadmap. They are distinct from the ADM lifecycle phases in `spec/ADM_v1_DRAFT.md`.

## Roadmap Phase 0: Repository Foundation

- Define vision.
- Define constitution.
- Capture initial handover.
- Create first draft specification.
- Create first master prompt draft.

## Roadmap Phase 1: Agentic Operating System

- [x] Define decision records.
- [x] Define research and review protocols.
- [x] Define repository governance and release hardening.
- [x] Define project-owned memory.
- [x] Define agent registry.
- [x] Define handover automation.

## Roadmap Phase 2: SaaS Foundation Standard

- [x] Define users, organizations, tenants, workspaces, memberships, roles, permissions, billing readiness, entitlements, quotas, usage and cost tracking, jobs, workers, observability, audit logs, admin diagnostics, data lifecycle, developer experience, testing, and performance budgets.

## Roadmap Phase 3: AI Foundation Standard

- [x] Define provider abstraction, prompt registry, tool registry, evaluation, AI cost tracking, routing, fallback, caching, safety rules, observability, audit, AI artifact lifecycle, and the boundary to the SaaS Foundation Standard.

## Roadmap Phase 4: Master Prompt

- [x] Convert the specification into a model-neutral CLI-agent master prompt.
- [x] Define Master Prompt Standard authority order, initialization contract, scope declaration, quality gate contract, review contract, foundation triggers, handover contract, and adapter boundary.

## Roadmap Phase 5: Adapters

- [x] Define Adapter Prompt Standard as a thin tool-specific layer below the canonical Master Prompt Standard.
- [x] Add initial adapter prompts for Claude Code CLI, Codex CLI, and Generic CLI Agent.
- [x] Defer Gemini CLI and Antigravity CLI adapters until their current tool behavior is explicitly verified.

## Roadmap Phase 6: Review and Validation Hardening

- [x] Accept the current review validation modes as the Roadmap Phase 6 baseline.
- [x] Normalize review validation mode and review-set scoping ADR status to match implemented repository behavior.
- [x] Add targeted fixture coverage for review-set filtering, target-ref filtering, and stale-review protection.
- [x] Preserve the advisory, existing-strict, and complete-set distinction without adding workflow hardening or release automation.

## Foundation Consistency and Release Hygiene Baseline (v0.25)

This is a consolidation baseline after Roadmap Phase 6. It is not Roadmap Phase 7.

- [x] Accept v0.25 as a foundation consistency and release hygiene baseline.
- [x] Synchronize status and version language across canonical ADM documents without pretending older standards were newly created in v0.25.
- [x] Modernize `docs/RELEASE_RUNBOOK.md` with generic release examples and final tag semantics.
- [x] Clarify manual GitHub ruleset audit expectations before governance-relevant releases.
- [x] Preserve Roadmap Phase 7 as open and unimplemented.
- [x] Avoid new runtime code, workflow hardening, release automation, provider SDKs, MCP integration, adapter expansion, branch-protection changes, and v1 release-candidate claims.

## Review Archive Policy Baseline (v0.26)

This is a review-storage hygiene baseline after v0.25. It is not Roadmap Phase 7.

- [x] Accept v0.26 as the Review Archive Policy baseline.
- [x] Define `.ai/reviews/archive/<review_set_id>/` as the future location for historical review sets after their release or governance purpose is complete.
- [x] Preserve direct `.ai/reviews/*.md` files as the active review validation area.
- [x] Add targeted fixture coverage proving archived review subdirectories are ignored by the standard validator path.
- [x] Defer historical review migration until a later explicit PR.
- [x] Avoid validator production logic changes, workflow changes, release automation, review index generation, runtime code, provider SDKs, MCP integration, adapter expansion, branch-protection changes, and v1 release-candidate claims.

## Review Archive Migration Batch 1 (v0.27)

This is an operational review-storage hygiene baseline after v0.26. It is not Roadmap Phase 7.

- [x] Accept v0.27 as Review Archive Migration Batch 1.
- [x] Move completed historical review sets up to v0.25 under `.ai/reviews/archive/<review_set_id>/`.
- [x] Preserve original review file contents and metadata.
- [x] Keep the current v0.26 review set directly under `.ai/reviews/` as active release evidence.
- [x] Avoid production validator logic changes, workflow changes, release automation, review index generation, runtime code, provider SDKs, MCP integration, adapter expansion, branch-protection changes, and v1 release-candidate claims.
- [x] Preserve Roadmap Phase 7 as open and unimplemented.

## Roadmap Phase 7: Handover and Session Continuity

- [x] Accept v0.28 as the Session Continuity Baseline for Roadmap Phase 7.
- [x] Define reliable session-continuity behavior for future agents using repository-owned evidence.
- [x] Define `.ai/handover/README.md` as the durable handover discovery and commit policy.
- [x] Harden `templates/HANDOVER_TEMPLATE.md` with continuity status, target refs, target commits, review-set IDs, and latest evidence fields.
- [x] Keep chat history, hidden model memory, local profiles, scratch files, raw logs, and tool caches non-authoritative.
- [x] Evaluate handover linting, prefill, and cross-checking as future possibilities without turning automation into approval truth.
- [x] Avoid runtime code, real automation, Handover linter, workflow changes, release automation, provider SDKs, MCP integration, adapter expansion, branch-protection changes, Review Archive Migration, Phase 8 work, and v1 release-candidate claims.

## Roadmap Phase 8: Adapter Expansion and Tool Verification

- [x] Accept v0.29 as the Tool Verification Discovery Baseline for Roadmap Phase 8.
- [x] Define Tool Verification as a required discovery and governance gate before any deferred or future tool-specific adapter.
- [x] Keep Gemini CLI and Antigravity CLI deferred until explicitly verified and approved in a later adapter PR.
- [x] Keep adapters thin, downstream from `prompts/master_prompt.md`, and free from runtime or provider lock-in.
- [x] Avoid new adapters, runtime code, provider SDKs, MCP integration, local tool profiles, workflow changes, validator changes, release automation, Handover linting, branch-protection changes, Review Archive Migration, Phase 9 work, and v1 release-candidate claims in v0.29.
- [ ] Accept a future verified adapter only after current tool behavior is documented, reviewed, and explicitly approved.

## Roadmap Phase 9: v1 Release Candidate Criteria

- [ ] Define the exact evidence required for a v1 release candidate.
- [ ] Require synchronized specification, roadmap, changelog, ADRs, and review artifacts for v1 readiness.
- [ ] Require release-grade complete-set validation before tagging a v1 release candidate.

## v1 Readiness Criteria

ADM may be considered v1-ready only when the accepted standards, governance evidence, roadmap scope, review evidence, and release process are synchronized as one coherent repository state.

Minimum criteria:

- Roadmap Phase 0 through Roadmap Phase 7 are accepted and reflected in the specification.
- Roadmap Phase 8 through Roadmap Phase 9 are documented with explicit scope and non-scope.
- Roadmap phases remain distinct from ADM lifecycle phases.
- Governance, review validation, release validation, project-owned memory, agent registry, handover automation, SaaS Foundation, AI Foundation, Master Prompt Standard, Adapter Prompt Standard, Roadmap Continuation, Review and Validation Hardening, Foundation Consistency and Release Hygiene, Review Archive Policy, Review Archive Migration Batch 1, and Session Continuity Baseline have accepted ADR coverage.
- Deferred adapters are not treated as implemented or accepted without current tool-behavior verification.
- v1 release candidates have a complete six-role review set and manual release-grade `complete-set` validation.
- Governance-relevant v1 release candidates include manual GitHub ruleset audit evidence.
- v1 does not require runtime code, provider SDKs, MCP integration, local tool profiles, workflow changes, additional validator hardening, release automation, additional review archive migration, Handover linting, or adapter expansion unless those are accepted by later explicit roadmap phases and ADRs.
