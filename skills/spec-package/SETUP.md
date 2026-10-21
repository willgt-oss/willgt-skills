# SETUP — first-run config for Spec & Impact

**Requires first:** nothing (this file is the bootstrap). **Used by:** `change-impact`, `technical-design`, `spec-package`.

Before any of the three skills does real work, read **`.willgt/skills.yaml`** at the repository root. If that file is missing, run this setup once, write the file, then continue. Say **"reconfigure spec & impact"** to ask the questions again and overwrite the file.

Skills only **read** tracker references from this file. They never call a tracker API.

---

## File schema (`.willgt/skills.yaml`)

```yaml
version: 1
spec_root: spec/                 # Q1 where spec packages live
work_tracker: none               # Q2 none | file | github-issues | jira | linear | other:<name>
work_item_ref: ""                # Q2b how a feature is named there, e.g. "GH issue #", "PROJ-123", or a file path
approval: decisions-file         # Q3 decisions-file | pr-merge | tracker-status
decisions_file: DECISIONS.md     # Q3b if decisions-file
design_depth: standard           # Q4 light | standard | full
new_technology: ask-human        # Q5 ask-human (default) | allowed-list:<file>
test_runner: auto                # Q6 auto | playwright | jest | pytest | kotlin-test | maestro | other:<cmd>
```

Commit this file with the project so every agent sees the same answers.

---

## Questions (ask one at a time)

Show the default in parentheses. Accept Enter for the default. Explain each in one line.

1. **Where should spec packages live?** (default `spec/`)  
   Directory under the repo root that holds feature packages (`PRD.md`, `screen.yaml`, AC, …).

2. **Where do you track features / work items?** (`none` / `file` / `github-issues` / `jira` / `linear` / `other:<name>`)  
   Skills only store a reference string; they do not call the tracker. If not `none`, also ask **Q2b**: how a feature is named there (e.g. `GH issue #`, `PROJ-123`, or a file path) → `work_item_ref`.

3. **What counts as "approved to design/build"?**  
   - `decisions-file` — a line in a decisions file (default `DECISIONS.md`; ask path → `decisions_file`)  
   - `pr-merge` — the PR that adds/updates the PRD is merged to the base branch  
   - `tracker-status` — a status on the work item named by `work_item_ref`

4. **How deep should technical design go?**  
   - `light` — one page: approach, data changes, API sketch, risks  
   - `standard` — full TRD template (Interfaces, Data, Failure)  
   - `full` — TRD + OpenAPI fragment + event schemas + decision records + reuse scan

5. **New libraries or services?**  
   - `ask-human` (default) — always stop and ask the human with options  
   - `allowed-list:<file>` — only names listed in that file may be added without asking

6. **Which test runner runs acceptance tests?** (`auto` by default)  
   `auto` | `playwright` | `jest` | `pytest` | `kotlin-test` | `maestro` | `other:<cmd>`

---

## After answers

1. Create `.willgt/` if needed.
2. Write `.willgt/skills.yaml` with `version: 1` and the six answers (plus Q2b / Q3b when applicable).
3. Tell the user the path and that they can re-run setup with **"reconfigure spec & impact"**.
4. Resume the original skill request using the new config.

---

## Defaults (Enter on every question)

```yaml
version: 1
spec_root: spec/
work_tracker: none
work_item_ref: ""
approval: decisions-file
decisions_file: DECISIONS.md
design_depth: standard
new_technology: ask-human
test_runner: auto
```
