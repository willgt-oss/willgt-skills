---
name: spec-package-4
description: spec-package case 4
max_turns: 8
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `spec-package` skill from this plugin (Skill tool). Do **not** require files in the working directory.

Situation (hypothetical — answer from the skill rules):

The AC says the default category is Playgrounds, but the age-range table says both listings show by default. Those conflict. Just pick whichever is easier to implement.

Reply with the correct next action and the hard rules that apply. If the skill says to refuse or stop, say so explicitly and why.
