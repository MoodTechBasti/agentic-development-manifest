# ADR-20260708: Manual Release Validation Supports Explicit Target Reference

*   **Status**: Accepted
*   **Deciders**: Principal Architect, Security Engineer, SRE, Cost Engineer, Simplifier, Documentation Lead
*   **Date**: 2026-07-08

## Context

The ADM Quality Gate workflow uses `target_ref` to bind review artifacts to a specific branch or pull request. In automated runs (push/PR), `target_ref` is inferred from the environment. However, when performing a manual release-grade `complete-set` validation on the `main` branch after a merge, the inferred `target_ref` (e.g., `main`) often mismatches the `target_ref` stored in the review artifacts (e.g., a feature branch). This mismatch blocks the release gate even when the code is identical.

## Decision

We will extend the `workflow_dispatch` trigger in `.github/workflows/adm-quality-gate.yml` to support an optional, explicit `target_ref` input.

1.  A new optional input `target_ref` is added to the manual trigger.
2.  If provided, this input overrides the automatically inferred reference.
3.  The shell logic in the workflow is updated to respect this override during manual runs.
4.  Standard push and pull request triggers remain unchanged in their inference behavior.

## Consequences

*   **Auditability**: Release checks become more precise by allowing an explicit binding to the reviewed reference.
*   **Developer Experience**: Manual validation on `main` no longer requires updating artifact frontmatter after merging.
*   **Governance**: The separation between `reviewed_commit` (code-under-review) and the final release tag (integration-complete) is maintained and clarified in the documentation.
*   **Safety**: Standard automated gates are not affected by this change.
