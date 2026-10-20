---
name: technical-design-3
description: standard depth — TRD + one openapi path, no event
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `technical-design` skill from this plugin (Skill tool). If needed, read `skills/spec-package/TYPES.md` once. Answer from those rules. Do **not** create files. Do **not** explore the whole plugin tree.

Situation (hypothetical — answer from the skill rules):

`.willgt/skills.yaml` has `design_depth: standard`. The PRD for invoice-download is approved. A change-impact record already exists with confirmed links. The feature exposes one HTTP path `GET /invoices/{id}/pdf` and emits no event. Write the technical design.

Reply with the exact files you would write, the TRD level-2 headings, and what you would not write.
