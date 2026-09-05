# Stapledon-swarm

Hard-SF world frame for Habitat-kit. Three-layer bible (AI context / human wiki / production map) for one independently orbiting cell in the Kepler-62 Stapledon swarm. Not a novel. Not the generator.

## 1. What this repo is

A versioned, loadable bible. Context for [Habitat-kit](https://github.com/Plygonality/Habitat-kit) and the rest of the Plygonality toolchain.

| Layer | File | Job |
| --- | --- | --- |
| A | [`bible/layer-a-ai.md`](bible/layer-a-ai.md) | ≤ ~800 words. Load into a model. |
| B | [`bible/layer-b-wiki.md`](bible/layer-b-wiki.md) | Numbered human wiki. Every major claim tagged. |
| C | [`bible/layer-c-production.md`](bible/layer-c-production.md) | Habitat-kit / Time-slice / Blend-ci map. Ends with the asset-generation checklist. |

OPEN items live in [`bible/open-questions.md`](bible/open-questions.md). Tags are defined in [`schema/status-tags.md`](schema/status-tags.md). How to revise: [`prompts/revise-bible.md`](prompts/revise-bible.md). Operator constraints: [`constraints/operator-rules.md`](constraints/operator-rules.md). Physics rejects: [`constraints/physics-checklist.md`](constraints/physics-checklist.md).

## 2. What this is not

- **Not Habitat-kit.** This repo does not ship a generator, graphs, or apply scripts.
- **Not Blend-ci.** This repo does not cook a `.blend` or hash a PNG.
- **Not a swarm sim.** No N-body, no cell-count engine.
- **Not a story file** to drop into [Hard-SciFi-idea-generator](https://github.com/Plygonality/Hard-SciFi-idea-generator) or any other generator repo.
- **Not Unit-canon.** Scale is not owned here.
- **Not a novel.** No named characters, factions, religions, or generation-ship endings.

## 3. How to load Layer A into a model

1. Clone this repo.
2. Put [`bible/layer-a-ai.md`](bible/layer-a-ai.md) in the model context. That file is the load.
3. Do not also dump Layer B, Layer C, or this README into the same context unless the model is revising the bible or mapping a still.
4. If the model asks a question that is OPEN, the answer is “unset.” Do not let it fill the gap.
5. Habitat-kit work after load: one cell, three Habitat Cuts, Unit-canon sockets. Anything else is out of scope.

```text
context = bible/layer-a-ai.md
optional, human only = bible/layer-b-wiki.md
optional, production mapping = bible/layer-c-production.md
```

## 4. How Habitat Cuts map

Same cell. Same hull. Epoch is a parameter. IDs are Time-slice’s. Habitat-kit does not fork Time-slice.

| Habitat Cut | Time-slice id | Reads as |
| --- | --- | --- |
| construction | `construction` | Scaffold, incomplete, work lights, arcs |
| operational | `operational` | Hull complete, structured lights, lived-in wear |
| relic | `relic` | Oxidation, breach, debris, ghost signal |

Decay-pass and signal-field sockets stay in Time-slice / Habitat-kit. This repo only says what those states mean in-world.

## 5. Binding numbers

Scale lengths are listed so a stranger can read this table once. They **live in Unit-canon**. This repo must not become a second copy. Change them at https://github.com/Plygonality/Unit-canon

| Quantity | Work figure | Owner / note |
| --- | --- | --- |
| Distance Sol → Kepler-62 | 982 ly | This bible (CANON) |
| Peak speed | 0.2c | Peak, not cruise (CANON) |
| Transit | ~5000–5100 yr | Bang-coast-bang at ~0.001 g (INFERENCE from the two rows above) |
| Kepler-62 mass / luminosity | 0.76 M☉ / 0.26 L☉ | Work figures (CANON). Catalog scatter is OPEN. |
| Swarm outer radius | 3.6 AU | This bible (CANON) |
| Flux at 3.6 AU | ≈ 0.020 S☉ | 0.26 / 3.6² (INFERENCE) |
| Teq | ~120 K | Work figure (CANON) |
| Grid | 1.0 m | [Unit-canon](https://github.com/Plygonality/Unit-canon) |
| Deck | 3.0 m | [Unit-canon](https://github.com/Plygonality/Unit-canon) |
| Airlock | 1.0 m | [Unit-canon](https://github.com/Plygonality/Unit-canon) |
| Human figure | 1.80 m | [Unit-canon](https://github.com/Plygonality/Unit-canon) |

Mass-table correction (CANON): **1 mm @ 1% of a 3.6 AU sphere ≈ 0.012 M⊕**. **12 M⊕ is a 1 m plate @ 1%.** The old 12 M⊕ @ 1 mm figure is a slip. Delete it.

## 6. Toolchain

| Repo | Role relative to this bible |
| --- | --- |
| [Habitat-kit](https://github.com/Plygonality/Habitat-kit) | Builds the one cell. Reads this frame. Does not live here. |
| [Time-slice](https://github.com/Plygonality/Time-slice) | Same seed, three epochs. Habitat Cuts use its IDs. |
| [Probe-kit](https://github.com/Plygonality/Probe-kit) | Crawler / drone / debris instances on the cell. |
| [Unit-canon](https://github.com/Plygonality/Unit-canon) | Grid, deck, airlock, figure. Sole owner of those numbers. |
| [Collection-linter](https://github.com/Plygonality/Collection-linter) | Role checks against Unit-canon. Not a world-fact checker. |
| [Blend-ci](https://github.com/Plygonality/Blend-ci) | Headless cook + hash / lint. Proof that a dump still renders. |

## 7. Non-goals and OPEN items

Non-goals: implement Habitat-kit or Blend-ci here; add Python packages, CI test suites, or a web UI; fill OPEN items; retcon the key-art silhouette into planets b–f; copy Unit-canon values as if this repo owns them; commit artwork binaries.

OPEN items are listed only in [`bible/open-questions.md`](bible/open-questions.md). They stay unset. The large key-art body is not Kepler-62b–f; what it *is* remains OPEN.

Payload class on the 0.2c hop: gram-probes, dormant whole-brain emulations, digital archives. That is a non-goal for living crews and generation ships, not an OPEN item.

MIT. See [`LICENSE`](LICENSE).
