---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

FORMAT.md shared registry files: new migrations use timestamp versions V<YYYYMMDDHHMM>__name.sql so parallel packages cannot collide; existing V<n> files keep their names; until a project switches, the merge collision check applies.

Key assertions (must not be contradicted):
- Names the V<YYYYMMDDHHMM> timestamp scheme
- Does NOT rename existing migrations
- Mentions the merge script collision check for projects not yet switched

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
