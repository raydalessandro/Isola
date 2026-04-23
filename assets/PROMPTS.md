# Prompt generazione immagini — L'Isola dei Tre Venti

Prompt strutturati per generare/rigenerare immagini con Grok Imagine (o BFL
FLUX Kontext Pro). L'obiettivo è mantenere coerenza visiva attraverso tutta
la libreria.

---

## Style anchor (da includere SEMPRE)

Questo blocco va incollato in OGNI prompt per garantire coerenza.

```
Style: hand-painted children's book illustration, watercolor and brown ink,
aged paper texture, warm earthy palette (cream, terracotta, olive green,
sea teal, warm brown, sun yellow, sand). Painterly but readable, slightly
textured lines, not cartoon, not photorealistic, not manga, not 3D.
Evocative, inhabited, gentle but not saccharine. References: Wolf Erlbruch,
Beatrice Alemagna, Beatrix Potter, European picture-book tradition.
```

## Regole universali (SEMPRE)

1. **NESSUN TESTO NELL'IMMAGINE.** Zero etichette, zero scritte, zero
   lettere visibili in qualsiasi punto della composizione. Nemmeno finti
   simboli runici o lettere fantasy. I modelli diffusion non scrivono
   italiano in modo affidabile — tutti i nomi dei luoghi vengono applicati
   come layer SVG sopra l'immagine nella web app. L'immagine è solo
   paesaggio dipinto.
2. **Nessun umano adulto in scena** (il mondo è abitato da animali
   antropomorfi). Unici umani: Gabriel, Elias, Noah — bambini — non in
   queste immagini.
3. **I 4 quartieri cardinali non sono simbolici** — disegnali per landmark
   (forno, pontile, orti, pascoli) e non come aree elementali
   (Fuoco/Acqua/Terra/Aria). Il mandala a 5 poli deve essere *leggibile*
   ma mai *dichiarato*.
4. **Nessun simbolo/rune/scritta esoterica** visibile.
5. **La notte** è ambiente, non entità: niente occhi nel buio, niente
   personificazioni.
6. **Niente pattern geometrici evidenti** (spirali, mandala, cerchi
   perfetti) nella composizione. Tutto deve sembrare organico.
7. **Cornice carta/pergamena** può stare se è parte dello sfondo; ma
   anche lì nessun testo, nessuna "compass rose" scritta.

---

## Architettura tile — approccio adottato

**Non si genera un'unica master map monolitica.** Si generano tile separati
(1 paper-base + 5 quartieri + N luoghi) che la web app assembla + label/hot
spot in overlay SVG. Ogni tile va chiesto **senza testo, senza scritte**.
La coerenza visiva tra tile viene dallo style anchor condiviso + dalla
pratica di passare un tile già approvato come reference image nelle
generazioni successive.

---

## L0a — Paper base (sfondo mappa, 1 sola)

La "pergamena" su cui poggiano i tile. Solo oceano + bordo, nessun
landmark.

```
[Style anchor]

Aspect ratio 9:16 portrait. Aged parchment sheet filling the frame,
with subtle fold lines, small tea stains, softly worn edges. Centered on
the parchment, a large empty oval-ish shape (island silhouette, no
content inside — just an empty land-colored base, to be filled in
another layer). Around the oval, painted sea-teal water with soft
painted waves, a few scattered distant rocks near the southeast corner,
a faint stepping-stone trail leading off the north edge of the parchment.

Three small painted wind indicators in three different corners (tiny
curling brushstrokes suggesting breeze direction) — no arrows, no text,
no symbols. A painted sun motif half-rising from one edge.

ABSOLUTELY NO TEXT. NO LABELS. NO LETTERS. NO COMPASS ROSE. NO NUMBERS.
NO FANTASY SCRIPT. NO RUNES. The island silhouette is visually blank.
```

---

## L0b — Master island composed (opzionale)

Se si vuole una master-map complessiva generata (invece di assemblata dai
5 tile), stesso prompt di L0a MA con l'isola già dipinta dentro (non
vuota). Usato come fallback visivo.

```
[Style anchor]

Aspect ratio 9:16 portrait. Aged parchment sheet. Centered: a painted
top-down island, roughly oval, irregular coastline. Island internal
features (visual only, NO names, NO text):

- Center: a small cluster of thatched-roof stone houses around a wide
  square with a very large old tree and a small circular well.
- North (top): two tall twin mountain peaks with a dark cave mouth on
  one slope, a ravine between peaks, a green grazing plateau with a
  few small sheep shapes, a rocky lookout edge.
- East (right): one large stone building with a smoking chimney, a
  small solitary house uphill catching dawn light.
- South (bottom): a wooden pier extending into the water, a tiny shore
  hut, a sandy pebble beach, low fisher cottages.
- West (left): concentric rings of cultivated patchwork fields
  transitioning into dense intertwined forest with two small earth-mound
  burrow-houses at the margin.
- A ring river encircling the center village, connecting to all quarters.
- Walking paths as faint painted lines connecting village to each
  quarter.

Around the island: painted sea with gentle waves, a stepping-stone
trail off the north, small distant islands off the southeast. Three
small wind-stroke indicators in corners. ABSOLUTELY NO TEXT. NO LABELS.
NO LETTERS. NO COMPASS. The map is purely visual — every name will be
applied later as an SVG overlay.
```

---

## L1 — Tile quartieri (5 totali, 3/4 perspective)

Framing consistente: vista 3/4 dall'alto (non top-down, non laterale). Orario
cambia per quartiere. **Zero testo nelle immagini.**

### L1.centro — Il Villaggio (usato per sapere cosa disegnare, non per scriverlo)

```
[Style anchor]

3/4 perspective illustrated scene, aspect ratio 9:16 portrait. Midday
light.

Central village square of an island inhabited by gentle animal characters.
At the heart of the square: a huge old tree with wide spreading branches
and a stone well beside it. A long stone bench nearby where two elderly
female animals (a hedgehog and a badger) sit quietly watching. Around
the square: a small thatched workshop where a woodpecker carpenter is
working; a round thatched cottage; a low school building toward one
edge with a grey heron (the teacher) visible at the door. Four dirt
paths leaving the square in four directions.

In the square: a red fox in flour-dusted terracotta apron; a cormorant
with a dark shell necklace; ONE grey squirrel (not two, only one) with
a soft leather pouch; a small group of animals pushing a wicker
wheelbarrow.

ABSOLUTELY NO TEXT. NO SIGNS. NO WRITING. NO LETTERS ANYWHERE.
```

### L1.forno — Quartiere del Forno (est, alba)

```
[Style anchor]

3/4 perspective, aspect ratio 9:16 portrait. First-light dawn, sky
rose-peach-pale-gold gradient.

Eastern quarter of a small island. Large stone-and-wood bakery building
with a big smoking chimney, warm orange light spilling from the oven
windows and open doorway. Stacked firewood against the wall. A solitary
small house on a gentle rise in the distance, catching first sun. Three
dirt paths converging near the bakery. A red fox in a flour-dusted
terracotta apron standing at the bakery door.

ABSOLUTELY NO TEXT. NO SIGNS. NO SHOP LETTERING. NO WRITING.
```

### L1.pontile — Quartiere del Pontile (sud, mezzogiorno)

```
[Style anchor]

3/4 perspective, aspect ratio 9:16 portrait. Clear midday light, sea
teal-green.

Southern coastal quarter of a small island. A long wooden pier
extending over shallow water with small painted boats moored to it. A
small wooden-and-thatch hut at the shore end. An old tortoise character
with visible scars on her shell standing near the pier. To one side: a
river mouth where fresh water meets sea in a brackish fan of sand. A
pebble beach with scattered shells. A small cliff-side cottage with a
cormorant on the porch. Low fisher cottages clustered nearby.

ABSOLUTELY NO TEXT. NO SIGNS. NO WRITING. NO BOAT NAMES.
```

### L1.orti — Quartiere degli Orti (ovest, pomeriggio)

```
[Style anchor]

3/4 perspective, aspect ratio 9:16 portrait. Warm late-afternoon gold
light.

Western quarter of a small island. Concentric rings of cultivated fields
forming a patchwork circle: outer ring fruit trees in soft bloom, middle
ring tall grains and beans, inner ring low herbs and vegetables in
rows. Two small earth-mound burrow-houses set into the forest margin on
one side — rounded turf-covered domes with wooden doors. Dense leafy
forest with intertwined canopy in the background. A few animal workers
in the fields with curved-handle hoes, engaged in quiet labor.

ABSOLUTELY NO TEXT. NO SIGNS. NO CROP LABELS. NO WRITING.
```

### L1.montagne — Quartiere dei Pascoli (nord, tramonto)

```
[Style anchor]

3/4 perspective, aspect ratio 9:16 portrait. Sunset sky:
orange-violet-deep-blue gradient.

Northern mountainous quarter of a small island. Two tall twin peaks
with a deep ravine running between them. A dark cave mouth visible
halfway up one slope. A wide high grazing plateau with a scatter of
sheep and goats. A steep rocky outcrop overlooking the island below. A
grey heron character standing on the rocky lookout at sunset, silhouetted
against the colored sky. A climbing path winding up from below.

ABSOLUTELY NO TEXT. NO SIGNS. NO WRITING.
```

---

## L2 — Luoghi singoli (template, ~26 da generare)

Usare questo template sostituendo `[LUOGO]`, `[CHI C'È]`, `[SENSI]`, `[ORA]`.

```
[Style anchor]

Detailed illustrated scene of a single place on the island. Aspect ratio
9:16 portrait.

Place: [LUOGO - nome canonico italiano]
Characters present: [CHI C'È - lista personaggi canonici, 0-2 max]
Time of day: [ORA - alba / mattina / mezzogiorno / pomeriggio / sera / notte]
Atmosphere (odore/suono/luce): [SENSI - una frase per ciascuno]

No labels in the image itself (clean scene, labels will be overlaid in UI).
Italian feel, European picture-book tradition.
```

**Esempi di luoghi da L2 da generare:**
- Il Forno di Fiamma (interno visto da fuori attraverso la porta aperta all'alba)
- Il Pontile di Bartolo (vista lunga dal mare verso riva)
- La Grotta di Grunto (imbocco a mezzogiorno, Grunto sulla soglia)
- L'Albero Vecchio (primo piano, radici esposte, corteccia scura)
- Il Pozzo (vista ravvicinata, secchio di legno, pietra bagnata)
- La Scuola di Stria (esterno con cuccioli all'uscita)
- La Bocca (dove fiume incontra mare, isolotti di sabbia)
- La Spiaggia delle Conchiglie (a bassa marea, sabbia ricca)
- La Casa-tana di Rovo (soglia, tenda di giunchi, bandana scura appesa)
- Roccia Alta (vista dallo sperone verso l'isola sotto)
- Case Basse dei Pescatori (cluster al tramonto)
- [...altri 15 luoghi dal canone, uno per uno]

---

## L3 — Personaggi (template, 23 ritratti)

```
[Style anchor]

Character portrait illustration, aspect ratio 3:4 portrait.
Painted on aged paper, as if torn from a naturalist's sketchbook.

Character: [NOME CANONICO]
Species: [SPECIE]
Role: [MESTIERE/RUOLO]
Distinctive attribute: [FIRMA VISIVA dal canone]
Expression: [2-3 parole — calmo, attento, saggio, giocoso, etc.]

Three-quarter view, soft brown ink outline, watercolor fill. Subject
centered, simple background (single warm color wash, hint of their
typical surroundings). No text, no labels. Animals are gently
anthropomorphic — they stand upright, wear simple garments, but retain
animal features (snout, paws, fur/feathers). Not cartoon big-eyes.
Readable at small size for a phone screen.
```

**Lista personaggi per L3** (vedi `world/characters/` per dettagli canonici):

| Categoria | Chi |
|---|---|
| primari (5) | Bartolo, Fiamma, Rovo, Stria, Mèmolo |
| testimoni (1) | Grunto |
| secondari (4) | Salvia, Nodo, Amo, Zolla |
| cuccioli (5) | Pun, Toba, Bru, Cardo, Liù |
| gruppi (6) | Coltivatori del Cerchio, Mercato del Mezzogiorno, Vecchie del Mercato, Mantenitori, Camminanti, Pastori *(per i gruppi: ritratti di gruppo, non individuali)* |

---

## L3-alt — Oggetti-simbolo (13 icone)

```
[Style anchor]

Single-object illustration, aspect ratio 1:1 square. Painted on aged
parchment. Soft brown ink, watercolor wash. Three-quarter view of the
object, isolated, no background, small painted shadow beneath. Readable
as an icon on a phone screen at 120px.

Object: [NOME OGGETTO E MATERIALE]
Associated character/group: [A CHI APPARTIENE]
```

Oggetti canonici dal mondo:
- Zappa manico curvo (Coltivatori)
- Scala a pioli corta (Mantenitori)
- Carriola vimini intrecciato (Camminanti)
- Grembiule terracotta infarinato (Fiamma)
- Bandana scura (Rovo)
- Scialle cenere (Stria)
- Sciarpa annodata male (Mèmolo)
- Cesto vimini sottile (Salvia)
- Corda arrotolata (Nodo)
- Collana conchiglia conica scura (Amo)
- Bisaccia pelle morbida (Zolla)
- Cicatrice lunga fianco sinistro (Grunto) *[non oggetto — tratto]*

---

## Workflow consigliato

1. **Prima genera L0a paper-base** (pergamena + oceano + bordi, isola
   vuota). Questa fissa il framing e la texture carta. 1-2 iterazioni per
   ottenerla pulita.
2. **Poi L1.centro** (village) come tile-anchor — è il polo con più densità
   di elementi, se funziona funziona tutto.
3. Con L1.centro approvata, **passa gli altri 4 quartieri** (forno, pontile,
   orti, montagne) USANDO L1.centro come **reference image** in Grok
   Imagine. Questo è il trucco di coerenza stilistica: invece di sperare
   che lo style anchor basti, dai all'AI una sorgente visiva concreta.
4. Poi passa a **L2 luoghi singoli** uno per volta, sempre con reference
   image del quartiere di appartenenza.
5. **L3 personaggi** in batch: genera i 23 ritratti con lo stesso style
   anchor per consistenza + un personaggio già approvato come reference.
6. **L3-alt oggetti**: icone batch, stesso trattamento.

**Regola di ferro**: l'immagine non contiene mai testo. I nomi li
applichiamo noi via SVG nella web app. Se compare anche solo una lettera
nell'immagine, rigenera.

Se un'immagine non soddisfa, regenera con variazioni di prompt — ma NON
cambiare lo style anchor (quello è il collante visivo del progetto).

---

## Note tecniche

- **Risoluzione**: genera tutto a >= 2048×2048 quando possibile. Downscale
  in UI, upscale mai.
- **Formato salvataggio**: PNG (lossless) per master; WebP per consumo web.
- **Naming**: `assets/<livello>/<slug>.png` — slug in italiano, kebab-case,
  nomi canonici (es. `forno-di-fiamma.png`, non `bakery.png`).
- **Portrait 9:16** è default per smartphone; solo i ritratti L3 sono 3:4;
  solo gli oggetti L3-alt sono 1:1.
