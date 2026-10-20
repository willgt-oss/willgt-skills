---
type: llm
weight: 1
---

Answer from the `technical-design` skill.

Pass if the answer matches this expected behavior (substance):

Respects `design_depth: light`. Plans a one-page design (approach, data changes, API sketch, risks). Does **not** require the full TRD template with Interfaces/Data/Failure as the deliverable. Does not invent OpenAPI fragments or event schemas as required output for light depth.

Key assertions (must not be contradicted):
- Names light depth or the one-pager sections (approach / data / API sketch / risks)
- Does NOT require a full TRD with exactly Interfaces, Data, Failure as the light deliverable
- Does NOT treat OpenAPI + event.schema.json as required for light depth

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
