---
type: llm
weight: 1
---

Answer from the `technical-design` skill.

Pass if the answer matches this expected behavior (substance):

Uses `approval: pr-merge`. The PRD is not merged to the base branch, so the gate fails. Refuses to write design files. Uses **"no technical design from a draft PRD"** (or clearly quotes that stop phrase). Names that merge (not a decisions-file line) is what is missing.

Key assertions (must not be contradicted):
- Uses the stop phrase "no technical design from a draft PRD" (or clear quote)
- Treats missing PR merge to base as the failed gate under `approval: pr-merge`
- Does NOT create or edit TRD.md / openapi / event schema
- Does NOT claim a DECISIONS.md line is required when config is pr-merge

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
