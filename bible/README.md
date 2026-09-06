# Bible layers

This directory is the world frame. It is not Habitat-kit. It is not a novel.

| File | Layer | Reader | Job |
| --- | --- | --- | --- |
| [`layer-a-ai.md`](layer-a-ai.md) | A | A model | ≤ ~800 words. Load this and stop. Enough to refuse illegal builds. |
| [`layer-b-wiki.md`](layer-b-wiki.md) | B | A human | Numbered wiki. Every major claim tagged CANON / INFERENCE / OPEN. |
| [`layer-c-production.md`](layer-c-production.md) | C | Habitat-kit / Time-slice / Blend-ci | What those repos may instance. Ends with the asset-generation checklist. |
| [`open-questions.md`](open-questions.md) | — | Anyone | OPEN list only. Do not fill it here. |

## How to use them

1. **Load Layer A** into a model that will author Habitat-kit graphs, Time-slice playbooks, or still briefs. Do not also dump Layer B into the same context unless the model is revising the bible.
2. **Read Layer B** when a number is in dispute or a still looks wrong. Layer B wins over Layer A if they drift.
3. **Read Layer C** when mapping a still or a generator state. Layer C does not add world facts.
4. **Leave OPEN items blank.** Filling them in a prompt is a bible revision. Use [`../prompts/revise-bible.md`](../prompts/revise-bible.md).

## What each layer is allowed to contain

| | Layer A | Layer B | Layer C |
| --- | --- | --- | --- |
| Binding numbers | yes, compact | yes, tagged | yes, as sockets / still rules |
| Derivations | only if needed to refuse a build | yes, tagged INFERENCE | no new ones |
| OPEN items | point at the list | tagged in place | “do not instance” |
| Named characters, factions, religions | no | no | no |
| Habitat-kit Python / graphs | no | no | names and sockets only |
| Artwork binaries | point at `stills/` | embed `stills/` with captions in §12–13 | map the three files; do not cook Habitat Cuts |

## Conflict order

1. [`../constraints/operator-rules.md`](../constraints/operator-rules.md)
2. Layer B CANON
3. Layer B INFERENCE
4. Layer A (if B is silent)
5. Layer C mapping
6. OPEN — remain unset

Unit-canon numbers are not owned here. If a length is in dispute, [Unit-canon](https://github.com/Plygonality/Unit-canon) wins for scale. This bible wins for world facts. Operator system stills live in [`../stills/`](../stills/). They do not override tagged claims.
