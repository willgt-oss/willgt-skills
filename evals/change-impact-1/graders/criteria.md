---
type: llm
weight: 1
---

Answer from the `change-impact` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Searches existing spec files (PRD requirement ids, screen.yaml, flow.yaml, OpenAPI fragments, event schemas, ac.feature ids). Proposes each match as a candidate question to Product with its evidence. Writes candidates with status proposed. Confirms nothing on its own.

Key assertions (must not be contradicted):
- Runs a search over spec files before proposing any candidate
- Each candidate turn names the target id and an evidence file path
- Each candidate is asked as a question ending in '?'
- Every candidate written before a Product answer has status proposed
- Writes no touches, depends_on or protected_ac value before a Product answer

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
