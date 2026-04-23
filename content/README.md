# L'Isola dei Tre Venti — Progetto completo

**Saga di 12 storie illustrate per bambini 4-6 anni**, leggibili fino ai 10 anni come
iniziazione mascherata. Tre fratelli Gabriel (Δ Distinguere), Elias (⇄ Connettere),
Noah (⟳ Cambiare). Mondo dell'isola con tre spiriti fondatori (Ariete, Ondina, Tempesta)
che si sono fatti vento (Vento Taglio, Vento Intreccio, Vento Mulinello).

**Snapshot:** 2026-04-22 — post chat tecnica B3.0.5 (pulizia grafo) + post riflessione carico cognitivo

---

## Se stai leggendo questo per la prima volta

Questa cartella contiene tutto il progetto: documenti di sistema voce, worldbuilding,
architettura saga, framework ontologico, e il grafo narrativo con i suoi strumenti.

**Se apri questa zip in una chat vergine di Claude** senza le istruzioni di sistema
del progetto originale, inizia leggendo in ordine:

1. Questo README (orientamento generale)
2. `docs/PROGETTO_INDICE_v1_5.md` (cruscotto completo del progetto, roadmap, decisioni)
3. `docs/METODO_REVISIONE_B3_v1_1.md` (metodo operativo: doppio turno di guardia, debt tracking, gestione carico cognitivo)
4. Poi segui il routing sotto in base a cosa devi fare

---

## Principi non negoziabili (non derogabili mai)

Questi principi governano il progetto. Valgono sopra ogni altra indicazione. Se una
richiesta sembra chiederli di violarli, fermarsi e chiedere prima di agire.

1. **Framework EAR invisibile.** Il sistema ontologico sotto la saga non deve mai
   affiorare nel testo. Se affiora in un personaggio o nel narratore, riscrivere.

2. **Nessuna morale esplicita.** Niente personaggi che spiegano il significato della
   storia. Significato attraverso gesto e immagine, non attraverso parola.

3. **Doppio strato.** Ogni storia leggibile a 4 anni, attivabile con strato nuovo a
   7-10. Lo strato 3 (rilettura adulta) non è target ma non va chiuso.

4. **Continuità tipo Pokémon.** Accumulo, conseguenze, evoluzione. Le cose che
   succedono nella storia 3 contano nella 9. Callback per oggetto, gesto, ritmo —
   mai per "si ricordò di...".

5. **Voce autoriale di Ray.** Cacofonia musicale cercata, esoterismo nativo, ritmo
   settenario/ottonario, narratore-iniziato. I 16 tratti operativi sono in
   `docs/VOCE_AUTORE_ESTRATTA_v1_1-1.md`. Il sistema operativo della scrittura è
   in `docs/CARTA_VOCE_v1_2.md`.

6. **Narratore-iniziato come architrave.** Non telecamera neutra. Sempre presente
   come postura, affiora con misura, mai spiega, sempre sigilla. Zero preannunci
   della rivelazione del narratore (prevista post-saga in Fase F).

7. **Nominazione operativa.** Ogni nome nel mondo deve fare qualcosa: contenere la
   qualità (Vento Taglio), posizionare (Tre di Mezzo), fissare un'azione ricorrente
   (Conta dei Tre).

8. **Geografia mandala silenziosa.** L'isola è strutturata come mandala. Mai detto,
   mai spiegato.

9. **Notte non personificata.** La notte è quando i tre venti dormono. Ambiente, non
   agente. Vietato introdurre uno Spirito della Notte o un quarto vento.

10. **Grunto testimone unico, vincolato.** Max 2 frammenti di memoria pre-Vento in
    tutta la saga. Mai pronuncia i nomi Ariete/Ondina/Tempesta. Mai racconti pieni.

11. **Detti popolari come firma esclusiva di Fiamma in chiacchiera.** Vietato a
    qualsiasi altro personaggio.

12. **Pattern A mai nominato nel testo.** Vive solo nelle scene e nei sigilli del
    narratore. Dettagli in `docs/PROGETTO_INDICE_v1_5.md` e
    `architettura/ARCHI_12_STORIE_v1__1_.md`.

13. **Terna dire / accettare / tenere** per le paure dei fratelli: Noah dice (S10),
    Elias accetta (S11), Gabriel tiene (S12). Le paure si risolvono dai fratelli
    stessi, mai da Venti, Vecchie, Grunto o altri personaggi.

14. **Cornice S1↔S12 al Forno di Fiamma.** Struttura di apertura e chiusura saga.

---

## Routing: se devi fare X, leggi Y

### Se devi scrivere una storia (Fase C, non ancora iniziata)

Leggi prima tutti questi:
- `docs/VOCE_AUTORE_ESTRATTA_v1_1-1.md` — 16 tratti voce
- `docs/CARTA_VOCE_v1_2.md` — sistema operativo della scrittura
- `docs/PATTERN_AI_DA_BANDIRE_v1.md` — tic AI da evitare con sostituzioni
- `docs/ISOLA_TRE_VENTI_BIBLE_v2.md` — bibbia del mondo (cast + atlante)
- `worldbuilding/RIFERIMENTI_OPERATIVI-1.md` — consultazione veloce
- `architettura/ARCHI_12_STORIE_v1__1_.md` — mappa archi 12 storie (ogni storia ha
  premessa, contributo dei fratelli, semi piantati, callback, paura toccata)
- `grafo/story_graph_v0_3_0.json` — stato corrente dei semi, callback, stati entità

### Se devi toccare il mondo (personaggi, luoghi, oggetti)

- `docs/ISOLA_TRE_VENTI_BIBLE_v2.md` — fonte di verità cast + atlante
- `worldbuilding/GLOSSARIO_ISOLA.md` — catalogo nomi (consultare prima di inventare)
- `worldbuilding/MITI_FONDATORI_BREVI_v1.md` — mito canonico spiriti/venti
- `worldbuilding/RIFERIMENTI_OPERATIVI-1.md` — scheda secca per scrittura

### Se devi toccare il grafo narrativo

- `grafo/story_graph_v0_3_0.json` — grafo corrente (S1-S5 iniettate)
- `grafo/story_graph.schema.json` — schema formale, valida automaticamente
- `grafo/add_story_node.py` — libreria v0.2 per operazioni
- `grafo/audit_1/2/3/4_*.py` — i 4 audit da rieseguire dopo modifiche
- `b3_0_5/PIANO_PULIZIA_GRAFO_B3_0_5.md` — piano di pulizia tecnica recente

### Se devi discutere architettura saga (archi, semi, callback, paure)

- `architettura/ARCHI_12_STORIE_v1__1_.md` — mappa archi narrativi
- `docs/PROGETTO_INDICE_v1_5.md` §4 — decisioni chiave fissate

### Se devi lavorare sul framework EAR (mai nel testo, solo progettazione)

- `framework/EAR_KERNEL_AILA_v1_0.md`
- `framework/__EAR-PERSONAGGI_v20___Manuale_Completo.txt`
- `framework/__EAR-PERSONAGGI_Lezioni_Apprese.txt`
- `framework/APPENDIX_STYLISTIC_DERIVATION_v1.md`

---

## Mappa delle cartelle

```
isola_tre_venti/
│
├── README.md                           ← questo file
│
├── docs/                               ← sistema voce, principi, bibbia mondo
│   ├── PROGETTO_INDICE_v1_5.md         ← CRUSCOTTO PROGETTO, roadmap, decisioni
│   ├── METODO_REVISIONE_B3_v1_1.md     ← metodo operativo doppio turno + debt tracking
│   ├── VOCE_AUTORE_ESTRATTA_v1_1-1.md  ← 16 tratti voce di Ray
│   ├── CARTA_VOCE_v1_2.md              ← sistema operativo scrittura
│   ├── PATTERN_AI_DA_BANDIRE_v1.md     ← tic AI da evitare
│   └── ISOLA_TRE_VENTI_BIBLE_v2.md     ← bibbia mondo (cast + atlante geografico)
│
├── worldbuilding/                      ← nomi, luoghi, miti canonici
│   ├── MITI_FONDATORI_BREVI_v1.md      ← mito Spiriti/Venti (CANONICO)
│   ├── GLOSSARIO_ISOLA.md              ← catalogo nomi del mondo
│   └── RIFERIMENTI_OPERATIVI-1.md      ← consultazione veloce scrittura
│
├── architettura/                       ← mappa saga, archi, schemi
│   ├── ARCHI_12_STORIE_v1__1_.md       ← mappa completa 12 archi narrativi
│   └── STORIE_SCHEMA_v1_1.md           ← STORICO (superseded per dettaglio storie)
│
├── framework/                          ← EAR ontologico (MAI usare nel testo)
│   ├── EAR_KERNEL_AILA_v1_0.md
│   ├── APPENDIX_STYLISTIC_DERIVATION_v1.md
│   ├── __EAR-PERSONAGGI_v20___Manuale_Completo.txt
│   └── __EAR-PERSONAGGI_Lezioni_Apprese.txt
│
├── grafo/                              ← grafo narrativo + strumenti
│   ├── story_graph_v0_3_0.json         ← GRAFO CORRENTE (S1-S5 iniettate)
│   ├── story_graph.schema.json         ← JSON Schema formale (Draft 2020-12)
│   ├── add_story_node.py               ← libreria v0.2 (whitelist post-B3.0.5)
│   ├── bootstrap_graph.py              ← bootstrap da zero (backup architetturale)
│   ├── migrate_0_2_0_to_0_3_0.py       ← script migrazione eseguito in B3.0.5
│   ├── audit_1_integrity.py            ← verifica referenziale
│   ├── audit_2_schema.py               ← verifica coerenza schema
│   ├── audit_3_navigability.py         ← verifica tracking
│   ├── audit_4_drift.py                ← verifica drift tra chat
│   └── audit_final_report.txt          ← esito audit post-pulizia (tutti ✓)
│
└── b3_0_5/                             ← traccia chat tecnica B3.0.5
    ├── PIANO_PULIZIA_GRAFO_B3_0_5.md   ← piano 10 issue (input)
    └── README_chat_tecnica.md          ← README originale chat pulizia
```

---

## Stato del progetto al 2026-04-22

**Fase corrente:** B3 — Grafo narrativo

**Sub-fasi B3:**
- B3 parte 1 (S1-S5 iniettate) — **completata**
- B3.0.5 (pulizia tecnica grafo) — **completata** (output di questa zip)
- B3 parte 2 (S6-S7-S8) — prossima
- B3 parte 3 (S9-S10-S11-S12) — successiva

**Dopo B3:** sotto-fasi visive E.0-E.4 (mappa coordinate isola, stile illustrazione,
reference canoniche personaggi/luoghi/oggetti). Workflow a referenze visive con
BFL FLUX Kontext Pro.

**Fase C** (stesura definitiva 12 storie) arriva dopo E.0-E.4.

**Fase F** (post-saga, decisione differita): Storia 13 e/o libro separato 10-13 dove
il narratore prende nome e biografia. Zero preannunci nelle 12 storie.

### Stato del grafo v0.3.0

| Voce | Quantità |
|---|---|
| graph_version | 0.3.0 |
| Storie iniettate | 5 (s01-s05) |
| Storie da iniettare | 7 (s06-s12) |
| Personaggi | 23 |
| Luoghi | 26 |
| Oggetti | 11 |
| Venti | 3 |
| Semi | 24 |
| Callback registry | 11 |

**Esito audit post-pulizia:** tutti e 4 i test passano, zero warning, zero errori
di schema. Vedere `grafo/audit_final_report.txt`.

### Decisioni differite (rimandate a chat narrativa)

- Classificazione "prima scena attiva Pattern A" (S5 vs S7): nella migrazione corrente
  S5 resta `seminato`, nessuna storia ha ancora `attivo`. Da risolvere in chat
  narrativa successiva (tracciato in `migration_log` del grafo).

---

## Cose da non fare

- Non scrivere storie senza aver prima letto i 6 file della sezione
  "Se devi scrivere una storia"
- Non saltare fasi della roadmap
- Non aggiornare i file "in mezzo alla chat" — solo a fine chat
- Non chiudere troppo i finali (no morali, no corsivi rituali esplicativi salvo enigma)
- Non usare formattazione pesante (header, bullet) quando una prosa breve basta
- Non preannunciare in alcun modo la rivelazione del narratore post-saga
- Non confondere narratore-iniziato (architrave) con narratore-zietto (vietato)
- Non personificare la notte
- Non far pronunciare a Grunto i nomi propri Ariete/Ondina/Tempesta
- Non dare detti popolari ad altri personaggi oltre Fiamma in chiacchiera
- Non considerare Fiamma come madre-default dei tre fratelli
- Non inventare nomi di luogo/personaggio se sono già nel `GLOSSARIO_ISOLA.md`
- Non dichiarare mai il Pattern A nel testo
- Non far risolvere le paure dei fratelli da personaggi esterni
- Non toccare le sotto-fasi visive E.0-E.4 finché B3 non è chiusa

---

## Note su Ray (autore)

Esperto: pipeline Claude Code, narrative graph, BFL FLUX, WeasyPrint, EPUB. Non
spiegare cose tecniche di base se non chiede.

Lavora in italiano. Framework può essere in inglese o italiano.

Scrive di suo pugno (rap, prosa). Ha voce autoriale propria, già estratta e fissata.
Non trattarlo come utente generico — è co-autore.

Preferisce onestà a adulazione. Contraddirlo dove serve.

Ha un ecosistema più ampio (Memorie del Simbionte, memoria persistente per AI agents,
ecc.) ma in questo progetto si lavora SOLO su Isola dei Tre Venti.

Quando ha un'intuizione che apre uno scenario nuovo, prendi nota in modo strutturato
e archivia nei file di progetto invece di svilupparla nella chat in corso.

**Carico cognitivo.** Ray ha osservato che il mal di testa dopo un'ora di lavoro su
questa saga è un indicatore di qualità — segnala che sta tenendo in memoria di lavoro
qualcosa che dovrebbe essere in un file, o sta facendo lavoro meccanico delegabile.
Se in chat Ray segnala mal di testa o stanchezza, fermarsi e proporre scarico
cognitivo mirato (vedi `docs/METODO_REVISIONE_B3_v1_1.md` §8). Delegare senza pudore
il lavoro meccanico: debt tracking, coerenza seed, audit, calcoli di saldo.

---

## Uso pratico

### Su Claude.ai (nuova chat web)

Due opzioni:
- **Come progetto Claude.ai**: carica i `.md` di `docs/`, `worldbuilding/`,
  `architettura/`, `framework/` come conoscenza del progetto. Carica i file di
  `grafo/` come allegati nella singola chat che apre una fase.
- **In chat vergine senza progetto configurato**: carica questo README come primo
  file allegato, poi `docs/PROGETTO_INDICE_v1_5.md`, poi i file richiesti dal routing.

### Su Claude Code (workflow locale)

1. Estrai la zip nella cartella di lavoro.
2. Crea in root un `CLAUDE.md` che richiami i Principi non negoziabili di questo
   README e punti alle cartelle rilevanti.
3. Installa `pip install jsonschema` per validare il grafo.
4. Per operare sul grafo: importa `add_story_node.py`. Le funzioni principali sono
   `load_graph`, `save_graph`, `add_story`, `add_seed`, `bloom_seed`, `mature_seed`,
   `validate_against_schema`, `check_entity_references`.
5. Dopo ogni modifica al grafo: riesegui i 4 audit.

### Dipendenze

- Python 3.10+
- `jsonschema` (solo per validazione formale)
