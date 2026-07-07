---
template_id: ADM-TMP-REV-DOC
template_type: review
review_type: documentation
role: Documentation Reviewer
template_status: accepted
version: 1.0.0
last_updated: 2026-07-08
runtime_target: .ai/reviews/
---

# ADM Review Template: Documentation

## 1. Runtime Metadata

| Field | Value |
| --- | --- |
| Review ID | REV-DOC-[YYYYMMDD]-[feature-slug] |
| Review date | [YYYY-MM-DD] |
| Reviewer agent | Documentation Reviewer |
| Target | [ADR ID, commit hash, feature, or path] |
| Target files | [repo-relative paths] |
| Status | PENDING / PASSED / FAILED / NEEDS_REVISION |
| Confidence score | [1-10] |

## 2. Decision Documentation Gates

- [ ] Architecture-relevant decisions are documented in ADR or ACP format.
- [ ] Decision status matches the actual review state.
- [ ] Rejected alternatives, tradeoffs, and risks are documented.
- [ ] Deprecated decisions are marked instead of silently overwritten.

## 3. Repository Documentation Gates

- [ ] `README.md` is updated if setup, commands, assumptions, or project behavior changed.
- [ ] Module READMEs are updated when module boundaries, APIs, data flow, or ownership changed.
- [ ] `CHANGELOG.md` records material changes.
- [ ] New templates, scripts, and protocols are documented where the next agent can find them.

## 4. API, Schema, and Code Documentation Gates

- [ ] Public interfaces, commands, APIs, schemas, or data formats are documented.
- [ ] Complex functions or non-obvious logic include concise docstrings or comments.
- [ ] Data lifecycle, tenant isolation, and security assumptions are documented near the relevant code or module.
- [ ] Diagrams are updated when they materially affect comprehension.

## 5. Agent Handover Gates

- [ ] The handover can explain what changed, why, what was checked, and what remains next.
- [ ] Open questions, risks, and unfinished tasks are explicit.
- [ ] A fresh agent can continue without relying on hidden chat context.

## 6. Findings

- Missing docs:
- Stale docs:
- Ambiguous docs:
- Required ADR or handover updates:

## 7. Required Actions Before Merge

- [ ] [Documentation action, owner, affected path]

## 8. Review Vote

- Vote: APPROVED / APPROVED_WITH_CONDITIONS / REJECTED
- Blocking reason if rejected:
- CI-ready: YES / NO
