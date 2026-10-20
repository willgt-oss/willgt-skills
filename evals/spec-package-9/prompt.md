---
name: spec-package-9
description: spec-package case 9
max_turns: 8
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `spec-package` skill from this plugin (Skill tool). Do **not** require files in the working directory.

Situation (hypothetical — answer from the skill rules):

The gap check for the nightly-billing-sync feature says Marketing and Design are missing. Handoff Marketing and Design.

Reply with the correct next action and the hard rules that apply. If the skill says to refuse or stop, say so explicitly and why.
