# Pull Request: ADM Compliance Check

## 1. Summary

Describe the change precisely.

- What changed:
- Why it changed:
- Scope boundary:

## 2. ADM Self-Check

Mark every applicable item.

- [ ] Model-neutral: no vendor-specific model, CLI, or API is required unless documented as optional.
- [ ] CLI-friendly: scripts or checks can be executed from a terminal.
- [ ] Artifact-based: important decisions, reviews, or handovers are committed as files, not only described in chat or PR comments.
- [ ] Repository-relative paths: documentation uses paths such as `templates/reviews/`, not `/templates/reviews/`.
- [ ] No transient markers: no NotebookLM source markers, temporary chat annotations, or local scratch notes were committed.
- [ ] No secrets: no tokens, keys, credentials, private URLs, or sensitive local paths were committed.

## 3. Quality Gates

- [ ] Line-limit check considered for changed source files.
- [ ] Review validator considered for `.ai/reviews/` changes.
- [ ] New or changed scripts remain dependency-light and documented.
- [ ] Any governance-relevant change has an ADR or documented decision.
- [ ] Documentation and `CHANGELOG.md` are updated when behavior changes.

## 4. Review Scope

Select one.

- [ ] No review artifact needed: small documentation, typo, or non-governance change.
- [ ] Existing-strict validation is enough: review files exist and must be structurally valid.
- [ ] Complete review set needed: release, phase transition, security-sensitive change, or governance change.

If complete review set is needed:

```text
review_set_id:
target_ref:
target_commit:
```

## 5. Validation Evidence

Use exact commands, workflow runs, and outcomes. Do not mix local validation with GitHub workflow evidence.

### Local validation

```bash
# Example
python scripts/check_limits.py --path . --max-lines 300
python scripts/test_validate_reviews.py
python scripts/validate_reviews.py --path . --mode existing-strict
```

Result:

```text
PASSED | FAILED | NOT RUN
```

### GitHub Actions PR gate

```text
Workflow:
Run number:
Head commit:
Status:
Conclusion:
```

### Manual release-grade workflow_dispatch

Required before release tagging when the PR changes governance, validation, release, roadmap, or review semantics.

```text
Workflow:
Run number:
Branch: main
review_gate_mode: complete-set
review_set_id:
target_ref:
reviewed_commit:
Status:
Conclusion:
```

If not run:

```text
NOT RUN: <reason>
```

## 6. Risks and Follow-Up

- Known risks:
- Deferred work:
- Follow-up PR or issue:
