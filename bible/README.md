# Bible

World frame. Habitat-kit is a different repo. This is not a novel.

| File | Job |
| --- | --- |
| [`wiki.md`](wiki.md) | Numbered wiki. Claims tagged CANON / INFERENCE / OPEN. Source of truth. |
| [`production.md`](production.md) | What Habitat-kit, Time-slice, and Blend-ci may instance. Checklist at the end. |
| [`open-questions.md`](open-questions.md) | OPEN list. Do not fill it. |

## How to use them

1. **Read the wiki** for the world. If a still or a kit dump fights it, the wiki wins.
2. **Read production** when mapping a still or a Habitat Cut. It does not add world facts.
3. **Leave OPEN items blank.** Filling them is a bible revision. Log it in [`../CHANGELOG.md`](../CHANGELOG.md). Programme-history names in the wiki are tagged claims, not OPEN fills on a still.

## What each file is allowed to contain

| | Wiki | Production |
| --- | --- | --- |
| Binding numbers | yes, tagged | sockets / still rules |
| Derivations | yes, tagged INFERENCE | none new |
| OPEN items | tagged in place | do not instance |
| Named characters, factions, religions | programme-history names only, tagged | no |
| Habitat-kit Python / graphs | no | names and sockets only |
| Artwork | embed `stills/` with captions in §12–13 | map the three files; Habitat Cuts stay unshot |

## Conflict order

1. [`../constraints/project-rules.md`](../constraints/project-rules.md)
2. Wiki CANON
3. Wiki INFERENCE
4. Production mapping
5. OPEN stays unset

Unit-canon wins on length. This bible wins on world facts. Key-art: [`../stills/`](../stills/). The stills do not override tagged claims.
