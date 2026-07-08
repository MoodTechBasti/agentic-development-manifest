# ADR-20260708-foundation-consistency-release-hygiene-baseline

> ID: ADR-20260708-foundation-consistency-release-hygiene-baseline
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `README.md`, `ROADMAP.md`, `CHANGELOG.md`, `spec/ADM_v1_DRAFT.md`, `docs/RELEASE_RUNBOOK.md`, `docs/REPOSITORY_GOVERNANCE.md`, `docs/REVIEW_RUNBOOK.md`, `docs/OPERATING_SYSTEM.md`, `docs/SAAS_FOUNDATION_BLUEPRINT.md`, `docs/AI_FOUNDATION_STANDARD.md`, `docs/MASTER_PROMPT_STANDARD.md`, `docs/ADAPTER_PROMPT_STANDARD.md`, `prompts/adapters/README.md`, `docs/decisions/ADR-20260708-stable-reviewed-code-sha.md` |
| New dependencies | no |
| Security review | PASSED |
| Cost review | PASSED |
| Performance review | PASSED |

## 1. Context and Reason

After v0.24 the repository has a coherent review-validation baseline, but several foundation documents still expose older draft markers from the releases that originally introduced them.

That is not automatically a semantic error: the SaaS, AI, Master Prompt, and Adapter standards were intentionally introduced in earlier versions. The problem is governance clarity. A reader should be able to distinguish:

1. the release where a standard was first accepted,
2. the current synchronized repository state,
3. whether a later roadmap phase has actually started.

The release runbook also still used a specific v0.13 example as the central release example. That is too easy to copy mechanically and can hide the current release rule: merge the PR, determine the stable reviewed commit, run manual complete-set validation on `main`, and only then tag the final `main` commit that includes the review artifacts.

A remaining ADR status drift also existed in `docs/decisions/ADR-20260708-stable-reviewed-code-sha.md`: the stable reviewed-code SHA mechanism had been implemented and documented since v0.11.1, but the ADR still said `PROPOSED`.

## 2. Decision

ADM accepts v0.25 as a Foundation Consistency and Release Hygiene Baseline.

v0.25 is a consolidation block. It does not start Roadmap Phase 7 and it does not implement a new mechanism.

The baseline does six things:

1. Synchronizes current version and status language across canonical ADM documents.
2. Preserves original roadmap-phase meaning for already accepted standards instead of pretending they were newly created in v0.25.
3. Modernizes release hygiene documentation with a generic release example.
4. Clarifies that GitHub ruleset checks remain manual external audits before governance-relevant releases.
5. Normalizes the stable reviewed-code SHA ADR status to accepted repository truth.
6. Records v0.25 as repository-foundation cleanup before later Roadmap Phase 7 work.

## 3. Scope Boundary

v0.25 may change documentation, ADRs, roadmap status, changelog entries, and review artifacts.

v0.25 does not add:

- Roadmap Phase 7 implementation,
- Handover linting,
- Handover prefill automation,
- release automation,
- workflow hardening,
- branch-protection changes,
- runtime code,
- MCP integration,
- provider SDKs,
- new dependencies,
- Gemini CLI adapter,
- Antigravity CLI adapter,
- v1 release candidate status.

## 4. Release Hygiene Semantics

A release tag points to the final `main` commit after the review artifacts are merged and the manual release-grade complete-set validation has passed.

The `target_commit` inside review artifacts points to the stable non-review commit that was reviewed. For v0.25 that means the documentation and ADR synchronization commit before adding the six review artifacts.

This preserves the distinction between reviewed content and the final tag commit that includes review evidence.

## 5. Repository Ruleset Audit Semantics

GitHub rulesets are external repository settings. ADM source files can document the required state, but they cannot prove the active GitHub settings by themselves.

Therefore governance-relevant releases must include a manual ruleset audit step. Documentation may require that audit, but must not claim the audit has happened unless there is separate evidence from GitHub settings or maintainer confirmation.

## 6. Alternatives

### Alternative A: Start Roadmap Phase 7 immediately

- Description: Move directly into Handover and Session Continuity.
- Reason for rejection: The foundation still had visible consistency and release-hygiene debt. Starting Phase 7 would build on a noisy base.

### Alternative B: Bump every document title to v0.25 without review

- Description: Replace every old version marker mechanically.
- Reason for rejection: That hides origin and scope. v0.25 is a synchronization baseline, not the release that originally defined all standards.

### Alternative C: Leave release runbook examples tied to v0.13

- Description: Keep the old concrete release example as the primary path.
- Reason for rejection: It invites stale copy-paste and makes the current tag semantics less obvious.

### Alternative D: Automate the release gate now

- Description: Add release automation or workflow hardening.
- Reason for rejection: That is explicitly outside the v0.25 consolidation scope and requires a separate ADR.

### Alternative E: Leave implemented stable-SHA ADR as proposed

- Description: Keep `ADR-20260708-stable-reviewed-code-sha.md` in proposed state because the mechanism already works.
- Reason for rejection: That would leave exactly the kind of governance drift v0.25 exists to remove.

## 7. Trade-offs

### Pros

- Removes visible version/status drift before additional roadmap expansion.
- Makes the release path harder to misapply.
- Keeps Phase 7 cleanly open instead of smuggling it into a hygiene release.
- Improves v1-readiness evidence without claiming v1 readiness.

### Cons

- Does not add new runtime capability.
- Does not make GitHub settings automatically auditable.
- Requires future agents to keep origin version and synchronization version distinct.

## 8. Risks and Consequences

- Risk: Future agents may treat v0.25 as a functional roadmap phase.
- Mitigation: Roadmap Phase 7 remains explicitly open and unimplemented.

- Risk: Status synchronization may look like content recertification of every older standard.
- Mitigation: Documents must preserve their original roadmap-phase identity while stating their current synchronized status.

- Risk: Ruleset audit language may be misread as proof that settings were checked.
- Mitigation: Governance documents state that the audit is manual and external unless separately evidenced.

## 9. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.

## 10. Affected Files

- [x] `docs/decisions/ADR-20260708-foundation-consistency-release-hygiene-baseline.md`
- [x] `docs/decisions/ADR-20260708-stable-reviewed-code-sha.md`
- [x] `docs/RELEASE_RUNBOOK.md`
- [x] `docs/REPOSITORY_GOVERNANCE.md`
- [x] `docs/REVIEW_RUNBOOK.md`
- [x] `docs/OPERATING_SYSTEM.md`
- [x] `docs/SAAS_FOUNDATION_BLUEPRINT.md`
- [x] `docs/AI_FOUNDATION_STANDARD.md`
- [x] `docs/MASTER_PROMPT_STANDARD.md`
- [x] `docs/ADAPTER_PROMPT_STANDARD.md`
- [x] `prompts/adapters/README.md`
- [x] `spec/ADM_v1_DRAFT.md`
- [x] `README.md`
- [x] `ROADMAP.md`
- [x] `CHANGELOG.md`

## 11. Review Log

- [x] Principal Architect: APPROVED — `REV-ARCH-20260708-foundation-consistency-release-hygiene.md`
- [x] Security Lead: APPROVED — `REV-SEC-20260708-foundation-consistency-release-hygiene.md`
- [x] Performance Lead: APPROVED — `REV-PERF-20260708-foundation-consistency-release-hygiene.md`
- [x] Cost Engineer: APPROVED — `REV-COST-20260708-foundation-consistency-release-hygiene.md`
- [x] Simplifier: APPROVED — `REV-SIMP-20260708-foundation-consistency-release-hygiene.md`
- [x] Documentation Reviewer: APPROVED — `REV-DOC-20260708-foundation-consistency-release-hygiene.md`

## 12. Final Outcome

Accepted for v0.25 as a documentation, consistency, and release-hygiene baseline after maintainer approval and successful validation of the full review set.
