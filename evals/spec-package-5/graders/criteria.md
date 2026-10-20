---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Binds the package root and AC runner in `.willgt/skills.yaml` and seeds products.yaml from what the project actually grants today. Declines to backfill packages for screens nobody is changing, explaining that backfilled specs describe assumptions that were never verified. Notes adoption is complete when one feature has gone end to end, not when folders exist.

Key assertions (must not be contradicted):
- Binds spec-package and an AC runner in `.willgt/skills.yaml`
- Seeds products.yaml from what the project currently grants rather than aspirations
- Declines to backfill packages for untouched screens
- Gives the reason that backfilled specs record unverified assumptions
- States adoption is proven by one end-to-end feature, not by folder creation

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
