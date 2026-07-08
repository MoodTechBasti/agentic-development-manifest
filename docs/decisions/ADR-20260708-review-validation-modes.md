# Architecture Decision Record: Review Validation Modes and Gate Enforcement

> ID: ADR-20260708-review-validation-modes
> Status: PROPOSED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `scripts/validate_reviews.py`, `.github/workflows/adm-quality-gate.yml`, `docs/REVIEW_VALIDATION.md`, `docs/OPERATING_SYSTEM.md`, `spec/ADM_v1_DRAFT.md` |
| New dependencies | No |
| Security review | PENDING |
| Cost review | PENDING |
| Performance review | PENDING |

## 1. Context and Reason

ADM needs review governance that can be enforced by CI without freezing normal feature development.

The current review validator already checks completed review artifacts under `.ai/reviews/`, but the previous behavior only distinguished between normal strict validation and the advisory compatibility flag. That is not precise enough for production governance:

- feature branches need feedback without deadlocks
- pull requests to protected branches need malformed review artifacts to fail
- release branches need a complete six-role parliament review before release readiness
- manual workflow runs need an explicit way to test stricter gates

Without named modes, future agents can confuse "strict syntax validation" with "complete review set enforcement".

## 2. Decision

ADM defines three explicit review validation modes:

1. `advisory`
   - validates existing review files
   - reports errors
   - exits with status code `0`
   - intended for early feature branches and local exploration

2. `existing-strict`
   - validates existing review files
   - exits with status code `1` on malformed artifacts
   - does not require all six review files to exist
   - intended for pull requests to `main` / `master` while ADM is still below full release-gate maturity

3. `complete-set`
   - validates existing review files
   - requires one passing, CI-ready review for every standard parliament type:
     - `architect`
     - `security`
     - `performance`
     - `cost`
     - `simplifier`
     - `documentation`
   - requires each completed review artifact to have `review_status: PASSED` and `ci_ready: true`
   - exits with status code `1` if the full set is missing or not CI-ready
   - intended for release branches and explicit manual release-readiness checks

The deprecated `--advisory` flag remains as a backward-compatible alias for `--mode advisory`.

## 3. Evidence

- ADM's lifecycle states that every phase ends with review and quality gate.
- ADM already defines the six standard review roles in the Multi-Agent Parliament.
- The repository already separates reusable templates under `templates/reviews/` from runtime artifacts under `.ai/reviews/`.
- The zero-dependency validator approach remains compatible with transient CI containers and model-neutral agent execution.

## 4. Alternatives

### Alternative A: Hard blocking on all branches

- Description: Run complete-set validation for every branch and pull request.
- Reason for rejection: This blocks active feature development before a phase is actually ready for parliament review.

### Alternative B: Pure advisory validation everywhere

- Description: Keep all CI review validation non-blocking.
- Reason for rejection: This gives visibility but no production protection. Unreviewed work could pass into release branches.

### Alternative C: Only document review expectations

- Description: Leave enforcement to human reviewers or agent handovers.
- Reason for rejection: ADM's purpose is to move critical quality gates into versioned, machine-checkable repository state.

## 5. Trade-offs

### Pros

- Prevents feature-branch review deadlocks.
- Gives production/release flows a real governance gate.
- Makes CI behavior explicit and auditable.
- Preserves model neutrality because any capable agent can write the same file-based review artifacts.
- Keeps the validator dependency-free.

### Cons

- Adds branching logic to the workflow.
- Requires maintainers to understand the difference between syntax validation and complete parliament validation.
- Requires future release processes to define branch naming conventions consistently.

## 6. Risks and Consequences

- Short-term risks: A release branch can fail until all six reviews are present and CI-ready.
- Long-term risks: If branch naming conventions drift, workflows may run a weaker mode than intended.
- Mitigation plan:
  - Document mode semantics in `docs/REVIEW_VALIDATION.md`.
  - Keep `workflow_dispatch` mode selection for manual verification.
  - Use `release/**` branches for complete-set enforcement until ADM defines a stronger phase marker.

## 7. ADM Exemptions

None.

## 8. Affected Files

- [x] `scripts/validate_reviews.py`
- [x] `.github/workflows/adm-quality-gate.yml`
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

Proposed for adoption in v0.10.

Next step: run the validator in all three modes and then create the first real review artifact only after the mode semantics are merged.
