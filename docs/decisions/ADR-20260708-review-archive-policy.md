# ADR-20260708-review-archive-policy

> ID: ADR-20260708-review-archive-policy
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `.ai/README.md`, `README.md`, `ROADMAP.md`, `CHANGELOG.md`, `docs/REVIEW_VALIDATION.md`, `docs/REVIEW_RUNBOOK.md`, `scripts/test_validate_reviews.py`, `.ai/reviews/` |
| New dependencies | no |
| Security review | required for release readiness |
| Cost review | required for release readiness |
| Performance review | required for release readiness |

## 1. Context and Reason

ADM keeps completed review artifacts as versioned runtime history under `.ai/reviews/`.

That is correct for repository-backed truth, but the repository now contains many completed six-role review sets from earlier governance and release work. Keeping all historical sets directly in `.ai/reviews/` makes the active review area increasingly noisy for future agents.

The validator currently reads only direct Markdown files from the configured review directory. It does not recursively scan subdirectories. Therefore an archive subtree under `.ai/reviews/archive/` would be ignored by the normal `.ai/reviews/` validation path.

That behavior is useful, but before v0.26 it was implicit. ADM needs an explicit archive policy before any historical review sets are moved.

## 2. Decision

ADM accepts v0.26 as the Review Archive Policy baseline.

The policy defines a safe archival boundary without migrating historical review files yet.

Review artifacts have two states:

1. **Active review artifacts** live directly under `.ai/reviews/` and are part of normal review validation.
2. **Archived review artifacts** may live under `.ai/reviews/archive/<review_set_id>/` and are preserved as historical evidence, but are not part of the normal `.ai/reviews/` validation path.

Archived reviews remain repository-owned history. Archiving must not change their meaning, rewrite their review votes, or pretend they reviewed a different commit.

## 3. Accepted Rules

1. New completed review artifacts are written directly to `.ai/reviews/` first.
2. A review set may be archived only after the release, governance decision, or phase-transition evidence it supports is complete.
3. The archive path is `.ai/reviews/archive/<review_set_id>/`.
4. Archived reviews retain their original frontmatter unless a later explicit ADR defines migration metadata.
5. Archived reviews must not be used to satisfy a new release-grade `complete-set` gate unless the validator is explicitly pointed at that archive directory for a historical audit.
6. Archiving must not be used to hide malformed current review artifacts.
7. v0.26 does not move existing review artifacts.

## 4. Validator Semantics

The current validator discovers direct `*.md` files in the configured review directory only.

For the standard command:

```bash
python3 scripts/validate_reviews.py --path . --mode existing-strict
```

that means direct files under `.ai/reviews/` are validated, while `.ai/reviews/archive/**` is ignored.

This is accepted as the v0.26 baseline behavior.

v0.26 adds fixture coverage for this behavior but does not change `scripts/validate_reviews.py`.

## 5. Scope Boundary

v0.26 may change documentation, ADRs, validator fixture tests, roadmap status, changelog entries, and v0.26 review artifacts.

v0.26 does not add:

- review-file migration,
- review index generation,
- recursive validation,
- new validator mode,
- workflow hardening,
- release automation,
- Roadmap Phase 7 implementation,
- Handover linting,
- runtime code,
- MCP integration,
- provider SDK integration,
- Gemini CLI adapter,
- Antigravity CLI adapter,
- branch-protection changes,
- v1 release candidate status.

## 6. Alternatives

### Alternative A: Do nothing and start Roadmap Phase 7

- Description: Ignore archive policy and begin Handover and Session Continuity work.
- Reason for rejection: The review runtime area already contains enough historical sets that a clear archive boundary should exist before building more continuity semantics on top of `.ai/`.

### Alternative B: Documentation-only policy

- Description: Document archive rules without touching tests.
- Reason for rejection: The important behavior would remain an untested implementation detail. A future recursive scan could silently pull archived reviews back into normal validation.

### Alternative C: Policy plus minimal validator fixture coverage

- Description: Document the policy and add one targeted test proving archive subdirectories are ignored by the standard validator path.
- Decision: Accepted.

### Alternative D: Full review storage redesign

- Description: Add review indexes, manifests, active-set registries, archive migration tooling, or new validator modes.
- Reason for rejection: Too large for v0.26. The current problem is policy clarity and regression protection, not a need for a new review-storage subsystem.

## 7. Trade-offs

### Pros

- Makes review archival semantics explicit before any file movement.
- Reduces future governance ambiguity around `.ai/reviews/` growth.
- Preserves existing validator simplicity.
- Adds regression coverage without changing production validator logic.
- Keeps Roadmap Phase 7 cleanly blocked until review storage hygiene is defined.

### Cons

- Does not reduce the current number of top-level review files yet.
- Archived review discovery for historical audits remains manual unless a later explicit ADR adds tooling.
- A later migration PR is still needed if maintainers decide to move old review sets.

## 8. Migration Rule

Historical review migration is explicitly deferred.

A later migration PR may move completed historical review sets into `.ai/reviews/archive/<review_set_id>/`, but only after:

1. this policy is merged,
2. normal validation still passes,
3. the migration PR clearly lists moved review sets,
4. release-relevant review evidence remains discoverable from git history and documented release notes.

## 9. Final Outcome

Accepted as the v0.26 Review Archive Policy baseline.

No existing review artifacts are moved in v0.26. No validator production logic is changed in v0.26.
