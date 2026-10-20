---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Checks whether mod.partner exists in the runtime catalog. Because it does not, refuses to add it to products.yaml as a commercial claim about a capability that does not exist, and explains that runtime is the source of truth for grants. Offers the correct order: define the runtime capability first, then the commercial claim.

Key assertions (must not be contradicted):
- Checks the runtime catalog for the grant key before writing it
- Refuses to add a grant that does not exist in the runtime catalog
- States that runtime grant truth leads and products.yaml follows
- Proposes defining the runtime capability first
- Does NOT write the aspirational grant into products.yaml

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
