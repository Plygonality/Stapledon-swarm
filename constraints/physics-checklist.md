# Physics checklist

Reject a still, graph, or brief that fails a row. Work figures are CANON. Catalog values that differ get a note. They do not get used.

## Binding work figures

| Check | Pass | Fail |
| --- | --- | --- |
| Distance Sol → Kepler-62 | 982 ly | "nearby"; 1200 ly NASA press figure used as the work distance |
| Peak and coast speed | 0.2c, labeled as peak and as coast | 0.2c as trip-average; 982 yr at 0.2c; "cruise at 0.2c is wrong" |
| Acceleration | ~0.001 g bang-coast-bang | 1 g for years; continuous 0.2c burn |
| Transit time | ~5,106 yr external / ~5,008 yr proper | 982 yr (light-travel); "a few centuries" |
| Launch window | 2085–2095 CE founding dispatch | 3000 CE as the founding launch |
| Star mass / luminosity | 0.76 M☉ / 0.26 L☉ work figures | Sol twins; catalog 0.69 M☉ / ~0.21 L☉ used as if they replace the work figures |
| Swarm outer radius | 3.6 AU | 1 AU "Earth analog"; Dyson shell at the HZ |
| Flux at 3.6 AU | ≈ 0.020 S☉ | 1 S☉ panels; blue-white key |
| Teq work figure | ~120 K | shirtsleeve exterior; Earth-daylight grade |
| Scale | Unit-canon only | magic lengths in graphs |

## Transit arithmetic (INFERENCE from the binding row)

Special-relativistic constant proper acceleration ≈ 0.001 g, stationary endpoints:

```
v_peak = v_coast = 0.2 c
α      ≈ 0.001 g
t_burn, external ≈ 197.7 yr each (boost, then brake)
s_burn           ≈ 20.0 ly each
s_coast          ≈ 982 − 40.0 ≈ 942.1 ly
t_coast          ≈ 942.1 / 0.2 ≈ 4710.2 yr
t_total, external ≈ 197.7 + 4710.2 + 197.7 ≈ 5105.7 yr
τ_total, proper   ≈ 5007.9 yr
clock difference  ≈ 97.9 yr
```

γ(0.2c) ≈ 1.021. Time-dilation on the coast is a few percent. Leave it off stills. Dormancy is not dilation. Clock frames: Gregorian CE in a Sol-barycentric frame; onboard proper time; experienced time. Hardware that keeps those clocks is OPEN.

Light-travel Sol → Kepler-62 is 982 yr. Radio reply ~1964 yr. No live talk.

A 2090 departure arrives around 7196. Confirmation sent then can reach Sol around 8178. An immediate reply can reach Kepler around 9160.

Nearby hops use the same α and stop at the destination. A 4.24 ly hop peaks at ~0.066c and cannot reach 0.2c. A 100 ly hop does reach 0.2c.

A later 0.5c hop at the same α takes ~2,483 yr. A 3000 CE example arrives around 5483. That row is representative, not a second founding launch.

Dispatch in 2085–2095 is not the same as finishing acceleration in that decade. A Kepler-class boost lasts ~198 external years.

## Flux and temperature

```
F / F_earth ≈ L / r² = 0.26 / 3.6² ≈ 0.020 S☉
```

~120 K is the look-dev work figure. You do not re-fit a blackbody every pass. Bare 4π absorber at 0.020 S☉ sits colder (~105 K at A = 0). Sun-facing plate sits warmer. Waste heat, view factor, coating: OPEN. Do not "correct" 120 K in a brief.

Exterior is IR-dark. Work lights carry the visible key. Star is a K2 disk.

## Mass table (correction)

Sphere area at R = 3.6 AU:

```
4πR² ≈ 3.64 × 10²⁴ m²
```

| Thickness | Fill | Mass order | Status |
| --- | --- | --- | --- |
| 1 mm | 1% of sphere | ≈ 0.012 M⊕ | CANON correction. Use this. |
| 1 m | 1% of sphere | ≈ 12 M⊕ | CANON. This is what 12 M⊕ bought. |

The old 12 M⊕ @ 1 mm figure swapped millimeters and meters. Delete it if it comes back.

Implied mean density for 0.012 M⊕ @ 1 mm @ 1% is ~2 g cm⁻³. INFERENCE. Not a material spec. Alloy / ice / slag mix is OPEN.

1 mm at 1% is cheap in planetary mass. 1 m at 1% is a small planet taken apart. Do not draw both on one budget.

## Geometry

- Independently orbiting cells. No rigid shell. No ringworld.
- Outer radius 3.6 AU. Interior of that sphere may be occupied. The bound is the outer edge.
- Kepler-62b–f orbit well inside 3.6 AU (published a ≤ 0.72 AU). They are not the swarm. They are not the large key-art body.
- One Habitat-kit build is **one cell**.
- Cells specialise. The featured relic cell is one computing habitat.

## Payload class

| Allowed on the 0.2c hop | Rejected |
| --- | --- |
| Gram-probes | Living crew as the hop design |
| Dormant WBE and ASI states | Generation ship |
| Digital archives | Named passengers, factions, chapels on the hull |
| Selective authorised activation | A civilisation running on one gram-probe |

WBE that wake into meat at destination is OPEN. Do not draw a nursery to close it.

Picotechnology: picometre precision, atomic and molecular working machines. A few-picometre complete robot fails.

Interstellar gas and dust at 0.2c are a damage term. Ignore-erosion briefs fail.

## Lighting and thermal failures

| Symptom | Likely fault |
| --- | --- |
| Exterior reads as Earth noon | Flux ignored; Sol lighting on a Kepler cell |
| Gold foil + deep blue shadows as default "space" | Palette standing in for 0.020 S☉ |
| Breathable balcony, no visor, no heat | 120 K ignored |
| Star is white and small like Sol | K2 / 0.26 L☉ ignored |
| Cell spans kilometers with no joints | Unit-canon / one-cell rule ignored |
| Large planet-shaped body labeled 62e or 62f | Key-art retcon |
| Large irregular silhouette captioned as a planet | Fights `stills/01-eclipse.jpg` / `03-inward.jpg` |
| Distant diamond marks treated as the Habitat-kit mesh | Scale / one-cell rule ignored |
| Relic cell captioned as the dead swarm | Featured-cell rule ignored |

## Scale

Do not copy these into node trees. Read [Unit-canon](https://github.com/Plygonality/Unit-canon):

| Measure | Work value | Owner |
| --- | --- | --- |
| Grid | 1.0 m | Unit-canon |
| Deck | 3.0 m | Unit-canon |
| Airlock | 1.0 m | Unit-canon |
| Human figure | 1.80 m | Unit-canon |
