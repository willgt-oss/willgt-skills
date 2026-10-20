---
name: spec-package-18
description: first-run setup when starting spec-package with no config
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Skill, Glob, Grep, Write]
runs: 1
---

Load the `spec-package` skill from this plugin (Skill tool). Answer from the skill rules. Do not explore the whole plugin tree.

Situation (hypothetical):

The repo has **no** `.willgt/skills.yaml`. Someone asks you to start a new package for products-home.

Reply with the correct next action and the hard rules that apply.
