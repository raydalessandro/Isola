#!/usr/bin/env python3
"""Valida world/ contro gli schema JSON e la coerenza cross-entity.

Check:
- ogni id in world/ è univoco
- ogni relazioni[].target_id risolve a un id presente nell'indice
  OPPURE la relazione è di tipo 'porta_socchiusa' (esonerata dal resolve)
- ogni frontmatter valida contro lo schema corrispondente

Exit code 0 se tutto ok, 1 altrimenti.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parent.parent
WORLD = REPO_ROOT / "world"


def _split_frontmatter(text: str) -> dict[str, Any]:
    """Estrae il frontmatter YAML dalla scheda Markdown."""
    # salta eventuale commento HTML iniziale
    lines = text.splitlines()
    i = 0
    # salta righe di commento HTML multiriga (<!-- ... -->)
    if i < len(lines) and lines[i].lstrip().startswith("<!--"):
        while i < len(lines) and "-->" not in lines[i]:
            i += 1
        i += 1  # salta la riga con -->
    # salta eventuali righe vuote
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i >= len(lines) or lines[i].strip() != "---":
        raise ValueError("frontmatter mancante: manca --- di apertura")
    i += 1
    buf: list[str] = []
    while i < len(lines) and lines[i].strip() != "---":
        buf.append(lines[i])
        i += 1
    if i >= len(lines):
        raise ValueError("frontmatter mancante: manca --- di chiusura")
    return yaml.safe_load("\n".join(buf)) or {}


def _load_schema(name: str) -> dict[str, Any]:
    p = WORLD / "_schema" / name
    return json.loads(p.read_text(encoding="utf-8"))


def validate() -> tuple[bool, list[str]]:
    errors: list[str] = []

    char_schema = _load_schema("character.schema.json")
    avatar_schema = _load_schema("avatar.schema.json")
    char_validator = Draft202012Validator(char_schema)
    avatar_validator = Draft202012Validator(avatar_schema)

    all_ids: set[str] = set()
    duplicates: list[str] = []
    # raccogliamo (path, frontmatter, validator) per il secondo passaggio
    records: list[tuple[Path, dict[str, Any], Draft202012Validator]] = []

    # Characters
    for p in sorted((WORLD / "characters").rglob("*.md")):
        try:
            fm = _split_frontmatter(p.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{p}: parse frontmatter fallito: {exc}")
            continue
        cid = fm.get("id")
        if cid is None:
            errors.append(f"{p}: id mancante")
            continue
        if cid in all_ids:
            duplicates.append(cid)
        else:
            all_ids.add(cid)
        records.append((p, fm, char_validator))

    # Avatars
    avatars_dir = WORLD / "avatars"
    if avatars_dir.exists():
        for p in sorted(avatars_dir.rglob("*.md")):
            try:
                fm = _split_frontmatter(p.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"{p}: parse frontmatter fallito: {exc}")
                continue
            cid = fm.get("id")
            if cid is None:
                errors.append(f"{p}: id mancante")
                continue
            if cid in all_ids:
                duplicates.append(cid)
            else:
                all_ids.add(cid)
            records.append((p, fm, avatar_validator))

    for did in duplicates:
        errors.append(f"id duplicato: {did}")

    # Schema validation + ref resolution
    for p, fm, validator in records:
        schema_errs = sorted(validator.iter_errors(fm), key=lambda e: e.path)
        for e in schema_errs:
            errors.append(f"{p}: schema: {list(e.path)}: {e.message}")
        for rel in fm.get("relazioni", []) or []:
            tipo = rel.get("tipo")
            target = rel.get("target_id")
            if tipo == "porta_socchiusa":
                continue
            if target not in all_ids:
                errors.append(
                    f"{p}: relazione {tipo} target_id non risolto: {target}"
                )

    # _index.json coerenza
    idx_path = WORLD / "_index.json"
    if not idx_path.exists():
        errors.append("world/_index.json mancante")
    else:
        idx = json.loads(idx_path.read_text(encoding="utf-8"))
        indexed_ids = {e["id"] for e in idx.get("characters", [])} | {
            e["id"] for e in idx.get("avatars", [])
        }
        missing = all_ids - indexed_ids
        for m in sorted(missing):
            errors.append(f"_index.json: id mancante {m}")
        extra = indexed_ids - all_ids
        for m in sorted(extra):
            errors.append(f"_index.json: id in eccesso {m}")

    return (len(errors) == 0, errors)


def main() -> int:
    ok, errors = validate()
    if ok:
        print("validate: OK")
        return 0
    for e in errors:
        print(f"ERR: {e}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
