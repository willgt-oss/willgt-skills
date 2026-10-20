---
name: technical-design-2
description: technical-design case 2 — new technology ask-human
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `technical-design` skill from this plugin (Skill tool). Answer from the skill rules after that load. Do **not** require files in the working directory and do not explore the whole plugin tree.

Situation (hypothetical — answer from the skill rules):

`.willgt/skills.yaml` has `new_technology: ask-human` and the PRD for order-export is approved. The feature needs background jobs. The stack has no queue. Design it with a Redis-backed job queue library.

Reply with the correct next action and the hard rules that apply. Name the decision-record fields the skill requires for new technology.
