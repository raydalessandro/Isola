# Isola — Mondo interattivo online

Repo di sviluppo del **mondo interattivo online de "L'Isola dei Tre Venti"**.

Obiettivo: costruire l'esperienza web (PWA Next.js + R3F) che accompagna la
saga di 12 storie illustrate. I dati del mondo (personaggi, luoghi, oggetti,
venti, miti, archi narrativi) restano perfettamente coerenti con il canone
narrativo.

**Live**: https://isola-nk6b.vercel.app
**Ultimo checkpoint**: [`CHECKPOINT.md`](CHECKPOINT.md) (2026-04-23)

---

## Struttura repo

```
/
├── README.md         ← questo file
├── CHECKPOINT.md     ← snapshot stato + consigli ricerca
├── LICENSE
│
├── content/          ← SORGENTE NARRATIVA (canone, read-only)
│   ├── docs/
│   ├── worldbuilding/
│   ├── architettura/
│   ├── framework/
│   ├── grafo/
│   └── b3_0_5/
│
├── world/            ← DATI DERIVATI (generati da content/ via pipeline)
│   ├── characters/   ← 18 schede MD+YAML
│   ├── avatars/      ← Gabriel, Elias, Noah
│   ├── geography/    ← 27 location + paths + features + terrain
│   ├── _schema/
│   └── _index.json
│
├── tools/            ← PIPELINE PYTHON + API INTERROGABILE
│   ├── build_world.py
│   ├── geography.py
│   ├── geo_query.py
│   ├── parse/
│   ├── render/
│   └── tests/        ← 116 test, CI verde
│
├── web/              ← WEB APP (Next.js 16 + R3F + PWA)
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── public/
│
├── assets/           ← riferimenti visivi (immagini Grok, WIP)
│
└── legacy/           ← prototipi (index.html statico)
```

### Separazione di ruoli

- **`content/`** — sorgente narrativa di verità. Toccato solo dal lavoro
  narrativo. Flusso mono-direzionale: `content/` → `world/` → `web/`.
- **`world/`** — rigenerabile dalla pipeline `tools/`. Stessi dati
  consumati da Python (narrativa) e TS (web) con API in parità.
- **`tools/`** — pipeline + API interrogabile. Permette a un'AI autore di
  chiedere `geo.walking_time("forno", "grotta_grunto", "child_walk")`
  invece di avere la bibbia intera in context.
- **`web/`** — consumer puro di `world/`. Zero dati hardcoded.

---

## Stato attuale (vedi [`CHECKPOINT.md`](CHECKPOINT.md) per dettagli)

- [x] Pipeline `content/` → `world/` deterministica
- [x] 18 schede personaggio canoniche
- [x] 27 location + rete sentieri + features + terrain
- [x] API geografia Python + TS (stessa semantica)
- [x] Tempi canonici fedeli alla bibbia §8.1 (120 min per Roccia Alta, ecc.)
- [x] 116 test + CI GitHub Actions
- [x] PWA Next.js in 3D, installabile, online su Vercel
- [x] Camera Google Earth (drag + pinch + tilt)
- [x] Interazione tap-and-hold → descent, swipe-down → ascent, dwell → nome
- [x] Terreno con rilievi leggibili, 5 zone colore per quartiere
- [x] Fiume che Gira visibile con sorgente e foce
- [x] 1 tile (Forno) renderizzato con dettaglio a L1
- [ ] Altri 4 tile (Pontile, Orti, Montagne, Centro)
- [ ] Character presence nei quartieri
- [ ] Ground-level view
- [ ] Painterly post-processing

---

## Comandi utili

### Python (pipeline + API geografia)

```bash
# Rigenera world/characters da content/
python tools/build_world.py

# Query geografia
python -m tools.geo_query walking-time albero_vecchio grotta_di_grunto --speed child_walk
python -m tools.geo_query nearby albero_vecchio --radius 200
python -m tools.geo_query distance-to-river casa_del_mattino

# Test
python -m unittest discover -s tools/tests -v
```

### Web

```bash
cd web
npm install
npm run dev            # http://localhost:3000
npm run lint
npm run build
```

### Deploy

Automatico su push a `main`. Vercel rebuilda e redeploya in ~1 minuto.

---

## Principi non negoziabili (dal canone narrativo)

1. **Framework EAR invisibile** — mai in UI, mai in metadati user-facing.
2. **Nessuna morale esplicita** nel testo o UI.
3. **Mandala silenzioso**: i 4 quartieri cardinali NON si chiamano
   "Fuoco/Acqua/Terra/Aria" user-facing. Solo "del Forno", "del Pontile",
   "degli Orti", "delle Montagne".
4. **Notte non personificata**.
5. **Nominazione operativa**: nomi canonici dal `GLOSSARIO_ISOLA`.
6. **Geografia mandala silenziosa**: struttura mai dichiarata.
7. **Pattern A mai nominato**.
8. **Detti popolari esclusivi di Fiamma**.

Elenco completo e motivazioni in [`content/README.md`](content/README.md) §
"Principi non negoziabili".
