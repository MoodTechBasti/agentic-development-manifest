# ADM Handover Continuity Policy

The `.ai/handover/` directory stores durable session handovers for ADM-compatible work.

It is a session-continuity layer, not a scratch directory, chat archive, approval system, CI source, or runtime automation surface.

## Purpose

A future agent should be able to answer these questions from repository-owned evidence:

1. What was the last meaningful session state?
2. Which task can be continued?
3. Which checks were actually run?
4. Which files changed?
5. Which reviews, refs, commits, and risks matter?
6. Which role should continue the work?

## File naming

Durable handovers should use this filename pattern:

```text
Handoff-YYYYMMDD-HHMM-<short-scope>.md
```

Examples:

```text
Handoff-20260708-1530-session-continuity-baseline.md
Handoff-20260708-1800-review-validation-followup.md
```

Use repository-relevant slugs. Do not include private names, local machine names, secrets, ticket URLs, or raw chat markers in filenames.

## Required metadata

Each durable handover should include these header fields:

```text
Session ID:
Timestamp:
Outgoing agent:
Active registry role:
Target recipient:
Continuity status:
Target ref:
Target commit:
Review set id:
Latest repo evidence checked:
```

`Continuity status` must be one of:

| Status | Meaning |
| --- | --- |
| `READY` | Enough repository evidence exists for the next agent to continue the stated next task. |
| `PARTIAL` | Some evidence exists, but missing checks, scope, or state must be verified first. |
| `BLOCKED` | A named blocker prevents continuation. |
| `UNKNOWN` | The handover cannot establish reliable continuation state. |

`READY` is not approval. It does not mean CI passed, reviews passed, the PR is mergeable, a release is valid, or a tag may be created.

## Latest handover discovery

When an agent needs the latest handover, it must use repository evidence:

1. Prefer explicit `Timestamp:` values inside handover files.
2. Use filename timestamps only when internal timestamps are missing or equal.
3. If timestamps conflict, are malformed, or point to multiple plausible latest files, report `AMBIGUOUS`.
4. If no relevant handover exists, report `UNKNOWN`.
5. Do not reconstruct latest state from chat history, hidden model memory, local scratch files, raw logs, local tool profiles, or tool caches.

A stale handover may still be useful evidence, but it must be reported as stale when newer repository evidence contradicts it.

## Evidence rules

Handovers must use repository-relative paths.

Allowed evidence examples:

- git branch, ref, commit, or diff evidence,
- changed repository paths,
- check commands and actual results,
- cited CI run or workflow result,
- review artifact IDs, `review_set_id`, `target_ref`, and `target_commit`,
- accepted ADRs and canonical docs,
- active `.ai/tasks/` or curated `.ai/memory/` files.

Forbidden evidence examples:

- raw chat transcripts,
- hidden model-memory dumps,
- raw local logs,
- private local paths,
- private URLs,
- credentials, tokens, secrets,
- uncited CI claims,
- guessed review votes,
- invented commit SHAs or roles.

## Checks and unknowns

Do not mark a check as passed unless it was actually run or proven by a cited CI run.

Use:

- `PASSED` only for executed or cited successful checks,
- `FAILED` for executed failed checks,
- `NOT RUN` for checks that were not executed,
- `UNKNOWN` when the result cannot be established from repository evidence,
- `N/A` only when the check is genuinely not applicable.

## Agent Registry routing

If a handover references a registry role, that role must exist in `.ai/agents/` or the handover must document the role gap as an open question.

Do not invent roles to make routing look complete.

## Commit policy

Commit `.ai/handover/*.md` only when a future agent or maintainer needs the handover to reconstruct session state.

Do not commit low-value session notes, transient scratch output, raw logs, or prompt experiments.

## Relationship to automation

Future automation may prefill, lint, or cross-check handovers only within the boundaries accepted by ADR-20260708-handover-automation and ADR-20260708-session-continuity-baseline.

Automation must not approve work, invent evidence, mark checks passed, create release tags, merge PRs, or mutate branch protection.
