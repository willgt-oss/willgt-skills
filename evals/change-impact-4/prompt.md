---
name: change-impact-4
description: change-impact case 4
max_turns: 8
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `change-impact` skill from this plugin (Skill tool). Do **not** require files in the working directory.

Situation (hypothetical — answer from the skill rules):

QA: verify ticket bulk-discount-api at its tip. The ticket has protected_ac: AC-CART-011, AC-CART-012.

Reply with the correct next action and the hard rules that apply. If the skill says to refuse or stop, say so explicitly and why.
