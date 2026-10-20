---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Accepts that the unit layer is proven and refuses to extend that to the feature working. States that unit-level green does not prove the screen renders, the control is reachable, or a user can operate it. Names the layer proven and the gap, and asks for evidence at the layer the AC actually describes before closing.

Key assertions (must not be contradicted):
- States which layer the passing tests actually proved
- Refuses to treat unit-level green as proof the feature works
- Names the untested layer explicitly
- Requests evidence at the layer the AC describes before closing
- Does NOT mark the feature done on the unit result alone

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
