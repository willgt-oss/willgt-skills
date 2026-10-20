---
name: technical-design-6
description: design_depth light produces one-pager not full TRD
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `technical-design` skill from this plugin (Skill tool). Answer from the skill rules. Do **not** create files. Do not explore the whole plugin tree.

Situation (hypothetical):

`.willgt/skills.yaml` exists with `design_depth: light` and `approval: decisions-file`. The PRD for invoice-download is approved (on the base branch; a Go line names it in DECISIONS.md). A change-impact record already exists with confirmed links. Write the technical design.

Reply with the exact form of output you would produce (section names) and what you would **not** write (full TRD / OpenAPI files).
