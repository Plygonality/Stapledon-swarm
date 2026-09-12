# Physics checklist

Reject a still, graph, or brief that fails a row. Work figures are CANON. Catalog values that differ get a note. They do not get used.

## Binding work figures

| Check | Pass | Fail |
| --- | --- | --- |
| Distance Sol → Kepler-62 | 982 ly | "nearby"; 1200 ly NASA press figure used as the work distance |
| Peak and coast speed | 0.2c after laser boost, labeled as peak and as coast | 0.2c as trip-average; 982 yr at 0.2c |
| Launch architecture | Laser-driven lightsail; solar-powered laser plant allowed | Solar-wind sail; sunlight alone to 0.2c; 0.001 g default burns |
| Boost (reference family) | ~226 s, ~0.049 AU, ~34 000 g | Two-century burns; 5 106 yr as default transit |
| Unbraked coast | ~4 910 yr external / ~4 811 yr proper | 7191–7201 A.D. as current arrival; 982 yr ship time |
| Launch window | 2085–2095 A.D. founding dispatch | 3000 A.D. as the founding launch |
| Capture | Settlement occurs; mechanism OPEN | Silent Kepler brake laser; Kepler sunlight captures 0.2c |
| Probe body | 1–10 g; sail extra | Body mass includes the sail without saying so |
| Star mass / luminosity | 0.76 M☉ / 0.26 L☉ work figures | Sol twins; catalog 0.69 M☉ / ~0.21 L☉ used as if they replace the work figures |
| Swarm outer radius | 3.6 AU, independent orbits | 1 AU "Earth analog"; Dyson shell at the HZ; rigid lattice |
| Flux at 3.6 AU | ≈ 0.020 S☉ ≈ 27.3 W/m² | 1 S☉ panels; "virtually invisible" exteriors; blue-white key |
| Teq work figure | ~120 K for passive exterior under stated assumptions | Every machine at 120 K; shirtsleeve exterior; Earth-daylight grade |
| Scale | Unit-canon only | magic lengths in graphs |

## Launch arithmetic (INFERENCE from the adopted family)

Ideal receding reflector, constant nominal \(P\), sail-system mass = body mass, \(\sigma = 0.1\) g/m², \(I_0 = 10\) GW/m². Script: [`../calc/lightsail.py`](../calc/lightsail.py).

```
F(β) = (2P/c) · (1-β)/(1+β)
d(γ m v)/dt = F(β)
dx/dt = v

1 g body + 1 g sail, P = 100 GW:
  t_launch ≈ 226 s
  τ        ≈ 225 s
  t_emit   ≈ 202 s
  x        ≈ 7.31e9 m ≈ 0.049 AU
  a(0)     ≈ 3.4e4 g0
```

Do not swap those times with kinetic energy or with \(P t\).

Obsolete: constant 0.001 g, ~198 yr burns, ~5 106 yr total, 7191–7201 A.D. arrival. Historical note only.

```
982 ly / 0.2c = 4910 yr external
τ_coast ≈ 4910 / 1.02062 ≈ 4811 yr
2085–2095 + 4910 → unbraked passage 6995–7005 A.D.
```

Passage is not capture.

Light-travel Sol → Kepler-62 is 982 yr. Radio reply ~1964 yr for stationary endpoints. No live talk.

## Flux and temperature

```
F / F_earth ≈ L / r² = 0.26 / 3.6² ≈ 0.020 S☉
F ≈ 0.26 × 1361 W m⁻² / 3.6² ≈ 27.3 W m⁻²
```

~120 K is the look-dev work figure for a passive exterior under stated assumptions. You do not re-fit a blackbody every pass. Bare 4π absorber at 0.020 S☉ sits colder (~105 K at A = 0). Sun-facing plate sits warmer. Waste heat, view factor, coating: OPEN. Do not "correct" 120 K in a brief. Do not put every computer at 120 K.

27.3 W/m² is dim. It is not a black void. Exterior still takes starlight. Work lights carry the close-up visible key. Star is a K2 disk.

## Mass table (correction)

Sphere area at R = 3.6 AU:

```
4πR² ≈ 3.64 × 10²⁴ m²
```

| Thickness | Fill | Mass order | Status |
| --- | --- | --- | --- |
| 1 mm | 1% of sphere | ≈ 0.012 M⊕ | CANON plate-only example. Use this. |
| 1 m | 1% of sphere | ≈ 12 M⊕ | CANON plate-only example. This is what 12 M⊕ bought. |

The old 12 M⊕ @ 1 mm figure swapped millimeters and meters. Delete it if it comes back. Neither row is the total built swarm mass.

Implied mean density for 0.012 M⊕ @ 1 mm @ 1% is ~2 g cm⁻³. INFERENCE. Not a material spec. Alloy / ice / slag mix is OPEN.

## Geometry

- Independently orbiting cells. No rigid shell. No ringworld. No arbitrary rigid lattice.
- Outer radius 3.6 AU. Interior of that sphere may be occupied. The bound is the outer edge.
- Kepler-62b–f orbit well inside 3.6 AU (published a ≤ 0.72 AU). They are not the swarm. They are not the large key-art body. No detected-life implication.
- One Habitat-kit build is **one cell**.
- Cells specialise. The featured relic cell is one archive / computing habitat.

## Payload class

| Allowed on the 0.2c hop | Rejected |
| --- | --- |
| 1–10 g probe body; sail extra | Living crew as the hop design |
| Dormant WBE and ASI states | Generation ship |
| Picobot seeds; digital archives | Named passengers, factions, chapels on the hull |
| Selective authorised activation | A civilisation running on one gram-class probe |

WBE that wake into meat at destination is OPEN. Do not draw a nursery to close it.

Picotechnology: picometre precision, atomic and molecular working machines. A few-picometre complete robot fails.

Interstellar gas and dust at 0.2c are a damage term. Ignore-erosion briefs fail. Survival design stays OPEN.

## Lighting and thermal failures

| Symptom | Likely fault |
| --- | --- |
| Exterior reads as Earth noon | Flux ignored; Sol lighting on a Kepler cell |
| Gold foil + deep blue shadows as default "space" | Palette standing in for 27.3 W/m² |
| Exterior captioned as virtually invisible | 2% of S☉ treated as zero |
| Breathable balcony, no visor, no heat | 120 K ignored |
| Every rack labelled 120 K | Active plant confused with passive Teq |
| Star is white and small like Sol | K2 / 0.26 L☉ ignored |
| Cell spans kilometers with no joints | Unit-canon / one-cell rule ignored |
| Large planet-shaped body labeled 62e or 62f | Key-art retcon |
| Large irregular silhouette captioned as a planet | Fights `stills/01-eclipse.jpg` / `03-inward.jpg` |
| Distant diamond marks treated as the Habitat-kit mesh | Scale / one-cell rule ignored |
| Relic cell captioned as the dead swarm | Featured-cell rule ignored |
| Vacuum hull "oxidised" with no environment | Oxidation used as default weathering |
| Cells welded into a rigid lattice | Independent-orbit rule ignored |

## Scale

Do not copy these into node trees. Read [Unit-canon](https://github.com/Plygonality/Unit-canon):

| Measure | Work value | Owner |
| --- | --- | --- |
| Grid | 1.0 m | Unit-canon |
| Deck | 3.0 m | Unit-canon |
| Airlock | 1.0 m | Unit-canon |
| Human figure | 1.80 m | Unit-canon |
