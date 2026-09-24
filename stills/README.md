# Key-art stills

Caches of key-art, two families. Tracked with Git LFS. They are not Habitat Cuts and they are not source of truth: tagged wiki claims win.

| Family | Files | When / where |
| --- | --- | --- |
| Kepler system | `01-eclipse.jpg`, `02-lattice.jpg`, `03-inward.jpg` | Destination. After settlement. K2 disk. |
| Sol launch | `04-boom.jpg`, `05-cross.jpg`, `06-face.jpg`, `07-fleet.jpg` | Origin. Original probes leaving Earth, 2085–2095 A.D. |

Habitat Cuts (`construction` / `operational` / `relic`) are generated from [Habitat-kit](https://github.com/Plygonality/Habitat-kit):

```bash
python -m habitat_kit apply-script --all-states --object HabitatModule
```

Those PNGs live in Habitat-kit `screenshots/`. Do not dump them here.

Habitat-kit does not have to match these frames. Reader-facing dates in the bible are Gregorian A.D.

## Kepler system

![Kepler-62 with an irregular silhouette on the disk and a cell veil](01-eclipse.jpg)

*`01-eclipse.jpg`. Wide. Star in the middle. Kepler-62 as an orange-yellow K disk, prominences. Large irregular body in silhouette. Not Kepler-62b–f. Swarm as stacked veils of independently orbiting dark cells, not a rigid lattice. Locks: large-body shape class, K-disk, veil.*

![Rows of dark geometric cells receding, K-disk in the upper right](02-lattice.jpg)

*`02-lattice.jpg`. Wide. Star in the upper right. Distant cells as repeated sharp silhouettes (arrowhead, diamond, triangular). Apparent rows are a camera effect on independent orbits. Filename does not lock a rigid grid. Faint red traces, red-brown haze allowed. Small circular disk may sit on the limb. That disk is not the large body. Planet ID OPEN. Locks: distant cell silhouette, traces / haze.*

![Looking inward: lattice on the disk, small circular transit, irregular body in the foreground](03-inward.jpg)

*`03-inward.jpg`. Camera already inside the swarm. Fine field of independent cells across the disk. Same irregular foreground body as `01-eclipse`. Small circular transit is a different object. Not a Habitat Cut. Locks: inward camera, cell field on the disk, transit ≠ large body.*

## Sol launch

Late 21st century. Original gram-class Von Neumann probes on laser-driven lightsails. Earth is Earth. These are not Kepler stills. Launch diamonds are not the distant cell marks in `02-lattice`.

![Hub, chassis, and four spars of a lightsail probe, Earth faint in the background](04-boom.jpg)

*`04-boom.jpg`. Close. Hub and chassis. Four long spars. Thin truss. Dark bays on the body are look-dev, not a mass-row change. Sail membrane may be out of key. Earth limb faint behind. 2085–2095 A.D. window, not a locked day. Locks: four-boom layout, gram-class hub, gossamer frame.*

![Edge-on lightsail as a thin bright cross against Earth's disk](05-cross.jpg)

*`05-cross.jpg`. Far. Edge-on. Membrane so thin it reads as a bright cross. Hub as a speck. Earth disk and atmosphere limb. An unlit face may sit as a dark diamond. Locks: edge-on cross, Earth as origin, extreme thinness. Does not lock range or sail metres.*

![Reflective diamond lightsail, square-on-point, four circular illumination marks](06-face.jpg)

*`06-face.jpg`. Close. Reflective diamond membrane, square-on-point. Four spars. Hub at centre. Soft circular marks on the face are look-dev illumination. They do not lock beam count, wavelength, or aperture. Locks: diamond planform, reflective face.*

![Several diamond lightsails as dark silhouettes against Earth's limb](07-fleet.jpg)

*`07-fleet.jpg`. Wide. Earth's limb. Several diamond silhouettes at different distances. Nearest may show a bright hub. Visible count is camera selection. A batch is still of order 1 000. Locks: batch departure as a visual class, diamond silhouette from afar.*

| File | Camera | What it locks |
| --- | --- | --- |
| [`01-eclipse.jpg`](01-eclipse.jpg) | Wide, star in the middle. Large irregular body on Kepler-62. | Body is non-spherical. Swarm as cell veils. Star is a K disk with prominences. |
| [`02-lattice.jpg`](02-lattice.jpg) | Wide, star in the upper right. Receding cells. | Distant cells as repeated sharp silhouettes. Not a rigid lattice. Faint red traces / haze allowed. |
| [`03-inward.jpg`](03-inward.jpg) | Inside the swarm, looking in. Foreground irregular body. Independent cells on the disk. | Same large-body rule. Small circular transit on the star is a different object. |
| [`04-boom.jpg`](04-boom.jpg) | Close. Hub, chassis, four spars. Earth faint. | Four-boom layout. Gram-class hub. Gossamer frame. Sol departure. |
| [`05-cross.jpg`](05-cross.jpg) | Far. Edge-on cross on Earth's disk. | Edge-on thinness. Earth is the origin. |
| [`06-face.jpg`](06-face.jpg) | Close. Reflective diamond face. | Square-on-point planform. Reflective membrane. Face marks are look-dev. |
| [`07-fleet.jpg`](07-fleet.jpg) | Wide. Several diamonds on Earth's limb. | Fleet as a visual class. Visible count is not batch size. |

## Rules

Kepler system:

- The large irregular silhouette is **not** Kepler-62b–f. Do not label it. Do not name it.
- A small circular disk on the star may be a published planet. Do not pick the letter. Do not treat it as the large body.
- Those three frames do not set cell count, plate thickness, or fill fraction. Those stay OPEN.
- Habitat-kit builds one close-up cell. The diamond / arrowhead marks in `01`–`03` are distant silhouettes.
- Kepler stills do not lock a year.

Sol launch:

- Earth in `04`–`07` is Earth. Do not caption them as Kepler-62.
- Launch diamonds are gram-class sails. They are not Kepler cell silhouettes and not the Habitat-kit mesh.
- Diamond planform is look-dev. The adopted family table still quotes circular diameters as equivalent-area figures.
- Face marks do not lock beam count, pointing, or aperture. That stays OPEN.
- These frames do not lock sail metres, boom length, membrane thickness, or whether the sail stays attached after the boost.
- Visible fleet count does not lock the batch size. Batches remain of order 1 000.
- The frames lock the 2085–2095 A.D. window, not a day inside it.

Habitat Cuts (`construction` / `operational` / `relic`) are not in this folder. They are generated from Habitat-kit and stay unshot here.

Tagged write-up: [`../bible/wiki.md`](../bible/wiki.md) §12–13. Probe look-dev: [`../bible/probes.md`](../bible/probes.md) §11. Production map: [`../bible/production.md`](../bible/production.md) §4. Reader-facing dates in the bible are Gregorian A.D.
