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

## Da sistemare (prima di trattarli come asset definitivi)

1. Testi in immagine misti italiano/inglese — solo italiano.
2. Refusi label (es. Zolla doppio in centro).
3. Master map: versione portrait per smartphone (oggi è landscape).
4. Consistenza palette e mano grafica tra le 6 immagini (sono di generazioni
   diverse, si vede nella resa di alcuni dettagli).
5. Mancano vignette per: scuole/botteghe singole, spiagge minori,
   Guado, Casa del Mattino isolata, singoli scenari sensoriali per alba/giorno/sera/notte.

## Come rigenerare

Vedere `assets/PROMPTS.md` (WIP) per i prompt strutturati da usare con Grok
Imagine o BFL FLUX Kontext Pro.
