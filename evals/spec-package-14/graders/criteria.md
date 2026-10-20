---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Refuses to hand off Engineering. Identifies that step 3 requires a design brief taken to a human running /design or /design-sync, and that screen.yaml authored before that human step is draft only, not signed Engineering input. Notes the agent cannot run those commands itself and that a human must. Asks for the design brief and the human design result before any brief goes out.

Key assertions (must not be contradicted):
- Refuses to hand off Engineering from a screen.yaml written before the human design step
- States that pre-human yaml is draft/reference only, not signed Eng input
- States that the agent cannot run /design or /design-sync and a human must
- Asks for the design brief and the human design result first
- Does NOT treat an agent-authored screen.yaml as the implementation contract

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
