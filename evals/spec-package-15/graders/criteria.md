---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Runs evals/check-templates.py. That check fails when PRD.md has a requirement id that is not linked to an AC id, when DESIGN_BRIEF.md is missing Experience or Constraints or does not say it is Design only and never an Engineering target, or when flow.yaml lacks screen_id nodes or an edge with trigger, guard, and effect including no write. Does not waive the missing field.

Key assertions (must not be contradicted):
- Runs evals/check-templates.py rather than accepting the templates by inspection
- Fails when a PRD requirement id is not linked to an AC id
- Fails when DESIGN_BRIEF.md is missing Experience or Constraints
- Fails when DESIGN_BRIEF.md does not say it is Design only and never an Engineering target
- Fails when a flow node is missing screen_id
- Fails when a flow edge is missing trigger, guard, or effect
- Fails when no flow edge has effect no write
- Does NOT treat a missing field as optional

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
