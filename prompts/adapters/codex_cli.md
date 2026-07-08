# ADM Adapter Prompt — Codex CLI

Use this adapter when starting a Codex CLI session in an ADM-controlled repository.

## Canonical Dependency

This adapter does not replace ADM.

Before implementation, use `prompts/master_prompt.md` as the canonical onboarding prompt and preserve the authority order from `docs/MASTER_PROMPT_STANDARD.md` and `docs/ADAPTER_PROMPT_STANDARD.md`.

If this adapter conflicts with the canonical master prompt, the canonical master prompt wins.

## Tool-Specific Guidance

Codex CLI may be useful for:

- repository-aware reasoning,
- patch planning,
- controlled edits,
- terminal validation,
- review of diffs and tests,
- handover preparation.

Use Codex CLI as a controlled execution environment. Do not treat Codex-specific state as ADM project truth.

## Required Operating Rules

1. Start read-only until repository state and task scope are clear.
2. Use repository files, not hidden memory or prior chat state, to establish project truth.
3. State role, goal, affected files, exclusions, assumptions, risks, and planned next action before implementation.
4. Prefer explicit patch-sized changes over broad rewrites.
5. Keep command execution scoped to the task and report destructive or risky actions before running them.
6. Do not treat Codex cache, previous conversation state, local tool profile state, or generated plan state as authority.
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

The handover must clearly separate executed checks from planned checks and must not invent CI, review, approval, commit, or release state.

## Output Expectation

When reporting to the maintainer, state:

- what changed,
- why it changed,
- files changed,
- checks run and results,
- risks or deferred work,
- whether the branch is PR-ready or not.
