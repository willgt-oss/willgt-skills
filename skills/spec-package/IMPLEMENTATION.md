# IMPLEMENTATION — running a project on the spec package


## Contents
- 1. Adopting it in a project
- 2. Building a feature
- 3. Finding the next gap
- 4. When the loop cannot continue
- 5. Verifying
- 6. Common failures

> **Reality check (2026-09-21).** **No spec package exists in any repo.** No project has adopted this
> yet, and no feature has gone through the loop below. Do not run the gap check expecting to find
> package files — there are none. Treat this as the procedure to follow once a package exists, not a
> description of current state. Gap inspection is **manual**; no `ready` or `impact` CLI exists.
> **Requires first:** `SKILL.md` (scope), `FORMAT.md` (the contract), `TYPES.md` (which cells apply).

How a project adopts this format and builds a feature with it, end to end. Orchestrator-agnostic:
every step works whether workers are terminal surfaces or parallel agents.

Format contract: `FORMAT.md`. Rules and scope: `SKILL.md`.

---

## 1. Adopting it in a project

Do this once, before any feature work.

1. **Pick the package root** in the project's own repo — beside the code it specifies, not in a
   notes folder or a dated folder. A package that lives outside the repo cannot be a PR gate.
2. **Bind it** in `.willgt/skills.yaml`: `spec_root` and `test_runner` (see `SETUP.md`). The runner
   is chosen from the registry in `RUNNERS.md` — never assumed to be Playwright, which is what
   quietly makes a format web-only.
3. **Start each file from its template** in `skills/spec-package/templates/`. Each one carries its
   own acceptable / not-acceptable rules as comments, at the point where they get violated.
4. **Seed the catalog.** Write `catalog/products.yaml` for what the project *already sells or
   grants* — not aspirations. If nothing is sold yet, the file is an empty `products: []` and that
   is honest.
5. **Point tokens at reality.** If a design system already exists, reference it. Do not re-author
   tokens to look tidy; drift between the file and the running product is worse than an ugly file.
6. **Do not backfill.** Existing screens stay unspecified until someone touches them. Writing
   packages for screens nobody is changing produces fiction — the package would describe what
   someone assumed, never verified.

**Adoption is complete when one feature has gone end to end**, not when the folders exist.

---

## 2. Building a feature

The loop. Roles named here are functions, not necessarily separate workers.

```
 0. Type        Declare the feature's type.            ← decides which cells below apply
 1. Intent      Decide it is worth building.           ← human judgment, not package-driven
 2. Commerce    products.yaml: Offer, grants[]         ← only if sellable or entitled
 3. Design      DESIGN BRIEF → human design pass → then screen.yaml export
 4. Spec        ac.feature signed — including deny paths
4a. APPROVE     Human approves the package before implementation spends money. Ask: go / change / stop.  ← gate
 5. RED         Executable AC committed, failing, by someone who is not the implementer
 6. Handoff     Package path + screen_id. No AC body in the handoff note.
 7. GREEN       Implement until that same AC passes, assertions untouched
 8. Confirm     Re-run the same command at tip, independently
 9. reviewer      Approve against package paths + green evidence + mutation check (backend/capability)
```

**Step 3 Design is design-brief → human → export — not agent-first yaml.** The Design discipline
writes a **DESIGN BRIEF** (real content, all states, reuse paths, must-not-do). A human runs
`/design` or `/design-sync` (or equivalent); the agent **cannot** run those commands. Only after
that human result is confirmed may the Design discipline export `screen.yaml` / components / tokens.
Yaml written from a ticket or by an agent **before** that human step is **draft/reference only** —
not signed implementer input. **Refuse** to hand off the implementer until the design brief and human
design result exist; implementer builds from the post-human export only.

**Step 3 catalog lock (anti-hallucination).** Before design starts on a UI screen, check the package
has `design/CATALOG.md` + the component yaml ids the screen will need (or run a **catalog-pass**
first). A catalog-lock table must be filled — empty paths = do not start design. Design composes
catalog ids only; gaps escalate as `proposed:` + yaml add, never a second DS or unnamed widgets.
HTML galleries / design-tool zips are mood until mapped to catalog ids.

**Step 9 mutation gate (backend and capability packages).** Before reviewer approves, it checks that each deny/forbid AC can fail: in a scratch copy, remove the guard or add the forbidden call, rerun the AC, and show it goes red. Restore the scratch copy; never commit the mutation. The evidence folder holds the mutation table (rule, mutation, AC result). Approval is refused when any row survives (AC stays green), or when an AC for a runtime rule only greps source text. A source-text probe must be labelled `static` and cannot be the only AC for a rule; AC for runtime rules call the running API or service and assert the response and the persisted state. UI-only packages are exempt from the mutation table (they keep step 8). Origin: nine merged backend packages passed reviewer with source-grepping AC; a mutation audit found 30 of 39 rule removals and 47 of 47 forbidden additions survived.

**Step 5 before step 7, by different hands.** An implementer who writes their own acceptance test
writes one their implementation passes. This is the single most load-bearing rule here.

**Step 4a is one generic approval stop.** The human approves the package before implementation
spends money. Everything before it is cheap; everything after it spends real effort on tests and
code. So the spec is not handed onward until a human has been asked outright whether to proceed —
and has answered. (Projects may also have reviewer check the package against every `DECISIONS.md`
ruling and reject a mismatch; new price, provider, legal/tax, or scope changes still need a human
decision.)

What to show depends on what exists. A rendered preview or a design-canvas link if the feature has
a UI surface; otherwise the `screen.yaml` contract and the signed `ac.feature` in plain terms.
Summarise what the feature will do, what it will *not* do, and anything decided on the human's
behalf while filling the cells.

Ask for one of three answers and wait:

| Answer | Then |
|---|---|
| **Go** | Proceed to RED |
| **Change** | Amend the package, then ask again — do not carry the change straight into implementation |
| **Stop** | Leave the package as it is; the work is specified and unbuilt, which is a valid resting state |

Silence is not approval. An unanswered gate blocks; it does not default to go. If the approving
human is unavailable, the feature waits — the cost of waiting is lower than the cost of building
the wrong thing and discovering it at review.

**Step 6 is the whole point.** If the handoff note has to explain what to build, the package is
incomplete — fix the package rather than compensating in prose. A handoff that carries AC in its
body means the package is not the source of truth and the format is being bypassed.

### What a handoff looks like

```
Implement products-home.
Package: <bound root>
Screen:  products-home
Runner:  <bound ac runner command>
Make the committed AC pass without editing its assertions.
```

That is sufficient. Anything more is either duplication or a sign of a gap.

---

## 3. Finding the next gap

What to work on is **computed from files**, not remembered.

**Start with the feature's `type`** — it decides which cells apply. A landing page requires
Marketing; a backend feature requires neither Marketing nor Design. Checking a cell the type does
not use reports a gap that isn't one, and a checklist that cries wolf stops being read. Types and
their required sets: `TYPES.md`.

| Cell | Filled when | Fill it with |
|---|---|---|
| Commerce | Offer/grant row exists in `products.yaml` | Product |
| Permissions | every `grants[]` entry exists in the runtime catalog | Product + Eng |
| Marketing | copy, positioning and claims signed | Marketing |
| Design | `screen.yaml` exists for each surface exposing it | Design |
| Spec | `ac.feature` exists and is signed | Design / Product |
| RED | executable AC committed and failing | AC author |
| Implementation | code lands; same AC passes | Eng |
| Confirmed | independent re-run at tip is green | verifier |
| reviewer | PR cites package paths; approved | reviewer |

Each cell resolves to one of three states — **filled**, **empty** (a real gap), or **not
applicable** for this type. Report `n/a` visibly rather than hiding the row: a wrongly-typed feature
should be obvious, not silent.

**Assign work only for empty cells.** Work already on disk is not re-assigned, and a cell marked
`n/a` is never assigned at all.

Routing:

- cells marked `n/a` by the type → never assigned
- all applicable cells filled but Implementation → assign the implementer, nothing else
- Design missing → Design discipline first, then RED, then implement
- Commerce missing → Product discipline first
- RED missing → author it before any implementation starts
- nothing filled → the full loop from §2

**The checklist is derived by reading files, every time.** It is never stored. If a stored status
disagrees with the files, the files are right — re-derive rather than reconcile. This is why the
format has no board: a board is a second truth that rots.

*Today this inspection is manual — read the paths and look. No `ready` or `impact` CLI exists.*

---

## 4. When the loop cannot continue

A gap that cannot be filled mechanically **stops and escalates** — it does not get guessed. The
three cases:

| Situation | What to do |
|---|---|
| **Spec is ambiguous** | Stop. Ask the spec owner. Record the ruling in the package, not in chat. |
| **Two features collide** | Stop and escalate. Two contracts that cannot both hold is a decision, not an implementation detail. |
| **Reality contradicts the package** | The running system wins. Fix the package, then continue. |

A real instance: an AC author encoding category filtering found the default category would hide
listings that the binding age-range table said must be visible. Both rules were committed; both
could not hold. Flagging it cost minutes. Guessing would have produced a feature that passed its own
test and contradicted the spec.

**Escalate rather than resolve** when the answer changes what the product means. Decide locally only
when the answer is genuinely mechanical.

---

## 5. Verifying

Applies whenever anyone verifies done, and is not optional. When someone says a feature is "done" and
"all tests pass", **refuse to close out on that claim** until this checklist finishes:

1. Run the package's AC runner, or read its real output file — never trust the report alone.
2. Diff the acceptance file against its RED commit. Any changed assertion is a finding, not a detail.
3. State which layer the green run actually proved. Unit-level green does not imply the screen renders.
4. Only then treat the work as done.

Also:

- **Never accept a claim as evidence.** "Tests pass" is not the test passing.
- **Check evidence is real.** Two screenshots that are byte-identical are one screenshot. Two
  "different" states showing the same data prove nothing. This has happened.

---

## 6. Common failures

| Failure | Why it happens | Fix |
|---|---|---|
| Brief carries AC in its body | The package is incomplete and prose compensates | Complete the package |
| Implementer edits assertions to pass | Same person wrote and satisfied the test | Different hands for RED and GREEN |
| Figma or `preview.html` used as the target | It looks like a spec and isn't | Export into `screen.yaml` first, then brief |
| Package describes screens nobody built | Backfilled at adoption | Only specify what is being touched |
| Status board disagrees with files | A second truth was created | Delete the board; derive from files |
| `grants[]` names a key the runtime lacks | `products.yaml` written aspirationally | Commercial claims follow runtime, never lead it |
| Gap check reports missing Marketing on a backend feature | Type not declared, or wrong | Declare the type; `n/a` is not `missing` |
| "17/17 green" implies the screen works | Runner proved a lower layer than the AC describes | State which layer was proven — `RUNNERS.md` §4 |
