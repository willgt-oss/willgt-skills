---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Applies the step 9 mutation gate in IMPLEMENTATION.md: the grep probe is `static` and cannot be the only AC for a runtime rule, so Review asks for AC that call the API and assert response and persisted state, plus a mutation table showing each deny AC goes red when the guard is removed in a scratch copy. Does not approve.

Key assertions (must not be contradicted):
- Refuses to approve on a source-grepping AC alone
- Requires AC that call the running API or service and assert response and persisted state
- Requires a mutation table in the evidence folder
- Does NOT commit the scratch mutation

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
