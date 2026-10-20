---
name: technical-design-7
description: approval pr-merge gate checks merge not decisions line
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `technical-design` skill from this plugin (Skill tool). Answer from the skill rules. Do not explore the whole plugin tree.

Situation (hypothetical):

`.willgt/skills.yaml` has `approval: pr-merge`. The PRD for order-export sits only on a feature branch; that PR is **not** merged to the base branch. There is no DECISIONS.md line. Engineering asks you to write the technical design.

Reply with the correct next action. Quote the skill's exact stop phrase. Name what is missing under `pr-merge` (not under decisions-file).
