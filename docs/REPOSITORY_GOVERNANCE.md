# Repository Governance

This document defines the repository-level safeguards that keep ADM changes reviewable, reproducible, and release-ready.

## 1. Protected branch

The default branch is `main`.

`main` is the canonical integration branch and must not be treated as a scratch branch, agent workspace, or direct-write target.

## 2. Required GitHub ruleset

The repository must keep an active branch ruleset for the default branch.

Expected ruleset:

```text
Name: main-protection
Enforcement: Active
Target: Default branch
Bypass list: empty
```

Required branch rules:

- Require a pull request before merging.
- Require conversation resolution before merging.
- Require status checks to pass before merging.
- Require the `ADM Quality Gate` status check from GitHub Actions.
- Require branches to be up to date before merging.
- Block force pushes.
- Restrict deletions.

Solo-maintainer repositories may keep required approvals at `0` while the repository is still in early ADM governance hardening. Raising approvals to `1` should happen only when a second real reviewer or a stable code-owner process exists.

## 3. No bypass by default

The default governance posture is that nobody is on the bypass list.

Adding a bypass entry weakens the rule and must be documented in an ADR or an equivalent governance decision before it is applied.

## 4. Merge path

The standard merge path is:

1. Create a non-`main` branch.
2. Commit the change on that branch.
3. Open a pull request against `main`.
4. Complete the PR template.
5. Let `ADM Quality Gate` pass.
6. Resolve all PR conversations.
7. Merge through GitHub.
8. Delete the feature branch after merge.

Direct changes to `main` are not an accepted workflow.

## 5. Required check identity

The required status check is:

```text
ADM Quality Gate
```

The expected source is GitHub Actions.

A check with the same name from another source must not be used as a substitute unless the repository governance documentation is updated first.

## 6. Release gate policy

A release-grade ADM change must satisfy all of the following before it is considered releasable:

- The change is merged through a pull request.
- `ADM Quality Gate` passed on the PR.
- The PR had no unresolved conversations at merge time.
- `CHANGELOG.md` documents the change when governance, validation behavior, or release process changed.
- A complete six-role ADM review set exists for release readiness, phase transitions, governance changes, architecture-critical changes, or security-, cost-, or performance-sensitive changes.
- Release-grade complete-set validation is run manually when a release or phase transition depends on a specific reviewed code commit. See [docs/RELEASE_RUNBOOK.md](file:///home/basti/projects/agentic-development-manifest/docs/RELEASE_RUNBOOK.md) for execution details.

The release gate is intentionally stricter than the normal PR gate. The normal PR gate prevents structurally invalid changes from entering `main`; the release gate proves that a specific ADM state has been reviewed as a complete unit.

## 7. Manual ruleset audit

GitHub repository rulesets are repository settings, not ordinary versioned source files. Therefore this repository documents the expected settings, but the settings themselves must be audited in GitHub.

Audit checklist:

- `main-protection` exists.
- Enforcement is `Active`.
- Target is the default branch.
- Bypass list is empty.
- Pull requests are required before merge.
- Conversation resolution is required.
- `ADM Quality Gate` is a required check.
- The required check source is GitHub Actions.
- Branches must be up to date before merging.
- Force pushes are blocked.
- Deletions are restricted.

If any item fails, the repository is not governance-complete, even if the source files look correct.
