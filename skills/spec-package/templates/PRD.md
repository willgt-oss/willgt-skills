# PRD — <capability>

Formalises `PRODUCT.md` for this capability. Product owns writes. This is the lean agent card: problem, goals, non-goals, and requirements. It is not a novel, and it is not `ac.feature`.

Each requirement has a `requirement_id`. Each requirement lists the `ac_ids` that prove it. An AC id with no requirement, or a requirement with no AC id, is incomplete.

## Problem

<who is blocked, and by what>

## Goals

- <outcome>

## Non-goals

- <explicitly out of this PRD>

## Touches (optional)

<!-- Existing ids this feature changes: requirement, screen_id, flow, API path, event, AC. One per line, only after Product confirmed each. Omit the section if none. -->

## Protected AC (optional)

<!-- Existing AC ids that must stay green. Copy them onto every work item as `protected_ac`; the verifier reruns them. Omit if none. -->

## Requirements

| requirement_id | statement | ac_ids |
|----------------|-----------|--------|
| REQ-001 | <observable requirement> | AC-001 |
