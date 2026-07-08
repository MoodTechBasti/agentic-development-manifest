# ADM Release Runbook

This runbook describes the process for validating and executing an ADM release.

## 1. What is an ADM Release?

An ADM release is a repository state that has been formally reviewed by all six mandatory ADM roles and has passed the manual `complete-set` release gate.

A release is marked by an annotated Git tag, for example `v0.25`.

## 2. Release Prerequisites

Before a release can be tagged:

1. All release-scope changes must be merged into `main` via pull requests.
2. `ADM Quality Gate` must have passed on the PR or PRs.
3. All PR conversations must be resolved.
4. `CHANGELOG.md` must describe the release.
5. A complete six-role ADM review set must exist under `.ai/reviews/` for the stable reviewed state.
6. The active GitHub ruleset state must be manually audited when the release is governance-, validation-, or release-process relevant.
7. Manual release-grade `complete-set` validation must pass on `main`.

## 3. Normal PR Gate vs. Release Gate

- **Normal PR Gate (`existing-strict`)**: Runs automatically on PRs. It ensures that existing runtime review artifacts are structurally valid. It does not require all six reviews for every ordinary PR.
- **Release Gate (`complete-set`)**: Run manually before a release. It ensures that a specific `review_set_id` contains all six mandatory reviews, all `PASSED`, all `ci_ready`, and all bound to the same `target_ref` and `target_commit`.

## 4. Commit and Tag Semantics

ADM distinguishes the reviewed content commit from the final release tag commit.

- **Stable reviewed commit**: the non-review commit that contains the code, documentation, or governance state being reviewed.
- **Review artifact commit**: the later commit or commits that add the six `.ai/reviews/` files pointing to the stable reviewed commit.
- **Final release tag**: the final `main` commit after the review artifacts are merged and manual release-grade validation has passed.

The tag must point to the final `main` commit that includes the review artifacts. The reviews themselves must keep `target_commit` set to the stable reviewed commit.

## 5. Standard Release Flow

1. Merge the release PR into `main`.
2. Pull or fetch the final `main` state locally.
3. Identify the stable reviewed commit named by the review artifacts.
4. Manually audit the active GitHub ruleset if the release is governance-relevant.
5. Trigger `ADM Quality Gate` manually on `main`.
6. Use `review_gate_mode: complete-set`.
7. Provide the exact `review_set_id`, `target_ref`, and `reviewed_commit`.
8. Wait for the manual run to pass.
9. Create and push the annotated release tag on the final `main` commit.

## 6. Manual Release Validation Inputs

Trigger the `ADM Quality Gate` workflow manually on the `main` branch.

| Parameter | Value | Description |
| --- | --- | --- |
| `review_gate_mode` | `complete-set` | Hardens the check to require all six roles. |
| `review_set_id` | e.g., `RSV-YYYYMMDD-release-slug` | The review set to validate. |
| `target_ref` | e.g., `adm-v025-foundation-consistency-release-hygiene` | The branch or reference used inside the review artifacts. |
| `reviewed_commit` | e.g., `<stable-non-review-sha>` | The stable code or documentation commit that was reviewed. |

## 7. Generic Execution Example

Use current release values, not stale values copied from older examples.

```text
review_gate_mode: complete-set
review_set_id: RSV-YYYYMMDD-release-slug
target_ref: <release-branch-or-reviewed-ref>
reviewed_commit: <stable-non-review-sha>
```

For v0.25, the shape is:

```text
review_gate_mode: complete-set
review_set_id: RSV-20260708-foundation-consistency-release-hygiene
target_ref: adm-v025-foundation-consistency-release-hygiene
reviewed_commit: <stable v0.25 documentation commit before review artifacts>
```

## 8. Tagging

Only if the manual run is green, tag the final `main` commit:

```bash
git switch main
git pull --ff-only origin main
git tag -a vX.Y -m "ADM vX.Y <release summary>"
git push origin vX.Y
```

For v0.25, use the concrete release tag only after the PR has merged and the manual release-grade check has passed on `main`.

> [!IMPORTANT]
> Never set a Git tag before the manual `complete-set` release check has passed on `main`.
