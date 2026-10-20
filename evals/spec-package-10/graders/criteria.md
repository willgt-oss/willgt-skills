---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Distinguishes not-applicable from missing. Checks the types of the features in play: if none are sellable_module, an empty products.yaml is correct and no gap exists. Only treats it as a gap when a sellable feature actually requires an Offer.

Key assertions (must not be contradicted):
- Checks whether any feature in play is of type sellable_module
- States that an empty products: [] is valid when nothing is sold
- Does NOT brief Product to invent Offers for a project that sells nothing
- Treats not-applicable and missing as different states

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
