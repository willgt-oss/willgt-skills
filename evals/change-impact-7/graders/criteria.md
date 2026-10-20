---
type: llm
weight: 1
---

Answer from the `change-impact` skill without inventing private hosts.

Pass if the answer matches this expected behavior (substance):

Does not invent impact links yet. Detects missing `.willgt/skills.yaml` and runs (or describes running) the first-run setup from `skills/spec-package/SETUP.md`: asks the setup questions one at a time (or states it will), then writes `.willgt/skills.yaml` with defaults if the user accepts Enter. Only after that would change-impact proceed.

Key assertions (must not be contradicted):
- Mentions missing `.willgt/skills.yaml` or that setup must run first
- Points at SETUP.md or the six setup questions / writing the config file
- Does NOT invent confirmed impact links before setup
- Does NOT skip setup and dive straight into searching specs as if configured

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
