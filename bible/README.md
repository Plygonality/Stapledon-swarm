# Bible layers

World frame. Habitat-kit is a different repo. This is not a novel.

| File | Layer | Reader | Job |
| --- | --- | --- | --- |
| [`layer-a-ai.md`](layer-a-ai.md) | A | A model | ~800 words or less. Load this and stop. |
| [`layer-b-wiki.md`](layer-b-wiki.md) | B | A human | Numbered wiki. Claims tagged CANON / INFERENCE / OPEN. |
| [`layer-c-production.md`](layer-c-production.md) | C | Habitat-kit / Time-slice / Blend-ci | What those repos may instance. Checklist at the end. |
| [`open-questions.md`](open-questions.md) | | Anyone | OPEN list. Do not fill it. |

## How to use them

1. **Load Layer A** when a model will author Habitat-kit graphs, Time-slice playbooks, or still briefs. Skip Layer B unless you are revising the bible.
2. **Read Layer B** when a number is in dispute or a still looks wrong. Layer B wins if they drift.
3. **Read Layer C** when mapping a still or a generator state. Layer C does not add world facts.
4. **Leave OPEN items blank.** Filling them is a bible revision. Prompt: [`../prompts/revise-bible.md`](../prompts/revise-bible.md).

## What each layer is allowed to contain

| | Layer A | Layer B | Layer C |
| --- | --- | --- | --- |
| Binding numbers | yes, compact | yes, tagged | sockets / still rules |
| Derivations | only if needed to refuse a build | yes, tagged INFERENCE | none new |
| OPEN items | point at the list | tagged in place | do not instance |
| Named characters, factions, religions | no | no | no |
| Habitat-kit Python / graphs | no | no | names and sockets only |
| Artwork | point at `stills/` | embed `stills/` with captions in §12–13 | map the three files; Habitat Cuts stay unshot |

## Conflict order

1. [`../constraints/operator-rules.md`](../constraints/operator-rules.md)
2. Layer B CANON
3. Layer B INFERENCE
4. Layer A (if B is silent)
5. Layer C mapping
6. OPEN stays unset

Unit-canon wins on length. This bible wins on world facts. Operator stills: [`../stills/`](../stills/). They do not override tagged claims.
