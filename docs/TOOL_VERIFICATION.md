# ADM — Tool Verification

> Origin: accepted in v0.29 as Roadmap Phase 8
> Current sync: v0.29 Tool Verification Discovery Baseline
> Scope: discovery and governance gate for deferred or future adapter prompts, not adapter implementation

Tool Verification defines what ADM must know before a deferred or future CLI tool can receive a dedicated adapter prompt.

It is a governance and discovery baseline. It is not a runtime integration, provider SDK, MCP server, local tool profile, workflow, validator, release automation, or acceptance of a new adapter.

## 1. Purpose

Tool-specific adapter prompts are allowed only when their behavior is based on current, reviewable evidence.

Tool Verification prevents agents from creating adapters from:

- chat memory,
- hidden model memory,
- outdated tool assumptions,
- marketing descriptions,
- local profiles,
- tool cache,
- raw experiments that cannot be reviewed,
- unsupported claims about CLI behavior.

## 2. Authority Order

Tool Verification sits below canonical ADM standards and above future adapter acceptance.

Authority order:

1. `spec/ADM_v1_DRAFT.md`, `docs/CONSTITUTION.md`, `ROADMAP.md`, governance docs, release docs, foundation standards, Master Prompt Standard, Adapter Prompt Standard, and accepted ADRs.
2. `prompts/master_prompt.md`.
3. This Tool Verification policy.
4. Versioned runtime artifacts such as `.ai/reviews/`, `.ai/handover/`, `.ai/decisions/`, and `.ai/agents/`.
5. Future tool-specific adapter prompts, only after explicit acceptance.
6. Local transient notes as non-authoritative working evidence.
7. Chat history, hidden model memory, tool cache, local profiles, and vendor-owned state: never authoritative project truth.

## 3. Verification Scope

A tool-verification note or future adapter proposal must describe the current behavior of the tool being considered.

Minimum fields:

| Field | Requirement |
| --- | --- |
| Tool identity | Name, version or current release reference, verification date, and execution environment. |
| Instruction model | How the tool accepts system, project, repository, or session instructions. |
| Repository access | How the tool reads files, discovers project state, and handles missing or ambiguous evidence. |
| Planning behavior | Whether the tool supports plan mode, approval checkpoints, task decomposition, or equivalent controls. |
| Edit behavior | How edits are proposed, applied, diffed, reverted, and scoped to small reviewable changes. |
| Command behavior | Whether shell commands can run, how approval works, and how failures are reported. |
| Review behavior | Whether the tool can review diffs, preserve review metadata, and avoid invented check or CI claims. |
| Tool state | What memory, cache, profile, IDE state, or vendor state exists and why it is not repository truth. |
| Governance risks | Known risks around ADM authority, branch rules, validation, reviews, handovers, releases, and evidence. |
| Generic fallback | Whether `prompts/adapters/generic_cli_agent.md` remains sufficient. |

## 4. Evidence Rules

Tool Verification evidence must be:

- current enough for the proposed adapter PR,
- repository-relative where paths are needed,
- concise,
- non-sensitive,
- reviewable by a human maintainer,
- explicit about unknowns and uncertainty.

Tool Verification evidence must not include:

- secrets,
- tokens,
- provider credentials,
- private URLs,
- private local paths,
- raw logs,
- hidden memory exports,
- tool cache dumps,
- proprietary internal dumps,
- machine-specific profile files.

If current tool behavior cannot be verified without leaking unsafe information, the tool remains deferred.

## 5. Adapter Eligibility

Tool Verification is not adapter approval.

A future adapter PR becomes eligible only when it can show:

1. current Tool Verification evidence,
2. a clear reason why the Generic CLI Agent adapter is insufficient,
3. a thin adapter scope below `prompts/master_prompt.md`,
4. no runtime, SDK, MCP, workflow, validator, or local-profile dependency,
5. documentation synchronization,
6. review evidence appropriate to the governance impact.

Even after verification, ADM may still reject a dedicated adapter if the tool can be covered safely by the Generic CLI Agent adapter.

## 6. Deferred Candidates

Gemini CLI and Antigravity CLI remain deferred candidates after v0.29.

They are not accepted adapter prompts.

They must not be treated as:

- implemented,
- approved,
- release-ready,
- equivalent to Claude Code CLI, Codex CLI, or Generic CLI Agent,
- verified by chat history or hidden model memory.

## 7. Non-goals

Tool Verification does not introduce:

- Gemini CLI adapter,
- Antigravity CLI adapter,
- any other new adapter,
- runtime code,
- provider SDKs,
- MCP integration,
- local tool profiles,
- workflow changes,
- validator changes,
- release automation,
- Handover linter,
- branch-protection changes,
- Review Archive Migration,
- Roadmap Phase 9 implementation,
- v1 release-candidate claims.

## 8. Final Audit

Before proposing a future adapter, verify:

- tool behavior is current and documented,
- the Generic CLI Agent adapter is insufficient,
- hidden tool state is not treated as repository truth,
- the adapter would remain thin and downstream from the canonical master prompt,
- ADM governance, CI, review validation, ADRs, PR hygiene, release hygiene, and handover duties remain intact,
- README, Roadmap, Changelog, Specification, Operating System, Master Prompt Standard, Adapter Prompt Standard, and adapter README are synchronized.
