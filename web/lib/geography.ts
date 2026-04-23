/**
 * Geografia dell'Isola dei Tre Venti — mirror TypeScript del modulo Python
 * in `tools/geography.py`. Stessa semantica, stessi preset, stesso algoritmo.
 *
 * Sorgente di verità: `world/geography/*.json` (fuori da `web/`).
 *
 * Convenzione coordinate: Three.js. Origine (0,0) = Albero Vecchio.
 * est=+x, sud=+z, su=+y. Unità nel JSON: metri.
 *
 * Questo file è client-safe (nessun import Node). La funzione di caricamento
 * da filesystem sta in `geography-load.ts` (server-only).
 */

// ---------------------------------------------------------------------------
// Preset velocità canoniche — m/s
// ---------------------------------------------------------------------------

export const WALKING_SPEEDS_MPS = {
  adult_walk: 1.2,
  child_walk: 0.8,
  bartolo_walk: 0.4,
  child_run: 2.0,
} as const;

export type SpeedPreset = keyof typeof WALKING_SPEEDS_MPS;

/**
 * Moltiplicatore sul tempo mechanical per difficulty del terreno.
 * Applicato solo agli edges senza canonical_time_min (fallback).
 */
export const DIFFICULTY_MULTIPLIER: Record<string, number> = {
  easy: 1.0,
  steep: 2.5,
  sandy: 1.3,
};

/** Velocità baseline usata per i tempi canonical (Bibbia §8.1 = adult_walk). */
const BASELINE_SPEED: SpeedPreset = "adult_walk";

// ---------------------------------------------------------------------------
// Tipi dati (shape dei JSON in world/geography/)
// ---------------------------------------------------------------------------

export type Coords = {
  x: number;
  z: number;
  y: number;
};

export type Quartiere = {
  id: string;
  label: string;
  center: { x: number; z: number };
  radius_m: number;
  elevation_m: number;
  color: string;
  descrizione: string;
};

/**
 * Shape di `world/geography/island.json` (bounds + 5 quartieri).
 * Storicamente chiamato `IslandGeography`; rinominato in `IslandGeographyData`
 * per evitare collisione con la classe di query omonima.
 */
export type IslandGeographyData = {
  version: string;
  island: {
    bounds: {
      width_m: number;
      depth_m: number;
      unit_scale_three: number;
    };
    shape: "oval" | "circle" | "rect";
  };
  quartieri: Quartiere[];
  notes?: string;
};

export type Location = {
  id: string;
  nome_canonico: string;
  categoria: string;
  quartiere: string | null;
  coords: Coords;
  descrizione_breve: string;
  porta_socchiusa: boolean;
};

export type LocationRaw = Location & {
  fonti: string[];
};

export type LocationsDoc = {
  version: string;
  notes?: string;
  locations: LocationRaw[];
};

export type Edge = {
  from: string;
  to: string;
  via: string | null;
  distance_m: number;
  difficulty: "easy" | "steep" | "sandy";
  canonical_time_min?: number | null;
};

export type NamedRoute = {
  id: string;
  nome_canonico?: string;
  from_quartiere: string;
  to_quartiere: string;
};

export type PathsDoc = {
  version: string;
  notes?: string;
  named_routes: NamedRoute[];
  edges: Edge[];
};

// ---------------------------------------------------------------------------
// Features (polyline/polygon/cluster canonici)
// ---------------------------------------------------------------------------

/**
 * Whitelist dei tipi di feature accettati. Deve restare in parita'
 * con `tools/tests/test_geography.py::ALLOWED_FEATURE_TYPES`.
 */
export type FeatureType =
  | "polyline_open"
  | "polyline_closed"
  | "polygon"
  | "concentric_rings"
  | "structure_cluster"
  | "point_cluster";

export type Waypoint = { x: number; z: number; y?: number };

export type Feature = {
  type: FeatureType;
  description?: string;
  waypoints?: Waypoint[];
  vertices?: Array<{ x: number; z: number }>;
  center?: { x: number; z: number };
  rings?: Array<{ radius_m: number; content: string }>;
  structures?: Array<{
    id: string;
    position: Coords;
    type: string;
  }>;
  points?: Array<{ id: string; position: Coords }>;
  width_m_avg?: number;
  avg_elevation_m?: number;
  fonti?: string[];
};

export type FeaturesDoc = {
  version: string;
  notes?: string;
  features: Record<string, Feature>;
};

// ---------------------------------------------------------------------------
// Terrain profile per quartiere + heightmap anchor points
// ---------------------------------------------------------------------------

export type TerrainProfile =
  | "grassy_plain"
  | "warm_hill"
  | "sandy_coast"
  | "patchwork_cultivated"
  | "rocky_mountain"
  | "forest_margin";

export type QuartiereTerrainDetails = {
  profile: TerrainProfile;
  base_color: string;
  roughness: number;
  avg_elevation_m: number;
  trees_density: string;
  water_proximity: string;
};

export type HeightmapAnchor = {
  x: number;
  z: number;
  y: number;
  label: string;
};

export type TerrainDoc = {
  version: string;
  notes?: string;
  quartieri_profiles: Record<string, QuartiereTerrainDetails>;
  heightmap_anchors: HeightmapAnchor[];
  fonti?: string[];
};

// ---------------------------------------------------------------------------
// Helpers scena
// ---------------------------------------------------------------------------

/**
 * Convert a world coordinate (meters) to Three.js scene units.
 * 1 Three.js unit = 100 m (unit_scale_three). Three.js Y is up;
 * our canonical x = east, z = south (positive), y = elevation.
 */
export function metersToUnits(meters: number, scale = 100): number {
  return meters / scale;
}

/**
 * Palette — mirror of legacy/index.html CSS variables so the 3D scene
 * stays coherent with the paper-map prototype.
 */
export const PALETTE = {
  cream: "#f5ead5",
  creamShade: "#ebdebe",
  creamDeep: "#e0ceaa",
  terracotta: "#c8532c",
  terracottaDeep: "#9c3d1e",
  olive: "#5c6b3b",
  oliveLight: "#8a9a6b",
  sea: "#1e5d6e",
  seaLight: "#4a8595",
  seaDeep: "#0f3a48",
  ink: "#2a2319",
  warmBrown: "#6b4423",
  sun: "#e8a547",
  sand: "#d8bd8a",
} as const;

// ---------------------------------------------------------------------------
// API interrogabile (mirror di tools/geography.py::IslandGeography)
// ---------------------------------------------------------------------------

function euclidean(a: Coords, b: Coords): number {
  const dx = a.x - b.x;
  const dz = a.z - b.z;
  const dy = a.y - b.y;
  return Math.sqrt(dx * dx + dz * dz + dy * dy);
}

/**
 * Mini-heap binario (stdlib TS non include PriorityQueue).
 * Sufficiente per Dijkstra su poche decine di nodi.
 */
class MinHeap<T> {
  private items: Array<{ key: number; val: T }> = [];

  push(key: number, val: T): void {
    this.items.push({ key, val });
    this.bubbleUp(this.items.length - 1);
  }

  pop(): { key: number; val: T } | undefined {
    if (this.items.length === 0) return undefined;
    const top = this.items[0];
    const last = this.items.pop()!;
    if (this.items.length > 0) {
      this.items[0] = last;
      this.sinkDown(0);
    }
    return top;
  }

  get size(): number {
    return this.items.length;
  }

  private bubbleUp(i: number): void {
    while (i > 0) {
      const p = Math.floor((i - 1) / 2);
      if (this.items[p].key <= this.items[i].key) break;
      [this.items[p], this.items[i]] = [this.items[i], this.items[p]];
      i = p;
    }
  }

  private sinkDown(i: number): void {
    const n = this.items.length;
    while (true) {
      const l = 2 * i + 1;
      const r = 2 * i + 2;
      let smallest = i;
      if (l < n && this.items[l].key < this.items[smallest].key) smallest = l;
      if (r < n && this.items[r].key < this.items[smallest].key) smallest = r;
      if (smallest === i) break;
      [this.items[smallest], this.items[i]] = [
        this.items[i],
        this.items[smallest],
      ];
      i = smallest;
    }
  }
}

export class IslandGeography {
  private readonly island: IslandGeographyData;
  private readonly locs: Map<string, Location>;
  private readonly edgesList: Edge[];
  private readonly adj: Map<string, Array<[string, number]>>;
  private readonly edgeLookup: Map<string, Edge>;
  private readonly routes: NamedRoute[];
  private readonly featuresMap: Record<string, Feature>;
  private readonly terrainDoc: TerrainDoc | null;

  constructor(
    island: IslandGeographyData,
    locations: LocationsDoc,
    paths: PathsDoc,
    features?: FeaturesDoc | null,
    terrain?: TerrainDoc | null,
  ) {
    this.island = island;
    this.locs = new Map();
    for (const raw of locations.locations) {
      const loc: Location = {
        id: raw.id,
        nome_canonico: raw.nome_canonico,
        categoria: raw.categoria,
        quartiere: raw.quartiere,
        coords: {
          x: Number(raw.coords.x),
          z: Number(raw.coords.z),
          y: Number(raw.coords.y),
        },
        descrizione_breve: raw.descrizione_breve,
        porta_socchiusa: Boolean(raw.porta_socchiusa),
      };
      this.locs.set(loc.id, loc);
    }
    this.edgesList = paths.edges.map((e) => ({ ...e }));
    this.adj = new Map();
    this.edgeLookup = new Map();
    for (const id of this.locs.keys()) {
      this.adj.set(id, []);
    }
    for (const e of this.edgesList) {
      if (!this.adj.has(e.from)) this.adj.set(e.from, []);
      if (!this.adj.has(e.to)) this.adj.set(e.to, []);
      this.adj.get(e.from)!.push([e.to, e.distance_m]);
      this.adj.get(e.to)!.push([e.from, e.distance_m]);
      this.edgeLookup.set(`${e.from} ${e.to}`, e);
      this.edgeLookup.set(`${e.to} ${e.from}`, e);
    }
    this.routes = paths.named_routes.map((r) => ({ ...r }));
    this.featuresMap = features?.features ?? {};
    this.terrainDoc = terrain ?? null;
  }

  /** Costruisce da JSON già letti (client-side, test, ecc.) */
  static fromData(
    island: IslandGeographyData,
    locations: LocationsDoc,
    paths: PathsDoc,
    features?: FeaturesDoc | null,
    terrain?: TerrainDoc | null,
  ): IslandGeography {
    return new IslandGeography(island, locations, paths, features, terrain);
  }

  // ---------------- lookup ----------------

  location(id: string): Location {
    const l = this.locs.get(id);
    if (!l) throw new Error(`Location sconosciuta: ${id}`);
    return l;
  }

  allLocations(): Location[] {
    return Array.from(this.locs.values()).sort((a, b) =>
      a.id.localeCompare(b.id),
    );
  }

  quartieri(): Quartiere[] {
    return this.island.quartieri.map((q) => ({ ...q }));
  }

  islandBounds(): IslandGeographyData["island"]["bounds"] {
    return { ...this.island.island.bounds };
  }

  edges(): Edge[] {
    return this.edgesList.map((e) => ({ ...e }));
  }

  namedRoutes(): NamedRoute[] {
    return this.routes.map((r) => ({ ...r }));
  }

  // ---------------- distanza e tempo ----------------

  distance(a: string, b: string): number {
    return euclidean(this.location(a).coords, this.location(b).coords);
  }

  pathDistance(a: string, b: string): number {
    const route = this.path(a, b);
    if (route.length < 2) return this.distance(a, b);
    let total = 0;
    for (let i = 0; i < route.length - 1; i++) {
      const u = route[i];
      const v = route[i + 1];
      const nbrs = this.adj.get(u) ?? [];
      let step: number | null = null;
      for (const [nb, d] of nbrs) {
        if (nb === v) {
          step = d;
          break;
        }
      }
      total += step ?? this.distance(u, v);
    }
    return total;
  }

  /**
   * Tempo di percorrenza in minuti, per-edge sul cammino Dijkstra.
   * Policy (mirror di tools/geography.py::walking_time):
   * 1. edge con canonical_time_min (Bibbia §8.1, baseline adult_walk) →
   *    quel tempo scalato per il rapporto adult_walk / speed;
   * 2. altrimenti fallback mechanical distance/speed moltiplicato
   *    per DIFFICULTY_MULTIPLIER[difficulty].
   */
  walkingTime(a: string, b: string, speed: SpeedPreset = "adult_walk"): number {
    if (!(speed in WALKING_SPEEDS_MPS)) {
      throw new Error(`Preset velocità sconosciuto: ${speed}`);
    }
    if (!this.locs.has(a)) throw new Error(`Location sconosciuta: ${a}`);
    if (!this.locs.has(b)) throw new Error(`Location sconosciuta: ${b}`);
    if (a === b) return 0;

    const mps = WALKING_SPEEDS_MPS[speed];
    const baselineMps = WALKING_SPEEDS_MPS[BASELINE_SPEED];
    const speedRatio = baselineMps / mps;

    const route = this.path(a, b);
    if (route.length < 2) return 0;

    let totalMin = 0;
    for (let i = 0; i < route.length - 1; i++) {
      const u = route[i];
      const v = route[i + 1];
      const edge = this.edgeLookup.get(`${u} ${v}`);
      if (!edge) {
        const d = this.distance(u, v);
        totalMin += d / mps / 60;
        continue;
      }
      if (edge.canonical_time_min != null) {
        totalMin += edge.canonical_time_min * speedRatio;
      } else {
        const mult = DIFFICULTY_MULTIPLIER[edge.difficulty] ?? 1.0;
        totalMin += (edge.distance_m / mps / 60) * mult;
      }
    }
    return totalMin;
  }

  // ---------------- pathfinding ----------------

  /**
   * Dijkstra sulla rete sentieri. Se a==b → [a]. Se non connessi →
   * cammino virtuale [a,b] (parità con l'implementazione Python).
   */
  path(a: string, b: string): string[] {
    if (!this.locs.has(a)) throw new Error(`Location sconosciuta: ${a}`);
    if (!this.locs.has(b)) throw new Error(`Location sconosciuta: ${b}`);
    if (a === b) return [a];

    const dist = new Map<string, number>();
    const prev = new Map<string, string | null>();
    dist.set(a, 0);
    prev.set(a, null);
    const pq = new MinHeap<string>();
    pq.push(0, a);
    const visited = new Set<string>();

    while (pq.size > 0) {
      const entry = pq.pop()!;
      const u = entry.val;
      const d = entry.key;
      if (visited.has(u)) continue;
      visited.add(u);
      if (u === b) break;
      const nbrs = [...(this.adj.get(u) ?? [])].sort((x, y) => {
        if (x[0] < y[0]) return -1;
        if (x[0] > y[0]) return 1;
        return 0;
      });
      for (const [v, w] of nbrs) {
        const nd = d + w;
        const current = dist.has(v) ? dist.get(v)! : Number.POSITIVE_INFINITY;
        if (nd < current) {
          dist.set(v, nd);
          prev.set(v, u);
          pq.push(nd, v);
        }
      }
    }

    if (!dist.has(b)) {
      // non connesso: cammino virtuale
      return [a, b];
    }

    const route: string[] = [];
    let cur: string | null = b;
    while (cur !== null && cur !== undefined) {
      route.push(cur);
      cur = prev.get(cur) ?? null;
    }
    route.reverse();
    return route;
  }

  // ---------------- query spaziali ----------------

  nearby(loc: string, radiusM = 500): string[] {
    const center = this.location(loc).coords;
    const out: Array<{ d: number; id: string }> = [];
    for (const other of this.locs.values()) {
      if (other.id === loc) continue;
      const d = euclidean(center, other.coords);
      if (d <= radiusM) out.push({ d, id: other.id });
    }
    out.sort((x, y) => {
      if (x.d !== y.d) return x.d - y.d;
      return x.id.localeCompare(y.id);
    });
    return out.map((r) => r.id);
  }

  quartiereOf(loc: string): string | null {
    return this.location(loc).quartiere;
  }

  elevation(loc: string): number {
    return this.location(loc).coords.y;
  }

  /**
   * Euristica approssimata di visibilità (non true line-of-sight).
   * Vedi `tools/geography.py::visible_from` per il contratto semantico.
   */
  visibleFrom(loc: string, elevationBonusM = 0): string[] {
    const center = this.location(loc);
    const ea = center.coords.y + elevationBonusM;
    const out: Array<{ d: number; id: string }> = [];
    for (const other of this.locs.values()) {
      if (other.id === loc) continue;
      if (other.porta_socchiusa) continue;
      const d = euclidean(center.coords, other.coords);
      let visible = false;
      if (ea > other.coords.y) {
        visible = true;
      } else if (center.coords.y >= 100 && d <= 3000) {
        visible = true;
      }
      if (visible) out.push({ d, id: other.id });
    }
    out.sort((x, y) => {
      if (x.d !== y.d) return x.d - y.d;
      return x.id.localeCompare(y.id);
    });
    return out.map((r) => r.id);
  }

  // ---------------- features (polyline/polygon/cluster) ----------------

  /** Tutte le feature geografiche (river, forest, etc.). Copia difensiva. */
  features(): Record<string, Feature> {
    const out: Record<string, Feature> = {};
    for (const [k, v] of Object.entries(this.featuresMap)) {
      out[k] = { ...v };
    }
    return out;
  }

  /** Una feature per id. Throw se sconosciuta. */
  feature(featureId: string): Feature {
    const f = this.featuresMap[featureId];
    if (!f) throw new Error(`Feature sconosciuta: ${featureId}`);
    return { ...f };
  }

  // ---------------- terrain profile + heightmap anchors ----------------

  /** Profilo terreno di un quartiere (es. 'sandy_coast'). */
  terrainProfile(quartiereId: string): TerrainProfile {
    const profiles = this.terrainDoc?.quartieri_profiles ?? {};
    const p = profiles[quartiereId];
    if (!p) throw new Error(`Quartiere sconosciuto: ${quartiereId}`);
    return p.profile;
  }

  /** Dettagli completi profilo terreno. */
  terrainProfileDetails(quartiereId: string): QuartiereTerrainDetails {
    const profiles = this.terrainDoc?.quartieri_profiles ?? {};
    const p = profiles[quartiereId];
    if (!p) throw new Error(`Quartiere sconosciuto: ${quartiereId}`);
    return { ...p };
  }

  /** Anchor points per generazione heightmap. Copia difensiva. */
  anchorPoints(): HeightmapAnchor[] {
    const anchors = this.terrainDoc?.heightmap_anchors ?? [];
    return anchors.map((a) => ({ ...a }));
  }

  // ---------------- query spaziali su feature lineari ----------------

  /**
   * Distanza minima (m) da una location ai segmenti del Fiume che Gira
   * (proiezione xz, ignora elevazione). Coerente con
   * `tools/geography.py::distance_to_river`.
   */
  distanceToRiver(locationId: string): number {
    const loc = this.location(locationId);
    const river = this.featuresMap["fiume_che_gira"];
    if (!river) {
      throw new Error(
        "fiume_che_gira non presente in features.json; distanceToRiver non disponibile.",
      );
    }
    const wps = river.waypoints ?? [];
    if (wps.length < 2) {
      throw new Error("fiume_che_gira deve avere almeno 2 waypoints.");
    }
    const px = loc.coords.x;
    const pz = loc.coords.z;
    const n = wps.length;
    const isClosed = river.type === "polyline_closed";
    const last = isClosed ? n : n - 1;
    let best = Number.POSITIVE_INFINITY;
    for (let i = 0; i < last; i++) {
      const a = wps[i];
      const b = wps[(i + 1) % n];
      const d = pointToSegment2d(px, pz, a.x, a.z, b.x, b.z);
      if (d < best) best = d;
    }
    return best;
  }
}

function pointToSegment2d(
  px: number,
  pz: number,
  ax: number,
  az: number,
  bx: number,
  bz: number,
): number {
  const dx = bx - ax;
  const dz = bz - az;
  const lenSq = dx * dx + dz * dz;
  if (lenSq === 0) {
    return Math.sqrt((px - ax) ** 2 + (pz - az) ** 2);
  }
  let t = ((px - ax) * dx + (pz - az) * dz) / lenSq;
  if (t < 0) t = 0;
  else if (t > 1) t = 1;
  const qx = ax + t * dx;
  const qz = az + t * dz;
  return Math.sqrt((px - qx) ** 2 + (pz - qz) ** 2);
}
