"""Unit-canon is the owner of grid / deck / airlock / figure."""

from __future__ import annotations

import json
from pathlib import Path

from canon import UNIT_CANON_KEYS
from unit_canon import load

ROOT = Path(__file__).resolve().parents[2]
CALC = ROOT / "calc"


def test_imported_lengths_match_unit_canon_file() -> None:
    item = load()
    assert UNIT_CANON_KEYS["meters_per_grid"] == item.meters_per_grid
    assert UNIT_CANON_KEYS["deck_height"] == item.deck_height
    assert UNIT_CANON_KEYS["airlock_diameter"] == item.airlock_diameter
    assert UNIT_CANON_KEYS["human_figure.standing_height"] == item.human_figure.standing_height


def test_constraint_unit_canon_figures_match_import() -> None:
    physics = json.loads((ROOT / "constraints" / "physics.json").read_text(encoding="utf-8"))
    owned = [fig for fig in physics["figures"] if fig.get("owner") == "unit-canon"]
    assert {fig["unit_canon_key"] for fig in owned} == set(UNIT_CANON_KEYS)
    for fig in owned:
        expected = UNIT_CANON_KEYS[fig["unit_canon_key"]]
        assert fig["value"] == expected, f"{fig['id']}: {fig['value']} != {expected}"


def test_calc_imports_unit_canon_or_documents_local_physics() -> None:
    canon_src = (CALC / "canon.py").read_text(encoding="utf-8")
    assert "from unit_canon import" in canon_src
    lightsail_src = (CALC / "lightsail.py").read_text(encoding="utf-8")
    assert "LOCAL PHYSICS" in lightsail_src
    assert "Unit-canon" in lightsail_src
    for name in ("METERS_PER_GRID", "DECK_HEIGHT", "AIRLOCK_DIAMETER", "HUMAN_FIGURE"):
        assert name not in lightsail_src
