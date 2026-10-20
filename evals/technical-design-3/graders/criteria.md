---
type: llm
weight: 1
---

Answer from the `technical-design` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Uses TYPES.md / skill file rules to choose artifacts. Plans TRD.md with level-2 headings exactly Interfaces, Data, Failure, plus one openapi.yaml path fragment for the single HTTP path. Plans no event.schema.json. Creates no other design-document format. Does not copy PRD Problem or Goals into the TRD. Knowledge-only answers that list these files and headings (without writing them) still pass.

Key assertions (must not be contradicted):
- Chooses files from TYPES.md / skill rules (mentions TYPES or the HTTP-path / no-event rule)
- TRD.md level-2 headings are exactly Interfaces, Data, Failure
- openapi.yaml covers exactly one path
- Does NOT write or plan event.schema.json
- Does NOT invent an extra design-document format beyond TRD.md, openapi.yaml and optional decision records
- TRD.md does NOT copy the PRD Problem or Goals text

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
