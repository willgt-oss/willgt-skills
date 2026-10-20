---
type: llm
weight: 1
---

Answer from the `change-impact` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Reruns the ticket's own AC and also AC-CART-011 and AC-CART-012 against the ticket's environment. A failing protected AC is a bug finding that sends the ticket back, not a note.

Key assertions (must not be contradicted):
- Runs AC-CART-011 and AC-CART-012 in addition to the ticket's own AC
- Saves evidence for each protected AC
- Does NOT move the ticket forward when a protected AC fails

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
