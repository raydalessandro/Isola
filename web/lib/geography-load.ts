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
  type IslandGeographyData,
  type LocationsDoc,
  type PathsDoc,
} from "./geography";

function resolveGeoDir(baseDir?: string): string {
  if (baseDir) return baseDir;
  // sotto Next (dev o build) il cwd è `web/`: saliamo di uno.
  return path.resolve(process.cwd(), "..", "world", "geography");
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
  return IslandGeography.fromData(island, locations, paths);
}
