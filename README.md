# Stapledon-swarm

Hard-SF world bible for Habitat-kit. One independently orbiting cell in the Kepler-62 Stapledon swarm. Not a novel. Not the generator.

Key-art, system scale. These are not Habitat Cuts. The large irregular body is not Kepler-62b–f. Notes in [`bible/wiki.md`](bible/wiki.md) §12–13.

![Kepler-62 with an irregular silhouette on the disk and a cell veil](stills/01-eclipse.jpg)

*`01-eclipse`. Wide. Star in the middle. Kepler-62 as a K disk, prominences visible. Large irregular body in silhouette (planets b–f are out). Swarm sits as stacked cell veils.*

![Rows of dark geometric cells receding, K-disk in the upper right](stills/02-lattice.jpg)

*`02-lattice`. Star shoved into a corner. Distant cells as repeated sharp silhouettes. Faint red traces, some haze. Small circular disk on the limb, if you see one, is not the large body.*

![Looking inward: lattice on the disk, small circular transit, irregular body in the foreground](stills/03-inward.jpg)

*`03-inward`. Camera already inside the swarm. Fine lattice across the disk. Same irregular foreground body. Small circular transit is a different object. Habitat Cuts are not this shot.*

Index: [`stills/README.md`](stills/README.md).

## 1. What this repo is

A world bible. Habitat-kit and the rest of the Plygonality stack read it.

| File | Job |
| --- | --- |
| [`bible/wiki.md`](bible/wiki.md) | Numbered wiki. Claims tagged. |
| [`bible/production.md`](bible/production.md) | What Habitat-kit, Time-slice, and Blend-ci may instance. Checklist at the end. |
| [`bible/open-questions.md`](bible/open-questions.md) | OPEN list. Leave it. |

Tags: [`schema/status-tags.md`](schema/status-tags.md). Project rules: [`constraints/project-rules.md`](constraints/project-rules.md). Physics rejects: [`constraints/physics-checklist.md`](constraints/physics-checklist.md). Stills: [`stills/`](stills/).

## 2. What this is not

Habitat-kit lives in its own repo. No generator, no graphs, no apply scripts here.

Blend-ci cooks dumps. This repo does not run Blender or hash a PNG.

No swarm integrator. No N-body. No cell-count engine.

Do not paste this into [Hard-SciFi-idea-generator](https://github.com/Plygonality/Hard-SciFi-idea-generator).

Scale is [Unit-canon](https://github.com/Plygonality/Unit-canon). We list the numbers once so you can read the table. We do not own them.

No named people, factions, religions, or generation-ship endings on a still or Habitat Cut. Programme-history names live in the wiki.

## 3. How to read the wiki

Start at [`bible/wiki.md`](bible/wiki.md). That file is the source. If a still or a kit dump fights it, the wiki wins. Programme history is wiki §16–24. Reader-facing dates are Gregorian A.D.

[`bible/production.md`](bible/production.md) is only the map onto Habitat-kit / Time-slice / Blend-ci. It does not add world facts.

OPEN means unset. Do not invent the missing piece. Habitat-kit may do one cell, three Habitat Cuts, Unit-canon sockets. That is the scope.

## 4. How Habitat Cuts map

One cell. One hull. Epoch is a socket. IDs come from Time-slice. Habitat-kit does not fork that repo.

| Habitat Cut | Time-slice id | Reads as |
| --- | --- | --- |
| construction | `construction` | Scaffold, incomplete, work lights, arcs |
| operational | `operational` | Closed hull, structured lights, wear |
| relic | `relic` | Oxidation, breach, debris, leftover 2085 request |

Decay-pass and signal-field stay in Time-slice / Habitat-kit. We only say what the three states mean.

## 5. Binding numbers

Lengths below are for reading. Source file is Unit-canon. Edit there: https://github.com/Plygonality/Unit-canon

| Quantity | Work figure | Owner / note |
| --- | --- | --- |
| Distance Sol → Kepler-62 | 982 ly | This bible (CANON) |
| Peak and coast speed | 0.2c | Peak and coast. Not trip-average. 982 yr is light-travel (CANON) |
| Transit | ~5,106 yr external / ~5,008 yr proper | Bang-coast-bang at ~0.001 g (INFERENCE from the two rows above) |
| Founding launch | 2085–2095 A.D. | Original probes. ~1 billion (CANON) |
| Original Kepler arrival | 7191–7201 A.D. | 2090 → ~7196 (INFERENCE) |
| Kepler-62 mass / luminosity | 0.76 M☉ / 0.26 L☉ | Work figures (CANON). Catalog scatter is OPEN. |
| Swarm outer radius | 3.6 AU | This bible (CANON) |
| Flux at 3.6 AU | ≈ 0.020 S☉ | 0.26 / 3.6² (INFERENCE) |
| Teq | ~120 K | Work figure (CANON) |
| Grid | 1.0 m | [Unit-canon](https://github.com/Plygonality/Unit-canon) |
| Deck | 3.0 m | [Unit-canon](https://github.com/Plygonality/Unit-canon) |
| Airlock | 1.0 m | [Unit-canon](https://github.com/Plygonality/Unit-canon) |
| Human figure | 1.80 m | [Unit-canon](https://github.com/Plygonality/Unit-canon) |

Mass-table correction (CANON): **1 mm @ 1% of a 3.6 AU sphere ≈ 0.012 M⊕**. **12 M⊕ is a 1 m plate @ 1%.** Someone swapped millimeters and meters. Drop the old 12 M⊕ @ 1 mm number.

## 6. Toolchain

| Repo | Role relative to this bible |
| --- | --- |
| [Habitat-kit](https://github.com/Plygonality/Habitat-kit) | Builds the cell. Reads this frame. Code is over there. |
| [Time-slice](https://github.com/Plygonality/Time-slice) | Same seed, three epochs. Habitat Cuts use those IDs. |
| [Probe-kit](https://github.com/Plygonality/Probe-kit) | Crawler, drone, debris as instances. |
| [Unit-canon](https://github.com/Plygonality/Unit-canon) | Grid, deck, airlock, figure. |
| [Collection-linter](https://github.com/Plygonality/Collection-linter) | Role checks against Unit-canon. Does not know Kepler-62. |
| [Blend-ci](https://github.com/Plygonality/Blend-ci) | Headless cook. Hash and lint. |

## 7. Non-goals and OPEN items

Out of scope: Habitat-kit or Blend-ci code here; Python packages; CI; a web UI; filling OPEN items; labeling the key-art body as planets b–f; copying Unit-canon into this repo as if we own it; extra image binaries outside [`stills/`](stills/).

OPEN list is only [`bible/open-questions.md`](bible/open-questions.md). Leave it. The stills do not name the large body.

Hop payload: gram-probes, dormant WBE and ASI states, digital archives. Living crew and generation ships are rejected, not left OPEN. A gram-probe does not run a civilisation.

MIT. [`LICENSE`](LICENSE).
