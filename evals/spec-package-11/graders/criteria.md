---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Resolves the runner from the registry rather than copying another project's binding. Identifies Playwright as the web binding and unsuitable for a mobile surface, names the registry alternatives and their status, and binds the runner in `.willgt/skills.yaml`. Notes that any candidate must satisfy the four runner requirements on real work before being registered.

Key assertions (must not be contradicted):
- Consults the runner registry instead of assuming Playwright
- Identifies Playwright as unsuitable for the mobile surface
- Binds spec-package-ac-runner in `.willgt/skills.yaml`
- States that an unproven runner must meet the four requirements on real work first
- Does NOT copy another project's runner binding unexamined

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
