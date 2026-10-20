# TYPES — feature types and what each requires


## Contents
- 1. The distinction that matters
- 2. Types
- 3. Agentic features — open problem
- 4. How types change
- 5. Using a type

> **Reality check (2026-09-21).** The type rows below are **provisional** — refined by retro, not
> designed up front. A type nobody has built is a hypothesis. The `agentic` type is explicitly
> unsettled (§3). No package exists yet, so no type has been exercised on real work.
> **Requires first:** `SKILL.md` (scope). **Used by:** `IMPLEMENTATION.md` § Finding the next gap.

Not every feature needs every part of the package. A landing page needs Marketing and no commerce; a
backend endpoint needs neither Marketing nor Design. Without types, a gap check reports "missing" for
things that were never applicable, and the checklist cries wolf until people stop reading it.

A feature declares its `type`. The type decides which cells are **required**, which are
**not applicable**, and therefore who owns the work.

---

## 1. The distinction that matters

| State | Meaning | Blocks? |
|---|---|---|
| **Required, filled** | Done | no |
| **Required, empty** | A real gap — brief the owner | **yes** |
| **Not applicable** | This type does not use that cell | no |

`products.yaml` with no Offer is a **gap** for a sellable module and **not applicable** for an
internal dashboard screen. Same empty file, different verdict. Never treat "not applicable" as done
— it is a third state, and a checklist that collapses it into either of the others is lying.

---

## 2. Types

**Provisional.** These required-sets are a starting point, not a finished taxonomy. They are refined
by retro — see §4. If a type's row is wrong in practice, that is a retro finding, not a reason to
improvise around it.

| Type | Commerce | Marketing | Design | Eng | AC | Notes |
|---|---|---|---|---|---|---|
| `backend` | n/a | n/a | n/a | required | required | API, job, migration. No UI surface, so no `screen.yaml`. |
| `fullstack` | n/a | n/a | required | required | required | The common case: a screen plus the backend behind it. |
| `dashboard_screen` | n/a | n/a | required | required | required | Internal or tenant UI. Not sold on its own. |
| `landing_page` | n/a | **required** | required | required | required | Public marketing surface. Copy, positioning and claims are Marketing's, not Design's. |
| `sellable_module` | **required** | optional | required | required | required | Has an Offer and `grants[]`. The only type where the commerce half of the format is exercised. |
| `agentic` | depends | depends | depends | required | **see §3** | New. Acceptance does not work the same way — treat as unsettled. |

A feature may be more than one type only if it genuinely is (a sellable module *with* a landing
page). Prefer splitting it into two features with their own ids.

---

## 3. Agentic features — open problem

A new type, and the one we understand least. Flagged rather than guessed.

**The acceptance model does not transfer.** Every other type proves itself with a deterministic test:
same input, same output, green or red. An agentic feature produces different output each run. A
Then-clause asserting exact output either fails constantly or is loosened until it asserts nothing.

So an agentic feature probably needs **evals** — behavioral assertions checkable from a transcript,
scored across runs — where other types need AC. That is a different artifact with a different pass
criterion, and this project already has an eval standard to borrow from
(`the project eval standard`).

Likely to need, unproven:

- Evals in place of, or alongside, executable AC
- The instruction or prompt artifact under version control, like any other contract
- Declared guardrails: what it must refuse, what it must not claim
- A cost and latency budget, since both are unbounded by default

**Do not finalise this row until a real agentic feature has been built.** Anything written now is a
guess with a table around it.

---

## 4. How types change

Through retro, not redesign.

1. A feature hits a gap the type did not predict — a required cell that was not applicable after all,
   or a role nobody thought to brief.
2. That becomes a retro finding, filed like any other.
3. At triage, the type's row is amended, or a new type is added.
4. The change lands with its evals updated in the same commit.

This is deliberate: the taxonomy is discovered from work that actually happened, not designed in
advance from imagined cases. A type nobody has built is a hypothesis.

---

## 5. Using a type

Declared on the feature, and it drives the gap check in `IMPLEMENTATION.md` § Finding the next gap:

```yaml
feature: products-home
type: dashboard_screen
```

The gap check then reports only on that type's required cells. Everything else is reported as
`n/a`, visibly — not hidden, so a wrong type is obvious rather than silent.

`TRD.md`, an `openapi.yaml` fragment, and an `event.schema.json` follow the same rule. A `backend`
or `fullstack` feature that exposes an interface needs the TRD. The OpenAPI fragment is required
only when that interface is one HTTP path. The event schema is required only when the feature emits
an event. A `dashboard_screen` or `landing_page` with no interface and no event does not get these
files. Existing screens are not backfilled.
