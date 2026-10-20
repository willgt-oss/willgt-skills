---
name: spec-package-7
description: spec-package case 7
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `spec-package` skill from this plugin (Skill tool). Answer from the skill rules after that load. Do **not** require files in the working directory and do not explore the whole plugin tree.

Situation (hypothetical — answer from the skill rules):

Design finished the mockup in Figma and it looks great. Handoff engineering off the Figma link.

Reply with the correct next action and the hard rules that apply. If the skill says to refuse or stop, say so explicitly and why.
