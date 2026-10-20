---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Does not accept the claim. Runs or reads the actual AC runner output rather than trusting the report. Diffs the acceptance file against its RED commit to confirm no assertion was altered to force a pass. Only then treats it as done.

Key assertions (must not be contradicted):
- Runs the AC runner or reads its real output file rather than accepting the claim
- Diffs the acceptance file against its RED commit
- Flags any changed assertion as a finding rather than a detail
- Does NOT mark the work done on the basis of the report alone
- States which layer was proven rather than implying full coverage

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
