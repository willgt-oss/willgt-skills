# FORMAT — the package contract


## Contents
- 1. Binding a package to a project
- 2. Files
- Shared registry files (2026-10-04)
- 3. Ownership summary
- 4. CI gates — target, not live
- 5. Changing this format

> **Requires first:** `SKILL.md` (scope and hard rules). **Related:** `TYPES.md` decides which of
> these files a given feature actually needs. No CI validates the package. Existing screens are not
> backfilled when a template is added.

File-by-file. Projects that adopt the format share this contract. Changes here affect every project
using it — see § Changing this format.

---

## 1. Binding a package to a project

The package root and AC runner come from **`.willgt/skills.yaml`** (`spec_root`, `test_runner` —
see `SETUP.md`), never hardcoded in a guide, template or brief:

```yaml
# .willgt/skills.yaml (excerpt)
spec_root: spec/          # package root under the repo
test_runner: auto         # or playwright | jest | pytest | kotlin-test | maestro | other:<cmd>
```

A project with no `.willgt/skills.yaml` (or no `spec_root`) has not adopted this format yet — run
`SETUP.md` first. The format is opt-in per project.

---

## 2. Files

### `catalog/products.yaml` — Product owns writes

Commercial meaning. What a buyer gets, and what that entitles them to.

```yaml
products:
  - id: the-product-core
    name: the product Core
    offers:
      - id: pro-monthly
        price_id: <billing provider price id>
        delivery_mode: ai          # ai | specialist | hybrid
        grants:
          - mod.voice
          - host.analytics
```

- `grants[]` **must be a subset of** the runtime catalog (`module_feature_catalog`). Runtime is the
  truth; this file is the commercial claim about it.
- **No layout here.** If a field describes where something appears, it belongs in `screen.yaml`.

### `design/tokens.json` — Design owns writes

Design tokens. Consumed by implementation and lint. A project adopting an existing token set points
at it rather than re-authoring.

### `design/components/*.yaml` — Design owns writes

Closed component contracts: the variants and states that exist. Closed means an implementation may
not invent a variant that is not listed.

### `design/CATALOG.md` — Design owns writes (index)

Human + agent index of **stable catalog ids** → yaml path → surfaces. Required once a project has
more than a handful of components. DESIGN BRIEFs and `screen.yaml` regions **compose ids from this
index**; they do not invent parallel widgets. Missing id → `proposed:<Name>` + Design adds yaml
before Eng treats the screen as ready — not freestyle markup in the brief.

**Architecture default:** one platform DS + optional **palette overlays** (rebind semantic tokens).
Surface kits (`kit.landing`, `kit.builder`, …) are compose indexes, not forked design systems.

### `screens/<screen_id>/screen.yaml` — Design owns writes

Export only after DESIGN BRIEF → human `/design` or `/design-sync` (see IMPLEMENTATION.md §2 step 3). Pre-human yaml is draft, not Eng input.

The UI contract that agents actually read. `screen_id` is stable and is the ID used in every brief.
Every `regions[].component` (and pattern-level bindings) **must** be a catalog id present under
`design/components/` (or explicitly `proposed:` only while a catalog-pass brief is open).

```yaml
screen_id: products-home
route: /app
personas: [tenant_admin]
regions:
  - id: product_list
    component: ProductCard
    repeats: products.yaml#products
actions:
  - id: cta_manage
    triggers: navigate(screen: module-detail)
```

IDs in `regions[]` and `actions[]` are referenced by AC, so renaming one breaks its test — which is
the intended coupling.

**Every error state names its real trigger, and says whether it is a failure.** A `screen.yaml`
`states:` entry that describes an error or refusal must say, in plain words, what actually causes
it — the real condition, read off the real code or API contract, not a guess ("a slug with no
matching client", "the write failed server-side", "the session lost reach to this client mid-page"
— not just "an error occurs"). Next to that, the entry says which of the two kinds of state it is:

- **Expected/designed** — this state is a normal, intended outcome of a normal input (a typo'd
  URL, a deliberately denied write, a card that's correctly not entitled). Seeing it is not a bug.
- **FAILURE on an otherwise-healthy page** — this state firing for a session or input that
  *should* have worked cleanly is a defect to catch, not a state to silently render through.

A state can be both, for different triggers — say so for each one, not as a single blanket label
on the whole state. This exists because of a real, live miss: `tenant-path-routing`'s own error
state correctly described *what the error looked like* ("Unknown tenant host") but never said
*which trigger made it a failure* versus *which trigger made it expected* — so when a code path
regressed and started firing it for healthy sessions, nothing in the spec said that was wrong, and
it shipped to staging uncaught. Every screen's own existing error states should be checked against
this convention going forward, not only new ones written after this line was added.

### `screens/<screen_id>/ac.feature` — Design/Product sign

Observable behavior in Given/When/Then. Must include deny paths, not only happy paths.

```gherkin
Feature: Products home
  Scenario: Entitled module is manageable
    Given the client is entitled to "mod.voice"
    When they open "/app"
    Then the "mod.voice" card shows action "Manage"

  Scenario: Unentitled module cannot be enabled from the UI alone
    Given the client is not entitled to "mod.voice"
    When they open "/app"
    Then the "mod.voice" card shows action "Enable"
    And activating it opens confirmation before any write
```

Signed means a named person accepted it. Unsigned AC does not gate anything.

### `screens/<screen_id>/<ac runner file>` — executable AC

Written **failing first**, by someone other than the implementer. The implementer makes that same
file pass **without editing its assertions**. Changing a Then-clause to force a pass is the failure
mode this exists to prevent.

The filename follows the project's runner binding — `ac.spec.ts` for Playwright, a Kotlin test class
for mobile.

### `screens/<screen_id>/preview.html` — optional, humans only

*(Optional by design. The decision owner approval gate — `IMPLEMENTATION.md` §2 step 4a — can be satisfied by a
rendered preview, a Claude Design canvas link, or the contract explained in plain terms. What matters
is that the decision owner is asked before effort is spent, not which artifact does the asking.)*

A rendered preview for people to look at. **Never an implementation target.** An agent pointed at
this instead of `screen.yaml` is the wrong contract.

### v2 — `PRD.md`, `DESIGN_BRIEF.md`, `flow.yaml`

Templates: `templates/PRD.md`, `templates/DESIGN_BRIEF.md`, `templates/flow.yaml`,
`templates/TRD.md`, `templates/openapi.yaml`, `templates/event.schema.json`.
`evals/check-templates.py` fails when a template is missing the fields below. Existing screens are
not backfilled.

| File | Relates to `PRODUCT.md` | Relates to the others |
|------|-------------------------|------------------------|
| `PRD.md` | Formalises `PRODUCT.md`. Same intent, as requirement ids. | Each requirement lists `ac_ids`. It does not replace `ac.feature`. |
| `DESIGN_BRIEF.md` | Experience and constraints taken from that intent. | Input to Design only. Never an implementer target. Not `screen.yaml`. |
| `flow.yaml` | The screens that intent crosses. | Nodes are `screen_id`. Each edge has `trigger`, `guard`, and `effect`. `effect: no write` is a real value. Not a design brief and not an API schema. |

`PRODUCT.md` stays the prose intent for a screen. The PRD is the id-joined card. They must not contradict. A design brief is not an implementer input. A flow does not author tokens, motion, or brand hex.

### Technical files — `TRD.md`, `openapi.yaml`, `event.schema.json`

implementer owns writes. `TYPES.md` decides when a feature needs each file. A feature with no interface, no HTTP path, and no event does not get them. Existing screens are not backfilled.

| File | Required shape |
|------|----------------|
| `TRD.md` | Interfaces, data, and failure behavior. It does not restate the PRD. |
| `openapi.yaml` | One path fragment. Not the bundled `spec/api/openapi.yaml`. |
| `event.schema.json` | One event. Names the event and its required fields. |

**Migration:** existing packages keep the files they already have. Add a PRD, design brief, or flow when that capability is in scope. Add a TRD, an OpenAPI fragment, or an event schema only when `TYPES.md` says the feature needs it. Do not backfill untouched screens.

---

### Optional impact fields — `touches`, `protected_ac` (2.1.0)

Both are optional. A package without them stays valid; existing files are not backfilled. They record what a new feature affects, so a change to existing behavior is checked before code exists (method: `skills/change-impact/SKILL.md`).

| Field | Where | Meaning |
|-------|-------|---------|
| `touches` | `PRD.md` (`## Touches` section, one id per line) and `flow.yaml` (top-level list) | Ids of existing requirements, screens, flows, API paths, events or AC the feature changes. Written only after Product confirms each link. |
| `protected_ac` | `PRD.md` (`## Protected AC` section) | Existing AC ids that must stay green. Copied onto every work item of the feature; the verifier reruns them with that item's own AC. |

Values are ids that exist in the package, never prose. Names follow OSLC Change Management 3.0 (`touches` = affects, `protected_ac` = relatedTestCase). `depends_on` is not part of the format.

## Shared registry files (2026-10-04)

Parallel packages must not edit one shared file, or every parallel merge conflicts (11 of 22 the product merges did, all on two files).

- **AC runner projects** are discovered from the package folders (one project per folder that has an AC runner file), not listed by hand in the runner config. A new package adds no config line.
- **API schemas** live per package as `<package>/openapi.yaml` fragments. The platform file (e.g. `spec/api/openapi.yaml`) is generated by a bundler and never hand-edited. Two fragments defining the same path or schema differently fail the preflight.
- **Database migrations (Flyway) use timestamp versions, not "the next integer".** A new migration is named `V<YYYYMMDDHHMM>__<what>.sql` (UTC, minute precision; add seconds if two land in one minute). Two packages written in parallel then never claim the same number, and ordering follows authoring time. Existing `V<n>` files keep their names; a project switches by making its next migration timestamped (set `outOfOrder` if a late-merging older timestamp must still apply). Until a project switches, the merge script's collision check applies.

Until a project has the bundler and discovery, merges use the project merge playbook, which unions both files mechanically.

## 3. Ownership summary

| File | Owns writes | Reads it |
|---|---|---|
| `catalog/products.yaml` | Product | implementation, CI grant check |
| `design/tokens.json` | Design | implementation, lint |
| `design/components/*.yaml` | Design | implementation, CI |
| `screens/<id>/screen.yaml` | Design | implementation, review |
| `screens/<id>/ac.feature` | Design / Product | AC author, implementation |
| `screens/<id>/<ac file>` | AC author (RED) → implementer (GREEN) | review, CI |
| `TRD.md` | implementer | implementation |
| `openapi.yaml` | implementer | bundler, implementation |
| `event.schema.json` | implementer | implementation |
| `preview.html` | Design | humans |

Cross-links are by **ID** — `screen_id`, grant keys, catalog keys, region and action ids. No role
needs to hold all files in their head; the IDs are the joins.

---

## 4. CI gates — target, not live

**No CI enforces any of this today.** When built:

1. Schema-validate `screen.yaml` and `products.yaml`
2. Every `grants[]` entry exists in the runtime catalog
3. Touched **and regression** AC green
4. No `preview.html` referenced from any brief or PR description

Until then these are manual checks, and the AC re-run at tip is the real enforcement point.

---

## 5. Changing this format

Every project that uses this format reads this file, so a change affects them all.

- During an active comparison window, this file is **frozen**. Fixing a genuine error is allowed;
  changing what the format means is not.
- Any change lands with its evals updated in the same commit.
- Adding a file type or a required field is a breaking change for existing packages — state a
  migration or don't make it.
