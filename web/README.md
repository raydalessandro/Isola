# L'Isola dei Tre Venti — PWA (web shell)

Next.js 16 + React Three Fiber app che presenta l'isola dall'alto,
navigabile stile Google Earth, installabile come PWA su smartphone.

Questo è il **v0** del mondo interattivo: un'isola heightmap low-poly, 5
hotspot sui poli del villaggio e un pannello overlay per aprire un luogo.

## Prerequisiti

- Node.js ≥ 20 (testato con 22)
- npm ≥ 10

## Setup locale

```bash
cd web
npm install
npm run dev
```

Apre su http://localhost:3000.

In modalità dev il service worker non è registrato (per evitare cache
aggressive durante lo sviluppo). Per testare l'installabilità PWA:

```bash
npm run build
npm run start
# apri http://localhost:3000 in Chrome → DevTools → Application → Manifest
```

### HTTPS su rete locale (iOS install test)

Safari iOS richiede HTTPS per registrare un service worker. Per testare su
un iPhone collegato alla stessa LAN:

```bash
npx next dev --experimental-https --hostname 0.0.0.0
```

Poi apri `https://<ip-laptop>:3000` da Safari, e "Aggiungi a Home" dal
menu condividi.

## Struttura

```
web/
├── app/
│   ├── layout.tsx          — font loading (Cormorant + Caveat), manifest, viewport
│   ├── page.tsx            — legge world/ + geography al build, monta IslandScene
│   └── globals.css         — palette coerente con legacy/index.html
├── components/
│   ├── IslandScene.tsx     — Canvas R3F + lighting + MapControls
│   ├── Island.tsx          — heightmap procedurale (simplex-noise)
│   ├── Ocean.tsx           — plane blu-teal + vertex wave sin-based
│   ├── Hotspot.tsx         — pin 3D per quartiere
│   ├── HotspotPanel.tsx    — overlay UI slide-up
│   └── ServiceWorkerRegister.tsx
├── lib/
│   ├── geography.ts        — tipi + palette + metersToUnits()
│   └── world.ts            — fs-readers per ../world/_index.json e ../world/geography/island.json
├── public/
│   ├── manifest.json
│   ├── sw.js               — service worker hand-crafted (no bundler)
│   └── icon-*.png          — generate da scripts/generate-icons.mjs
└── scripts/
    └── generate-icons.mjs  — sharp → PNG da SVG (terracotta "I")
```

## Fonti dati canoniche (fuori da `web/`)

- `world/_index.json` — elenco personaggi/avatar generato dalla pipeline `tools/`
- `world/geography/island.json` — geometria canonica dell'isola (bounds, quartieri, coordinate in metri)

Questi file vengono letti a **build time** da `lib/world.ts` (SSG).

## Palette & tipografia

Mirror della palette in `legacy/index.html`. Font:
- **Cormorant Garamond** (serif, body)
- **Caveat** (handwritten, titoli)

## PWA

- `public/manifest.json` — installabile
- `public/sw.js` — service worker shell + runtime cache
- `components/ServiceWorkerRegister.tsx` — registra solo in production build

## Comandi

```bash
npm run dev       # dev server
npm run build     # produzione (SSG)
npm run start     # serve la build
npm run lint      # ESLint
```

## Cosa NON è ancora nel v0

- Ground-level walk ("entrare" in un quartiere).
- Più di 5 hotspot (NPC, scene, oggetti).
- Shader dell'oceano avanzato (caustics, foam).
- Deep-linking `?quartiere=forno`.
- Localizzazione (solo IT).
- Push notifications.
