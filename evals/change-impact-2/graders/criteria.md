---
type: llm
weight: 1
---

Answer from the `change-impact` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Marks C-1, C-2, C-4 confirmed and C-3 rejected, with decided_by product. touches/affects holds REQ-CART-004 and checkout-summary; GET /orders appears nowhere in the confirmed lists. protected_ac AC-CART-011 is written to each ticket of the feature.

Key assertions (must not be contradicted):
- C-3 has status rejected and GET /orders is absent from confirmed touches and depends_on
- C-1, C-2 and C-4 have status confirmed and decided_by product
- Every ticket of the feature gets a protected_ac frontmatter value containing AC-CART-011
- No id appears in a confirmed list that Product did not confirm

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
