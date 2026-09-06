# Layer B — human wiki

Tagged source. If Layer A is shorter or smoother, this file still wins. Tags: [`../schema/status-tags.md`](../schema/status-tags.md). OPEN items are also listed in [`open-questions.md`](open-questions.md).

## 1. Scope

**CANON.** This bible is the world frame for one independently orbiting cell in a Stapledon swarm at Kepler-62. It is context for Habitat-kit and the rest of the Plygonality toolchain.

**CANON.** This bible is not Habitat-kit, not Blend-ci, not a swarm simulator, and not a story file for the concept generator.

**CANON.** No named characters, factions, religions, or generation-ship endings.

## 2. Status tags

**CANON.** Every major claim in this file carries CANON, INFERENCE, or OPEN.

**CANON.** OPEN is unset. Filling it is a bible revision, not look-dev.

## 3. Sol / Kepler split

**CANON.** Sol is the origin industrial base. Kepler-62 is the destination system.

**CANON.** Do not light a Kepler still with a G2 disk. Do not put 1 S☉ panel grades on a 0.020 S☉ orbit and call the cell operational.

**CANON.** Hardware that is Sol-built and Kepler-used must be labeled as such on the still or the brief. Unlabeled mix is a fail.

**OPEN.** Whether Sol keeps a live command loop, or only a 982 yr one-way archive dump.

## 4. Transit

**CANON.** Distance Sol → Kepler-62 is 982 ly.

**CANON.** Peak speed is 0.2c. That number is a peak, not a cruise average.

**CANON.** Acceleration work figure is ~0.001 g. Profile is bang-coast-bang: boost, coast, brake.

**INFERENCE.** v = 0.2c, a ≈ 0.001 g gives ~194 yr per burn, ~19.4 ly per burn, ~943 ly coast, ~4716 yr coast, **~5000–5100 yr** total.

**INFERENCE.** Light-travel is 982 yr. A radio round trip is ~1964 yr. No live conversation.

**INFERENCE.** γ(0.2c) ≈ 1.021. Time-dilation is a few percent. It is not a plot device.

**OPEN.** Ship-frame vs barycentric clocks; who keeps time and on what hardware.

**OPEN.** What physically supplies the 0.001 g (beamed sail, onboard drive, staged). This bible locks the profile, not the engine card.

## 5. Payload class

**CANON.** Allowed on the hop: gram-probes, dormant whole-brain emulations (WBE), digital archives.

**CANON.** Not allowed as the transit design: living crew, generation ship, named passengers.

**CANON.** Dormant WBE travel as cargo, not as a society. No shipboard culture.

**OPEN.** Whether any WBE instantiate in meat at destination.

**OPEN.** Whether gram-probes remain a live mesh after arrival or become feedstock.

## 6. Star (work figures)

**CANON.** Target star is Kepler-62. Constellation Lyra. Distance 982 ly.

**CANON.** Work figures for this bible: **0.76 M☉**, **0.26 L☉**. Production uses these.

**CANON.** Spectral class used for look-dev: K2. Disk is orange, not Sol-white.

**INFERENCE.** Published catalogs often quote ~0.69 M☉, ~0.21 L☉, Teff ~4925 K, R★ ~0.64 R☉, age ~7 Gyr. Those may be cited as catalog. They do not replace the work figures.

**OPEN.** Exact catalog reconciliation against 0.76 M☉ / 0.26 L☉.

## 7. Planets

**CANON.** Five published transiting planets: Kepler-62b, c, d, e, f. None of them is the large key-art body.

**CANON.** Published order, inner to outer (work table for stills; radii/periods from the discovery literature, not invented):

| Body | Period (d) | a (AU) | Radius (R⊕) | Role in this bible |
| --- | --- | --- | --- | --- |
| b | 5.71 | 0.055 | 1.31 | Interior planet. Not the swarm. Not key-art. |
| c | 12.44 | 0.093 | 0.54 | Interior planet. Not the swarm. Not key-art. |
| d | 18.16 | 0.120 | 1.95 | Interior planet. Not the swarm. Not key-art. |
| e | 122.4 | 0.427 | ~1.6 | HZ-class in the literature. Not the swarm. Not key-art. |
| f | 267.3 | 0.718 | ~1.4 | HZ-class in the literature. Not the swarm. Not key-art. |

**CANON.** All five orbit well inside the 3.6 AU swarm bound.

**OPEN.** Whether e / f are mined, ignored, or reserved.

**OPEN.** Additional unseen planets. Literature has speculated; this bible does not adopt any.

## 8. Swarm geometry

**CANON.** The swarm is independently orbiting cells, not a rigid shell, not a ringworld, not a solid Dyson sphere.

**CANON.** Outer radius **R = 3.6 AU**. That is the bound Habitat-kit and stills treat as the swarm edge.

**INFERENCE.** Flux at 3.6 AU: F/F⊕ ≈ L/r² = 0.26 / 3.6² ≈ **0.020 S☉**.

**CANON.** Teq work figure at the swarm edge: **~120 K**. Look-dev uses this. Do not “correct” it in a brief.

**INFERENCE.** A bare 4π, A = 0 absorber at 0.020 S☉ sits near ~105 K. A sun-facing plate sits warmer. ~120 K is a work figure that sits between those limits.

**OPEN.** Waste-heat, view factor, and coating under the 120 K figure.

**OPEN.** Cell count and spacing law inside 3.6 AU.

**CANON.** One Habitat-kit build is one cell, not the swarm.

## 9. Mass budget

**CANON.** Mass-table correction: **1 mm of plate at 1% of a 3.6 AU sphere ≈ 0.012 M⊕**.

**CANON.** **12 M⊕ is a 1 m plate at 1%** of the same sphere. The old 12 M⊕ @ 1 mm figure is a millimeter/meter slip. Delete it.

**INFERENCE.** Sphere area 4πR² at 3.6 AU ≈ 3.64 × 10²⁴ m². The two rows differ by 1000× thickness and therefore 1000× mass.

**INFERENCE.** Mean density implied by 0.012 M⊕ @ 1 mm @ 1% is ~2 g cm⁻³. That is not a material spec.

**OPEN.** Plate thickness and fill fraction of the built swarm.

**OPEN.** Alloy / ice / slag mix.

**INFERENCE.** A 1 mm 1% swarm is cheap in planetary mass. A 1 m 1% swarm is a disassembled small planet. Drawing both as the same budget is a fail.

## 10. One cell

**CANON.** The subject Habitat-kit may build is one independently orbiting cell: hard-surface, industrial / brutalist, Unit-canon sockets.

**CANON.** Scale is not owned here. Grid 1.0 m, deck 3.0 m, airlock 1.0 m, human 1.80 m live in [Unit-canon](https://github.com/Plygonality/Unit-canon).

**CANON.** Habitat-kit actors already named for the cell: airlock, deck bay, truss, hatch. This bible does not add a second actor set.

**OPEN.** Interior program beyond those actors (labs, tanks, racks, unused volume).

**OPEN.** Atmosphere mix, pressure, shirtsleeve volumes.

**OPEN.** Power architecture (beamed, local PV, RTG-class, waste-heat loop).

**OPEN.** In-system propulsion after arrival: what brakes a cell, what station-keeps it.

## 11. Habitat Cuts

**CANON.** Three named states. They are Time-slice epoch IDs. Habitat-kit does not fork Time-slice.

| Cut | Time-slice id | Reads as |
| --- | --- | --- |
| construction | `construction` | Scaffold, incomplete, work lights, arcs. Almost no oxidation. |
| operational | `operational` | Hull complete. Structured lights. Lived-in wear. No scaffold. |
| relic | `relic` | Oxidation, breach, debris. Ghost signal. Scaffold gone. |

**CANON.** Same hull. Epoch is a parameter. It does not redesign the cell.

**OPEN.** The failure mode that produces the relic cut (abandonment, impact, thermal, instruction halt).

## 12. Key-art body

**CANON.** The large body in the system / key-art stills is **not** Kepler-62b, c, d, e, or f.

**CANON.** In the operator stills that body is an irregular, non-spherical silhouette with blocky / cutout edges. It is not a circular planet disk.

**CANON.** Do not retcon that silhouette onto planets b–f. Do not label it 62e or 62f to make the still “read.”

![01-eclipse — irregular key-art body against Kepler-62](../stills/01-eclipse.jpg)

*The large body. Irregular, non-spherical, blocky / cutout edges. Not a circular planet disk. Not Kepler-62b–f. Identity and name stay OPEN.*

**OPEN.** What the body is: constructed, captured, or a non-planet natural.

**OPEN.** Its name. Do not assign one to close the question.

## 13. Stills

**CANON.** Three operator system stills are in [`../stills/`](../stills/). They are key-art. They are not Habitat-kit proofs and not Habitat Cuts.

### 13.1 Eclipse — `stills/01-eclipse.jpg`

![Kepler-62 eclipsed by the irregular key-art body; swarm as a cell veil](../stills/01-eclipse.jpg)

*Operator key-art. Wide, star-centered. Kepler-62 as an orange-yellow K disk with granulation and prominences. A large irregular body sits in silhouette against the disk — not Kepler-62b–f, not a circular planet. The swarm reads as a multi-layer veil of many independent dark cells, not a rigid shell. Radial traces may cut the veil. Exterior key is the star, not Earth noon. Cell count and fill stay OPEN.*

**CANON.** Frame as captioned. Large body rule as in §12.

### 13.2 Lattice — `stills/02-lattice.jpg`

![Receding lattice of dark geometric cells; K-disk in the upper right](../stills/02-lattice.jpg)

*Operator key-art. Wide. Star occupies a corner: K disk, not Sol-white. Distant cells read as repeating sharp geometric silhouettes (arrowhead / diamond / triangular). Rows recede along faint red orbital traces. Red-brown haze allowed. A small circular disk may sit on the stellar limb — that disk is not the large key-art body. Which of b–f, if any, stays OPEN. These marks are system-scale silhouettes, not the Habitat-kit mesh.*

**CANON.** Frame as captioned.

### 13.3 Inward — `stills/03-inward.jpg`

![Inward view: lattice over the disk, small circular transit, same irregular foreground body](../stills/03-inward.jpg)

*Operator key-art. Camera inside the swarm, looking in. Fine lattice / web over the disk. Same class of irregular foreground body as 13.1. A small circular transit disk may sit on the star. That disk is not the large body. Do not assert which published planet it is. Do not treat this frame as a Habitat Cut.*

**CANON.** Frame as captioned.

**CANON.** A small circular disk on the star may be a published planet. Do not treat it as the large key-art body.

**OPEN.** Which of b–f, if any, is that circular transit disk.

**CANON.** These frames do not lock cell count, plate thickness, or fill fraction.

**CANON. Habitat Cut stills (unshot).** Construction / operational / relic of one close-up cell. Scaffold / complete / relic as in §11. Unit-canon figure or airlock readable for scale. Probe-kit crawler / drone / debris allowed as instances, not as a second generator. Same camera family across the three cuts if the set is a Time-slice proof.

**CANON.** Distant diamond / arrowhead marks in the key-art are system-scale silhouettes. They are not the Habitat-kit mesh. Habitat-kit builds one industrial / brutalist cell at Unit-canon scale.

**INFERENCE.** The three operator files sell system scale and the large-body rule. The Habitat Cuts sell the cell Habitat-kit is allowed to build.

## 14. Failure modes

**CANON.** Refuse a brief or a still that does any of the following:

- Treats 0.2c as cruise, or 982 yr as ship time.
- Sends meat crews as the transit design.
- Restores 12 M⊕ as the 1 mm swarm.
- Lights a Kepler cell as Sol / 1 S☉.
- Labels the large key-art body as Kepler-62b–f.
- Treats the distant diamond / arrowhead marks as the Habitat-kit mesh.
- Builds the whole swarm inside Habitat-kit.
- Fills an OPEN item with a name, a church, or a government.
- Copies Unit-canon lengths into this repo as if owned here.

## 15. Non-goals

**CANON.** This bible does not:

- Simulate N-body swarm dynamics.
- Specify a language, flag, or government.
- Replace Hard-SciFi-idea-generator.
- Replace Unit-canon, Habitat-kit, Time-slice, Probe-kit, Collection-linter, or Blend-ci.
- Close the OPEN list.
