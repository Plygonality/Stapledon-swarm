# Layer C. Production map

No new world facts. Maps Layer B onto Habitat-kit, Time-slice, Probe-kit, Unit-canon, Collection-linter, and Blend-ci. If a sentence is not a mapping, delete it.

## 1. Who builds what

| Repo | May instance | May not |
| --- | --- | --- |
| **This bible** | Tagged facts, OPEN list, operator key-art in `stills/` | Graphs, cooks, Python packages, Habitat Cuts |
| **[Habitat-kit](https://github.com/Plygonality/Habitat-kit)** | One cell. Actors: airlock, deck bay, truss, hatch. Three Habitat Cuts. | The swarm. The large key-art body. A second generator. |
| **[Time-slice](https://github.com/Plygonality/Time-slice)** | Epoch IDs `construction` / `operational` / `relic` on that cell. Decay-pass + signal-field. | A new identity per epoch. Extra epochs for plot. |
| **[Probe-kit](https://github.com/Plygonality/Probe-kit)** | Crawler, drone, debris as instances on the cell. | A second habitat generator. Named operators. |
| **[Unit-canon](https://github.com/Plygonality/Unit-canon)** | Grid 1.0 m, deck 3.0 m, airlock 1.0 m, figure 1.80 m. | Numbers copied into graphs in this repo. |
| **[Collection-linter](https://github.com/Plygonality/Collection-linter)** | Roles `human_figure`, `airlock`, `deck`, `grid` against Unit-canon. | World-fact checks. Linter does not know Kepler-62. |
| **[Blend-ci](https://github.com/Plygonality/Blend-ci)** | Headless cook of a Habitat-kit / gn-as-code dump. Viewport or workbench PNG. Hash / lint drift. | Writing the bible. Building the cell. |

## 2. Habitat Cuts → Time-slice

Same hull. Epoch is a socket pack. Habitat-kit does not fork Time-slice.

| Habitat Cut | Time-slice `epoch` | Decay-pass | Signal-field |
| --- | --- | --- | --- |
| construction | `construction` | High scaffold, high incomplete, near-zero oxidation | Work lights, arcs, messy |
| operational | `operational` | Wear, hull closed, no scaffold | Lanes, running lights |
| relic | `relic` | Oxidation, breach, debris; scaffold gone | Sparse leftovers |

Emitter sites stay seed-locked. Epoch only weights which sites are live.

Do not add a fourth cut. Arrival, founding, and war are plot. They are not epochs.

## 3. What a cell graph is allowed to show

Allowed:

- One hard-surface cell. Industrial / brutalist.
- Unit-canon sockets for every length.
- Habitat-kit actors already in that kit: airlock, deck bay, truss, hatch.
- Probe-kit instances: crawler, drone, debris.
- Work lights that beat 0.020 S☉ starlight.
- The three states in the table above.

Rejected:

- The full 3.6 AU swarm as a Habitat-kit object.
- A planet-scale body labeled Kepler-62b–f.
- Sol-white key on a Kepler cell.
- Named signage, chapels, flags, crew.
- Magic lengths.
- A generation-ship interior.

## 4. Still mapping

| Still | File | Owner | Camera |
| --- | --- | --- | --- |
| Eclipse | [`stills/01-eclipse.jpg`](../stills/01-eclipse.jpg) | Operator. This repo. | System. Large irregular body ≠ b–f. |
| Lattice | [`stills/02-lattice.jpg`](../stills/02-lattice.jpg) | Operator. This repo. | System. Receding geometric cells. |
| Inward | [`stills/03-inward.jpg`](../stills/03-inward.jpg) | Operator. This repo. | System. Lattice on the disk. Small circular transit is a different object. |
| Construction cell | Habitat-kit `screenshots/construction/` | Habitat-kit + Time-slice + Blend-ci | Cell. Same rig as the other two cuts. Unshot here. |
| Operational cell | Habitat-kit `screenshots/operational/` | Habitat-kit + Time-slice + Blend-ci | Cell. Unshot here. |
| Relic cell | Habitat-kit `screenshots/relic/` | Habitat-kit + Time-slice + Blend-ci | Cell. Unshot here. |

`stills/` is operator key-art. Blend-ci does not cook those three. Habitat-kit does not rebuild them. Captions: [`layer-b-wiki.md`](layer-b-wiki.md) §13.

Distant cells in the key-art read as sharp dark polygons. System-scale silhouette. Habitat-kit instances one airlock / deck-bay / truss / hatch cell.

If look-dev is chasing these frames:

| Cue | Keep | Drop |
| --- | --- | --- |
| Star | Orange-yellow K disk, prominences fine | Sol-white, tiny G2 |
| Swarm | Many independent dark cells; veil / lattice | Solid shell, single ringworld |
| Large body | Irregular, blocky, unlabeled | Caption 62b–f |
| Small circular disk | Optional transit; unnamed | Call it the large body |
| Haze / traces | Faint red orbital traces | Default Earth-blue space |

## 5. Lighting map

| Quantity | Work figure | Where it lands |
| --- | --- | --- |
| Star | K2, 0.26 L☉ | HDRI / sun lamp color. |
| Flux at cell | ≈ 0.020 S☉ | Exterior fill. Almost nothing in the visible. |
| Teq | ~120 K work figure | No shirtsleeve exteriors. IR-dark hull. |
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

Collection-linter reports length faults. This bible does not.

## 7. Sol hardware vs Kepler hardware

Sol-built prop (gram-probe, archive canister, sail remnant): tag `origin=sol` on the object or the brief. Assembled at Kepler-62: `origin=kepler`. Unlabeled mix fails.

Habitat-kit v1 can skip Sol props. It still cannot light the cell as Sol.

## 8. Asset-generation checklist

Run this before a Habitat-kit dump, a Time-slice playbook, or a Blend-ci cook. Fail on a row = stop.

1. **One cell.** Independently orbiting cell. Not the swarm. Not a planet.
2. **Unit-canon only.** Lengths from Unit-canon. No magic numbers in graphs.
3. **Three cuts, same hull.** `construction` / `operational` / `relic`. Epoch is a parameter. Relic is not a redesign.
4. **Actors.** Habitat-kit: airlock, deck bay, truss, hatch. Probe-kit instances: crawler, drone, debris.
5. **Flux.** Exterior fill ≈ 0.020 S☉. Work lights carry the visible key. Star is K2.
6. **Temperature.** Teq work figure ~120 K. No shirtsleeve balcony. No Earth-noon grade.
7. **Payload class.** No living crew as the design. Gram-probe / dormant WBE / archive as hardware only.
8. **Sol / Kepler.** Unlabeled Sol lighting or Sol hardware on a Kepler cell fails.
9. **Key-art body.** System still: large body is irregular and not Kepler-62b–f. Match `stills/01-eclipse.jpg` / `stills/03-inward.jpg`. No label.
10. **Mass.** Do not caption a foil swarm as 12 M⊕. 1 mm @ 1% ≈ 0.012 M⊕. 12 M⊕ is 1 m @ 1%.
11. **0.2c is peak.** No caption that the cell cruised at 0.2c for 982 yr.
12. **OPEN.** No new names, factions, religions, or an identity for the large body.
13. **Relic.** Time-slice epoch. Not a sermon.
14. **Cooks live elsewhere.** Graphs: Habitat-kit. Cooks: Blend-ci. Screenshots prove those repos.
15. **Linter.** Collection-linter roles pass against Unit-canon before a PNG counts as a Habitat Cut.
