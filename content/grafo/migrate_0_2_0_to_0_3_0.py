#!/usr/bin/env python3
"""
Migrazione grafo 0.2.0 → 0.3.0.
Applica i task 1-9 del PIANO_PULIZIA_GRAFO_B3_0_5.md.

Non tocca alcuna narrazione. Solo struttura dati.
"""

import json
import copy
from pathlib import Path
from datetime import date

SRC = Path("/home/claude/b3/story_graph_v0_2_0.json")
DST = Path("/home/claude/b3/story_graph_v0_3_0.json")

with open(SRC, "r", encoding="utf-8") as f:
    g = json.load(f)

# Tengo traccia delle modifiche per il migration_log
changes = []

# =============================================================
# TASK 1 — Creare le 2 entità mancanti
# =============================================================

if "pastori" not in g["entities"]["characters"]:
    g["entities"]["characters"]["pastori"] = {
        "type": "gruppo_istituzione",
        "species": "animali_misti_pastori_stagionali",
        "home_location": "pascoli_alti",
        "quadrant": "aria_nord",
        "role_saga": "sfondo_stagionale_coltivatori_del_vento_nord",
        "note": "Gruppo-istituzione come coltivatori_del_cerchio. Scendono con greggi in autunno (S11). Non individuati."
    }
    changes.append("Creata entità characters.pastori (gruppo-istituzione, quadrante aria_nord)")

if "torrente_affluente_foresta" not in g["entities"]["locations"]:
    g["entities"]["locations"]["torrente_affluente_foresta"] = {
        "type": "corso_acqua_minore",
        "quadrant": "terra_ovest",
        "position": "attraversa_foresta_intrecciata_sfocia_fiume_che_gira",
        "features": [
            "piena_primaverile_porta_via_passaggi_precari",
            "tronco_ponte_di_stagione"
        ],
        "role_saga": "luogo_di_s05_ponte_di_rami",
        "_note": "Dettagliato in Bible §8 ma non presente come entità registrata fino a S5."
    }
    changes.append("Creata entità locations.torrente_affluente_foresta (corso d'acqua minore, quadrante terra_ovest)")


# =============================================================
# TASK 2 — Migrare pattern_a_active a stringa con whitelist
# =============================================================

PATTERN_A_WHITELIST = {"none", "pre_eco", "seminato", "attivo", "bloomed"}

# Mappatura deterministica secondo §1 Task 2.2 del piano
PATTERN_A_MIGRATION = {
    "s01": "none",       # era false (bool)
    "s02": "pre_eco",    # era false, ma c'era nota pre-eco visiva
    "s03": "none",       # era false
    "s04": "none",       # era "inattivo" (str)
    "s05": "seminato",   # era "seminato" — invariato
}

for sid, new_val in PATTERN_A_MIGRATION.items():
    if sid in g["stories"]:
        old_val = g["stories"][sid].get("pattern_a_active")
        g["stories"][sid]["pattern_a_active"] = new_val
        if old_val != new_val:
            changes.append(f"{sid}.pattern_a_active: {old_val!r} → {new_val!r}")

# Aggiorno anche quote_tracker pattern_a_stories coerentemente
# Logica: storie con pattern_a_active in {attivo, bloomed} sono "attive"
# "pre_eco" e "seminato" sono presenti ma non contano come pattern manifestato
# Lascio la definizione esistente in quote_tracker ma la riallineo
qt = g.setdefault("quote_tracker", {})
active_pa_states = {"attivo", "bloomed"}
qt["pattern_a_stories"] = sorted([
    sid for sid, s in g["stories"].items()
    if s.get("pattern_a_active") in active_pa_states
])
# Aggiungo un tracker separato per "seminato" e "pre_eco" per visibilità
qt["pattern_a_seminato_stories"] = sorted([
    sid for sid, s in g["stories"].items()
    if s.get("pattern_a_active") == "seminato"
])
qt["pattern_a_pre_eco_stories"] = sorted([
    sid for sid, s in g["stories"].items()
    if s.get("pattern_a_active") == "pre_eco"
])
changes.append("Ricalcolato quote_tracker.pattern_a_stories (solo attivo+bloomed); aggiunti tracker pre_eco/seminato")


# =============================================================
# TASK 3 — Estendere whitelist seed type/status
#          Generalizzare frame_pattern_a → frame
# =============================================================

# Migro tutti i semi con type=frame_pattern_a a type=frame
frame_pattern_a_migrated = []
for seed_id, seed in g["seeds"].items():
    if seed.get("type") == "frame_pattern_a":
        seed["type"] = "frame"
        # Marcatore che conserva l'info: è un frame dell'architettura saga
        seed.setdefault("related_to_saga_architecture", True)
        frame_pattern_a_migrated.append(seed_id)

if frame_pattern_a_migrated:
    changes.append(f"Migrati {len(frame_pattern_a_migrated)} seme(i) da type='frame_pattern_a' → 'frame' "
                   f"(related_to_saga_architecture=true): {frame_pattern_a_migrated}")


# =============================================================
# TASK 4 — Armonizzazione schema campi seme
#   4.a rinomina related_gesture_seed → related_seed
#   4.b rimuovi maturing_type (assorbito in maturing_in_stories[].note)
#   4.c rimuovi bloom_form (assorbito in bloom_type/note)
#   4.d sposta rename_history in g.migration_log
# =============================================================

rename_history_archive = []
for seed_id, seed in g["seeds"].items():

    # 4.a — related_gesture_seed → related_seed
    if "related_gesture_seed" in seed:
        old = seed.pop("related_gesture_seed")
        # Se related_seed già esiste, lo tengo; altrimenti lo promuovo
        if "related_seed" not in seed:
            seed["related_seed"] = old
        else:
            # caso raro: entrambi presenti, unisco in lista
            existing = seed["related_seed"]
            if isinstance(existing, list):
                if old not in existing:
                    existing.append(old)
            else:
                if existing != old:
                    seed["related_seed"] = [existing, old]
        changes.append(f"{seed_id}: related_gesture_seed → related_seed ({old!r})")

    # 4.b — maturing_type
    if "maturing_type" in seed:
        mt = seed.pop("maturing_type")
        # Provo a spostarlo nelle note di maturing_in_stories se esiste
        mat_list = seed.get("maturing_in_stories", [])
        if mat_list and isinstance(mat_list, list):
            # Assegno al primo maturing privo di note
            merged = False
            for entry in mat_list:
                if isinstance(entry, dict) and not entry.get("note"):
                    entry["note"] = f"maturing_type={mt}"
                    merged = True
                    break
            if not merged:
                # metto come nota generale del seme
                seed.setdefault("_absorbed_maturing_type", mt)
        else:
            seed.setdefault("_absorbed_maturing_type", mt)
        changes.append(f"{seed_id}: rimosso maturing_type={mt!r} (assorbito)")

    # 4.c — bloom_form
    if "bloom_form" in seed:
        bf = seed.pop("bloom_form")
        # Provo ad assorbirlo in bloom_type o in una nota bloom
        if "bloom_type" in seed and seed["bloom_type"] != bf:
            seed.setdefault("_absorbed_bloom_form", bf)
        elif "bloom_type" not in seed:
            seed["bloom_type"] = bf
        changes.append(f"{seed_id}: rimosso bloom_form={bf!r} (assorbito)")

    # 4.d — rename_history
    if "rename_history" in seed:
        rh = seed.pop("rename_history")
        rename_history_archive.append({
            "seed_id": seed_id,
            "rename_history": rh
        })
        changes.append(f"{seed_id}: spostato rename_history in migration_log")


# =============================================================
# TASK 5 — Popolare registry g.callbacks dai callback inline
# =============================================================

if "callbacks" not in g or not isinstance(g["callbacks"], dict):
    g["callbacks"] = {}

populated = 0
for sid, story in g["stories"].items():
    for cb in story.get("callbacks_made", []):
        cb_id = cb.get("callback_id")
        if not cb_id:
            continue
        if cb_id in g["callbacks"]:
            # già registrato; verifico conflitti minori senza sovrascrivere
            continue
        # creo record di registry con marcatura di provenienza
        record = copy.deepcopy(cb)
        record["registered_in_story"] = sid
        g["callbacks"][cb_id] = record
        populated += 1

changes.append(f"Popolato registry g.callbacks con {populated} voci da callback inline "
               f"(mantenuti anche inline nei nodi-storia)")


# =============================================================
# TASK 9 — Bump version + migration_log
# =============================================================

g["graph_version"] = "0.3.0"
g["last_updated"] = str(date.today())

mlog = g.setdefault("migration_log", [])
entry = {
    "from_version": "0.2.0",
    "to_version": "0.3.0",
    "date": str(date.today()),
    "phase": "B3.0.5",
    "scope": "pulizia tecnica grafo — nessuna modifica narrativa",
    "changes": changes,
    "whitelist_updates": {
        "ALLOWED_SEED_STATUS": ["active", "seminato", "maturing", "bloomed", "closed"],
        "ALLOWED_SEED_TYPES": [
            "fisico", "gesto", "capacita", "relazionale", "ritmo",
            "spatial_echo", "pattern", "fenomeno", "paura", "frame",
            "luogo"
        ],
        "PATTERN_A_ACTIVE_VALUES": sorted(PATTERN_A_WHITELIST),
        "removed_seed_type": "frame_pattern_a (generalizzato → frame)"
    },
    "deferred_decisions": [
        "Classificazione 'prima scena pattern_a attivo' (S5 vs S7): rimandata a chat narrativa successiva. "
        "Migrazione attuale non assegna alcun 'attivo' a S1-S5; S5 resta 'seminato'."
    ],
    "archived_rename_history": rename_history_archive
}
mlog.append(entry)


# =============================================================
# SCRITTURA
# =============================================================

with open(DST, "w", encoding="utf-8") as f:
    json.dump(g, f, ensure_ascii=False, indent=2)

print(f"Scritto: {DST}")
print(f"Modifiche totali registrate: {len(changes)}")
print(f"graph_version: {g['graph_version']}")
print(f"callbacks registry: {len(g['callbacks'])}")
print(f"rename_history archiviati: {len(rename_history_archive)}")
