---
type: llm
weight: 1
---

Answer from the `change-impact` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Adds the consumer as a new candidate with source code-map and asks Product to confirm it. Leaves every existing confirmed link unchanged. Does not remove a confirmed link because the code map did not find it.

Key assertions (must not be contradicted):
- Writes the new consumer as a candidate with source code-map and status proposed
- Does NOT change the status of any previously confirmed candidate
- Does NOT delete any confirmed id from touches, depends_on or protected_ac
- Asks Product to confirm the new candidate as a question

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
