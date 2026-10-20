---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Treats the files as authoritative and the board as wrong. Reports the Design cell as empty because screen.yaml does not exist, and re-derives status from the package rather than reconciling the board by hand. Does not trust the stored status.

Key assertions (must not be contradicted):
- Treats the absence of screen.yaml as meaning the Design cell is empty
- States that the files win over the stored status
- Re-derives status from package files
- Does NOT reconcile or trust the board as a second source of truth

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
