---
type: llm
weight: 1
---

Answer from the `technical-design` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Checks the PRD gate from config (`approval: decisions-file`). PRD not on base branch and/or no decisions-file approval → draft. Refuses to write TRD.md, openapi.yaml or event.schema.json. Uses the exact stop phrase **"no technical design from a draft PRD"**. Names the missing approval (base-branch PRD and/or a recorded approval in DECISIONS.md).

Key assertions (must not be contradicted):
- Uses the exact phrase "no technical design from a draft PRD" (or clearly quotes that stop phrase)
- Does NOT create or edit TRD.md, openapi.yaml or event.schema.json
- Names missing base-branch commit and/or missing decisions-file approval
- Does NOT require an epic tool or epic phase

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
