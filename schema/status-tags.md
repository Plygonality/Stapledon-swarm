# Status tags

Every major claim in this bible carries one tag. The tag is part of the claim. Do not strip it when quoting.

| Tag | Meaning | Who may change it | What a generator may do |
| --- | --- | --- | --- |
| **CANON** | Locked for this version. Operator-set or published measurement adopted as a work figure. | A tagged bible revision. Not a look-dev pass. | Use as given. Do not “improve.” |
| **INFERENCE** | Derived from CANON by arithmetic, geometry, or a stated model. Wrong if the model is wrong. | A tagged bible revision that shows the derivation. | Use. Prefer the parent CANON if they conflict. |
| **OPEN** | Unset. Not a prompt to invent. | Only a later bible revision that promotes it to CANON or INFERENCE. | Leave blank. Do not fill. Do not name. |

## Rules

1. A sentence without a tag in Layer B is a defect. Fix the sentence or delete it.
2. Layer A may drop tags for density. Layer B remains the tagged source. If Layer A and Layer B disagree, Layer B wins.
3. Layer C does not create world facts. It only maps tagged facts onto Habitat-kit / Time-slice / Blend-ci.
4. Promoting OPEN → CANON requires a CHANGELOG entry and a reason (measurement, operator lock, or derivation now shown).
5. Demoting CANON → OPEN is a breaking change. Bump the minor version at least.
6. Catalog astronomy and this bible’s work figures can differ. When they do, the work figure is CANON for production. The catalog value is noted, not used.

## How to write a tagged claim

```
CANON. Peak speed is 0.2c. That is a peak, not a cruise average.
INFERENCE. Two 0.001 g burns to 0.2c and back, plus a 0.2c coast over 982 ly, total ~5000–5100 yr.
OPEN. Plate thickness and fill fraction of the built swarm.
```

Do not write “maybe,” “perhaps,” or “in the lore.” Use the tag.
