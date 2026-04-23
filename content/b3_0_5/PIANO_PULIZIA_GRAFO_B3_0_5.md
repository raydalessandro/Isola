# GRAFO NARRATIVO — Piano di Pulizia e Armonizzazione

**Contesto.** Dopo il completamento di S1-S5 (blocco A + metà blocco B), un audit tecnico ha rilevato 10 issue strutturali nel grafo `story_graph_v0_2_0.json`. Questo documento le raccoglie classificandole, propone le fix, e definisce il nuovo schema canonico per le chat successive (S6-S12).

**Fase di riferimento.** B3.0.5 — pulizia tecnica tra parte 1 (S1-S5) e parte 2 (S6-S8) di B3.

**Obiettivo.** Grafo navigabile, schema stabile, drift chiuso. **Non cambiare narrazione — solo struttura.**

**Chat dedicata.** Questo è un task puramente tecnico. Non richiede decisioni narrative. Da eseguire in chat separata breve.

---

## §0. Classificazione issue

### Errori veri (3) — fix obbligata

| # | Issue | Dove | Cosa è successo |
|---|---|---|---|
| 1 | Referenza rotta `pastori` | `stories.s02.characters_offscreen_or_background` | ID entità citato ma mai creato nel registro |
| 2 | Referenza rotta `torrente_affluente_foresta` | `stories.s05.location_primary.id` | ID location citato ma mai creato nel registro |
| 3 | Tipo incoerente `pattern_a_active` | `stories.s01-s05` | bool in S1-S3, str in S4-S5 |

### Emerse organicamente (5) — ratifica richiesta

| # | Issue | Natura | Azione |
|---|---|---|---|
| 4 | Seme con `status="seminato"` | Nuovo stato intermedio | Aggiungere a whitelist |
| 5 | Seme con `type="luogo"` | Nuovo tipo (luogo come seme) | Aggiungere a whitelist |
| 6 | Seme con `type="frame_pattern_a"` | Nuovo tipo | Valutare: generalizzare o mantenere specifico |
| 7 | 4 campi nuovi nei semi chat B | `materiale_associato`, `pattern_a_first_active_scene`, `related_seed`, `related_to_saga_architecture` | Ratificare come opzionali nello schema |
| 8 | 3 campi nuovi in `characters_in_scene` | `client_current`, `distinct_from_sNN`, `plant_named` | Ratificare come opzionali contestuali |

### Ibridi (2) — valutazione caso per caso

| # | Issue | Nota |
|---|---|---|
| 9 | Campi spariti nei semi chat B | `bloomed_in_story`, `brother`, `maturing_planned_stories`, `resolution_mode`, `bloom_form`, `object_ref`, `related_gesture_seed`, `rename_history`, `maturing_in_stories`, `maturing_type` — alcuni utili, alcuni ridondanti |
| 10 | Campi top-level spariti | `key_phrase_attributed_to`, `night_scene_notes`, `wind_transition` — opzionali contestuali, non errori |

---

## §1. Task della chat tecnica

### Task 1 — Creare le due entità mancanti (blocca integrità referenziale)

**1.1** Aggiungere in `entities.characters.pastori`:

```json
"pastori": {
  "type": "gruppo_istituzione",
  "species": "animali_misti_pastori_stagionali",
  "home_location": "pascoli_alti",
  "quadrant": "aria_nord",
  "role_saga": "sfondo_stagionale_coltivatori_del_vento_nord",
  "note": "Gruppo-istituzione come coltivatori_del_cerchio. Scendono con greggi in autunno (S11). Non individuati."
}
```

**1.2** Aggiungere in `entities.locations.torrente_affluente_foresta`:

```json
"torrente_affluente_foresta": {
  "type": "corso_acqua_minore",
  "quadrant": "terra_ovest",
  "position": "attraversa_foresta_intrecciata_sfocia_fiume_che_gira",
  "features": ["piena_primaverile_porta_via_passaggi_precari", "tronco_ponte_di_stagione"],
  "role_saga": "luogo_di_s05_ponte_di_rami",
  "_note": "Dettagliato in Bible §8 ma non presente come entità registrata fino a S5."
}
```

### Task 2 — Uniformare `pattern_a_active` a stringa con whitelist

**2.1** Nuova whitelist per `pattern_a_active`:

```
"none"      → pattern non presente nemmeno come eco
"pre_eco"   → immagine fisica anticipatoria, non semina contabilizzata
"seminato"  → seme formale piantato, bloom future pianificate
"attivo"    → pattern visibile nella scena (prima scena attiva = S7 o S5 secondo revisione)
"bloomed"   → pattern manifestato pienamente
```

**2.2** Migrazione dei valori esistenti:

| Storia | Valore attuale | Nuovo valore |
|---|---|---|
| s01 | `false` (bool) | `"none"` |
| s02 | `false` (bool) | `"pre_eco"` (c'era nota pre-eco visiva) |
| s03 | `false` (bool) | `"none"` |
| s04 | `"inattivo"` (str) | `"none"` |
| s05 | `"seminato"` (str) | `"seminato"` (invariato) |

### Task 3 — Ratificare whitelist estese

**3.1** Aggiornare in `add_story_node.py`:

```python
ALLOWED_SEED_STATUS = {"active", "seminato", "maturing", "bloomed", "closed"}

ALLOWED_SEED_TYPES = {
    # tipi originali
    "fisico", "gesto", "capacita", "relazionale", "ritmo",
    "spatial_echo", "pattern", "fenomeno", "paura", "frame",
    # tipi emersi in chat B
    "luogo", "frame_pattern_a"
}
```

**3.2 — Decisione da prendere.** `frame_pattern_a` vs generalizzazione:
- Opzione A: tenere `frame_pattern_a` come tipo dedicato (è un seme-architettura specifico)
- Opzione B: usare il tipo generico `frame` (più simmetrico con `seed_pagnotta_grunto_rito` che è già `frame`)

**Raccomandazione:** Opzione B (generalizzare). I "frame" della saga sono architetture silenti (cornici S1-S12, Pattern A). Distinguerli per tipo diverso crea inutile proliferazione.

### Task 4 — Armonizzare schema campi seme

**4.1** Dopo analisi caso per caso, questi campi devono essere **mantenuti ufficialmente opzionali** (usati quando applicabili):

**Campi di stato** (mantenere):
- `bloomed_in_story` — obbligatorio se `status="bloomed"`
- `maturing_in_stories` — obbligatorio se `status="maturing"`
- `maturing_planned_stories` — opzionale, lista di storie dove si prevede maturing futuro

**Campi di contesto** (mantenere):
- `brother` — obbligatorio se `type="paura"` (identifica il fratello)
- `resolution_mode` — obbligatorio se `type="paura"` (dire/accettare/tenere)
- `strato` — opzionale (indica lo strato narrativo: strato_3, strato_3_silenzioso, ecc.)

**Campi di riferimento** (mantenere):
- `object_ref` — opzionale, ID oggetto in entities.objects
- `location_ref` — opzionale, ID luogo in entities.locations
- `related_seed` — opzionale, ID di un altro seme collegato
- `related_gesture_seed` — opzionale, alias di `related_seed` specifico per gesti

**Campi di chat B da ratificare**:
- `materiale_associato` — opzionale (materiale fisico legato al seme, es. "rami", "ortica")
- `pattern_a_first_active_scene` — opzionale, booleano (true solo per il seme che marca la prima scena attiva)
- `related_to_saga_architecture` — opzionale, booleano (true per semi-architettura vs semi-scena)

**Campi da rinominare per simmetria**:
- `related_gesture_seed` → unificare con `related_seed` (evitare campo specifico solo per gesti)

**Campi da rimuovere** (ridondanti):
- `maturing_type` → assorbito in `maturing_in_stories[].note`
- `bloom_form` → assorbito in `bloom_type` o in `bloomed_in_story.note`
- `rename_history` → non strutturato, sposta in metadato separato `g.migration_log`

### Task 5 — Pulizia registry callback

**Decisione da prendere:**

- Opzione A: **Rimuovere `g.callbacks`** (sempre vuoto, confonde). I callback vivono inline nei nodi-storia.
- Opzione B: **Popolare `g.callbacks`** retroattivamente copiando gli 11 callback inline, così il registry diventa fonte di verità query-friendly.

**Raccomandazione:** Opzione B. Vantaggi: query singola per "tutti i callback" possibile; indice separato per analisi distribuzione. Costo: 11 voci da copiare (automatizzabile in uno script di 10 righe). Duplicazione accettabile perché callbacks sono write-once.

### Task 6 — Documentare campi top-level opzionali

**Campi top-level del nodo-storia, classificazione definitiva:**

**Obbligatori (34 attualmente universali):**
- tutti quelli presenti in tutte le 5 storie attuali

**Opzionali contestuali:**
- `season_passage` — solo storie di passaggio stagionale
- `key_phrase_indicative` — solo se esiste frase-chiave
- `key_phrase_attributed_to` — solo se frase-chiave attribuita a personaggio (eccezione)
- `key_phrase_notes` — solo se c'è nota sulla frase-chiave
- `wind_transition` — solo quando `wind_active=null` (storia di vento sospeso)
- `night_scene_notes` — solo se `night_scene=true`
- `pattern_a_notes` — solo se `pattern_a_active != "none"`
- `characters_offscreen_or_background` — solo se applicabile
- `seeds_bloomed_here` — solo se bloomed > 0
- `seeds_maturing_here` — solo se maturing > 0
- `seeds_picked_up` — solo se > 0

Aggiungere al documento dello schema un indice `field_obligatoriness` che elenca questi.

### Task 7 — Creare JSON Schema formale

Produrre `story_graph.schema.json` conforme a [JSON Schema Draft 2020-12] che formalizzi:

- Tutte le whitelist (seed types, seed status, pattern_a values, wind IDs)
- Tutti i campi obbligatori/opzionali
- Le relazioni referenziali ($ref su ID)

Vantaggi:
1. Validazione automatica via `jsonschema` library
2. Documentazione auto-generata
3. Un revisore esterno può validare il proprio lavoro prima di consegnarlo
4. LangChain/CrewAI futuro può usarlo per prompt guidance

### Task 8 — Aggiornare `add_story_node.py`

Dopo i task 1-7, aggiornare lo script a versione 0.2:

- Nuove whitelist
- Nuova funzione `validate_against_schema(graph)` che richiama JSON Schema
- Funzione `migrate_pattern_a_active(graph)` che applica task 2.2
- Funzione `populate_callbacks_registry(graph)` per task 5 opzione B
- Funzione `check_entity_references(graph)` che esegue task 1 come validazione pre-save

### Task 9 — Versionamento e log migrazione

**9.1** Bumpare graph_version: `0.2.0` → `0.3.0` (breaking schema change su pattern_a_active)

**9.2** Aggiungere campo `g.migration_log` con entry:

```json
"migration_log": [
  {
    "from_version": "0.2.0",
    "to_version": "0.3.0",
    "date": "2026-04-XX",
    "changes": [
      "Creata entità characters.pastori",
      "Creata entità locations.torrente_affluente_foresta",
      "Migrato pattern_a_active: bool → str con whitelist",
      "Aggiornata ALLOWED_SEED_STATUS con 'seminato'",
      "Aggiornata ALLOWED_SEED_TYPES con 'luogo'",
      "Generalizzato frame_pattern_a → frame",
      "Popolato registry g.callbacks da inline",
      "Pubblicato story_graph.schema.json"
    ]
  }
]
```

---

## §2. Decisioni richieste prima della chat tecnica

Ray deve validare prima dell'esecuzione:

1. **Task 3.2** — `frame_pattern_a` → generalizzare a `frame`? (raccomandato sì)
2. **Task 5** — Registry callback: rimuovere o popolare? (raccomandato popolare)
3. **Task 4** — Conferma lista campi da rimuovere: `maturing_type`, `bloom_form`, `rename_history` (quest'ultimo sposta in migration_log)
4. **Task 4** — Conferma rinomina `related_gesture_seed` → `related_seed`

---

## §3. Ordine di esecuzione nella chat tecnica

1. Creare le 2 entità mancanti (task 1) — sblocca integrità referenziale
2. Migrare `pattern_a_active` (task 2) — uniforma tipo
3. Aggiornare whitelist e script (task 3) — ratifica emersioni
4. Armonizzare campi seme (task 4) — chiude drift chat A/B
5. Decidere sul registry callback (task 5)
6. Documentare campi opzionali (task 6)
7. Generare JSON Schema (task 7)
8. Aggiornare `add_story_node.py` a v0.2 (task 8)
9. Bump version e log (task 9)
10. Eseguire audit di verifica finale — tutte le 10 issue risolte, zero warning

**Output atteso:**
- `story_graph_v0_3_0.json` — grafo pulito
- `add_story_node_v0_2.py` — script aggiornato
- `story_graph.schema.json` — schema formale
- `audit_final_report.txt` — log esito audit post-fix

**Dopo la chat tecnica:** si apre chat B3 parte 2 (S6-S7-S8) con schema stabilizzato. Il revisore esterno può validare il proprio lavoro usando lo schema formale — niente più drift.

---

## §4. Nota per chi eseguirà la chat tecnica

Non modificare nulla della narrazione. Non toccare testi di descrizioni, premesse, note voce. Questo è lavoro puramente di struttura dati. Se durante l'esecuzione emerge ambiguità narrativa, annotare e chiedere a Ray prima di procedere. Non risolvere narrativamente in chat tecnica.

#END
