# ADM Review Runbook

This runbook describes the operational happy path for creating, validating, and eventually archiving ADM review sets.

## 1. When to use a complete review set

Use a six-role complete review set for:

- release readiness,
- phase transitions,
- governance changes,
- architecture-critical changes,
- security-, cost-, or performance-sensitive changes.

A v1 release candidate is release-readiness, phase-transition, and governance relevant. It therefore requires a fresh complete six-role review set for the v1-RC target state.

Do not reuse an older release review set as v1-RC proof. The v1-RC review artifacts must bind to the stable reviewed content commit with explicit `review_set_id`, `target_ref`, and `target_commit`.


Do not require a complete review set for every small feature branch. Use `advisory` or `existing-strict` there.

## 2. Current hardening baselines

### v0.24 Review and Validation Hardening

Roadmap Phase 6 starts from the existing review validation model instead of replacing it.

The accepted v0.24 baseline keeps these guardrails:

- Normal PRs to `main` use `existing-strict` and must not require all six reviews.
- Release-grade or phase-transition checks use `complete-set` with explicit scope.
- Stale review artifacts must not satisfy a newer scoped release gate.
- Manual release-grade validation must bind to the reviewed code commit, not merely the commit containing review artifacts.
- Workflow hardening, release automation, new schemas, or branch protection changes require a separate explicit ADR.

### v0.25 Foundation Consistency and Release Hygiene

v0.25 is a consolidation baseline, not Roadmap Phase 7.

The accepted v0.25 baseline keeps these guardrails:

- Review artifacts must point to the stable non-review commit they reviewed.
- The final release tag must point to the final `main` commit after review artifacts are merged and manual release validation has passed.
- Release runbook examples must stay generic enough that stale version-specific values are not copied blindly.
- Repository ruleset audit remains a manual external check before governance-relevant releases.
- Phase 7 handover/session-continuity work remains open until a later explicit PR and ADR.

### v0.26 Review Archive Policy

v0.26 defines the review archive boundary before any historical review migration.

The accepted v0.26 baseline keeps these guardrails:

- Direct `.ai/reviews/*.md` files are the active review validation area.
- Historical review sets may later move to `.ai/reviews/archive/<review_set_id>/` after their release or governance purpose is complete.
- Archived reviews remain repository-owned historical evidence.
- Normal validation against `.ai/reviews/` does not recursively validate archive subdirectories.
- v0.26 does not move historical review artifacts and does not change production validator logic.

## 3. Standard review roles

A complete ADM review set requires exactly one passing, CI-ready review for each role:

| Review type | Runtime prefix |
| --- | --- |
| `architect` | `REV-ARCH` |
| `security` | `REV-SEC` |
| `performance` | `REV-PERF` |
| `cost` | `REV-COST` |
| `simplifier` | `REV-SIMP` |
| `documentation` | `REV-DOC` |

## 4. Repository merge precondition

Before a governance, release, or phase-transition PR is considered merge-ready, the repository settings must match `docs/REPOSITORY_GOVERNANCE.md`.

Minimum required state:

- `main-protection` exists and is active.
- The target is the default branch.
- The bypass list is empty.
- Pull requests are required before merging.
- Conversation resolution is required before merging.
- `ADM Quality Gate` is required from GitHub Actions.
- Branches must be up to date before merging.
- Force pushes are blocked.
- Deletions are restricted.

These settings live in GitHub, not in source control. They must be manually audited when repository governance is changed or when a governance-relevant release claims release readiness.

The audit result must be stated in the PR body, release note, or maintainer release checklist when it is release-relevant. Do not claim source files prove the active GitHub settings.

## 5. Happy path

### Step 1: Commit the content under review

Finish the code, documentation, or governance change first.

Record the stable content-under-review SHA:

```bash
git rev-parse HEAD
```

This value becomes `target_commit`.

### Step 2: Choose review scope

Choose one set ID and one target reference.

Example:

```text
review_set_id: RSV-YYYYMMDD-release-slug
target_ref: adm-v026-review-archive-policy
target_commit: <stable-non-review-sha>
```

Use the branch or ref where the reviewed content existed. Do not change `target_ref` merely to make an old review set pass.

### Step 3: Create runtime review files

Copy the six templates from `templates/reviews/` into `.ai/reviews/` and rename each file by its runtime `review_id`.

Example filenames:

```text
.ai/reviews/REV-ARCH-YYYYMMDD-release-slug.md
.ai/reviews/REV-SEC-YYYYMMDD-release-slug.md
.ai/reviews/REV-PERF-YYYYMMDD-release-slug.md
.ai/reviews/REV-COST-YYYYMMDD-release-slug.md
.ai/reviews/REV-SIMP-YYYYMMDD-release-slug.md
.ai/reviews/REV-DOC-YYYYMMDD-release-slug.md
```

Do not use static runtime names such as `.ai/reviews/architect.md`.

### Step 4: Fill required frontmatter

All six files must share the same:

- `review_set_id`,
- `target_ref`,
- `target_commit`.

Each file must also have:

```yaml
review_status: PASSED
ci_ready: true
```

for release-grade complete-set validation.

### Step 5: Validate locally

Validate existing review artifacts:

```bash
python3 scripts/validate_reviews.py --path . --mode existing-strict
```

Validate a complete set:

```bash
python3 scripts/validate_reviews.py \
  --path . \
  --mode complete-set \
  --review-set-id RSV-YYYYMMDD-release-slug \
  --target-ref adm-v026-review-archive-policy \
  --target-commit <stable-non-review-sha>
```

### Step 6: Open the PR

The normal PR workflow runs `existing-strict`. It proves that existing runtime review artifacts are structurally valid.

For governance PRs, the PR description must also state whether `docs/REPOSITORY_GOVERNANCE.md` still matches the active GitHub ruleset, or explicitly state that the ruleset audit was not performed in the agent environment.

### Step 7: Run release-grade validation manually after merge

After merge, run the GitHub workflow manually:

1. Open **Actions**.
2. Select **ADM Quality Gate**.
3. Click **Run workflow**.
4. Select branch `main`.
5. Set `review_gate_mode` to `complete-set`.
6. Provide the `review_set_id`.
7. Provide the `target_ref` used in the artifacts.
8. Provide the `reviewed_commit` stable SHA.
9. Run the workflow.

The workflow should print the selected mode, target ref, and reviewed code commit before running the validator.

## 6. Review archive path

After a release or governance decision is complete, historical review sets may later be archived under:

```text
.ai/reviews/archive/<review_set_id>/
```

Archive migration is not automatic and must be done in a separate explicit PR.

Do not move the review set that is still being used for current release-grade validation. Archive only after the release or governance evidence is complete and recoverable from the repository history.

Archived review files keep their original review metadata. Do not retarget archived reviews to a newer branch, newer commit, or newer release.

## 7. Common failures

### Missing role

Cause: one of the six required review types is missing.

Fix: add the missing runtime review artifact.

### Duplicate role

Cause: two files in the same review set declare the same `review_type`.

Fix: keep exactly one file per role for the review set.

### Mismatched review_set_id

Cause: one file belongs to a different set.

Fix: align all six files to the same `review_set_id`.

### Mismatched target_commit

Cause: one review points to a different reviewed code commit.

Fix: verify the actual content-under-review SHA and align all six files.

### Stale review set

Cause: old reviews exist but do not match the requested `review_set_id`, `target_ref`, or `target_commit`.

Fix: create or select the correct scoped review set for the current target. Do not weaken the scope filter to make stale reviews pass.

### Archived review set unexpectedly ignored

Cause: archived reviews live under `.ai/reviews/archive/**`, while normal validation reads direct `.ai/reviews/*.md` files only.

Fix: keep the current active review set directly under `.ai/reviews/`. Use archive paths only for historical sets whose release or governance purpose is complete.

### PASSED with ci_ready false

Cause: the review says it passed but is not CI-ready.

Fix: either set `ci_ready: true` after the review is complete, or change `review_status` to `PENDING`, `FAILED`, or `NEEDS_REVISION`.

### Invalid review_id

Cause: the review ID does not match the required prefix and date pattern.

Fix: use the correct prefix, date, and slug, for example `REV-SEC-20260708-auth-hardening`.

### Ruleset audit claimed without evidence

Cause: documentation or a PR claims repository governance readiness, but no manual GitHub ruleset audit evidence is provided.

Fix: perform the audit in GitHub settings or state clearly that it was not performed by the agent.

## 8. Validator fixture tests

Run the validator fixture test suite with:

```bash
python3 scripts/test_validate_reviews.py
```

The test suite covers both the happy path and expected failure modes for malformed, incomplete, duplicate, mismatched, stale scoped review sets, and archived review subdirectories ignored by the standard validator path.
