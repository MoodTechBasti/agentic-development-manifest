---
template_id: ADM-TMP-REV-SEC
template_type: review
review_type: security
role: Security Engineer
template_status: accepted
version: 1.1.0
last_updated: 2026-07-08
runtime_target: .ai/reviews/
review_id: ""
review_status: PENDING
review_date: ""
reviewer_agent: ""
target: ""
target_files: []
ci_ready: false
confidence_score: null
---

# ADM Review Template: Security

## 1. Runtime Metadata

| Field | Value |
| --- | --- |
| Review ID | REV-SEC-[YYYYMMDD]-[feature-slug] |
| Review date | [YYYY-MM-DD] |
| Reviewer agent | Security Engineer |
| Target | [ADR ID, commit hash, feature, or path] |
| Target files | [repo-relative paths] |
| Review status | PENDING / PASSED / FAILED / NEEDS_REVISION |
| Confidence score | [1-10] |
| CI-ready | true / false |

## 2. Tenant Isolation Gates

- [ ] Every data access path enforces tenant or workspace scope.
- [ ] Background jobs, queues, caches, object storage, and logs preserve tenant isolation.
- [ ] Direct object references cannot cross tenant boundaries.
- [ ] Cross-tenant admin actions are explicitly authorized and auditable.

## 3. Web and API Security Gates

- [ ] Authentication and authorization are enforced for all relevant endpoints.
- [ ] Inputs are validated and typed before persistence, execution, or model calls.
- [ ] SQL injection, XSS, path traversal, RCE, and unsafe deserialization risks were checked.
- [ ] Rate limits or quotas exist for abuse-prone endpoints.
- [ ] Services run with least privilege.

## 4. AI Security Gates

- [ ] System instructions and user inputs are separated.
- [ ] Prompt injection, prompt leakage, and tool-abuse paths were checked.
- [ ] LLM calls have token, timeout, and recursion limits.
- [ ] Generated outputs are validated before being trusted or persisted.

## 5. Secrets and Configuration Gates

- [ ] No hardcoded secrets, API keys, passwords, certificates, or private tokens exist.
- [ ] Secrets are loaded from environment variables or a secrets manager.
- [ ] Sensitive values are not written to logs, traces, errors, or handovers.

## 6. Findings

| Risk | Severity | Evidence | Mitigation |
| --- | --- | --- | --- |
| [Risk] | CRITICAL / HIGH / MEDIUM / LOW | [Path or note] | [Required fix] |

## 7. Required Actions Before Merge

- [ ] [Security fix, owner, affected path]

## 8. Review Vote

- Vote: APPROVED / APPROVED_WITH_CONDITIONS / REJECTED
- Blocking reason if rejected:
- CI-ready: true / false
