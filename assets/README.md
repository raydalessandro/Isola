# assets/ — riferimenti visivi

Materiale visivo del mondo. Immagini generate con Grok Imagine, **senza
testo dentro**. I nomi dei luoghi saranno un layer SVG nella web app.

## Stato attuale (L0–L1 coperti)

### `map/`
- `paper-base.jpg` — L0a: pergamena + oceano + isola silhouette vuota.
  Sfondo per assemblare i tile dei quartieri.
- `island-master.jpg` — L0b: vista complessiva dell'isola con tutti i
  landmark principali (montagne gemelle, orti, villaggio centrale con
  albero, forno, pontile, cottage, barche). Nessun testo. Stile
  illustrato hand-drawn con inchiostro + acquerello caldo.

### `quartieri/` (tile L1)
- `centro.jpg` — villaggio centrale: Albero Vecchio, Pozzo, Panca di
  Pietra con riccio+tasso, volpe-Fiamma, cormorano-Amo, picchio-Nodo in
  bottega, airone-Stria, scoiattolo, carriola dei Camminanti. **Stile
  illustrato** (acquerello + inchiostro marrone), coerente con
  `island-master.jpg`.
- `forno.jpg` — forno di Fiamma al tramonto, volpe che inforna, camino
  fumante, catasta legna, Casa del Mattino in lontananza. **Stile
  cinematic/3D**, diverso da centro+master.
- `pontile.jpg` — pontile di Bartolo, tartaruga sulla spiaggia,
  cormorano sulla casetta, capanna a palafitta, barche, conchiglie.
  **Stile cinematic/3D**.
- `orti.jpg` — Orti del Cerchio concentrici, due casa-tana tipo burrow,
  alberi in fiore, contadini al centro. **Stile cinematic/3D**.
- `montagne.jpg` — Montagne Gemelle al tramonto, airone-Stria sulla
  scogliera, pecore sui Pascoli Alti, grotta, sentiero. **Stile
  cinematic/3D**.

### `drafts/`
Materiale di lavoro, non asset definitivi.

- `atlante-isola-landscape.png` — primo master map in landscape con testo
  inglese/italiano misto. Superseduto da `map/island-master.jpg`, ma
  utile come reference di contenuto (ha più dettagli esplicitati).
- `centro-cartoon-alt.jpg` — versione alternativa del villaggio in stile
  cartoon/Disney. Scartata: non coerente con master illustrato né con
  cinematic dei quartieri.
- `master-v2-attempts/tentativo-01..03.jpg` — 3 tentativi di master
  portrait con testo (fallito). Utili come reference di style.

## Nota aperta — coerenza stilistica

Le immagini attuali sono in **tre stili diversi**:
- **Stile A (illustrato hand-drawn)**: `island-master.jpg`,
  `quartieri/centro.jpg`. Acquerello + inchiostro marrone, children's
  book tradizione europea.
- **Stile B (cartoon)**: `drafts/centro-cartoon-alt.jpg`. Non usato.
- **Stile C (cinematic/3D)**: `quartieri/forno|pontile|orti|montagne.jpg`.
  Quasi fotorealistici, cinematografici, molto evocativi ma di
  "linguaggio" diverso da master.

Stile A e C sono entrambi belli ma non parlano la stessa lingua. Questa è
una decisione aperta: tenere tutto in A, tutto in C, o scegliere un ibrido.
Vedi discussione in conversazione.

## Architettura tile (adottata)

Decisione: le immagini sono **paesaggio dipinto senza testo**. I nomi dei
luoghi, i label, gli hotspot interattivi sono **un layer SVG sopra
l'immagine** nella web app, con font Caveat (già caricato in `index.html`).

Vantaggi: nomi sempre corretti, multilingua gratis, immagini rigenerabili
senza rompere nulla, interattività nativa.

### Struttura assets prevista

```
assets/
├── map/
│   ├── paper-base.jpg              ← L0a: pergamena + oceano, isola vuota  ✓
│   └── island-master.jpg           ← L0b: vista complessiva isola          ✓
├── quartieri/                      ← L1: 5 tile (stile da armonizzare)     ✓
│   ├── centro.jpg                                                          ✓
│   ├── forno.jpg                                                           ✓
│   ├── pontile.jpg                                                         ✓
│   ├── orti.jpg                                                            ✓
│   └── montagne.jpg                                                        ✓
├── luoghi/                         ← L2: luoghi singoli (~26 da generare)  ○
├── personaggi/                     ← L3: ritratti (23)                     ○
├── oggetti/                        ← L3-alt: icone oggetti-simbolo (13)    ○
└── drafts/                         ← tentativi, non definitivi
```

## Come rigenerare

Vedere `assets/PROMPTS.md` per prompt strutturati. Regola di ferro:
**nessun testo nelle immagini**. Mai.
