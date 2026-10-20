---
type: llm
weight: 1
---

Answer from the `change-impact` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Writes the confirmed touches into the optional PRD.md ## Touches section and the flow.yaml touches list (spec-package 2.1.0). Does not add depends_on to either file, because depends_on is not a spec-package field; it stays in the impact record.

Key assertions (must not be contradicted):
- Writes only Product-confirmed touches into PRD.md and flow.yaml
- Does NOT add depends_on to any PRD.md or flow.yaml
- Does NOT edit any file under skills/spec-package/
- Keeps depends_on in the impact record file

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
