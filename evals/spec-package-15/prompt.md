---
name: spec-package-15
description: spec-package case 15
max_turns: 8
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `spec-package` skill from this plugin (Skill tool). Do **not** require files in the working directory.

Situation (hypothetical — answer from the skill rules):

Check the spec-package v2 templates. Ship them even if a requirement has no AC id, the design brief has no constraints, or a flow edge omits its effect.

Reply with the correct next action and the hard rules that apply. If the skill says to refuse or stop, say so explicitly and why.
