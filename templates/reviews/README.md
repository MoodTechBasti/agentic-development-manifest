# ADM Review Templates

This directory contains reusable review templates for the ADM multi-agent review process.

## Template location vs runtime location

- Reusable templates live in `templates/reviews/`.
- Completed review artifacts live in `.ai/reviews/`.

Do not store empty templates in `.ai/reviews/`. That directory is runtime project memory and should contain concrete, dated review artifacts only.

## Available templates

| Template | Role | Runtime ID prefix |
| --- | --- | --- |
| `architect.md` | Principal Architect | `REV-ARCH` |
| `security.md` | Security Engineer | `REV-SEC` |
| `performance.md` | SRE and Performance Lead | `REV-PERF` |
| `cost.md` | Cost Engineer | `REV-COST` |
| `simplifier.md` | Simplifier | `REV-SIMP` |
| `documentation.md` | Documentation Reviewer | `REV-DOC` |

## Usage

Copy the relevant template into `.ai/reviews/`, rename it with the runtime review ID, and fill it before marking the related work CI-ready.

Example:

```bash
cp templates/reviews/security.md .ai/reviews/REV-SEC-20260708-ai-routing.md
```

The completed review must state a final vote and CI-readiness status.
