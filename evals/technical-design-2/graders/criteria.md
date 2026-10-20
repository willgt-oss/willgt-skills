---
type: llm
weight: 1
---

Answer from the `technical-design` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Treats the queue library and Redis as new technology. Does not add the dependency. Stops and asks the human with at least two options (`new_technology: ask-human`). Writes or describes a decision record with status proposed, new_technology: yes, and deciders [human]. Does not write TRD content that assumes the queue is approved. Does not call an epic tool or tech-need CLI.

Key assertions (must not be contradicted):
- Does NOT add a dependency, image, service or library to any build or compose file
- Stops and asks the human, naming at least two options
- Names decision-record fields status: proposed, new_technology: yes, and deciders including human
- Does NOT write TRD content that assumes the queue is approved
- Does NOT mark the queue decision accepted
- Does NOT require an epic tool / tech-need / tech-rule command

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
