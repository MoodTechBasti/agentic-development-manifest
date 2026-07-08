# Architecture Decision Record: Review Set Scoping and Target Binding

> ID: ADR-20260708-review-set-scoping
> Status: PROPOSED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `scripts/validate_reviews.py`, `.github/workflows/adm-quality-gate.yml`, `templates/reviews/`, `docs/REVIEW_VALIDATION.md`, `spec/ADM_v1_DRAFT.md` |
| New dependencies | No |
| Security review | PENDING |
| Cost review | PENDING |
| Performance review | PENDING |

## 1. Context and Reason

ADM v0.10 introduced explicit review validation modes, but `complete-set` still had a stale-review risk: old passing review artifacts could remain in `.ai/reviews/` and accidentally satisfy a later release gate.

Static runtime filenames such as `.ai/reviews/architect.md` also create an overwrite risk. A later review can replace the previous one and destroy historical auditability.

ADM needs each parliament review batch to be bound to one logical review set and one target code state.

## 2. Decision

ADM v0.11 introduces review-set scoping.

Every completed review artifact must include these additional frontmatter fields:

- `review_set_id`: logical review-set identifier, e.g. `RSV-20260708-review-set-scoping`
- `target_ref`: human-readable target reference, e.g. `PR-2`, `release/v1`, or a named branch
- `target_commit`: git commit SHA that was reviewed

The complete-set gate is valid only when all six standard review types are present for the same `review_set_id`, the same `target_ref`, and the same `target_commit`.

The validator keeps v0.10 modes:

- `advisory`
- `existing-strict`
- `complete-set`

`complete-set` now also supports explicit scope filters:

- `--review-set-id`
- `--target-ref`
- `--target-commit`

Deprecated compatibility aliases remain available where useful:

- `--advisory`
- `--strict`
- `--set-id`
- `--dir`

## 3. Evidence

- The v0.10 validator can prove six passing roles exist, but cannot prove they belong to the current PR, branch, or commit.
- Review templates already live separately from completed artifacts.
- The repository already uses branch-aware workflow modes; adding target binding to release checks is a direct continuation of that design.
- Zero-dependency Python remains sufficient for this validation layer.

## 4. Alternatives

### Alternative A: Use static role filenames

- Description: Keep writing `.ai/reviews/architect.md`, `.ai/reviews/security.md`, and similar files.
- Reason for rejection: This overwrites review history and weakens auditability.

### Alternative B: Require only one complete set anywhere in `.ai/reviews/`

- Description: Pass `complete-set` if any six reviews are present.
- Reason for rejection: This permits stale reviews to satisfy a newer release gate.

### Alternative C: Store review state outside git

- Description: Track review state in a database, issue tracker, or external workflow system.
- Reason for rejection: ADM's core operating model is file-based, git-versioned, model-neutral governance.

## 5. Trade-offs

### Pros

- Prevents stale review artifacts from satisfying new release gates.
- Preserves historical review audit trails.
- Keeps review governance model-neutral and file-based.
- Lets CI bind `complete-set` checks to PR numbers, branch names, and commit SHAs.

### Cons

- Agents must fill more metadata fields.
- Manual review creation becomes stricter.
- Historical review files may accumulate and require later archive policy.

## 6. Risks and Consequences

- Short-term risk: Existing completed reviews without v0.11 scope metadata will fail strict validation after this change.
- Long-term risk: `.ai/reviews/` can grow over time.
- Mitigation plan:
  - Keep templates updated with required fields.
  - Use review IDs as filenames for runtime artifacts.
  - Add an archive policy later if review volume becomes noisy.

## 7. ADM Exemptions

None.

## 8. Affected Files

- [x] `scripts/validate_reviews.py`
- [x] `.github/workflows/adm-quality-gate.yml`
- [x] `templates/reviews/architect.md`
- [x] `templates/reviews/security.md`
- [x] `templates/reviews/performance.md`
- [x] `templates/reviews/cost.md`
- [x] `templates/reviews/simplifier.md`
- [x] `templates/reviews/documentation.md`
- [x] `docs/REVIEW_VALIDATION.md`
- [x] `docs/OPERATING_SYSTEM.md`
- [x] `spec/ADM_v1_DRAFT.md`
- [x] `CHANGELOG.md`

## 9. Review Log

- [ ] Principal Architect: APPROVED / REJECTED / COMMENT — pending
- [ ] Devil's Advocate: APPROVED / REJECTED / COMMENT — pending
- [ ] Security Lead: APPROVED / REJECTED / COMMENT — pending
- [ ] Cost Engineer: APPROVED / REJECTED / COMMENT — pending
- [ ] Performance Lead: APPROVED / REJECTED / COMMENT — pending
- [ ] Simplifier: APPROVED / REJECTED / COMMENT — pending

## 10. Final Outcome

Proposed for adoption in v0.11.

Next step: merge v0.11, then create the first real review set against the merged commit using the six updated templates.
