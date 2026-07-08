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

## Roadmap Phase 7: Handover and Session Continuity

- [ ] Define reliable session-continuity behavior for future agents using repository-owned evidence.
- [ ] Evaluate handover linting, prefill, and cross-checking without turning automation into approval truth.
- [ ] Keep chat history, hidden model memory, local profiles, scratch files, and raw logs non-authoritative.

## Roadmap Phase 8: Adapter Expansion and Tool Verification

- [ ] Verify current tool behavior before accepting any additional tool-specific adapter.
- [ ] Keep Gemini CLI and Antigravity CLI deferred until explicitly verified and approved.
- [ ] Keep adapters thin, downstream from `prompts/master_prompt.md`, and free from runtime or provider lock-in.

## Roadmap Phase 9: v1 Release Candidate Criteria

- [ ] Define the exact evidence required for a v1 release candidate.
- [ ] Require synchronized specification, roadmap, changelog, ADRs, and review artifacts for v1 readiness.
- [ ] Require release-grade complete-set validation before tagging a v1 release candidate.

## v1 Readiness Criteria

ADM may be considered v1-ready only when the accepted standards, governance evidence, roadmap scope, review evidence, and release process are synchronized as one coherent repository state.

Minimum criteria:

- Roadmap Phase 0 through Roadmap Phase 5 are accepted and reflected in the specification.
- Roadmap Phase 6 through Roadmap Phase 9 are documented with explicit scope and non-scope.
- Roadmap phases remain distinct from ADM lifecycle phases.
- Governance, review validation, release validation, project-owned memory, agent registry, handover automation, SaaS Foundation, AI Foundation, Master Prompt Standard, Adapter Prompt Standard, Roadmap Continuation, Review and Validation Hardening, and Foundation Consistency and Release Hygiene have accepted ADR coverage.
- Deferred adapters are not treated as implemented or accepted without current tool-behavior verification.
- v1 release candidates have a complete six-role review set and manual release-grade `complete-set` validation.
- Governance-relevant v1 release candidates include manual GitHub ruleset audit evidence.
- v1 does not require runtime code, provider SDKs, MCP integration, local tool profiles, workflow changes, additional validator hardening, or release automation unless those are accepted by later explicit roadmap phases and ADRs.
