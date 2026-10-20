---
type: llm
weight: 1
---

Answer from the `change-impact` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Performs the skill's export mapping (the mapping **is** the export — not an external binary). Uses the link names `affects`, `related_test`, and `derived_from` (not the record field names touches / protected_ac / depends_on). Maps those to the OSLC CM / PROV-O export terms from the skill table. Exports confirmed links only — never proposed or rejected.

Key assertions (must not be contradicted):
- Names the link names affects, related_test and derived_from
- Names at least one OSLC/PROV export term from the skill table (e.g. oslc_cm:affectsRequirement, oslc_cm:relatedTestCase, or prov:wasDerivedFrom)
- Exports no candidate whose status is proposed or rejected
- Does NOT refuse solely because "export is not built"

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (for example: no confirmed candidates yet).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
