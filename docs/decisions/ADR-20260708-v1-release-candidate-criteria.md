# ADR-20260708-v1-release-candidate-criteria

> ID: ADR-20260708-v1-release-candidate-criteria
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `ROADMAP.md`, `spec/ADM_v1_DRAFT.md`, `docs/RELEASE_RUNBOOK.md`, `docs/REVIEW_RUNBOOK.md`, `docs/REVIEW_VALIDATION.md`, `.ai/README.md`, `README.md`, `CHANGELOG.md` |
| New dependencies | no |
| Security review | pending review set |
| Cost review | pending review set |
| Performance review | pending review set |

## 1. Context and Reason

After v0.31, ADM has accepted Roadmap Phase 8, review archive hygiene, release-evidence clarification, and validator output clarity.

Roadmap Phase 9 remained open: ADM still needed exact criteria for when a future repository state may be treated as a v1 release candidate.

Without a criteria ADR, future agents could make three unsafe mistakes:

- treat v0.32 itself as a v1 release candidate,
- reuse older release review sets as v1-RC proof,
- confuse local validation, GitHub workflow evidence, ruleset audit evidence, and source documentation.

v0.32 therefore defines the v1-RC criteria without creating a v1-RC release.

## 2. Decision

ADM accepts v0.32 as Roadmap Phase 9: v1 Release Candidate Criteria.

A future v1 release candidate may be tagged only when the target repository state has synchronized documentation, accepted decision evidence, complete review evidence, explicit release validation evidence, and manual ruleset audit evidence where release-relevant.

v0.32 defines criteria only. It does not declare ADM v1-ready, does not create a v1 release candidate, and does not authorize a v1 or v1-RC tag.

## 3. v1 Release Candidate Evidence Checklist

A v1 release candidate requires:

1. synchronized `README.md`, `ROADMAP.md`, `CHANGELOG.md`, `spec/ADM_v1_DRAFT.md`, and relevant governance runbooks,
2. accepted ADR coverage for completed roadmap phases and governance baselines,
3. a fresh complete six-role review set for the v1-RC target state,
4. review artifacts bound to the stable reviewed content commit through explicit `review_set_id`, `target_ref`, and `target_commit`,
5. release-grade `complete-set` validation for the exact v1-RC scope,
6. explicit release evidence distinguishing GitHub PR quality gate, GitHub manual workflow evidence, local terminal evidence, and ruleset audit evidence,
7. manual GitHub ruleset audit evidence for governance-relevant v1-RC release readiness,
8. a non-ambiguous active `.ai/reviews/` area for the v1-RC release gate.

## 4. Scope Boundary

v0.32 may:

- define v1-RC evidence criteria,
- clarify release and review runbooks for v1-RC use,
- clarify the active review evidence boundary,
- synchronize README, roadmap, changelog, and specification status,
- add this ADR and later a complete six-role review set for v0.32.

v0.32 does not add:

- v1 release-candidate status,
- a v1 tag,
- a v1-RC tag,
- workflow changes,
- release automation,
- new validator modes,
- recursive archive validation,
- review index generation,
- runtime code,
- MCP integration,
- provider SDK integration,
- adapter expansion,
- Handover linting,
- branch-protection changes,
- review archive migration.

## 5. Active Review Evidence Boundary

Direct files under `.ai/reviews/` remain the active review validation area.

For a future v1 release candidate, this active area must not be ambiguous. Historical or completed non-RC review sets should either be archived before the v1-RC release process or explicitly documented as intentionally active and out of scope.

The v1-RC release gate must always use explicit `review_set_id`, `target_ref`, and `target_commit`.

## 6. Alternatives

### Alternative A: Declare v0.32 as v1-RC

- Reason for rejection: v0.32 defines criteria. It does not prove that ADM is v1-ready.

### Alternative B: Build release automation first

- Reason for rejection: ADM's current release process is evidence-based and manual. Automation is not required to define v1-RC criteria.

### Alternative C: Add a new validator mode for v1-RC

- Reason for rejection: Existing scoped `complete-set` validation is sufficient. A new mode would add semantics without need.

### Alternative D: Migrate or archive review sets in v0.32

- Reason for rejection: That would turn v0.32 into another review archive migration. The correct scope is criteria definition only.

### Alternative E: Add a review index

- Reason for rejection: A review index may be useful later, but v1-RC criteria can be expressed with the existing review-set, target-ref, and target-commit model.

## 7. Risks and Consequences

- Risk: Future agents may read v0.32 as a v1-RC declaration.
- Mitigation: Canonical docs state that v0.32 defines criteria only and does not create v1-RC status.

- Risk: Older complete review sets may be reused as v1-RC proof.
- Mitigation: v1-RC requires a fresh, explicitly scoped six-role review set for the v1-RC target state.

- Risk: Active `.ai/reviews/` files may confuse v1-RC evidence.
- Mitigation: A future v1-RC gate must avoid ambiguity by archiving completed historical review sets or documenting them as out of scope.

- Risk: Ruleset audit evidence may be confused with source documentation.
- Mitigation: Manual GitHub ruleset audit remains external evidence and must be explicitly recorded.

## 8. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.
