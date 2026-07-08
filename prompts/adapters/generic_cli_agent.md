# ADM Adapter Prompt — Generic CLI Agent

Use this adapter when a concrete CLI agent has no accepted ADM-specific adapter prompt.

## Canonical Dependency

This adapter does not replace ADM.

Before implementation, use `prompts/master_prompt.md` as the canonical onboarding prompt and preserve the authority order from `docs/MASTER_PROMPT_STANDARD.md` and `docs/ADAPTER_PROMPT_STANDARD.md`.

If this adapter conflicts with the canonical master prompt, the canonical master prompt wins.

## Generic CLI Assumptions

The agent may be able to:

- read repository files,
- inspect diffs,
- edit files,
- run terminal commands,
- summarize work.

If any capability is unavailable, state the limitation and continue with the smallest safe repository-backed workflow.

## Required Operating Rules

1. Start read-only until task scope is clear.
2. Do not rely on hidden model memory, chat history, local cache, local profiles, prior session state, or tool-specific context as repository truth.
3. Read the canonical ADM files required by `prompts/master_prompt.md`.
4. State role, goal, affected areas, exclusions, assumptions, risks, and next action before implementation.
5. Keep edits small and repository-relative.
6. Report every unverified fact as uncertain instead of reconstructing it from memory.
7. Do not create branches, commits, PRs, tags, workflow changes, validator changes, provider integrations, or local tool profiles unless explicitly in scope.

## Quality Gate Handling

Before PR-ready or complete claims, report actual evidence for:

```bash
python3 scripts/check_limits.py --path . --max-lines 300
python3 scripts/test_validate_reviews.py
python3 scripts/validate_reviews.py --path . --mode existing-strict
```

For governance changes, roadmap phase transitions, or releases, also use complete-set validation with the active `review_set_id`, `target_ref`, and stable `target_commit`.

Unrun checks must be reported as `NOT RUN`.

## Handover Handling

For significant sessions, create or update a repository-owned handover using `templates/HANDOVER_TEMPLATE.md`.

The handover must be evidence-based and repository-relative.

## Output Expectation

When reporting to the maintainer, state:

- what changed,
- why it changed,
- files changed,
- checks run and results,
- risks or deferred work,
- whether the branch is PR-ready or not.
