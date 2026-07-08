# ADM Release Runbook

This runbook describes the process for validating and executing an ADM release.

## 1. What is an ADM Release?

An ADM release is a repository state that has been formally reviewed by all six mandatory ADM roles and has passed release-grade `complete-set` validation.

A release is marked by an annotated Git tag, for example `v0.31`.

## 2. Release Prerequisites

Before a release can be tagged:

1. All release-scope changes must be merged into `main` via pull requests.
2. `ADM Quality Gate` must have passed on the PR or PRs.
3. All PR conversations must be resolved.
4. `CHANGELOG.md` must describe the release.
5. A complete six-role ADM review set must exist under `.ai/reviews/` for the stable reviewed state.
6. The active GitHub ruleset state must be manually audited when the release is governance-, validation-, or release-process relevant.
7. Release-grade `complete-set` validation must pass on the final `main` state before tag creation.
8. The release record must state which evidence path was used: GitHub manual workflow, local terminal validation, or both.

## 3. Normal PR Gate vs. Release Gate

- **Normal PR Gate (`existing-strict`)**: Runs automatically on PRs. It ensures that existing runtime review artifacts are structurally valid. It does not require all six reviews for every ordinary PR.
- **Release Gate (`complete-set`)**: Run before a release. It ensures that a specific `review_set_id` contains all six mandatory reviews, all `PASSED`, all `ci_ready`, and all bound to the same `target_ref` and `target_commit`.

## 4. Commit and Tag Semantics

ADM distinguishes the reviewed content commit from the final release tag commit.

- **Stable reviewed commit**: the non-review commit that contains the code, documentation, or governance state being reviewed.
- **Review artifact commit**: the later commit or commits that add the six `.ai/reviews/` files pointing to the stable reviewed commit.
- **Final release tag**: the final `main` commit after the review artifacts are merged and release-grade validation has passed.

The tag must point to the final `main` commit that includes the review artifacts. The reviews themselves must keep `target_commit` set to the stable reviewed commit.

## 5. Release Evidence Paths

ADM recognizes two evidence paths for release-grade validation:

1. **GitHub manual workflow evidence**: trigger `ADM Quality Gate` through `workflow_dispatch` on `main` with `review_gate_mode: complete-set` and the exact release scope.
2. **Local terminal evidence**: run the equivalent release-grade commands from a clean local checkout of `main` and record the exact command output.

For governance-, validation-, or release-process relevant releases, GitHub manual workflow evidence is the preferred release evidence because it is repository-hosted and easier to audit later.

Local terminal evidence may be used as an additional or fallback signal, but it must be labeled as local evidence. Do not describe local validation as a GitHub manual workflow run.

If a required evidence path is not run, the release record must say `NOT RUN` and explain why.

## 6. Standard Release Flow

1. Merge the release PR into `main`.
2. Pull or fetch the final `main` state locally.
3. Identify the stable reviewed commit named by the review artifacts.
4. Manually audit the active GitHub ruleset if the release is governance-relevant.
5. Run release-grade `complete-set` validation on `main` using at least one documented evidence path.
6. Prefer triggering `ADM Quality Gate` manually on `main` for governance-, validation-, and release-process releases.
7. Use `review_gate_mode: complete-set`.
8. Provide the exact `review_set_id`, `target_ref`, and `reviewed_commit`.
9. Wait for the release-grade validation to pass.
10. Create and push the annotated release tag on the final `main` commit.

## 7. Manual GitHub Release Validation Inputs

Trigger the `ADM Quality Gate` workflow manually on the `main` branch.

| Parameter | Value | Description |
| --- | --- | --- |
| `review_gate_mode` | `complete-set` | Hardens the check to require all six roles. |
| `review_set_id` | e.g., `RSV-YYYYMMDD-release-slug` | The review set to validate. |
| `target_ref` | e.g., `adm-v031-foundation-hygiene-cleanup` | The branch or reference used inside the review artifacts. |
| `reviewed_commit` | e.g., `<stable-non-review-sha>` | The stable code or documentation commit that was reviewed. |

## 8. Local Release Validation Commands

Use current release values, not stale values copied from older examples.

```bash
python3 scripts/check_limits.py --path . --max-lines 300
python3 scripts/test_validate_reviews.py
python3 scripts/validate_reviews.py --path . --mode existing-strict
python3 scripts/validate_reviews.py \
  --path . \
  --mode complete-set \
  --review-set-id RSV-YYYYMMDD-release-slug \
  --target-ref <release-branch-or-reviewed-ref> \
  --target-commit <stable-non-review-sha>
```

## 9. Evidence Record Template

Record release evidence explicitly:

```text
GitHub PR Quality Gate: PASSED | FAILED | NOT RUN
GitHub manual release workflow: PASSED | FAILED | NOT RUN
Local release validation: PASSED | FAILED | NOT RUN
Ruleset audit: PASSED | FAILED | NOT RUN
Review set ID: RSV-YYYYMMDD-release-slug
Target ref: <release-branch-or-reviewed-ref>
Stable reviewed commit: <stable-non-review-sha>
Final tag commit: <final-main-sha>
```

## 10. Tagging

Only if release-grade validation is green, tag the final `main` commit:

```bash
git switch main
git pull --ff-only origin main
git tag -a vX.Y -m "ADM vX.Y <release summary>"
git push origin vX.Y
```

> [!IMPORTANT]
> Never set a Git tag before release-grade `complete-set` validation has passed on `main` and the evidence path has been recorded without ambiguity.
