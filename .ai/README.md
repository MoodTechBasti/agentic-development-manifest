# ADM Runtime Artifact Policy

The `.ai/` directory is the repository-backed memory layer for ADM-compatible agent work.

It is not a generic scratch directory.

## Versioned artifacts

The following `.ai/` content may be committed when it is intentional, reviewable, non-sensitive, and relevant to project governance or future agent handover:

- `.ai/reviews/*.md` for completed runtime review artifacts
- `.ai/decisions/*.md` for project-specific runtime decisions
- `.ai/handover/*.md` for durable session handovers
- `.ai/memory/*.md` for curated durable memory notes
- `.ai/knowledge/*.md` for curated project knowledge or research summaries
- `.ai/tasks/*.md` for active or planned work state that must survive handover
- `.ai/README.md` for this policy

Runtime review artifacts must use their `review_id` as filename, for example:

```text
.ai/reviews/REV-SEC-20260708-auth-hardening.md
```

Do not use static role filenames such as `.ai/reviews/security.md` for completed runtime reviews.

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

Commit `.ai/` content only when a future agent or maintainer must be able to reconstruct a decision, review, handover, durable memory note, curated knowledge summary, or active task from git history.

Do not commit local exploration, tool noise, prompt experiments, raw logs, credentials, private paths, private URLs, sensitive local data, or temporary notes.