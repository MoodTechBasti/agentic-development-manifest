---
template_id: ADM-TMP-REV-ARCH
template_type: review
review_type: architect
role: Principal Architect
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

# ADM Review Template: Architect

## 1. Runtime Metadata

| Field | Value |
| --- | --- |
| Review ID | REV-ARCH-[YYYYMMDD]-[feature-slug] |
| Review date | [YYYY-MM-DD] |
| Reviewer agent | Principal Architect |
| Target | [ADR ID, commit hash, feature, or path] |
| Target files | [repo-relative paths] |
| Review status | PENDING / PASSED / FAILED / NEEDS_REVISION |
| Confidence score | [1-10] |
| CI-ready | true / false |

## 2. Architecture Gates

- [ ] The change follows Modular Monolith First unless an accepted ADR justifies another architecture.
- [ ] Module boundaries are explicit and avoid circular dependencies.
- [ ] Interfaces are typed, documented, and stable enough for other agents to use.
- [ ] Existing modules are reused where appropriate instead of duplicating logic.
- [ ] New dependencies are justified by an ADR or review finding.

## 3. Code Structure Gates

- [ ] New or changed source files stay under 300 lines, or an accepted ADM exemption exists.
- [ ] The design avoids God classes, hidden global state, and magic side effects.
- [ ] The implementation is testable through dependency injection, mocks, fakes, or clear seams.
- [ ] Foundation code paths are prepared for the expected coverage target.

## 4. SaaS Foundation Fit

- [ ] The change preserves tenant isolation boundaries.
- [ ] Data ownership and lifecycle responsibilities are clear.
- [ ] The design can evolve without premature microservices or infrastructure complexity.

## 5. Findings

- Strengths:
- Risks:
- Technical debt:
- Required ADRs:

## 6. Required Actions Before Merge

- [ ] [Action item, owner, affected path]

## 7. Review Vote

- Vote: APPROVED / APPROVED_WITH_CONDITIONS / REJECTED
- Blocking reason if rejected:
- CI-ready: true / false
