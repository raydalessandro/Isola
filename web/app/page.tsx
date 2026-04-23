import IslandScene from "@/components/IslandScene";
import {
  loadIslandGeography,
  loadLocations,
  loadWorldIndex,
} from "@/lib/world";

export const dynamic = "force-static";

export default function Home() {
  const geography = loadIslandGeography();
  const locationsDoc = loadLocations();
  const world = loadWorldIndex();

  // world/_index.json is loaded to prove the pipeline works and to have
  // it ready for future expansion (e.g. NPC pins). Currently we only
  // surface a count so the build-time read is not dead-stripped.
  const charCount = (world?.characters?.length ?? 0) + (world?.avatars?.length ?? 0);

  // Strip `fonti` (private metadata) before shipping to the client bundle.
  const locations = locationsDoc.locations.map((l) => ({
    id: l.id,
    nome_canonico: l.nome_canonico,
    categoria: l.categoria,
    quartiere: l.quartiere,
    coords: l.coords,
    descrizione_breve: l.descrizione_breve,
    porta_socchiusa: l.porta_socchiusa,
  }));

  return (
    <main data-char-count={charCount}>
      <IslandScene geography={geography} locations={locations} />
    </main>
  );
}
