# ADR-20260708-foundation-hygiene-cleanup

> ID: ADR-20260708-foundation-hygiene-cleanup
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `docs/decisions/`, `docs/RELEASE_RUNBOOK.md`, `.github/pull_request_template.md`, `scripts/validate_reviews.py`, `scripts/test_validate_reviews.py`, `README.md`, `ROADMAP.md`, `CHANGELOG.md`, `spec/ADM_v1_DRAFT.md`, `docs/OPERATING_SYSTEM.md` |
| New dependencies | no |
| Security review | pending review set |
| Cost review | pending review set |
| Performance review | pending review set |

## 1. Context and Reason

After v0.30, the repository had a clean release tag, archived historical review evidence, and no active `adm-v*` branch residue.

A pre-v1 foundation audit still found small hygiene issues:

- v0.29 and v0.30 ADRs still contained `pending review set` wording after their review sets and release tags already existed.
- `docs/RELEASE_RUNBOOK.md` required release-grade validation, but did not clearly distinguish GitHub manual workflow evidence from local terminal evidence.
- `.github/pull_request_template.md` did not force contributors to separate local validation, PR CI evidence, and manual release-grade workflow evidence.
- `scripts/validate_reviews.py` correctly validated all direct review files before applying complete-set scope filters, but the output could make out-of-scope active review files look like part of the scoped release proof.

These are not v0.30 correctness defects. They are foundation hygiene issues worth fixing before Roadmap Phase 9.

## 2. Decision

ADM accepts v0.31 as a Foundation Hygiene Cleanup.

v0.31 may:

1. finalize stale ADR review-evidence wording for already completed v0.29 and v0.30 review sets,
2. clarify release evidence policy in the release runbook,
3. strengthen the PR template so validation evidence types are not mixed,
4. improve review-validator output wording without changing validation semantics,
5. synchronize canonical status documents for the v0.31 cleanup.

## 3. Scope Boundary

v0.31 does not add:

- Roadmap Phase 9 implementation,
- v1 release-candidate status,
- workflow changes,
- release automation,
- new validator modes,
- recursive archive validation,
- review index generation,
- runtime code,
- MCP integration,
- provider SDK integration,
- adapter expansion,
- branch-protection changes.

## 4. Release Evidence Policy

Release evidence must explicitly distinguish:

- local terminal validation,
- GitHub Actions PR gate evidence,
- manual GitHub `workflow_dispatch` release-grade evidence,
- manual ruleset audit evidence.

Local release-grade validation is useful and may be required by maintainers, but it must not be described as a GitHub manual workflow run.

For governance-, validation-, and release-process relevant releases, GitHub manual workflow evidence is the preferred release record because it is repository-hosted and easier to audit later.

## 5. Validator Output Policy

The review validator may continue to structurally validate all direct `.ai/reviews/*.md` files before applying complete-set scope filters.

When running `complete-set`, the output should make this order explicit so future maintainers do not confuse structurally valid out-of-scope reviews with the scoped release proof.

This is an output-clarity change only. It does not change:

- which files are scanned,
- which archive files are ignored,
- required review roles,
- required `PASSED` status,
- required `ci_ready: true`,
- `review_set_id`, `target_ref`, or `target_commit` scoping.

## 6. Alternatives

### Alternative A: Leave ADR `pending review set` wording alone

- Reason for rejection: It preserves stale final-state evidence in accepted ADRs after release tags already exist.

### Alternative B: Treat local release validation and GitHub manual workflow evidence as interchangeable without labels

- Reason for rejection: That weakens auditability and makes release records ambiguous.

### Alternative C: Refactor the validator deeply

- Reason for rejection: The validator semantics are already covered by fixture tests. v0.31 only needs output clarity, not a behavioral rewrite.

### Alternative D: Start Roadmap Phase 9 immediately

- Reason for rejection: v0.31 exists to clean foundation hygiene before defining v1 release-candidate criteria.

## 7. Risks and Consequences

- Risk: Updating old ADR status lines could be mistaken for rewriting historical decisions.
- Mitigation: v0.31 only finalizes review-evidence status and final outcome notes. It does not retarget historical review artifacts or change decision semantics.

- Risk: Release evidence rules could be read as requiring release automation.
- Mitigation: The runbook remains manual and evidence-based. No workflow behavior changes are included.

- Risk: Validator output wording could be mistaken for a new validator mode.
- Mitigation: No new mode, input, or pass/fail behavior is introduced.

## 8. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.

## 9. Final Outcome

Pending six-role review set after the stable non-review target commit is created.
