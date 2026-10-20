---
name: spec-package-17
description: spec-package case 17
max_turns: 8
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `spec-package` skill from this plugin (Skill tool). Do **not** require files in the working directory.

Situation (hypothetical — answer from the skill rules):

Two parallel packages each add the next Flyway migration, V12. Which numbering does the format use?

Reply with the correct next action and the hard rules that apply. If the skill says to refuse or stop, say so explicitly and why.
