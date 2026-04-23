# Isola — Mondo interattivo online

Repo di sviluppo del **mondo interattivo online de "L'Isola dei Tre Venti"**.

Obiettivo: costruire l'esperienza web (PWA, probabilmente Next.js / React) che
accompagna la saga di 12 storie illustrate. I dati del mondo (personaggi,
luoghi, oggetti, venti, miti, archi narrativi) devono restare perfettamente
coerenti con la realtà canonica definita nel materiale di progetto.

Quando il mondo interattivo sarà completo verrà pubblicato insieme alla saga.

---

## Struttura repo

```
/
├── index.html        ← prototipo mappa navigabile (statico, punto di partenza)
├── LICENSE
├── README.md         ← questo file
└── content/          ← fonte di verità del mondo (estratta dal progetto)
    ├── README.md                 ← orientamento al progetto narrativo
    ├── docs/                     ← voce autore, principi, bibbia mondo
    ├── worldbuilding/            ← nomi, luoghi, miti canonici
    ├── architettura/             ← mappa saga, 12 archi narrativi
    ├── framework/                ← EAR ontologico (uso interno, mai nel testo)
    ├── grafo/                    ← grafo narrativo JSON + tool Python
    └── b3_0_5/                   ← traccia chat tecnica pulizia grafo
```

### Separazione di ruoli

- **root** — codice dell'applicazione web (oggi solo `index.html`; in futuro
  progetto Next/PWA).
- **`content/`** — materiale canonico del mondo. Fonte unica di verità per
  qualsiasi dato mostrato nell'app. Nessun dato del mondo va hardcoded nel
  codice: si legge da qui.

---

## Punti d'ingresso

- Per capire il **progetto narrativo** (principi, voce, roadmap): parti da
  [`content/README.md`](content/README.md), poi
  [`content/docs/PROGETTO_INDICE_v1_5.md`](content/docs/PROGETTO_INDICE_v1_5.md).
- Per capire la **geografia/cast** del mondo:
  [`content/docs/ISOLA_TRE_VENTI_BIBLE_v2.md`](content/docs/ISOLA_TRE_VENTI_BIBLE_v2.md)
  e [`content/worldbuilding/GLOSSARIO_ISOLA.md`](content/worldbuilding/GLOSSARIO_ISOLA.md).
- Per capire il **grafo narrativo** (stato semi, callback, storie iniettate):
  [`content/grafo/story_graph_v0_3_0.json`](content/grafo/story_graph_v0_3_0.json)
  con schema [`content/grafo/story_graph.schema.json`](content/grafo/story_graph.schema.json).
- Per l'attuale **prototipo di mappa navigabile**: [`index.html`](index.html).

---

## Stato

- [x] Materiale di progetto importato e organizzato in `content/`
- [x] Mappa navigabile statica (`index.html`) presente come prototipo
- [ ] Scelta stack definitiva (Next.js PWA / React / altro)
- [ ] Inizializzazione progetto web
- [ ] Layer di accesso dati che legge da `content/` (o da un export strutturato)
- [ ] UI/UX del mondo interattivo

---

## Principi non negoziabili (dal progetto narrativo)

Questi vincoli valgono **anche** nel mondo interattivo:

- **Framework EAR invisibile.** Nessun termine ontologico deve affiorare
  nell'UI destinata al lettore.
- **Nessuna morale esplicita.** Nessun testo UI che "spieghi" il significato.
- **Nominazione operativa.** Rispettare i nomi canonici del `GLOSSARIO_ISOLA`.
- **Geografia mandala silenziosa.** Struttura mai dichiarata nell'interfaccia.
- **Notte non personificata.** La notte è ambiente, non agente/entità.
- **Pattern A mai nominato.** Nemmeno nei metadati visibili.

Elenco completo e motivazioni in [`content/README.md`](content/README.md) §
"Principi non negoziabili".
