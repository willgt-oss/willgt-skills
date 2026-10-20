---
name: technical-design-5
description: change-impact before TRD when record missing
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `technical-design` skill from this plugin (Skill tool). Answer from the skill rules after that load. Do **not** explore the whole plugin tree.

Situation (hypothetical — answer from the skill rules):

`.willgt/skills.yaml` exists (`design_depth: standard`). Engineering: write the technical design for the approved feature refund-request. The PRD gate is already satisfied. **No change-impact record exists yet.**

Reply with the correct next action before any TRD is written. Name the skill you open first.
