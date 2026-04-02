#!/usr/bin/env python3
"""Validate shared_data JSON files and, when available, validate content against schemas."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / "shared_data"
SCHEMAS = SHARED / "schemas"


def load_json(path: Path):
    return json.loads(path.read_text())


def main() -> int:
    for path in sorted(SHARED.glob("*.json")):
        load_json(path)
        print(f"OK JSON: {path.relative_to(ROOT)}")

    try:
        import jsonschema  # type: ignore
    except Exception:
        print("jsonschema not installed; skipped schema validation")
        return 0

    unit_schema = load_json(SCHEMAS / "unit.schema.json")
    detachment_schema = load_json(SCHEMAS / "detachment.schema.json")
    strat_schema = load_json(SCHEMAS / "stratagem.schema.json")

    for unit in load_json(SHARED / "units.json"):
        jsonschema.validate(unit, unit_schema)
    for det in load_json(SHARED / "detachments.json"):
        jsonschema.validate(det, detachment_schema)
    for strat in load_json(SHARED / "stratagems.json"):
        jsonschema.validate(strat, strat_schema)

    print("OK schema: units/detachments/stratagems")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
