# ADR-20260708-review-archive-migration-batch-2

> ID: ADR-20260708-review-archive-migration-batch-2
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `.ai/reviews/`, `.ai/reviews/archive/`, `.ai/README.md`, `README.md`, `ROADMAP.md`, `CHANGELOG.md`, `docs/OPERATING_SYSTEM.md`, `spec/ADM_v1_DRAFT.md` |
| New dependencies | no |
| Security review | PASSED via `RSV-20260708-review-archive-migration-batch-2` |
| Cost review | PASSED via `RSV-20260708-review-archive-migration-batch-2` |
| Performance review | PASSED via `RSV-20260708-review-archive-migration-batch-2` |

## 1. Context and Reason

v0.26 accepted the Review Archive Policy.

v0.27 migrated completed historical review sets up to v0.25 into `.ai/reviews/archive/<review_set_id>/`.

After v0.29, the direct `.ai/reviews/` active validation area again contains multiple completed historical review sets:

- `RSV-20260708-review-archive-policy`
- `RSV-20260708-review-archive-migration-batch-1`
- `RSV-20260708-session-continuity-baseline`
- `RSV-20260708-tool-verification-discovery-baseline`

Only the latest release evidence should remain active before Roadmap Phase 9 v1 Release Candidate Criteria are planned.

## 2. Decision

ADM accepts v0.30 as Review Archive Migration Batch 2.

This migration moves completed review sets for v0.26 through v0.28 from direct `.ai/reviews/*.md` files into:

```text
.ai/reviews/archive/<review_set_id>/
```

The v0.29 Tool Verification Discovery Baseline review set remains directly under `.ai/reviews/` as the current active release evidence.

## 3. Migrated Review Sets

The following completed review sets are migrated in this batch:

- `RSV-20260708-review-archive-policy`
- `RSV-20260708-review-archive-migration-batch-1`
- `RSV-20260708-session-continuity-baseline`

## 4. Preservation Rules

Moved review files retain their original file contents and frontmatter.

The migration does not retarget historical reviews, rewrite votes, change `target_ref`, change `target_commit`, change `review_status`, or change `ci_ready`.

## 5. Scope Boundary

v0.30 may move completed review files and update documentation that records the migration.

v0.30 does not add:

- production validator logic changes,
- recursive validation,
- new validator modes,
- workflow changes,
- release automation,
- review index generation,
- Roadmap Phase 9 implementation,
- v1 release-candidate status,
- Handover linting,
- runtime code,
- MCP integration,
- provider SDK integration,
- Gemini CLI adapter,
- Antigravity CLI adapter,
- branch-protection changes.

## 6. Validation Expectations

Normal validation against `.ai/reviews/` should continue to validate only the active direct review files.

Archived historical review files are preserved for auditability and git history, but normal validation should not recursively include them.

Release-grade validation for v0.30 must use the v0.30 review set directly under `.ai/reviews/` and the stable non-review migration commit as `target_commit`.

## 7. Trade-off

This migration intentionally keeps review storage simple.

ADM does not add a review index, archive manifest, recursive validator, or automation layer because the current direct-file plus archive-directory model is sufficient and already covered by validator fixture tests.

## 8. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.

## 9. Final Outcome

Six-role review set was completed under `RSV-20260708-review-archive-migration-batch-2` and release-grade validation passed before tagging v0.30.
