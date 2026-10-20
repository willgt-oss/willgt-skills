---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Checks `.willgt/skills.yaml` for a spec-package binding. Because one exists, writes a brief that carries only the package root, the screen_id, and the AC runner command. Does NOT restate acceptance criteria in the brief body, does NOT paste a Figma URL, and does NOT point at preview.html. Confirms a failing AC is already committed before briefing an implementer.

Key assertions (must not be contradicted):
- Reads `.willgt/skills.yaml` to resolve the spec-package root instead of hardcoding a path
- Handoff contains the screen_id
- Handoff contains the package root path
- Does NOT include acceptance criteria prose in the brief body
- Does NOT reference preview.html as the implementation target
- Does NOT reference a Figma URL as the implementation target
- Verifies a failing AC file exists before briefing the implementer

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
