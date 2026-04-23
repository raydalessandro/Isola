// Parity runner — esegue query geografia in TypeScript e stampa JSON.
// Invocato da test_parity.py (Python) tramite `node --experimental-strip-types`.
// Legge stdin (una query JSON o array di query) e scrive su stdout i risultati.
//
// Schema query: {"type": <string>, ...args}
//   distance     {"a": id, "b": id}                  -> {"value_m": number}
//   walking_time {"a": id, "b": id, "speed": preset} -> {"value_min": number}
//   path         {"a": id, "b": id}                  -> {"route": string[]}
//   path_distance{"a": id, "b": id}                  -> {"value_m": number}
//   nearby       {"loc": id, "radius_m": number}     -> {"ids": string[]}
//   quartiere_of {"loc": id}                          -> {"quartiere": string|null}
//   elevation    {"loc": id}                          -> {"value_m": number}
//
// Sorgente TS: ../../web/lib/geography.ts

import { readFileSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";
import {
  IslandGeography,
  type FeaturesDoc,
  type IslandGeographyData,
  type LocationsDoc,
  type PathsDoc,
  type SpeedPreset,
  type TerrainDoc,
} from "../../web/lib/geography.ts";

const here = dirname(fileURLToPath(import.meta.url));
const geoDir = resolve(here, "..", "..", "world", "geography");

const island = JSON.parse(
  readFileSync(resolve(geoDir, "island.json"), "utf-8"),
) as IslandGeographyData;
const locations = JSON.parse(
  readFileSync(resolve(geoDir, "locations.json"), "utf-8"),
) as LocationsDoc;
const paths = JSON.parse(
  readFileSync(resolve(geoDir, "paths.json"), "utf-8"),
) as PathsDoc;

function readOpt<T>(p: string): T | null {
  if (!existsSync(p)) return null;
  return JSON.parse(readFileSync(p, "utf-8")) as T;
}

const features = readOpt<FeaturesDoc>(resolve(geoDir, "features.json"));
const terrain = readOpt<TerrainDoc>(resolve(geoDir, "terrain.json"));

const geo = IslandGeography.fromData(
  island,
  locations,
  paths,
  features,
  terrain,
);

type Query =
  | { type: "distance"; a: string; b: string }
  | { type: "walking_time"; a: string; b: string; speed: SpeedPreset }
  | { type: "path"; a: string; b: string }
  | { type: "path_distance"; a: string; b: string }
  | { type: "nearby"; loc: string; radius_m: number }
  | { type: "quartiere_of"; loc: string }
  | { type: "elevation"; loc: string }
  | { type: "distance_to_river"; loc: string }
  | { type: "terrain_profile"; quartiere: string }
  | { type: "anchor_points_count" };

function runQuery(q: Query): unknown {
  switch (q.type) {
    case "distance":
      return { value_m: geo.distance(q.a, q.b) };
    case "walking_time":
      return { value_min: geo.walkingTime(q.a, q.b, q.speed) };
    case "path":
      return { route: geo.path(q.a, q.b) };
    case "path_distance":
      return { value_m: geo.pathDistance(q.a, q.b) };
    case "nearby":
      return { ids: geo.nearby(q.loc, q.radius_m) };
    case "quartiere_of":
      return { quartiere: geo.quartiereOf(q.loc) };
    case "elevation":
      return { value_m: geo.elevation(q.loc) };
    case "distance_to_river":
      return { value_m: geo.distanceToRiver(q.loc) };
    case "terrain_profile":
      return { profile: geo.terrainProfile(q.quartiere) };
    case "anchor_points_count":
      return { count: geo.anchorPoints().length };
  }
}

const raw = readFileSync(0, "utf-8");
const input = JSON.parse(raw);
const queries: Query[] = Array.isArray(input) ? input : [input];
const results = queries.map((q) => runQuery(q));
process.stdout.write(JSON.stringify(results));
