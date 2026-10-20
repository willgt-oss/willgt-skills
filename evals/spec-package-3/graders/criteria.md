---
type: llm
weight: 1
---

Answer from the `spec-package` skill without a real repo checkout.

Pass if the answer matches this expected behavior (substance):

Derives the readiness row by inspecting package files on disk — products.yaml for the Offer, screen.yaml, ac.feature, the executable AC — and reports which cells are empty. Names only the owners of empty cells. Does not brief roles whose work already exists on disk, and does not consult a stored board or status file.

Key assertions (must not be contradicted):
- Inspects package files on disk to determine each cell
- Reports which specific cells are empty
- Names only the owners of empty cells
- Does NOT brief roles whose artifacts already exist
- Does NOT rely on a stored board, checklist or status file as the source of truth
- Does NOT claim a ready or impact CLI exists

Also pass if the agent correctly **refuses or stops because a rule in the loaded skill requires it** (same substance as the expected behavior above).

Fail if the answer only says the skill is unavailable, unknown, not installed, or could not be loaded, and stops for that reason — that is not a skill-rule refuse and must FAIL.

Fail if the answer invents private project hosts, confirms Product links without confirmation, or proceeds when the skill requires a stop.
