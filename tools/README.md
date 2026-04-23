# tools/ — pipeline build world/

Pipeline Python deterministica che legge da `content/` (sorgente narrativa di
verità) e rigenera `world/` (schede pubbliche consumate dalla web app).

## Regola aurea

`world/` è **completamente rigenerabile** da `content/`. Stesso input →
output identico byte-per-byte. Nessun umano edita `world/` a mano.

## Dipendenze

- Python ≥ 3.10
- `PyYAML`
- `jsonschema`

Vedi `requirements.txt`.

## Come rigenerare

```bash
make world        # python3 tools/build_world.py
make validate     # python3 tools/validate.py
make world-check  # build + git diff world/ --exit-code
```

## Scope corrente

Questo round genera **solo personaggi e avatar** (18 totali):

- 3 avatar → `world/avatars/`
- 5 primari, 1 testimone, 4 secondari, 5 cuccioli → `world/characters/<categoria>/`

Locations, oggetti, venti, gruppi e spiriti arrivano in round successivi.

## Vincolo fondamentale: nessuna label framework in world/

Le schede pubbliche **non** proiettano:

- Δ / ⇄ / ⟳ come etichette o attributi
- Pattern A / pattern AI da bandire
- `seeds`, `callbacks`, `debts`, `quote_tracker`
- `fragments_budget` (Grunto) o metadati di scrittura

Questi restano nel grafo in `content/` e sono metadati di scrittura, non
materiale esposto al lettore.

## Layout

```
tools/
  build_world.py    entrypoint
  validate.py       validator schema + ref cross-entity
  parse/
    graph.py        carica content/grafo/story_graph_v0_3_0.json
    bibbia.py       estrae §2 cast e §4 abitanti da ISOLA_TRE_VENTI_BIBLE_v2.md
    glossario.py    estrae voci cast da GLOSSARIO_ISOLA.md
  render/
    card.py         emette Markdown + frontmatter YAML deterministico
```

## Determinismo

- YAML dump con `sort_keys=True`, `default_flow_style=False`, `allow_unicode=True`
- JSON dump con `sort_keys=True, indent=2, ensure_ascii=False`
- Nessun timestamp
- Iterazione sempre su sequenze ordinate (`sorted(...)`)
- Newline LF, encoding UTF-8 senza BOM

## Modulo geografia

`tools/geography.py` è il modulo interrogabile sulla geografia dell'isola.
Legge direttamente `world/geography/*.json` (sorgente di verità) ed espone
un'API stdlib-only. È **indipendente** da `build_world.py`: la geografia è
scritta a mano (con coordinate derivate dalla Bibbia §8 e dal Glossario
§1-§2) e non viene rigenerata dalla pipeline. Se in futuro un parser dedicato
leggerà le coordinate dalla Bibbia, potrà emettere `locations.json` e
`paths.json`; per ora sono file editabili manualmente.

### CLI — `python -m tools.geo_query`

Interroga la geografia da terminale:

```bash
# distanza in linea retta (m)
python -m tools.geo_query distance forno_di_fiamma grotta_di_grunto
# → 3376 m

# tempo di percorrenza lungo la rete sentieri, in minuti
python -m tools.geo_query walking-time forno_di_fiamma grotta_di_grunto --speed child_walk
# → 114.9 min (child_walk)

# cammino Dijkstra nella rete sentieri
python -m tools.geo_query path orti_del_cerchio pontile_di_bartolo
# → orti_del_cerchio -> albero_vecchio -> pontile_di_bartolo (2 archi, 4.20 km)

# luoghi entro un raggio
python -m tools.geo_query nearby albero_vecchio --radius 200

# elenco completo o filtrato per quartiere
python -m tools.geo_query list
python -m tools.geo_query list --quartiere pontile

# quartiere contenente un luogo
python -m tools.geo_query quartiere-of forno_di_fiamma

# euristica di visibilità (approssimata)
python -m tools.geo_query visible-from roccia_alta

# output JSON strutturato
python -m tools.geo_query distance forno_di_fiamma grotta_di_grunto --json
```

Preset di velocità disponibili:

| preset          | m/s  | uso canonico                     |
|-----------------|------|----------------------------------|
| `adult_walk`    | 1.2  | abitanti adulti sui sentieri     |
| `child_walk`    | 0.8  | i tre fratelli                   |
| `bartolo_walk`  | 0.4  | tartaruga fuori dall'acqua       |
| `child_run`     | 2.0  | gioco/fuga                       |

### API Python

```python
from tools.geography import IslandGeography

geo = IslandGeography()  # autodetect world/geography/

geo.location("forno_di_fiamma")          # → Location(...)
geo.all_locations()                      # list[Location] ordinate per id
geo.distance("a", "b")                   # float (m, linea retta 3D)
geo.path("orti_del_cerchio", "pontile_di_bartolo")  # list[str] (Dijkstra)
geo.walking_time("a", "b", speed="child_walk")      # float (minuti)
geo.nearby("albero_vecchio", radius_m=200)          # list[str]
geo.quartiere_of("forno_di_fiamma")      # "forno" | None
geo.elevation("grotta_di_grunto")        # float (m)
geo.visible_from("roccia_alta")          # list[str] (euristica)
```

Visibilità è una **euristica approssimata** (non true line-of-sight):
B visibile da A se `elevation(A) + bonus > elevation(B)` oppure se A è
alto (≥100 m) e la distanza ≤ 3 km. Documentato nel docstring.

### Mirror TypeScript

`web/lib/geography.ts` è il mirror client-safe (stessa API, stessa
semantica, stesso algoritmo Dijkstra). Il loader da disco sta in
`web/lib/geography-load.ts` (server-only, usa `fs`).

### Vincoli canonici rispettati

- Nessuna label framework EAR (Δ/⇄/⟳), nessun Pattern A, nessun
  seed/callback nei file di geografia o nell'API.
- Quartieri identificati da id tecnici (`centro/forno/pontile/orti/montagne`).
  Mai label "Fuoco/Acqua/Terra/Aria" nell'output user-facing.
- `Piccole Isole all'orizzonte` e `guado_di_pietre_piatte` inclusi come
  `porta_socchiusa=true` (presenti come riferimento, non esplorabili).

### Test

```bash
python -m unittest tools.tests.test_geography
```

29 test (stdlib `unittest`, pytest non richiesto).
