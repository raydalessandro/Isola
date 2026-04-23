# assets/ — riferimenti visivi

Materiale visivo del mondo. **Indicativo, non definitivo.** Generato con Grok
Imagine come punto di partenza per fissare identità visiva e coerenza
geografica.

Qualsiasi immagine qui può servire sia come **riferimento di stile** (per
generazioni future) sia come **asset diretto** (se passa il vaglio di
coerenza canonica).

## Contenuto attuale

### `map/`
- `atlante-isola.png` — **master map**, atlante completo vista dall'alto.
  Mostra i 5 poli (centro + 4 quartieri cardinali), venti, zone non ancora
  nominate (porte socchiuse), Guado di Pietre Piatte, Piccole Isole
  all'orizzonte. **WIP**: alcuni testi sono misti italiano/inglese da
  ripulire.

### `quartieri/`
Vignette 3/4 vista per ogni polo. Nomi canonici dei luoghi sono corretti;
alcuni label minori hanno refusi/ridondanze da ripulire.

- `centro-villaggio.png` — piazza con Albero Vecchio, Pozzo, Panca di Pietra,
  bottega di Nodo, casetta tonda di Mèmolo, Scuola di Stria. **Nota**: Zolla
  compare doppio nel disegno (due label diversi sullo stesso personaggio) —
  da correggere in rigenerazione.
- `fuoco.png` — quartiere del Forno (est). Forno di Fiamma col camino
  fumante, Via dell'Alba, Via del Pontile, Via che Sale, Casa del Mattino.
  Scena notturna.
- `acqua.png` — quartiere del Pontile (sud). Pontile di Bartolo, capanna di
  Bartolo, La Bocca, Spiaggia delle Conchiglie, Casa di Amo, Case Basse dei
  Pescatori.
- `terra.png` — quartiere degli Orti (ovest). Orti del Cerchio a fasce
  concentriche, Foresta Intrecciata, Casa-tana di Rovo, Casa-tana di Zolla.
- `aria.png` — quartiere dei Pascoli (nord). Montagne Gemelle, Burrone,
  Grotta di Grunto, Pascoli Alti. Via del Pontile e Via che Sale.

## Vincoli canonici rispettati dalle immagini

- Geografia mandala silenziosa: 5 poli presenti ma **mai nominati con label
  elementali** (Fuoco/Acqua/Terra/Aria sono nomi interni — nei vignette
  compaiono per landmark: "Forno", "Pontile", "Orti", "Pascoli").
- Nomi canonici: Albero Vecchio, Pozzo, Panca di Pietra, Fiume che Gira,
  Bocca, Grotta di Grunto, Montagne Gemelle, Orti del Cerchio, Foresta
  Intrecciata, Roccia Alta tutti presenti.
- Venti modellati con caratteristiche (Taglio alba/nitido, Intreccio
  giorno/scambio, Mulinello sera/imprevedibile).
- Zone non ancora nominate / Piccole Isole all'orizzonte / Guado di Pietre
  Piatte: mantenute come porte socchiuse per espansione futura.

## Architettura tile (adottata)

Dopo i primi tentativi di master-map monolitica si è visto che:
- i diffusion model non scrivono italiano in modo affidabile (i nomi
  risultano sempre leggermente sbagliati e diversi tra una run e l'altra)
- una mappa unica non è rigenerabile per parti senza perdere la coerenza

**Decisione**: le immagini sono **paesaggio dipinto senza testo**. I nomi
dei luoghi, i label, gli hotspot interattivi sono **un layer SVG sopra
l'immagine** nella web app, con font Caveat (già caricato in `index.html`).
Vantaggi: nomi sempre corretti, multilingua gratis, immagini rigenerabili
senza rompere nulla, interattività nativa.

### Struttura assets prevista

```
assets/
├── map/
│   ├── paper-base.png              ← L0a: pergamena + oceano, isola vuota
│   └── island-master.png           ← L0b: vista complessiva isola (fallback)
├── quartieri/                      ← L1: 5 tile 3/4 perspective
│   ├── centro.png
│   ├── forno.png
│   ├── pontile.png
│   ├── orti.png
│   └── montagne.png
├── luoghi/                         ← L2: luoghi singoli (~26 da generare)
├── personaggi/                     ← L3: ritratti (23)
├── oggetti/                        ← L3-alt: icone oggetti-simbolo (13)
└── drafts/                         ← tentativi, non definitivi
    └── master-v2-attempts/         ← 3 tentativi master portrait con Grok
```

### Drafts correnti

`drafts/master-v2-attempts/tentativo-01..03.jpg` — 3 generazioni Grok
Imagine in portrait: stile e struttura promettenti, ma testo nelle
immagini sempre garbled ("Canadu" invece di "Guado", "Cava del Mattino"
invece di "Casa", ecc.). **Utili come reference di stile**, non come
asset finali.

## Come rigenerare

Vedere `assets/PROMPTS.md` per prompt strutturati. Regola di ferro:
**nessun testo nelle immagini**. Mai.
