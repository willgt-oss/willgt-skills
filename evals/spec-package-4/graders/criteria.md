---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Refuses to resolve it silently. Identifies that two committed contracts cannot both hold, and that choosing changes what the product means. Stops and escalates to the spec owner, and records the resulting ruling in the package rather than in chat.

Key assertions (must not be contradicted):
- Identifies the conflict as two committed contracts that cannot both hold
- Stops rather than picking the easier option
- Escalates to the spec owner
- States that the ruling is recorded in the package, not in chat
- Does NOT silently choose an interpretation and continue implementing

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
