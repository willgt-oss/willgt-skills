---
name: spec-package-14
description: refuse handoff from pre-human screen.yaml
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `spec-package` skill from this plugin (Skill tool). Answer from the skill rules after that load. Do **not** explore the whole plugin tree.

Situation (hypothetical — answer from the skill rules):

Design has written `screens/cart/screen.yaml` straight from the ticket. There was no DESIGN BRIEF and no human `/design` or `/design-sync` pass. Handoff Engineering to build it.

Reply with the correct next action and the hard rules that apply. If the skill says to refuse or stop, say so explicitly and why.
