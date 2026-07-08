# ADR-20260708: Main Protection Ruleset

## Status

Accepted

## Context

ADM now has a quality gate, review validator, validator fixture tests, review templates, runtime review artifacts, a review runbook, a pull request template, and repository hygiene documentation.

Those source-level controls are not sufficient if `main` can still be changed directly, force-pushed, or deleted.

## Decision

Protect the default branch with a GitHub ruleset named `main-protection`.

The expected state is:

- Enforcement is active.
- The target is the default branch.
- The bypass list is empty.
- Pull requests are required before merging.
- Conversation resolution is required before merging.
- `ADM Quality Gate` is a required status check from GitHub Actions.
- Branches must be up to date before merging.
- Force pushes are blocked.
- Deletions are restricted.

Required approvals may remain `0` while the repository is a solo-maintainer repository. This avoids blocking the maintainer while still preventing direct writes to `main`.

## Consequences

- `main` becomes an integration branch, not an agent workspace.
- All normal changes must flow through pull requests.
- The PR template and `ADM Quality Gate` become part of the enforceable merge path.
- Repository settings must be audited manually because GitHub rulesets are not committed source files.
- Raising required approvals to `1` remains a future hardening step once a second real reviewer or CODEOWNERS process exists.

## Related documentation

- `docs/REPOSITORY_GOVERNANCE.md`
- `docs/REVIEW_RUNBOOK.md`
- `.github/pull_request_template.md`
