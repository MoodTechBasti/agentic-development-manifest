---
template_id: ADM-TMP-REV-COST
template_type: review
review_type: cost
role: Cost Engineer
template_status: accepted
version: 1.2.0
last_updated: 2026-07-08
runtime_target: .ai/reviews/
review_id: ""
review_set_id: ""
target_ref: ""
target_commit: ""
review_status: PENDING
review_date: ""
reviewer_agent: ""
target: ""
target_files: []
ci_ready: false
confidence_score: null
---

# ADM Review Template: Cost

## 1. Runtime Metadata

| Field | Value |
| --- | --- |
| Review ID | REV-COST-[YYYYMMDD]-[feature-slug] |
| Review set ID | RSV-[YYYYMMDD]-[feature-slug] |
| Target ref | PR-[number], release branch, or named ref |
| Target commit | Git commit SHA being reviewed |
| Review date | [YYYY-MM-DD] |
| Reviewer agent | Cost Engineer |
| Target | [ADR ID, commit hash, feature, or path] |
| Target files | [repo-relative paths] |
| Review status | PENDING / PASSED / FAILED / NEEDS_REVISION |
| Confidence score | [1-10] |
| CI-ready | true / false |

## 2. AI and Token Cost Gates

- [ ] The selected model is the cheapest model that can reliably solve the task.
- [ ] Expensive models are limited to tasks that justify their cost.
- [ ] System prompts and context are compact enough to avoid avoidable token overhead.
- [ ] Provider caching is used when available without creating hard provider lock-in.
- [ ] LLM calls have token, timeout, and recursion limits.
- [ ] Agent loops have a hard maximum iteration count.

## 3. Infrastructure Cost Gates

- [ ] Compute usage scales predictably with users, tenants, workspaces, jobs, or requests.
- [ ] Storage growth is bounded by retention, archive, and deletion rules.
- [ ] Background work is queued, bounded, and observable.
- [ ] Expensive third-party calls are tracked and rate-limited.

## 4. Cost Attribution Gates

- [ ] Usage can be attributed to user, workspace, tenant, feature, request, worker time, and model call where applicable.
- [ ] Quotas or entitlements prevent unpaid or abusive usage growth.
- [ ] Cost telemetry is sufficient for later pricing and gross-margin analysis.

## 5. Cost Estimate

| Unit | Estimated cost | Evidence | Status |
| --- | --- | --- | --- |
| Per user | [value] | [source or assumption] | OK / RISK |
| Per tenant or workspace | [value] | [source or assumption] | OK / RISK |
| Per API request | [value] | [source or assumption] | OK / RISK |
| Per worker job | [value] | [source or assumption] | OK / RISK |
| Per model call | [value] | [source or assumption] | OK / RISK |

## 6. Findings

- Cost risks:
- Missing telemetry:
- Optimization opportunities:
- Required ADRs:

## 7. Required Actions Before Merge

- [ ] [Cost-control action, owner, affected path]

## 8. Review Vote

- Vote: APPROVED / APPROVED_WITH_CONDITIONS / REJECTED
- Blocking reason if rejected:
- CI-ready: true / false
