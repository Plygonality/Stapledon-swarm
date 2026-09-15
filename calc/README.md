# Launch reference

[`lightsail.py`](lightsail.py) reprints the adopted laser-driven lightsail family. [`check_consistency.py`](check_consistency.py) checks geometry, boost integrals, coast years, the README binding table, and Unit-canon scale rows. [`canon.py`](canon.py) imports grid, deck, airlock, and figure from [Unit-canon](https://github.com/Plygonality/Unit-canon).

`lightsail.py` is stdlib. SI/IAU constants there are a documented local override: Unit-canon has no c / g0 / AU / S☉ fields. Tests need `pip install -e ".[dev]"` (pytest, jsonschema, unit-canon). Neither script is a swarm simulator and neither models braking.

```bash
pip install -e ".[dev]"
pytest -q
python calc/lightsail.py
python calc/check_consistency.py
```

CI runs calc tests only. No image jobs.

Authoritative write-up: [`../bible/appendix-launch.md`](../bible/appendix-launch.md). Tagged claims: [`../bible/probes.md`](../bible/probes.md). Constraint schema: [`../schema/constraints.schema.json`](../schema/constraints.schema.json).

Reader-facing dates in the bible are Gregorian A.D. The script prints durations, not calendar years.
