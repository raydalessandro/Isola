import fs from "node:fs";
import path from "node:path";
import type {
  FeaturesDoc,
  IslandGeographyData,
  LocationsDoc,
  TerrainDoc,
} from "./geography";

/**
 * Server-side loader: reads the canonical world data from the repo root at
 * build/render time. These files live OUTSIDE the `web/` app so the narrative
 * source of truth is decoupled from the PWA shell.
 */

export type WorldIndex = {
  version: string;
  avatars: Array<{
    id: string;
    nome_canonico: string;
    categoria: string;
    path: string;
  }>;
  characters: Array<{
    id: string;
    nome_canonico: string;
    categoria: string;
    path: string;
  }>;
};

function repoRoot(): string {
  // When running under Next (dev or build) the cwd is `web/`.
  return path.resolve(process.cwd(), "..");
}

export function loadWorldIndex(): WorldIndex | null {
  try {
    const p = path.join(repoRoot(), "world", "_index.json");
    const raw = fs.readFileSync(p, "utf-8");
    return JSON.parse(raw) as WorldIndex;
  } catch {
    return null;
  }
}

export function loadIslandGeography(): IslandGeographyData {
  const p = path.join(repoRoot(), "world", "geography", "island.json");
  const raw = fs.readFileSync(p, "utf-8");
  return JSON.parse(raw) as IslandGeographyData;
}

export function loadLocations(): LocationsDoc {
  const p = path.join(repoRoot(), "world", "geography", "locations.json");
  const raw = fs.readFileSync(p, "utf-8");
  return JSON.parse(raw) as LocationsDoc;
}

export function loadFeatures(): FeaturesDoc {
  const p = path.join(repoRoot(), "world", "geography", "features.json");
  const raw = fs.readFileSync(p, "utf-8");
  return JSON.parse(raw) as FeaturesDoc;
}

export function loadTerrain(): TerrainDoc {
  const p = path.join(repoRoot(), "world", "geography", "terrain.json");
  const raw = fs.readFileSync(p, "utf-8");
  return JSON.parse(raw) as TerrainDoc;
}
