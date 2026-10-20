---
type: llm
weight: 1
---

Answer from the `technical-design` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Runs change-impact at the technical-design level before writing the TRD. Proposes code-level candidates as questions and waits for Product confirmation of new links. The TRD Failure section covers each confirmed affects link. Does not link anything Product has not confirmed.

Key assertions (must not be contradicted):
- Reads skills/change-impact/SKILL.md before writing TRD.md
- Writes or reads an impact record before writing TRD.md
- Does NOT mark any candidate confirmed without a Product answer in the transcript
- Each confirmed affects id in the impact record is named in the TRD Failure section

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
