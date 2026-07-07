---
template_id: ADM-TMP-REV-SIMP
template_type: review
review_type: simplifier
role: Simplifier
template_status: accepted
version: 1.0.0
last_updated: 2026-07-08
runtime_target: .ai/reviews/
---

# ADM Review Template: Simplifier

## 1. Runtime Metadata

| Field | Value |
| --- | --- |
| Review ID | REV-SIMP-[YYYYMMDD]-[feature-slug] |
| Review date | [YYYY-MM-DD] |
| Reviewer agent | Simplifier |
| Target | [ADR ID, commit hash, feature, or path] |
| Target files | [repo-relative paths] |
| Status | PENDING / PASSED / FAILED / NEEDS_REVISION |
| Confidence score | [1-10] |

## 2. Simplicity Gates

- [ ] The change is the simplest implementation that satisfies the requirement.
- [ ] New modules, files, abstractions, and patterns are justified and minimal.
- [ ] The implementation avoids premature microservices, queues, event systems, or service meshes.
- [ ] Interfaces are not introduced before there are multiple real implementations or clear test seams.
- [ ] Configuration remains understandable and avoids unnecessary environment variables.

## 3. Code Reduction Gates

- [ ] New or changed files remain below 300 lines, or an accepted ADM exemption exists.
- [ ] Similar logic was checked for existing reusable modules before adding new code.
- [ ] Duplicate code is removed or explicitly justified.
- [ ] Control flow is explicit and avoids hidden side effects.
- [ ] Complex branches, nested loops, and magic decorators are reduced where possible.

## 4. Dependency Gates

- [ ] New dependencies are necessary and cannot reasonably be replaced by existing project code or standard libraries.
- [ ] Dependency risk, maintenance, security, and cost were considered.
- [ ] Removing a dependency was considered before adding a new one.

## 5. Findings

- Overengineering found:
- Code that can be deleted:
- Abstractions that can be removed:
- Dependency concerns:

## 6. Required Actions Before Merge

- [ ] [Simplification action, owner, affected path]

## 7. Review Vote

- Vote: APPROVED / APPROVED_WITH_CONDITIONS / REJECTED
- Blocking reason if rejected:
- CI-ready: YES / NO
