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

1. **Solo testo in italiano** in etichette visibili. Nessuna parola inglese.
2. **Nessun umano adulto in scena** (il mondo è abitato da animali
   antropomorfi). Unici umani: Gabriel, Elias, Noah — bambini — non in
   queste immagini.
3. **Non etichettare i quartieri come "Fuoco/Acqua/Terra/Aria"** — se li
   mostri, chiamali per landmark ("del Forno", "del Pontile", "degli Orti",
   "dei Pascoli", "il Villaggio").
4. **Nessun simbolo/rune/scritta esoterica** visibile.
5. **La notte** è ambiente, non entità: niente occhi nel buio, niente
   personificazioni.
6. **Niente pattern geometrici evidenti** (spirali, mandala, cerchi
   perfetti) nella composizione. Tutto deve sembrare organico.

---

## L0 — Master map (atlante isola)

### Prompt

```
[Style anchor]

Top-down illustrated atlas map of an island, aspect ratio 9:16 (portrait
for smartphone), painted on aged parchment with subtle fold lines and tea
stains. Island shape: roughly oval with irregular coast, ~8km north-south,
~7km east-west.

Compose five named regions (but DO NOT label them as cardinal directions or
elements — use only landmark names):

- CENTER: "Il Villaggio" — cluster of stone and wood thatched houses around
  a central square with a huge old tree ("L'Albero Vecchio") and a stone
  well ("Il Pozzo"). A stone bench ("Panca di Pietra") visible.

- EAST: quarter of the oven — large stone bakery with smoking chimney
  ("Il Forno di Fiamma"), isolated house ("Casa del Mattino") on a small
  rise facing sunrise.

- SOUTH: coastal quarter — wooden pier extending over water ("Il Pontile
  di Bartolo"), a small hut ("La capanna di Bartolo"), pebble beach
  ("La Spiaggia delle Conchiglie"), cliff house ("Casa di Amo"), low fisher
  cottages ("Case Basse dei Pescatori"). River mouth where fresh water
  meets sea ("La Bocca").

- WEST: quarter of the gardens — concentric rings of cultivated fields
  ("Gli Orti del Cerchio") transitioning into an intertwined forest
  ("La Foresta Intrecciata") with burrow-houses at margins ("Casa-tana di
  Rovo", "Casa-tana di Zolla").

- NORTH: twin mountains ("Montagne Gemelle") with a visible cave
  ("La Grotta di Grunto"), a steep ravine ("Il Burrone"), an elevated
  rocky outcrop overlooking everything ("Roccia Alta"), high pastures
  ("Pascoli Alti") with sheep and goats.

A ring river flows around the center, connecting all quarters ("Il Fiume
che Gira").

Paths between quarters (use Italian names):
- "Via dell'Alba" (east)
- "Via del Pontile" (south)
- "Via degli Orti" (west)
- "Via che Sale" (north)

Beyond the island, in the sea: a faint stepping-stone path north
("Il Guado di Pietre Piatte"), small distant islands on the SE horizon
("Piccole Isole all'orizzonte"). Mark two zones on the coast as "Zone
non ancora nominate" (unexplored).

Small wind indicators at three corners (dawn-east, midday-south, sunset-SW)
with tiny painted arrows — no labels, no symbols.

Labels in italic Italian serif, brown ink. Paper border with worn edges.
No grid lines, no modern compass rose, no coordinates.
```

---

## L1 — Vignette quartieri (5 totali)

Framing consistente: vista 3/4 dall'alto (non top-down, non laterale). Orario
dipende dal vento che domina il quartiere.

### L1.centro — Il Villaggio

```
[Style anchor]

3/4 perspective illustrated scene, aspect ratio 9:16 portrait.

Central village square of an island inhabited by animal characters. Huge
old tree at center ("L'Albero Vecchio") with sprawling branches. A stone
well ("Il Pozzo") beside it. Long stone bench ("Panca di Pietra") where
two elderly female animals sit quietly (hedgehog, badger — "le Vecchie
del Mercato"). Small thatched workshop ("La bottega di Nodo") with a
woodpecker carpenter visible. Round thatched cottage ("La casetta tonda
di Mèmolo"). School building ("La Scuola di Stria") visible toward one
edge. Paths named "Via dell'Alba", "Via del Pontile", "Via degli Orti",
"Via che Sale" diverging from the square.

In the square, midday activity: a fox baker ("Fiamma") in terracotta
flour-dusted apron; a cormorant fisher ("Amo"); a grey squirrel ("Zolla")
with a soft leather pouch — SHOW ZOLLA ONLY ONCE. A small group of
"Camminanti" with a wicker wheelbarrow.

Italian labels only. Labels in italic Italian serif, brown ink.
```

### L1.forno — Quartiere del Forno (est)

```
[Style anchor]

3/4 perspective, aspect ratio 9:16 portrait.

Eastern quarter at first light. Large stone and wood bakery with a big
smoking chimney ("Il Forno di Fiamma"), warm orange light spilling from
the windows. Stacked firewood beside it. A small solitary house on a
rise ("Casa del Mattino") catching first sun. Paths labeled "Via dell'Alba"
(rising east), "Via del Pontile" (leaving south), "Via che Sale"
(leaving north). A red fox in flour-dusted apron ("Fiamma") opening the
bakery door. Sky: dawn gradient rose-peach-pale-gold.

Italian labels only.
```

### L1.pontile — Quartiere del Pontile (sud)

```
[Style anchor]

3/4 perspective, aspect ratio 9:16 portrait.

Southern coastal quarter at midday. Long wooden pier extending over
shallow water ("Il Pontile di Bartolo"). A small hut at shore end
("La capanna di Bartolo"), an old tortoise character ("Bartolo") with a
scarred shell visible near the pier. River meeting sea in a brackish
mouth ("La Bocca"). Pebble beach with scattered shells ("La Spiaggia
delle Conchiglie"). Small cliff house with a cormorant on the porch
("Casa di Amo"). Low fisher cottages ("Case Basse dei Pescatori").
Paths: "Via del Pontile" entering from north. Sky: clear midday,
sea teal-green.

Italian labels only.
```

### L1.orti — Quartiere degli Orti (ovest)

```
[Style anchor]

3/4 perspective, aspect ratio 9:16 portrait.

Western quarter in late afternoon. Concentric rings of cultivated fields
("Gli Orti del Cerchio") — outer ring fruit trees, middle ring grains
and legumes, inner ring herbs and vegetables. Two small earth-mound
burrow-houses at the forest margin ("Casa-tana di Rovo", "Casa-tana di
Zolla"). Dense, leafy, intertwined-canopy forest in the background
("La Foresta Intrecciata"). Working community visible ("Coltivatori
del Cerchio") with curved-handle hoes. Paths: "Via degli Orti" entering
from east. Sky: warm late-afternoon gold.

Italian labels only.
```

### L1.montagne — Quartiere dei Pascoli (nord)

```
[Style anchor]

3/4 perspective, aspect ratio 9:16 portrait.

Northern mountainous quarter at sunset. Two twin peaks ("Montagne
Gemelle"). A deep ravine between ("Il Burrone"). A cave mouth halfway up
one slope ("La Grotta di Grunto"). High grazing plateau with sheep and
goats ("Pascoli Alti"). A steep rocky lookout ("Roccia Alta") with
panoramic view over the island. Paths: "Via che Sale" climbing from
south. A grey heron ("Stria") perched on Roccia Alta at sunset. Sky:
sunset orange-violet-deep-blue gradient.

Italian labels only.
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

1. **Prima genera UNA master map v2** (portrait, italiano pulito) — è il
   master style reference.
2. Una volta approvata la master, rigenera le **5 vignette quartieri** con
   lo stesso style anchor + riferimento alla master per coerenza.
3. Poi passa a **L2 luoghi singoli** uno per volta, con la relativa scena.
4. **L3 personaggi** in batch: genera i 23 ritratti con lo stesso style
   anchor per consistenza.
5. **L3-alt oggetti**: icone batch, stesso trattamento.

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
