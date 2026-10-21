---
name: change-impact
description: >-
  Finds existing requirements, screens, flows, API paths, events and acceptance ids a new feature may touch or depend on; proposes each as a Product question; records only confirmed links and protected acceptance ids for verifier reruns. Use at feature intake and before technical design when asked what existing behavior a change can break.
license: Apache-2.0
metadata:
  author: WillGT
  version: "0.3.0"
  tier: STANDARD
  category: Quality
---

# change-impact (a check others call)

**Before anything else:** read `.willgt/skills.yaml` at the repo root. If it does not exist, run the setup in `skills/spec-package/SETUP.md`, then continue.

## Contents
- Scope
- Hard rules
- Files and locations
- Intake run (Level 2, Product)
- Technical-design run (Level 3, implementer)
- Work items and verifier
- Link names and export
- Format status
- Run checklist
- Known limits

## Scope

- type: a check. Called by Product at feature intake and by `skills/technical-design/SKILL.md`. It is not the technical design.
- input: the new feature's draft PRD / flow / work-item list, the existing spec-package files under `spec_root` (`skills/spec-package/FORMAT.md`), and `.willgt/skills.yaml`.
- output: one impact record per feature; `protected_ac` on each work item of the feature when the project tracks them.
- decides links: Product. The AI proposes; Product confirms or rejects each candidate.

## Hard rules

1. Nothing is linked without a Product confirmation. A candidate starts `status: proposed`.
2. Each candidate is asked as a question that names the target id and its evidence path, and ends with `?`.
3. A rejected candidate never appears in `confirmed`.
4. Candidates are append-only. Never delete one; never change a confirmed or rejected status except on a new Product answer, recorded with its date.
5. Code-level results (technical-design run) add candidates with `source: code-map`. They never remove or replace a confirmed link.
6. Do not edit `skills/spec-package/` itself. In a project package, write only the optional `touches` / `protected_ac` fields, only from Product-confirmed links. See Format status.
7. Search results are candidates, not facts. Recovered links miss implicit and indirect dependencies; Product confirmation is required for every link.

## Files and locations

- Impact record: `.willgt/impact/<feature_id>.impact.yaml` from `skills/change-impact/templates/impact-record.yaml` (outside `spec_root`).
- Spec packages to search: under `spec_root` from `.willgt/skills.yaml` (default `spec/`).
- Work items: when `work_tracker` is not `none`, name features with `work_item_ref` (skills only store/read that reference string — never call a tracker API). Write confirmed `protected_ac` ids onto each work item the project uses for the feature (frontmatter, issue body, or linked file — whatever the project already uses).

## Intake run (Level 2, Product)

1. Read the new feature's draft PRD requirement statements, flow nodes and edges, and named API paths and events.
2. Search the existing package (bound `spec-package` root): `PRD.md` requirement ids and statements, `screen.yaml` screen_id / regions / actions, `flow.yaml` nodes and edges, `openapi.yaml` paths, `event.schema.json` titles, `ac.feature` scenario ids. Search terms: nouns and verbs of each new requirement, shared screen_ids, shared paths, shared event names, shared grant keys.
3. Record each match as a candidate: kind, target_id, link (`affects` if the feature changes it, `derived_from` if the feature relies on it unchanged, `related_test` for an AC that must still pass), evidence path:line.
   Rule of thumb: An existing, already-passing test that exercises the touched route or function is `related_test` by default. Reclassify it to `affects` only if the new feature changes what that specific test asserts. A target the feature extends additively without changing it for existing callers is `related_test` or `derived_from`, never `affects`, even when the search draft labelled it so; re-deriving the link type is Product's job. Resolve a bare test filename to its full path before recording evidence (two repos can hold files with the same name).
4. Ask Product one question per candidate. Example shape: `C3: GET /orders (spec/api/orders.openapi.yaml:12) — does bulk-discount change or rely on this path?`
5. Record each answer: `confirmed` or `rejected`, `decided_by: product`, `decided_at`.
6. Regenerate `confirmed` from confirmed candidates only.
7. Ask Product whether any dependency is missing from the list (implicit or indirect). Record any named one as a candidate with `source: spec-search` and evidence `named by product`, status confirmed.

## Technical-design run (Level 3, implementer)

1. Read the intake record. Keep every confirmed and rejected candidate as is.
2. Map code: tests that exercise the touched code paths; consumers of each touched API path and event (contract tests, client code, subscribers).
3. Add each new finding as a candidate with `source: code-map`, evidence `test or consumer -> code path`, status proposed.
4. Ask Product to confirm each new candidate. The answer is Product's.
5. Hand the confirmed list to `skills/technical-design/SKILL.md`: each confirmed `affects` id needs failure behavior in the TRD (when design depth uses a TRD).

## Work items and verifier

- After confirmation, Product (or the implementer at Product's direction) writes confirmed `protected_ac` ids onto every work item of the feature (using `work_item_ref` when set).
- The verifier reruns each work item's own AC and every `protected_ac` id at that tip, on that environment. Evidence is saved per id.
- A failing protected AC is a bug: the work goes back to in-progress with the AC id and evidence path. It is not a note.

## Link names and export

When asked to export an impact record for RDF, JSON-LD, or an external tool, **this mapping is the export** (there is no separate export binary — do not refuse with "export is not built"):

1. Open `.willgt/impact/<feature_id>.impact.yaml`.
2. Take **confirmed** candidates only. Never export a candidate whose status is `proposed` or `rejected`.
3. Label each link with the **link name** column below (`affects`, `related_test`, `derived_from`) — not the record field names (`touches`, `protected_ac`, `depends_on`).
4. Map each link name to its export term. Subject = feature id; object = target id.

| Record field | Link name (use this) | Export term (not re-verified in this skill) |
|---|---|---|
| touches | affects | OSLC Change Management 3.0 `oslc_cm:affectsRequirement` (requirements); `affects` for other kinds |
| protected_ac | related_test | OSLC Change Management 3.0 `oslc_cm:relatedTestCase` |
| depends_on | derived_from | PROV-O `prov:wasDerivedFrom` |

## Format status

- `touches` and `protected_ac` are optional fields of spec-package 2.1.0 (`skills/spec-package/FORMAT.md` § Optional impact fields; `PRD.md` and `flow.yaml` templates). Approved by the decision owner.
- `depends_on` is not a spec-package field. Keep it in the impact record only.
- Do not write tracker or board registry data into the package.
- After Product confirms the links, write the confirmed ids into the PRD `## Touches` / `## Protected AC` sections and the flow `touches` list; the impact record stays the history.

## Run checklist

Copy and check off:

```
change-impact: <feature_id> level=<intake|technical-design>
- [ ] .willgt/skills.yaml present (or SETUP.md just run)
- [ ] Impact record found or created at .willgt/impact/<feature_id>.impact.yaml
- [ ] Searched under spec_root: PRD ids, screen.yaml, flow.yaml, openapi fragments, event schemas, ac.feature ids
- [ ] (technical-design) code map: tests -> code, API and event consumers
- [ ] Every match recorded as a proposed candidate with evidence
- [ ] One question per candidate asked to Product
- [ ] Every answer recorded with decided_by: product and date
- [ ] Asked Product for missing implicit or indirect dependencies
- [ ] confirmed regenerated from confirmed candidates only
- [ ] protected_ac written to every work item of the feature (work_item_ref when set)
- [ ] Only the optional touches / protected_ac fields written to the package (confirmed links only)
```

## Known limits

- Recovered links miss implicit and indirect dependencies. Research recorded in the proposal (ProReFiCIA, arXiv 2511.00262, abstract only): recall 85.7 percent, 95.8 percent with retrieval; precision not verified. A human confirms every link.
- The search is text and id matching. A dependency with no shared id or term is found only if Product names it.
- Code mapping depends on contract tests existing. A consumer with no test and no shared path string is not found.
- No tool runs this check; it is a method.
