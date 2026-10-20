---
type: llm
weight: 1
---

Answer from the `spec-package` skill.

Pass if the answer matches this expected behavior (substance):

Detects missing `.willgt/skills.yaml` and runs (or describes) first-run setup from SETUP.md before creating package files under `spec_root`. Asks setup questions (or states it will) and would write the config. Does not invent a package path that ignores setup.

Key assertions (must not be contradicted):
- Mentions missing `.willgt/skills.yaml` or SETUP.md / first-run questions
- Would write `.willgt/skills.yaml` (or asks the six questions) before packaging
- Uses or names `spec_root` (default `spec/`) only after setup / from config
- Does NOT skip setup entirely

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
