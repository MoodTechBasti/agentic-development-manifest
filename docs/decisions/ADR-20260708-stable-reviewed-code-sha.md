# Architecture Decision Record: Stable Reviewed-Code SHA for Complete Review Sets

> ID: ADR-20260708-stable-reviewed-code-sha
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## 1. Context

ADM v0.11 binds complete review sets to `review_set_id`, `target_ref`, and `target_commit`.

A follow-up review found a deadlock risk: if CI requires `target_commit` to equal the current workflow SHA, then adding `.ai/reviews/*.md` artifacts changes the commit SHA. The review artifact cannot reliably name the commit that contains itself.

The mechanism has been implemented since v0.11.1: complete-set gates can use an explicit manual `reviewed_commit`, and automated resolution uses the latest commit that changed repository content outside `.ai/reviews/`.

## 2. Decision

`target_commit` means the stable code-under-review or documentation-under-review commit, not necessarily the workflow commit that contains the review artifacts.

For `complete-set` gates, CI resolves the reviewed commit as follows:

1. If a manual `workflow_dispatch` run provides `reviewed_commit`, use that value.
2. Otherwise, use the latest commit that changed repository content outside `.ai/reviews/`.

This keeps review artifacts separate from the repository state they reviewed.

## 3. Consequences

### Positive

- Avoids self-deadlocking review gates.
- Preserves the ability to commit review artifacts after the reviewed content commit.
- Keeps `target_commit` meaningful as the content-under-review anchor.
- Supports release hygiene where the final tag commit includes review artifacts, while review files still point to the stable reviewed commit.

### Negative

- Requires full git history in CI checkout.
- Assumes runtime review artifacts are stored under `.ai/reviews/`.
- Mixed commits that change reviewed content and review artifacts together remain discouraged.

## 4. Required Operating Rule

Agents should use this sequence for complete release-grade review sets:

1. Commit the code or documentation that needs review.
2. Record that commit SHA as `target_commit`.
3. Create the six `.ai/reviews/REV-*` artifacts in a later commit.
4. Run `complete-set` against the recorded content-under-review SHA.

## 5. Affected Files

- [x] `.github/workflows/adm-quality-gate.yml`
- [x] `docs/REVIEW_VALIDATION.md`
- [x] `docs/OPERATING_SYSTEM.md`
- [x] `spec/ADM_v1_DRAFT.md`
- [x] `CHANGELOG.md`

## 6. Final Outcome

Accepted as implemented repository behavior since v0.11.1. Status normalized during v0.25 Foundation Consistency and Release Hygiene cleanup.
