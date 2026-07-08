# ADR-20260708-roadmap-continuation-v1-readiness

> ID: ADR-20260708-roadmap-continuation-v1-readiness
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `ROADMAP.md`, `spec/ADM_v1_DRAFT.md`, `README.md`, `CHANGELOG.md` |
| New dependencies | no |
| Security review | PASSED |
| Cost review | PASSED |
| Performance review | PASSED |

## 1. Context and Reason

ADM Roadmap Phase 5 accepted the Adapter Prompt Standard and the initial adapter prompt set.

After Phase 5, `ROADMAP.md` had no documented next roadmap block. That creates a governance risk: future work could drift into validators, adapter expansion, handover automation, runtime integration, MCP integration, provider SDKs, or release automation without first deciding the strategic path to v1.

This ADR accepts v0.23 as the Roadmap Continuation and v1 Readiness Plan. It extends the roadmap after Phase 5 and defines minimum v1-readiness evidence without implementing later mechanisms.

Roadmap phases in `ROADMAP.md` remain distinct from ADM lifecycle phases in `spec/ADM_v1_DRAFT.md`.

## 2. Decision

ADM adopts Roadmap Continuation and v1 Readiness Criteria as the canonical v0.23 planning block.

`ROADMAP.md` now documents the next planned roadmap sequence:

| Roadmap phase | Purpose |
| --- | --- |
| Roadmap Phase 6 | Review and Validation Hardening |
| Roadmap Phase 7 | Handover and Session Continuity |
| Roadmap Phase 8 | Adapter Expansion and Tool Verification |
| Roadmap Phase 9 | v1 Release Candidate Criteria |

The roadmap continuation is intentionally a plan, not implementation. Future PRs must still receive explicit maintainer approval before they implement validators, workflows, handover automation, adapter expansion, runtime, provider SDKs, MCP integration, local tool profiles, or release automation.

## 3. v1 Readiness Criteria

ADM may be considered v1-ready only when the repository state proves the following:

- Roadmap Phase 0 through Roadmap Phase 5 are accepted and reflected in the specification.
- Roadmap Phase 6 through Roadmap Phase 9 are documented with explicit scope and non-scope.
- Roadmap phases remain distinct from ADM lifecycle phases.
- Governance, review validation, release validation, project-owned memory, agent registry, handover automation, SaaS Foundation, AI Foundation, Master Prompt Standard, and Adapter Prompt Standard have accepted ADR coverage.
- Deferred adapters are not treated as implemented or accepted without current tool-behavior verification.
- A v1 release candidate has a complete six-role review set and manual release-grade `complete-set` validation.
- v1 does not require runtime code, provider SDKs, MCP integration, local tool profiles, workflow changes, validator hardening, or release automation unless those are accepted by later explicit roadmap phases and ADRs.

## 4. Scope Boundary

v0.23 is documentation, ADR, roadmap continuation, v1-readiness criteria, specification sync, README sync, changelog sync, and review artifacts only.

It does not add:

- runtime implementation,
- provider SDK integration,
- tool integration,
- local tool profiles,
- MCP integration,
- database schema,
- validator enforcement,
- workflow changes,
- handover automation implementation,
- release automation,
- release tag,
- Gemini CLI adapter,
- Antigravity CLI adapter,
- provider secrets.

## 5. Evidence

- `ROADMAP.md` previously ended at Roadmap Phase 5 after accepting Adapter Prompt Standard.
- `spec/ADM_v1_DRAFT.md` already distinguishes Roadmap phases from ADM lifecycle phases.
- Review validation already supports `advisory`, `existing-strict`, and `complete-set` modes.
- Release governance already requires complete review evidence and manual release-grade validation before tags.
- Gemini CLI and Antigravity CLI are already deferred candidates in the Adapter Prompt Standard.

## 6. Alternatives

### Alternative A: Build Review and Validation Hardening immediately

- Description: Start v0.23 by adding validators, schemas, or workflow hardening.
- Reason for rejection: That implements a mechanism before accepting the next roadmap structure.

### Alternative B: Build Handover and Session Continuity immediately

- Description: Start v0.23 by implementing handover linting, prefill, or session-continuity automation.
- Reason for rejection: Useful later, but still a mechanism. The roadmap gap must be closed first.

### Alternative C: Expand adapters immediately

- Description: Add Gemini CLI, Antigravity CLI, or more tool-specific adapters.
- Reason for rejection: Gemini CLI and Antigravity CLI remain deferred until their current tool behavior is verified.

### Alternative D: Declare v1 immediately

- Description: Treat the existing accepted standards as sufficient for v1.
- Reason for rejection: The roadmap lacked Phase 6+ and had no release-candidate criteria.

## 7. Trade-offs

### Pros

- Closes the strategic roadmap gap after Phase 5.
- Prevents accidental mechanism-first work.
- Defines a safer path to v1 without overbuilding.
- Preserves the Roadmap/Lifecycle distinction.
- Keeps deferred adapters honest.

### Cons

- Adds planning documentation without new automation.
- Requires future PRs to continue the same governance discipline.
- v1-readiness remains a criterion set, not a completed v1 release.

## 8. Risks and Consequences

- Short-term risk: Maintainers may expect v0.23 to build Phase 6 immediately.
- Long-term risk: Roadmap Phase 6 through Phase 9 can drift if later PRs ignore this ADR.
- Governance risk: Roadmap Phase 6 can be confused with Lifecycle Phase 6.
- Adapter risk: Deferred tools can be treated as accepted without verification.
- Mitigation plan: Keep v0.23 documentation-only, state non-scope explicitly, require explicit later ADRs and full review sets for phase transitions.

## 9. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.

## 10. Affected Files

- [x] `docs/decisions/ADR-20260708-roadmap-continuation-v1-readiness.md`
- [x] `ROADMAP.md`
- [x] `spec/ADM_v1_DRAFT.md`
- [x] `README.md`
- [x] `CHANGELOG.md`

## 11. Review Log

- [x] Principal Architect: APPROVED — `REV-ARCH-20260708-roadmap-continuation-v1-readiness.md`
- [x] Security Lead: APPROVED — `REV-SEC-20260708-roadmap-continuation-v1-readiness.md`
- [x] Performance Lead: APPROVED — `REV-PERF-20260708-roadmap-continuation-v1-readiness.md`
- [x] Cost Engineer: APPROVED — `REV-COST-20260708-roadmap-continuation-v1-readiness.md`
- [x] Simplifier: APPROVED — `REV-SIMP-20260708-roadmap-continuation-v1-readiness.md`
- [x] Documentation Reviewer: APPROVED — `REV-DOC-20260708-roadmap-continuation-v1-readiness.md`

## 12. Final Outcome

Accepted for v0.23 after maintainer approval and successful validation of the full review set.
