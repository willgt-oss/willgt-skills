# Spec & Impact

*by WillGT · plugin id `willgt-skills`*

Three Claude Code skills that turn a vague feature idea into a spec an AI agent can build against, show what the change touches, and design the build.

**Created by WillGT.** · License: **Apache-2.0** · Version 0.1.0 · Website: https://willgt-oss.github.io/willgt-skills/ (how it works, eval results, verification record, launch post)

| Skill | What it does |
|-------|--------------|
| `spec-package` | A repo-local, executable spec for a feature: PRD, Gherkin acceptance tests, flows, screen contracts, API fragments |
| `change-impact` | Finds the existing requirements, screens, flows, APIs, events and tests a new feature may touch. You confirm each link |
| `technical-design` | Writes the "how it is built" design for an approved feature, at the depth you chose |

## What you can build with it

- **An executable spec for a feature.** A folder in your repo with a PRD, acceptance tests in Gherkin, flows, screen contracts and API fragments. An AI agent or a developer implements against it. "Done" means the acceptance tests pass, not that someone says so.
- **A change-impact record.** Before anyone builds, you get a list of the existing requirements, screens, APIs and tests the new feature may touch. You confirm or reject each one. Confirmed tests become protected: they must still pass.
- **A technical design.** A TRD (Interfaces, Data, Failure), OpenAPI and event fragments, decision records and a reuse scan. How much you get depends on the depth you chose: `light`, `standard` or `full`.

### How the three chain

```
define            find what it touches      design the build        implement
spec-package  ->  change-impact         ->  technical-design    ->  make the failing
(PRD, AC, flows)  (confirmed links)         (TRD, API, decisions)   acceptance tests pass
```

1. `spec-package` defines the work and the acceptance tests.
2. `change-impact` searches the existing specs and proposes what the feature touches. You confirm each link.
3. `technical-design` reads the confirmed links and designs the build. It refuses to start from a PRD that is not approved.
4. The implementer works until the committed acceptance tests go from failing to passing, without editing their assertions.

You can use each skill alone.

## Install

Requires [Claude Code](https://claude.com/claude-code). Then:

```bash
claude plugin marketplace add willgt-oss/willgt-skills
claude plugin install willgt-skills@willgt-skills
```

Skills live under `skills/<name>/` and follow the [Agent Skills](https://agentskills.io) layout (`SKILL.md`).

You also need a git repo for your project. Acceptance tests run with your own test runner (for example Playwright, Jest, pytest, kotlin-test or Maestro). The skills do not install one.

## Use it in Cursor

The skills follow the open [Agent Skills](https://agentskills.io) format, so Cursor loads them from your project:

```bash
mkdir -p .cursor/skills
cp -R path/to/willgt-skills/skills/* .cursor/skills/
```

Tested on October 20, 2026 with the Cursor Agent CLI and its default model:

| Behavior | Result |
|---|---|
| Picks change-impact on its own for "I want to add 2FA, what does it touch?", lists each link with file:line evidence and asks you to confirm each one | pass |
| Refuses to close a feature on "tests pass" without runner output and a RED baseline | pass |
| Refuses a technical design when the PRD is not on the base branch and approved | pass |
| Runs the first-run setup one question at a time | pass |

Use Agent mode so the skills can write `.willgt/skills.yaml` and the impact and decision records; Ask mode only reads.

## First run

The first time any of the three skills runs in a repo, it asks six setup questions, one at a time. Press Enter to accept the default. It then writes **`.willgt/skills.yaml`** at the repo root. Commit that file so every agent in the repo sees the same answers.

| # | Question | Default | Key |
|---|----------|---------|-----|
| 1 | Where should spec packages live? | `spec/` | `spec_root` |
| 2 | Where do you track work items? `none`, `file`, `github-issues`, `jira`, `linear`, `other:<name>` | `none` | `work_tracker` (+ `work_item_ref`) |
| 3 | What counts as "approved to design/build"? A decisions file, a PR merge, or a tracker status | decisions file (`DECISIONS.md`) | `approval` (+ `decisions_file`) |
| 4 | How deep should technical design go? `light`, `standard`, `full` | `standard` | `design_depth` |
| 5 | New libraries or services: always ask you, or allow a list from a file? | ask you | `new_technology` |
| 6 | Which test runner runs acceptance tests? | `auto` | `test_runner` |

The file looks like this:

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

The skills only read a work-item reference from this file. They never call a tracker API.

To change your answers, say **"reconfigure spec & impact"**. The full schema is in `skills/spec-package/SETUP.md`.

## Quick start (5 minutes)

Example feature: password reset. Open Claude Code in your repo and type these prompts, one at a time.

1. `Run the Spec & Impact first-run setup.`
   Answer the six questions (or press Enter six times). A file appears: `.willgt/skills.yaml`.

2. `Use spec-package to define a "password reset" feature: user asks for a reset link by email, opens it, sets a new password. Include the deny paths.`
   Files appear under your `spec_root` (default `spec/`), started from the package templates: a PRD with requirement ids, a `flow.yaml`, an `ac.feature` with Given/When/Then scenarios, and an API fragment for the reset endpoints. If the feature has a screen, a `screen.yaml` is needed too. Read them. Say go, change or stop.

3. Record your approval the way you chose in setup. With the default, add a line to `DECISIONS.md` that names the password reset PRD and says Go.

4. `Run change-impact for password-reset at intake.`
   A file appears: `.willgt/impact/password-reset.impact.yaml`. The skill asks you one question per candidate, for example: "Does password-reset change or rely on POST /login (spec/.../openapi.yaml:12)?" Answer each one. Then it asks if any dependency is missing.

5. `Use technical-design for password-reset.`
   With the default depth you get a TRD with Interfaces, Data and Failure, plus one API fragment per HTTP path. If the design needs a new library or service (an email provider, say), the skill stops and asks you to choose between options. It writes a decision record with status `proposed` in `.willgt/decisions/password-reset.decisions.yaml`.

6. Hand the package path to your agent or developer: `Implement password-reset from <spec path>. Make the committed acceptance tests pass without editing their assertions.`

## How each skill works

### spec-package

**Use it when:** you start a feature, fill in the spec, hand work to an implementer, or check that work is done.

**It produces:** a package folder in your repo. Examples: `PRD.md`, `PRODUCT.md`, `DESIGN_BRIEF.md`, `flow.yaml`, `screen.yaml`, `ac.feature`, an executable acceptance test, `products.yaml`, design tokens and component contracts. Not every feature needs every file. `TYPES.md` says which files each feature type needs (`backend`, `fullstack`, `dashboard_screen`, `landing_page`, `sellable_module`, `agentic`).

**Hard rules it enforces:**
- A handoff carries a package path and a screen id, not acceptance criteria pasted into chat.
- Done means the package's acceptance tests pass, shown by real runner output. A claim is not enough.
- A changed assertion in the acceptance file, compared with its failing commit, is a finding.
- The tests are written and committed failing before implementation, by someone other than the implementer.
- A human approves the package before implementation starts (go, change or stop). Silence is not approval.
- A design-tool link or a preview page is never the contract. If `screen.yaml` is missing, it stops.
- The files win. A status or checklist that disagrees with them is wrong.

### change-impact

**Use it when:** a feature is taken in, and again before technical design. It answers: what existing behavior can this change break?

**It produces:** an impact record at `.willgt/impact/<feature_id>.impact.yaml`. Each candidate has a kind, a target id, a link type (`affects`, `derived_from`, `related_test`), and the file and line it was found at. Confirmed `protected_ac` ids are listed for the verifier to rerun.

**Hard rules it enforces:**
- Nothing is linked without your confirmation. Every candidate starts as `proposed`.
- Each candidate is asked as one question that names the target and its evidence.
- Candidates are never deleted. A rejected one never appears in the confirmed list.
- Code-level findings are added as new candidates. They never replace a confirmed link.
- A failing protected acceptance test is a bug, not a note.

It searches by text and ids. A dependency that shares no id or term with the feature is found only if you name it.

### technical-design

**Use it when:** a feature's PRD is approved and you need to design how it is built, or you need to record a technical decision.

**It produces, by depth:**
- `light`: one page with approach, data changes, API sketch and risks.
- `standard`: a TRD with Interfaces, Data and Failure, plus the OpenAPI path fragments and event schemas the feature type requires.
- `full`: all of `standard`, plus decision records and a reuse scan (your own modules first, then self-hostable open source, then hosted services).

**Hard rules it enforces:**
- No technical design from a draft PRD. It says so and names the missing approval.
- It uses only change-impact links you confirmed.
- New technology (any library, framework, provider, service, database or language not already in the stack) stops the work. It lists at least two options and asks you. It never edits build files. It never marks the decision accepted until you rule.
- Decision records are short structured fields, not essays.
- Every confirmed `affects` link needs failure behavior in the TRD.

## Quality

Before release, the skills went through these checks:

- **Validation.** `claude plugin validate --strict` and the Agent Skills reference validator (`skills-ref validate`).
- **Anthropic skill checklist.** Each skill was reviewed against Anthropic's "Checklist for effective Skills" (description, body length, one-level reference files, examples).
- **Evals against a no-skill baseline.** Eval cases for each skill live in `evals/`. Each is run with the skill and without it, and the results are compared.

  Results for v0.1.0 (32 cases, 3 runs each, Claude Code's plugin eval tool with a no-skill baseline arm):

  | Skill | Cases | Score with skill | Score without skill | Cases fully passing |
  |---|---|---|---|---|
  | change-impact | 7 | 100% | 0% | 7 / 7 |
  | technical-design | 7 | 100% | 0% | 7 / 7 |
  | spec-package | 18 | 94% | 0% | 17 / 18 |

- **Security review.** The tree was scanned for secrets and private terms, and read for hidden instructions. The skills are readable text and templates.

## What it does not do

- It makes no network calls of its own. It sends and fetches nothing.
- It never installs anything. New technology is a question to you.
- It never invents approvals. Approval comes from your decisions file, a PR merge, or a tracker status you named.
- It does not call a tracker API. It only stores and reads a reference.
- It is not a project-management tool, a planner or an orchestrator. It does not decide what to build or who builds it.
- No CI enforces the package format, and no `ready` or `impact` command exists. The skills are methods that Claude follows.

## Using it in your company / forking

Any organization may use or fork this Apache-2.0 tree. When you fork or redistribute:

- Keep `LICENSE` and `NOTICE`, and the existing copyright headers.
- Mark each file you changed with a notice that it was changed.
- Rename the fork. Use "WillGT" only to describe the origin, for example "based on Spec & Impact by WillGT". Do not use it as your product name.
- State in your README that the work is based on https://github.com/willgt-oss/willgt-skills under Apache-2.0.

## Collaborate

Want to collaborate or partner? Reach us on GitHub: open an issue or a discussion.

Contributing: see `CONTRIBUTING.md`. Contributions are made under the terms in `CLA.md`.

## Security

Report vulnerabilities privately with GitHub private vulnerability reporting: Security, then Report a vulnerability. Do not open public issues for security problems. See `SECURITY.md`.

## Privacy

Spec & Impact collects, sends and stores nothing outside your project. See [`PRIVACY.md`](PRIVACY.md).

## License and trademark

Licensed under the Apache License 2.0. See `LICENSE` and `NOTICE`.

"WillGT" is a trademark of WillGT. The license grants no trademark rights. You may say your work is "Created by WillGT" or "Built with WillGT" when it uses these skills, and link to this repository. Anything that implies endorsement or official status needs written permission. See `TRADEMARKS.md`.

Copyright 2026 WillGT. Created by WillGT.
