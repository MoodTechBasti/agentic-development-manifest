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

## 5. Validation Performed

List commands or GitHub Actions runs.

```bash
# Example
python scripts/check_limits.py --path . --max-lines 300
python scripts/test_validate_reviews.py
python scripts/validate_reviews.py --path . --mode existing-strict
```

## 6. Risks and Follow-Up

- Known risks:
- Deferred work:
- Follow-up PR or issue:
