# B3.0.5 — Chat di pulizia grafo narrativo

**Contenuto di questa zip.** Tutto il necessario per la chat tecnica di pulizia e armonizzazione del grafo narrativo della saga *L'Isola dei Tre Venti*.

**Ordine di lettura consigliato:**

1. **`PIANO_PULIZIA_GRAFO_B3_0_5.md`** — il documento principale. Contiene la classificazione delle 10 issue rilevate (3 errori + 5 emerse + 2 ibride), i 9 task ordinati, le 4 decisioni che richiedono validazione di Ray prima dell'esecuzione, e l'output atteso.

2. **`story_graph_v0_2_0.json`** — grafo corrente da pulire. Contiene S1-S5 iniettate, 22 characters, 25 locations, 11 objects, 24 seeds.

3. **`add_story_node.py`** — script attuale con funzioni `load_graph`, `save_graph`, `add_story`, `add_seed`, `mature_seed`, `bloom_seed`, `close_seed`, `update_entity_state`. Da aggiornare a v0.2 nel task 8 del piano.

4. **`bootstrap_graph.py`** — script di bootstrap che crea il grafo da zero. Backup architetturale: dalle entità anagrafiche si può ricostruire la struttura base se serve. Non va toccato in questa chat.

**Script di audit (4 file `audit_N_*.py`):**

Da rieseguire al termine della chat di pulizia come verifica finale. Tutte e 10 le issue devono passare:

- `audit_1_integrity.py` — verifica referenze rotte (task 1 deve passarli tutti)
- `audit_2_schema.py` — coerenza schema e tipi (task 2-3 devono passarli tutti)
- `audit_3_navigability.py` — simmetria tracking e quote (verifica che la pulizia non abbia rotto nulla)
- `audit_4_drift.py` — drift tra nodi di chat diverse (dopo pulizia il drift deve sparire)

**Come usarli:**
```bash
# metti tutti i file in una dir, poi:
python3 audit_1_integrity.py
python3 audit_2_schema.py
python3 audit_3_navigability.py
python3 audit_4_drift.py
```

I path nei file di audit puntano a `/home/claude/story_graph_v0_2_0.json` — da aggiornare al path dove viene salvato nella chat tecnica.

**Output atteso della chat di pulizia:**

- `story_graph_v0_3_0.json` — grafo pulito
- `add_story_node.py` v0.2 — script aggiornato con whitelist estese e validator
- `story_graph.schema.json` — JSON Schema formale (task 7, creazione ex novo)
- `audit_final_report.txt` — log dei 4 audit rieseguiti dopo la pulizia, zero warning

**Regola d'oro della chat tecnica:**

Non toccare la narrazione. Non modificare descrizioni, premesse, note voce, frasi-chiave. Questo è lavoro puramente di struttura dati. Se durante l'esecuzione emerge ambiguità narrativa, fermarsi e chiedere a Ray.

---

*Dopo questa chat, la chat successiva (B3 parte 2) riparte con lo schema stabilizzato per iniettare S6-S7-S8.*
