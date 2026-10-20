# SPDX-License-Identifier: Apache-2.0
#!/usr/bin/env python3
"""Fail when the v2 templates are missing their required fields."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "templates"


def fail(msg: str) -> None:
    print(f"FAIL {msg}", file=sys.stderr)


def check_prd(text: str) -> list[str]:
    errors = []
    if "PRODUCT.md" not in text:
        errors.append("PRD.md does not say it formalises PRODUCT.md")
    rows = re.findall(r"^\|\s*(REQ-\d+)\s*\|.*\|\s*([^|]+)\|", text, re.M)
    if not rows:
        errors.append("PRD.md has no requirement_id rows")
    for req_id, ac_cell in rows:
        ac_ids = re.findall(r"AC-\d+", ac_cell)
        if not ac_ids:
            errors.append(f"PRD.md {req_id} is not linked to an AC id")
    # optional impact fields (2.1.0): present and marked optional, never required
    for heading in ("Touches", "Protected AC"):
        if not re.search(rf"^## {heading} \(optional\)\s*$", text, re.M):
            errors.append(f"PRD.md is missing '## {heading} (optional)'")
    return errors


def check_design_brief(text: str) -> list[str]:
    errors = []
    if not re.search(r"^## Experience\s*$", text, re.M):
        errors.append("DESIGN_BRIEF.md is missing ## Experience")
    if not re.search(r"^## Constraints\s*$", text, re.M):
        errors.append("DESIGN_BRIEF.md is missing ## Constraints")
    if not re.search(r"Design only", text) or not re.search(
        r"[Nn]ever an implementer target", text
    ):
        errors.append(
            "DESIGN_BRIEF.md does not say it is Design only and never an implementer target"
        )
    return errors


def check_flow(text: str) -> list[str]:
    errors = []
    if not re.search(r"(?m)^nodes:\s*$", text):
        errors.append("flow.yaml is missing nodes")
    screen_ids = re.findall(r"(?m)^\s+- screen_id:\s+\S+", text)
    if not screen_ids:
        errors.append("flow.yaml nodes are missing screen_id")
    if not re.search(r"(?m)^#\s*touches \(optional\)", text):
        errors.append("flow.yaml does not document the optional touches field")
    if not re.search(r"(?m)^edges:\s*$", text):
        errors.append("flow.yaml is missing edges")
    blocks = re.split(r"(?m)^\s+- ", text.split("edges:", 1)[-1] if "edges:" in text else "")
    ok_edge = False
    no_write = False
    for block in blocks:
        has = all(re.search(rf"(?m)^\s*{name}:\s+\S", block) for name in ("trigger", "guard", "effect"))
        if has:
            ok_edge = True
        if re.search(r"(?m)^\s*effect:\s+no write\s*$", block):
            no_write = True
    if not ok_edge:
        errors.append("flow.yaml has no edge with trigger, guard, and effect")
    if not no_write:
        errors.append('flow.yaml has no edge whose effect is "no write"')
    return errors


def check_trd(text: str) -> list[str]:
    errors = []
    if "implementer owns writes" not in text:
        errors.append("TRD.md does not say implementer owns writes")
    if not re.search(r"does not restate the PRD", text):
        errors.append("TRD.md does not say it does not restate the PRD")
    for heading in ("Interfaces", "Data", "Failure"):
        if not re.search(rf"^## {heading}\s*$", text, re.M):
            errors.append(f"TRD.md is missing ## {heading}")
    return errors


def check_openapi(text: str) -> list[str]:
    errors = []
    if not re.search(r"(?m)^openapi:\s+\S+", text):
        errors.append("openapi.yaml is missing an openapi version")
    if not re.search(r"(?m)^paths:\s*$", text):
        errors.append("openapi.yaml is missing paths")
    paths = re.findall(r"(?m)^  /\S+:\s*$", text)
    if len(paths) != 1:
        errors.append(f"openapi.yaml must contain one path, found {len(paths)}")
    if not re.search(r"Not the bundled spec/api/openapi\.yaml", text):
        errors.append("openapi.yaml does not say it is not the bundled spec/api/openapi.yaml")
    return errors


def check_event(text: str) -> list[str]:
    errors = []
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        return [f"event.schema.json is not JSON: {exc}"]
    name = data.get("title")
    if not isinstance(name, str) or not name.strip():
        errors.append("event.schema.json does not name the event")
    required = data.get("required")
    if not isinstance(required, list) or not required or not all(isinstance(item, str) and item for item in required):
        errors.append("event.schema.json has no required fields")
    return errors


def main() -> int:
    checks = {
        "PRD.md": check_prd,
        "DESIGN_BRIEF.md": check_design_brief,
        "flow.yaml": check_flow,
        "TRD.md": check_trd,
        "openapi.yaml": check_openapi,
        "event.schema.json": check_event,
    }
    errors: list[str] = []
    for name, fn in checks.items():
        path = ROOT / name
        if not path.is_file():
            errors.append(f"missing template {name}")
            continue
        errors.extend(fn(path.read_text()))
    if errors:
        for err in errors:
            fail(err)
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
