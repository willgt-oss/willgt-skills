---
name: technical-design-4
description: write decision record cursor vs offset pagination
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `technical-design` skill from this plugin (Skill tool). Answer from the skill rules. Do **not** explore the whole plugin tree.

Situation (hypothetical — answer from the skill rules):

`.willgt/skills.yaml` exists. The feature invoice-list is approved. Engineering: record the decision to paginate the invoice list with a **cursor** instead of an **offset**. This is not new technology.

Reply with the decision-record fields you would write (id, date, status, deciders, context, decision, options, consequences, new_technology). Include at least cursor and offset in options.
