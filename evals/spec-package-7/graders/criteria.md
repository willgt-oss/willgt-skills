---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Refuses to start work from Figma. Explains that Figma is export-only and must be written into screen.yaml and tokens before anyone starts, and that if the export-to-git step is skipped the correct action is to stop. Asks for the export to land first.

Key assertions (must not be contradicted):
- Refuses to hand off an implementer from a Figma URL
- States that Figma is export-only into package files
- Requires screen.yaml to exist before briefing
- Stops rather than proceeding with the link
- Does NOT treat a visual preview as the implementation contract

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
