"""Existing geometry / boost / coast / table checks, collected as pytest."""

from __future__ import annotations

import pytest

from check_consistency import (
    check_boost,
    check_coast,
    check_epochs,
    check_geometry,
    check_readme_table,
    check_unit_canon_table,
)

CHECKS = (
    check_geometry,
    check_boost,
    check_coast,
    check_readme_table,
    check_epochs,
    check_unit_canon_table,
)


@pytest.mark.parametrize("fn", CHECKS, ids=lambda f: f.__name__)
def test_consistency_check(fn) -> None:
    errors = fn()
    assert errors == [], "\n".join(errors)
