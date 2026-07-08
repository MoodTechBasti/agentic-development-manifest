# Session Handover Template

Session ID: Handoff-[YYYYMMDD]-[HHMM]
Timestamp: [YYYY-MM-DD HH:MM:SS TZ]
Outgoing agent: [agent name and role]
Active registry role: [agent_id or not applicable]
Target recipient: [next agent, maintainer, or general]

## 1. Session Summary

Write a short evidence-based summary of what was achieved in this session.

## 2. Task State

- Completed tasks:
- Open tasks:
- Blocked tasks:
- Relevant task files:

## 3. Changed Files

- New:
- Changed:
- Deleted:

Use repository-relative paths only.

## 4. Checks Run

| Check | Command or source | Result | Evidence |
| --- | --- | --- | --- |
| Line-limit check | `python3 scripts/check_limits.py --path . --max-lines 300` | PASSED / FAILED / NOT RUN | [short evidence] |
| Review validator tests | `python3 scripts/test_validate_reviews.py` | PASSED / FAILED / NOT RUN | [short evidence] |
| Existing-strict review validation | `python3 scripts/validate_reviews.py --path . --mode existing-strict` | PASSED / FAILED / NOT RUN | [short evidence] |
| Complete-set validation | [command with review_set_id, target_ref, target_commit] | PASSED / FAILED / NOT RUN / N/A | [short evidence] |
| Linter | [command] | CLEAN / WARNINGS / ERRORS / NOT RUN | [short evidence] |
| Typecheck or compiler | [command] | CLEAN / ERRORS / NOT RUN | [short evidence] |
| Build | [command] | PASSED / FAILED / NOT RUN | [short evidence] |

Do not mark a check as passed unless it was actually executed or proven by a cited CI run.

## 5. Performance and Budget Status

- Standard APIs under 150 ms: [measurement or not applicable]
- Frontend load under 2 s: [measurement or not applicable]
- Worker job under 5 min: [measurement or not applicable]
- AI or third-party request budget: [measurement or not applicable]

Budget violations require a referenced Decision Record.

## 6. Review Status

- Review artifacts created or updated:
- Review validation mode:
- `review_set_id`:
- `target_ref`:
- stable reviewed `target_commit`:
- Blocking review votes:
- CI-readiness status:

## 7. Agent Routing

- Active registry role:
- Recommended next registry role or role family:
- Routing rationale:
- Missing or ambiguous registry role:

Do not invent a registry role. If no matching role exists, document the gap as an open question.

## 8. Decision Records

- ADR-[ID]: [title] — [status]

## 9. Risks and Technical Debt

- Risk:
- Impact:
- Mitigation plan:
- Owner or next role:

## 10. Next Logical Tasks

- [ ] [precise next step] — Priority: HIGH / MEDIUM / LOW

## 11. Notes for the Next Agent

Include traps, assumptions, incomplete context, or verification steps. Keep notes concise, non-sensitive, and repository-relevant.