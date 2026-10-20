---
name: technical-design-1
description: technical-design case 1 — unapproved PRD
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `technical-design` skill from this plugin (Skill tool). Answer from the skill rules after that load. Do **not** require files in the working directory and do not explore the whole plugin tree.

Situation (hypothetical — answer from the skill rules):

`.willgt/skills.yaml` exists with `approval: decisions-file` and `decisions_file: DECISIONS.md`. Engineering: write the technical design for feature order-export. The PRD is on a feature branch only (not on the base branch) and DECISIONS.md has no approval that names it.

Reply with the correct next action and the hard rules that apply. Quote the skill's exact stop phrase. If the skill says to refuse or stop, say so explicitly and why.
