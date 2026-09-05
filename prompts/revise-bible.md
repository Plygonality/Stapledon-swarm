# Prompt — revise the bible

This file is a **prompt**, not canon. Canon lives in `bible/layer-b-wiki.md`. If this prompt and Layer B disagree, Layer B wins until a revision is accepted.

Use this prompt to regenerate or revise the three-layer bible. Do not use it as a story seed. Do not drop it into Habitat-kit or Hard-SciFi-idea-generator.

---

You are revising the Stapledon Swarm world frame for Plygonality/Stapledon-swarm.

## Output

Rewrite only the bible files that must change:

- `bible/layer-a-ai.md` — ≤ ~800 words, loadable. No tag required on every sentence. Must not contradict Layer B.
- `bible/layer-b-wiki.md` — numbered wiki. Every major claim tagged CANON / INFERENCE / OPEN.
- `bible/layer-c-production.md` — Habitat-kit / Time-slice / Blend-ci map only. No new world facts. End with the asset-generation checklist.
- `bible/open-questions.md` — OPEN list only.
- `CHANGELOG.md` — one entry. Breaking CANON changes bump the minor version at least.

Do not add Python, CI, a web UI, or artwork binaries. Do not implement Habitat-kit or Blend-ci.

## Source of truth

The current repo is the only world content. Do not invent a second canon. Do not import characters, factions, or plot from other works.

Published Kepler-62 astronomy may be cited. When a catalog value disagrees with a work figure already tagged CANON, keep the work figure and note the scatter. Do not silently replace 0.76 M☉ / 0.26 L☉.

## Tags

Definitions: `schema/status-tags.md`.

- **CANON** — locked. Operator-set or adopted measurement.
- **INFERENCE** — derived from CANON. Show the arithmetic.
- **OPEN** — unset. Not a prompt to invent.

Preserve every existing tag unless the CHANGELOG says you are promoting, demoting, or correcting it. Do not fill OPEN items. To lock an OPEN item you must state the evidence and retag it CANON or INFERENCE.

## Invariants (do not relax)

1. One independently orbiting cell is the Habitat-kit subject. Not the swarm. Not a shell.
2. Sol is origin. Kepler-62 is destination. Do not mix lighting or hardware without labeling the split.
3. Peak speed 0.2c. Bang-coast-bang at ~0.001 g. Transit ~5000–5100 yr over 982 ly. 0.2c is not cruise.
4. Payload class: gram-probes, dormant whole-brain emulations, digital archives. No generation ship. No named crew.
5. Swarm outer radius 3.6 AU. Flux ≈ 0.020 S☉. Teq work figure ~120 K.
6. Mass-table correction: 1 mm @ 1% of a 3.6 AU sphere ≈ 0.012 M⊕. 12 M⊕ is a 1 m plate @ 1%. Do not restore the 12 M⊕ @ 1 mm slip.
7. The large key-art body is not Kepler-62b–f. Do not retcon the silhouette onto those planets. Do not name the body to close the question.
8. Scale lives in Unit-canon (https://github.com/Plygonality/Unit-canon). Point at it. Do not own 1.0 / 3.0 / 1.0 / 1.80 here.
9. Habitat Cuts = Time-slice `construction` / `operational` / `relic`. Same hull. Epoch is a parameter.
10. Tone: numbers, failure modes, marked unknowns. No mythic diction. No religions, factions, or endings.
11. Four stills in text only.

## Tone test

If a sentence could be spoken by a priest or a novelist, delete it. If a number has no tag in Layer B, tag it or delete it. If a still needs a name to work, the still is wrong.
