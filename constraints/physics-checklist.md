# Physics checklist

Reject a still, graph, or brief that fails a row. Work figures are CANON for this bible. Catalog values that differ are noted, not used.

## Binding work figures

| Check | Pass | Fail |
| --- | --- | --- |
| Distance Sol → Kepler-62 | 982 ly | “nearby,” 1200 ly NASA press figure used as the work distance |
| Peak speed | 0.2c, labeled peak | 0.2c as cruise; >0.2c without a bible revision |
| Acceleration | ~0.001 g bang-coast-bang | 1 g for years; continuous 0.2c burn |
| Transit time | ~5000–5100 yr | 982 yr (light-travel); “a few centuries” |
| Star mass / luminosity | 0.76 M☉ / 0.26 L☉ work figures | Sol twins; catalog 0.69 M☉ / ~0.21 L☉ used as if they replace the work figures |
| Swarm outer radius | 3.6 AU | 1 AU “Earth analog”; Dyson shell at the HZ |
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

γ(0.2c) ≈ 1.021. Time-dilation on the coast is a few percent. Do not turn that into a plot. Ship-frame vs barycentric split is OPEN if anyone needs it for a clock prop.

Light-travel Sol → Kepler-62 is 982 yr. A radio reply is ~1964 yr. Do not stage a conversation.

## Flux and temperature

```
F / F_earth ≈ L / r² = 0.26 / 3.6² ≈ 0.020 S☉
```

~120 K is the **work figure** for look-dev, not a derived blackbody you must re-fit every pass. A bare 4π absorber at 0.020 S☉ sits colder (~105 K at A = 0). A sun-facing plate sits warmer. Waste heat, view factor, and coating are OPEN. Do not “correct” 120 K in a still brief.

Exterior is IR-dark. Visible key is work lights, not the star. The star is a K2 disk, not Sol.

## Mass table (correction)

Sphere area at R = 3.6 AU:

```
4πR² ≈ 3.64 × 10²⁴ m²
```

| Thickness | Fill | Mass order | Status |
| --- | --- | --- | --- |
| 1 mm | 1% of sphere | ≈ 0.012 M⊕ | CANON correction. Use this. |
| 1 m | 1% of sphere | ≈ 12 M⊕ | CANON. This is what 12 M⊕ actually bought. |

The old 12 M⊕ @ 1 mm figure is a millimeter/meter slip. Delete it wherever it reappears.

Implied mean density for 0.012 M⊕ @ 1 mm @ 1% is ~2 g cm⁻³. That is INFERENCE, not a material spec. Alloy / ice / slag mix is OPEN.

A 1 mm 1% swarm is cheap in planetary mass. A 1 m 1% swarm is a small planet, disassembled. Do not draw both and call them the same budget.

## Geometry

- Independently orbiting cells. Not a rigid shell. Not a single ringworld.
- Outer radius 3.6 AU. Interior of that sphere may be occupied; the bound is the outer edge.
- Kepler-62b–f orbit well inside 3.6 AU (published a ≤ 0.72 AU). They are not the swarm and not the large key-art body.
- One Habitat-kit build is **one cell**, not the swarm.

## Payload class

| Allowed on the 0.2c hop | Not allowed |
| --- | --- |
| Gram-probes | Living crew as the transit design |
| Dormant whole-brain emulations | Generation ship |
| Digital archives | Named passengers, factions, chapels |

WBE that wake into meat at destination is OPEN and stays unset. Do not draw a nursery to close it.

## Lighting and thermal failure modes

| Symptom | Likely fault |
| --- | --- |
| Exterior reads as Earth noon | Flux ignored; Sol lighting on a Kepler cell |
| Gold foil + deep blue shadows as default “space” | Palette substituting for 0.020 S☉ |
| Breathable balcony, no visor, no heat | 120 K ignored |
| Star is white and small like Sol | K2 / 0.26 L☉ ignored |
| Cell spans kilometers with no joints | Unit-canon / one-cell rule ignored |
| Large planet-shaped body labeled 62e or 62f | Key-art retcon |

## Scale (pointer only)

Do not copy these into node trees. Read them from [Unit-canon](https://github.com/Plygonality/Unit-canon):

| Measure | Work value | Owner |
| --- | --- | --- |
| Grid | 1.0 m | Unit-canon |
| Deck | 3.0 m | Unit-canon |
| Airlock | 1.0 m | Unit-canon |
| Human figure | 1.80 m | Unit-canon |
