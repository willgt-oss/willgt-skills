---
name: change-impact-7
description: first-run setup when .willgt/skills.yaml is missing
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Skill, Glob, Grep, Write]
runs: 1
---

Load the `change-impact` skill from this plugin (Skill tool). Answer from the skill rules. Do **not** explore the whole plugin tree.

Situation (hypothetical):

The repo has **no** `.willgt/skills.yaml`. Product asks you to run change-impact for feature bulk-discount.

Reply with the correct next action and the hard rules that apply.
