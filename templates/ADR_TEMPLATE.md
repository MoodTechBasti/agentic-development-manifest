# Architecture Decision Record Template

> ID: ADR-[YYYYMMDD]-[title-slug]
> Status: DRAFT / PROPOSED / ACCEPTED / REJECTED / DEPRECATED
> Last updated: [YYYY-MM-DD]
> Owner: [agent role]

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | [1-10] |
| Affected modules | [module list] |
| New dependencies | [yes/no; list if yes] |
| Security review | PENDING / PASSED / EXEMPT |
| Cost review | PENDING / PASSED / EXEMPT |
| Performance review | PENDING / PASSED / EXEMPT |

## 1. Context and Reason

Describe the concrete problem, requirement, constraint, or risk that makes this decision necessary.

## 2. Decision

State the decision precisely and unambiguously.

## 3. Evidence

List the evidence that supports this decision.

- Source or internal reference:
- Benchmark or measurement:
- Relevant code path:
- Research note:

## 4. Alternatives

Document at least two alternatives and why they were rejected.

### Alternative A: [name]

- Description:
- Reason for rejection:

### Alternative B: [name]

- Description:
- Reason for rejection:

## 5. Trade-offs

### Pros

- [benefit]

### Cons

- [cost or downside]

## 6. Risks and Consequences

- Short-term risks:
- Long-term risks:
- Mitigation plan:

## 7. ADM Exemptions

Use this section only when an implementation must intentionally exceed an ADM quality rule.

Line-limit exemptions must use this exact machine-readable format so `scripts/check_limits.py` can detect them:

```text
ADM-Exemption: src/path/to/file.py (Max: 500)
```

Rules:

- The ADR status must be ACCEPTED or APPROVED before the exemption is valid.
- The path must be repository-relative.
- The maximum line count must be explicit.
- The reason must be explained in sections 1, 3, 5, and 6.

## 8. Affected Files

Use repository-relative paths.

- [ ] `path/to/file`

## 9. Review Log

- [ ] Principal Architect: APPROVED / REJECTED / COMMENT — [comment]
- [ ] Devil's Advocate: APPROVED / REJECTED / COMMENT — [comment]
- [ ] Security Lead: APPROVED / REJECTED / COMMENT — [comment]
- [ ] Cost Engineer: APPROVED / REJECTED / COMMENT — [comment]
- [ ] Performance Lead: APPROVED / REJECTED / COMMENT — [comment]
- [ ] Simplifier: APPROVED / REJECTED / COMMENT — [comment]

## 10. Final Outcome

State whether the decision was accepted, rejected, or postponed, and explain the next step.
