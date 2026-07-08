# ADM Adapter Prompts

This directory contains tool-specific adapter prompts for ADM-controlled repositories.

Adapter prompts are downstream from:

1. `spec/ADM_v1_DRAFT.md`
2. `docs/MASTER_PROMPT_STANDARD.md`
3. `docs/ADAPTER_PROMPT_STANDARD.md`
4. `prompts/master_prompt.md`
5. accepted ADRs and governance documents
6. `docs/RELEASE_RUNBOOK.md` and release-hygiene rules when release claims are made

## Rule

Use an adapter prompt only after accepting the canonical ADM master prompt as authoritative.

An adapter may explain how to operate a specific CLI tool. It must not weaken ADM authority order, initialization, scope declaration, ADR rules, review validation, CI evidence, PR hygiene, release hygiene, or handover duties.

## Initial Adapter Set

| File | Purpose |
| --- | --- |
| `claude_code_cli.md` | Adapter for Claude Code CLI sessions. |
| `codex_cli.md` | Adapter for Codex CLI sessions. |
| `generic_cli_agent.md` | Fallback adapter for unknown or future CLI agents. |

Gemini CLI and Antigravity CLI are deferred candidates after v0.25. They are not accepted adapter prompts until a later explicit PR verifies current tool behavior and adds them.

## Forbidden Content

Do not store:

- secrets,
- tokens,
- provider credentials,
- private local paths,
- private URLs,
- raw logs,
- hidden memory exports,
- tool cache dumps,
- machine-specific profile files.

Tool-specific local configuration belongs outside this standard unless a later ADR explicitly accepts it.
