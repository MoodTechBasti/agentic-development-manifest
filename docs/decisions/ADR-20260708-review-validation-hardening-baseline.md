# ADR-20260708-review-validation-hardening-baseline

> ID: ADR-20260708-review-validation-hardening-baseline
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `ROADMAP.md`, `spec/ADM_v1_DRAFT.md`, `README.md`, `CHANGELOG.md`, `docs/REVIEW_VALIDATION.md`, `docs/REVIEW_RUNBOOK.md`, `scripts/test_validate_reviews.py`, `docs/decisions/ADR-20260708-review-validation-modes.md`, `docs/decisions/ADR-20260708-review-set-scoping.md` |
| New dependencies | no |
| Security review | PASSED |
| Cost review | PASSED |
| Performance review | PASSED |

## 1. Context and Reason

Roadmap Phase 6 starts after the v0.23 Roadmap Continuation and v1 Readiness Plan. Phase 6 is about review and validation hardening, but it must not accidentally turn into broad workflow automation, release automation, or mandatory complete review sets for every ordinary pull request.

ADM already has a working review validator, fixture tests, three validation modes, target-bound review sets, and a branch-aware quality gate. The next hardening step is therefore not to rebuild the mechanism. The next step is to stabilize the accepted semantics, remove ADR status drift, and add targeted regression coverage for the existing scope-binding behavior.

Two older ADRs already describe implemented behavior but still carried `Status: PROPOSED`:

- `docs/decisions/ADR-20260708-review-validation-modes.md`
- `docs/decisions/ADR-20260708-review-set-scoping.md`

That status drift weakens repository-backed truth. If implemented behavior is treated as accepted in the specification, documentation, workflow, and validator, the corresponding decision records must not remain proposed.

## 2. Decision

ADM accepts v0.24 as the Roadmap Phase 6 Review and Validation Hardening Baseline.

This baseline does four things:

1. Promotes the already-implemented review validation mode decision to accepted status.
2. Promotes the already-implemented review-set scoping and target-binding decision to accepted status.
3. Clarifies that the current validation modes remain the stable Phase 6 baseline:
   - `advisory`
   - `existing-strict`
   - `complete-set`
4. Adds targeted validator fixture coverage for scope filtering and stale-review protection without changing workflow enforcement.

The baseline keeps normal pull requests on `existing-strict`. It keeps release-grade validation behind explicit `complete-set` runs for release branches or manual release-readiness checks.

## 3. Accepted Validation Semantics

`advisory` remains the safe feedback mode for early or exploratory work. It may report malformed artifacts without blocking.

`existing-strict` remains the normal protected-branch and pull-request mode. It blocks malformed completed review artifacts but does not require all six review roles to exist.

`complete-set` remains the release-grade and phase-transition mode. It requires all six standard review roles, `review_status: PASSED`, `ci_ready: true`, one shared `review_set_id`, one shared `target_ref`, and one shared `target_commit`.

A stale review set must not satisfy a later scoped release or phase-transition validation. Target binding remains mandatory for release-grade complete-set validation.

## 4. Scope Boundary

v0.24 may change documentation, accepted ADR status, review-validation runbooks, validator fixture tests, and review artifacts.

v0.24 may add targeted tests for existing validator behavior.

v0.24 does not add:

- new runtime behavior,
- provider SDK integration,
- MCP integration,
- local tool profiles,
- release automation,
- new workflow enforcement modes,
- mandatory complete-set validation for ordinary PRs,
- new schemas or schema language,
- Gemini CLI adapter,
- Antigravity CLI adapter,
- provider secrets,
- branch-protection changes.

## 5. Evidence

- `scripts/validate_reviews.py` already implements `advisory`, `existing-strict`, and `complete-set` modes.
- The validator already requires scoped metadata for passed or CI-ready reviews.
- The workflow already selects validation mode by branch context and manual dispatch inputs.
- `docs/REVIEW_VALIDATION.md` already documents the three-mode model and target-binding behavior.
- `docs/REVIEW_RUNBOOK.md` already documents stable reviewed-code SHA handling and manual release-grade validation.
- `CHANGELOG.md` records v0.10 and v0.11 as implemented release entries for review validation modes and review-set scoping.

## 6. Alternatives

### Alternative A: Enforce complete-set on every pull request

- Description: Require six passing reviews for all PRs to `main`.
- Reason for rejection: This would deadlock normal feature work and contradict the existing distinction between normal PR gates and release gates.

### Alternative B: Introduce a new schema layer

- Description: Add a schema language or extra parser for review artifacts.
- Reason for rejection: The current zero-dependency frontmatter validator is sufficient for the baseline. A schema layer can be evaluated later only if the vocabulary becomes too large for the current validator.

### Alternative C: Add release automation

- Description: Automatically run release-grade checks and tag releases after merge.
- Reason for rejection: ADM still requires explicit manual release-grade validation before tagging. v0.24 hardens review semantics, not release automation.

### Alternative D: Leave implemented ADRs as proposed

- Description: Keep the older review-validation ADRs in proposed status because their implementation already exists.
- Reason for rejection: That creates governance drift between the repository state and its decision records.

## 7. Trade-offs

### Pros

- Closes real governance drift before adding new mechanisms.
- Strengthens v1-readiness evidence.
- Adds targeted regression coverage without overbuilding.
- Preserves the current low-friction PR model.
- Keeps release-grade validation explicit and auditable.

### Cons

- Does not add a new validator feature.
- Does not automate releases.
- Requires future PRs to continue respecting the current mode boundaries.

## 8. Risks and Consequences

- Risk: Future agents may over-interpret Phase 6 as permission to hard-block all PRs with complete-set validation.
- Risk: More tests can create false confidence if they only check happy-path fixtures.
- Risk: Review artifacts can continue to accumulate under `.ai/reviews/`.
- Mitigation: Keep scope filtering tests explicit, preserve normal PR mode as `existing-strict`, and defer archive policy to a later ADR if review volume becomes a real problem.

## 9. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.

## 10. Affected Files

- [x] `docs/decisions/ADR-20260708-review-validation-hardening-baseline.md`
- [x] `docs/decisions/ADR-20260708-review-validation-modes.md`
- [x] `docs/decisions/ADR-20260708-review-set-scoping.md`
- [x] `docs/REVIEW_VALIDATION.md`
- [x] `docs/REVIEW_RUNBOOK.md`
- [x] `scripts/test_validate_reviews.py`
- [x] `ROADMAP.md`
- [x] `spec/ADM_v1_DRAFT.md`
- [x] `README.md`
- [x] `CHANGELOG.md`

## 11. Review Log

- [x] Principal Architect: APPROVED — `REV-ARCH-20260708-review-validation-hardening-baseline.md`
- [x] Security Lead: APPROVED — `REV-SEC-20260708-review-validation-hardening-baseline.md`
- [x] Performance Lead: APPROVED — `REV-PERF-20260708-review-validation-hardening-baseline.md`
- [x] Cost Engineer: APPROVED — `REV-COST-20260708-review-validation-hardening-baseline.md`
- [x] Simplifier: APPROVED — `REV-SIMP-20260708-review-validation-hardening-baseline.md`
- [x] Documentation Reviewer: APPROVED — `REV-DOC-20260708-review-validation-hardening-baseline.md`

## 12. Final Outcome

Accepted for v0.24 after maintainer approval and successful validation of the full review set.
