# ADR-20260708-review-archive-migration-batch-1

> ID: ADR-20260708-review-archive-migration-batch-1
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `.ai/reviews/`, `.ai/reviews/archive/`, `README.md`, `ROADMAP.md`, `CHANGELOG.md` |
| New dependencies | no |
| Security review | required for release readiness |
| Cost review | required for release readiness |
| Performance review | required for release readiness |

## 1. Context and Reason

v0.26 accepted the Review Archive Policy and intentionally did not move old review artifacts.

That was the right sequencing: policy first, migration later.

After v0.26, `.ai/reviews/` is formally defined as the active review validation area, but it still contains many completed historical review sets. This creates avoidable navigation noise for future agents before Roadmap Phase 7 Handover and Session Continuity.

## 2. Decision

ADM accepts v0.27 as Review Archive Migration Batch 1.

The migration moves completed historical review sets from direct `.ai/reviews/*.md` files into:

```text
.ai/reviews/archive/<review_set_id>/
```

The current v0.26 review set remains directly under `.ai/reviews/` so the latest release evidence remains immediately visible until a later release supersedes it.

## 3. Migrated Review Sets

The following completed historical review sets are migrated in this batch:

- `RSV-20260708-main-protection-ruleset`
- `RSV-20260708-review-governance-v0111`
- `RSV-20260708-release-baseline-hardening`
- `RSV-20260708-spec-prompt-alignment`
- `RSV-20260708-project-owned-memory`
- `RSV-20260708-agent-registry`
- `RSV-20260708-handover-automation`
- `RSV-20260708-saas-foundation-standard`
- `RSV-20260708-ai-foundation-standard`
- `RSV-20260708-master-prompt-standard`
- `RSV-20260708-adapter-prompt-standard`
- `RSV-20260708-roadmap-continuation-v1-readiness`
- `RSV-20260708-review-validation-hardening-baseline`
- `RSV-20260708-foundation-consistency-release-hygiene`

## 4. Preservation Rules

Moved review files retain their original file contents and frontmatter.

The migration does not retarget historical reviews, rewrite votes, change `target_ref`, change `target_commit`, change `review_status`, or change `ci_ready`.

## 5. Scope Boundary

v0.27 may move historical review files and update documentation that records the migration.

v0.27 does not add:

- production validator logic changes,
- recursive validation,
- new validator modes,
- workflow changes,
- release automation,
- review index generation,
- Roadmap Phase 7 implementation,
- Handover linting,
- runtime code,
- MCP integration,
- provider SDK integration,
- Gemini CLI adapter,
- Antigravity CLI adapter,
- branch-protection changes,
- v1 release candidate status.

## 6. Validation Expectations

Normal validation against `.ai/reviews/` should continue to validate only the active direct review files.

Archived historical review files are preserved for auditability and git history, but normal validation should not recursively include them.

Release-grade validation for v0.27 must use the v0.27 review set directly under `.ai/reviews/` and the stable non-review migration commit as `target_commit`.

## 7. Final Outcome

Accepted as v0.27 Review Archive Migration Batch 1.

The active `.ai/reviews/` area is reduced to current release evidence while historical evidence remains repository-owned under `.ai/reviews/archive/<review_set_id>/`.
