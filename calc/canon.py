"""Unit-canon lengths for calc/.

Import the four scale measures. Do not copy them into this repo as owned numbers.

Local physics constants live in lightsail.py (c, g0, AU, IAU solar constant).
Unit-canon has no fields for those. That is not a scale override.
"""

from __future__ import annotations

from unit_canon import load

CANON = load()

METERS_PER_GRID = CANON.meters_per_grid
DECK_HEIGHT = CANON.deck_height
AIRLOCK_DIAMETER = CANON.airlock_diameter
HUMAN_FIGURE_M = CANON.human_figure.standing_height

UNIT_CANON_KEYS = {
    "meters_per_grid": METERS_PER_GRID,
    "deck_height": DECK_HEIGHT,
    "airlock_diameter": AIRLOCK_DIAMETER,
    "human_figure.standing_height": HUMAN_FIGURE_M,
}
