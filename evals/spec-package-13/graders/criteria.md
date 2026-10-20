---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Identifies this as an agentic feature, where the acceptance model does not transfer: output is non-deterministic, so asserting exact responses either fails constantly or gets loosened until it asserts nothing. Proposes evals scored across runs instead, notes the likely additional artifacts, and states that the agentic type is unsettled and should not be finalised from a guess.

Key assertions (must not be contradicted):
- Identifies the feature as the agentic type
- Explains that deterministic exact-output assertions do not work for non-deterministic output
- Proposes evals in place of or alongside executable AC
- States that the agentic type is an open problem not yet settled by real work
- Does NOT write an ac.feature asserting exact model output

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
