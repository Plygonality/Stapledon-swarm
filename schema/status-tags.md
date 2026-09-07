# Status tags

Every major claim in the wiki gets one tag. Keep the tag when you quote.

| Tag | Meaning | Who may change it | In a still or kit |
| --- | --- | --- | --- |
| **CANON** | Locked for this version. Set here, or a published number we adopted as a work figure. | A tagged bible revision. Look-dev does not get to move it. | Use it. Do not "improve" it. |
| **INFERENCE** | Follows from CANON by arithmetic, geometry, or a model we stated. Wrong if the model is wrong. | A tagged revision that shows the derivation. | Use it. If it fights the parent CANON, keep the CANON. |
| **OPEN** | Unset. | A later revision that promotes it. | Leave blank. No fill. No name. |

## Rules

1. Wiki sentence with no tag is a defect. Tag it or delete it.
2. `production.md` maps facts. It does not add them.
3. OPEN to CANON needs a CHANGELOG line and a reason (measurement, a lock, or a derivation you can show).
4. CANON down to OPEN is breaking. Bump the minor version.
5. Catalog numbers and work figures can disagree. Production uses the work figure. Catalog stays in a note.

## Claim format

```
CANON. Peak speed is 0.2c. Cruise at 0.2c is wrong.
INFERENCE. Two 0.001 g burns to 0.2c and back, plus a 0.2c coast over 982 ly, total ~5000–5100 yr.
OPEN. Plate thickness and fill fraction of the built swarm.
```

Skip "maybe", "perhaps", "in the lore". Use the tag.
