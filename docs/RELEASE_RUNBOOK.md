# ADM Release Runbook

This runbook describes the process for validating and executing an ADM release.

## 1. What is an ADM Release?

An ADM release is a state of the repository that has been formally reviewed by all six mandatory ADM roles and has passed the manual `complete-set` release gate. A release is marked by a Git tag (e.g., `v0.13`).

## 2. Release Prerequisites

Before a release can be tagged:

1.  All changes must be merged into `main` via pull requests.
2.  `ADM Quality Gate` must have passed on all PRs.
3.  A complete six-role ADM review set must exist under `.ai/reviews/` for the target state.
4.  `CHANGELOG.md` must be updated with the new version.
5.  Manual release-grade `complete-set` validation must pass on `main`.

## 3. Normal PR Gate vs. Release Gate

*   **Normal PR Gate (`existing-strict`)**: Runs automatically on PRs. Ensures that *if* review artifacts exist, they are structurally valid. It does not require a full set of reviews.
*   **Release Gate (`complete-set`)**: Run manually before a release. Ensures that a specific `review_set_id` contains all six mandatory reviews, all `PASSED`, all `ci_ready`, and all bound to the same `target_ref` and `target_commit`.

## 4. Manual Release Validation

To execute the release gate, trigger the `ADM Quality Gate` workflow manually on the `main` branch.

### Parameters

| Parameter | Value | Description |
| --- | --- | --- |
| `review_gate_mode` | `complete-set` | Hardens the check to require all six roles. |
| `review_set_id` | e.g., `RSV-20260708-main-protection-ruleset` | The ID of the review set to validate. |
| `target_ref` | e.g., `adm-v013-repository-governance` | The reference (branch) where the reviews were performed. |
| `reviewed_commit` | e.g., `cf2866e...` | The stable code commit that was reviewed. |

### Commitment Logic

*   **`reviewed_commit`**: The SHA of the code *before* the review artifacts were added (or the SHA the reviews explicitly point to).
*   **Final Tag**: The SHA of the `main` branch *after* the manual release check passes. This commit will include the successful review artifacts.

## 5. Execution Example (v0.13)

To validate the v0.13 release:

1.  Go to **Actions** -> **ADM Quality Gate**.
2.  Click **Run workflow**.
3.  Branch: `main`.
4.  Inputs:
    *   `review_gate_mode`: `complete-set`
    *   `review_set_id`: `RSV-20260708-main-protection-ruleset`
    *   `target_ref`: `adm-v013-repository-governance`
    *   `reviewed_commit`: `cf2866eaf6cf772f6d9937f21b84e07fb6d9e648`
5.  Click **Run workflow**.

## 6. Tagging

Only if the manual run is **green**, proceed to tag the release:

```bash
git checkout main
git pull
git tag -a v0.13 -m "Release v0.13: Repository Governance"
git push origin v0.13
```

> [!IMPORTANT]
> Never set a Git tag before the manual `complete-set` release check has passed on `main`.
