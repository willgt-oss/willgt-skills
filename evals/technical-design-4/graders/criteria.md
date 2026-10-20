---
type: llm
weight: 1
---

Answer from the `technical-design` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Writes one decision record from the template: id, date, status, deciders, context of 2 to 5 sentences, decision of 1 to 3 sentences, options, consequences, new_technology no. No new technology, so Engineering may accept it.

Key assertions (must not be contradicted):
- Writes a record with every field of skills/technical-design/templates/decision-record.yaml present
- The context field has between 2 and 5 sentences
- The decision field has between 1 and 3 sentences
- options lists at least two options including cursor and offset
- new_technology is no

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
