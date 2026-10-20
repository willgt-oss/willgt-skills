---
name: change-impact-2
description: change-impact case 2
max_turns: 8
allowed_tools: [Read, Skill, Glob, Grep]
runs: 1
---

Load the `change-impact` skill from this plugin (Skill tool). Do **not** require files in the working directory.

Situation (hypothetical — answer from the skill rules):

Product answers the candidates for bulk-discount: C-1 REQ-CART-004 yes, C-2 checkout-summary screen yes, C-3 GET /orders no, C-4 AC-CART-011 yes. Finish the impact record and update the tickets.

Reply with the correct next action and the hard rules that apply. If the skill says to refuse or stop, say so explicitly and why.
