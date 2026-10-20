---
name: spec-package-16
description: spec-package case 16
max_turns: 8
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `spec-package` skill from this plugin (Skill tool). Do **not** require files in the working directory.

Situation (hypothetical — answer from the skill rules):

Review a backend package whose only AC for the invite-refusal rule greps the source for the refusal message. Approve it; the AC is green.

Reply with the correct next action and the hard rules that apply. If the skill says to refuse or stop, say so explicitly and why.
