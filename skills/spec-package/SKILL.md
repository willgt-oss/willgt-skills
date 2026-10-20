---
name: spec-package
description: >-
  Repo-local executable specification package format: package layout, types, runners, and implementation loop so agents implement against signed AC colocated with the code. Use when adopting the format, filling package cells, handing off implementation, or verifying done via green AC.
license: Apache-2.0
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
metadata:
  author: WillGT
  version: "2.1.0"
  tier: STANDARD
  category: Engineering
---

# spec-package — the work-definition format

**Before anything else:** read `.willgt/skills.yaml` at the repo root. If it does not exist, run the setup in `skills/spec-package/SETUP.md`, then continue. Packages live under `spec_root` (default `spec/`). Acceptance runs use `test_runner` (default `auto`).

> **This file is the entry point — read it before FORMAT, IMPLEMENTATION, TYPES or RUNNERS.**
> No CI enforces the package. The `ready` / `impact` CLIs and the feature graph **do not exist**.

**Provides capability:** `spec-package`  
**Version:** 2.1.0  
**Status:** Format locked · v2 templates · no CI enforces it

## Contents
- Why this exists
- The package
- Hard rules
- Adopting in a repo — design conformance and existing code
- Routing
- Scope — what this is not
- Known limits

A repo-local specification package that coding agents implement against. It defines **what work is**,
not who runs the agents. The same format applies whether one human or many agents do the work.

---

## Why this exists

Three failures it removes, each observed:

1. **Agents cannot reliably "see" a design** from an HTML path, a Figma URL, or prose in a chat.
2. **Product intent gets reinvented** as entitlement matrices or ad-hoc tables each sprint.
3. **"Done" is argued rather than demonstrated** — a screenshot, a claim, a status label.

The package answers each with a file: the contract is committed, the acceptance test is executable,
and "done" is that test passing.

---

## The package

Path is bound per project — never hardcoded. See `FORMAT.md` for the full file-by-file contract.

```
catalog/products.yaml       Product → Offer → delivery_mode → grants[]   — Product owns writes
design/tokens.json          design tokens                                — Design owns writes
design/components/*.yaml    closed component contracts                   — Design owns writes
screens/<screen_id>/
  PRODUCT.md                screen intent (prose)                        — Product owns writes
  PRD.md                    requirement ids, each linked to AC ids       — Product owns writes
  DESIGN_BRIEF.md           experience and constraints                    — Design input only
  flow.yaml                 screen_id nodes; edges trigger/guard/effect   — Product owns writes
  screen.yaml               the UI contract agents read                  — Design owns writes
  ac.feature                Gherkin Given/When/Then                      — Design/Product sign
  ac.spec.ts                executable AC: RED first, then GREEN
  preview.html              HUMANS ONLY — never a brief target
```

**The AC runner is per project.** `ac.spec.ts` is the web/Playwright binding; a mobile project binds
a different runner in the same slot. The filename varies — the rule does not: **executable AC,
colocated with the thing it proves.**

---

## Hard rules

1. **Briefs carry a package path + `screen_id`.** Never prose AC pasted into chat, never a Figma URL,
   never `preview.html` as an implementation target.
2. **Done = that package's AC is GREEN**, proven by runner output — never by a verbal "tests pass" or
   "looks like the design". Before closing work: (a) run the package AC runner or read its real
   output file; (b) diff the acceptance file against its RED commit and treat any changed assertion
   as a finding; (c) say which layer was proven. Do not mark done on a report alone.
3. **Runtime grant truth stays in code** (`module_feature_catalog`). `products.yaml` `grants[]` must
   be a subset of it.
4. **Regression is caught by each feature's own colocated AC**, not by a person remembering an
   earlier feature.
5. **Design tools are optional and export-only** — Figma and Claude Design are places to design; they
   write *into* package files (`screen.yaml`, tokens, catalog). A Figma URL is never an implementer
   handoff. If `screen.yaml` is missing or the export-to-git step was skipped: **stop**; do not brief
   or hand off anyone; ask for the export to land first. A visual preview is not the implementation
   contract.
6. **Human design pass before implementer handoff.** Step 3 is DESIGN BRIEF → human `/design` or
   `/design-sync` → then `screen.yaml` export. An agent **cannot** run those human commands. Yaml
   written from a ticket (or by an agent) **before** that human result is **draft/reference only** —
   not signed implementer input. **Refuse** to hand off the implementer from pre-human yaml; ask for
   the design brief and the human design result first.
7. **The files win.** Any status, board or checklist that disagrees with the package is wrong and is
   re-derived, never reconciled by hand.
8. **Templates are checked by script, not by eye.** Before shipping a template change, run
   `evals/check-templates.py` (this skill's folder). It fails on a PRD requirement without an AC id, a
   DESIGN_BRIEF.md missing Experience or Constraints or the "Design only" line, and a flow node
   without `screen_id` or an edge without trigger, guard and effect. Fix the template; never waive a
   missing field.

---

## Adopting in a repo — design conformance and existing code

Adopting the format, in order:

1. **Bind it.** Read `.willgt/skills.yaml` (run `SETUP.md` if it is missing) so `spec_root` and `test_runner` are set.
2. **Seed `products.yaml` from what the project grants today**, not from plans.
3. **Do not backfill.** Screens nobody is changing stay unspecified until someone touches them; then that screen gets its package. Packages written for untouched screens record assumptions nobody verified.
4. **Adoption is complete when one feature has gone end to end** (package → RED → GREEN), not when the folders exist.

AC proves behavior, not that a screen uses the catalog and tokens. A product can pass every AC while its UI uses one-off components and a token points at a value that does not exist. So, from the first package:

- **Lint is on from day one:** every semantic token resolves; every `component:` in a `screen.yaml` exists in the catalog; app code has no raw colors or sizes and imports the shared library. Gate for new work; a baseline file for older code.
- **The shared component library is built with the first screens**, one implementation per catalog contract, tokens only.
- **Generate a visual page from tokens + contracts** for review. It shows broken tokens and missing components that reading YAML does not.

---

## Routing

| You want to | Read |
|---|---|
| First-run questions and `.willgt/skills.yaml` | `SETUP.md` |
| The file-by-file contract, schemas, ownership | `FORMAT.md` |
| Which cells a feature needs — types, `n/a` vs missing | `TYPES.md` |
| Which AC runner a project uses, adding one | `RUNNERS.md` |
| Starting a package file | `templates/` |
| Run a project with this — adopt it, build a feature end to end | `IMPLEMENTATION.md` |
| Know what to work on next / who to brief | `IMPLEMENTATION.md` § Finding the next gap |
| Check behavior is correct | `evals/evals.json` |

---

## Scope — what this is not

- **Not a project-management tool.** It says nothing about spawning, assigning or tracking workers.
- **Not a planner.** A list of gaps is not a plan. Deciding *what* to build and in what order stays
  with humans.
- **Not universal.** Feature and screen work fits. Infra, research, incidents and triage do not —
  handle those with the project's usual process.

## Known limits

- No CI enforces any gate; the schemas in `FORMAT.md` are written but unenforced.
- The `ready` / `impact` CLIs described as future work **do not exist**. Gap-finding is manual.
- v2 templates are not backfilled onto existing screens. A screen keeps its current files until that screen is in scope.
