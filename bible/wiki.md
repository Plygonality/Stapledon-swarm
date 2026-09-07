# Wiki

Tagged source. Tags: [`../schema/status-tags.md`](../schema/status-tags.md). OPEN list: [`open-questions.md`](open-questions.md).

## 1. Scope

**CANON.** World frame for one independently orbiting cell in a Stapledon swarm at Kepler-62. Habitat-kit and the rest of the Plygonality stack read it.

**CANON.** This repo is not Habitat-kit, Blend-ci, a swarm integrator, or a story dump for the concept generator.

**CANON.** No named characters, factions, religions, or generation-ship endings.

## 2. Status tags

**CANON.** Major claims in this file carry CANON, INFERENCE, or OPEN.

**CANON.** OPEN means unset. Filling it is a bible revision.

## 3. Sol / Kepler split

**CANON.** Sol is the origin industrial base. Kepler-62 is the destination.

**CANON.** Do not light a Kepler still with a G2 disk. 1 S☉ panel grades on a 0.020 S☉ orbit are not "operational".

**CANON.** Sol-built hardware used at Kepler needs a label on the still or the brief. Unlabeled mix fails.

**OPEN.** Whether Sol keeps a live command loop, or only a 982 yr one-way archive dump.

## 4. Transit

**CANON.** Distance Sol → Kepler-62 is 982 ly.

**CANON.** Peak speed is 0.2c. Cruise at 0.2c is wrong.

**CANON.** Acceleration work figure is ~0.001 g. Profile is bang-coast-bang: boost, coast, brake.

**INFERENCE.** v = 0.2c, a ≈ 0.001 g: ~194 yr per burn, ~19.4 ly per burn, ~943 ly coast, ~4716 yr coast, **~5000–5100 yr** total.

**INFERENCE.** Light-travel is 982 yr. Radio round trip ~1964 yr. No live conversation.

**INFERENCE.** γ(0.2c) ≈ 1.021. Time-dilation is a few percent. Leave it off stills.

**OPEN.** Ship-frame vs barycentric clocks; who keeps time and on what hardware.

**OPEN.** What physically supplies the 0.001 g (beamed sail, onboard drive, staged). The profile is locked. The engine card is not.

## 5. Payload class

**CANON.** Allowed on the hop: gram-probes, dormant whole-brain emulations (WBE), digital archives.

**CANON.** Rejected as the hop design: living crew, generation ship, named passengers.

**CANON.** Dormant WBE are cargo. No shipboard culture.

**OPEN.** Whether any WBE instantiate in meat at destination.

**OPEN.** Whether gram-probes remain a live mesh after arrival or become feedstock.

## 6. Star (work figures)

**CANON.** Target star is Kepler-62. Constellation Lyra. Distance 982 ly.

**CANON.** Work figures: **0.76 M☉**, **0.26 L☉**. Production uses these.

**CANON.** Look-dev spectral class: K2. Disk is orange.

**INFERENCE.** Catalogs often quote ~0.69 M☉, ~0.21 L☉, Teff ~4925 K, R★ ~0.64 R☉, age ~7 Gyr. Cite those as catalog. They do not replace the work figures.

**OPEN.** Exact catalog reconciliation against 0.76 M☉ / 0.26 L☉.

## 7. Planets

**CANON.** Five published transiting planets: Kepler-62b, c, d, e, f. None of them is the large key-art body.

**CANON.** Inner to outer, from the discovery literature:

| Body | Period (d) | a (AU) | Radius (R⊕) | Role |
| --- | --- | --- | --- | --- |
| b | 5.71 | 0.055 | 1.31 | Interior. Off the key-art body. |
| c | 12.44 | 0.093 | 0.54 | Interior. Off the key-art body. |
| d | 18.16 | 0.120 | 1.95 | Interior. Off the key-art body. |
| e | 122.4 | 0.427 | ~1.6 | HZ-class in the literature. Off the key-art body. |
| f | 267.3 | 0.718 | ~1.4 | HZ-class in the literature. Off the key-art body. |

**CANON.** All five orbit well inside 3.6 AU.

**OPEN.** Whether e / f are mined, ignored, or reserved.

**OPEN.** Additional unseen planets. Papers have guessed. This bible adopts none.

## 8. Swarm geometry

**CANON.** Independently orbiting cells. No rigid shell. No ringworld. No solid Dyson sphere.

**CANON.** Outer radius **R = 3.6 AU**. Habitat-kit and the stills treat that as the edge.

**INFERENCE.** Flux at 3.6 AU: F/F⊕ ≈ L/r² = 0.26 / 3.6² ≈ **0.020 S☉**.

**CANON.** Teq work figure at the edge: **~120 K**. Use it. Do not "correct" it in a brief.

**INFERENCE.** Bare 4π, A = 0 absorber at 0.020 S☉ sits near ~105 K. A sun-facing plate sits warmer. 120 K is the work figure between those.

**OPEN.** Waste-heat, view factor, and coating under the 120 K figure.

**OPEN.** Cell count and spacing law inside 3.6 AU.

**CANON.** One Habitat-kit build is one cell.

## 9. Mass budget

**CANON.** Mass-table correction: **1 mm of plate at 1% of a 3.6 AU sphere ≈ 0.012 M⊕**.

**CANON.** **12 M⊕ is a 1 m plate at 1%** of the same sphere. The old 12 M⊕ @ 1 mm figure swapped millimeters and meters. Delete it.

**INFERENCE.** Sphere area 4πR² at 3.6 AU ≈ 3.64 × 10²⁴ m². The two rows differ by 1000× thickness, so 1000× mass.

**INFERENCE.** Mean density implied by 0.012 M⊕ @ 1 mm @ 1% is ~2 g cm⁻³. That is not a material spec.

**OPEN.** Plate thickness and fill fraction of the built swarm.

**OPEN.** Alloy / ice / slag mix.

**INFERENCE.** 1 mm at 1% is cheap in planetary mass. 1 m at 1% is a small planet taken apart. Drawing both on one budget fails.

## 10. One cell

**CANON.** Habitat-kit may build one independently orbiting cell. Hard-surface. Industrial / brutalist. Unit-canon sockets.

**CANON.** Scale is not owned here. Grid 1.0 m, deck 3.0 m, airlock 1.0 m, human 1.80 m live in [Unit-canon](https://github.com/Plygonality/Unit-canon).

**CANON.** Habitat-kit actors already named: airlock, deck bay, truss, hatch. No second actor set in this bible.

**OPEN.** Interior program beyond those actors (labs, tanks, racks, unused volume).

**OPEN.** Atmosphere mix, pressure, shirtsleeve volumes.

**OPEN.** Power architecture (beamed, local PV, RTG-class, waste-heat loop).

**OPEN.** In-system propulsion after arrival: what brakes a cell, what station-keeps it.

## 11. Habitat Cuts

**CANON.** Three states. Time-slice epoch IDs. Habitat-kit does not fork Time-slice.

| Cut | Time-slice id | Reads as |
| --- | --- | --- |
| construction | `construction` | Scaffold, incomplete, work lights, arcs. Almost no oxidation. |
| operational | `operational` | Closed hull. Structured lights. Wear. Scaffold gone. |
| relic | `relic` | Oxidation, breach, debris. Leftover signal. Scaffold gone. |

**CANON.** Same hull. Epoch is a parameter. It does not redesign the cell.

**OPEN.** The failure mode that produces the relic cut (abandonment, impact, thermal, instruction halt).

## 12. Key-art body

**CANON.** The large body in the system stills is **not** Kepler-62b, c, d, e, or f.

**CANON.** In the key-art stills the silhouette is irregular, non-spherical, with blocky / cutout edges. It is not a circular planet disk.

**CANON.** Do not move that silhouette onto planets b–f. Do not label it 62e or 62f so the still "reads".

![01-eclipse: irregular key-art body against Kepler-62](../stills/01-eclipse.jpg)

*The large body. Irregular, non-spherical, blocky / cutout edges. Not a circular planet disk. Not Kepler-62b–f. Identity and name stay OPEN.*

**OPEN.** What the body is: constructed, captured, or a non-planet natural.

**OPEN.** Its name. Do not assign one to close the question.

## 13. Stills

**CANON.** Three system stills sit in [`../stills/`](../stills/). Key-art. Habitat-kit does not have to match them. Habitat Cuts are a different set.

### 13.1 Eclipse. `stills/01-eclipse.jpg`

![Kepler-62 with an irregular silhouette on the disk and a cell veil](../stills/01-eclipse.jpg)

*Wide. Star in the middle. Kepler-62 as an orange-yellow K disk, granulation and prominences. Large irregular body in silhouette on the disk. Planets b–f are out. Swarm as stacked veils of dark cells. Radial traces can cut the veil. Key is the star. Cell count and fill stay OPEN.*

**CANON.** Frame as captioned. Large body rule as in §12.

### 13.2 Lattice. `stills/02-lattice.jpg`

![Rows of dark geometric cells receding, K-disk in the upper right](../stills/02-lattice.jpg)

*Wide. Star in a corner. K disk. Distant cells as repeated sharp silhouettes (arrowhead, diamond, triangular). Rows recede on faint red traces. Red-brown haze is fine. Small circular disk may sit on the limb. That disk is not the large body. Planet letter stays OPEN. Marks are distant silhouettes.*

**CANON.** Frame as captioned.

### 13.3 Inward. `stills/03-inward.jpg`

![Looking inward: lattice on the disk, small circular transit, irregular body in the foreground](../stills/03-inward.jpg)

*Camera already inside the swarm. Fine lattice across the disk. Same class of irregular foreground body as 13.1. Small circular transit on the star is a different object. Do not pick a planet letter. This is not a Habitat Cut.*

**CANON.** Frame as captioned.

**CANON.** A small circular disk on the star may be a published planet. It is not the large key-art body.

**OPEN.** Which of b–f, if any, is that circular transit disk.

**CANON.** These frames do not lock cell count, plate thickness, or fill fraction.

**CANON. Habitat Cut stills (unshot).** Construction, operational, relic of one close-up cell. States as in §11. Unit-canon figure or airlock in frame for scale. Probe-kit crawler / drone / debris as instances only. Same camera across the three cuts if you are proving Time-slice.

**CANON.** Diamond and arrowhead marks in the key-art are system-scale silhouettes. Habitat-kit builds one industrial / brutalist cell at Unit-canon scale.

**INFERENCE.** The three key-art files show system scale and the large-body rule. Habitat Cuts show the cell Habitat-kit is allowed to build.

## 14. Failure modes

**CANON.** Reject a brief or a still that does any of these:

- Treats 0.2c as cruise, or 982 yr as ship time.
- Sends meat crews as the hop design.
- Restores 12 M⊕ as the 1 mm swarm.
- Lights a Kepler cell as Sol / 1 S☉.
- Labels the large key-art body as Kepler-62b–f.
- Treats the distant diamond / arrowhead marks as the Habitat-kit mesh.
- Builds the whole swarm inside Habitat-kit.
- Fills an OPEN item with a name, a church, or a government.
- Copies Unit-canon lengths into this repo as if owned here.

## 15. Non-goals

**CANON.** This bible does not:

- Run N-body swarm dynamics.
- Specify a language, flag, or government.
- Replace Hard-SciFi-idea-generator.
- Replace Unit-canon, Habitat-kit, Time-slice, Probe-kit, Collection-linter, or Blend-ci.
- Close the OPEN list.
