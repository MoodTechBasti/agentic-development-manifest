# ADR-20260708-tool-verification-discovery-baseline

> ID: ADR-20260708-tool-verification-discovery-baseline
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `ROADMAP.md`, `README.md`, `CHANGELOG.md`, `spec/ADM_v1_DRAFT.md`, `docs/OPERATING_SYSTEM.md`, `docs/TOOL_VERIFICATION.md`, `docs/ADAPTER_PROMPT_STANDARD.md`, `docs/MASTER_PROMPT_STANDARD.md`, `prompts/master_prompt.md`, `prompts/adapters/README.md` |
| New dependencies | no |
| Security review | PASSED via `RSV-20260708-tool-verification-discovery-baseline` |
| Cost review | PASSED via `RSV-20260708-tool-verification-discovery-baseline` |
| Performance review | PASSED via `RSV-20260708-tool-verification-discovery-baseline` |

## 1. Context and Reason

Roadmap Phase 8 covers Adapter Expansion and Tool Verification.

ADM already accepts the Adapter Prompt Standard and the initial adapter set for Claude Code CLI, Codex CLI, and Generic CLI Agent. Gemini CLI and Antigravity CLI remain deferred candidates because their current tool behavior has not yet been explicitly verified.

The remaining Phase 8 gap is not adapter implementation. The gap is a governance baseline that defines what must be known before a future tool-specific adapter can be proposed.

Without a Tool Verification Discovery Baseline, agents can prematurely create Gemini CLI, Antigravity CLI, IDE, MCP, or provider-specific adapter prompts based on assumptions, old memory, marketing claims, local profiles, or unreviewed tool experiments.

That would weaken ADM's core rule: adapter prompts may specialize operation, but they must stay thin, downstream from the canonical master prompt, and free from runtime or provider lock-in.

## 2. Decision

ADM accepts v0.29 as the Roadmap Phase 8 Tool Verification Discovery Baseline.

Tool Verification is now a required discovery and governance gate before any deferred or future CLI tool receives a dedicated ADM adapter prompt.

This baseline defines:

1. what must be verified before a future adapter PR is eligible,
2. how deferred adapter candidates remain non-accepted until verification and explicit approval,
3. how tool capability must be separated from tool state,
4. how adapter work remains downstream from `prompts/master_prompt.md`,
5. which implementation work remains out of scope for v0.29.

The canonical operational policy is documented in `docs/TOOL_VERIFICATION.md`.

## 3. Required Tool Verification Evidence

A future adapter PR may be considered only after current tool behavior has been documented from repository-reviewable evidence.

Minimum evidence:

| Area | Required evidence |
| --- | --- |
| Tool identity | Tool name, tested version or current release reference, execution environment, and date of verification. |
| Initialization behavior | How the tool starts, accepts system/project instructions, loads files, and handles repository context. |
| Planning behavior | Whether the tool has plan mode, task planning, approval gates, or equivalent interaction patterns. |
| File and diff behavior | How it reads files, proposes edits, writes files, shows diffs, and avoids unintended broad changes. |
| Command behavior | Whether and how it executes shell commands, reports output, handles failures, and requests approval. |
| Review behavior | Whether it can inspect changes, reason about tests, and preserve review-scope metadata without inventing results. |
| Tool state boundary | Which hidden memory, cache, local profiles, IDE state, conversation state, or vendor state exists and why it is not repository truth. |
| Governance risks | Known ways the tool could bypass ADM authority, checks, reviews, approvals, CI truth, release hygiene, or handover rules. |
| Fallback | Whether Generic CLI Agent remains sufficient when tool-specific behavior is unverified, unstable, or unnecessary. |

Tool Verification evidence must be concise, repository-relative, non-sensitive, and reviewable. It must not include credentials, private local paths, raw logs, hidden memory exports, proprietary dumps, or personal access tokens.

## 4. Deferred Candidate Policy

Gemini CLI and Antigravity CLI remain deferred candidates.

They are not accepted adapter prompts in v0.29.

They must not be represented as implemented, approved, verified, release-ready, or equivalent to the accepted adapter set.

A later explicit adapter PR may add one of them only if it includes:

1. current Tool Verification evidence,
2. an accepted ADR or equivalent governance decision for the adapter semantics,
3. documentation synchronization,
4. a complete six-role review set when the change is roadmap- or governance-significant,
5. local validation and release-grade validation where applicable.

## 5. Relationship to Adapter Prompt Standard

The Adapter Prompt Standard remains the canonical Roadmap Phase 5 standard for thin tool-specific prompts.

Tool Verification does not replace the Adapter Prompt Standard. It sits before adapter acceptance and asks whether a dedicated adapter is justified at all.

A verified tool still may not need a dedicated adapter if Generic CLI Agent is sufficient.

Adapter prompts remain downstream from:

1. `spec/ADM_v1_DRAFT.md`,
2. `docs/MASTER_PROMPT_STANDARD.md`,
3. `prompts/master_prompt.md`,
4. `docs/ADAPTER_PROMPT_STANDARD.md`,
5. accepted ADRs and governance documents.

## 6. Relationship to Master Prompt Standard

The Master Prompt Standard remains canonical and tool-neutral.

Tool Verification must not smuggle Gemini-, Antigravity-, IDE-, MCP-, provider-, or machine-specific behavior into `prompts/master_prompt.md`.

The master prompt may reference Tool Verification as a governance trigger, but it must not become a tool-specific adapter or runtime profile.

## 7. Non-goals

v0.29 does not introduce:

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

## 8. Alternatives

### Alternative A: Add Gemini CLI and Antigravity CLI adapters immediately

- Description: Create adapter prompts based on expected or remembered tool behavior.
- Reason for rejection: This would encode unverified behavior into canonical repository artifacts and make adapter prompts less trustworthy.

### Alternative B: Keep deferral language only in the Adapter Prompt Standard

- Description: Leave the existing deferred-candidate wording as the only control.
- Reason for rejection: The repository needs a clear discovery gate that future agents can apply before proposing adapter expansion.

### Alternative C: Build an automated tool-verification harness now

- Description: Add scripts, schemas, workflow checks, or runtime probes for tool verification.
- Reason for rejection: v0.29 needs governance semantics first. Automation before stable criteria would freeze the wrong abstraction.

## 9. Trade-offs

### Pros

- Prevents premature adapter expansion.
- Keeps ADM model-neutral and repository-backed.
- Gives future adapter PRs clear eligibility criteria.
- Preserves Generic CLI Agent as a safe fallback.
- Separates tool capability from hidden tool state.

### Cons

- Adds one more policy document.
- Requires future agents to collect evidence before adding adapters.
- Does not itself verify Gemini CLI, Antigravity CLI, or any future tool.

## 10. Risks and Consequences

- Risk: Agents may treat Tool Verification as adapter approval.
- Mitigation: Verification is only eligibility evidence; adapter acceptance still requires explicit PR scope, documentation sync, and reviews.

- Risk: Tool behavior can change after verification.
- Mitigation: Future adapter PRs must use current behavior and document freshness.

- Risk: Verification evidence may leak local or proprietary state.
- Mitigation: `docs/TOOL_VERIFICATION.md` forbids secrets, raw logs, private paths, credentials, and hidden memory exports.

## 11. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.

## 12. Affected Files

- [x] `docs/decisions/ADR-20260708-tool-verification-discovery-baseline.md`
- [x] `docs/TOOL_VERIFICATION.md`
- [x] `ROADMAP.md`
- [x] `README.md`
- [x] `CHANGELOG.md`
- [x] `spec/ADM_v1_DRAFT.md`
- [x] `docs/OPERATING_SYSTEM.md`
- [x] `docs/ADAPTER_PROMPT_STANDARD.md`
- [x] `docs/MASTER_PROMPT_STANDARD.md`
- [x] `prompts/master_prompt.md`
- [x] `prompts/adapters/README.md`

## 13. Review Log

- [x] Principal Architect: PASSED via `RSV-20260708-tool-verification-discovery-baseline`
- [x] Security Lead: PASSED via `RSV-20260708-tool-verification-discovery-baseline`
- [x] Performance Lead: PASSED via `RSV-20260708-tool-verification-discovery-baseline`
- [x] Cost Engineer: PASSED via `RSV-20260708-tool-verification-discovery-baseline`
- [x] Simplifier: PASSED via `RSV-20260708-tool-verification-discovery-baseline`
- [x] Documentation Reviewer: PASSED via `RSV-20260708-tool-verification-discovery-baseline`

## 14. Final Outcome

Six-role review set was completed under `RSV-20260708-tool-verification-discovery-baseline` and release-grade validation passed before tagging v0.29.
