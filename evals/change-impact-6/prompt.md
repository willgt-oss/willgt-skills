---
name: change-impact-6
description: change-impact case 6 — RDF export mapping
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `change-impact` skill from this plugin (Skill tool). Answer from the skill rules after that load. Do **not** require files in the working directory and do not explore the whole plugin tree.

Situation (hypothetical — answer from the skill rules):

`.willgt/skills.yaml` exists. Export the bulk-discount impact record for an RDF tool.

Reply with the correct next action and the hard rules that apply. Name the link names and export terms the skill uses. The skill's mapping table **is** the export (there is no separate export binary).
