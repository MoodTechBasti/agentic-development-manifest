# ADM Agent Registry

The `.ai/agents/` directory describes repository-owned agent roles for ADM-compatible work.

It is not a permission engine, sandbox, local tool profile, or vendor-specific agent configuration.

## Purpose

Agent Registry files help future agents answer four questions before implementation:

1. Which role am I operating as?
2. Which project context must I read first?
3. Which files or areas may I change for this task?
4. Which role should receive the next handover?

## Minimal registry fields

A registry entry should define:

| Field | Purpose |
| --- | --- |
| `agent_id` | Stable repository-local identifier |
| `role` | Human-readable role name |
| `mission` | Primary responsibility |
| `reads` | Required initialization context |
| `writes` | Expected write areas when in scope |
| `forbidden` | Areas not to change without explicit approval |
| `handover_to` | Recommended next role or role family |
| `review_scope` | Review responsibility, if any |

## Handover routing

Handover Automation may consume `agent_id`, `role`, and `handover_to` to check whether a handover references an existing next role.

It must not invent missing roles or treat registry write areas as technical permissions.

If a handover needs a role that does not exist yet, the handover should record that as an open registry question.

## Commit policy

Agent Registry artifacts may be committed when they are intentional, reviewable, non-sensitive, and useful for future agent coordination.

Do not commit:

- local tool profiles
- hidden model-memory exports
- private local paths
- credentials or private URLs
- raw chat transcripts
- temporary role experiments

## Rule of thumb

The Agent Registry describes durable project roles. It does not grant technical permissions. GitHub rulesets, CI, code review, and local sandboxing remain the enforcement layers.