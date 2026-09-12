#!/usr/bin/env python3
"""Reference integrator for the adopted laser-driven lightsail launch family.

Stdlib only. Prints geometry and the boost to β = 0.2 under the bible's
force convention. Not a mission simulator.

Convention
----------
P  nominal beam power crossing a stationary plane over the sail's projected
   area, assuming beam containment. Not automatically intercepted power under
   every optical convention, and not transmitter output after losses.

F(β) = (2P / c) * (1 - β) / (1 + β)   ideal receding reflector
d(γ m v) / dt = F(β)
dx / dt = v
"""

from __future__ import annotations

import math

C = 299792458.0
G0 = 9.80665
AU = 149597870700.0
YEAR = 365.25 * 86400.0
S_SUN = 1361.0  # IAU nominal solar constant, W/m²


def sail_diameter_m(area_m2: float) -> float:
    return 2.0 * math.sqrt(area_m2 / math.pi)


def force_beta(P_w: float, beta: float) -> float:
    return (2.0 * P_w / C) * (1.0 - beta) / (1.0 + beta)


def dt_dbeta(m_kg: float, P_w: float, beta: float) -> float:
    F0 = 2.0 * P_w / C
    return (m_kg * C / F0) * (1.0 + beta) ** (-0.5) * (1.0 - beta) ** (-2.5)


def proper_time_s(m_kg: float, P_w: float, beta: float) -> float:
    F0 = 2.0 * P_w / C
    return (m_kg * C / F0) * beta / (1.0 - beta)


def simpson(func, a: float, b: float, n: int = 20000) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    total = func(a) + func(b)
    for i in range(1, n):
        x = a + i * h
        total += (4.0 if i % 2 else 2.0) * func(x)
    return total * h / 3.0


def boost_to_beta(m_kg: float, P_w: float, beta_f: float = 0.2) -> dict:
    t = simpson(lambda b: dt_dbeta(m_kg, P_w, b), 0.0, beta_f)
    x = simpson(lambda b: b * C * dt_dbeta(m_kg, P_w, b), 0.0, beta_f)
    tau = proper_time_s(m_kg, P_w, beta_f)
    t_emit = t - x / C
    gamma = 1.0 / math.sqrt(1.0 - beta_f * beta_f)
    ke = (gamma - 1.0) * m_kg * C * C
    a0 = force_beta(P_w, 0.0) / m_kg
    return {
        "t_launch_s": t,
        "tau_s": tau,
        "t_emit_s": t_emit,
        "x_m": x,
        "x_million_km": x / 1.0e9,
        "x_au": x / AU,
        "a0_g": a0 / G0,
        "gamma": gamma,
        "ke_j": ke,
        "e_nominal_emit_j": P_w * t_emit,
        "e_nominal_tlaunch_j": P_w * t,
    }


def reference_family() -> list[dict]:
    rows = []
    intensity = 10.0e9  # W/m²
    sigma = 0.1  # g/m² sail-system areal density
    for body_g in (1.0, 5.0, 10.0):
        area = body_g / sigma
        sail_g = body_g
        total_g = body_g + sail_g
        P_w = intensity * area
        rows.append(
            {
                "body_g": body_g,
                "area_m2": area,
                "diameter_m": sail_diameter_m(area),
                "sail_g": sail_g,
                "total_g": total_g,
                "P_gw": P_w / 1.0e9,
                "boost": boost_to_beta(total_g / 1000.0, P_w),
            }
        )
    return rows


def main() -> None:
    print("Reference family (ideal reflection, 10 GW/m², 0.1 g/m² sail system)")
    print(
        f"{'body':>6} {'area':>8} {'diam':>8} {'sail':>6} {'total':>6} {'P':>8}"
    )
    for row in reference_family():
        print(
            f"{row['body_g']:5.0f}g {row['area_m2']:7.0f}m² "
            f"{row['diameter_m']:7.2f}m {row['sail_g']:5.0f}g "
            f"{row['total_g']:5.0f}g {row['P_gw']:7.0f}GW"
        )
    b = reference_family()[0]["boost"]
    print()
    print("Boost to 0.2c (same P/m for every row)")
    print(f"  launch-frame duration     {b['t_launch_s']:.3f} s")
    print(f"  onboard proper time       {b['tau_s']:.3f} s")
    print(f"  transmitter emission      {b['t_emit_s']:.3f} s")
    print(f"  distance                  {b['x_million_km']:.2f} million km ({b['x_au']:.4f} AU)")
    print(f"  initial acceleration      {b['a0_g']:.0f} g")
    print(f"  kinetic energy (2 g stack) {b['ke_j']:.3e} J")
    print(f"  nominal beam energy P·t_em {b['e_nominal_emit_j']:.3e} J")
    flux = 0.26 * S_SUN / (3.6**2)
    print()
    print(f"Kepler-62 flux at 3.6 AU (0.26 L☉, S☉={S_SUN:.0f} W/m²): {flux:.2f} W/m²")
    gamma = 1.0 / math.sqrt(1.0 - 0.04)
    print(f"982 ly at 0.2c: {982/0.2:.0f} yr external, {982/0.2/gamma:.1f} yr proper")


if __name__ == "__main__":
    main()
