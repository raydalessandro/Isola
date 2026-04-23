#!/usr/bin/env python3
"""
add_story_node.py — v0.2 (post B3.0.5)
Aggiunge/aggiorna un nodo-storia nel grafo narrativo.

Novità v0.2:
- Whitelist estese: 'seminato' aggiunto a ALLOWED_SEED_STATUS;
  'luogo' aggiunto a ALLOWED_SEED_TYPES; 'frame_pattern_a' rimosso (generalizzato a 'frame')
- PATTERN_A_ACTIVE_VALUES: whitelist formale per pattern_a_active
  ('none', 'pre_eco', 'seminato', 'attivo', 'bloomed')
- validate_against_schema(graph): valida contro story_graph.schema.json
- check_entity_references(graph): verifica integrità referenziale pre-save
- migrate_pattern_a_active(graph): migrazione bool → str con whitelist
- populate_callbacks_registry(graph): popola g['callbacks'] dai callback inline

Tipi di seme (seed.type):
- fisico          : oggetto tangibile (bastoncino, pagnotta, nido, braccialetto)
- gesto           : azione ricorrente (raccogliere bastoncini, indicare in silenzio)
- capacita        : competenza acquisita (nodo Marinaro di Elias)
- relazionale     : dinamica tra personaggi (Bru-quello-solo)
- ritmo           : codice sonoro (TUM-tum-TUM, TOK-TOK-TOK)
- spatial_echo    : posizione/luogo che acquisisce senso nel ritorno (cengia burrone S1→S12)
- pattern         : appartenenza a Pattern A (cose rotte che arrivano)
- fenomeno        : evento raro del mondo (quando l'acqua trema, Concerto)
- paura           : seme di paura di un fratello (richiede brother + resolution_mode)
- frame           : elemento di cornice saga (pagnotta S1↔S12, Forno, Pattern A architetturale)
- luogo           : luogo che funziona come seme (acquisisce senso con il ritorno)

Status seme:
- active   = piantato, non ancora ripreso
- seminato = seme formale piantato con bloom future pianificate (architetturale)
- maturing = ripreso in storia/e intermedia/e senza bloom (cresce)
- bloomed  = fiorito nella storia target (richiede bloomed_in_story)
- closed   = chiuso definitivamente
"""

import json
from pathlib import Path
from datetime import date

GRAPH_PATH = Path("/home/claude/b3/story_graph.json")
SCHEMA_PATH = Path("/home/claude/b3/story_graph.schema.json")


# =============================================================
# WHITELIST (post B3.0.5)
# =============================================================

ALLOWED_SEED_TYPES = {
    "fisico", "gesto", "capacita", "relazionale", "ritmo",
    "spatial_echo", "pattern", "fenomeno", "paura", "frame",
    "luogo",  # aggiunto in B3.0.5
}

ALLOWED_SEED_STATUS = {
    "active",
    "seminato",  # aggiunto in B3.0.5
    "maturing",
    "bloomed",
    "closed",
}

PATTERN_A_ACTIVE_VALUES = {
    "none",      # pattern non presente nemmeno come eco
    "pre_eco",   # immagine fisica anticipatoria, non semina contabilizzata
    "seminato",  # seme formale piantato, bloom future pianificate
    "attivo",    # pattern visibile nella scena
    "bloomed",   # pattern manifestato pienamente
}

BROTHERS = {"gabriel", "elias", "noah"}
RESOLUTION_MODES = {"dire", "accettare", "tenere"}


# =============================================================
# I/O
# =============================================================

def load_graph(path: Path = GRAPH_PATH) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_graph(graph: dict, path: Path = GRAPH_PATH, validate: bool = True) -> None:
    """
    Salva il grafo. Se validate=True, esegue check_entity_references e
    validate_against_schema (se disponibile) prima di scrivere.
    """
    if validate:
        ref_warnings = check_entity_references(graph)
        if ref_warnings:
            print(f"[save_graph] {len(ref_warnings)} warning di integrità referenziale:")
            for w in ref_warnings[:10]:
                print(f"  ⚠ {w}")
        try:
            schema_errors = validate_against_schema(graph)
            if schema_errors:
                print(f"[save_graph] {len(schema_errors)} errori di schema:")
                for e in schema_errors[:10]:
                    print(f"  ✗ {e}")
        except ImportError:
            print("[save_graph] jsonschema non installato, skip validazione schema")
        except FileNotFoundError:
            print(f"[save_graph] schema non trovato in {SCHEMA_PATH}, skip")

    graph["last_updated"] = str(date.today())
    with open(path, "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)


# =============================================================
# VALIDAZIONE
# =============================================================

def validate_against_schema(graph: dict, schema_path: Path = SCHEMA_PATH) -> list[str]:
    """
    Valida il grafo contro story_graph.schema.json.
    Richiede `jsonschema` installato.
    """
    from jsonschema import Draft202012Validator

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    validator = Draft202012Validator(schema)
    errors = []
    for err in sorted(validator.iter_errors(graph), key=lambda e: list(e.path)):
        path = "/".join(str(p) for p in err.path) or "<root>"
        errors.append(f"at {path}: {err.message}")
    return errors


def check_entity_references(graph: dict) -> list[str]:
    """
    Verifica che tutti gli ID referenziati nei nodi-storia e nei semi
    esistano nel registro entità. Ritorna lista di warning.
    """
    warnings = []

    chars = set(graph["entities"].get("characters", {}).keys())
    subgroups = set()
    for c in graph["entities"].get("characters", {}).values():
        subgroups |= set(c.get("sub_groups", {}).keys())
    locs = set(graph["entities"].get("locations", {}).keys())
    winds = set(k for k in graph["entities"].get("winds", {}).keys() if not k.startswith("_"))
    seeds = set(graph.get("seeds", {}).keys())
    stories = set(graph.get("stories", {}).keys())

    for sid, s in graph.get("stories", {}).items():
        for ch in s.get("characters_in_scene", []):
            cid = ch.get("id")
            if cid and cid not in chars and cid not in subgroups:
                warnings.append(f"{sid}.characters_in_scene: '{cid}' non esiste")
        for ch in s.get("characters_offscreen_or_background", []):
            cid = ch.get("id")
            if cid and cid not in chars and cid not in subgroups:
                warnings.append(f"{sid}.offscreen: '{cid}' non esiste")

        loc_id = s.get("location_primary", {}).get("id")
        if loc_id and loc_id not in locs:
            warnings.append(f"{sid}.location_primary: '{loc_id}' non esiste")
        for loc in s.get("locations_secondary", []):
            lid = loc.get("id")
            if lid and lid not in locs:
                warnings.append(f"{sid}.location_secondary: '{lid}' non esiste")

        w = s.get("wind_active")
        if w and w not in winds:
            warnings.append(f"{sid}.wind_active: '{w}' non esiste")

        for field in ("seeds_planted", "seeds_picked_up",
                      "seeds_bloomed_here", "seeds_maturing_here"):
            for seed_id in s.get(field, []):
                if seed_id not in seeds:
                    warnings.append(f"{sid}.{field}: '{seed_id}' non esiste")

        for cb in s.get("callbacks_made", []):
            fs = cb.get("from_story")
            if fs and fs not in stories:
                warnings.append(f"{sid}.callback {cb.get('callback_id')}: from_story='{fs}' non esiste")

    for seed_id, seed in graph.get("seeds", {}).items():
        for target in seed.get("bloom_target_stories", []):
            if not (target.startswith("s0") or target.startswith("s1")):
                warnings.append(f"{seed_id}: bloom_target='{target}' non sembra uno story_id valido")

    return warnings


def _validate_story_node(graph: dict, node: dict) -> list[str]:
    """Validazione sintetica inline di un singolo nodo-storia."""
    warnings = []
    story_id = node.get("id")
    if not story_id:
        warnings.append("MANCA id")
        return warnings

    pa = node.get("pattern_a_active")
    if pa is not None and pa not in PATTERN_A_ACTIVE_VALUES:
        warnings.append(f"{story_id}: pattern_a_active='{pa}' non in whitelist {sorted(PATTERN_A_ACTIVE_VALUES)}")

    chars = set(graph["entities"].get("characters", {}).keys())
    subgroups = set()
    for c in graph["entities"].get("characters", {}).values():
        subgroups |= set(c.get("sub_groups", {}).keys())
    locs = set(graph["entities"].get("locations", {}).keys())

    for ch in node.get("characters_in_scene", []):
        cid = ch.get("id")
        if cid and cid not in chars and cid not in subgroups:
            warnings.append(f"personaggio non esistente: {cid}")

    loc = node.get("location_primary", {}).get("id")
    if loc and loc not in locs:
        warnings.append(f"location primaria non esistente: {loc}")

    for seed_id in node.get("seeds_picked_up", []):
        if seed_id not in graph.get("seeds", {}):
            warnings.append(f"seed non esistente: {seed_id}")

    return warnings


# =============================================================
# OPERAZIONI
# =============================================================

def add_story(graph: dict, node: dict, overwrite: bool = False) -> list[str]:
    """Aggiunge un nodo-storia. Ritorna warning dalla validazione inline."""
    story_id = node["id"]
    if story_id in graph["stories"] and not overwrite:
        raise ValueError(f"storia {story_id} già presente, usa overwrite=True")

    warnings = _validate_story_node(graph, node)
    graph["stories"][story_id] = node

    qt = graph.setdefault("quote_tracker", {})
    qt.setdefault("pattern_a_stories", [])
    qt.setdefault("pattern_a_seminato_stories", [])
    qt.setdefault("pattern_a_pre_eco_stories", [])
    qt.setdefault("when_water_trembles_stories", [])
    qt.setdefault("night_scenes", [])
    qt.setdefault("tok_tok_tok_stories", [])
    qt.setdefault("fiamma_detti_per_storia", {})
    qt.setdefault("grunto_fragments_used", 0)

    pa = node.get("pattern_a_active")
    if pa in ("attivo", "bloomed"):
        if story_id not in qt["pattern_a_stories"]:
            qt["pattern_a_stories"].append(story_id)
    elif pa == "seminato":
        if story_id not in qt["pattern_a_seminato_stories"]:
            qt["pattern_a_seminato_stories"].append(story_id)
    elif pa == "pre_eco":
        if story_id not in qt["pattern_a_pre_eco_stories"]:
            qt["pattern_a_pre_eco_stories"].append(story_id)

    if node.get("when_water_trembles"):
        if story_id not in qt["when_water_trembles_stories"]:
            qt["when_water_trembles_stories"].append(story_id)

    if node.get("night_scene"):
        if story_id not in qt["night_scenes"]:
            qt["night_scenes"].append(story_id)

    fiamma_detti = 0
    for ch in node.get("characters_in_scene", []):
        if ch["id"] == "fiamma" and ch.get("mode") == "chiacchiera":
            fiamma_detti = ch.get("detti_count", 0)
    if fiamma_detti:
        qt["fiamma_detti_per_storia"][story_id] = fiamma_detti

    for ch in node.get("characters_in_scene", []):
        if ch["id"] == "grunto" and ch.get("fragment_used"):
            qt["grunto_fragments_used"] += 1
            budget = graph["entities"]["characters"].get("grunto", {}).get("fragments_budget")
            if budget is not None:
                budget["used"] = budget.get("used", 0) + 1

        if ch["id"] == "nodo" and ch.get("tok_tok_tok"):
            if story_id not in qt["tok_tok_tok_stories"]:
                qt["tok_tok_tok_stories"].append(story_id)

    graph.setdefault("callbacks", {})
    for cb in node.get("callbacks_made", []):
        cb_id = cb.get("callback_id")
        if cb_id and cb_id not in graph["callbacks"]:
            record = dict(cb)
            record["registered_in_story"] = story_id
            graph["callbacks"][cb_id] = record

    return warnings


def add_seed(graph: dict, seed: dict, overwrite: bool = False) -> None:
    """Aggiunge un seme al registro globale."""
    seed_id = seed["seed_id"]
    if seed_id in graph["seeds"] and not overwrite:
        raise ValueError(f"seme {seed_id} già presente, usa overwrite=True")

    seed_type = seed.get("type")
    if seed_type not in ALLOWED_SEED_TYPES:
        raise ValueError(
            f"tipo seme non valido: {seed_type!r}. Ammessi: {sorted(ALLOWED_SEED_TYPES)}"
        )

    status = seed.get("status", "active")
    if status not in ALLOWED_SEED_STATUS:
        raise ValueError(
            f"status seme non valido: {status!r}. Ammessi: {sorted(ALLOWED_SEED_STATUS)}"
        )

    if seed_type == "paura":
        if seed.get("brother") not in BROTHERS:
            raise ValueError(f"seme 'paura' richiede brother in {sorted(BROTHERS)}, trovato: {seed.get('brother')!r}")
        if seed.get("resolution_mode") not in RESOLUTION_MODES:
            raise ValueError(
                f"seme 'paura' richiede resolution_mode in {sorted(RESOLUTION_MODES)}, "
                f"trovato: {seed.get('resolution_mode')!r}"
            )

    if status == "bloomed" and not seed.get("bloomed_in_story"):
        raise ValueError("seme status='bloomed' richiede bloomed_in_story")
    if status == "maturing" and not seed.get("maturing_in_stories"):
        raise ValueError("seme status='maturing' richiede maturing_in_stories")

    graph["seeds"][seed_id] = seed


def bloom_seed(graph: dict, seed_id: str, in_story: str) -> None:
    """Segna un seme come fiorito."""
    if seed_id not in graph["seeds"]:
        raise ValueError(f"seme {seed_id} non esiste")
    graph["seeds"][seed_id]["status"] = "bloomed"
    graph["seeds"][seed_id]["bloomed_in_story"] = in_story
    story = graph["stories"].get(in_story)
    if story is not None:
        story.setdefault("seeds_bloomed_here", [])
        if seed_id not in story["seeds_bloomed_here"]:
            story["seeds_bloomed_here"].append(seed_id)


def mature_seed(graph: dict, seed_id: str, in_story: str, note: str = "") -> None:
    """Segna un seme come 'maturing'."""
    if seed_id not in graph["seeds"]:
        raise ValueError(f"seme {seed_id} non esiste")
    seed = graph["seeds"][seed_id]
    seed["status"] = "maturing"
    seed.setdefault("maturing_in_stories", [])
    entry = {"story": in_story}
    if note:
        entry["note"] = note
    if not any((isinstance(e, dict) and e.get("story") == in_story) or e == in_story
               for e in seed["maturing_in_stories"]):
        seed["maturing_in_stories"].append(entry)
    story = graph["stories"].get(in_story)
    if story is not None:
        story.setdefault("seeds_maturing_here", [])
        if seed_id not in story["seeds_maturing_here"]:
            story["seeds_maturing_here"].append(seed_id)


def close_seed(graph: dict, seed_id: str, in_story: str, reason: str = "") -> None:
    """Chiude un seme."""
    if seed_id not in graph["seeds"]:
        raise ValueError(f"seme {seed_id} non esiste")
    seed = graph["seeds"][seed_id]
    seed["status"] = "closed"
    seed["closed_in_story"] = in_story
    if reason:
        seed["close_reason"] = reason


def add_callback(graph: dict, callback: dict) -> None:
    """Aggiunge un callback al registro globale."""
    cb_id = callback["callback_id"]
    graph.setdefault("callbacks", {})
    if cb_id in graph["callbacks"]:
        raise ValueError(f"callback {cb_id} già presente")
    graph["callbacks"][cb_id] = callback


def update_entity_state(graph: dict, entity_id: str, story_id: str, state: str,
                        entity_type: str = "characters") -> None:
    """Aggiorna state_by_story di un'entità."""
    ent = graph["entities"][entity_type].get(entity_id)
    if not ent:
        raise ValueError(f"entità {entity_id} non esiste")
    ent.setdefault("state_by_story", {})
    ent["state_by_story"][story_id] = state


def diff_story(graph: dict, story_id: str) -> str:
    return json.dumps(graph["stories"].get(story_id, {}), ensure_ascii=False, indent=2)


# =============================================================
# HELPER DI MIGRAZIONE
# =============================================================

def migrate_pattern_a_active(graph: dict, mapping: dict) -> list[str]:
    """Migra pattern_a_active dei nodi-storia secondo la mappa fornita."""
    changes = []
    for sid, new_val in mapping.items():
        if new_val not in PATTERN_A_ACTIVE_VALUES:
            raise ValueError(f"pattern_a_active nuovo valore non in whitelist: {new_val!r}")
        if sid in graph["stories"]:
            old = graph["stories"][sid].get("pattern_a_active")
            graph["stories"][sid]["pattern_a_active"] = new_val
            if old != new_val:
                changes.append(f"{sid}: pattern_a_active {old!r} → {new_val!r}")
    return changes


def populate_callbacks_registry(graph: dict) -> int:
    """Popola graph['callbacks'] dai callback inline nei nodi-storia."""
    graph.setdefault("callbacks", {})
    added = 0
    for sid, story in graph.get("stories", {}).items():
        for cb in story.get("callbacks_made", []):
            cb_id = cb.get("callback_id")
            if not cb_id or cb_id in graph["callbacks"]:
                continue
            record = dict(cb)
            record["registered_in_story"] = sid
            graph["callbacks"][cb_id] = record
            added += 1
    return added


if __name__ == "__main__":
    g = load_graph()
    print(f"Grafo caricato v{g.get('graph_version')}: "
          f"{len(g['entities']['characters'])} personaggi, "
          f"{len(g['stories'])} storie, "
          f"{len(g['seeds'])} semi, "
          f"{len(g.get('callbacks', {}))} callback")

    ref_warnings = check_entity_references(g)
    if ref_warnings:
        print(f"\n{len(ref_warnings)} warning di integrità referenziale:")
        for w in ref_warnings[:5]:
            print(f"  ⚠ {w}")
    else:
        print("\n✓ Integrità referenziale pulita")

    try:
        schema_errors = validate_against_schema(g)
        if not schema_errors:
            print("✓ Grafo valida contro schema")
        else:
            print(f"{len(schema_errors)} errori di schema:")
            for e in schema_errors[:5]:
                print(f"  ✗ {e}")
    except ImportError:
        print("(jsonschema non installato, skip validazione schema)")
