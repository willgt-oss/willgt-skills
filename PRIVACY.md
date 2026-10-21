# Privacy policy — Spec & Impact (willgt-skills)

**Effective:** October 20, 2026 · **Publisher:** WillGT

## Summary
Spec & Impact collects nothing, sends nothing and stores nothing outside your own project.

## What the plugin is
Three Claude Code skills (`spec-package`, `change-impact`, `technical-design`) made of Markdown instructions, templates and one local check script. It has no MCP servers, hooks, connectors or background processes.

## Data it handles
- **Reads:** files in the project you open with Claude: spec files (PRD, acceptance tests, flows, screen and API contracts) and your `.willgt/skills.yaml` settings.
- **Writes:** the same kinds of files inside your project (for example `spec/…`, `.willgt/impact/…`, `.willgt/decisions/…`), only when you ask Claude to.
- **Personal data:** none is requested or collected. If your own spec files contain personal data, it stays in your project.

## What it sends
- Nothing to WillGT or any third party. The plugin makes no network calls of its own.
- Your conversation with Claude is handled by Anthropic under Anthropic's terms and privacy policy, as with any Claude use.

## Retention
WillGT receives no data from the plugin, so it retains none.

## Children
The plugin is a software-development tool and is not intended for users under 18.

## Changes and contact
Changes to this policy are published in this file and noted in `CHANGELOG.md`. Questions: open an issue or a discussion at https://github.com/willgt-oss/willgt-skills.
