# ADM Adapter Prompt — Claude Code CLI

Use this adapter when starting a Claude Code CLI session in an ADM-controlled repository.

## Canonical Dependency

This adapter does not replace ADM.

Before implementation, use `prompts/master_prompt.md` as the canonical onboarding prompt and preserve the authority order from `docs/MASTER_PROMPT_STANDARD.md` and `docs/ADAPTER_PROMPT_STANDARD.md`.

If this adapter conflicts with the canonical master prompt, the canonical master prompt wins.

## Tool-Specific Guidance

Claude Code CLI may be useful for:

- repository inspection,
- planning,
- controlled file edits,
- local command execution,
- test and validation loops,
- summarizing diffs and handovers.

Use those capabilities as execution aids only. They are not approval, review, CI truth, or release authority.

## Required Operating Rules

1. Start read-only until scope is understood.
2. Read the canonical ADM files required by `prompts/master_prompt.md`.
3. State role, goal, affected areas, exclusions, assumptions, risks, and next action before implementation.
4. Keep edits small and reviewable.
5. Use Claude-specific planning or loop features only when they preserve ADM gates.
6. Do not treat Claude memory, chat history, prior session context, local cache, slash-command state, or tool profile state as repository truth.
7. Do not create branches, commits, PRs, tags, workflow changes, validator changes, MCP integrations, or local tool profiles unless explicitly in scope.

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

The handover must not invent checks, commits, CI results, review votes, roles, approvals, or completed work.

## Output Expectation

When reporting to the maintainer, state:

- what changed,
- why it changed,
- files changed,
- checks run and results,
- risks or deferred work,
- whether the branch is PR-ready or not.
