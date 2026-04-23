# Checkpoint — sessione 2026-04-23

Snapshot del progetto alla fine della prima sessione di lavoro. Serve come
punto d'appoggio per riprendere: cosa esiste, perché, cosa manca, e
consigli di ricerca per il prossimo salto di qualità.

**Ultimo commit di sessione**: `6e2f032`
**Live su**: https://isola-nk6b.vercel.app
**CI**: GitHub Actions verde su `main`

---

## Cosa esiste oggi

### `content/` — sorgente narrativa canonica
Tutta la bibbia del mondo (docs, worldbuilding, architettura, framework,
grafo narrativo, b3_0_5). **Immutabile da questo lato**: si modifica solo
tramite il lavoro narrativo. Tutto il resto del repo ne deriva.

### `world/` — dati derivati, canonici, rigenerabili
- **18 schede personaggio** in MD+YAML (3 avatar + 5 primari + 1 testimone
  + 4 secondari + 5 cuccioli), generati da `tools/build_world.py` a partire
  da `content/`. Deterministici.
- **27 location canoniche** (`world/geography/locations.json`) con
  coordinate in metri, origine Albero Vecchio, convenzione Three.js.
- **Rete sentieri** (`world/geography/paths.json`) con `canonical_time_min`
  estratti dalla bibbia §8.1 per tempi fedeli al canone.
- **Features canoniche** (`world/geography/features.json`): fiume ad
  anello (15 waypoints), foresta, spiaggia, orti concentrici, cluster
  villaggio, pascoli alti, vette gemelle.
- **Profili terreno per quartiere** + 13 anchor points di elevazione
  (`world/geography/terrain.json`).
- **`world/_index.json`**: indice flat consumato dalla web app.

### `tools/` — pipeline Python interrogabile
- `build_world.py` — parser deterministico content/ → world/schede
- `geography.py` — API IslandGeography: `distance`, `walking_time`,
  `path` (Dijkstra), `nearby`, `quartiere_of`, `elevation`,
  `visible_from`, `features`, `terrain_profile`, `anchor_points`,
  `distance_to_river`
- `geo_query.py` — CLI per query rapide (`python -m tools.geo_query ...`)
- `tests/` — **116 test** (pytest/unittest), 0.15s di esecuzione
- `tests/test_parity.py` — verifica parità numerica Python ↔ TypeScript

### `web/` — Next.js 16 + R3F PWA
- Scena 3D navigabile con camera Google Earth (drag/pinch/tilt)
- Terreno anchor-based (IDW + light noise), amplificazione rilievo 2.5×
  solo in rendering
- 5 zone di colore distinte per quartiere, blend gaussiano
- Fiume ad anello visibile con sorgente alle Montagne e foce alla Bocca
- 2 Montagne Gemelle come picchi separati con snow-cap
- 1 tile renderizzato a L1 (Forno): building con camino, Casa del Mattino,
  catasta, alberi, finestre che flickerano
- Ambient breathing: fumo dal Forno, nuvola sulle Montagne, spighe Orti
- Interazione: tap-and-hold 0.5s → descent; dwell su location → nome in
  Caveat; swipe-down 2-finger → ascent
- Finger presence (Tearaway-inspired): alone crema sotto il dito
- PWA installabile, offline-capable, service worker custom
- Build pulito, lint pulito, CI verde

### `assets/` — materiale visivo di riferimento
Immagini generate con Grok Imagine durante la ricerca di identità visiva.
**Non asset principali**, sono reference di mood.

### `legacy/` — prototipi
`index.html` statico preservato come reference.

---

## Architettura — decisioni portanti

1. **Content source → World derived → Web consumer**.
   `content/` è sorgente narrativa, toccato solo dal lavoro narrativo.
   `world/` è derivato da `content/` tramite pipeline deterministica.
   `web/` legge solo da `world/`. Flusso mono-direzionale, zero drift.
2. **Immagini senza testo**. I diffusion model non scrivono italiano
   affidabile. Regola di ferro: mai testo nelle immagini. Nomi sono layer
   SVG/HTML in overlay, controllabili, multilingua gratis.
3. **Modulo geografia interrogabile**. Stessa API in Python (narrativa) e
   TypeScript (web). Un AI autore può chiamare `geo.walking_time()`
   invece di avere la bibbia intera in context.
4. **Architettura tile**. Ogni quartiere è un componente React
   indipendente che consuma `world/geography/`. Rifare un tile = zero
   regressioni sugli altri. Sostituire BoxGeometry con .glb Blender =
   cambio locale.
5. **Coordinate sistema Three.js**. Origine Albero Vecchio, est=+x,
   sud=+z, su=+y. Unità JSON in metri, scena scala 1u = 100m.
6. **Tempi canonici over mechanical**. `paths.json` ha
   `canonical_time_min` per archi dove la bibbia dichiara un tempo.
   Fallback mechanical con difficulty multiplier dove tace.
7. **Determinismo in ogni pipeline**. Seed fissi, JSON sort_keys=True,
   YAML ordinato, iterazioni su sorted(). Build uguale a ogni rerun.
8. **Modularità prima di bellezza**. Ogni layer swappabile senza
   riscrivere il resto. Costo up-front 20-30%, payoff enorme a lungo
   termine.

---

## Principi non negoziabili (dal canone)

Vincoli che valgono SOPRA qualsiasi scelta tecnica:

- **Framework EAR invisibile** (Δ / ⇄ / ⟳): mai in UI, mai in metadati
  user-facing, mai in prompt di generazione immagini.
- **Nessuna morale esplicita**, nessun personaggio che spiega il
  significato.
- **Mandala silenzioso**: i 4 quartieri cardinali NON si chiamano
  "Fuoco/Acqua/Terra/Aria" user-facing. Si chiamano per landmark ("del
  Forno", "del Pontile", "degli Orti", "delle Montagne").
- **Notte non personificata**: la notte è ambiente, non agente.
- **Nominazione operativa**: rispettare il canone (Albero Vecchio, Fiume
  che Gira, ecc.).
- **Pattern A mai nominato**.
- **Detti popolari esclusivi di Fiamma**.

Elenco completo in `content/README.md` §Principi non negoziabili.

---

## Todo aperti

### Alta priorità (narrativa + base funzionale)
- [ ] **Altri 4 tile**: Pontile, Orti, Montagne, Centro (il più complesso)
- [ ] **Character presence**: tap su un luogo → il personaggio che ci vive
  fa qualcosa di discreto (non un popup)
- [ ] **Interazione "il mondo avvolge"**: meccaniche oltre il dwell-name,
  per far sentire immersione al tap. Discussione in sessione, da
  prototipare.

### Media priorità (qualità esperienza)
- [ ] **Ground-level view**: scendere dentro un quartiere, camera a
  livello persona, guardarsi intorno. Grossa feature.
- [ ] **Polish gesti**: validare che swipe-down 2-finger sia intuitivo
  per bambini, altrimenti ripensare (tap-on-edge? long-press?)
- [ ] **PinchOutHint aggiornato** col gesto swipe-down (se non già fatto)
- [ ] **Estetica**: il terreno è leggibile ma grezzo. Painterly
  shader/post-processing (vedi consigli sotto)

### Bassa priorità (nice to have)
- [ ] **Authoring mode in 3D**: drag-drop in scena che scrive su
  world/geography/ (oggi si edita a mano)
- [ ] **Audio ambient**: vento, mare, forno, sentieri. Registrato ad hoc
  (come da tua scelta).
- [ ] **Time of day**: alba/mezzogiorno/tramonto/notte, con i 3 venti
  canonici che hanno orari dichiarati
- [ ] **Narratore whisper**: 1 frase breve quando entri in un luogo,
  in voice-over Ray o Caveat text

### Tecniche (debito/manutenzione)
- [ ] Character names/voci in bibbia che affiorano durante dwell (oggi
  solo nome location)
- [ ] Migrazione eventuale a `@react-spring/three` per animazioni più
  complesse (ora lerp manuale)
- [ ] Test E2E Playwright per gesture mobile (oggi solo unit test backend)

---

## Known issues

1. **Swipe-down 2-finger**: nuovo gesto, non ancora testato a lungo. Se
   non intuitivo, sostituire con altra meccanica.
2. **Nuvola sulle Montagne**: è stata sostituita con 3 sfere, ma ancora
   appare "bianca opaca" invece che soffice. Migliorare con additive
   blending o particelle.
3. **Font size nome dwell**: ora 40px, da testare a lungo.
4. **Stile misto nei tile**: solo il Forno ha dettaglio L1. Gli altri 4
   quartieri restano zone di colore piatte quando ci entri.

---

## Consigli di ricerca

Per il "lavoro strato per strato" che hai in mente. Ordinati per impatto
visivo / costo di implementazione.

### Rendering painterly/toon (alto impatto, basso costo)

Il cambio più grosso per la minor quantità di codice. Trasforma "low-poly
grezzo" in "libro illustrato".

- **Three.js `MeshToonMaterial`**: materiale cartoon shading built-in.
  5 righe di codice.
- **Postprocessing**: libreria `postprocessing` (di vanruesc) con
  `OutlineEffect`, `BloomEffect`, `DepthOfFieldEffect`. Applichi un pass
  globale, cambia tutto.
- **EffectComposer** di Three ufficiale per `OutlinePass`.
- **Riferimenti visivi da studiare**:
  - *A Short Hike* (2019): low-poly flat-shaded + outline + post-process.
    Il target estetico più vicino a noi.
  - *Sable* (2021): flat-shaded + outline + palette ristretta. Simile ma
    più adulto.
  - *Genshin Impact*: cel-shader molto complesso, ma i trucchi di base
    sono replicabili in Three.
  - *Monument Valley*: non 3D ma la direzione cromatica e la geometria
    iconica sono lezione.
- **Search terms**: "three.js toon shader tutorial", "three.js outline
  postprocessing", "stylized webgl low poly"

### Asset pipeline con tool esterno (medio impatto, medio costo)

Smettere di generare geometria in .tsx e iniziare a modellare a mano.

- **Blender** (free, open source). Per questo livello di complessità
  (case, alberi, oggetti-simbolo) 1-2 settimane di apprendimento bastano.
- **Export glTF/glb** è standard industriale. Si carica in R3F con
  `useGLTF` di Drei.
- **Asset gratuiti di placeholder**:
  - [Kenney](https://kenney.nl/assets) — tutto free, ottimo per
    prototipo low-poly
  - [Poly Pizza](https://poly.pizza) — low-poly free
  - [Quaternius](https://quaternius.com) — ultra-low-poly
- **Workflow**: modelli il Forno in Blender una volta, esporti .glb,
  carichi nel componente `QuartiereForno`. Se cambi l'asset Blender,
  basta ri-esportare.
- **Search terms**: "blender low poly cottage tutorial", "r3f useGLTF
  tutorial", "gltf transform compression"

### Terreno da tool dedicato (alto impatto, alto costo setup)

Se vuoi che il terreno sembri vero e non geometrico.

- **Gaea** (freemium, tier free è decente): produce heightmap procedurali
  fantasy painterly. Esporti PNG, lo carichi come displacement map in R3F.
- **World Creator** (commerciale, ma power tool)
- **WorldMachine** (più vecchio, molto usato)
- **In alternativa, GIS open source**: QGIS con plugin per heightmap.
- **Workflow**: generi heightmap 2048×2048 in Gaea → PNG →
  `<planeGeometry>` con `displacementMap` in R3F. Molto più fedele delle
  nostre interpolazioni IDW.
- **Search terms**: "three.js heightmap displacement map", "gaea world
  machine heightmap"

### Interaction design per bambini (formativo)

Per sostanziare l'idea "il mondo avvolge al tap" che abbiamo lasciato
aperta.

- **Video di gameplay analizzati in Studio**: guarda in slow-motion le
  reazioni visive di queste app:
  - Nosy Crow "Little Red Riding Hood" (iOS/Android)
  - Toca Life World (loop qualsiasi)
  - Amanita Design "Samorost 3" (PC/mobile)
  - Tearaway (PS Vita gameplay su YouTube)
- **Libri**:
  - *"The Art of Game Design: A Book of Lenses"* — Jesse Schell
  - *"Designing Games for Children"* — Carla Fisher
  - *"A Theory of Fun for Game Design"* — Raph Koster
- **Principi da appuntarsi**: feedback immediato, reversibilità zero
  stakes, exploration reward (non goal), piccoli rituali ripetibili.

### Performance mobile 3D (importante, tecnico)

Per tenere la PWA fluida quando cresce di contenuti.

- **Spector.js**: Chrome extension per profilare draw call e stato WebGL
- **Lighthouse**: verifica PWA compliance e performance budget
- **Compressioni**:
  - **Draco** per mesh compression
  - **KTX2** per texture (supporto Basis Universal)
  - **glTF Transform CLI** per ottimizzare .glb
- **Instancing**: per ripetere alberi/rocce senza moltiplicare draw call,
  usa `InstancedMesh` (Three) o `Instances` di Drei
- **LOD**: tile distanti hanno versione low-poly, vicini alta
- **Search terms**: "r3f performance tips", "three.js instancing tutorial",
  "gltf transform compression"

### Se vuoi andare oltre Next.js/R3F

Quando questo stack mostra il limite (improbabile nei prossimi 6 mesi):

- **Babylon.js**: more batteries included per meccaniche di gioco
  (navmesh, physics)
- **PlayCanvas**: engine web-first, editor visuale, buono per team non
  dev-only
- **Godot HTML5 export**: motore di gioco completo se serve davvero
- **Unity WebGL**: pesante ma maturo, va pensato per mobile 3D
- **Unreal Engine 5 Pixel Streaming**: remote rendering, overkill per ora

Il nostro stack attuale reggerà per altri round. Non cambiare prima che
mostri un sintomo reale.

---

## Come riprendere in una nuova sessione

Quando apri una nuova chat di sviluppo:

1. **Context starter**: "Sto lavorando su `/home/user/Isola`, repo del
   mondo interattivo online de L'Isola dei Tre Venti. Ultimo commit:
   `6e2f032`. Leggi `CHECKPOINT.md` (questo file) e `README.md` per
   orientarti. Poi dimmi lo stato e cosa proporresti."
2. **File chiave da leggere per entrare nel contesto**:
   - `CHECKPOINT.md` (questo)
   - `README.md` (repo orientation)
   - `content/README.md` (principi non negoziabili del progetto
     narrativo)
   - `world/README.md` (come è fatto lo strato derivato)
   - `tools/README.md` (pipeline + CLI geografia)
3. **Comandi utili**:
   - Test Python: `python -m unittest discover -s tools/tests -v`
   - Query geografia: `python -m tools.geo_query path pontile_di_bartolo grotta_di_grunto`
   - Web dev: `cd web && npm run dev`
   - Web build: `cd web && npm run lint && npm run build`
   - Deploy: automatico su push a `main` (Vercel)
4. **Quando lanciare un agent vs lavoro diretto**:
   - Agent in background: task deterministici pesanti (pipeline,
     scaffolding, refactor coordinati). Mantieni context tuo leggero.
   - Lavoro diretto: design, decisioni, piccoli fix mirati, debug.
5. **Pattern di sessione che ha funzionato bene**: discutere prima di
   scrivere, decidere 2-3 cose concrete, delegare all'agent, verificare
   sul telefono, iterare.

---

## Ringraziamenti / note per te

- Hai condotto bene. Le scelte chiave (modularità, tile-based, tempi
  canonici, wordless) sono state tue — io ho solo tradotto in tecnica.
- Il "brutto ma c'è" di fine giornata è sano: significa che la fondazione
  regge e che ora puoi alzare la qualità iterando.
- Non esagerare con i tool nuovi tutti insieme. Blender + painterly
  shader + heightmap tool tutti a cascata ti bruciano. **Uno alla
  volta**, uno per sessione, verificando il payoff.
- Riposa la testa. I progetti ricchi come questo premiano il ritorno
  con occhi freschi.
