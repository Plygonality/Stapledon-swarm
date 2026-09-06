# Physics checklist

Reject a still, graph, or brief that fails a row. Work figures are CANON. Catalog values that differ get a note. They do not get used.

## Binding work figures

| Check | Pass | Fail |
| --- | --- | --- |
| Distance Sol → Kepler-62 | 982 ly | "nearby"; 1200 ly NASA press figure used as the work distance |
| Peak speed | 0.2c, labeled peak | 0.2c as cruise; >0.2c without a bible revision |
| Acceleration | ~0.001 g bang-coast-bang | 1 g for years; continuous 0.2c burn |
| Transit time | ~5000–5100 yr | 982 yr (light-travel); "a few centuries" |
| Star mass / luminosity | 0.76 M☉ / 0.26 L☉ work figures | Sol twins; catalog 0.69 M☉ / ~0.21 L☉ used as if they replace the work figures |
| Swarm outer radius | 3.6 AU | 1 AU "Earth analog"; Dyson shell at the HZ |
| Flux at 3.6 AU | ≈ 0.020 S☉ | 1 S☉ panels; blue-white key |
| Teq work figure | ~120 K | shirtsleeve exterior; Earth-daylight grade |
| Scale | Unit-canon only | magic lengths in graphs |

## Transit arithmetic (INFERENCE from the binding row)

```
v_peak     = 0.2 c
a          ≈ 0.001 g ≈ 0.00981 m s⁻²
t_burn     = v / a ≈ 194 yr each (boost, then brake)
s_burn     ≈ 19.4 ly each
s_coast    ≈ 982 − 2 × 19.4 ≈ 943 ly
t_coast    ≈ 943 / 0.2 ≈ 4716 yr
t_total    ≈ 194 + 4716 + 194 ≈ 5100 yr
```

γ(0.2c) ≈ 1.021. Time-dilation on the coast is a few percent. Leave it off stills. Ship-frame vs barycentric split is OPEN.

Light-travel Sol → Kepler-62 is 982 yr. Radio reply ~1964 yr. No live talk.

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

## Payload class

| Allowed on the 0.2c hop | Rejected |
| --- | --- |
| Gram-probes | Living crew as the hop design |
| Dormant whole-brain emulations | Generation ship |
| Digital archives | Named passengers, factions, chapels |

WBE that wake into meat at destination is OPEN. Do not draw a nursery to close it.

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

## Scale

Do not copy these into node trees. Read [Unit-canon](https://github.com/Plygonality/Unit-canon):

| Measure | Work value | Owner |
| --- | --- | --- |
| Grid | 1.0 m | Unit-canon |
| Deck | 3.0 m | Unit-canon |
| Airlock | 1.0 m | Unit-canon |
| Human figure | 1.80 m | Unit-canon |
