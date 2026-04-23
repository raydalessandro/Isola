# PROGETTO INDICE — L'Isola dei Tre Venti

**Versione:** 1.5
**Data:** 2026-04-22
**Stato:** Documento master di navigazione e roadmap della saga
**Funzione:** Visione d'insieme del progetto, fasi completate/in corso/pianificate, elenco dei file canonici con numero di versione, decisioni architetturali storicizzate.

**Si parla con:** tutti i file del progetto (elencati in §3).

---

## §1. VISIONE COMPLESSIVA

**Progetto:** saga di 12 storie illustrate per bambini 4-6 anni (leggibili fino ai 10 come iniziazione mascherata), ambientate sull'**Isola dei Tre Venti**. Tre fratelli umani (Gabriel, Elias, Noah) protagonisti, mondo abitato da animali antropomorfizzati. Framework **EAR** (Δ Distinguere / ⇄ Connettere / ⟳ Cambiare) come architettura silente, mai nominato nel testo.

**Prodotti previsti:**
- Libro 0 — *I Tre Miti Fondatori* (libro a sé, racconta la cosmogonia)
- Libri 1-12 — Saga (4 cicli EAR × 3 storie)
- Libro 13 o separato post-saga — sviluppo narratore per fascia 10-13 (Fase F)
- Pipeline di produzione automatizzata (v2 Claude Code native, in sviluppo separato)

**Target principali di lettura:**
- Strato 1 (4-6 anni): evento, sensazione, immagine, emozione semplice
- Strato 2 (7-10 anni): ambiguità, scelte morali implicite, meccanismi del mondo
- Strato 3 (adulto, non target ma aperto): struttura cosmologica/iniziatica — mai chiusa

**Invisibilità** è il vincolo più forte del progetto. Framework EAR mai nominato. Mandala silenzioso (isola + villaggio + venti + stagioni) mai nominato come mandala. Sistema interno di continuità mai visibile al lettore. Pattern A (*le cose rotte arrivano lo stesso*, riconosciuto in B2) mai dichiarato.

---

## §2. ROADMAP — FASI

### ✅ Fase A1 — Impianto voce base

**Chat:** A1
**Output:** `CARTA_VOCE_v1_0.md`, `PATTERN_AI_DA_BANDIRE_v1.md`
**Stato:** ✅ Chiusa

### ✅ Fase A2 — Bibbia cosmologica

**Chat:** A2
**Output:** `ISOLA_TRE_VENTI_BIBLE_v1_0.md`, `MITI_FONDATORI_BREVI_v1.md`
**Stato:** ✅ Chiusa

### ✅ Fase A2.5b-c — Estrazione voce autore + Raffinamento

**Chat:** A2.5b-c
**Output:** `VOCE_AUTORE_ESTRATTA_v1_0.md`, `APPENDIX_STYLISTIC_DERIVATION_v1.md`, `CARTA_VOCE_v1_1.md`, `ISOLA_TRE_VENTI_BIBLE_v1_1.md`
**Stato:** ✅ Chiusa

### ✅ Fase A3 — Bibbia secondari + Atlante isola

**Chat:** A3
**Output:** `ISOLA_TRE_VENTI_BIBLE_v2.md`, `GLOSSARIO_ISOLA.md`, `RIFERIMENTI_OPERATIVI.md`, `CARTA_VOCE_v1_2.md`, `VOCE_AUTORE_ESTRATTA_v1_1.md`
**Stato:** ✅ Chiusa

### ⏭️ Fase B — Architettura narrativa saga

**Fase B1 — Leitmotiv saga.** ⏭️ **SALTATA** (decisione Ray, apertura B2). I Tre Venti sono già leitmotiv strutturale (Bible §1.3, Carta v1.2). Non serve fissarne uno tematico sopra. Riconosciuto in B2 il **Pattern A** come famiglia di immagini ricorrente da onorare nelle chiusure di blocco — non un leitmotiv dichiarato, una continuità sotterranea.

**Fase B2 — Mappa 12 archi narrativi.** ✅ **CHIUSA**.
**Output:** `ARCHI_12_STORIE_v1.md`
**Contenuto:** Per ogni storia: stagione + ciclo, luogo, vento, premessa, problema, contributo dei tre fratelli, momento-soglia, risoluzione, frase-chiave indicativa, semi piantati e ripresi, paura toccata, abitanti in scena con ruolo familiare episodico, palette emotiva, callback, note voce. Distribuzione cast (19 abitanti + 4 gruppi + cuccioli). Distribuzione ruoli familiari episodici (mai stesso adulto due storie di fila). Distribuzione momenti rari (frammenti Grunto, detti Fiamma, address al lettore, frase-firma narratore, paronomastici, cantilene Coltivatori, TOK-TOK Nodo, fenomeno *quando l'acqua trema*, scene notturne). Pattern A riconosciuto. Terna strato 3 *dire/accettare/tenere* identificata. Mismatch principali con `STORIE_SCHEMA_v1_1.md` emendati. Pre-grafo dei semi/callback.

**Fase B3 — Schema grafo narrativo + QUOTE_TRACKER.** 🔄 **IN CORSO**.
**Metodo:** una storia per chat, validazione blocco-per-blocco, doppio turno di guardia (vedi decisione 23 e `METODO_REVISIONE_B3.md`).
**Storie completate nel grafo:**
- ✅ S1 (chat precedente)
- ✅ S2 (chat precedente)
- ✅ S3 (chat precedente)
- ✅ **S4** (chat corrente — `Le Radici che Parlano`)
- ✅ **S5** (chat corrente — `Il Ponte di Rami`)
- ⏭️ S6 prossima chat (`Il Dono per Mèmolo`)
- ⏭️ S7-S12 successive (una per chat)
- ⏭️ Consolidamento grafo post-S6 (revisione e uniformazione nodi)
- ⏭️ Consolidamento grafo post-S12 (QUOTE_TRACKER finale, revisione coerenza cross-storia)

**Output corrente:** `story_graph_v0.2.0.json` (S1-S5 complete, 24 seeds attivi, quote_tracker parziale). Sostituisce `story_graph.json` base. 
**Output da produrre:** `QUOTE_TRACKER.md` (alla fine di B3, post-S12).

**Questioni aperte per il resto di B3:**
- S6: consegna messaggio Stria ai Pastori (off-screen, decisione già presa in B3 come nota in S2), frase precisa di Mèmolo (candidata: *"Le cose che si perdono non si perdono. Si nascondono dove non sai cercare."*), paronomastico fisico (sciarpa di Mèmolo), firma gestuale Vecchie da istituire (indicare in silenzio, bloom S11), detto popolare Fiamma generico su carattere di Mèmolo (non anticipazione trama).
- S8: *quando l'acqua trema* prima apparizione in saga (Liù annuncio come ipotesi).
- S9: Liù vola al Forno con notizia (ipotesi da decidere).
- S11: quattro coni a Elias intenzionali, frase precisa di Mèmolo opzionale.
- S12: TOK-TOK in S12 (implicito o no), frammento pre-Vento Grunto unico saga, *Il Concerto* da aggiungere a Glossario in aggiornamento Fase D.
- Revisione post-S6: promozione di seed impliciti (corda di Nodo) a seed autonomi se confermati, uniformazione nodi S1-S6, decisione globale su gruppi-istituzioni come sfondo vs. attori episodici.

### ⏭️ Fase C — Schemi 12 storie

**Stato:** ⏭️ Futura
**Contenuto:** per ogni storia, schema dettagliato (non scrittura) — beat visivi mappati, dialoghi principali abbozzati, indicazioni di illustrazione, note di voce. Uscita: 12 schemi pronti per Fase D.

### ⏭️ Fase D — Scrittura saga

**Stato:** ⏭️ Futura
**Struttura:** una chat per ogni blocco di 3 storie (4 chat totali). Pipeline `automated-picture-book-v2` entra in gioco qui per ciascuna storia (draft → validate → prompts → assemble). Include riscrittura della pilota S1 (decisione Ray: trama tenuta, voce rifatta), e prima scrittura di S4 e S7 (le pilote esistenti sono solo riferimento di trama, da rifare). Aggiornamenti `GLOSSARIO_ISOLA.md` man mano (es. *Il Concerto* in S12). **Doppio turno di guardia esteso alla prosa** (decisione 23).

### ⏭️ Fase E — Impaginazione + illustrazioni

**Stato:** ⏭️ Futura
**Contenuto:** illustrazioni per le 12 storie via BFL FLUX Kontext Pro; impaginazione PDF/EPUB3 via pipeline; revisione finale voce sui secondari (debito tecnico saggezza-taratura, vedi `CARTA_VOCE_v1_2.md` §5.1); controllo coerenza cross-storia.

### ⏭️ Fase F — Sviluppo narratore post-saga

**Stato:** ⏭️ Futura (post-saga)
**Contenuto:** rivelazione del narratore-iniziato per fascia 10-13. Forma da definire: Storia 13 singola (modello *Verità*) oppure libro separato stile *Il mondo di Sofia*. Apre la porta socchiusa verso *oltre il mare*. Riprende le porte socchiuse della saga: chi è il narratore, cosa vuol dire *visto / respirato* del frammento Grunto S12, frutti da fuori di Bartolo, paura di Gabriel non risolta, storia di Bru, cicatrice di Grunto, genitori dei fratelli.

---

## §3. FILE CANONICI DEL PROGETTO

### §3.1 Documenti attivi (ultima versione)

**Impianto voce e stile:**
- `VOCE_AUTORE_ESTRATTA_v1_1.md` — 16 tratti stilistici estratti + §4 principio memoria-lunga vs canonico mitico
- `APPENDIX_STYLISTIC_DERIVATION_v1.md` — derivazione da corpus adulto
- `CARTA_VOCE_v1_2.md` — regole operative di scrittura, checklist, tabù, quote
- `PATTERN_AI_DA_BANDIRE_v1.md` — pattern AI da evitare, lista chiusa
- `EAR_KERNEL_AILA_v1_0.md` — kernel teorico del framework EAR

**Mondo:**
- `ISOLA_TRE_VENTI_BIBLE_v2.md` — Bible completa del mondo (cosmogonia, protagonisti, cast 19+4 gruppi, luoghi, struttura narrativa, palette, Atlante §8, changelog)
- `MITI_FONDATORI_BREVI_v1.md` — tre miti fondatori (libro 0)
- `GLOSSARIO_ISOLA.md` — catalogo completo dei nomi del mondo
- `RIFERIMENTI_OPERATIVI.md` — scheda secca consultazione veloce per scrittura

**Architettura saga:**
- `ARCHI_12_STORIE_v1.md` — mappa 12 archi narrativi (output Fase B2)
- `PROGETTO_INDICE_v1_5.md` — questo file

**Grafo narrativo (Fase B3 — in costruzione):**
- `story_graph_v0_3_0.json` — **AGGIORNATO in v1.5** — grafo narrativo con S1-S5 complete, 24 seeds, 11 callback registry popolato, schema v0.3.0 post-pulizia B3.0.5. Valida contro schema formale.
- `story_graph.schema.json` — **NUOVO in v1.5** — JSON Schema formale Draft 2020-12. Valida grafo automaticamente via `jsonschema` library. Fonte di verità per campi obbligatori/opzionali, whitelist, referenze.
- `add_story_node.py` v0.2 — script operazioni grafo (whitelist estese, validazione, integrity check)
- `audit_1_integrity.py`, `audit_2_schema.py`, `audit_3_navigability.py`, `audit_4_drift.py` — i 4 audit automatici da rieseguire dopo modifiche
- `migrate_0_2_0_to_0_3_0.py` — script migrazione (riferimento storico)
- `bootstrap_graph.py` — backup architetturale

**Metodologia:**
- `METODO_REVISIONE_B3_v1_1.md` — **AGGIORNATO in v1.5** — descrive il doppio turno di guardia + scarico cognitivo + debt tracking + gestione carico cognitivo. Esteso dopo B3.0.5 e dopo osservazione mal di testa come indicatore di qualità.

**Pipeline produzione (fuori dal progetto di scrittura):**
- Pipeline `automated-picture-book-v2` su Claude Code nativa

### §3.2 File storici (superati)

- `CARTA_VOCE_v1_0.md`, `CARTA_VOCE_v1_1.md` — superati da v1.2
- `ISOLA_TRE_VENTI_BIBLE_v1_0.md`, `ISOLA_TRE_VENTI_BIBLE_v1_1.md` — superati da v2.0
- `VOCE_AUTORE_ESTRATTA_v1_0.md` — superato da v1.1
- `STORIE_SCHEMA_v1_0.md` — superato da v1.1
- `STORIE_SCHEMA_v1_1.md` — **superseded da `ARCHI_12_STORIE_v1.md` per la mappa archi**. Resta come riferimento storico.
- `PROGETTO_INDICE_v1_0.md`, `PROGETTO_INDICE_v1_1.md`, `PROGETTO_INDICE_v1_2.md`, `PROGETTO_INDICE_v1_3.md`, `PROGETTO_INDICE_v1_4.md` — superati da v1.5
- `story_graph.json` (base S1-S3, versione 0.1.0) — superato da `story_graph_v0_3_0.json`
- `story_graph_v0_2_0.json` — superato dopo migrazione B3.0.5
- `METODO_REVISIONE_B3.md` (v1.0) — superato da `METODO_REVISIONE_B3_v1_1.md`
- Pilote AI storie 1, 4, 7 (prima stesura) — da riscrivere in Fase D

### §3.3 File da creare

**Fase B3 (in corso):**
- `story_graph_vX.Y.Z.json` incrementale per ogni chat (S6, S7, ..., S12)
- `QUOTE_TRACKER.md` consolidato alla chiusura di B3 (post-S12)

**Fase C:**
- `SCHEMA_STORIA_01.md` ... `SCHEMA_STORIA_12.md`

**Fase D:**
- Testi 12 storie

**Fase E:**
- File illustrazioni + PDF/EPUB3 via pipeline

**Fase F:**
- Documento di architettura post-saga (forma e contenuti della rivelazione narratore)

---

## §4. DECISIONI ARCHITETTURALI — STORICO CUMULATIVO

### Decisioni 1-10 (Fasi A1-A2)

1. Framework EAR (Δ/⇄/⟳) come architettura invisibile
2. Tre fratelli umani unici umani dell'isola, tutti gli altri animali antropomorfizzati
3. Cosmogonia in due epoche (Mitica + Presente), trasformazione Spiriti in Venti
4. Invisibilità assoluta del framework nel testo
5. Saga 12 storie = 4 cicli da 3 (Δ/⇄/⟳/integrato)
6. Multi-strato di lettura (4 anni / 7-10 anni / strato 3 aperto)
7. Continuità tipo Pokémon (accumulo, conseguenze, evoluzione)
8. Libro 0 separato per i tre Miti Fondatori
9. P6: ogni storia richiede tutti e tre i fratelli
10. Narratore-iniziato come postura (mai spiega, sempre sigilla), rivelazione prevista in Fase F

### Decisioni 11-14 (Fasi A2.5b-c)

11. 16 tratti stilistici estratti dal corpus italiano adulto di Ray, raffinati per la saga
12. Doppio strato → multi-strato (Fase A2.5b)
13. Tabù §3.7: niente preannunci della rivelazione del narratore nelle 12 storie
14. Quote saga per i tratti rari (paronomastico fisico, frase-firma narratore, address al lettore, metanarrazione, memoria lunga narratore)

### Decisioni 15-19 (Fase A3)

15. **Sfasamento stagionale della saga.** Saga = 1 anno completo. I 4 cicli EAR sfasati di una storia rispetto alle stagioni (mandala silenzioso temporale). Vedi `ISOLA_TRE_VENTI_BIBLE_v2.md` §8.7 + `CARTA_VOCE_v1_2.md` §2.9.
16. **La notte come spazio non mitico.** Quarto tempo del giorno, ma non abitato da spirito, non personificato, non quarto vento. Vedi `ISOLA_TRE_VENTI_BIBLE_v2.md` §1.5 + `CARTA_VOCE_v1_2.md` §3.8.
17. **Grunto testimone unico della trasformazione mitica.** Stambecco vecchio verde del Burrone, architrave dello strato 3. Vincoli operativi stretti. Vedi `ISOLA_TRE_VENTI_BIBLE_v2.md` §1.4 + `CARTA_VOCE_v1_2.md` §1.14 + `VOCE_AUTORE_ESTRATTA_v1_1.md` §4.2.
18. **Debito tecnico saggezza-taratura.** Segnalato per revisione finale Fase D/E. Vedi `CARTA_VOCE_v1_2.md` §5.1.
19. **Geografia frattale con cast esteso.** Tre cinture concentriche, quattro quartieri cardinali, ~8×7 km, 19 abitanti + 4 gruppi + 3 fratelli. Vedi `ISOLA_TRE_VENTI_BIBLE_v2.md` §4 + §8 + `GLOSSARIO_ISOLA.md`.

### Decisioni 20-22 (Fase B2)

20. **Pattern A — *Le cose rotte arrivano lo stesso* — riconosciuto come famiglia di immagini ricorrente.** Non un leitmotiv dichiarato (B1 saltata), una continuità sotterranea da onorare nelle chiusure di blocco. Mai nominato nel testo. Prima semina formale **S5** (rami caduti diventano materia), bloom trasversale attraverso la saga, chiusura silente S12. Si lega a *quando l'acqua trema* (Bible §8). Architettura silente del modo in cui la saga risolve senza dichiarare. Vedi `ARCHI_12_STORIE_v1.md` §0.5.

21. **Terna strato 3 architrave saga: *dire / accettare / tenere*.** Le tre paure dei fratelli si risolvono in modi simmetrici per modo del fratello, non per evento. Noah dice (S10), Elias accetta (S11), Gabriel tiene (S12). Modi maturi universali di stare con se stessi. Strato 3 architrave dell'intera saga.

22. **Cornice S1↔S12 al Forno con Fiamma.** Decisione di chiusura saga: la storia 12 chiude la cornice aperta in S1 (Forno, pagnotta a Grunto). I fratelli rientrano al Forno la sera del Concerto, mangiano un dolce normale con Fiamma (quattro fette, una per Fiamma). Gesto delle briciole Gabriel/Noah. Braccialetto S9 al polso di Gabriel (mai descritto). Sigillo del narratore con quattro funzioni (giorno/anno/paura/Fase F). Massima sobrietà. Simmetria coi pochi mezzi.

### Decisioni 23-25 (Fase B3 — NUOVE in v1.4)

23. **Doppio turno di guardia come metodo operativo.** Metodo emerso empiricamente durante S4-S5 e consolidato in `METODO_REVISIONE_B3.md`. Ogni storia passa da due agenti complementari: Claude come agente ontologico (tiene EAR, voce, Pattern A, quote, vincoli), critico esterno come agente fisico (tempi, distanze, luci, acustica, sequenza eventi). Le loro attenzioni si contraddicono parzialmente — Claude tende a giustificare ontologicamente contraddizioni fisiche; il critico, non conoscendo l'ontologia, le trova. Il metodo produce **cristallizzazione senza limitazione**: le correzioni del critico non cambiano cosa succede, cambiano come succede materialmente, e spesso fanno emergere principi impliciti del mondo che l'ontologia non esplicitava. Da applicare a tutta Fase B3 e da estendere a Fase D (prosa). Vedi `METODO_REVISIONE_B3.md` per il ciclo operativo completo (6 turni).

24. **Canale vibrazione vs. aria — principio fisico del mondo.** Emerso in S4 da correzione del critico (contraddizione Rovo-sente/Salvia-non-sente). La Foresta ha due canali percettivi: aria (per voci basse e continue — cantilene; disperde voci corte ad alto volume — grida) e tessuto sotterraneo delle radici (per vibrazioni — battiti, colpi ritmici su legno). Chi ha contatto col tessuto (palmo sulla terra, unghie nell'humus, passo pesante tra radici) percepisce via-tessuto; chi sta solo sopra in superficie (zampe leggere, raccoglitori concentrati) percepisce solo via-aria. Principio istituito in S4, esteso in S5 (TOK-TOK-TOK su legno viaggia in entrambi i canali). Non nominato nel testo, vive nelle azioni e nei gesti. Vedi `story_graph_v0.2.0.json` S4 structural_notes.

25. **Eredità tecnica + materiale come gesto di trasmissione.** Emerso in S5 da correzione del critico (la corda di Nodo che entra nel ponte). Quando un maggiore trasmette a un fratello una capacità (es. Nodo Marinaro a Elias), la trasmissione include spesso anche **un pezzo di materia** dell'artigiano (corda dalla matassa al braccio di Nodo). Il know-how e la materia entrano insieme nel fare dei fratelli. Per ora tracciato implicitamente dentro `seed_nodo_marinaro_capacita_elias` nel campo `materiale_associato`. Se il pattern si conferma in S8 (Nodo-Mantenitore passa altra corda) e S11 (corda intrecciata alla festa), si promuove a seed autonomo nella revisione grafo post-S6. Vedi `story_graph_v0.2.0.json` S5 structural_notes.

### Decisioni 26-28 (B3 parte 2 — NUOVE in v1.5)

26. **Gruppi-istituzioni come sfondo funzionale.** Decisione operativa presa prima di S6. I gruppi-istituzioni (Coltivatori del Cerchio, Mercato del Mezzogiorno, Vecchie del Mercato, Mantenitori, Camminanti, Pescatori del Pontile, Pastori) sono **sfondo costante che può occasionalmente servire la narrazione** — es. un passante del Mercato che porge un oggetto, un Coltivatore che indica una direzione, un Mantenitore che passa una corda. **Mai indipendenti, mai individuati, mai protagonisti di un'azione che richieda giustificazione.** Regola applicabile dal B3 parte 2 in avanti. Vincoli Bible §4 (ogni gruppo-istituzione ha già i suoi constraint individuali) restano validi e sovraordinati.

27. **Vecchie del Mercato come umane — porta socchiusa.** Le Vecchie restano umane per ora (unici umani oltre i tre fratelli). Trattate come **istituzione corale silente** (vincolo Bible §4.19), mai individuate, mai con parole proprie, mai nome individuale. Sono presenza di gruppo che indica in silenzio. Se emerge in scrittura Fase C che la loro umanità crea problemi di coerenza del mondo (difficile giustificare la loro presenza come umane senza raccontare una storia dedicata), si rivaluta — possibile trasformazione in anziane di varie specie animali già presenti (tartarughe vecchie, ricce vecchie, lepri vecchie). Porta socchiusa, decisione rimandabile. Segnata come questione aperta future.

28. **Debt tracking operativo delegato a Claude.** A partire da S6, Claude produce mini-report di debt tracking a fine di ogni storia chiusa, senza che Ray lo chieda. Soglie operative S5-S12 fissate in `METODO_REVISIONE_B3_v1_1.md` §5. Ray riceve un indicatore leading (saldo aperti cumulativo) senza dover monitorare. Se il saldo supera la soglia o il trend è preoccupante, Claude alza bandiera con "Attenzione" e segnala quali bloom attesi devono chiudere nella prossima storia.

### Decisioni future (da prendere in Fase B+)

- Promozione di seed impliciti (corda di Nodo) a seed autonomi — revisione post-S8.
- Uniformazione retroattiva format seed tra chat A (S1-S3) e chat B (S4-S5) — revisione post-S8, quando avremo 8 storie di dati e potremo decidere con evidenza quale format tenere.
- Vecchie del Mercato umane vs animali — decisione rimandabile a Fase C (scrittura prosa) se emerge problema di coerenza.
- Forma esatta della rivelazione del narratore in Fase F.

---

## §5. METODO DI LAVORO

### §5.1 Principi operativi consolidati

- **Una fase = una chat** (con fine aggiustamento: in Fase B3 è *una storia = una chat*, con eccezioni giustificate come S4+S5 insieme).
- **Architettura prima di costruzione.** Si discute e si fissa la struttura prima di scrivere i contenuti.
- **Validazione blocco-per-blocco.** Durante le fasi lunghe, Claude propone output per blocchi e Ray valida prima di passare avanti.
- **Doppio turno di guardia** (decisione 23) — Claude + critico esterno su ogni storia prima della chiusura del nodo-grafo.
- **Scarico cognitivo a inizio chat** (nuovo in v1.5, vedi `METODO_REVISIONE_B3_v1_1.md` §2.1 e §8) — Ray dichiara 2-3 cose in mente, Claude archivia in posto stabile, Ray torna libero per visione d'insieme.
- **Debt tracking delegato** (nuovo in v1.5, decisione 28) — Claude produce mini-report a fine storia, Ray non monitora.
- **File caricati nel progetto sostituendo i vecchi.** Ray aggiorna il progetto sostituendo i file vecchi con le nuove versioni.
- **Multi-strato sempre come criterio.** Ogni decisione di scrittura passa il test: funziona a 4 anni? apre qualcosa a 7-10? lascia porta socchiusa per adulto?
- **Invisibilità come vincolo forte.** Framework e sistema interno di continuità mai visibili al lettore.
- **Schema formale come protezione strutturale** (post-B3.0.5) — ogni modifica al grafo valida contro `story_graph.schema.json`. Il drift di schema è tecnicamente impossibile. Il drift di contenuto è legittimo ma monitorato.

### §5.2 Stile di lavoro di Ray con Claude

- Conciso ma sostanziale
- Prosa + tabelle quando utile
- Preferenze dichiarate esplicitamente
- Validazione prima di produrre
- Realismo geografico/fisico importante anche dove i bambini non noteranno
- Iterazione stretta: una proposta, feedback, correzione, prossimo blocco
- Ruolo di Ray nel doppio turno di guardia: script passante tra Claude e critico (turni 2 e 5); intervento d'autore tra turno 3 e 4 (scelte che richiedono voce di Ray)

### §5.3 Pipeline tecnica separata

La scrittura/validazione narrativa (Fasi A-D) è **un flusso a sé**, che produce file .md canonici e il grafo .json. La pipeline di produzione `automated-picture-book-v2` è **un altro flusso**, che prende il file di una storia validata e genera illustrazioni (BFL FLUX Kontext Pro) + PDF print-ready + EPUB3. I due flussi si incontrano in Fase D (per ogni storia) e si ricongiungono totalmente in Fase E.

### §5.4 Gestione del carico cognitivo (nuovo in v1.5)

La saga al suo stato corrente coinvolge: 16 tratti voce + cast ~25 personaggi + 4 gruppi + 26 luoghi + 3 venti + Pattern A su 8 storie + terna strato 3 + quote saga + mandala silenzioso + schema JSON + grafo 24 seed + 11 callback + framework EAR invisibile. Supera la memoria di lavoro non aiutata. Il sistema di distribuzione del carico (schema formale, audit automatici, JSON Schema validator, critico esterno, Claude) serve esattamente a scaricare la memoria di Ray.

**Mal di testa come indicatore.** Ray ha riconosciuto il mal di testa dopo un'ora di lavoro come segnale che sta tenendo in memoria di lavoro qualcosa che dovrebbe essere in un file, o sta facendo lavoro meccanico delegabile. Regole operative in `METODO_REVISIONE_B3_v1_1.md` §8.

**Principi:**
- Se Ray sente salire il mal di testa, si ferma e chiede *"cosa sto tenendo in memoria che è già scritto?"*.
- Delega a Claude tutto il meccanico: debt tracking, coerenza seed, audit, ricostruzioni timeline, calcoli di saldo.
- Ray tiene la visione (decisioni d'autore, tono, intuizioni, giudizio).
- Check di scarico a inizio chat: 5 minuti per dichiarare cose da non perdere.

Per dettaglio vedi `METODO_REVISIONE_B3_v1_1.md` §8.

---

## §6. CHANGELOG INDICE

### v1.5 (2026-04-22) — post B3.0.5 + riflessione carico cognitivo

- Decisioni 26-28 aggiunte in §4 (gruppi-istituzioni come sfondo funzionale, Vecchie porta socchiusa, debt tracking delegato a Claude)
- §5.1 aggiornato con principi operativi nuovi: scarico cognitivo, debt tracking delegato, schema formale come protezione strutturale
- Nuova §5.4: gestione del carico cognitivo (mal di testa come indicatore, regole di scarico)
- File nuovo aggiunto all'elenco canonico: `METODO_REVISIONE_B3_v1_1.md` (estensione del v1.0 con §5 debt tracking, §8 gestione cognitiva, turno 0 scarico cognitivo)
- `METODO_REVISIONE_B3.md` (v1.0) marcato come superato da v1.1
- Aggiornamento questioni aperte future: gruppi decisione chiusa, uniformazione format seed rimandata a post-S8 (non più post-S6), Vecchie porta socchiusa Fase C, promozione seed impliciti a post-S8
- Riferimento a pacchetto B3.0.5 (story_graph_v0.3.0.json, story_graph.schema.json, audit automatici) come infrastruttura stabile

### v1.4 (2026-04-22) — durante Fase B3 (post S4-S5)

- Fase B3 marcata 🔄 In corso (non più ⏭️ Prossima)
- Stato B3 dettagliato: S1-S5 complete nel grafo, S6 prossima chat, S7-S12 successive
- File nuovi aggiunti all'elenco canonico: `story_graph_v0.2.0.json`, `METODO_REVISIONE_B3.md`
- `story_graph.json` base (v0.1.0 con S1-S3) marcato come superato
- Decisioni 23-25 aggiunte in §4 (doppio turno di guardia, canale vibrazione, eredità tecnica+materiale)
- Questioni aperte del resto di B3 elencate con maggiore dettaglio (S6 nota specifica, S8/S9/S11/S12 note specifiche)
- §5.1 aggiornato: `una fase = una chat` con aggiustamento `una storia = una chat` per B3
- §5.2 aggiornato: ruolo di Ray nel doppio turno di guardia
- Questione aperta aggiunta: gruppi-istituzioni come sfondo vs. attori episodici (valutazione post-S6)

### v1.3 (2026-04-21) — post Fase B2

- Fase B2 marcata ✅ Chiusa
- Fase B1 marcata ⏭️ SALTATA (decisione Ray, motivata)
- Fase B3 marcata ⏭️ Prossima, con questioni aperte da risolvere elencate
- File nuovo aggiunto all'elenco canonico: `ARCHI_12_STORIE_v1.md`
- `STORIE_SCHEMA_v1_1.md` marcato come superseded da `ARCHI_12_STORIE_v1.md` per la mappa archi (resta come riferimento storico)
- Decisioni 20-22 aggiunte in §4 (Pattern A riconosciuto, terna *dire/accettare/tenere*, cornice S1↔S12 al Forno)
- Pre-grafo semi/callback presente in §5 di `ARCHI_12_STORIE_v1.md` come materiale grezzo per B3

### v1.2 (2026-04-21) — post Fase A3

- Fase A3 marcata ✅ Chiusa
- File nuovi aggiunti: `ISOLA_TRE_VENTI_BIBLE_v2.md`, `GLOSSARIO_ISOLA.md`, `RIFERIMENTI_OPERATIVI.md`, `CARTA_VOCE_v1_2.md`, `VOCE_AUTORE_ESTRATTA_v1_1.md`
- Decisioni 15-19 aggiunte in §4

### v1.1 (2026-04-21) — post Fase A2.5b-c

- Fasi A2.5b-c marcate chiuse
- File `VOCE_AUTORE_ESTRATTA_v1_0.md`, `APPENDIX_STYLISTIC_DERIVATION_v1.md`, `CARTA_VOCE_v1_1.md`, `ISOLA_TRE_VENTI_BIBLE_v1_1.md` aggiunti

### v1.0 (2026-01-19) — inizio progetto

Versione iniziale dell'indice. Fase A1 e A2 descritte. Roadmap complessiva tracciata.

---

**FINE PROGETTO INDICE v1.5**
