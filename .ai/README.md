# ADM Runtime Artifact Policy

The `.ai/` directory is the repository-backed memory layer for ADM-compatible agent work.

It is not a generic scratch directory.

## Versioned artifacts

The following `.ai/` content may be committed when it is intentional, reviewable, non-sensitive, and relevant to project governance or future agent handover:

- `.ai/reviews/*.md` for completed runtime review artifacts in the active review area
- `.ai/reviews/archive/<review_set_id>/*.md` for archived historical review artifacts after their release or governance purpose is complete
- `.ai/decisions/*.md` for project-specific runtime decisions
- `.ai/handover/*.md` for durable session handovers
- `.ai/handover/README.md` for the Session Continuity discovery and commit policy
- `.ai/memory/*.md` for curated durable memory notes
- `.ai/knowledge/*.md` for curated project knowledge or research summaries
- `.ai/tasks/*.md` for active or planned work state that must survive handover
- `.ai/agents/*.md` or `.ai/agents/*.yml` for repository-owned agent role definitions and registry metadata
- `.ai/README.md` for this policy

Runtime review artifacts must use their `review_id` as filename, for example:

```text
.ai/reviews/REV-SEC-20260708-auth-hardening.md
```

Do not use static role filenames such as `.ai/reviews/security.md` for completed runtime reviews.

## Review archive policy

Direct files under `.ai/reviews/` are the active review validation area.

Historical review sets may later be moved to:

```text
.ai/reviews/archive/<review_set_id>/
```

Archive directories preserve historical review evidence. They are not scratch space and must not be used to hide malformed current reviews.

Archived review files should keep their original frontmatter unless a later accepted ADR defines explicit migration metadata. Their `review_set_id`, `target_ref`, `target_commit`, review vote, and CI-readiness fields remain historical truth.

The standard review validator path validates direct `.ai/reviews/*.md` files only. It does not recursively validate `.ai/reviews/archive/**` during normal `existing-strict` or `complete-set` runs against `.ai/reviews/`.

v0.26 defines this policy. v0.27 migrates completed historical review sets up to v0.25 into the archive path. v0.30 migrates completed v0.26, v0.27, and v0.28 review sets into the archive path while keeping current v0.29 release evidence active under `.ai/reviews/`.

## Agent Registry

The Agent Registry under `.ai/agents/` describes durable agent roles, responsibility boundaries, required reading context, expected write areas, and handover routing.

Agent Registry files are not:

- local tool profiles
- permission sandboxes
- hidden model-memory exports
- vendor-specific assistant settings

Use `.ai/agents/README.md` to document the registry policy. Future projects may add `registry.md`, `registry.yml`, or role-specific files when the role model needs more structure.

## Handover Automation and Session Continuity

Structured handovers under `.ai/handover/` may be committed when they describe meaningful session state for future agents.

Handover Automation may later prefill, lint, or validate handover structure, but it must not invent:

- checks or command results
- CI status
- review votes
- commit SHAs
- registry roles
- approvals
- completed work

Session Continuity defines how future agents consume durable handover evidence before implementation.

Concrete handovers should use `templates/HANDOVER_TEMPLATE.md`, follow `.ai/handover/README.md`, keep repository-relative paths, and record missing checks as `NOT RUN` instead of pretending they passed.

When the latest handover is missing, stale, malformed, or ambiguous, agents must report `UNKNOWN` or `AMBIGUOUS` instead of reconstructing project state from chat history, hidden model memory, local scratch files, raw logs, local tool profiles, or tool caches.

A handover `Continuity status` is not approval, CI truth, review approval, merge readiness, release readiness, or tag permission.

## Project-owned memory

Project-owned memory is durable project knowledge owned by the repository, not by a model, chat window, local workstation, or vendor-specific tool profile.

A memory file must be:

- curated, not raw output
- concise enough for future agents to scan
- explicit about uncertainty or freshness limits
- repository-relative when it references files
- safe to commit to the repository

Do not commit hidden model-memory dumps, raw chat transcripts, raw research dumps, prompt experiments, local tool logs, machine-specific paths, or personal notes that do not affect future project execution.

## Decision location rule

Use `docs/decisions/` for ADM standard architecture decisions.

Use `.ai/decisions/` for project-specific runtime decisions made inside an ADM-controlled repository.

## Ignored local artifacts

The following local agent output is transient and must not be committed:

- `.ai/tmp/`
- `.ai/temp/`
- `.ai/scratch/`
- `.ai/logs/`
- `.ai/cache/`
- `.ai/local/`
- `.ai/workspace/`
- `.ai/sessions/`
- `.ai/transient/`
- `*.scratch.md`

## Rule of thumb

Commit `.ai/` content only when a future agent or maintainer must be able to reconstruct a decision, review, handover, durable memory note, curated knowledge summary, active task, or durable agent role from git history.

Do not commit local exploration, tool noise, prompt experiments, raw logs, credentials, private paths, private URLs, sensitive local data, or temporary notes.
