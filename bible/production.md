# Production map

No new world facts. Maps the wiki and detail files onto Habitat-kit, Time-slice, Probe-kit, Unit-canon, Collection-linter, and Blend-ci. If a sentence is not a mapping, delete it.

## 1. Who builds what

| Repo | May instance | May not |
| --- | --- | --- |
| **This bible** | Tagged facts, OPEN list, key-art in `stills/`, calculation appendix | Graphs, cooks, Python packages, Habitat Cuts, a simulator |
| **[Habitat-kit](https://github.com/Plygonality/Habitat-kit)** | One cell. Actors: airlock, deck bay, truss, hatch. Three Habitat Cuts. Lineage joints / hatches / service modules as mesh vocabulary. | The swarm. The large key-art body. A second generator. Extra epoch IDs. |
| **[Time-slice](https://github.com/Plygonality/Time-slice)** | Epoch IDs `construction` / `operational` / `relic` on that cell. Decay-pass + signal-field. | A new identity per epoch. Extra epochs for plot. |
| **[Probe-kit](https://github.com/Plygonality/Probe-kit)** | Crawler, drone, debris as instances on the cell. Gram-class probe body and sail remnant as props. | A second habitat generator. Named crew. |
| **[Unit-canon](https://github.com/Plygonality/Unit-canon)** | Grid 1.0 m, deck 3.0 m, airlock 1.0 m, figure 1.80 m. | Numbers copied into graphs in this repo. Lineage does not fork units. |
| **[Collection-linter](https://github.com/Plygonality/Collection-linter)** | Roles `human_figure`, `airlock`, `deck`, `grid` against Unit-canon. | World-fact checks. Linter does not know Kepler-62. |
| **[Blend-ci](https://github.com/Plygonality/Blend-ci)** | Headless cook of a Habitat-kit / gn-as-code dump. Viewport or workbench PNG. Hash / lint drift. | Writing the bible. Building the cell. |

## 2. Habitat Cuts → Time-slice

Same hull. Epoch is a socket pack. Habitat-kit does not fork Time-slice. System history does not add IDs.

| Habitat Cut | Time-slice `epoch` | Decay-pass | Signal-field |
| --- | --- | --- | --- |
| construction | `construction` | High scaffold, high incomplete, near-zero oxidation | Work lights, arcs, messy |
| operational | `operational` | Wear, hull closed, no scaffold | Lanes, running lights |
| relic | `relic` | Empty former habitation; protected archive plant; mixed-period repairs; scaffold gone | Sparse leftovers. Request for restoration or continued preservation. |

Emitter sites stay seed-locked. Epoch only weights which sites are live.

Do not add a fourth cut. Arrival, founding, and war are plot. They are not epochs.

Relic maps [`featured-cell.md`](featured-cell.md). Do not stamp names. Do not caption the swarm as dead. Do not default to evil AI, universal war, or magic.

Oxidation in the decay-pass needs a brief that supplies a credible environment or exposure history. Otherwise use impact, radiation, thermal fatigue, joint failure, or deposits.

## 3. What a cell graph is allowed to show

Allowed:

- One hard-surface cell. Industrial / brutalist.
- Unit-canon sockets for every length.
- Habitat-kit actors already in that kit: airlock, deck bay, truss, hatch.
- Lineage expressed as recurring joints, hatch designs, service modules, and repair traces.
- Related shells with different quarantine / soil / environmental kit when mapping [`preservation.md`](preservation.md).
- Probe-kit instances: crawler, drone, debris. Optional `origin=sol` gram-class body or sail remnant.
- Work lights that read against 27.3 W/m² starlight.
- The three states in the table above.

Rejected:

- The full 3.6 AU swarm as a Habitat-kit object.
- A rigid lattice of cells.
- A planet-scale body labeled Kepler-62b–f.
- Sol-white key on a Kepler cell.
- Named signage, chapels, flags, crew, invented protagonists.
- Magic lengths or a second unit system for a lineage.
- A generation-ship interior.
- A civilisation running inside a gram-probe prop.
- A destination braking laser implied in the background.
- Detected-life captions on e / f.

## 4. Still mapping

| Still | File | Owner | Camera |
| --- | --- | --- | --- |
| Eclipse | [`stills/01-eclipse.jpg`](../stills/01-eclipse.jpg) | This repo | System. Large irregular body ≠ b–f. Independent cells, not a rigid lattice. |
| Lattice | [`stills/02-lattice.jpg`](../stills/02-lattice.jpg) | This repo | System. Receding geometric cells. Filename does not lock a grid. |
| Inward | [`stills/03-inward.jpg`](../stills/03-inward.jpg) | This repo | System. Independent cells on the disk. Small circular transit is a different object. |
| Construction cell | Habitat-kit `screenshots/construction/` | Habitat-kit + Time-slice + Blend-ci | Cell. Same rig as the other two cuts. Unshot here. |
| Operational cell | Habitat-kit `screenshots/operational/` | Habitat-kit + Time-slice + Blend-ci | Cell. Unshot here. |
| Relic cell | Habitat-kit `screenshots/relic/` | Habitat-kit + Time-slice + Blend-ci | Cell. Empty habitation + protected archive plant. Unshot here. |

`stills/` is key-art. Blend-ci does not cook those three. Habitat-kit does not rebuild them. Captions: [`wiki.md`](wiki.md) §13.

Distant cells in the key-art read as sharp dark polygons. System-scale silhouette. Habitat-kit instances one airlock / deck-bay / truss / hatch cell.

If look-dev is chasing these frames:

| Cue | Keep | Drop |
| --- | --- | --- |
| Star | Orange-yellow K disk, prominences fine | Sol-white, tiny G2 |
| Swarm | Many independent dark cells; veil / field | Solid shell, single ringworld, rigid lattice |
| Large body | Irregular, blocky, unlabeled | Caption 62b–f |
| Small circular disk | Optional transit; unnamed | Call it the large body |
| Haze / traces | Faint red orbital traces | Default Earth-blue space; welded grid |
| Exterior light | 27.3 W/m² is dim, not a black void | "Virtually invisible" exteriors |

## 5. Lighting map

| Quantity | Work figure | Where it lands |
| --- | --- | --- |
| Star | K2, 0.26 L☉ | HDRI / sun lamp color. |
| Flux at cell | ≈ 0.020 S☉ ≈ 27.3 W/m² | Exterior fill. Dim. Visible. |
| Teq | ~120 K work figure for passive exterior under stated assumptions | Not shirtsleeve exteriors. Not every interior rack. |
| Active plant | Separate from Teq | Computers and radiators have their own temperatures. |
| Key | Work lights | Construction: arcs, temporary. Operational: structured. Relic: sparse leftovers. |

Earth-noon viewport means the cook is wrong. Mesh can still be right.

## 6. Scale map

Read from Unit-canon. Do not copy the JSON into this repo.

| Socket / role | Unit-canon key | Habitat-kit use |
| --- | --- | --- |
| Grid | `meters_per_grid` | Snap, array pitch |
| Deck | `deck_height` | Deck bay span |
| Airlock | `airlock_diameter` | Tube, hatch clear |
| Figure | `human_figure.standing_height` | Scale mannequin |

Collection-linter reports length faults. This bible does not. Lineage changes joints, not metres.

## 7. Sol hardware vs Kepler hardware

Sol-built prop (gram-class probe body, archive canister, sail remnant): tag `origin=sol` on the object or the brief. Assembled at Kepler-62: `origin=kepler`. Unlabeled mix fails.

Sail remnant mass is extra to the 1–10 g body. Do not caption a 2 g stack as "1 g including sail."

Habitat-kit v1 can skip Sol props. It still cannot light the cell as Sol.

## 8. Asset-generation checklist

Run this before a Habitat-kit dump, a Time-slice playbook, or a Blend-ci cook. Fail on a row = stop.

1. **One cell.** Independently orbiting cell. Not the swarm. Not a planet. Not a rigid lattice.
2. **Unit-canon only.** Lengths from Unit-canon. No magic numbers in graphs. Lineage does not fork units.
3. **Three cuts, same hull.** `construction` / `operational` / `relic`. Epoch is a parameter. Relic is not a redesign. No fourth epoch.
4. **Actors.** Habitat-kit: airlock, deck bay, truss, hatch. Probe-kit instances: crawler, drone, debris. Lineage: joints, hatches, service modules, repair traces.
5. **Flux.** Exterior fill ≈ 27.3 W/m² (0.020 S☉). Dim, not a void. Work lights carry the close-up key. Star is K2.
6. **Temperature.** Teq work figure ~120 K for passive exterior under stated assumptions. Active plant is separate. No shirtsleeve balcony. No Earth-noon grade.
7. **Payload class.** No living crew as the design. 1–10 g body, sail extra, dormant WBE / ASI / archive as hardware only. No civilisation-on-a-probe caption.
8. **Sol / Kepler.** Unlabeled Sol lighting or Sol hardware on a Kepler cell fails.
9. **Key-art body.** System still: large body is irregular and not Kepler-62b–f. Match `stills/01-eclipse.jpg` / `stills/03-inward.jpg`. No label. No detected-life caption on e / f.
10. **Mass.** Do not caption a foil swarm as 12 M⊕. 1 mm @ 1% ≈ 0.012 M⊕. 12 M⊕ is 1 m @ 1%. Plate examples are not total swarm mass.
11. **0.2c is peak and coast.** No caption that the hop averaged 0.2c, or ran 982 yr at 0.2c. No 0.001 g two-century burn. No 7191–7201 default arrival. No silent Kepler brake laser.
12. **OPEN.** No new factions, religions, invented protagonists, or an identity for the large body.
13. **Relic.** Time-slice epoch. Empty habitation, protected unawakened archives, mixed repairs, restoration / preservation request. Not a dead swarm. Not a sermon. Oxidation needs an environment.
14. **Cooks live elsewhere.** Graphs: Habitat-kit. Cooks: Blend-ci. Screenshots prove those repos. `calc/lightsail.py` reprints launch numbers. It is not a simulator.
15. **Linter.** Collection-linter roles pass against Unit-canon before a PNG counts as a Habitat Cut.
