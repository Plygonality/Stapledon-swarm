# Layer C — production map

No new world facts. This file maps Layer B onto Habitat-kit, Time-slice, Probe-kit, Unit-canon, Collection-linter, and Blend-ci. If a sentence here is not a mapping, delete it.

## 1. Who builds what

| Repo | May instance | May not |
| --- | --- | --- |
| **This bible** | Tagged facts, OPEN list, operator key-art in `stills/` | Graphs, cooks, Python packages, Habitat Cuts |
| **[Habitat-kit](https://github.com/Plygonality/Habitat-kit)** | One cell. Actors: airlock, deck bay, truss, hatch. Three Habitat Cuts. | The swarm. The large key-art body. A second generator. |
| **[Time-slice](https://github.com/Plygonality/Time-slice)** | Epoch IDs `construction` / `operational` / `relic` on that cell. Decay-pass + signal-field. | A new identity per epoch. A fourth epoch named for story. |
| **[Probe-kit](https://github.com/Plygonality/Probe-kit)** | Crawler, drone, debris as instances on the cell. | A second habitat generator. Named operators. |
| **[Unit-canon](https://github.com/Plygonality/Unit-canon)** | Grid 1.0 m, deck 3.0 m, airlock 1.0 m, figure 1.80 m. | Nothing in this repo copies those numbers into graphs. |
| **[Collection-linter](https://github.com/Plygonality/Collection-linter)** | Roles `human_figure`, `airlock`, `deck`, `grid` against Unit-canon. | World-fact checks. Linter does not know Kepler-62. |
| **[Blend-ci](https://github.com/Plygonality/Blend-ci)** | Headless cook of a Habitat-kit / gn-as-code dump. Viewport or workbench PNG. Hash / lint drift. | Authoring the bible. Authoring the cell. |

## 2. Habitat Cuts → Time-slice

Same hull. Epoch is a socket pack. Habitat-kit does not fork Time-slice.

| Habitat Cut | Time-slice `epoch` | Decay-pass (read as) | Signal-field (read as) |
| --- | --- | --- | --- |
| construction | `construction` | High scaffold, high incomplete, near-zero oxidation | Chaotic, hot, work lights and arcs |
| operational | `operational` | Lived-in wear, hull complete, no scaffold | Structured lanes, running lights |
| relic | `relic` | Oxidation, breach, debris; scaffold gone | Sparse survivors, ghost traces |

Emitter sites stay seed-locked. Epoch only weights which sites are live.

Do not invent a fourth cut for “arrival,” “founding,” or “war.” Those are story. They are not epochs.

## 3. What a cell graph is allowed to show

Allowed:

- One hard-surface cell. Industrial / brutalist.
- Unit-canon sockets for every length.
- Habitat-kit actors already in that kit: airlock, deck bay, truss, hatch.
- Probe-kit actors as instances: crawler, drone, debris.
- Work lights that beat 0.020 S☉ starlight.
- Three states from the table above.

Not allowed:

- The full 3.6 AU swarm as a Habitat-kit object.
- A planet-scale body labeled Kepler-62b–f.
- Sol-white key on a Kepler cell.
- Named signage, chapels, flags, crew.
- Magic lengths.
- A generation-ship interior.

## 4. Still mapping

| Still | File | Owner | Camera |
| --- | --- | --- | --- |
| Eclipse | [`stills/01-eclipse.jpg`](../stills/01-eclipse.jpg) | Operator key-art. This repo. | System. Large irregular body ≠ b–f. |
| Lattice | [`stills/02-lattice.jpg`](../stills/02-lattice.jpg) | Operator key-art. This repo. | System. Receding geometric cells. |
| Inward | [`stills/03-inward.jpg`](../stills/03-inward.jpg) | Operator key-art. This repo. | System. Lattice over disk; small circular transit ≠ large body. |
| Construction cell | Habitat-kit `screenshots/construction/` | Habitat-kit + Time-slice + Blend-ci | Cell. Same rig as the other two cuts. Unshot here. |
| Operational cell | Habitat-kit `screenshots/operational/` | Habitat-kit + Time-slice + Blend-ci | Cell. Unshot here. |
| Relic cell | Habitat-kit `screenshots/relic/` | Habitat-kit + Time-slice + Blend-ci | Cell. Unshot here. |

The three `stills/` files are not Habitat-kit proofs. Blend-ci does not cook them. Habitat-kit does not recreate them. Captioned frames live in [`layer-b-wiki.md`](layer-b-wiki.md) §13.

Distant cells in the key-art read as sharp dark polygons. That is a silhouette at system scale. Do not build a diamond planet in Habitat-kit. The kit instances one airlock / deck-bay / truss / hatch cell.

If a look-dev pass matches these frames:

| Cue | Do | Do not |
| --- | --- | --- |
| Star | Orange-yellow K disk, prominences allowed | Sol-white, tiny G2 |
| Swarm | Many independent dark cells; veil / lattice | Solid shell, single ringworld |
| Large body | Irregular, blocky, unlabeled | Caption 62b–f |
| Small circular disk | Optional transit; unnamed | Call it the large body |
| Haze / traces | Faint red orbital traces allowed | Earth-blue space as default |

## 5. Lighting map (sockets, not story)

| Quantity | Work figure | Where it lands |
| --- | --- | --- |
| Star | K2, 0.26 L☉ | HDRI / sun lamp color. Not Sol. |
| Flux at cell | ≈ 0.020 S☉ | Exterior fill. Almost nothing in the visible. |
| Teq | ~120 K work figure | No shirtsleeve exteriors. IR-dark hull. |
| Key | Work lights | Construction: arcs, temporary. Operational: structured. Relic: sparse / ghost. |

If the viewport reads as Earth noon, the cook is wrong even if the mesh is right.

## 6. Scale map (pointer)

Read from Unit-canon. Do not duplicate the JSON here.

| Socket / role | Unit-canon key | Habitat-kit use |
| --- | --- | --- |
| Grid | `meters_per_grid` | Snap, array pitch |
| Deck | `deck_height` | Deck bay span |
| Airlock | `airlock_diameter` | Tube, hatch clear |
| Figure | `human_figure.standing_height` | Scale mannequin |

Collection-linter is the error surface. This bible is not.

## 7. Sol hardware vs Kepler hardware

If a prop is Sol-built (gram-probe, archive canister, sail remnant), tag the object or the brief `origin=sol`. If it is assembled at Kepler-62, tag `origin=kepler`. Unlabeled mix fails the still.

Habitat-kit v1 may ignore Sol props. It still may not light the cell as Sol.

## 8. Asset-generation checklist

Use this list before a Habitat-kit dump, a Time-slice playbook, or a Blend-ci cook. A fail on any row is a stop.

1. **One cell.** The object is one independently orbiting cell, not the swarm and not a planet.
2. **Unit-canon only.** Every length comes from Unit-canon. No magic numbers in graphs.
3. **Three cuts, same hull.** `construction` / `operational` / `relic`. Epoch is a parameter. No redesigned relic.
4. **Actors.** Habitat-kit: airlock, deck bay, truss, hatch. Probe-kit instances only as crawler / drone / debris.
5. **Flux.** Exterior fill ≈ 0.020 S☉. Work lights are the visible key. Star is K2, not Sol.
6. **Temperature.** Teq work figure ~120 K. No shirtsleeve balcony, no Earth-noon grade.
7. **Payload class.** No living crew as the design. Gram-probe / dormant WBE / archive only if they appear as hardware, not as named people.
8. **Sol / Kepler.** Unlabeled Sol lighting or Sol hardware on a Kepler cell is a fail.
9. **Key-art body.** If a system still is in the set, the large body is irregular and not Kepler-62b–f. Match `stills/01-eclipse.jpg` / `stills/03-inward.jpg`. Do not label it.
10. **Mass.** Do not caption a foil swarm as 12 M⊕. 1 mm @ 1% ≈ 0.012 M⊕. 12 M⊕ is 1 m @ 1%.
11. **0.2c is peak.** No caption that says the cell cruised at 0.2c for 982 yr.
12. **OPEN.** No new names, factions, religions, or “what the large body is.”
13. **No story ending.** Relic is a Time-slice epoch, not a morality play.
14. **This repo did not cook it.** Graphs live in Habitat-kit. Cooks live in Blend-ci. Screenshots are proof of those repos, not of this one.
15. **Linter.** Collection-linter roles pass against Unit-canon before the PNG is treated as a Habitat Cut.
