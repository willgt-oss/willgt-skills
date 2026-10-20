---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Checks the feature's declared type first. A billing sync is a backend feature, for which Marketing and Design are not applicable rather than missing. Reports those cells as n/a, briefs neither role, and flags that the gap check was run without a type or with the wrong type declared.

Key assertions (must not be contradicted):
- Checks the feature's declared type before briefing anyone
- Identifies Marketing and Design as not applicable for a backend feature
- Reports the cells as n/a rather than as gaps
- Does NOT brief Marketing
- Does NOT brief Design
- Flags the missing or incorrect type declaration as the underlying problem

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
