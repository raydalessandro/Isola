/**
 * Loader server-only della geografia. Legge `world/geography/*.json` da
 * disco e costruisce un'istanza `IslandGeography`.
 *
 * NON importare questo modulo da componenti client: userebbe `fs`.
 * Per consumi client-side, passa l'istanza pre-costruita via props
 * oppure usa direttamente i tipi puri in `./geography`.
 */
import "server-only";
import fs from "node:fs";
import path from "node:path";
import {
  IslandGeography,
  type FeaturesDoc,
  type IslandGeographyData,
  type LocationsDoc,
  type PathsDoc,
  type TerrainDoc,
} from "./geography";

function resolveGeoDir(baseDir?: string): string {
  if (baseDir) return baseDir;
  // sotto Next (dev o build) il cwd è `web/`: saliamo di uno.
  return path.resolve(process.cwd(), "..", "world", "geography");
}

function readJsonIfExists<T>(filePath: string): T | null {
  if (!fs.existsSync(filePath)) return null;
  return JSON.parse(fs.readFileSync(filePath, "utf-8")) as T;
}

export function loadGeography(baseDir?: string): IslandGeography {
  const dir = resolveGeoDir(baseDir);
  const island = JSON.parse(
    fs.readFileSync(path.join(dir, "island.json"), "utf-8"),
  ) as IslandGeographyData;
  const locations = JSON.parse(
    fs.readFileSync(path.join(dir, "locations.json"), "utf-8"),
  ) as LocationsDoc;
  const paths = JSON.parse(
    fs.readFileSync(path.join(dir, "paths.json"), "utf-8"),
  ) as PathsDoc;
  // features e terrain sono tolleranti: se mancano, retrocompat.
  const features = readJsonIfExists<FeaturesDoc>(
    path.join(dir, "features.json"),
  );
  const terrain = readJsonIfExists<TerrainDoc>(path.join(dir, "terrain.json"));
  return IslandGeography.fromData(island, locations, paths, features, terrain);
}
