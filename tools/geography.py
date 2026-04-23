"""Geography module for L'Isola dei Tre Venti.

Source of truth: world/geography/*.json
- island.json    — bounds + 5 quartieri (letto da web app esistente)
- locations.json — luoghi canonici con coordinate
- paths.json     — rete sentieri per pathfinding

Convenzione coordinate: Three.js. Origine (0,0) = Albero Vecchio.
est=+x, sud=+z, su=+y. Unità nel JSON: metri.

Velocità di percorrenza canoniche (preset nominati, in m/s):
- adult_walk    1.2   abitanti adulti sui sentieri
- child_walk    0.8   i tre fratelli
- bartolo_walk  0.4   tartaruga fuori dall'acqua
- child_run     2.0   gioco/fuga

Vincoli canonici:
- Nessun framework EAR, nessun Pattern A, nessun seed/callback.
- Solo geografia osservabile.
- Quartieri identificati da id tecnici (centro/forno/pontile/orti/montagne);
  MAI label 'Fuoco/Acqua/Terra/Aria' in output user-facing.
"""
from __future__ import annotations

import heapq
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

WALKING_SPEEDS_MPS: dict[str, float] = {
    "adult_walk": 1.2,
    "child_walk": 0.8,
    "bartolo_walk": 0.4,
    "child_run": 2.0,
}

SpeedPreset = Literal["adult_walk", "child_walk", "bartolo_walk", "child_run"]


@dataclass(frozen=True)
class Coords:
    x: float
    z: float
    y: float


@dataclass(frozen=True)
class Location:
    id: str
    nome_canonico: str
    categoria: str
    quartiere: str | None
    coords: Coords
    descrizione_breve: str
    porta_socchiusa: bool


@dataclass(frozen=True)
class Edge:
    from_id: str
    to_id: str
    via: str | None
    distance_m: float
    difficulty: str


def _euclidean(a: Coords, b: Coords) -> float:
    return math.sqrt(
        (a.x - b.x) ** 2 + (a.z - b.z) ** 2 + (a.y - b.y) ** 2
    )


def _resolve_data_dir(data_dir: str | Path | None) -> Path:
    """Trova la cartella world/geography. Accetta un path assoluto,
    un path relativo alla repo root, oppure None (autodetect)."""
    if data_dir is None:
        # autodetect: sali da questo file fino alla repo root
        here = Path(__file__).resolve()
        repo_root = here.parent.parent
        return repo_root / "world" / "geography"
    p = Path(data_dir)
    if p.is_absolute():
        return p
    # relativo a cwd o repo root: prova entrambi, preferisci cwd
    cwd_p = Path.cwd() / p
    if cwd_p.exists():
        return cwd_p
    here = Path(__file__).resolve()
    repo_root = here.parent.parent
    return repo_root / p


class IslandGeography:
    """API interrogabile sulla geografia dell'isola.

    Stesso dato (world/geography/*.json) consumato da:
    - autori AI in chat narrativa (tramite tools/geo_query.py CLI)
    - autori umani da terminale (CLI)
    - web app (mirror TypeScript in web/lib/geography.ts)
    """

    def __init__(self, data_dir: str | Path | None = None) -> None:
        base = _resolve_data_dir(data_dir)
        with (base / "island.json").open("r", encoding="utf-8") as fh:
            self._island: dict[str, Any] = json.load(fh)
        with (base / "locations.json").open("r", encoding="utf-8") as fh:
            loc_doc: dict[str, Any] = json.load(fh)
        with (base / "paths.json").open("r", encoding="utf-8") as fh:
            path_doc: dict[str, Any] = json.load(fh)

        self._locations: dict[str, Location] = {}
        for raw in loc_doc["locations"]:
            c = raw["coords"]
            loc = Location(
                id=raw["id"],
                nome_canonico=raw["nome_canonico"],
                categoria=raw["categoria"],
                quartiere=raw.get("quartiere"),
                coords=Coords(float(c["x"]), float(c["z"]), float(c["y"])),
                descrizione_breve=raw.get("descrizione_breve", ""),
                porta_socchiusa=bool(raw.get("porta_socchiusa", False)),
            )
            self._locations[loc.id] = loc

        self._edges: list[Edge] = []
        self._adj: dict[str, list[tuple[str, float]]] = {
            lid: [] for lid in self._locations
        }
        for raw in path_doc["edges"]:
            e = Edge(
                from_id=raw["from"],
                to_id=raw["to"],
                via=raw.get("via"),
                distance_m=float(raw["distance_m"]),
                difficulty=raw.get("difficulty", "easy"),
            )
            self._edges.append(e)
            # grafo non direzionato
            self._adj.setdefault(e.from_id, []).append((e.to_id, e.distance_m))
            self._adj.setdefault(e.to_id, []).append((e.from_id, e.distance_m))

        self._named_routes: list[dict[str, Any]] = list(
            path_doc.get("named_routes", [])
        )

    # ------------------------------------------------------------------
    # Lookup base
    # ------------------------------------------------------------------

    def location(self, id: str) -> Location:
        if id not in self._locations:
            raise KeyError(f"Location sconosciuta: {id!r}")
        return self._locations[id]

    def all_locations(self) -> list[Location]:
        # ordinamento deterministico per id
        return [self._locations[k] for k in sorted(self._locations)]

    def quartieri(self) -> list[dict[str, Any]]:
        return list(self._island["quartieri"])

    def island_bounds(self) -> dict[str, Any]:
        return dict(self._island["island"]["bounds"])

    # ------------------------------------------------------------------
    # Distanze e tempi
    # ------------------------------------------------------------------

    def distance(self, a: str, b: str) -> float:
        """Distanza in linea retta (3D euclidea) in metri."""
        la = self.location(a)
        lb = self.location(b)
        return _euclidean(la.coords, lb.coords)

    def path_distance(self, a: str, b: str) -> float:
        """Distanza lungo la rete sentieri (somma archi Dijkstra).
        Se i due nodi non sono connessi, fallback alla linea retta."""
        route = self.path(a, b)
        if len(route) < 2:
            return self.distance(a, b)
        total = 0.0
        for i in range(len(route) - 1):
            u, v = route[i], route[i + 1]
            # cerca l'arco (u,v) nella adiacenza
            step = None
            for nb, d in self._adj.get(u, []):
                if nb == v:
                    step = d
                    break
            if step is None:
                # non dovrebbe accadere: path() ritorna un cammino consistente
                step = self.distance(u, v)
            total += step
        return total

    def walking_time(
        self, a: str, b: str, speed: SpeedPreset = "adult_walk"
    ) -> float:
        """Tempo di percorrenza in minuti, lungo la rete sentieri
        (fallback: linea retta se i nodi non sono connessi).

        Il preset controlla solo la velocità; non modella la difficoltà
        degli archi (steep/sandy) — quella è informativa sull'arco.
        """
        if speed not in WALKING_SPEEDS_MPS:
            raise ValueError(
                f"Preset velocità sconosciuto: {speed!r}. "
                f"Valori ammessi: {sorted(WALKING_SPEEDS_MPS)}"
            )
        mps = WALKING_SPEEDS_MPS[speed]
        meters = self.path_distance(a, b)
        return (meters / mps) / 60.0  # secondi -> minuti

    # ------------------------------------------------------------------
    # Pathfinding
    # ------------------------------------------------------------------

    def path(self, a: str, b: str) -> list[str]:
        """Sequenza di location id per il percorso più breve nella rete
        sentieri (Dijkstra sui pesi distance_m di paths.json).

        Se a o b sono sconosciuti: KeyError.
        Se non esiste cammino nella rete: ritorna [a, b] (edge virtuale
        in linea retta — usato dai punti extra-rete come isole offshore).
        """
        if a not in self._locations:
            raise KeyError(f"Location sconosciuta: {a!r}")
        if b not in self._locations:
            raise KeyError(f"Location sconosciuta: {b!r}")
        if a == b:
            return [a]

        # Dijkstra
        dist: dict[str, float] = {a: 0.0}
        prev: dict[str, str | None] = {a: None}
        pq: list[tuple[float, str]] = [(0.0, a)]
        visited: set[str] = set()

        while pq:
            d, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            if u == b:
                break
            for v, w in sorted(self._adj.get(u, [])):
                nd = d + w
                if nd < dist.get(v, math.inf):
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))

        if b not in dist:
            # nodi non connessi: ritorna cammino virtuale
            return [a, b]

        # ricostruisci
        route: list[str] = []
        cur: str | None = b
        while cur is not None:
            route.append(cur)
            cur = prev.get(cur)
        route.reverse()
        return route

    # ------------------------------------------------------------------
    # Query spaziali
    # ------------------------------------------------------------------

    def nearby(self, loc: str, radius_m: float = 500) -> list[str]:
        """Id delle location entro radius_m (linea retta) da loc.
        Esclude loc stessa. Ordinate per distanza crescente, poi id."""
        center = self.location(loc)
        out: list[tuple[float, str]] = []
        for other in self._locations.values():
            if other.id == loc:
                continue
            d = _euclidean(center.coords, other.coords)
            if d <= radius_m:
                out.append((d, other.id))
        out.sort(key=lambda r: (r[0], r[1]))
        return [oid for _, oid in out]

    def quartiere_of(self, loc: str) -> str | None:
        """Il quartiere che contiene loc, o None per feature extra-quartiere
        (fiume, guado, isole offshore)."""
        return self.location(loc).quartiere

    def elevation(self, loc: str) -> float:
        return self.location(loc).coords.y

    def visible_from(
        self, loc: str, elevation_bonus_m: float = 0
    ) -> list[str]:
        """Euristica semplice (non line-of-sight reale) di visibilità:

        Una location B è considerata visibile da A se vale almeno una di:
        - elevation(A) + elevation_bonus > elevation(B)
          (A guarda verso il basso o alla stessa quota)
        - elevation(A) >= 100m AND distance(A,B) <= 3000m
          (punto panoramico: orizzonte libero a breve-media distanza)

        Esclude A stessa e le porte_socchiuse (non sono 'nell'isola').
        Ordine: distanza crescente, poi id.

        Approssimazione: non tiene conto di ostacoli intermedi
        (Montagne Gemelle tra osservatore e valle, per esempio).
        """
        center = self.location(loc)
        ea = center.coords.y + elevation_bonus_m
        out: list[tuple[float, str]] = []
        for other in self._locations.values():
            if other.id == loc:
                continue
            if other.porta_socchiusa:
                continue
            d = _euclidean(center.coords, other.coords)
            visible = False
            if ea > other.coords.y:
                visible = True
            elif center.coords.y >= 100 and d <= 3000:
                visible = True
            if visible:
                out.append((d, other.id))
        out.sort(key=lambda r: (r[0], r[1]))
        return [oid for _, oid in out]

    # ------------------------------------------------------------------
    # Introspezione
    # ------------------------------------------------------------------

    def edges(self) -> list[Edge]:
        return list(self._edges)

    def named_routes(self) -> list[dict[str, Any]]:
        return list(self._named_routes)
