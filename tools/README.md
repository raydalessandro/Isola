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
