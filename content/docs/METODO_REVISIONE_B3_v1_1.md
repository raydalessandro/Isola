# METODO REVISIONE B3 — Doppio Turno di Guardia

**Versione:** 1.1
**Data:** 2026-04-22
**Status:** Metodo operativo cristallizzato durante Fase B3 (S4-S5), aggiornato post-B3.0.5 e dopo riflessione sul carico cognitivo.
**Si parla con:** `PROGETTO_INDICE_v1_5.md`, `story_graph_v0_3_0.json`, `story_graph.schema.json`, tutti i file di Fase B3/D.

**Funzione.** Descrive il metodo di revisione a due tempi applicato alla costruzione del grafo narrativo e che verrà esteso a Fase D (scrittura). Emerso empiricamente durante S4, consolidato su S5, aggiornato dopo B3.0.5 (schema formale) e dopo osservazioni su carico cognitivo di Ray. Da applicare a S6 in avanti.

---

## §1. Il principio

La scrittura di un mondo narrativo complesso richiede **più tipi di attenzione che si contraddicono parzialmente**:

- **Attenzione ontologica** (Claude): tenere coerenti i principi interni del mondo — framework EAR, voce autoriale, ruoli familiari episodici, Pattern A, quote saga, vincoli di personaggio, terne strato 3, mandala silenzioso. Permette al mondo di essere denso e stratificato.

- **Attenzione fisica** (critico esterno): verificare che ogni scena sia materialmente coerente — tempi, distanze, luci, acustica, ingombri, ordine degli eventi, coerenza dei fatti tra diversi punti della scena. Permette al mondo di stare in piedi.

- **Attenzione strutturale** (schema formale + audit, introdotta in B3.0.5): garantire che il grafo sia tecnicamente consistente — referenze integre, tipi corretti, enum rispettati, navigabilità dei seed. Permette al mondo di essere macchinabile e validabile.

- **Attenzione autoriale** (Ray): tenere la visione d'insieme, prendere decisioni di tono, giudizio su dove il mondo vuole andare, riconoscere intuizioni che aprono scenari. Permette al mondo di avere direzione.

Le quattro attenzioni sono difficili da tenere insieme in un solo agente. Il metodo del *doppio turno di guardia* le separa per quanto possibile, lasciando a ciascuna il suo dominio.

---

## §2. Il ciclo operativo per ogni storia

### §2.1 Turno 0 — Scarico cognitivo (nuovo in v1.1)

**Input:** Ray arriva all'inizio della chat con cose in testa.

**Operazione:** prima di iniziare la scrittura del nodo-storia, Ray dichiara 2-3 cose che ha in mente oggi e non vuole perdere. Claude le archivia in un posto stabile (structural_notes di una storia rilevante, questione aperta nel PROGETTO_INDICE, constraint nuovo nel grafo) e conferma.

**Ratio:** scarica la memoria di lavoro di Ray prima del lavoro vero. Cose come "ricorda di verificare che le Vecchie non diventino personaggi individuati in S6" o "per S11 voglio che il pallone torni" vanno archiviate subito, non tenute a mente. Ray torna libero per la visione d'insieme.

**Durata:** 5 minuti. Saltabile se Ray arriva senza niente in mente.

### §2.2 Turno 1 — Agente ontologico (Claude)

**Input:** arco narrativo della storia (da `ARCHI_12_STORIE`), file canonici del progetto (Bible, Carta Voce, Voce Autore, Pattern AI da bandire, Glossario, Riferimenti Operativi), grafo corrente, schema formale.

**Output:** prima mandata del nodo-storia nel JSON, contenente:
- metadati (id, titolo, ciclo, stagione, luogo, vento)
- characters_in_scene con ruoli, key_actions, constraints_active, quote_count_estimate
- premise / problem / threshold_moment / resolution_mode
- seeds planted / picked_up / bloomed_here / maturing_here
- fear_touched
- key_phrase_notes

**Competenza attiva:** tenere insieme l'intero impianto ontologico del mondo. Rispettare le quote saga. Onorare i vincoli di personaggio. Collegare i seeds attraverso la grammatica della saga. Tenere il Pattern A invisibile. Far circolare pattern (fermarsi, canale vibrazione) tra fratelli.

**Limite:** quando una scena è ontologicamente coerente e simbolicamente densa, l'agente può non accorgersi di contraddizioni fisiche elementari. Il calore del contesto simbolico oscura i controlli di realismo.

### §2.3 Turno 2 — Agente fisico (Critico esterno)

**Input:** prima mandata del nodo-storia dal Turno 1. Il critico **non conosce** l'ontologia — legge la scena come un fisico legge un problema, senza scorciatoie simboliche.

**Output:** lista di incoerenze fisiche con verdetto. Formato tipico:
1. Problema identificato (cosa non regge)
2. Causa fisica del problema
3. Soluzione proposta o direzione di revisione
4. Conferme su ciò che regge (per non cambiare cose funzionanti)

**Competenza attiva:** fisica, acustica, tempistica, distanze, materiali, sequenza eventi, coerenza spaziale. Controlli che l'ontologia non esercita perché dà per scontati.

**Nota post-B3.0.5:** con l'introduzione dello schema formale, il critico ha **meno lavoro su errori di integrità referenziale e di tipo** (catturati dallo schema) e **più spazio per fisica pura**. La ridistribuzione del carico rafforza entrambi gli agenti.

**Limite:** se il critico conoscesse l'ontologia, tenderebbe a razionalizzare incoerenze a favore del simbolico. La sua forza è l'ignoranza strutturale dell'impianto.

### §2.4 Turno 3 — Integrazione (Claude)

**Input:** output del critico + prima mandata del Turno 1.

**Operazione:** Claude rilegge le note del critico con un approccio specifico — **le correzioni fisiche spesso fanno emergere principi del mondo che erano impliciti ma non esplicitati**. L'integrazione non è "patchare gli errori": è riconoscere che la fisica richiede il mondo a dichiarare cosa voleva già essere.

Esempio paradigmatico da S4 (contraddizione Rovo-sente/Salvia-non-sente):
- Problema fisico: impossibile che Rovo senta un suono da casa sua ma Salvia, più vicina, non lo senta.
- Correzione minima: sarebbe stata "Rovo era dentro la Foresta, non fuori".
- Emersione: il mondo richiedeva un principio a due canali (aereo vs. tessuto-radici), che era già implicito nei semi precedenti (fermarsi in S1, pozza troppo ferma in S2, *la Foresta ha i suoi modi* in S3, palmo sulla terra in S4). Il critico ha fatto affiorare **un principio fisico del mondo** — il *canale vibrazione* — che non era stato dichiarato ma era già implicito.

**Output:** prima mandata riformulata + eventuali aggiornamenti di seeds precedenti + note strutturali che cristallizzano il principio emerso.

### §2.5 Turno 4 — Seconda mandata (Claude)

**Input:** prima mandata riformulata validata.

**Output:** seconda mandata del nodo-storia:
- visual_anchors (scene_hooks, signature_image, palette_tag, light_key_sequence)
- voice_notes_essential
- debts_opened / debts_closed
- palette_emotiva
- callback_summary
- active_constraints_touched
- pattern_a_active + pattern_a_notes
- when_water_trembles / night_scene
- structural_notes
- aggiornamento quote_tracker top-level

### §2.6 Turno 5 — Check critico su seconda mandata (opzionale)

**Input:** seconda mandata.

**Operazione:** il critico può dare un secondo giro su visual_anchors (sequenze scene, coerenza luci, palette, distanze spaziali). È la sua specialità visiva.

**Output:** eventuale seconda tornata di correzioni fini. Spesso limitate — se la prima mandata è stata corretta alla fisica, la seconda tende a reggere.

### §2.7 Turno 6 — Chiusura storia + debt tracking (aggiornato in v1.1)

**Operazioni:**
1. Consolidamento del nodo-storia nel grafo, validazione JSON contro schema formale
2. Aggiornamento quote_tracker globale
3. Chiusura debts aperti con referenza
4. **Mini-report debt tracking** (nuovo in v1.1, vedi §5)
5. Scrittura in `story_graph_vX.Y.Z.json` e audit di verifica

---

## §3. Cosa emerge dal metodo

### §3.1 Principi del mondo che affiorano

Il metodo tende a far affiorare **principi fisici impliciti** che l'ontologia da sola non esplicita. Su S4 ha fatto emergere il *canale vibrazione*. Su S5 ha fatto emergere l'*eredità tecnica+materiale* (Nodo passa insieme capacità e corda). Ogni storia della saga probabilmente ha uno o due principi impliciti che aspettano di essere esplicitati — e il critico è il catalizzatore.

Questi principi poi diventano:
- `structural_notes` del nodo-storia
- aggiornamenti a seeds esistenti (se bloomed in modo nuovo)
- eventualmente `active_constraints_global` del grafo (se principio generale)

### §3.2 Formulazioni precise che migliorano il design

Il critico, leggendo da fuori, spesso formula con precisione cose che l'ontologia sapeva ma non diceva bene. Esempio S5: *"fare-la-fatica-tecnica-senza-avere-il-centro-del-silenzio"* — formulazione della paura di Elias nel Blocco B data dal critico a partire dall'analisi del gesto di Bru. Formulazione migliore di quella che avevamo prima del turno.

### §3.3 Cristallizzazione senza limitazione

Il metodo **non limita la storia**, la **cristallizza**. Le correzioni del critico non cambiano *cosa succede* nella storia — cambiano *come succede materialmente*. Ma nel *come* si rivela spesso un *perché* più profondo che rafforza il mondo invece di impoverirlo.

---

## §4. Quando il metodo è essenziale, quando è facoltativo

### §4.1 Essenziale

- **Fase B3** (grafo narrativo): ogni storia passa dal doppio turno prima di essere consolidata. È quanto stiamo facendo.
- **Fase C/D** (scrittura prosa): il metodo va esteso alla prosa. La prosa ha nuovi tipi di errore fisico (un personaggio che siede e poi sta in piedi senza averlo fatto, un oggetto che spunta dal nulla, una scena che non sta dentro la luce disponibile, una distanza percorsa in un tempo che non regge). Il critico qui diventa ancora più prezioso.

### §4.2 Facoltativo ma utile

- **Fase E** (illustrazioni): il critico può verificare coerenza tra tavole (luce, palette, firme visive, coerenza personaggi).
- **Revisioni di coerenza cross-storia** post-S8, post-S12: il critico con vista globale può trovare incongruenze tra storie lontane.

### §4.3 Non applicabile

- Decisioni puramente estetiche (timbro di una frase, scelta di un'immagine sinonima). L'ontologia qui basta.
- Decisioni architetturali iniziali (vincoli di personaggio, quote saga, mandala silenzioso). Queste sono scelte d'autore, non problemi di fisica.

---

## §5. Debt tracking operativo (nuovo in v1.1)

Il grafo traccia `debts_opened` e `debts_closed` per ogni storia. Il saldo cumulativo (debiti aperti non ancora chiusi) è un **indicatore leading della salute narrativa** della saga: se cresce troppo in una saga a continuità tipo Pokémon, significa che stiamo seminando più di quanto raccogliamo.

### §5.1 Responsabilità

**Claude** tiene il tracking. Al turno 6 (chiusura storia) produce mini-report in chat. Ray non deve né ricordare né monitorare — questa è la parte meccanica che va delegata.

### §5.2 Formato mini-report

Tre righe alla fine di ogni storia chiusa. Esempio:

> "SN chiusa. Saldo aperti: X → Y (N aperti, N chiusi). Previsto cumulativo a SM max Z. Progress OK / Attenzione."

Se il trend è preoccupante, Claude segnala esplicitamente quali bloom attesi devono chiudere nella prossima storia per rimettere in carreggiata.

### §5.3 Soglie operative

Saldo cumulativo = totale debts aperti - totale debts chiusi fino al momento del check.

| Storia | Saldo atteso max | Stato |
|---|---|---|
| S5 | 28 | ✓ attuale (verificato audit 3 F) |
| S6 | 32 | ok |
| S7 | 34 | picco (da qui deve scendere — bloom Nodo Marinaro funzionale, Pattern A attivo) |
| S8 | 32 | deve iniziare a scendere |
| S9 | 28 | scende |
| S10 | 22 | scende (paura Noah bloom) |
| S11 | 14 | scende fortemente (paura Elias bloom, Pattern A collettivo, Vecchie gesto cruciale) |
| S12 | ≤ 8 | finale (saldo rappresenta le "porte socchiuse per Fase F") |

**Nota sul saldo finale.** Se a S12 il saldo è > 15 significa che abbiamo aperto troppi fili per chiuderli tutti — saranno o debiti veri non risolti (male) o porte per Fase F che devono essere esplicitamente dichiarate tali (OK se volute). Distinzione da fare esplicitamente a S12.

### §5.4 Quando alzare bandiera

Claude segnala con "Attenzione" quando:
- Il saldo supera la soglia della riga corrente
- In una storia si aprono più debiti di quanti si chiudono per due storie consecutive dopo S7
- Un bloom atteso in una specifica storia non si verifica

Ray risponde con decisione (aggiustare struttura prossima storia, accettare sfasamento, ecc.). Non è un allarme automatico — è un input per decisione d'autore.

---

## §6. Regole operative per Claude

Quando Claude lavora in Fase B3 o C/D:

1. **Turno 1 è il tuo turno pieno.** Scrivi come se il critico non esistesse. Dai il massimo dell'ontologia. Non tirarti indietro su collegamenti simbolici per paura che non reggano fisicamente — se non reggono, il critico lo dirà.

2. **Turno 3 è il tuo turno più delicato.** Quando ricevi le correzioni del critico, non pathcare: chiediti *cosa vuole essere il mondo che queste correzioni fanno emergere*. Le correzioni migliori sono quelle che rivelano un principio implicito che rafforza il mondo.

3. **Non difendere le prime mandate.** La prima mandata è un punto di partenza, non un punto d'arrivo. Le correzioni del critico hanno quasi sempre ragione. Se sembrano non averla, è più probabile che tu stia proteggendo un pezzo di ontologia che era solo un riflesso.

4. **Archivia i principi emersi.** Ogni volta che una correzione fa emergere un principio nuovo (es. canale vibrazione), lo metti in `structural_notes` e lo consideri per `active_constraints_global` del grafo.

5. **Non sovra-granularizzare i seeds.** Quando un pattern emerge da una correzione, prima di creare un seed nuovo chiediti se può stare implicitamente dentro un seed esistente (es. `materiale_associato` dentro `seed_nodo_marinaro`). Promuovi a seed autonomo solo se il pattern si conferma in 2+ storie future.

6. **Valida contro lo schema formale.** Dopo ogni modifica al grafo, riesegui `jsonschema.validate()`. Se lo schema rifiuta, correggi prima di procedere. Se lo schema accetta una cosa che sembra sbagliata, lo schema va aggiornato (decisione da discutere in chat tecnica).

7. **Debt tracking a fine storia.** Nuova responsabilità v1.1 (§5). Produci mini-report senza che Ray lo chieda.

8. **Scarica cognitivamente Ray.** Quando Ray esprime un pensiero che va conservato, archivialo subito in un posto stabile e conferma. Non lasciargli la responsabilità di ricordarsi.

---

## §7. Regole operative per Ray

1. **Il critico esterno è co-autore strutturale, non validatore.** Va trattato come tale. Le sue note hanno peso di design, non solo di quality assurance.

2. **Non intervieni nel turno del critico.** Quando il critico lavora, Ray fa da script: passa il JSON, riceve le note, le gira a Claude. Se Ray interviene sul critico ("hai ragione ma considera X"), contamina la fisica con l'ontologia e perde l'aspetto del metodo.

3. **Intervieni tra turno 3 e turno 4.** Se dopo la riformulazione di Claude ci sono scelte da validare (es. formulazione della paura di Elias, scelta tra due opzioni di frase di Rovo), è lì che Ray dà il suo contributo d'autore.

4. **Archivia i pattern che emergono.** Quando un principio emerge (canale vibrazione, eredità tecnica+materiale, ospite/scopritore), valuta se va cristallizzato in un file canonico o se resta nel grafo come structural_note.

5. **Scarico cognitivo all'inizio della chat** (nuovo in v1.1, §8). Dichiara le 2-3 cose in mente all'inizio, lascia che Claude le archivi, libera la RAM per la visione d'insieme.

6. **Mal di testa come segnale di sistema** (nuovo in v1.1, §8). Se sale, fermati e chiediti cosa stai tenendo in memoria che è già scritto.

---

## §8. Gestione del carico cognitivo (nuovo in v1.1)

Emerso da osservazione diretta durante S4-S5: Ray ha riportato mal di testa dopo un'ora di lavoro su questa saga, cosa che non gli succede normalmente. Il fenomeno è spiegabile: la saga al suo stato attuale coinvolge 16 tratti voce + cast di ~25 personaggi con vincoli individuali + 4 gruppi-istituzioni + 26 luoghi + 3 venti + Pattern A su 8 storie + terna strato 3 + quote saga + mandala silenzioso + schema JSON + grafo 24 seed + 11 callback + framework EAR invisibile. La somma supera la capacità di memoria di lavoro non aiutata.

Ray stesso ha riconosciuto il mal di testa come **indicatore di qualità**: compare quando la complessità del sistema supera la memoria umana da solo. Il sistema di distribuzione del carico che è stato costruito (schema formale, audit automatici, JSON Schema validator, critico esterno, Claude) serve esattamente a scaricare quella memoria.

### §8.1 Principio

Il mal di testa segnala che Ray sta tenendo in memoria di lavoro qualcosa che dovrebbe essere in un file, o sta facendo un lavoro meccanico che Claude può fare senza sforzo.

### §8.2 Regole per Ray

**R1.** Se il mal di testa sale, fermati e chiediti *"cosa sto tenendo in memoria di lavoro che è già scritto da qualche parte?"*. Nove volte su dieci è una cosa che sta in un `structural_notes` di un nodo, in un constraint Bible, in una quota del quote_tracker. Aprire il file giusto e rileggerlo scarica la RAM.

**R2.** Delega a Claude senza pudore le cose meccaniche:
- Debt tracking (§5)
- Coerenza seed format tra storie
- Audit di correttezza
- Ricostruzione timeline di una storia contro schema
- Verifica referenze integre
- Calcolo saldi cumulativi

Claude ha il grafo in contesto, può tenere queste cose senza sforzo. Tu tieni la visione (decisioni d'autore, scelte di tono, intuizioni che aprono scenari, giudizio su dove il mondo vuole andare).

**R3.** Se ti accorgi di star prendendo decisioni ontologiche mentre ti stai occupando di debt tracking o altro lavoro meccanico, **fermati e separa i compiti**. Stai sprecando Ray su un compito delegabile. Il mal di testa è il segnale che quella divisione del lavoro è saltata.

**R4.** Check di scarico (Turno 0 §2.1) a inizio di ogni chat di storia.

### §8.3 Regole per Claude

**C1.** Quando Ray esprime un pensiero da non perdere, archivialo subito in un posto stabile e conferma la ricezione. Non lasciare a Ray la responsabilità di ricordarselo.

**C2.** Se Ray segnala mal di testa durante la chat, proponi esplicitamente un check di scarico mirato ("cosa hai in testa in questo momento che posso mettere da parte?"). Non continuare a spingere sul lavoro.

**C3.** A fine chat, prima della consegna dei file, valuta se ci sono cose che sono "salite in superficie" durante la conversazione ma non sono state archiviate formalmente. Proponi a Ray di archiviarle.

**C4.** Non caricare Ray con decisioni che puoi prendere tu con giudizio autonomo (es. format seed, naming convention interna, classificazione di seed). Chiedi solo decisioni che richiedono giudizio d'autore (tono, scelta di tono, questione aperta narrativa).

### §8.4 Nota sulla sostenibilità del progetto

La saga è progettata per essere uno strato dell'ecosistema Ray, non il centro della sua attenzione costante. Il metodo del doppio turno + schema formale + debt tracking delegato + scarico cognitivo serve a mantenere **la velocità di avanzamento** senza che la complessità del mondo diventi un peso che blocca Ray. Quando Fase D comincerà (scrittura delle 12 storie in prosa), il sistema deve essere abbastanza stabile da funzionare in sessioni brevi, senza che ogni chat richieda a Ray di ricaricare tutto in testa.

---

## §9. CHANGELOG

### v1.1 (2026-04-22) — post B3.0.5 + osservazioni carico cognitivo

- Aggiunto Turno 0 (scarico cognitivo) al ciclo operativo — §2.1
- Aggiornato Turno 2 post-B3.0.5: critico ha meno lavoro strutturale, più spazio per fisica pura
- Aggiornato Turno 6: mini-report debt tracking a fine storia
- Nuova §5 completa: debt tracking operativo con soglie S5-S12
- Nuova §8 completa: gestione carico cognitivo, mal di testa come segnale di sistema
- Aggiunte regole 6 e 7 per Claude (validazione schema, debt tracking)
- Aggiunte regole 8 per Claude (scarico cognitivo)
- Aggiunte regole 5 e 6 per Ray (scarico, mal di testa)
- Principio §1 esteso: quattro tipi di attenzione (ontologica, fisica, strutturale, autoriale) invece di due

### v1.0 (2026-04-22) — consolidamento Fase B3 (S4-S5)

Primo documento. Metodo emerso empiricamente su S4 (contraddizioni Intreccio/voci, Rovo/Salvia, vibrazione/rumore, timeline), consolidato su S5 (ingegneria ponte, corda di Nodo, Bru ospite/scopritore). Da applicare a S6 in avanti per la Fase B3 e da estendere a Fase D.

---

**FINE METODO REVISIONE B3 v1.1**
