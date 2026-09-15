"""Every constraints/*.json file must validate against schema/constraints.schema.json."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
CONSTRAINTS_DIR = ROOT / "constraints"
SCHEMA_PATH = ROOT / "schema" / "constraints.schema.json"


def _schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _constraint_json_files() -> list[Path]:
    files = sorted(CONSTRAINTS_DIR.glob("*.json"))
    assert files, f"no constraint JSON files in {CONSTRAINTS_DIR}"
    return files


@pytest.fixture(scope="module")
def validator() -> Draft202012Validator:
    schema = _schema()
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


@pytest.mark.parametrize("path", _constraint_json_files(), ids=lambda p: p.name)
def test_constraint_file_validates(path: Path, validator: Draft202012Validator) -> None:
    instance = json.loads(path.read_text(encoding="utf-8"))
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    messages = [f"{list(err.path)}: {err.message}" for err in errors]
    assert messages == [], f"{path.name} failed schema:\n" + "\n".join(messages)


def test_every_constraints_file_is_json_or_documented_markdown() -> None:
    """Constraint files are JSON. Markdown restatements must name a sibling JSON file."""
    unexpected = []
    json_names = {path.name for path in CONSTRAINTS_DIR.glob("*.json")}
    for path in sorted(CONSTRAINTS_DIR.iterdir()):
        if not path.is_file():
            unexpected.append(f"{path.name}: not a file")
            continue
        if path.suffix == ".json" or path.name == "README.md":
            continue
        if path.suffix == ".md":
            text = path.read_text(encoding="utf-8")
            if not any(name in text for name in json_names):
                unexpected.append(
                    f"{path.name}: markdown restatement must name a constraints JSON file"
                )
            continue
        unexpected.append(f"{path.name}: not JSON and not a documented markdown restatement")
    assert unexpected == [], "constraints/ has files CI cannot validate:\n" + "\n".join(unexpected)


def test_schema_rejects_unknown_keys_and_missing_kind_fields(validator: Draft202012Validator) -> None:
    physics = json.loads((CONSTRAINTS_DIR / "physics.json").read_text(encoding="utf-8"))
    extra = dict(physics)
    extra["not_a_field"] = True
    assert not validator.is_valid(extra)
    missing_rejects = dict(physics)
    del missing_rejects["rejects"]
    assert not validator.is_valid(missing_rejects)
    project = json.loads((CONSTRAINTS_DIR / "project-rules.json").read_text(encoding="utf-8"))
    missing_rules = dict(project)
    del missing_rules["rules"]
    assert not validator.is_valid(missing_rules)
