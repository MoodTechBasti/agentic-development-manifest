# ADM Runtime Artifact Policy

The `.ai/` directory is the repository-backed memory layer for ADM-compatible agent work.

It is not a generic scratch directory.

## Versioned artifacts

The following `.ai/` content may be committed when it is intentional, reviewable, and relevant to project governance:

- `.ai/reviews/*.md` for completed runtime review artifacts
- `.ai/decisions/*.md` for project-specific decisions
- `.ai/handover/*.md` for durable session handovers
- `.ai/README.md` for this policy

Runtime review artifacts must use their `review_id` as filename, for example:

```text
.ai/reviews/REV-SEC-20260708-auth-hardening.md
```

Do not use static role filenames such as `.ai/reviews/security.md` for completed runtime reviews.

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

Commit `.ai/` content only when a future agent or maintainer must be able to reconstruct a decision, review, or handover from git history.

Do not commit local exploration, tool noise, prompt experiments, raw logs, credentials, private paths, or temporary notes.
