---
template_id: ADM-TMP-REV-PERF
template_type: review
review_type: performance
role: SRE and Performance Lead
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
measurement_type: not_applicable
---

# ADM Review Template: Performance and SRE

## 1. Runtime Metadata

| Field | Value |
| --- | --- |
| Review ID | REV-PERF-[YYYYMMDD]-[feature-slug] |
| Review set ID | RSV-[YYYYMMDD]-[feature-slug] |
| Target ref | PR-[number], release branch, or named ref |
| Target commit | Git commit SHA being reviewed |
| Review date | [YYYY-MM-DD] |
| Reviewer agent | SRE and Performance Lead |
| Target | [ADR ID, commit hash, feature, or path] |
| Target files | [repo-relative paths] |
| Review status | PENDING / PASSED / FAILED / NEEDS_REVISION |
| Confidence score | [1-10] |
| Measurement type | measured / estimated / not_applicable |
| CI-ready | true / false |

## 2. Performance Budget Gates

| Metric | Budget | Result | Status |
| --- | --- | --- | --- |
| Standard API latency | < 150 ms | [value] | PASSED / FAILED / EXEMPT |
| Frontend load time | < 2.0 s | [value] | PASSED / FAILED / EXEMPT |
| Background worker duration | < 5.0 min | [value] | PASSED / FAILED / EXEMPT |
| Cold start | < 500 ms | [value] | PASSED / FAILED / EXEMPT |
| AI or third-party call | [service budget] | [value] | PASSED / FAILED / EXEMPT |

Any FAILED or EXEMPT status requires an ADR or explicit review finding.

## 3. Reliability Gates

- [ ] External calls use explicit timeouts.
- [ ] Retry policies use bounded retries with backoff and jitter.
- [ ] Circuit breakers protect fragile third-party or LLM-provider dependencies.
- [ ] Background jobs are idempotent or document why idempotency is not applicable.
- [ ] Persistent worker failures go to a dead letter queue or equivalent review path.
- [ ] Processes handle graceful shutdown without data loss.

## 4. Resource Efficiency Gates

- [ ] New or changed database queries were checked for N+1 patterns.
- [ ] Required indexes exist for tenant, workspace, foreign-key, and lookup fields.
- [ ] Caching has clear TTL and invalidation rules.
- [ ] Connection pools are bounded and released correctly.

## 5. Findings

- Bottlenecks:
- Missing measurements:
- Budget violations:
- Reliability risks:

## 6. Required Actions Before Merge

- [ ] [Performance or reliability fix, owner, affected path]

## 7. Review Vote

- Vote: APPROVED / APPROVED_WITH_CONDITIONS / REJECTED
- Blocking reason if rejected:
- CI-ready: true / false
