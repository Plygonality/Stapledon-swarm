#!/usr/bin/env python3
"""Calculation and table-consistency checks. Not a prose linter."""

from __future__ import annotations

import math
import pathlib
import re
import sys

from lightsail import AU, C, G0, S_SUN, boost_to_beta, reference_family, sail_diameter_m

ROOT = pathlib.Path(__file__).resolve().parents[1]


def near(a: float, b: float, rel: float = 0.01, abs_tol: float = 0.0) -> bool:
    return abs(a - b) <= max(abs_tol, rel * max(abs(a), abs(b)))


def check_geometry() -> list[str]:
    errors = []
    expected = {
        1.0: (10.0, 3.57, 1.0, 2.0, 100.0),
        5.0: (50.0, 7.98, 5.0, 10.0, 500.0),
        10.0: (100.0, 11.28, 10.0, 20.0, 1000.0),
    }
    for row in reference_family():
        area, diam, sail, total, power = expected[row["body_g"]]
        got = (
            row["area_m2"],
            row["diameter_m"],
            row["sail_g"],
            row["total_g"],
            row["P_gw"],
        )
        if not near(got[1], diam, rel=0.002):
            errors.append(f"diameter {row['body_g']}g: {got[1]} != {diam}")
        if got[0] != area or got[2] != sail or got[3] != total or got[4] != power:
            errors.append(f"family row {row['body_g']}g: {got} != {(area, diam, sail, total, power)}")
        if not near(sail_diameter_m(area), diam, rel=0.002):
            errors.append("diameter formula mismatch")
    return errors


def check_boost() -> list[str]:
    errors = []
    b = boost_to_beta(0.002, 1.0e11)
    expect = {
        "t_launch_s": 226.0,
        "tau_s": 225.0,
        "t_emit_s": 202.0,
        "x_million_km": 7.31,
        "x_au": 0.049,
        "a0_g": 34000.0,
    }
    if not near(b["t_launch_s"], expect["t_launch_s"], rel=0.01):
        errors.append(f"t_launch {b['t_launch_s']}")
    if not near(b["tau_s"], expect["tau_s"], rel=0.01):
        errors.append(f"tau {b['tau_s']}")
    if not near(b["t_emit_s"], expect["t_emit_s"], rel=0.02):
        errors.append(f"t_emit {b['t_emit_s']}")
    if not near(b["x_million_km"], expect["x_million_km"], rel=0.005):
        errors.append(f"x_million_km {b['x_million_km']}")
    if not near(b["x_au"], expect["x_au"], rel=0.03):
        errors.append(f"x_au {b['x_au']}")
    if not near(b["a0_g"], expect["a0_g"], rel=0.01):
        errors.append(f"a0 {b['a0_g']}")
    if b["t_emit_s"] >= b["t_launch_s"]:
        errors.append("emission duration should be shorter than launch-frame time")
    if abs(b["x_m"] / AU - b["x_au"]) > 1e-9:
        errors.append("AU conversion")
    # diffraction
    airy = 2.44 * 1e-6 * b["x_m"] / 5000.0
    if not near(airy, 3.57, rel=0.01):
        errors.append(f"airy {airy}")
    return errors


def check_coast() -> list[str]:
    errors = []
    gamma = 1.0 / math.sqrt(1.0 - 0.04)
    t = 982.0 / 0.2
    tau = t / gamma
    if not near(t, 4910.0, abs_tol=0.01):
        errors.append(f"coast years {t}")
    if not near(tau, 4811.0, rel=0.001):
        errors.append(f"coast proper {tau}")
    if int(2085 + t) != 6995 or int(2095 + t) != 7005:
        errors.append("passage window")
    flux = 0.26 * S_SUN / (3.6**2)
    if not near(flux, 27.3, rel=0.005):
        errors.append(f"flux {flux}")
    ke_1g = (gamma - 1.0) * 0.001 * C * C
    if not near(ke_1g, 1.85e12, rel=0.02):
        errors.append(f"KE 1g {ke_1g}")
    return errors


def check_readme_table() -> list[str]:
    """Authoritative README binding table must not publish obsolete arrival/transit as current."""
    errors = []
    text = (ROOT / "README.md").read_text()
    # Isolate the binding table.
    m = re.search(r"## 5\. Binding numbers(.*?)## 6\.", text, re.S)
    if not m:
        return ["README binding table missing"]
    block = m.group(1)
    if "7191" in block or "5,106" in block or "0.001 g" in block:
        errors.append("README binding table still publishes obsolete transit")
    if "6995" not in block or "27.3" not in block:
        errors.append("README binding table missing new work figures")
    return errors


def check_epochs() -> list[str]:
    prod = (ROOT / "bible/production.md").read_text()
    ids = re.findall(r"`(construction|operational|relic)`", prod)
    extra = set(re.findall(r"`epoch`[^`]*`([a-z_]+)`", prod))
    errors = []
    if not {"construction", "operational", "relic"}.issubset(set(ids)):
        errors.append("production missing an epoch id")
    return errors


def main() -> int:
    errors = []
    for fn in (check_geometry, check_boost, check_coast, check_readme_table, check_epochs):
        errors.extend(fn())
    if errors:
        print("FAIL")
        for e in errors:
            print(" ", e)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
