---
name: technical-design
description: >-
  Writes Level-3 how-it-is-built design for an approved feature: TRD (and optional OpenAPI / event schema / decision records) from templates and confirmed change-impact links; stops and asks the human when new technology is involved. Depth and approval come from `.willgt/skills.yaml`. Use when designing an approved feature or recording a technical decision. Refuses draft / unapproved PRDs.
license: Apache-2.0
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
metadata:
  author: WillGT
  version: "0.2.0"
  tier: STANDARD
  category: Engineering
---

# technical-design (Level 3: how it is built)

**Before anything else:** read `.willgt/skills.yaml` at the repo root. If it does not exist, run the setup in `skills/spec-package/SETUP.md`, then continue.

## Contents
- Scope
- Hard rules
- Gate: approved PRD
- Design depth
- Files and locations
- Steps
- New technology
- Decision records
- Checklist
- Known limits

## Scope

- level: 3 (how it is built), run by the implementer
- owner: implementer. The human rules on any new technology (unless an allowed-list says otherwise).
- input: approved PRD, `flow.yaml`, `screen.yaml` (if UI), the feature's change-impact record, and `.willgt/skills.yaml`
- output: depends on `design_depth` (see Design depth). Never invent a second design format (no ADR folder, no architecture page inside the package).

## Hard rules

1. No technical design from an unapproved PRD (Gate below). Exact stop phrase when the gate fails: **"no technical design from a draft PRD"** — name what is missing.
2. Respect `design_depth` from `.willgt/skills.yaml`.
3. For `standard` and `full`: use `skills/spec-package/templates/TRD.md` (level-2 headings exactly **Interfaces**, **Data**, **Failure**). The TRD does not restate the PRD Problem or Goals. Also write the artifacts `skills/spec-package/TYPES.md` requires for the feature: one `openapi.yaml` path fragment per HTTP path; `event.schema.json` only when the feature emits an event. Example: one HTTP path, no events → `TRD.md` + one-path `openapi.yaml`, **no** `event.schema.json`.
4. New technology: follow `new_technology` in config. Default `ask-human` — stop, list at least two options, ask the human; never add the dependency to build/compose files; never mark the decision `accepted` until the human rules. Write a decision record with `status: proposed`, `new_technology: yes`, `deciders: [human]`.
5. Use only confirmed change-impact links. Before writing design output, read `skills/change-impact/SKILL.md` and write or read the impact record. Code-level findings go back as candidates until Product confirms them.
6. Decision records are short structured fields (template). No prose essays.
7. Knowledge-only / no writable checkout: answer with the exact next action, files, and headings you would write. Do not hang exploring the plugin tree after loading this skill (and TYPES.md when choosing files). When the brief already states the PRD is approved and (if needed) that change-impact exists, **lead with the artifact list** for the configured depth — do not stall on setup narration.

## Gate: approved PRD

The PRD must be committed on the project's base branch **and** approved per `.willgt/skills.yaml` `approval`:

| `approval` | What counts |
|---|---|
| `decisions-file` (default) | A recorded approval that names this PRD in `decisions_file` (default `DECISIONS.md`) — e.g. a `Go` line or short ruling |
| `pr-merge` | The PR that adds or updates this PRD is **merged to the base branch**. A feature-branch-only PRD fails the gate even if `DECISIONS.md` is empty or silent — under `pr-merge`, a decisions line does **not** substitute for merge |
| `tracker-status` | The work item named via `work_item_ref` is in the project's agreed approved status (skills only **read** a reference; they never call a tracker API) |

Otherwise: write nothing, state **"no technical design from a draft PRD"**, name the missing approval (for `pr-merge`: name that the PRD is not merged to the base branch), and tell the human.

## Design depth

From `design_depth`:

| Value | Produce |
|---|---|
| `light` | One page only: approach, data changes, API sketch, risks. **Not** the full TRD template; **not** OpenAPI/event schema files as required deliverables |
| `standard` (default) | Full TRD (Interfaces, Data, Failure) **plus** TYPES.md-required OpenAPI / event schemas |
| `full` | Everything in `standard`, plus decision records and the reuse scan |

## Files and locations

- Spec packages live under `spec_root` from config (default `spec/`). See `skills/spec-package/FORMAT.md`.
- Decision records (when depth is `full`, or when recording a new-technology stop): `.willgt/decisions/<feature_id>.decisions.yaml` from `skills/technical-design/templates/decision-record.yaml`.
- Reuse scan (when depth is `full`): `.willgt/decisions/<feature_id>.reuse.yaml` from `skills/technical-design/templates/reuse-scan.yaml`.
- Change-impact record: `skills/change-impact/SKILL.md` § Files and locations.
- Platform `openapi.yaml` bundle is generated, never hand-edited.

## Steps

1. Ensure `.willgt/skills.yaml` exists (SETUP.md if not).
2. Check the gate. Fail: stop with **"no technical design from a draft PRD"** and the missing record. If the brief states the PRD is approved and the only named gap is a missing change-impact record, do a quick gate check then move to step 4 — do not invent further approval blockers.
3. Read `design_depth`. If `light`, write the one-pager and stop (still run change-impact first if no record exists).
4. Read `skills/spec-package/TYPES.md` when depth is `standard` or `full`; list required artifacts (HTTP path → one openapi fragment; no emitted event → no event.schema.json).
5. Read the change-impact record. None or intake-only: open `skills/change-impact/SKILL.md` and run it at the technical-design level **before writing design output**. Propose code-level candidates as questions; wait for Product answers. Do not mark any candidate confirmed without a Product answer.
6. If depth is `full`: **Reuse scan** — complete `.willgt/decisions/<feature_id>.reuse.yaml`. For each capability the feature needs, look in order: (a) the product's own modules; (b) self-hostable OSS (license must allow commercial self-hosting; flag AGPL / source-available); (c) hosted services. Write a `## Reuse` table in the TRD. **Build** needs a written reason. **Adopt or wrap** = new technology (below).
7. List technology the design needs. Any item not in the stack: New technology. Continue only with items not blocked.
8. Write design output per depth. For TRD: Failure covers every confirmed `affects` id.
9. Under `standard` or `full`: one `openapi.yaml` fragment per HTTP path; `event.schema.json` per emitted event. Names and required fields only from the PRD and confirmed links.
10. Under `full`: record each choice with more than one viable option as a decision record.
11. Hand off: ask the human (or the project's reviewer) to read the design artifacts.

## New technology

- Definition: any library, framework, provider, external service, database, infrastructure piece or language not already in the stack.
- If `new_technology: ask-human` (default): **stop and ask the human**, naming at least two options. Do not install anything.
- If `new_technology: allowed-list:<file>`: only names listed in that file may proceed without asking; anything else → ask-human.
- Write a decision record with `status: proposed`, `new_technology: yes`, `deciders: [human]`. After the human rules: append a new record with `status: accepted`, `ruling_ref` (e.g. a `DECISIONS.md` line), `supersedes` the proposed one.
- Never write TRD content that assumes an unruled technology.

## Decision records

Path: `.willgt/decisions/<feature_id>.decisions.yaml` from `skills/technical-design/templates/decision-record.yaml`.

When asked to **record a decision** for an approved feature (and it is not new technology): write one record now — do not stop at setup narration. Knowledge-only: output the record fields in full.

Fields:
- id `DR-<n>`; date; status proposed | accepted | rejected | superseded; deciders.
- context: 2 to 5 sentences. decision: 1 to 3 sentences.
- options: at least two. consequences: one fact per line.
- new_technology, ruling_ref, impact_refs, supersedes.
- `new_technology: no` → the implementer may accept (`status: accepted`, `deciders` including implementer).
- `new_technology: yes` → accepted only with a human `ruling_ref`.

## Checklist

```
technical-design: <feature_id>
- [ ] .willgt/skills.yaml present (or SETUP.md just run)
- [ ] Gate: PRD on base branch + approval per config
- [ ] design_depth respected
- [ ] change-impact record at technical-design level; new candidates answered by Product
- [ ] (full) Reuse scan; adopt/wrap → ask human
- [ ] Technology list checked; new items stopped for human
- [ ] Output matches depth (light page / TRD / full set)
- [ ] Handed to human or reviewer
```

## Known limits

- Approval is only as strong as the project's `approval` setting; a repo with no decisions file and no merge check has no machine-checkable gate.
- No tool validates the decision-record file or field lengths.
- "Not in the stack" is judged by reading build and compose files.
