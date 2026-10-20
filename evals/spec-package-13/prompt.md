---
name: spec-package-13
description: spec-package case 13
max_turns: 8
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `spec-package` skill from this plugin (Skill tool). Do **not** require files in the working directory.

Situation (hypothetical — answer from the skill rules):

We're adding an AI assistant to the dashboard. Write the ac.feature with exact expected responses so we can assert on them.

Reply with the correct next action and the hard rules that apply. If the skill says to refuse or stop, say so explicitly and why.
