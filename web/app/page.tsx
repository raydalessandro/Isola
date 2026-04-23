import IslandScene from "@/components/IslandScene";
import { loadIslandGeography, loadWorldIndex } from "@/lib/world";

export const dynamic = "force-static";

export default function Home() {
  const geography = loadIslandGeography();
  const world = loadWorldIndex();

  // world/_index.json is loaded to prove the pipeline works and to have
  // it ready for future expansion (e.g. NPC pins). Currently we only
  // surface a count so the build-time read is not dead-stripped.
  const charCount = (world?.characters?.length ?? 0) + (world?.avatars?.length ?? 0);

  return (
    <main data-char-count={charCount}>
      <IslandScene geography={geography} />
    </main>
  );
}
