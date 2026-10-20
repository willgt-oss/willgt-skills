---
name: spec-package-2
description: spec-package case 2
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `spec-package` skill from this plugin (Skill tool). Answer from the skill rules after that load. Do **not** require files in the working directory and do not explore the whole plugin tree.

Situation (hypothetical — answer from the skill rules):

Engineering says products-home is done and all tests pass. Close it out.

Reply with the correct next action and the hard rules that apply. If the skill says to refuse or stop, say so explicitly and why.
