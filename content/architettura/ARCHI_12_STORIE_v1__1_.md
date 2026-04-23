# ARCHI 12 STORIE — L'Isola dei Tre Venti

**Versione:** 1.0
**Data:** 2026-04-21
**Status:** Output Fase B2 — mappa archi narrativi delle 12 storie
**Autore:** EAR Lab + Claude (Fase B2)
**Si parla con:** `PROGETTO_INDICE_v1_3.md`, `ISOLA_TRE_VENTI_BIBLE_v2.md`, `CARTA_VOCE_v1_2.md`, `VOCE_AUTORE_ESTRATTA_v1_1.md`, `PATTERN_AI_DA_BANDIRE_v1.md`, `GLOSSARIO_ISOLA.md`, `RIFERIMENTI_OPERATIVI.md`, `MITI_FONDATORI_BREVI_v1.md`, `STORIE_SCHEMA_v1_1.md` (**superseded** da questo file per la mappa archi)

**Funzione:** Per ogni storia: stagione + ciclo, luogo, vento, premessa, problema, contributo dei tre fratelli, momento-soglia, risoluzione, frase-chiave indicativa, semi piantati e ripresi, paura toccata, abitanti in scena con ruolo familiare episodico, palette emotiva, callback, note voce. **Non è il testo delle storie** — è la mappa architetturale sopra cui in Fase C si costruiscono gli schemi di scrittura, e in Fase D si scrive.

**Cosa NON contiene:** né schemi-pagina (Fase C) né testo (Fase D) né grafo narrativo dettagliato (Fase B3 — prossima chat).

---

## §0. PANORAMICA E DECISIONI ARCHITETTURALI

### §0.1 Tabella maestra delle 12 storie

| # | Titolo provvisorio | Ciclo | Stagione | Luogo principale | Vento | Paura toccata | Maggiori in scena |
|---|---|---|---|---|---|---|---|
| 1 | La Nebbia delle Montagne Gemelle | A — Δ | Inverno | Aria nord — sentiero Montagne | Taglio | (Noah, freddo bianco — implicita) | Fiamma (cammeo) · Grunto (incontro) |
| 2 | Il Riflesso nella Pozza | A — Δ | Inverno | Aria nord — Pascoli Alti, pozza | Taglio | (Elias, "piccolo" — semina) | Stria (cammeo) |
| 3 | Il Pallone oltre la Foresta | A — Δ | Passaggio inverno → primavera | Terra ovest — margine Foresta Intrecciata | (Taglio assente, Mulinello in arrivo) | (Noah, sentore Foresta di sera — implicita) | Rovo · Bru |
| 4 | Le Radici che Parlano | B — ⇄ | Primavera | Terra ovest — Foresta Intrecciata | Intreccio | — | Salvia (cornice) · Rovo (registro diverso da S3) · Bru |
| 5 | Il Ponte di Rami | B — ⇄ | Primavera | Terra ovest — torrente nella Foresta | Intreccio | — | Nodo · Bru |
| 6 | Il Dono per Mèmolo | B — ⇄ | Passaggio primavera → estate | Tutta isola — quattro quartieri | Intreccio dominante (Taglio all'alba, Mulinello al ritorno) | — | Mèmolo · Pun · Stria · Fiamma · Salvia · Zolla · Vecchie · Liù |
| 7 | La Zattera dei Tre Rametti | C — ⟳ | Estate | Acqua sud — Fiume / Pontile / Bocca | Intreccio + Mulinello | (Gabriel, micro-eco) | Bartolo · Toba · Amo (cammeo) |
| 8 | L'Albero che Cadde di Sera | C — ⟳ | Estate | Centro Villaggio | Mulinello (forte) | (Gabriel, micro-eco) | Mèmolo · Nodo · Mantenitori · Liù · Vecchie · Fiamma · Stria (alba dopo) |
| 9 | Quel Pomeriggio di Ottobre | C — ⟳ | Passaggio estate → autunno | Quartiere di Fuoco — Forno + scuola | Mulinello (calmo) | **Gabriel — emerge** | Fiamma · Stria · cuccioli (Pun, Toba, Bru, Cardo, Liù) |
| 10 | La Notte senza Luna | D — ∫ | Autunno | Centro Villaggio + Pontile | Notte ferma → Taglio all'alba | **Noah — risolta** | Bartolo (silenzioso) · Amo (cammeo alba) · Fiamma (cammeo alba) · Grunto (acustico, lontano) |
| 11 | La Festa del Raccolto | D — ∫ | Autunno | Tutta isola — Piazza fulcro | Tutti e tre, sui tempi del giorno | **Elias — risolta** | Vecchie · Stria · Fiamma · Nodo · Mèmolo · Salvia · Zolla · Amo · Bartolo · Bru · Pun · Toba · Cardo (Rovo assente, segnato via Bru) |
| 12 | Quando i Tre Venti Suonano Insieme | D — ∫ | Passaggio autunno → inverno (anno chiuso) | Tutta isola → Roccia Alta → Forno | Tutti e tre (Concerto), poi Mulinello sera | **Gabriel — accolta** (non risolta) | Liù · Fiamma · Bartolo · **Grunto** (1 frammento pre-Vento — unico in saga) |

I titoli sono provvisori. Si limano in Fase D dopo aver scritto.

### §0.2 Distribuzione del cast

Quote rispettate (Bible §4.2: maggiori max 4 storie attive, minori 2-3, cuccioli e gruppi distribuiti).

| Personaggio | Apparizioni significative | Cammei | Tot |
|---|---|---|---|
| **Fiamma** | 1, 6, 9 | 8, 10, 11, 12 | 7 — densità accettata come *amalgama del villaggio* (decisione Ray) |
| **Bartolo** | 7, 10 | 11, 12 | 4 |
| **Rovo** | 3, 4 (registro diverso) | 11 (assenza segnata via Bru) | 3 attive + 1 *segnato* |
| **Stria** | 2, 9, 11 (cornice) | 8 (alba dopo), 12 (assente, Liù lo dice) | 3 attive + 2 cornice/segnati |
| **Mèmolo** | 6, 8 | 11 | 3 |
| **Grunto** | 1, 12 | 10 (acustico, lontano) | 2 attive + 1 acustico — **dentro vincolo** |
| **Salvia** | 4 (cornice), 6 | 11 | 3 |
| **Nodo** | 5, 8, 11 | — | 3 |
| **Amo** | — | 7, 10, 11 | 3 |
| **Zolla** | 11 | 6 | 2 |
| **Pun** | 6 | 9, 11 | 3 |
| **Toba** | 7 | 9, 11 | 3 |
| **Bru** | 3, 4, 5, 11 | — | 4 |
| **Cardo** | — | 9, 11 | 2 |
| **Liù** | 6, 12 | 8, 9 (?), 11 | 4 |

**Coltivatori, Mercato, Mantenitori, Camminanti, Pastori** come sfondo costante: evidenti in 4 (cantilena), 5, 6, 8, 11, e cammei sparsi.

### §0.3 Distribuzione ruoli familiari episodici

Regola Bible: mai stesso adulto due storie di fila nello stesso ruolo familiare.

| # | Madre/calore | Padre pratico | Nonno | Zio/a | Note |
|---|---|---|---|---|---|
| 1 | Fiamma (presenza calda di partenza, non madre piena) | — | — | — | |
| 2 | — | — | — | Stria (maestra-zia) | |
| 3 | — | — | — | Rovo (zio severo) | |
| 4 | Salvia (cornice, madre-pratica) | — | — | Rovo (**guardiano-iniziatore** — registro diverso da S3, risolve "due di fila") | |
| 5 | — | Nodo | — | — | |
| 6 | Salvia (cammeo casa) | — | — | Mèmolo (zio buffo, oggetto del dono); Stria (maestra-zia, cornice scuola) | |
| 7 | — | — | Bartolo | — | |
| 8 | — | Nodo (intervallato da S5 → S6 → S7 — coerente) | — | Mèmolo (frase precisa, registro serio non comico) | |
| 9 | Fiamma (calore per Gabriel — variante distribuita) | — | — | Stria (cornice scuola) | |
| 10 | Fiamma (cammeo all'alba al ritorno) | — | Bartolo (silenzioso notturno) | — | |
| 11 | Vecchie del Mercato (collettive) · Fiamma (banco dolci) | Nodo · Amo (cammeo) | Zolla · Bartolo (sera) | Mèmolo · Stria | tutti — festa |
| 12 | Fiamma (cornice di apertura+chiusura saga, modalità ferma) | — | Bartolo (Pontile passaggio) | Grunto (altro-da-famiglia, sigillo strato 3) | |

### §0.4 Distribuzione momenti rari (collegamento a futuro QUOTE_TRACKER)

| Momento | Quota saga | Storie proposte | Stato |
|---|---|---|---|
| Frammento pre-Vento Grunto | ≤2 | **12** (uno solo, unico in saga) | dentro quota |
| Detti popolari Fiamma chiacchiera | ≤2 per storia con Fiamma chiacchiera | 6 (1 generico Mèmolo) · 9 (1 generico tempo che passa) · 11 (1 generico raccolto) | distribuito |
| Scene notturne | 3-4 in saga | 1 (parziale, notte sui Pascoli prima dell'alba) · 8 (sera Mulinello forte + lanterne crepuscolo) · **10 (notte intera, scena piena)** · 12 (passaggio crepuscolare al ritorno) | 4 totali, dentro quota |
| "Quando l'acqua trema" (fenomeno raro Fiume) | ≤2 in saga | 8 (1ª, annunciata da Liù come ipotesi) · 12 (2ª e ultima, vista al guado nord) | dentro quota |
| Address al lettore | ≤6 in saga | 1 (chiusura blocco A apertura saga) · 4 (chiusura ⇄ in atto) · 7 (apertura blocco C) · 10 (chiusura buio) · 12 (chiusura saga) | 5 — 1 di margine |
| Frase-firma narratore esplicita | ≤2 in saga | **1** (apertura saga) · **12** (chiusura saga) | dentro quota |
| Memoria lunga narratore (incisi) | 1-2 per storia, ~15-20 totali | distribuito su tutte | da tracciare in B3 |
| Paronomastico fisico | ≤2 in saga | 6 (Mèmolo sciarpa annoda/aggroviglia, candidato) · 11 (pomo che rotola, candidato) | dentro quota |
| Cantilene Coltivatori | ≤4-5 in saga | 3 (sommessa, lavori preparazione) · 4 (semina piena, lontana) · 6 (passaggio Orti) · 8 (lavoro Mantenitori sfondo) · 10 (cornice serale "luna nera, terra ferma") | 5, dentro quota |
| TOK-TOK-TOK Nodo | 4-5 storie su 12 | 5 · 6 (cammeo bottega) · 8 (Mantenitori) · 11 (festa) · 12 ([implicito o no, da decidere D]) | 4-5, dentro quota |
| Onomatopee-oggetto cacofoniche | ≤6 in saga (1 per storia max) | 7 (STRAPP) · 8 (CRACK) · resto da decidere D | 2 nelle B2 |

### §0.5 Pattern A riconosciuto — *Le cose rotte arrivano lo stesso*

Pattern emerso in mappa, riconosciuto come famiglia di immagini ricorrente da onorare nelle chiusure di blocco. **Mai nominato nel testo.** Vive nelle scene:

- **Semina:** S6 (la cosa "perduta" non era persa — era nascosta).
- **Prima scena attiva:** S7 (zattera rotta arriva al mare, due rametti su tre).
- **Bloom:** S8 (l'albero caduto diventa legna; nido vuoto curato).
- **Variante notturna:** S10 (il buio era pieno).
- **Variante collettiva:** S11 (festa che non si vince, ciò che è in più dato a chi non aveva, frutti da fuori che arrivano).
- **Chiusura:** S12 (l'anno chiude, i fratelli cresciuti diversi sono ancora insieme).

Si lega all'immagine *quando l'acqua trema* (Bible §8): l'increspatura controcorrente non rompe il flusso. Pattern A è il modo in cui la saga *risolve* senza dichiarare. Architettura silente.

### §0.6 Vincolo Storia 12 (decisione Ray punto 1, blocco 0)

S12 chiude la saga per fascia 4-6 e apre la possibilità di continuazione futura per fascia ragazzi:
- **Strato 1 piena risoluzione** (i fratelli sono al Forno, hanno mangiato, dormiranno).
- **Strato 2 socchiuso** (la paura di Gabriel non è risolta, è accolta).
- **Strato 3 aperto** (frammento Grunto + sigillo narratore + porta verso *oltre il mare*).

Niente preannunci espliciti del futuro fuori-saga (Carta §3.7 e Bible §8.8).

### §0.7 Mismatch principali emendati rispetto a `STORIE_SCHEMA_v1_1.md`

`STORIE_SCHEMA_v1_1.md` resta come traccia storica ma è **superseded** per la mappa archi da questo file. Modifiche apportate:

1. **Storia 2** — "Lago tra Montagne" (inesistente in Atlante) → **pozza ghiacciata sui Pascoli Alti**. Bartolo (incompatibile geograficamente) → **Stria**.
2. **Storia 3** — "Bosco Scuro" (inesistente) → **margine Foresta Intrecciata**. Bru aggiunto.
3. **Storia 7** — Foglia rossa (autunnale, incompatibile con estate) → **zattera di tre rametti**. Bartolo entra nel suo elemento.
4. **Storia 9** — "Giorno del Compleanno" generico → **compleanno di Gabriel** (28 ottobre, mai data esplicita), cornice scuola di Stria, Forno, scena privata casa fratelli.
5. **Storia 11** — "Gara dell'Isola" → **Festa del Raccolto** (autunno, già implicita nel mondo). Niente gara, gesti rituali della festa.
6. **Storia 12** — Concept "Concerto" mantenuto, **chiusura riformulata**: cornice al Forno con Fiamma, gesto delle briciole, sigillo del narratore. Niente dialogo "Siamo come i Venti".
7. **Cast esteso** distribuito (vedi §0.2-0.3).
8. **Stagioni** mappate secondo §8.7 Bible.
9. **Finali dichiarativi** rimossi a livello di arco. Le frasi-chiave puntuali si lavorano in D.

---

## §1. BLOCCO A — Δ DISTINGUERE (storie 1-3, inverno + passaggio)

**Tema emotivo del blocco.** I fratelli imparano a vedere i confini, riconoscere differenze, fermarsi quando non distinguono. Δ all'esterno (nebbia, riflesso, confine della Foresta) e Δ all'interno (chi sono, come si vedono, dove si fermano).

**Atmosfere comuni.** Aria fredda, mattini più tardi, fiati visibili, stivali pesanti, mani in tasca, mantelli di lana. Calore dei luoghi chiusi (Forno) come polo opposto del freddo esterno. Notti lunghe.

---

### STORIA 1 — La Nebbia delle Montagne Gemelle

**Stagione + ciclo.** Inverno pieno. A — Δ.

**Luogo.** Quartiere d'Aria a nord. Sentiero che sale dai Pascoli Alti verso le Montagne Gemelle. Nella seconda parte: cengia presso il Burrone (sopra, non dentro).

**Vento.** Taglio all'alba (atteso). Notte ferma prima — i tre venti dormono.

**Premessa.** I fratelli decidono di salire alle Montagne Gemelle per vedere l'isola dall'alto. Passano dal Forno per scaldarsi. Fiamma li guarda, capisce dove vanno, gli mette in mano una pagnotta: *"Se passate dal Burrone — Grunto. Una sola, eh."* (frase da raffinare in D — direzione: detto popolare en passant ammesso, vincolo §1.13 Carta. Es. *"Più di una se la mangia per dispetto e poi non torna."*). **Niente frase su nebbia che rivela** (decisione Ray blocco 1: tagliata — la nebbia è esperienza dei fratelli, non saggezza anticipata).

**Problema.** Sopra i Pascoli Alti, nebbia di inversione termica li avvolge. Bianco totale. Non vedono più sentiero né montagne. Noah vuole correre. Elias propone di tenersi per mano. Gabriel sente che muoversi è sbagliato — ma non sa spiegare perché.

**Contributo dei tre fratelli.**
- **Gabriel:** si ferma e fa fermare gli altri. Decisione netta nel non-fare.
- **Elias:** tiene la mano di Noah, propone di stare nel poco spazio sicuro che vedono.
- **Noah:** dopo aver litigato si stringe ai fratelli senza dirlo. **Tiene un bastoncino raccolto in cammino** (citato **una sola volta en passant**, mai annunciato come oggetto — "ci si appoggiava un po' come fanno i grandi" o simile; decisione Ray blocco 1).

**Momento-soglia.** Gabriel dice *"No. Non muoverci"* e i fratelli si siedono. Decisione contraria all'istinto. Vento Taglio arriva poco dopo, la nebbia si apre, e davanti a loro — due passi — c'è il bordo del Burrone.

**Risoluzione.** Riprendono il sentiero (a sinistra). Salgono. Trovano la cengia di Grunto. **Incontro vero** (decisione Ray): Grunto *grunt*, batte uno zoccolo, manda via. Loro restano. Lui smette di guardarli (permesso). Gabriel posa la pagnotta su una pietra piatta. Grunto la annusa. Una parola sola: *"Buono."* I fratelli scendono prima che faccia buio. Tornano al Forno. Fiamma non chiede com'è andata.

**Frase-chiave indicativa.** Direzione: **immagine che sigilla, non regola.** Sigillo del narratore in chiusura (non di Fiamma). Nessuna frase-chiave dichiarativa. Da scrivere in D.

**Semi piantati.**
- Noah disagio per il bianco totale → prepara paura del buio (S10).
- **Bastoncino di Noah** raccolto in cammino → torna in S2 (cade nella pozza).
- **Pagnotta a Grunto** → istituisce piccolo rituale ricorrente (Fiamma sa che Grunto c'è, si ricorda di lui senza dirglielo, da prima dei fratelli). Strato 3 silenzioso.
- **Prima apparizione Grunto** come incontro vero, una sola parola — **zero frammenti pre-Vento.** Apre la porta a S12.
- *"Due passi dal burrone"* → micro-eco quando in S12 i fratelli passeranno di nuovo lassù (cresciuti, lo sapranno senza vederlo).
- **Gabriel sa la strada anche senza vedere** → Δ del personaggio, trasferito al buio in S10.

**Paura toccata.** Noah, implicita.

**Abitanti in scena.**
- **Fiamma** (Forno, mattina presto). Modalità chiacchiera, en passant. Detto popolare ammesso. Ruolo familiare: presenza calda di partenza.
- **Grunto** (cengia, Burrone). Una parola sola. Ruolo: altro-da-famiglia.

**Palette emotiva.** Bianco-grigio-azzurro freddo della nebbia → al diradarsi, oro pallido invernale del primo sole sui Pascoli + verde scuro del muschio nelle pietre + pelo verde di Grunto che si confonde col lichene. Caldo del Forno all'andata e al ritorno (cornice).

**Callback.** Nessuno (è la prima).

**Note voce.** Apertura saga = **una delle ≤2 frasi-firma narratore esplicite** (Carta §1.7). **Address al lettore** in chiusura (1 di ≤6 saga). Memoria lunga del narratore: 1-2 incisi (nebbia di alta quota / Burrone). Una scena notturna parziale (notte sui Pascoli prima dell'alba).

---

### STORIA 2 — Il Riflesso nella Pozza

**Stagione + ciclo.** Inverno pieno. A — Δ.

**Luogo.** Quartiere d'Aria a nord. Pascoli Alti — pozza piccola che d'estate è abbeveratoio per le capre dei Pastori, ora ghiacciata, con il velo di superficie appena sgelato da una giornata di sole.

**Vento.** Taglio (alba) — alla fine, una folata che increspa il velo d'acqua.

**Premessa.** **Stria** affida ai fratelli un messaggio per i Pastori sui Pascoli Alti — quel mattino lei vola altrove. *"Tu cosa pensi?"* — chiede a Gabriel quando lui le domanda dove stia andando. Vola via senza spiegare. Loro salgono.

**Problema.** A metà cammino trovano la pozza scoperta. Si chinano a bere. Vedono i loro riflessi — diversi da come si vedono loro. Gabriel si vede con la bocca tirata. Elias si vede **piccolo** — molto piccolo, tra i fratelli che nello specchio risultano più grandi di quanto siano. Noah si vede fermo (e lui non è mai fermo). Litigano: *"Tu non sei così!"* — *"E tu allora?"*. Elias resta zitto. Tocca l'acqua col dito, ritrae la mano.

**Contributo dei tre fratelli.**
- **Noah:** tira fuori il **bastoncino raccolto in S1** (callback) e lo getta nell'acqua per rabbia — gesto irriflesso. L'acqua si increspa, i riflessi tremolano.
- **Gabriel:** capisce per primo che il riflesso non è loro. Lo dice piano, una frase semplice — direzione, non parole esatte: *quello che vedi nello specchio è solo come ti guardi adesso. Non chi sei.*
- **Elias:** alza gli occhi dal riflesso, guarda Noah e Gabriel sulla riva. Mormora *"Voi siete grandi davvero."* Gabriel: *"E tu?"*. Elias non risponde. Poi: *"Andiamo."*

**Momento-soglia.** Il bastoncino di Noah nell'acqua. Gesto irriflesso che diventa rottura della falsa fissità. Il riflesso non era la verità — era una versione, fissata da un'acqua troppo ferma.

**Risoluzione.** Il bastoncino galleggia un attimo, si inclina, sparisce sotto. **Resta congelato dentro il velo che si richiude al calare del sole** — meccanica del mondo, **mai dichiarata nel testo** (decisione Ray blocco 1). Oggetto-fantasma per il rilettore. I fratelli si rialzano, riprendono il cammino verso i Pastori.

**Messaggio per i Pastori.** Da decidere in B3 (grafo): consegna off-screen breve dopo la pozza, **oppure** non-consegna esplicita con conseguenze in storia futura (Stria che ne accenna). Per ora aperto.

**Frase-chiave indicativa.** Direzione: rifiuto della falsa fissità senza dichiararla. Da affidare al narratore in chiusura, non a un personaggio. Da scrivere in D.

**Semi piantati.**
- **Elias che si vede piccolo** → seme forte della sua paura, da bloomare in S11.
- **Bastoncino di Noah** (callback S1) congelato nella pozza = oggetto-fantasma.
- Acqua + Vento Taglio → primissima eco fisica del Pattern A (l'increspatura non rompe il flusso).
- **Gesto-firma di Noah dei bastoncini** istituito (può tornare en passant in altre storie, mai stesso bastoncino).

**Paura toccata.** **Elias** — semina ("piccolo").

**Abitanti in scena.**
- **Stria**, cammeo a inizio storia. Una frase: *"Tu cosa pensi?"*. Ruolo familiare: maestra-zia.
- **Pastori** in lontananza (sfondo, non nominati uno per uno).

**Palette emotiva.** Blu profondo dell'acqua sotto il ghiaccio + bianco del velo + grigio pietra dei Pascoli. Quando il vento increspa: cerchi argentei. I riflessi un filo *più scuri, più rigidi* (eredita schema v1.1 App. C).

**Callback.** Bastoncino di Noah dalla S1. Stria istituita.

**Note voce.** Una scena di silenzio lungo dei tre fratelli (Carta — usata con misura). Memoria lunga del narratore: 1 inciso sulla pozza dei Pastori. Nessun address al lettore (è in S1 e arriverà in S4).

---

### STORIA 3 — Il Pallone oltre la Foresta

**Stagione + ciclo.** Passaggio inverno → primavera. A — Δ.

**Luogo.** Quartiere di Terra a ovest. Margine della Foresta Intrecciata, sul confine tra Orti del Cerchio e Foresta. Tardo pomeriggio → sera (Mulinello sta per iniziare, sole basso).

**Vento.** Taglio assente (è sera). La sua assenza si sente. Mulinello in arrivo, ancora silenzioso.

**Premessa.** I fratelli giocano col pallone (di stoffa cucita) ai margini degli Orti, nel tratto dove gli alberi della Foresta cominciano a infittirsi. **I Coltivatori chiudono il lavoro lontano (cantilena sommessa, lavori di preparazione, non semina** — decisione Ray blocco 1: non sovrapporre a quella piena di S4). Si fa tardi.

**Problema.** Un calcio mal misurato di Noah: il pallone rotola dentro la Foresta, scompare tra i tronchi. È quasi sera. Tutti sanno (per tradizione orale, nessuno spiega) che nella Foresta di sera non si entra. Noah vuole andare. Gabriel dice no. Elias indeciso.

**Contributo dei tre fratelli.**
- **Noah:** fa due passi dentro la Foresta, si ferma — la sera nella Foresta è davvero diversa dal margine. Torna indietro senza dirlo. Resta arrabbiato.
- **Gabriel:** blocca Noah ma non sa spiegare perché non si entra. Sente solo che non si fa.
- **Elias:** trova un modo terzo — chiamare nel buio della Foresta. Forse qualcuno c'è.

**Momento-soglia.** Elias che chiama nel buio: *"C'è nessuno?"*. Una voce risponde da dentro, brusca: *"Chi è?"*. È **Rovo**. Modo diverso di affrontare il limite — non oltrepassarlo, non stare fermi davanti.

**Risoluzione.** Rovo esce dalla Foresta col pallone in mano. **Lo posa per terra a un passo dal margine, dalla parte degli Orti — non lo lancia** (decisione Ray blocco 1: lanciare sarebbe gesto da zio bonario, Rovo non lo è). Brontola: *"Cosa fate qua a quest'ora? È buio. Andate."* **Bru** appare un attimo dietro Rovo, occhi che brillano, poi si ritira. Gabriel chiede perché non si entra di sera. Rovo non risponde subito. Poi, mentre già si volta: *"Le cose della Foresta hanno il loro orario."* Rientra. Bru lo segue.

**Frase-chiave indicativa.** *"Le cose della Foresta hanno il loro orario."* — affidata a Rovo, breve, embedded en passant. Tiene perché è pratica, non filosofia.

**Semi piantati.**
- **Bru** intravisto → prima sua apparizione, prepara presenza in S4-S5.
- **Rovo** che protegge senza ammetterlo → bloomerà in S4 (registro diverso, abitante-Foresta non guardiano-confine).
- **Pallone di stoffa cucita** = oggetto che torna in S11 (festa).
- **Foresta come luogo che ha tempi propri** → prepara la rete delle radici di S4.
- **Cantilena dei Coltivatori** sommessa al chiudere della giornata → **prima cantilena** (1 di ≤4-5 in saga).

**Paura toccata.** Noah — il buio della Foresta di sera. Variante geografica del buio puro (S10). Implicita.

**Abitanti in scena.**
- **Rovo**, modalità ferma e brusca. Una frase di sigillo. Ruolo familiare: zio severo.
- **Bru** intravisto, mai una frase. Ruolo: presenza silenziosa.
- **Coltivatori** in lontananza, voci che cantano a metà mentre rientrano.

**Palette emotiva.** Verde scuro/marrone della Foresta. Tardo pomeriggio: dorato → arancione → blu sera. Pallone color brace = unico punto caldo. Aria un filo più tiepida del solito di gennaio — primo segnale di passaggio.

**Callback.** Eco strutturale di S1 (il *fermarsi* prima del buio è eco del *fermarsi* nella nebbia — chiusura del ciclo Δ).

**Note voce.** Nessun address al lettore. Memoria lunga del narratore: 1-2 incisi sul margine Foresta come luogo di soglia. Cantilena Coltivatori sommessa, in lontananza.

---

## §2. BLOCCO B — ⇄ CONNETTERE (storie 4-6, primavera + passaggio)

**Tema emotivo del blocco.** I fratelli imparano a costruire e percepire connessioni — quelle invisibili (radici), quelle che si fanno (ponte), quelle che si tessono attraverso l'isola intera (rete di abitanti). ⇄ all'esterno (Foresta connessa, ponte costruito, isola attraversata) e ⇄ all'interno (Elias emerge come ponte tra fratelli, comincia a sentire il peso di "stare in mezzo").

**Atmosfere comuni.** Aria che si scalda. Foglie nuove. Erbe nuove (Salvia in attività piena). Coltivatori in semina, cantilene piene. Fiume più alto per scioglimento. Foresta che si riempie di rumori — uccelli, insetti. Sole più alto, ombre più nette a mezzogiorno.

**Nota architetturale del blocco — Elias ridistribuito.** Decisione Ray blocco 2: Elias **non è "quello delle idee"**. Tradirebbe il Tratto 7 (astrazione incarnata) e renderebbe la sua paura una constatazione invece di una sproporzione. Elias incarna ⇄ in azioni *fisiche* di tenuta, responsabilità, sensibilità relazionale. La sua paura va seminata nei micro-sguardi, mai nei ruoli. Una micro-occhiata per blocco. Mai nominata.

---

### STORIA 4 — Le Radici che Parlano

**Stagione + ciclo.** Primavera piena. B — ⇄.

**Luogo.** Quartiere di Terra a ovest. Margine + interno della Foresta Intrecciata. Mattina e mezzogiorno (Vento Intreccio).

**Vento.** Intreccio (giorno) — porta voci, attraversa le chiome, scuote le radici dalla parte che si vede.

**Premessa.** **Salvia** chiede ai fratelli di accompagnarla nella Foresta — primavera piena, deve raccogliere foglie nuove di **ortica giovane**. **Salvia entra solo per qualche metro al margine** (decisione Ray blocco 2: l'ortica giovane cresce ai margini, non nel cuore — coerenza Bible §4.9). Dice ai fratelli di restare ancora più fuori, vicino agli Orti. *"Voi qua. Torno presto."* In lontananza, **cantilena piena della semina** (bloomata da quella sommessa di S3).

**Problema.** Noah vede una **farfalla blu**. La segue di qualche passo. Poi qualche altro. **Va in profondità oltre la zona di lavoro di Salvia.** La farfalla sparisce. Noah è solo. Alberi tutti uguali. Gabriel ed Elias si accorgono dopo qualche minuto che Noah non c'è. Gridano. La Foresta inghiotte le voci. Gridare non funziona.

**Contributo dei tre fratelli.**
- **Noah:** si siede tra le radici di un grande albero. **Non piange — si ferma da solo** (decisione Ray blocco 2: Pokémon attivo. Ha attraversato il margine al buio in S3, qui *applica*). Tocca le radici col palmo — gesto suo, irriflesso. Le sente vibrare. Quando sente sotto la terra il TUM-tum-TUM, **risponde col palmo, attivamente. Quando sente Gabriel arrivare, batte più piano per non confonderlo.**
- **Gabriel:** dopo aver gridato senza risposta, dice *"Gridiamo no. Pensiamo."* (eco diretta del *"Aspettiamo"* di S1, applicato a problema diverso). **Cammina nella direzione del battito di Noah** — è movimento.
- **Elias:** si inginocchia, trova una radice grossa che esce dalla terra, **comincia a battere il ritmo che solo loro tre sanno** — TUM-tum-TUM-tum-TUM — **la loro canzone**, non spiegata. **Resta fermo a battere come ancora.** Tenuta fisica del battito = ⇄ in azione, faticoso, non solo idea (correzione Ray).

**Momento-soglia.** Doppio battito che si incontra. I tre hanno ruoli simultanei e fisici: **Elias è ancora, Noah è risposta, Gabriel è movimento**.

**Risoluzione.** Si ritrovano. Quando arrivano insieme nello stesso punto, **Bru** è lì — appoggiato a un tronco, occhi neri, non sembra sorpreso. Probabilmente ha seguito il movimento. Arriva **Rovo** poco dopo, brontolando: *"Si sente da fuori che battete. Avete fatto rumore di qua a Casa Salvia."* Non aiuta, non ha aiutato — è venuto a vedere chi disturbava. Bru sa già cosa è successo. Quando i fratelli tornano al margine, Salvia sta uscendo col cesto pieno di ortica giovane — non si è accorta di nulla. *"Pronti? Andiamo."*

**Frase-chiave indicativa.** Direzione: il narratore in chiusura sigilla con immagine, non con regola. Niente *"Nella Foresta se tocchi una radice tutti gli alberi sentono"* (frase pilota cancellata). Direzione: *quello che hanno trovato non era il sentiero — era un modo*.

**Semi ripresi dal blocco A.**
- **Rovo** (S3) → bloomato in registro coerente (entra brontolando, dà informazione affidabile data male, se ne va). Vive davvero in quella Foresta — S3 non era apparizione episodica.
- **Bru intravisto** (S3) → ora ha presenza concreta ma resta minimale (vincolo Bible §4.15).
- *"La Foresta ha i suoi tempi"* di Rovo (S3) → bloomato come *"la Foresta ha anche i suoi modi"*.
- **Cantilena Coltivatori** sommessa (S3) → bloomata in cantilena piena di semina.
- **Fermarsi quando non sai dove andare** (S1, Gabriel) → bloomato da Noah (S4) in modo autonomo. Pattern del fermarsi trasferito da fratello a fratello — eco della crescita.

**Semi piantati per blocchi C-D.**
- **TUM-tum-TUM-tum-TUM** istituito come **ritmo identitario dei tre** — patrimonio che torna in S12 (gesto delle mani sulla terra come eco silenziosa).
- **Bru** sviluppato — pronto per S5 con presenza piena.
- **Ortica giovane di primavera** nominata da Salvia — pianta calendario stagionale (vincolo Salvia rispettato: 1 per apparizione).
- **Micro-sguardo di Elias** seminato implicitamente: lui propone il ritmo, ma anche se tiene fisico, una piccolissima cosa storta dentro che non ha parole quando i fratelli si abbracciano per la riuscita. Mai nominato.

**Paura toccata.** Elias — micro-seme.

**Abitanti in scena.**
- **Salvia**, modalità lavoro — entra/esce, breve. Pianta nominata: ortica giovane. Ruolo familiare: madre-pratica (cornice).
- **Rovo**, registro confermato (zio severo) ma diverso da S3: **abitante della Foresta che sente il rumore di casa propria**, non guardiano del confine.
- **Bru**, presenza minima ma reale. Postura, no parole.
- **Coltivatori** in lontananza, semina in cantilena piena.

**Palette emotiva.** Verdi nuovi tenerissimi delle foglie di primavera + marrone scuro umido delle radici + grigio-marrone di Rovo + sabbia chiara di Salvia + cesto di ortica verde scuro. Farfalla di Noah: blu (singolo punto cromatico isolato che poi sparisce).

**Callback.**
- A S1: *fermarsi* come gesto attivo (trasferito da Gabriel a Noah; *"pensiamo"* di Gabriel erede del *"aspettiamo"*).
- A S3: Rovo, Bru, cantilena Coltivatori (passaggio→piena).

**Note voce.** **Address al lettore** in chiusura (1 di ≤6, eredita schema). Memoria lunga del narratore: 1-2 incisi sulla Foresta come tessuto vivo (mai detta come tessuto — questa è meta, non testo). TUM-tum-TUM in onomatopea, isolato graficamente. Cantilena in lontananza, parole spezzate.

---

### STORIA 5 — Il Ponte di Rami

**Stagione + ciclo.** Primavera piena (più tarda di S4 — fiori già aperti, Fiume più alto). B — ⇄.

**Luogo.** Quartiere di Terra a ovest. Un torrente che attraversa la Foresta Intrecciata e finisce nel Fiume che Gira — affluente. La piena primaverile ha portato via il vecchio passaggio (un tronco caduto da tempo che faceva da ponte).

**Vento.** Intreccio (giorno) — soffia tra le chiome, fa muovere i rami che dovranno essere intrecciati per il ponte. Eco silenziosa nome=cosa: Vento Intreccio + ponte che intreccia. Mai detto.

**Premessa.** I fratelli vogliono andare a vedere una **radura nuova** che Bru gli ha indicato (callback diretto a S4: Bru ha mostrato col mento la direzione mentre tornavano col cesto di Salvia). Chiamano Bru. Vanno insieme. Arrivano al torrente: il tronco-ponte non c'è più. L'acqua è alta, corre. Non si guada.

**Problema.** L'altra sponda è lì, a quattro-cinque metri. Tornare = rinunciare. Cercare un altro punto = ore. Stanno già pensando di rinunciare quando sentono **TOK-TOK-TOK** poco distante. È **Nodo**, sta riparando una **scaletta dei Coltivatori** (Nodo-artigiano, cliente: Coltivatori — distinto da Nodo-Mantenitore di S8). Vanno da lui.

**Contributo dei tre fratelli.**
- **Gabriel:** chiede a Nodo se può aiutarli. Nodo non risponde subito (continua a lavorare). Quando finisce il giro di nodo, alza la testa, *"Cosa vi serve."* — non come domanda, come constatazione. Gabriel spiega.
- **Elias:** ha l'idea — usare i rami caduti più grossi del bosco. Propone a Nodo. Nodo annuisce.
- **Noah:** corre a cercare i rami — si entusiasma, tira via Bru, raccoglie più rami di quanti ne serva, alcuni troppo piccoli, alcuni troppo grossi. Bru sceglie quelli giusti silenziosamente.

**Costruzione.** Nodo non costruisce per loro. Mostra **un nodo solo** — il **Marinaro** (Bible §4.10). Lo fa una volta. *"Adesso fai tu."* Tocca a **Elias** rifarlo. Sbaglia due volte, riesce alla terza. Gabriel tiene fermi i rami. Noah passa la corda. Bru segna in silenzio. Costruiscono. Il TOK-TOK-TOK di Nodo nel frattempo è ripreso, su altra cosa.

**Momento-soglia.** Quando il ponte è finito, Nodo non lo collauda. *"È vostro. Provatelo voi."* Si rimette al lavoro. **Elias passa per primo** (correzione Ray blocco 2: chi ha legato il nodo lo collauda. Gesto di responsabilità, non di ricompensa). Noah passa per secondo (più leggero). Gabriel passa per terzo (più pesante, conferma finale). Bru passa per quarto, ospite. **La sequenza crea ombra di tensione** (regge? regge?) **risolta sul terzo passaggio.** Il ponte regge.

**Risoluzione.** Trovano la radura dall'altra parte. Non è niente di speciale a guardarla — un cerchio d'erba con qualche pino intorno, la luce che cala dall'alto in modo verticale (decisione Ray blocco 2: **non specificare il numero degli alberi nel testo** — l'illustrazione può metterne tre, il testo no). Bru si siede al centro per primo. Loro fanno lo stesso. Restano un po', senza parole. Tornano. Al ritorno il ponte è ancora lì. Nodo se n'è già andato col suo TOK-TOK-TOK lontano nella Foresta.

**Frase-chiave indicativa.** Direzione: chiusura del narratore sull'idea che *non hanno trovato qualcosa, hanno fatto qualcosa che resta*. Mai dichiarato.

**Semi ripresi.**
- **Bru** (S3, S4) → ora compagno attivo di una scoperta. Resta minimale a parole, ma ha agency narrativa (indica la radura, sceglie i rami giusti, passa per quarto).
- **Foresta come tessuto** (S4) → ora estesa: la Foresta nasconde radure che si raggiungono solo se costruisci.
- **TOK-TOK-TOK di Nodo** (prima volta in saga, 1ª di ≤4-5 storie).

**Semi piantati per blocchi C-D.**
- **Il nodo Marinaro** insegnato da Nodo a Elias → eredità tecnica che Elias userà in **S7** (zattera), **S8** (legare albero), **S11** (festa). Elias diventa "quello che sa fare un nodo".
- **La radura coi pini** → luogo silenzioso del mondo, **callback in S12** (passaggio finale verso Roccia Alta).
- **Bru sa indicare luoghi che gli altri non vedono** → seme leggero.
- **Elias collauda per primo** = istituzione del modo di Elias (responsabilità di chi ha fatto). Da onorare in S8.

**Paura toccata.** Elias — micro-sguardo possibile (es. quando Bru si siede al centro della radura per primo, gesto silenzioso che il bambino di 4 non legge ma il rilettore vede). Mai nominato.

**Abitanti in scena.**
- **Nodo**, modalità lavoro (artigiano per Coltivatori, **non** Mantenitore qui — distinguere da S8). Mostra un nodo, una volta. *"Adesso fai tu."* Non collauda. Ruolo familiare: padre-pratico (intervallato bene da Rovo zio severo S3-S4).
- **Bru**, presenza piena ma silenziosa (vincolo: mai centro).

**Palette emotiva.** Verdi pieni della Foresta primaverile + marrone dei rami caduti + corda chiara di Nodo + cresta rossa di Nodo come unico punto vivo + grigio-marrone di Bru. Radura: verde quasi giallo nella luce verticale, tronchi scuri di pino.

**Callback.**
- A S4: Bru, Foresta, modo di affrontarla (battere/costruire).
- A S1: il fermarsi è già *fatto*, qui si fa qualcosa. Il blocco B costruisce sul blocco A.

**Note voce.** TOK-TOK-TOK di Nodo come onomatopea isolata graficamente. Memoria lunga del narratore: 1 inciso sui rami che cadono in inverno e diventano materia in primavera (Pattern A in semina). Nessun address al lettore (è in S4 e arriverà in S7).

---

### STORIA 6 — Il Dono per Mèmolo

**Stagione + ciclo.** Passaggio primavera → estate. Prime giornate calde, sole più alto, finestre che si aprono. B — ⇄ (storia di chiusura del blocco — la connessione come *cura della rete*).

**Luogo.** **Tutta isola** — quattro quartieri attraversati. Apertura e chiusura al centro Villaggio (Piazza con Albero Vecchio).

**Vento.** Intreccio dominante (giorno). All'alba Taglio per la partenza, alla sera il ritorno è col Mulinello.

**Premessa.** Mèmolo è triste. Non lo dice. Si vede da come trotterella più piano del solito, dalla sciarpa che sistema mille volte ma non con la solita allegria. **Pun**, suo figlio, lo nota. Lo dice ai fratelli a scuola. *"Papà ha perso una cosa. Non si ricorda dove."* **Stria**, dalla cattedra, sente. Non interviene. Una sola frase: *"E quale cosa?"*. Pun: *"Non lo sa. Ma è una cosa importante."* Stria torna alla lezione. I fratelli si guardano.

**Problema.** Aiutare Mèmolo a ritrovare l'oggetto. Ma Mèmolo non sa cosa ha perso e dove. Chiedergli direttamente è inutile. Bisogna **ricostruire la sua giornata** chiedendo agli abitanti dove l'hanno visto.

**Contributo dei tre fratelli.**
- **Elias:** ha l'idea. *"Possiamo chiedere a chi l'ha visto."* Disegna mentalmente il giro: est (Forno), sud (Pontile), ovest (Orti), nord (Pascoli — *no, troppo lontano per Mèmolo*). Resta: est, ovest, centro.
- **Gabriel:** traccia il giro, decide l'ordine — partire dal Forno, poi Orti, poi tornare al centro.
- **Noah:** ha l'energia di correre da un quartiere all'altro. Lo fa. **Raccoglie un bastoncino lungo la strada per il Pontile e poi un altro tornando dagli Orti** — gesto-firma piccolo en passant (li tiene in mano, distratto, li butta dopo, ne raccoglie altri). **Primo uso del gesto-firma** in modalità *"Noah cammina e raccoglie"*.

**Il giro.**
- **Forno (Quartiere di Fuoco — est).** Fiamma, modalità chiacchiera. *"Sì sì lo so, è venuto stamattina, cornetto e sciarpa annodata male, parlava di una scatoletta. Diceva che la portava dalla parte di Salvia."* **Detto popolare en passant ammesso, da riformulare in D in modo generico sul carattere di Mèmolo, NON anticipazione della trama presente** (correzione Ray blocco 2: la versione *"riccio che parla di scatoletta poi la dimentica al primo cespuglio"* anticipava la trama. Direzione: detto su Mèmolo come tipo, qualcosa tipo *"riccio che pensa con la sciarpa storta, pensiero gli scappa di tasca"* — da raffinare in D). Fiamma offre cornetti caldi. Noah ne intasca due, dà uno a Bru se lo vede.
- **Casa di Salvia (Quartiere di Terra — ovest).** Salvia ferma, mano breve. *"Sì, è venuto, gli ho dato un sacchettino di **tiglio** — testa pesante. Non aveva scatoletta in mano quando è andato via — l'aveva in mano quando è arrivato? Non ricordo. Aveva la sciarpa storta."* Pianta nominata: tiglio (1 per apparizione, vincolo rispettato).
- **Casa di Zolla (Quartiere di Terra — ovest, vicino).** Zolla, fuori a controllare una dispensa. *"Mèmolo è passato di qua, voleva due ghiande dell'anno scorso per qualcosa. Gliele ho date. La scatoletta? Non l'ho vista. Aveva qualcosa in tasca, forse."*
- **Mercato del Mezzogiorno (centro Villaggio).** **Vecchie del Mercato sulla Panca di Pietra.** Una alza un dito senza dire una parola — **indica un cespuglio dietro l'Albero Vecchio.** Le altre annuiscono. Non dicono altro (mai individuate, vincolo §4.19). **Firma gestuale istituita: *indicare in silenzio* — torna in S8 e S11.**

**Momento-soglia.** I fratelli vanno al cespuglio. **Pun** arriva di corsa — ha sentito da **Liù** (cammeo: Liù appare un attimo, *frrr*, *"Indovina chi vi cerca"*, riparte). **Elias trova insieme a Pun** (correzione Ray blocco 2: non Pun da solo). Pun apre la scatoletta, Elias guarda. **Elias vede che è un dente da latte** (di un cucciolo qualsiasi, non riconosce che è di Pun). **Pun lo riconosce.** Pun lo dice piano: *"È mio. L'avevo perso anni fa."* **Elias non dice niente, capisce, restituisce la scatoletta a Pun.** Pun la porta al padre. *"Capire e tirarsi indietro"* = ⇄ vero, sensibilità relazionale muta.

**Risoluzione.** Tornano a casa di Mèmolo coi quattro insieme. Mèmolo è in cortile, sciarpa di sbieco. **Pun gli mette in mano la scatoletta.** Mèmolo la apre, vede il dente, ride — un riso di sollievo che è anche un po' commosso, ma Mèmolo non dice perché. *"Aspetta dove l'avevo messa, l'avevo messa da... no. Sì. No."* Poi, **frase precisa una a storia (vincolo Bible §4.7)**: *"Le cose che si perdono non si perdono. Si nascondono dove non sai cercare."* Lo dice mentre infila la scatoletta in tasca senza guardarla. Poi torna confuso.

**Frase-chiave indicativa.** La frase precisa di Mèmolo è candidata. Già piena. Il narratore in chiusura non aggiunge regola — sigilla con immagine: il sole alto adesso, l'isola vista dall'alto è una rete di passi che oggi si è attivata.

**Semi ripresi.**
- **Liù** menzionata schema cast → prima apparizione vera, *frrr* + frase brevissima.
- **Salvia** (cornice S4) → ora cammeo nel proprio elemento, pianta nominata diversa (tiglio invece di ortica) → calendario di Salvia attivo.
- **Bastoncino di Noah**: tic gestuale en passant, mai annunciato — primo uso del gesto-firma.

**Semi piantati per blocchi C-D.**
- **Pattern A — le cose perse arrivano lo stesso** in semina: la cosa "perduta" non era persa, era nascosta. Il dente da latte di Pun custodito da Mèmolo è oggetto-strato 3 (l'adulto vede la tenerezza paterna nascosta).
- **Frase precisa di Mèmolo** istituita come "1 a storia se compare". Ricorre in S8.
- **Mappa silenziosa dell'isola** percorsa per intero per la prima volta (S6 = primo giro completo dei quattro punti) → eco strutturale del mandala silenzioso che si attiverà di nuovo in S11 (festa) e S12 (Concerto).
- **Le Vecchie del Mercato — *indicare in silenzio*** = firma del gruppo, **bloomerà in S11** come gesto di riconoscimento muto per Elias.
- **Micro-sguardo di Elias** (S4 variante S5): qui è capire l'altro (Pun) e tirarsi indietro. Variante leggera del seme paura.

**Paura toccata.** Elias — micro-eco (Elias trova ma è Pun a chiudere col padre. Sotto-traccia: *capire le cose degli altri silenziosamente non si vede*).

**Abitanti in scena.**
- **Mèmolo** (apertura, chiusura). Modalità confusa + frase precisa rara. Ruolo familiare: zio buffo, qui con fondo di tenerezza che il bambino sente senza sapere.
- **Pun** (scuola, poi finale). Ruolo: cucciolo della memoria pratica + ponte verso il padre.
- **Stria** (cammeo scuola). Ruolo: maestra-zia che vede e non interviene.
- **Fiamma** (cammeo Forno, modalità chiacchiera, 1 detto popolare riformulato).
- **Salvia** (cammeo casa, modalità lavoro, 1 pianta).
- **Zolla** (cammeo casa, modalità conta-stagioni).
- **Vecchie del Mercato** (cammeo Panca di Pietra, mai nominate, indicare in silenzio).
- **Liù** (cammeo *frrr*, una frase, riparte).

**Palette emotiva.** Sole più alto. Colori dei quattro quartieri attraversati (terracotta del Forno → sabbia di Salvia → ocra di Zolla → terracotta del centro). Scatoletta: legno scuro semplice. Dente da latte: unico riflesso freddo nella tavolozza calda.

**Callback.**
- A S5: Bru menzionato (Noah gli lascia un cornetto, Bru non in scena diretta — economia di personaggi).
- A S4: Salvia + cantilena Coltivatori (passaggio a primavera matura).
- A S1: Fiamma in modalità chiacchiera + detto popolare (eco di apertura saga, ma diversa applicazione).

**Note voce.** Detto popolare di Fiamma (1, dentro quota — generico, **non anticipazione trama**). Frase precisa di Mèmolo (1, dentro quota). **Paronomastico fisico candidato**: Mèmolo che sistema la sciarpa annodata male (es. *riannoda il nodo* / *aggroviglia*) — 1 di ≤2 saga, da raffinare in D. Memoria lunga del narratore: 1-2 incisi sull'isola attraversata. Nessun address al lettore.

---

## §3. BLOCCO C — ⟳ CAMBIARE (storie 7-9, estate + passaggio)

**Tema emotivo del blocco.** I fratelli imparano a stare nel cambiamento — cose che vanno via, cose che si rompono e arrivano lo stesso, cose che cadono e diventano altro, fratelli che crescono e diventano diversi. ⟳ all'esterno (Fiume, vento forte, stagione che vira) e ⟳ all'interno (Gabriel comincia a sentire che i fratelli non sono più gli stessi). **Il blocco non risolve niente — apre.**

**Atmosfere comuni.** Estate piena: caldo, finestre aperte, pesca all'alba e al tramonto, cuccioli alla Bocca, ombre più dure a mezzogiorno. Sere lunghe. Mulinello atteso ogni sera. Verso fine blocco: prime sere fresche, raccolto che inizia, foglie che cominciano a girare. Cambio di stagione *sentito*, mai dichiarato.

**Nota architetturale del blocco — temperatura più meditativa.** Più corti gli attriti, più peso negli sguardi che nei gesti. Coerente con ⟳ (cambiare = sentire qualcosa che si muove sotto, non agire). **Drammaturgia silenziosa degli sguardi installata** in questo blocco (Gabriel guarda Noah dietro il Pozzo S8, Gabriel guarda Noah dopo le fette S9, Elias vede Gabriel voltarsi quando Noah dà il braccialetto S9). Il bambino di 4 passa avanti senza vederli. Il rilettore li vede. Strato 3 puro.

**Pattern A in scena attiva** per la prima volta (semina S6 → bloom S7-S8). Dopo C il Pattern è installato.

---

### STORIA 7 — La Zattera dei Tre Rametti

**Stagione + ciclo.** Estate piena. C — ⟳.

**Luogo.** Lungo il Fiume che Gira, dal **guado di pietre piatte a nord** fino al **Pontile di Bartolo dentro La Bocca** a sud. Mezza giornata di cammino. Inizio mattino → tramonto.

**Vento.** Intreccio (giorno) accompagna il cammino — odori di Foresta e di mare. Mulinello (sera) all'arrivo, sposta cose alla Bocca.

**Premessa.** Mattina d'estate. **Noah ha l'idea**: *"Mettiamo qualcosa nel Fiume e seguiamolo fino al mare."* Idea sua, perché è ⟳ — gli viene da seguire l'acqua. **Elias propone di costruire una piccola zattera con tre rametti** raccolti la sera prima nel passaggio agli Orti — la lega col **nodo Marinaro** (callback diretto S5 — Elias usa la capacità acquisita, prima volta in scena vera). Tre rametti legati con filo d'erba secca. Gabriel chiede dove andrà. Decidono insieme. Camminano lungo la riva interna del Fiume.

**Problema.** A metà cammino — mezzogiorno, sole alto, Fiume che si stringe tra due massi — la zattera si incastra. Aspettano. Non si libera. Decidono insieme di liberarla. Elias allunga un bastoncino lungo per spostarla — gesto controllato, sa cosa sta facendo. Spinge piano. La zattera si muove. Si muove ancora. Poi —

**STRAPP.**

**Un rametto resta incastrato nei sassi. Due continuano. Il filo d'erba si è strappato dove i sassi tenevano stretto, non dove Elias aveva legato.** **Il nodo ha tenuto.** **Sono stati i sassi a strappare** (decisione Ray blocco 3: distinzione importante — Pattern A vero, non errore tecnico di Elias).

**Contributo dei tre fratelli.**
- **Noah:** idea iniziale. Quando STRAPP arriva, si ferma. Non piange (cresciuto da S3, S4). Dice piano *"Però due rametti vanno avanti."* — seme leggero per S9.
- **Elias:** ha legato bene (il nodo regge). Quando STRAPP, guarda il bastoncino in mano, non se stesso. Constatazione, non colpa. *"I sassi tenevano. Non c'era modo."* La distinzione tra *fare male* e *succedere* è tutta sua qui — sguardo adulto piccolo, non adultizzato (vedi nota Ray blocco 3).
- **Gabriel:** *"Andiamo avanti."* Decisione di continuare. **Una micro-occhiata di Gabriel a Noah** quando Noah dice la frase sui due rametti — Noah non è più quello che chiedeva di tornare a casa. Mai nominata. Preparazione lontana per S9.

**Momento-soglia.** Il momento di proseguire dopo la rottura. Non è la rottura il punto — è la decisione che la zattera *anche con due rametti* è ancora la zattera che stanno seguendo.

**Risoluzione.** Camminano fino alla Bocca. Passano vicino alla casa di **Amo** sulla scogliera est della Spiaggia delle Conchiglie — Amo ha le ali aperte al sole sulla scogliera, una croce nera. Nessuno parla. **Bartolo** è al Pontile, semi-disteso nella barca. Vede la zattera arrivare nell'acqua mista della Bocca — due rametti, filo d'erba mezzo sfrangiato. La guarda. **Non la raccoglie.** Si volta verso i fratelli — un occhio si chiude lento, si riapre lento. **Non dice niente** (modo di Bartolo nel blocco D istituito qui). **Toba** (cammeo, una sola scena) è seduta sul Pontile vicino al padre. Una domanda: *"E poi?"*. Bartolo non risponde. Noah: *"E poi è arrivata."* Toba ci pensa.

I fratelli restano a guardare la zattera che oscilla nell'acqua mista, finché non esce nel mare aperto. Non la prendono. Quando il sole comincia a calare tornano indietro lungo la riva — questa volta più dentro, attraverso gli Orti.

**Frase-chiave indicativa.** Direzione: chiusura del narratore con immagine. Pattern A in piena scena — *anche le cose rotte arrivano dove devono arrivare*, **non detto così**. Solo mostrato. Sigillo del narratore può lavorare sul Fiume che continua, sul fatto che la zattera ha imparato il mare anche senza un terzo rametto. Da affinare in D.

**Semi ripresi.**
- **Nodo Marinaro di Elias** (S5) → bloomato in azione vera. **Tiene.** Importante per il riequilibrio: Elias *sa fare* qualcosa che i fratelli non sanno, e il nodo che ha legato non ha ceduto. Visibile nei fatti, anche se nessuno lo dice.
- **Fermarsi quando non sai dove andare** (S1, S4) → qui *invertito*: continuare è la scelta giusta. Pattern di crescita — i fratelli sanno quando fermarsi e quando continuare.
- **Pattern A** (semina S6) → prima scena attiva.

**Semi piantati per blocco D.**
- **Bartolo che guarda senza prendere** → istituisce il modo di Bartolo nel blocco D (in S10 *"li vede e basta"*, nessuna parola).
- **Noah che dice *"però due rametti vanno avanti"*** → seme leggerissimo per *"non sono più piccolo come prima"* di S9.
- **L'oltre-il-mare** → la zattera esce nel mare aperto, narratore può farne un inciso minimo. Porta socchiusa per Fase F (Bible §8.8).

**Paura toccata.** Gabriel — micro-seme implicito (occhiata a Noah).

**Abitanti in scena.**
- **Bartolo** (Pontile, suo elemento). Ruolo familiare: nonno (silenzioso). Solo l'occhio che si chiude lento.
- **Toba** (cammeo, Pontile, una domanda). Ruolo: cucciola della domanda che apre.
- **Amo** (cammeo passante, scogliera, ali aperte, no parola).

**Palette emotiva.** Verde-blu del Fiume + verde Foresta sulla riva + sabbia chiara + grigio-piombo dei due massi che incastrano + filo d'erba verde-paglia + nero lucido di Amo croce sulla scogliera + verde-mare antico di Bartolo + tramonto arancione al ritorno.

**Callback.**
- Nodo Marinaro (S5) → bloom funzionale.
- Pattern A semina (S6) → prima attivazione.
- Gesto-firma di Noah dei bastoncini: questa volta è bastoncino-strumento (per spostare la zattera), non bastoncino raccolto camminando. Variante.

**Note voce.** **Address al lettore** in chiusura (1 di ≤6, primo del blocco C). **STRAPP** onomatopea isolata graficamente (1ª onomatopea-oggetto saga). Memoria lunga del narratore: 1-2 incisi sul Fiume e sui sassi che tengono per anni. Pattern A esplicito a livello di immagine, mai a livello di frase regola.

---

### STORIA 8 — L'Albero che Cadde di Sera

**Stagione + ciclo.** Estate piena (più tarda di S7 — afa). C — ⟳.

**Luogo.** Centro Villaggio. Piazza con Albero Vecchio + bottega di Nodo + casetta di Mèmolo + Pozzo. Cade un grande **noce** vicino al Pozzo, sulla via che porta dalla Piazza alla scuola di Stria. **NON l'Albero Vecchio** (che non cade mai — perno cosmologico silenzioso). Tardo pomeriggio → sera.

**Vento.** Mulinello (sera) — eccezionalmente forte. Annunciato da: cielo color piombo, mercato che chiude prima del solito, finestre che sbattono. **Liù** arriva con *frrr*: *"Il vento sale forte stasera. Forse l'acqua trema."* (correzione Ray blocco 3: ipotesi, non certezza — Liù messaggera, non veggente). **Quando l'acqua trema** = fenomeno raro Bible §8, **prima menzione in saga, 1 di ≤2.**

**Premessa.** I fratelli sono al Forno da Fiamma a finire un cornetto. Sentono il vento alzarsi. Liù passa col suo annuncio. Fiamma chiude le imposte. *"A casa veloci."* I fratelli escono. Mentre attraversano la Piazza per tornare verso casa, il Mulinello è già forte. Il noce vicino al Pozzo si piega. Si piega ancora. **CRACK.** Cade.

**Problema.** Nessuno è ferito (il noce cade verso il Pozzo, che resta intatto perché il tronco scarta in caduta). Ma la via per la scuola di Stria è bloccata. Il legno è dappertutto. Il Pozzo va liberato per la mattina dopo. **Mèmolo era uscito poco prima — chi sa per dove. Tornava verso la sua casetta tonda quando il noce è caduto** (refuso Ray blocco 3 chiarito). È confuso, sciarpa di sbieco, ronza in giro mormorando *"Aspetta, ero qui. Ero qui poco fa. Ero qui."*

**Contributo dei tre fratelli.**
- **Gabriel:** appena cade l'albero, la prima parola — *"Lì sotto c'era qualcuno?"*. Si ferma e *guarda* prima di muoversi (gesto di S1, ora in emergenza). Vede Mèmolo confuso e capisce in un attimo. **Gli si avvicina per istinto, non per deliberazione** (correzione Ray blocco 3: gesto istintivo, non piccolo adulto buono). Lo prende per mano, lo siede sul bordo del Pozzo. *"Stai qui. Sei qui."*
- **Elias:** arrivano i Mantenitori (collettivo, scale a pioli). Nodo è tra loro — **uno tra altri Mantenitori, uno gli passa una corda** (correzione Ray blocco 3: distinzione visiva da S5 Nodo-artigiano). Va a chiedere cosa serve. Nodo gli passa un capo di corda: *"Tieni. Lega quel ramo grosso per quando lo tiriamo via."* Elias riconosce il momento — lega col **nodo Marinaro** (callback S5/S7 in azione di crisi reale). Lavora in silenzio, accanto a Nodo, senza domande. Una volta sola, dopo il quarto nodo, Nodo lo guarda e fa un cenno con la testa.
- **Noah:** vede tra i rami caduti un **piccolo nido vuoto** — niente uccelli dentro, è un nido di maggio già abbandonato per la covata fatta. Lo raccoglie con cura, due mani, e lo posa al riparo dietro il Pozzo. Lo copre con una foglia. Gesto piccolo, irriflesso. Noah-⟳ alla sua maniera: salvare quello che resta anche se è vuoto.

**Momento-soglia.** Quando Mèmolo, seduto sul bordo del Pozzo accanto a Gabriel, smette di confondersi per un istante e dice — **frase precisa una a storia (vincolo Bible §4.7)** — *"L'albero ha aspettato che nessuno fosse sotto."* Lo dice piano, mentre infila una mano nella sciarpa storta a cercare qualcosa che non c'è. Poi torna confuso. Gabriel ed Elias sentono. Noah no — è dietro il Pozzo col nido.

**Risoluzione.** Mantenitori e Nodo lavorano fino alla notte (lanterne). I fratelli aiutano Elias finché possono, poi tornano a casa quando Fiamma li rimanda con un altro cornetto. Notte ferma — il Mulinello si è esaurito. La mattina dopo: legno in cataste, Pozzo libero, via libera per la scuola. **Stria** atterra sul tetto della scuola come ogni mattina. I Coltivatori passano in lontananza con la cantilena. **Mèmolo torna a passare di lì — si ferma davanti al Pozzo. Guarda il legno catastato.** Non dice niente. Si tocca la sciarpa. Va via.

Noah, prima di andare a scuola, va a controllare il nido dietro il Pozzo. È ancora lì.

**Frase-chiave indicativa.** Pattern A in scena chiarissima. **Frase precisa di Mèmolo *"L'albero ha aspettato che nessuno fosse sotto"*** è candidata a frase-chiave puntuale. È già dentro la storia. Il narratore in chiusura non ne aggiunge altra — sigilla solo con immagine.

**Semi ripresi.**
- **Nodo Marinaro** (S5, S7) → bloom in crisi reale. Elias diventa visibilmente "quello che sa fare i nodi" senza che nessuno lo dica.
- **Frase precisa di Mèmolo** (S6) → ricorre. Quota istituita.
- **Pattern A** (S6, S7) → bloom forte.
- **Liù** (S6) → cammeo coerente, ora porta annuncio del fenomeno raro (ipotesi).
- **TOK-TOK-TOK di Nodo** (S5) → presente in lavoro Mantenitori (3ª storia su 12 di ≤4-5 quota).
- **Vecchie del Mercato indicare in silenzio** (S6) → cammeo silenzioso dalla Panca di Pietra. Una alza una mano un attimo quando il noce cade.

**Semi piantati per blocco D.**
- **Il nido vuoto curato da Noah** → seme per S10 (notte senza luna, Noah). *Salvare quello che resta anche se è vuoto* è proto-gesto della cura nel buio.
- **Mèmolo che sta seduto sul Pozzo con Gabriel** → micro-eco di tenerezza muta tra Gabriel e Mèmolo.
- **Cataste di legna del noce** → diventeranno legna per l'inverno del Forno di Fiamma. Pattern A che si chiude in cerchio annuale, eco strutturale verso S12.
- **"Quando l'acqua trema"** istituito → 1 di ≤2 in saga.
- **Micro-occhiata di Gabriel verso Noah-dietro-il-Pozzo** che cura il nido da solo. Noah è cresciuto. Sotto-traccia.

**Paura toccata.** Gabriel — micro-eco.

**Abitanti in scena.**
- **Mèmolo** (centrale per il modo, non per l'azione). Frase precisa una. Ruolo familiare: zio buffo, qui con un fondo serio. Gabriel lo accudisce — inversione tenera dei ruoli, mai dichiarata.
- **Nodo** (lavoro, Mantenitore part-time, **uno tra altri**). TOK-TOK-TOK presente. Cenno della testa a Elias. Ruolo familiare: padre-pratico (intervallato da Bartolo nonno in S7).
- **Mantenitori** (collettivo, prima apparizione attiva piena). Scale a pioli, lanterne al crepuscolo.
- **Liù** (cammeo *frrr*, annuncio fenomeno raro come ipotesi).
- **Fiamma** (cammeo Forno, cornetti — modalità chiacchiera ridotta dal contesto, niente detto popolare qui).
- **Vecchie del Mercato** (cammeo silenzioso Panca di Pietra, una alza una mano).
- **Stria** (cammeo mattina dopo, atterra sul tetto come sempre — l'isola riprende).

**Palette emotiva.** Cielo color piombo + verde-grigio del noce piegato + bianco di pietra del Pozzo + nero lucido del legno spaccato fresco + arancione dei cornetti di Fiamma in cornice + giallo lanterne al crepuscolo. Notte ferma in mezzo. Mattina dopo: luce nitida pulita estiva.

**Callback.**
- Nodo Marinaro (S5, S7) → 3ª presenza, capacità installata.
- Frase precisa Mèmolo (S6).
- Pattern A (S6 semina, S7 prima scena, S8 scena piena).
- Liù (S6).
- Vecchie del Mercato indicare in silenzio (S6).

**Note voce.** **CRACK** onomatopea isolata graficamente (2ª onomatopea-oggetto saga dopo STRAPP S7). Memoria lunga del narratore: 1-2 incisi sull'Albero Vecchio che non cade mai. Una scena notturna brevissima accennata (notte ferma, lanterne lontane) — 2ª di 3-4 in saga, leggera. **Paronomastico fisico candidato**: Mèmolo che si rotola/aggroviglia (1ª opzione di ≤2 saga, in alternativa o congiunzione con S6).

---

### STORIA 9 — Quel Pomeriggio di Ottobre

**Stagione + ciclo.** Passaggio estate → autunno. Prime sere fresche. Foglie cominciano a girare. Castagne all'inizio. Raccolto degli Orti che parte. C — ⟳ (chiusura blocco). **Mai scrivere "l'autunno era arrivato" — scrivere "l'autunno cominciava" / "l'aria aveva cambiato"** (correzione Ray blocco 3).

**Luogo.** Quartiere di Fuoco — Forno di Fiamma + scuola di Stria (cornice mattina) + casa dei fratelli (sera). 28 ottobre = compleanno di Gabriel (Bible §2.2). **Mai data esplicita nel testo** — solo *"quel pomeriggio"* / *"il giorno del dolce di castagne"*.

**Vento.** Mulinello (sera) — calmo, non più forte come in S8. Si è esaurito col virare della stagione. All'alba Taglio è già un po' freddo — primo Taglio quasi-invernale.

**Premessa.** Sull'isola non ci sono compleanni con feste — c'è un piccolo rito: Fiamma fa il dolce di castagne (prime castagne dell'anno, calendario Zolla Bible §9.2), Stria a scuola lo annuncia con una frase, gli abitanti lo notano. Il festeggiato passa il giorno coi fratelli.

A scuola, mattino. **Stria** sulla porta vede entrare Gabriel. *"Tu cosa farai oggi che hai un anno in più?"*. Gabriel: *"Boh."* Stria: *"Pensaci."* Cuccioli (Pun, Toba, Bru, **Cardo**, Liù in volo sopra) sentono. **Cardo provoca (prima volta con voce in saga)**: *"Eh, ma chi te l'ha detto che è il tuo compleanno?"*. **Pun**: *"Mèmolo gliel'ha detto a Fiamma stamattina."* **Bru**: *"Sì."* **Toba**: *"E poi?"*. **Liù vola via verso il Forno.** (Ipotesi Ray blocco 3, da decidere in D: Liù è la fonte della notizia per Fiamma, vola al Forno prima dei fratelli.) **Provocazione di Cardo non ripresa, ognuno la sposta a modo suo** (correzione Ray).

**Problema.** Gabriel passa il pomeriggio con Elias e Noah a casa. Noah, che ha sei mesi più di quando li abbiamo conosciuti, ha imparato a fare un piccolo nodo — uno semplice (non il Marinaro, una variante più piccola che Elias gli ha mostrato in passaggio dopo S8). Lo fa per regalare a Gabriel un **braccialetto** di filo e ramoscelli — gesto di un Noah nuovo, che lavora di mani con calma per qualcuno. Lo annoda da solo. Quando lo dà a Gabriel: *"Te l'ho fatto io. Da solo."* Le tre parole **Da solo**.

**Il braccialetto deve essere brutto** (cura Ray blocco 3). Non grossolano-disastrato, ma evidentemente fatto da Noah — filo annodato non perfettamente, ramoscelli un po' irregolari, dimensioni approssimative. Bello solo perché lo ha fatto lui.

Gabriel ringrazia. Sorride. Si volta a prendere qualcosa dal tavolo. Per un attimo non guarda nessuno. **Stretto al cuore. Non spiegato.**

**Gabriel non si mette il braccialetto. Lo tiene in mano, lo guarda, lo posa sul tavolo accanto a sé** (cura Ray blocco 3). Resta sul tavolo per tutto il pomeriggio. Gabriel lo guarda di tanto in tanto. Gli altri non se ne accorgono.

**Contributo dei tre fratelli.** (Gabriel-centrico, gli altri sono presenti con misura)
- **Noah:** regala il braccialetto, lavorato in silenzio nei giorni precedenti. Non sa di aver scosso Gabriel.
- **Elias:** ha insegnato il nodo a Noah (off-screen, dopo S8). Quando Noah dà il regalo, Elias guarda Gabriel — vede il momento di volto-altrove. Capisce. Non dice niente. **Micro-sguardo di Elias** come nei semi del blocco B — qui è capire l'altro fratello, non sentirsi tagliato fuori. Variante leggera.
- **Gabriel:** è il festeggiato, oggi non agisce — *sente*. Per la prima volta nella saga è in posizione di osservatore di sé. ⟳ acuto in lui.

**Sera. Forno.** I tre vanno da Fiamma a prendere il dolce. Fiamma in modalità chiacchiera mentre toglie il dolce dal forno. **Detto popolare generico sul tempo che passa**: *"Eh ma si sa, anno che gira non è anno che torna. Ne fa un altro, diverso."* (1 detto, dentro quota — è generico, non riferito a Gabriel). Dolce di castagne (prime castagne dell'anno — micro-eco al raccolto di Zolla che parte adesso, eco strutturale verso S11).

A casa, sera. Tre fette del dolce. Gabriel taglia. **Si accorge di tagliare le fette diseguali — il piccolo per Noah, il medio per Elias, il grande per sé.** Lo fa quasi senza pensare, come ha sempre fatto da quando Noah era piccolissimo. Noah lo nota.

*"Perché il mio è piccolo?"*

Gabriel, senza pensare: *"Sei il piccolo."*

**Noah: *"Non sono più piccolo come prima."***

Pausa. Gabriel guarda Noah. Guarda la fetta. Guarda Elias.

**Momento-soglia.** Silenzio breve. Gabriel sorride — è un sorriso che è anche un po' commosso, ma Gabriel non spiega. **Cambia il taglio. Tre fette uguali.** *"Hai ragione."*

Mangiano. Elias dice qualcosa di pratico per stemperare — *"Le fette uguali stanno meglio nel piatto."* Noah ride. Gabriel sorride ancora. La sera passa. **Il braccialetto resta sul tavolo per tutto il dolce.**

**Risoluzione.** Non c'è risoluzione vera della paura. C'è l'apertura. Strato 1: il fratello maggiore ha ridiviso il dolce in fette uguali, è bello. Strato 2: Gabriel ha sentito che Noah cresce e ha dovuto cambiare il modo di tagliare — qualcosa si è mosso dentro. Strato 3: la paura di Gabriel di "perderli perché cresceranno diversi" si tocca per la prima volta con un gesto piccolo (le fette). Il narratore in chiusura sigilla con immagine sul vento Mulinello che la sera passa attraverso le finestre aperte. **Ultima immagine prima del sigillo: il braccialetto sul tavolo, accanto al piatto vuoto del dolce, e Gabriel che lo prende in mano mentre Noah ride di qualcosa che ha detto Elias. Lo prende, lo guarda. Non si dice se lo mette o no.** Decisione del lettore (o del Gabriel-saga di mesi dopo, cfr. S12).

**Frase-chiave indicativa.** *"Non sono più piccolo come prima."* — è già nel testo, è di Noah, è naturale. Funziona come frase-chiave perché il bambino di 4 la sente come *"Noah è diventato grande"*, il bambino di 9 sente che ha un peso per Gabriel, l'adulto coglie la paura. Multi-strato perfetto.

**Semi ripresi.**
- **Nodi** (S5 Elias, S8 Elias in crisi) → ora **trasferiti a Noah** (Elias glielo ha mostrato off-screen). Il sapere dei nodi viaggia tra i fratelli — eco silenziosa di TUM-tum-TUM di S4 (codice dei tre).
- **Stria con frase rilancio** (S2, S6) → ricorre.
- **Fiamma chiacchiera + detto popolare generico** (S1, S6) → ricorre.
- **Cuccioli scuola** (S6 collettivo) → cammeo distribuito (Cardo prima volta con voce, Pun, Bru, Toba, Liù).
- **Castagne** (calendario Zolla) → primo apparire stagionale, ponte verso S11.

**Semi piantati per blocco D.**
- **Paura di Gabriel emersa** → accolta in modo aperto in S12 (non risoluzione piena).
- **Le fette uguali** → micro-immagine candidata per cammeo simbolico in S11/S12.
- **Noah che annoda da solo** → nuova competenza, può tornare in S11.
- **Compleanno come rito non-rito** → istituito.
- **Braccialetto** → tornerà in S12 al polso di Gabriel (mai descritto come oggetto importante, solo visibile — decisione Ray blocco 4).

**Paura toccata.** **Gabriel — emerge.** Per la prima volta in saga, una paura affiora con peso visibile (un volto-altrove, un sorriso commosso, un cambio di gesto). Mai nominata.

**Abitanti in scena.**
- **Stria** (cornice scuola, una frase rilancio). Ruolo: maestra-zia.
- **Fiamma** (Forno, dolce castagne, modalità chiacchiera, 1 detto popolare generico). Ruolo: madre-calore — qui per Gabriel più che per Noah (variante distribuita, non default).
- **Cuccioli** (sfondo scuola): Cardo (prima volta con voce), Pun (memoria pratica), Bru (silenzioso), Toba ("E poi?"), Liù (vola via).

**Palette emotiva.** Mattina pulita di ottobre, luce nitida + giallo-arancio prime foglie autunnali + terracotta del Forno (cornice fissa) + marrone delle castagne + rosa-bordeaux del dolce + arancione del tramonto attraverso le finestre della casa dei fratelli. Sera fresca per la prima volta nel blocco — i fratelli forse hanno una camicia in più addosso.

**Callback.**
- Stria (S2).
- Fiamma chiacchiera + detto (S1, S6).
- Nodi (S5, S7, S8) → ora Noah lo fa.
- Cuccioli (S6 collettivo, ora individuati).

**Note voce.** Nessun address al lettore (è in S7 per il blocco). Memoria lunga del narratore: 1-2 incisi sull'isola in ottobre. Nessuna onomatopea-oggetto. Una scena di silenzio breve quando Gabriel taglia le fette diseguali — il silenzio è il momento stesso. Tono complessivo: più meditativo del blocco precedente.

---

## §4. BLOCCO D — INTEGRATO (storie 10-12, autunno + chiusura saga)

**Tema emotivo del blocco.** I fratelli stanno nelle proprie paure. Non le superano (sarebbe morale). Le attraversano (Noah), le accolgono attraverso un altro (Elias), le tengono dentro (Gabriel). Il blocco D non è apoteosi — è quiete. Ogni storia chiude qualcosa e lascia qualcosa aperto. La chiusura della saga è una chiusura *del tempo che hai vissuto con questi fratelli*, non *di tutto quello che resta da vivere*.

**Atmosfere comuni.** Autunno pieno: foglie cadute, terra umida, sole più basso, prime brine in chiusura (S12). Castagne, ghiande, noci nei sacchi e nelle dispense (Zolla in attività piena). Forno acceso più a lungo (Fiamma cuoce di più). Mantelli rimessi. Notti più lunghe. Fiume più alto per le piogge d'autunno. **L'isola si raccoglie su sé stessa.**

**Note architetturali del blocco.**

**(1) Modo della risoluzione.** Le tre risoluzioni del blocco D non avvengono mai per un *evento esterno che cambia il fratello*. Avvengono perché il fratello fa qualcosa **lui**. Noah dice *"Ho paura"* (gesto suo). Elias accetta un riconoscimento (gesto suo). Gabriel guarda l'isola intera e *non dice niente* (gesto suo). Nessun Vento Taglio che cura Noah, nessuna Vecchia che salva Elias, nessun Grunto che dà a Gabriel la chiave. **I personaggi del mondo sono cornici, mai risolutori.**

**(2) Narratore-iniziato in chiusura saga.** S12 contiene una delle ≤2 frasi-firma narratore esplicite (l'altra in S1) e l'unico frammento pre-Vento di Grunto in saga. Massima sobrietà — un solo tocco ciascuno, nella posizione esatta dove pesano.

**(3) Temperatura asciutta.** Il blocco D ha una temperatura particolare — **più asciutta** dei blocchi A-B-C. Meno avventura, più camminata. Più gesti, meno parole. Più sguardi, meno dialoghi. **In Fase D scrivere col respiro più piano.** È un blocco di fine giornata, in tutti i sensi.

**(4) Dire / accettare / tenere.** Le tre paure si risolvono in modi *non simmetrici per evento ma simmetrici per modo del fratello*: Noah dice (tre parole), Elias accetta (uno sguardo), Gabriel tiene (mani sulla terra, briciole, braccialetto). Sono i tre modi maturi di stare con se stessi — universali, non personalizzati. **Strato 3 architrave dell'intera saga.**

**(5) L'isola dopo S12 resta viva.** Bartolo continua a traghettare, Fiamma cuoce, Stria insegna, Grunto sale e scende dal Burrone, Vecchie sulla Panca di Pietra, Mercato del Mezzogiorno ogni giorno. Il narratore in chiusura saga **non chiude l'isola** — chiude l'anno con i tre fratelli. **Il mondo non si chiude.** Promessa per Fase F.

**Pattern A in chiusura silente.** In tutto il blocco D il Pattern A non viene mai *nominato*. Vive nelle immagini: S10 il buio era pieno (vuoto → pieno), S11 la festa che non si vince, il cono dato a Bru, i frutti da fuori (in più → arriva), S12 l'anno che chiude e i fratelli cresciuti diversi che sono ancora insieme (trasformato → arriva intero).

---

### STORIA 10 — La Notte senza Luna

**Stagione + ciclo.** Autunno pieno. D — integrato (Δ⇄⟳ tutti presenti, nessuno dominante).

**Luogo.** Casa dei fratelli (interno) → Piazza Villaggio (esterno notturno) → Via del Pontile fino al Pontile di Bartolo. Notte intera. All'alba: ritorno verso casa.

**Vento.** Notte ferma — i tre venti dormono (Bible §1.5, notte non personificata). All'alba: Taglio.

**Premessa.** Sera. Pioggia leggera ha fatto cadere le foglie del platano davanti casa per terra. Niente luna stanotte (annunciato dalla cantilena dei Coltivatori che hanno chiuso prima — *"luna nera, terra ferma, mani al fuoco"*, mai detto come informazione meteo, solo cantato in lontananza — **5ª e ultima cantilena saga**). Si va a dormire.

**Noah ha portato a letto, da S8, il nido vuoto.** Lo tiene sul comodino. Gli piace sapere che c'è.

**Problema.** Notte. Buio totale (no luna). Noah si sveglia. Sente il cuore. Il nido sul comodino è una sagoma scura. La casa fa rumori che di giorno non fa. Gabriel ed Elias dormono. Noah resta sotto le coperte. Il cuore va più forte. Si avvicina al letto di Gabriel — gesto suo da sempre. Ma stanotte non basta. Si tira su. Resta seduto sul bordo del letto di Gabriel.

Poi, piano: *"Gabriel."*

Gabriel si sveglia. Vede Noah. Non chiede.

**Noah, voce piccola: *"Ho paura."***

**Le tre parole. La soglia di tutto.**

**Contributo dei tre fratelli.**
- **Noah:** dice le tre parole. Per la prima volta in saga, ammette una paura ad alta voce. Tutto il blocco D di Noah è dentro queste tre parole.
- **Gabriel:** si sveglia subito. Non spiega, non rassicura. Sveglia Elias con un tocco. *"Vieni."*
- **Elias:** si alza senza chiedere. Capisce dall'aria della stanza.

**Decisione.** Escono di casa, in silenzio, tutti e tre. Mantelli sulle spalle, piedi scalzi negli stivali. Fuori è buio. Pioggia ferma da poco — l'aria è bagnata e fresca. Le foglie del platano per terra. Camminano verso la Piazza.

**Sviluppo.** Piazza vuota. Albero Vecchio è una sagoma più scura del cielo. Nessuno in giro. Noah tiene la mano di Gabriel, l'altra di Elias. Gabriel guida — sa la strada anche senza vedere (callback S1 indiretto). Elias non parla — capisce che l'unica cosa da fare è camminare insieme. Vanno verso sud, Via del Pontile.

**Cammino lungo nel buio.** **In Fase D far sentire la lunghezza del cammino senza dirla esplicitamente** (correzione Ray blocco 4): passano davanti al Forno spento, davanti alla casetta di Mèmolo buia, davanti agli orti che riposano. La camminata pesa. Il bambino di 4 sente che è stata una notte lunga senza che il narratore lo dica.

Noah sente:
- Il rumore dei propri stivali sulla pietra.
- L'odore della terra bagnata.
- Da lontano, **un *grunt* dal Burrone** (Grunto sveglio — è sempre più sveglio degli altri, dorme poco e male). **Effetto realistico**, non magico (correzione Ray blocco 4): di notte i suoni viaggiano molto più lontano, aria fredda porta meglio le frequenze basse. Il bambino di 9 lo riconosce come fenomeno fisico. Il *grunt* nel buio non è spaventoso — è *presenza*. Qualcuno è sveglio anche lui.
- **Un gufo che chiama** — *hu-hu-huùh* — non visto. Risposta da molto lontano. **Eco silenziosa con Tempesta = Gufo del libro 0** (correzione Ray blocco 4: in una notte in cui i venti dormono, l'unico verso notturno è del gufo, parente cosmologico del Vento Mulinello). Strato 3 puro.
- Le foglie sotto i piedi.

**Il buio non è vuoto. Il buio è pieno di cose che di giorno non senti.**

**Arrivano al Pontile.** **Bartolo** è seduto nella sua barca semi-disteso, occhi aperti — non dorme mai del tutto la notte. Vede i tre arrivare. Non si stupisce. **Non dice niente.** **Non parla per tutta la scena.** Modo istituito in S7 (vede e basta). Si fa un po' più in là — gesto silenzioso che fa spazio. I tre si siedono sul Pontile, accanto alla barca. Gambe che pendono sull'acqua.

Si sente l'acqua contro i pali del Pontile. Sale leggero al naso. Restano lì. Aspettano.

Poco prima dell'alba, l'aria cambia. Il cielo a est si fa appena meno nero. Una linea grigio-azzurra all'orizzonte sul mare. Vento Taglio comincia, freddo, leggero.

Da poco oltre, sulla scogliera est della Spiaggia, **Amo** apre le ali al sole che sta per arrivare — sagoma nera contro grigio. Non li vede. Sta facendo la sua cosa di sempre.

**Momento-soglia.** **Non è l'arrivo dell'alba.** La soglia era già stata attraversata prima — quando Noah ha detto *"Ho paura"*. L'alba è solo conferma. Quando il primo bordo di sole appare sull'acqua, Noah dice piano: *"Però era pieno."*

Gabriel: *"Cosa."*

Noah: *"Il buio. Era pieno."*

**Risoluzione.** Tornano a casa col primo Taglio addosso. **Fiamma** sta accendendo il forno (è prima dell'alba — ora di Fiamma). Li vede passare. Non chiede. Mette in mano a Noah un cornetto caldo. *"Hai mangiato?"* Noah fa di no con la testa. Fiamma gliene mette in mano un altro. Tornano a casa, mangiano, dormono ancora un po'.

Quella sera Noah tiene il nido sul comodino come sempre. Stavolta lo guarda, lo posa, dorme.

**Frase-chiave indicativa.** Direzione: il narratore in chiusura sigilla con immagine — **nessuna regola, nessun *"il buio non è vuoto"* dichiarato.** Quella verità è già detta da Noah dentro la storia in *"Però era pieno"*. Il narratore può lavorare sull'immagine del Pontile all'alba con i tre fratelli e Bartolo silenzioso nella barca, e il sole che si alza sull'acqua. Una porta socchiusa verso *quello che c'è oltre il mare*, mai dichiarata.

**Semi ripresi dal blocco precedente.**
- **Nido vuoto curato da Noah** (S8) → bloomato come oggetto di transizione di Noah verso il buio. *Salvare quello che resta anche se è vuoto* → preparazione perfetta per accogliere il buio come pieno.
- **Bartolo che vede e basta** (S7) → modo istituito, applicato in scena di crisi notturna. **Cornice silenziosa**, mai risolutore.
- **Gabriel sa la strada anche senza vedere** (S1) → trasferito al buio. Continuità Δ del personaggio.
- **Pattern A** (S6, S7, S8) → in modo nuovo: *anche le cose vuote sono piene* è la versione di Noah del Pattern.
- **Cantilena Coltivatori** in cornice serale (5ª saga, ultima — chiude quota).

**Semi piantati per S11/S12.**
- **Noah ha attraversato la prima paura sua** → libera energia per S11 e S12, Noah può essere pienamente attivo.
- **Bartolo silenzioso al Pontile come ricetto notturno** → eventuale eco in S12 quando i fratelli passano dal Pontile.
- **Amo cammeo all'alba** (3ª e ultima apparizione saga: S7, S10, S11).

**Paura toccata.** **Noah — risolta** (con il modo: **dire**). Attraversata, non superata.

**Abitanti in scena.**
- **Bartolo** (Pontile, notte). **Zero parole.** Ruolo familiare: nonno silenzioso (variante notturna). Pura cornice presente.
- **Amo** (cammeo all'alba sulla scogliera, sagoma nera, no parola).
- **Fiamma** (cammeo Forno pre-alba, *"Hai mangiato?"* — modalità ferma, non chiacchiera, niente detto popolare). Ruolo familiare: madre-calore al ritorno, brevissima. Cornetto come oggetto-cura.
- **Grunto** (presenza acustica solo — *grunt* dal Burrone udibile dalla Piazza nel silenzio. Coerente col vincolo "solo alle Montagne": qui non scende, si sente). Zero parole.

**Palette emotiva.** Nero della notte + grigio-azzurro dell'alba + sale e nero dell'acqua del Pontile + nero lucido di Amo croce sulla scogliera + arancio del forno di Fiamma a fine cornice + marrone del cornetto. Il nido sul comodino: bruno chiaro con sfumature dorate (eredita autunno).

**Callback.**
- Nido (S8 Noah).
- Bartolo modo (S7).
- Gabriel sa la strada (S1).
- Pattern A trasversale.
- Eco cosmologica Tempesta=Gufo (libro 0) col verso del gufo notturno.

**Note voce.** **Address al lettore** in chiusura (1 di ≤6, il 4° del blocco). **Una scena notturna piena** (è la più piena delle 3-4 in saga). Memoria lunga del narratore: 1-2 incisi sul Pontile di notte e sull'alba che arriva sempre, anche dopo le notti più nere (mai detta come massima). **Frase di Noah *"Però era pieno"*** è candidata a frase-chiave puntuale — molto forte, da bambino, multi-strato perfetto. Onomatopee: nessuna oggetto. *hu-hu-huùh* del gufo come unica nota acustica natura. *grunt* di Grunto come firma installata, qui nel buio = pesa.

---

### STORIA 11 — La Festa del Raccolto

**Stagione + ciclo.** Autunno pieno (più tardi di S10). D — integrato.

**Luogo.** Tutta isola in attivazione. Centro: Piazza Villaggio. Periferie: Orti del Cerchio (raccolto rituale al mattino), Pascoli Alti (Pastori scendono con greggi), Pontile (Bartolo arriva con qualcosa da fuori), Forno di Fiamma (dolce centrale). Mezzogiorno è il fulcro.

**Vento.** Tutti e tre, sui tempi del giorno (Taglio all'alba per chi parte presto, Intreccio di giorno per la festa piena, Mulinello la sera al ritorno). **L'isola che respira tutti i suoi tre venti in uno solo.**

**Premessa.** Festa del Raccolto = giorno annuale dell'isola in cui tutti gli abitanti del villaggio e dei quartieri si ritrovano in Piazza, ognuno porta qualcosa, si mangia insieme sotto l'Albero Vecchio, ci sono piccoli giochi collettivi non gare. **Non si premia nessuno. Non c'è capo. Si fa.** I tre fratelli partecipano. È la prima festa dell'isola che vediamo per intero in saga.

**Problema (sviluppo Elias).** All'inizio della festa, Elias si sente al posto suo. Lega corda intrecciata coi Mantenitori (usa il Marinaro, callback S5/S7/S8). Aiuta Nodo a riparare un banco improvvisato. Aiuta Salvia a portare un cesto di erbe per il dolce di Fiamma. Fa cose. Ma intorno a mezzogiorno succede una serie di cose che lo spostano.

**Le cose che lo spostano (3, ognuna piccola):**

1. **Gabriel** vince scherzosamente una piccola prova di forza coi Pastori (sollevare un sacco di castagne più alto degli altri). Risate. Gabriel ride. Tutti si congratulano — *"il maggiore dei tre, eh!"*. Elias guarda. Non dice niente.

2. **Noah** corre tra i banchi con Cardo e Pun e Toba — rompono un piccolo sgabello, **rotola un pomo**, ridono. **Paronomastico fisico candidato (rotola/rotola)** — 2° di ≤2 saga. Il nonno di un altro cucciolo (sfondo, non nominato) li sgrida con sorriso. Noah ride forte. Tutti guardano. **Noah è *vivo* e *visto*.** Elias si volta a sistemare un banco.

3. **Stria** dalla scuola (in cornice di passaggio) saluta gli alunni distribuendo a ognuno un piccolo cono di carta con dentro tre **ghiande dipinte** — gesto di Stria per la festa, che fa una volta all'anno (dato di mondo, mai spiegato). A Pun: *"Le porti a Mèmolo da parte mia."*. A Bru: *"Per Rovo."*. A Cardo: *"Per te."* (perché Cardo non ha nessuno a cui portarle — micro-strato 3, mai sottolineato). A Toba: *"Per Bartolo."*. **A Gabriel, Elias, Noah dà tre coni separati. Non li distingue. — Anzi: dà a Elias quattro coni invece di tre.** **Stria non sbaglia mai** (correzione Ray blocco 4): dà quattro perché *sa*. **Stria sa che Elias darà via uno.** Stria vede in Elias quello che le Vecchie vedranno più tardi. Lo riconosce da prima. Elias lo vive come errore — gli sembra che Stria si stia confondendo. **Strato 3 puro.** In Fase D: la consegna di Stria a Elias deve essere un attimo più lunga delle altre (uno sguardo che dura mezzo secondo in più), ma non commentata.

Elias guarda i suoi quattro coni in mano. Non c'è scritto chi sono. Sono ghiande dipinte. Come le altre. Elias sente quella cosa che è la sua paura — una piccola cosa storta dentro che non ha parole.

**Contributo dei tre fratelli.**
- **Gabriel:** presente, fa, partecipa. Vince la prova senza enfasi, ride. **Gabriel è *presente all'altro*** — stamattina ha visto Elias che era un po' lontano, ma non sa il perché. Si occupa di Noah più di Elias (si è abituato). Errore involontario.
- **Noah:** pieno di energia, gioca coi cuccioli. È vivo. **Noah è *libero*** — ha attraversato il buio in S10 e adesso non gli pesa nulla.
- **Elias:** fa, lega, costruisce, aiuta. Ma è nello sguardo di lato. Da S4 in poi, i micro-sguardi sono accumulati silenziosamente. Adesso esce il momento.

**Momento-soglia.** Pomeriggio inoltrato. La festa rallenta. Sotto l'Albero Vecchio, sulla Panca di Pietra, **le Vecchie del Mercato.** Una di loro — *l'indicare in silenzio* (firma istituita S6, S8) — **alza una mano e indica Elias.** Solo lui. Lo guarda negli occhi, una volta. Annuisce piano. Poi torna a guardare avanti.

**Nessuna spiegazione. Nessuna parola.**

Elias si ferma. Capisce di essere stato visto. Non ha vinto niente. Non gli hanno detto *bravo*. Una vecchia che non ha mai parlato in saga e che non parlerà mai gli ha indicato. Una volta sola.

**Risoluzione.** Elias resta lì un momento. Poi va da Gabriel e Noah, che sono al banco di Fiamma. Si siede accanto a loro. Mangia il dolce.

**I quattro coni di Stria** — Elias li distribuisce. Uno per Gabriel. Uno per Noah. Uno per sé. **Il quarto, dopo un secondo di esitazione, lo dà a Bru**, che è solo accanto al Pozzo (Rovo non è venuto alla festa, Bible §4.5: Rovo non sta nel villaggio. **Bru porta qualcosa per Rovo al ritorno** — un sacchetto delle erbe di Salvia, una porzione del dolce di Fiamma — mai descritto in dettaglio, solo visto. Strato 3: chi cura Rovo a distanza è Bru, e gli abitanti del villaggio lo sanno e si comportano di conseguenza). Bru lo prende, non dice grazie. Si guardano. Bru annuisce piccolissimo.

Elias torna a Gabriel e Noah. Mangia il dolce. La festa continua.

Sera. **Bartolo** è arrivato dal mare nel pomeriggio con la barca — ha portato qualcosa da fuori (un cesto di **frutti che non crescono sull'isola**, mai descritti in dettaglio, ma il bambino di 9 nota che esistono altre terre, eco Bible §8.8). Lo posa al banco di Fiamma. Non dice da dove. Bartolo, modo confermato (silenzioso, fa).

Tornano a casa col Mulinello della sera.

**A casa, sera. Due battute brevi:**

Elias: *"Oggi mi ha indicato una vecchia."*
Gabriel: *"Quale?"*
Elias: *"Una."*

(correzione Ray blocco 4: **due battute asciutte, conversazione si chiude su una sillaba.** Gabriel non capisce, non saprà mai bene cosa è successo a suo fratello quel pomeriggio, e questo è giusto.)

**Frase-chiave indicativa.** Nessun personaggio dice la frase di Elias. Il narratore in chiusura può lavorare sull'immagine di Elias coi quattro coni — quello che ha dato a Bru è parte del gesto. **Dare a chi non aveva è il suo modo di stare in mezzo. Non *quello in mezzo* come limite — *quello in mezzo* come funzione.** Mai dichiarato. Sigillo del narratore + due battute asciutte di Elias/Gabriel.

**Semi ripresi.**
- **Vecchie del Mercato indicare in silenzio** (S6, S8) → bloomato. Diventa il gesto di riconoscimento muto che salva Elias senza spiegarlo.
- **Nodo Marinaro** (S5, S7, S8) → ricorre, capacità installata di Elias.
- **Bartolo che porta qualcosa da fuori** → eredita Bible §8.8, prima volta visibile in saga.
- **Pattern A** → festa che non si vince, riconoscimento che non è premio, dare ciò che hai in più a chi non aveva. Variante.
- **Cuccioli con voci** (S6, S9) → ricorre tutto il gruppo.
- **Compleanno come rito non-rito** (S9) → la festa è lo stesso tipo di rito non-rito, su scala collettiva.
- **Stria che vede prima** (S2, S6, S9) → bloomata in modo cruciale: dà quattro coni perché sa.

**Semi piantati per S12.**
- **Frutti da fuori di Bartolo** → porta socchiusa più visibile (Fase F).
- **Bru riconosciuto da Elias come quello-solo** → eventuale eco in S12.
- **Coni di Stria distribuiti per legame** → istituisce un gesto di Stria per la chiusura annuale.

**Paura toccata.** **Elias — risolta** (con il modo: **accettare**. Complessa, non per vittoria, per riconoscimento muto da chi non parla mai).

**Abitanti in scena.** Tanti — è la festa.
- **Vecchie del Mercato** (Panca di Pietra). Una sola gesto, *indicare in silenzio*. Centrale per Elias. Mai nominate.
- **Stria** (cornice scuola, distribuzione coni — quattro a Elias intenzionali). Ruolo familiare: maestra-zia.
- **Fiamma** (banco dolci, modalità chiacchiera). Detto popolare ammesso (1, generico sul raccolto).
- **Nodo** (lavoro festa, TOK-TOK-TOK in lavoro su banco — 4ª storia su 12). Ruolo: padre-pratico.
- **Mèmolo** (presenza confusa nella festa, sciarpa storta, Pun che lo accompagna). Frase precisa una opzionale (da decidere D — possibilmente saltata per non saturare).
- **Salvia** (cammeo cesto erbe per Fiamma, pianta nominata: **rosmarino** — riserva, prima volta usata).
- **Zolla** (cammeo coi sacchi del raccolto, modalità conta-stagioni, *"Quest'anno noci in più. Fortuna."*).
- **Amo** (cammeo Mercato per scaricare un cesto di pesce festivo, modalità silenziosa, ridotto).
- **Bartolo** (cammeo arrivo Pontile con frutti da fuori, sera). Ruolo: nonno.
- **Cuccioli**: Pun (con Mèmolo), Toba (con Bartolo poi), Bru (solo, riconosciuto da Elias, porta a Rovo), Cardo (provoca-gioca con Noah).
- **Coltivatori, Mantenitori, Camminanti, Pastori** (collettivi, sfondo).
- **Rovo assente, segnato via Bru.**

**Palette emotiva.** Caldo autunnale: rossi e arancioni del raccolto + bruno scuro delle castagne + giallo-oro delle ghiande dipinte + verde scuro del rosmarino + terracotta dei banchi + vivo fuoco al centro Piazza per il dolce + grigio-cenere di Stria + verde mare antico di Bartolo che arriva. Sera al ritorno: viola-arancione Mulinello, fuochi di lanterne dei banchi che chiudono.

**Callback.**
- Vecchie indicare (S6, S8).
- Nodo Marinaro (S5, S7, S8 e qui Elias-corda).
- Bartolo modo (S7, S10, e qui *fa*).
- Cuccioli individuati (S9).
- Pattern A.
- Stria vede prima (S2, S6, S9).

**Note voce.** TOK-TOK-TOK Nodo (4ª storia su 12, dentro quota). Detto popolare Fiamma (1, generico). **Paronomastico fisico col pomo che rotola** (2° di ≤2 saga, da raffinare D). Memoria lunga del narratore: 2-3 incisi sull'isola che si raccoglie una volta all'anno (mai dichiarata come *rito*, solo *fatto*). Nessun address al lettore (è in S10 e arriverà in S12).

---

### STORIA 12 — Quando i Tre Venti Suonano Insieme

**Stagione + ciclo.** Passaggio autunno → inverno. Prima brina la mattina dopo (calendario §9.2). **Anno chiuso.** D — integrato totale.

**Luogo.** Tutta isola. Percorso che dall'alba al tramonto attraversa: casa dei fratelli → Forno → Pontile (cammeo Bartolo) → riva del Fiume sud → guado pietre piatte nord → **radura dei pini** (callback S5) → Pascoli Alti (cammeo, no Stria) → **Burrone** (incontro Grunto) → cengia che porta a **Roccia Alta** (arrivo finale). **Rientro al Forno alla sera.**

**Vento.** I Tre Venti soffiano insieme — **il Concerto** (Tratto 12 attivato — **nome proprio, da aggiungere a Glossario in aggiornamento Fase D**). Fenomeno raro che capita una volta ogni tanto, quando le condizioni meteo si allineano. Si capisce dall'aria che oggi sarà il giorno. Bisogna essere lassù per il momento giusto.

**Premessa.** Mattina presto. **Liù** vola alla finestra dei fratelli con un *frrr*: *"Oggi suonano. Andate?"* (correzione Ray blocco 4: Liù prima a chiamarlo *suonano* — implica un fatto che ha un nome, gli abitanti lo conoscono). Sì.

I fratelli partono. Non c'è altro motivo che essere lassù per il Concerto. Tutta la storia è *cammino*. Tutto il blocco A-C-D si depone ai loro piedi mentre attraversano l'isola. Il narratore-iniziato — qui, ed è una delle ≤2 frasi-firma esplicite saga — può aprire la storia con qualcosa di sigillato sull'anno che chiude. Da scrivere in D, sobrio.

**Sviluppo del cammino.**
Ogni tappa è breve, un cammeo solo, niente dialoghi lunghi. La storia è camminata, non parlata.

**Forno (mattino).** **Fiamma** sveglia, modalità ferma. *"Andate."* Mette in mano a Noah due cornetti caldi e una pagnotta nella sacca di Gabriel. *"Una è per Grunto."* (callback diretto S1 — la pagnotta a Grunto era come si è aperto la saga, è come la chiude). Niente detto popolare qui — Fiamma in modalità ferma, sa che è il giorno. **Sguardo lungo a Gabriel mentre escono.** (Micro-seme: Fiamma sa qualcosa che Gabriel sta vivendo. Mai dichiarato.)

**Pontile (passaggio).** **Bartolo** è già nella barca, occhi aperti sul mare. Vede i tre passare. Una mano si alza piano, ricade. Niente parola. Loro lo salutano col mento.

**Riva del Fiume — guado pietre piatte.** Acqua più alta per le piogge d'autunno. **Quando l'acqua trema** — il fenomeno raro, **2° di ≤2 saga** (1° in S8). Per un attimo il Fiume si increspa controcorrente e poi torna. I fratelli vedono. Gabriel: *"Hai visto?"* Elias: *"Sì."* Noah: *"Anche prima — c'era stato."* (callback indiretto S8, Noah ha imparato a sentire). Attraversano il guado.

**Radura dei pini (S5 callback).** I fratelli passano per la radura dove avevano costruito il ponte. La radura è autunnale ora — i pini hanno fatto cadere i loro aghi gialli sul cerchio d'erba. Si fermano un attimo. Noah cammina nel cerchio. Gli altri due lo guardano. Riprendono.

**Pascoli Alti.** Erba secca di fine autunno. Non c'è Stria — vola altrove oggi, Liù lo sa. I Pastori hanno già portato giù le greggi. È vuoto. Si vede l'isola estendersi.

**Burrone.** **Grunto è sulla cengia, dove Gabriel lo aveva incontrato in S1.** *Grunt* iniziale. *Via.* I fratelli restano. Grunto smette di guardarli (permesso, eredita S1). **Gabriel posa la pagnotta su una pietra piatta — gesto identico a S1, chiude la simmetria.**

**Qui — l'unico frammento pre-Vento Grunto della saga (Bible §1.4).**

Direzione di lavoro per Fase D: Grunto annusa la pagnotta. Sta in silenzio. Poi, **guardando lontano, non i fratelli**, dice qualcosa di breve e incompiuto. Direzione candidata (correzione Ray blocco 4):

*"Una volta era visto. Adesso si respira."*

(Soggetto sparito del tutto. Visto come stato del mondo, respirato come stato del mondo. Differenza tra due ere senza nominare nessuno. Più sicura. Mai i nomi propri Ariete/Ondina/Tempesta. Mai una scena pre-Vento ricostruita per intero. Mai nostalgia. Solo una distinzione muta tra *visto* e *respirato* — che il bambino di 4 non capisce, il bambino di 9 si chiede *cosa intende*, l'adulto coglie. **Architrave dello strato 3.**)

**Tre cure operative su questo frammento (per Fase D):**
1. Detto guardando lontano, non i fratelli.
2. Soggetto sparito del tutto (variante con *"si respira"*, non *"è respirato"* per evitare lettura passiva con soggetto omesso).
3. Dopo la frase, nessuna reazione visibile dei fratelli. Non Elias che dice *"Cosa?"*, non Gabriel che si volta. **I fratelli sentono e basta.** Forse Noah sposta un piede. Massimo. Il momento è di Grunto — e poi si chiude con la pagnotta annusata e il *"Buono"* di scambio.

I fratelli non chiedono nulla. Noah dice *"Buono?"* (eco rovesciato di S1 dove era Grunto a dirlo). Grunto: *"Buono."* Una parola sola, identica.

I fratelli salgono verso la Roccia Alta.

**Roccia Alta. Pomeriggio.** Vista totale: Foresta, Orti, Villaggio, Forno, Pontile, Bocca, mare attorno, **Montagne dietro le spalle** (correzione Ray blocco 4: alle spalle Grunto e il mito, davanti il mondo presente. Strato 3 silenzioso, sottolineato appena dal narratore). Aspettano. Si siedono.

**Il Concerto.** Comincia che non te ne accorgi all'inizio. Il Vento Taglio è ancora nell'aria che cala dalle Montagne (è pomeriggio inoltrato — Taglio non è alba, ma l'eco persiste in alto). Il Vento Intreccio sale dalla terra interna con gli odori dell'isola (Forno, Foresta, Mercato dell'ultimo passaggio del giorno). Il Vento Mulinello entra dal mare a sud, gira intorno alla Roccia.

I tre venti si incontrano *sulla* Roccia Alta — è il punto dove l'isola li unisce. **Non è suono di musica letterale.** È che l'aria diventa *piena di tutta l'isola insieme*, e per un momento i fratelli sentono il mondo come un corpo solo. **Da scrivere in D senza eccedere.**

**Momento-soglia.** Gabriel, seduto tra Elias e Noah, guarda l'isola sotto. Sente — senza dirlo — che i fratelli accanto a lui non sono più quelli con cui ha cominciato l'anno. Noah è cresciuto. Elias è cresciuto. Lui è cresciuto. Sono diversi. **La paura di Gabriel è in lui, intera. Non si risolve. La tiene.**

Una mano sua si appoggia sulla terra accanto a sé. Una mano di Noah, irriflessa, si appoggia sulla sua. Elias dall'altro lato, senza guardare, fa lo stesso col gomito. I tre stanno così. Pochi secondi. Niente.

**Gabriel non dice niente.**

**Resa.** Restano fino al tramonto. Quando il sole cala, il Concerto rallenta — i venti si separano, ognuno torna nel suo tempo. L'isola torna alla sera ordinaria (Mulinello solo). Si alzano. Cominciano a scendere.

**Risoluzione (chiusura saga — cornice al Forno).**

Scendono dalla Roccia Alta quando il sole è già basso. Il Concerto è finito. I tre venti sono tornati nei loro tempi (Mulinello solo, sera). Camminano in silenzio. Niente parole. Le ombre lunghe sui sentieri. Passano davanti al Burrone — Grunto non si vede più, è rientrato nella grotta. Passano dai Pascoli vuoti. Non rifanno la radura dei pini. Scendono direttamente verso il Villaggio per la Via che Sale.

Quando arrivano al Villaggio è quasi notte. La Piazza è quieta — l'Albero Vecchio è una sagoma scura contro il viola del cielo. **Una lampada accesa al Forno di Fiamma**, in fondo alla Via dell'Alba.

Vanno al Forno.

Fiamma è dentro, non sta cuocendo — sta rimettendo a posto la cucina prima della notte. Li vede entrare. Non chiede com'è andato il Concerto. Sa.

*"Sedete."*

Tira fuori dal forno (ancora caldo) un piccolo dolce — non è un dolce di festa, è un dolce normale, di quelli che fa qualche volta dopo cena per chi capita. Lo posa sul tavolo. **Quattro fette.** Una per Fiamma stavolta — siede con loro.

Mangiano in silenzio. Fiamma in modalità ferma, non chiacchiera. **Una sola frase, en passant**, mentre versa qualcosa di caldo nelle tazze: *"Domani brina."* **Niente detto popolare** — è il momento sbagliato, e Fiamma in modalità ferma non li usa.

I fratelli mangiano. Gabriel ha le mani sulla tazza. Elias mastica piano. Noah ha le gambe che dondolano dalla sedia (è ancora il piccolo, anche se cresciuto).

Fuori, il Mulinello cala. La sera diventa notte.

**Ultima immagine prima del sigillo del narratore.** Fiamma e i tre fratelli al tavolo del Forno. Una candela. Il dolce mangiato a metà. **Gabriel che, senza pensarci, prende una briciola dal piatto di Noah col dito e la porta alla bocca** — gesto che faceva da sempre, da quando Noah era piccolissimo e non finiva mai. Stavolta lo fa per abitudine, e Noah, anche lui per abitudine, sposta il piatto un po' più verso Gabriel — *prendi, se vuoi*. Gesto di sempre, gesto di adesso.

**Il braccialetto di Noah (S9) è al polso di Gabriel — non descritto come oggetto importante, solo visibile.** Il bambino di 4 vede; il rilettore collega; l'adulto si commuove.

**Sigillo del narratore.** Da scrivere in D con la penna più sottile della saga. **Quattro funzioni insieme:**

1. **Chiude il giorno** (sono al Forno, mangeranno, dormiranno).
2. **Chiude l'anno** (la prima brina arriva domani, Fiamma lo sa).
3. **Lascia aperta la paura di Gabriel** (le briciole + le fette uguali di S9 + il braccialetto al polso = il fratello maggiore continua a occuparsi del piccolo, anche se il piccolo non è più piccolo come prima).
4. **Lascia aperta la porta verso quello che c'è oltre il mare** (può essere un'immagine: fuori dal Forno, nel buio della Piazza, Bartolo non si vede ma c'è — il suo Pontile è là, il mare è là, Bartolo dorme nella barca).

**Vincoli sul sigillo:**
- Una frase, due al massimo. Non di più.
- Non una morale.
- Non un *"E così finì l'anno"* esplicito.
- Tono: simmetrico all'apertura saga (S1 frase-firma narratore). Se in S1 il narratore ha aperto un patto di lettura, in S12 lo chiude — restituendo qualcosa al lettore, non spiegandogli.

Direzione di lavoro per Fase D: **qualcosa che parta dall'idea che l'isola, di notte, dorme con tutti dentro** — i tre fratelli al Forno, Bartolo nella barca, Grunto nella grotta, Mèmolo nella casetta tonda, Stria in casa propria, le Vecchie del Mercato a casa loro — **e che il narratore restituisca al lettore il fatto di essere stato con loro per un anno.** Senza dirlo esattamente così.

**Frase-chiave indicativa.** **Nessuna**. La storia chiude senza frase-chiave puntuale — è il sigillo del narratore a chiudere, non una frase di personaggio o un detto popolare. Eccezionalità sostanziale per la storia di chiusura saga.

**Semi ripresi (tutti).**
- **Pagnotta a Grunto** (S1) → bloom totale, simmetria di apertura/chiusura saga.
- **Grunto** (S1) → bloom strato 3, frammento pre-Vento unico.
- **Quando l'acqua trema** (S8) → 2° e ultimo, chiude installazione.
- **Radura coi pini** (S5) → ricorre in passaggio, autunnale.
- **Bartolo modo** (S7, S10, S11) → ricorre, mano alzata che ricade.
- **Liù mestiere** (S6, S8, S9 ipotizzato) → ricorre.
- **Pattern A** → cresce sotto, mai dichiarato.
- **Mani dei fratelli che si toccano in silenzio** (eredita gesto-tipo della saga: TUM-tum-TUM S4, fette uguali S9, le mani sulla terra in S12 — variante finale).
- **Le fette uguali** (S9) → eco silenziosa nel gesto di Fiamma di tagliare quattro fette.
- **Braccialetto** (S9) → al polso di Gabriel, mai descritto.
- **Forno come cornice di apertura+chiusura saga** → simmetria S1 ↔ S12.

**Semi piantati per Fase F.**
- **Frammento pre-Vento di Grunto** → strato 3 aperto (chi è il narratore? cosa vuol dire *visto / respirato*?).
- **Frutti da fuori di Bartolo** (S11) → strato 3 aperto, *oltre il mare*.
- **Paura di Gabriel non risolta** → strato 3 aperto, candidato per saga futura fascia ragazzi.
- **Sguardo lungo di Fiamma a Gabriel mentre escono** (S12 inizio) → micro-seme: Fiamma sa qualcosa che Gabriel sta vivendo.
- **Il narratore-iniziato che ha sigillato l'anno** → il rivelarsi è in Fase F, ma il rilettore qui sente che *c'è qualcuno che racconta da una postura precisa*.

**Paura toccata.** **Gabriel — accolta**, non risolta. Modo: **tenere**.

**Abitanti in scena.**
- **Liù** (cammeo apertura, *frrr*, una frase: *"Oggi suonano. Andate?"*). Ruolo: portatrice di notizie.
- **Fiamma** (cornice apertura+chiusura saga, modalità ferma — pagnotta + sguardo lungo a Gabriel; sera: dolce normale + *"Sedete"* + *"Domani brina"*). Ruolo: madre-calore (cornice di apertura saga e chiusura saga, simmetria S1 ↔ S12).
- **Bartolo** (cammeo Pontile mattino, mano alzata che ricade; nel sigillo finale: presenza nella barca implicita, mai mostrata). Ruolo: nonno silenzioso.
- **Grunto** (Burrone, sua scena unica). Ruolo: altro-da-famiglia. **Frammento pre-Vento — l'unico in saga.**
- **Coltivatori, Pastori** (sfondo nelle tappe, brevissimi).

**Cammei totali ridotti.** Coerente con la natura della storia: meno chiacchiera del villaggio, più cammino e percezione. La saga si chiude col mondo che si fa silenzioso intorno ai tre.

**Palette emotiva.** Mattina: prima brina su erba autunnale, sole basso, arancione del Forno, bianco del fiato. Cammino: colori dell'autunno tardo (giallo-bruno, foglie cadute, fiume scuro). Burrone: verde scuro del lichene + verde di Grunto + grigio della pietra + cicatrice chiara di Grunto. Roccia Alta: vista totale dell'isola con tutti i colori dei quattro quartieri visibili dall'alto. Concerto: aria che si fa *vibrante*, colori che si scaldano insieme, vento che porta odori. Sera al ritorno: blu profondo del crepuscolo + tutta l'isola che torna calma + fumo dei camini di sotto. Forno-cornice finale: candela calda, dolce, tazze fumanti, sagome dei fratelli e di Fiamma intorno al tavolo.

**Callback.** Tutti i principali della saga, in cornice di chiusura.

**Note voce.** **Frase-firma narratore esplicita** (1 di ≤2 saga, l'altra in S1). **Frammento pre-Vento Grunto** (1 di ≤2 saga — qui l'unico). **Address al lettore** (1 di ≤6, ultimo della saga). **Quando l'acqua trema** (2° di ≤2 saga). Nessuna onomatopea-oggetto. Nessuna cantilena Coltivatori (chiusa in S10). TUM-tum-TUM dei fratelli — non in scena, ma il gesto delle mani sulla terra è la sua eco silenziosa. Memoria lunga del narratore: 3-4 incisi sparsi sul cammino e sull'isola intera.

---

## §5. SEMI E CALLBACK — TRACCIATO TRASVERSALE

Tabella sinottica dei semi piantati, ripresi e bloomati attraverso la saga. Versione preliminare di pre-grafo per Fase B3.

### §5.1 Oggetti, gesti, capacità

| Seme/elemento | Origine | Ricorrenze | Bloom finale |
|---|---|---|---|
| **Pagnotta a Grunto** (rito Fiamma↔Grunto) | S1 | — | S12 (chiusura simmetria) |
| **Bastoncino di Noah** (raccolto camminando) | S1 (en passant, una sola volta) | S2 (cade nella pozza, oggetto-fantasma congelato), S6 (gesto-firma istituito), S7 (variante: bastoncino-strumento per zattera) | gesto-firma diffuso |
| **TUM-tum-TUM** (codice dei tre fratelli) | S4 | — | S12 (eco silenziosa nelle mani sulla terra) |
| **Nodo Marinaro** (capacità di Elias) | S5 (insegnato da Nodo) | S7 (zattera, regge), S8 (crisi reale, regge) | S11 (festa, corda intrecciata) |
| **Foglie/rami caduti come materia** (Pattern A) | S5 (rami → ponte) | S6 (cosa "perduta" non è persa), S7 (zattera rotta arriva), S8 (noce caduto → cataste legna), S10 (nido vuoto → pieno), S11 (festa che non si vince), S12 (anno chiuso, fratelli diversi insieme) | Pattern A trasversale, mai dichiarato |
| **Pallone di stoffa cucita** | S3 | — | S11 (festa, eventuale ricomparsa giochi cuccioli) |
| **Nido vuoto curato da Noah** | S8 | S10 (oggetto di transizione verso il buio) | chiuso in S10 (resta sul comodino, non torna in S12) |
| **Braccialetto di Noah a Gabriel** | S9 (sul tavolo, non indossato) | — | S12 (al polso di Gabriel, mai descritto) |
| **Pomo che rotola / paronomastico** | S6 candidato + S11 | — | 2 di ≤2 saga |
| **Le fette uguali** (Gabriel taglia) | S9 | — | S12 (eco silenziosa nelle quattro fette del dolce di Fiamma) |
| **Coni di Stria con ghiande dipinte** | S11 (4 a Elias intenzionali) | — | gesto annuale di Stria (istituito) |
| **Frutti da fuori di Bartolo** | S11 | S12 (Bartolo nella barca, implicito, oltre-il-mare) | porta socchiusa Fase F |

### §5.2 Personaggi e relazioni

| Relazione/figura | Semina | Sviluppo | Bloom |
|---|---|---|---|
| **Bru** (presenza minimale che custodisce) | S3 (intravisto) | S4 (presenza concreta), S5 (compagno scoperta) | S11 (riconosciuto da Elias come quello-solo, porta a Rovo) |
| **Rovo** (zio severo, doppio registro) | S3 (guardiano confine) | S4 (abitante Foresta, registro diverso) | S11 (assente, segnato via Bru) |
| **Mèmolo + Pun** (paternità muta) | S6 (dente da latte, frase precisa) | S8 (Gabriel lo accudisce, frase precisa) | S11 (cammeo) |
| **Vecchie del Mercato** (indicare in silenzio) | S6 (firma istituita) | S8 (cammeo) | S11 (gesto cruciale per Elias) |
| **Stria che vede prima** | S2 (*"Tu cosa pensi?"*), S6 (sente Pun, una frase) | S9 (*"Tu cosa farai oggi che hai un anno in più?"*) | S11 (quattro coni a Elias intenzionali — sa) |
| **Bartolo che vede e basta** | S7 (modo istituito) | S10 (notte, zero parole) | S11 (porta frutti da fuori, *fa*) — S12 (mano che ricade, presenza implicita) |
| **Cuccioli con voci individuali** | S6 (collettivo) | S9 (Cardo prima volta voce) | S11 (gruppo distribuito) |
| **Grunto** (testimone unico) | S1 (incontro vero, *"Buono"*, zero frammenti) | S10 (presenza acustica notturna) | S12 (frammento pre-Vento unico saga) |
| **Liù mestiere informale** | S6 (*frrr*, prima volta) | S8 (annuncio fenomeno raro come ipotesi), S9 (vola al Forno con la notizia, ipotesi D) | S12 (apertura saga: *"Oggi suonano. Andate?"*) |

### §5.3 Mondo (fenomeni e luoghi)

| Elemento del mondo | Prima apparizione | Ricorrenze | Stato |
|---|---|---|---|
| **Quando l'acqua trema** (Fiume controcorrente) | S8 (1ª, Liù lo annuncia come ipotesi) | — | S12 (2ª e ultima, vista al guado nord) — quota ≤2 chiusa |
| **Il Concerto** (Tre Venti insieme) | S12 (Liù prima a chiamarlo *suonano*) | — | nominato e installato — **da aggiungere a Glossario in aggiornamento Fase D** |
| **Radura coi pini** | S5 (scoperta) | — | S12 (passaggio autunnale verso Roccia Alta) |
| **Foresta che ha tempi/modi propri** | S3 (*"hanno il loro orario"*) | S4 (radici come modo) | S5 (ponte come modo) |
| **Mappa intera dell'isola attraversata** | S6 (1ª volta giro completo) | S11 (1ª volta isola in attivazione collettiva) | S12 (ultima volta, verticale e contemplativo) |
| **Pontile come ricetto notturno** | S10 (Bartolo zero parole) | S12 (cammeo passaggio) | implicito Fase F |

### §5.4 Paure dei fratelli — traiettoria saga

| Fratello | Paura | Semina | Emergenza | Risoluzione/Modo |
|---|---|---|---|---|
| **Noah** | Buio | S1 (disagio bianco totale, implicita), S3 (sentore Foresta sera, implicita) | S8 (nido vuoto come proto-gesto cura) | **S10 — RISOLTA — modo: dire** |
| **Elias** | Non essere abbastanza ("piccolo" / "in mezzo") | S2 (*"piccolo"* nel riflesso) | Micro-sguardi distribuiti S4, S5, S6, S9 (variante) | **S11 — RISOLTA — modo: accettare** |
| **Gabriel** | Cresceranno diversi | Micro-occhiate S7, S8 | S9 (emerge — fette uguali, sorriso commosso) | **S12 — ACCOLTA, non risolta — modo: tenere** |

**Terna strato 3 architrave saga:** *dire / accettare / tenere*.

---

## §6. STRUTTURA GENERALE — RIEPILOGO

### §6.1 I quattro blocchi

| Blocco | Storie | Ciclo | Stagione | Movimento del fratello-nucleo | Pattern A |
|---|---|---|---|---|---|
| A | 1-3 | Δ Distinguere | Inverno + passaggio | Gabriel come guida naturale (fermarsi) | non ancora seminato |
| B | 4-6 | ⇄ Connettere | Primavera + passaggio | Elias come ponte fisico (tenere, costruire, capire) | seminato in S6 |
| C | 7-9 | ⟳ Cambiare | Estate + passaggio | Gabriel comincia a sentire crescere i fratelli | scena attiva S7-S8, *"qua l'acqua trema"* |
| D | 10-12 | Integrato | Autunno + passaggio (anno chiuso) | Tutti e tre nelle proprie paure | bloom silente, mai dichiarato |

### §6.2 Movimento Δ → ⇄ → ⟳ → integrato

- **Δ (A)**: imparare a vedere i confini, fermarsi quando non si distingue.
- **⇄ (B)**: imparare a costruire e percepire connessioni — invisibili (radici), fatte (ponte), tessute (rete di abitanti).
- **⟳ (C)**: imparare a stare nel cambiamento — cose che si rompono e arrivano lo stesso, fratelli che crescono.
- **Integrato (D)**: stare nelle proprie paure (dire / accettare / tenere) — non superarle, attraversarle.

### §6.3 Ciclo annuale

12 storie = 1 anno. Sfasamento stagionale: i 4 cicli EAR sono sfasati di una storia rispetto alle stagioni, in modo che il cambio di ciclo non coincida col cambio di stagione (mandala silenzioso temporale, Bible §8.7).

### §6.4 Quattro tempi del giorno presenti nella saga

- **Alba** (Taglio) — S1 (risoluzione), S6 (partenza), S10 (risoluzione), S12 (mattino partenza).
- **Giorno** (Intreccio) — S4 (Foresta), S5 (ponte), S6 (giro), S7 (cammino lungo Fiume), S11 (festa), S12 (cammino).
- **Sera** (Mulinello) — S3 (assenza Taglio, Mulinello in arrivo), S8 (Mulinello forte), S9 (Mulinello calmo), S11 (rientro festa), S12 (Concerto sera).
- **Notte** (i tre venti dormono) — S1 (parziale Pascoli), S8 (notte ferma in mezzo), **S10 (notte intera, scena piena)**, S12 (passaggio crepuscolare).

---

## §7. COSA RESTA DOPO S12

Note per Fase D e Fase F.

### §7.1 Per Fase D (scrittura)

**Temperatura di scrittura per blocco:**
- A: aria fredda, gesti pratici, dialoghi con un sotto-tono di scoperta.
- B: aria che si scalda, dialoghi più presenti, costruzione visibile.
- C: temperatura più meditativa, sguardi che pesano, parole più rade.
- D: temperatura asciutta, camminate più lente, gesti silenziosi, sigilli sobri.

**Pattern A** vive nelle immagini e nei sigilli del narratore. **Mai nominato.** Le frasi-chiave dei personaggi non lo dichiarano. Quando il narratore chiude una storia, lavora con immagini che lo onorano.

**Drammaturgia silenziosa degli sguardi** installata nel blocco C (Gabriel-Noah-Elias che si guardano in modi che il bambino di 4 non vede). Si propaga nel blocco D. **Bambini di 9 anni rileggono e li trovano.**

### §7.2 Per Fase E (illustrazioni)

**Firme visive** dei personaggi (Bible §4) da rispettare in ogni tavola.

**Oggetti-simbolo dei gruppi** (carriola di vimini Camminanti, zappa col manico curvo Coltivatori, scala a pioli Mantenitori) — riconoscimento visivo a colpo d'occhio.

**Grunto verde** che si confonde col lichene (Bible §4.8) — palette specifica per Burrone S1 e S12.

**Numero alberi della radura S5** non specificato nel testo — illustrazione libera (suggerito tre, eco silenziosa fratelli).

**Braccialetto S9 → S12** brutto-tenero, mai disastrato, evidentemente fatto da Noah. Visibile nelle tavole rilevanti senza enfasi.

### §7.3 Porte socchiuse — Fase F

L'isola dopo S12 resta viva. Il narratore non chiude l'isola, chiude l'anno. Promesse aperte:

- *Cosa c'è oltre il mare?* (Bartolo che traghetta verso fuori, frutti da fuori in S11)
- *Chi è il narratore?* (postura installata nelle frasi-firma S1 e S12, mai rivelato)
- *Cosa vuol dire visto / respirato?* (frammento pre-Vento Grunto S12)
- *Cresceranno davvero diversi i fratelli?* (paura di Gabriel non risolta, accolta)
- *Storia di Bru* (perché sta con Rovo)
- *Cicatrice di Grunto* (mai spiegata)
- *Chi sono i genitori dei fratelli* (assenti, ruolo distribuito)

**Tutte queste porte sono aperte per Fase F (Storia 13 e/o libro separato fascia 10-13).** Mai preannunciate nel testo della saga (vincolo Carta §3.7).

---

## §8. COLLEGAMENTI A FASE B3 (prossima chat)

Materiale grezzo già presente in questo file, da formalizzare in Fase B3:

- **STORY_GRAPH_v1.json** (o equivalente): grafo narrativo dei semi/callback (vedi §5).
- **QUOTE_TRACKER.md**: tracciamento operativo delle quote rare (frammenti Grunto, detti Fiamma, address al lettore, frase-firma narratore, paronomastici, cantilene Coltivatori, TOK-TOK Nodo, piante Salvia, fenomeni rari, scene notturne).

Questioni aperte da risolvere in B3:
- **Messaggio di Stria ai Pastori in S2**: consegna off-screen breve oppure non-consegna esplicita con conseguenze in storia futura?
- **Quattro coni di Stria a Elias in S11**: confermata l'intenzionalità (non errore) — da scrivere in D con consegna leggermente più lunga, sguardo mezzo secondo in più, mai commentato.
- **Frase precisa di Mèmolo in S11**: opzionale, da decidere se inserirla o saltarla per non saturare la storia di "frasi precise" (vincolo §4.7).
- **Liù vola al Forno con notizia S9 prima dei fratelli**: ipotesi da decidere D.
- **TOK-TOK in S12**: implicito o no, da decidere D.
- **Glossario**: aggiungere *Il Concerto* in aggiornamento Fase D.

---

## §9. CHANGELOG

### v1.0 (2026-04-21) — Fase B2

Versione iniziale del file. Mappa completa dei 12 archi narrativi con decisioni architetturali del Blocco 0 + Blocco A (S1-3) + Blocco B (S4-6) + Blocco C (S7-9) + Blocco D (S10-12). Pattern A riconosciuto come famiglia di immagini ricorrente da onorare nelle chiusure di blocco. Terna strato 3 *dire/accettare/tenere* identificata. Sfasamento stagionale Bible §8.7 mappato su tutte le storie. Cast distribuito secondo quote Bible §4.2. Ruoli familiari episodici distribuiti senza ripetizioni di fila. Momenti rari (frammenti Grunto, address al lettore, frasi-firma narratore, paronomastici, cantilene, fenomeno *quando l'acqua trema*, scene notturne) tutti dentro le quote previste.

`STORIE_SCHEMA_v1_1.md` superseded da questo file per la mappa archi. Resta come riferimento storico.

---

#END

*Δ ⇄ ⟳ — l'isola li ha tutti, il bambino non li sa, il rilettore li sente.*
