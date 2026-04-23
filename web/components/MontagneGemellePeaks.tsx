"use client";

import { useMemo } from "react";
import type { TerrainDoc } from "@/lib/geography";
import { PALETTE, metersToUnits } from "@/lib/geography";
import { RELIEF_AMPLIFICATION } from "./TerrainHeightmap";

type Props = {
  terrain: TerrainDoc;
};

/**
 * Montagne Gemelle — indicatori geometrici a L0 per rendere visibili DUE
 * vette distinte sopra il terreno heightmap-IDW.
 *
 * Canone: terrain.json::heightmap_anchors include peak_west (x=-150, z=-2820,
 * y=450) e peak_east (x=180, z=-2780, y=445). L'IDW della heightmap già
 * solleva il terreno in quei punti, ma al L0 aerial l'interpolazione
 * smorza la separazione visiva. Aggiungiamo due piccoli coni (ConeGeometry
 * low-poly flat-shaded) sulla sommità di ciascun anchor, color warm stone,
 * + un piccolo "snow cap" bianco-crema in cima.
 *
 * La y del cono è calcolata con RELIEF_AMPLIFICATION perché il terreno
 * renderizzato è ~2.5× più alto dei dati canonici (amplificazione artistica
 * rendering-only; dati in terrain.json restano immutati).
 *
 * Budget:
 *   - cono warm stone: ConeGeometry radialSegments=6 heightSegments=1 → 12
 *     triangoli ciascuno (6 lati + 6 base) × 2 picchi = 24 tri
 *   - snow cap: ConeGeometry 6 radial = 12 tri × 2 = 24 tri
 *   Totale ≈ 48 triangoli.
 */
export default function MontagneGemellePeaks({ terrain }: Props) {
  const peaks = useMemo(() => {
    const anchors = terrain.heightmap_anchors.filter(
      (a) => a.label === "peak_west" || a.label === "peak_east",
    );
    return anchors.map((a) => ({
      label: a.label,
      x: metersToUnits(a.x),
      // RELIEF_AMPLIFICATION è applicato al terreno, così i coni spuntano
      // correttamente *sopra* la cima del picco già amplificato.
      yGround: metersToUnits(a.y) * RELIEF_AMPLIFICATION,
      z: metersToUnits(a.z),
    }));
  }, [terrain]);

  return (
    <group>
      {peaks.map((p) => (
        <Peak key={p.label} x={p.x} yGround={p.yGround} z={p.z} />
      ))}
    </group>
  );
}

function Peak({ x, yGround, z }: { x: number; yGround: number; z: number }) {
  // Altezza aggiuntiva del cono sopra il terreno (unità Three).
  // ~2.0u = 200m di vetta "estrusa" sopra la heightmap.
  const coneH = 2.0;
  const coneR = 1.1;
  // Snow cap: ~25% dell'altezza in cima.
  const capH = 0.5;
  const capR = coneR * 0.38;

  return (
    <group position={[x, yGround, z]}>
      {/* Corpo della vetta — warm stone, flat-shading per far leggere le
          facce come roccia squadrata. */}
      <mesh position={[0, coneH / 2, 0]} castShadow receiveShadow>
        <coneGeometry args={[coneR, coneH, 6, 1]} />
        <meshStandardMaterial
          color="#6b5a48"
          roughness={0.95}
          flatShading
        />
      </mesh>
      {/* Snow cap in cima — cream, flat-shading. Sale leggermente sopra
          il cono principale per dare l'impressione di neve in vetta. */}
      <mesh position={[0, coneH + capH / 2 - 0.05, 0]} castShadow>
        <coneGeometry args={[capR, capH, 6, 1]} />
        <meshStandardMaterial
          color={PALETTE.cream}
          roughness={0.7}
          flatShading
        />
      </mesh>
    </group>
  );
}
