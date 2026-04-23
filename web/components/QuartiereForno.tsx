"use client";

import { useMemo, useRef } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";
import type { Location } from "@/lib/geography";
import { PALETTE, metersToUnits } from "@/lib/geography";
import LowPolyTree from "./LowPolyTree";

// Allinea i building tile alla superficie amplificata del terreno
// (vedi TerrainHeightmap::RELIEF_AMPLIFICATION). Dati canonici intatti.
const RELIEF = 2.5;
const liftY = (m: number) => metersToUnits(m) * RELIEF;

type Props = {
  locations: Location[];
};

/**
 * Dettaglio low-poly del quartiere del Forno, visibile quando il viewer
 * scende a L1 su quartiere "forno".
 *
 * Componenti:
 *  B.1 Forno di Fiamma — base stone + tetto thatched + camino + porta +
 *      due finestre emissive che flickerano (B.6).
 *  B.2 Case del Mattino — cottage più piccolo con tetto a prisma triangolare.
 *  B.3 Catasta di legna — 6 box impilati warm-brown, decorativa.
 *  B.4 Alberi sparsi — 6 LowPolyTree con rotazione/offset deterministici.
 *
 * Tutte le coordinate sono in METRI nei JSON sorgente; convertiamo una
 * volta a unità Three (1 u = 100 m) tramite metersToUnits. Le dimensioni
 * dei building, descritte in metri nei commenti, vengono espresse in
 * unità Three: es. 15 m × 10 m × 12 m → 0.15 × 0.10 × 0.12 u.
 *
 * Il fumo sul camino è GIÀ fornito dal componente Breathing/Smoke che vive
 * sopra il centro del quartiere; non duplichiamo (B.5).
 */
export default function QuartiereForno({ locations }: Props) {
  const fornoLoc = useMemo(
    () => locations.find((l) => l.id === "forno_di_fiamma"),
    [locations],
  );
  const casaMattinoLoc = useMemo(
    () => locations.find((l) => l.id === "casa_del_mattino"),
    [locations],
  );

  if (!fornoLoc) return null;

  const fx = metersToUnits(fornoLoc.coords.x);
  const fy = liftY(fornoLoc.coords.y);
  const fz = metersToUnits(fornoLoc.coords.z);

  return (
    <group>
      <FornoBuilding x={fx} y={fy} z={fz} />
      <LegnaStack
        x={fx + 0.1}
        y={fy}
        z={fz + 0.08}
      />
      {casaMattinoLoc && (
        <CasaDelMattino
          x={metersToUnits(casaMattinoLoc.coords.x)}
          y={liftY(casaMattinoLoc.coords.y)}
          z={metersToUnits(casaMattinoLoc.coords.z)}
        />
      )}
      <ForestSparse centerX={fx} centerZ={fz} groundY={fy} />
    </group>
  );
}

// ---------------------------------------------------------------------------
// B.1 Forno di Fiamma
// ---------------------------------------------------------------------------

function FornoBuilding({ x, y, z }: { x: number; y: number; z: number }) {
  // Misure in unità Three (metri / 100).
  //   base: 15m × 10m × 12m  →  0.15 × 0.10 × 0.12
  //   tetto: 15m × 4m × 14m  →  0.15 × 0.04 × 0.14
  //   camino: 2m × 8m × 2m   →  0.02 × 0.08 × 0.02
  //   porta: 2m × 3m         →  0.02 × 0.03
  // Ma a L1 la camera è a ~45u dal centro; con 1u=100m questo significa che
  // un edificio di 15m = 0.15u sarebbe invisibile. L'oggetto deve avere
  // PRESENZA a schermo → moltiplichiamo per un fattore "leggibilità"
  // artistico (10×) per renderlo iconico alla scala del gioco, come si fa
  // normalmente nelle mappe illustrate (Gorogoa/Tearaway).
  const SCALE = 10; // artistic amplification: 15m → 1.5u
  const baseW = 0.15 * SCALE; // 1.5
  const baseH = 0.1 * SCALE; // 1.0
  const baseD = 0.12 * SCALE; // 1.2
  const roofH = 0.04 * SCALE; // 0.4
  const roofW = 0.15 * SCALE; // 1.5
  const roofD = 0.14 * SCALE; // 1.4
  const chimH = 0.08 * SCALE; // 0.8
  const chimS = 0.02 * SCALE; // 0.2

  const stone = "#8a7a6a"; // warm-grey stone
  const stoneDark = "#5a4d40";
  const thatch = PALETTE.warmBrown;
  const doorColor = "#2f2418";

  // Flickering emissive windows — B.6
  const leftWinRef = useRef<THREE.MeshStandardMaterial>(null);
  const rightWinRef = useRef<THREE.MeshStandardMaterial>(null);
  useFrame(({ clock }) => {
    const t = clock.getElapsedTime();
    const base = 1.4;
    // Due fasi diverse, respiro lento + piccola perturbazione alta frequenza.
    const f1 = base + Math.sin(t * 1.6) * 0.25 + Math.sin(t * 7.0) * 0.08;
    const f2 = base + Math.sin(t * 1.3 + 1.7) * 0.25 + Math.sin(t * 6.5 + 0.9) * 0.08;
    if (leftWinRef.current) leftWinRef.current.emissiveIntensity = f1;
    if (rightWinRef.current) rightWinRef.current.emissiveIntensity = f2;
  });

  // Posizioniamo tutto in un group locale, la base appoggiata sul terreno.
  return (
    <group position={[x, y, z]}>
      {/* base stone */}
      <mesh position={[0, baseH / 2, 0]} castShadow receiveShadow>
        <boxGeometry args={[baseW, baseH, baseD]} />
        <meshStandardMaterial
          color={stone}
          roughness={0.95}
          flatShading
        />
      </mesh>

      {/* roof thatched — prism triangolare via box ruotato */}
      <mesh position={[0, baseH + roofH / 2, 0]} castShadow>
        <boxGeometry args={[roofW, roofH, roofD]} />
        <meshStandardMaterial color={thatch} roughness={0.9} flatShading />
      </mesh>

      {/* chimney — retro = +z nel frame locale (scelta arbitraria) */}
      <mesh
        position={[baseW * 0.28, baseH + chimH / 2, -baseD * 0.35]}
        castShadow
      >
        <boxGeometry args={[chimS, chimH, chimS]} />
        <meshStandardMaterial
          color={stoneDark}
          roughness={0.95}
          flatShading
        />
      </mesh>

      {/* porta — facciata sud (+z locale) */}
      <mesh
        position={[0, 0.03 * SCALE * 0.5 + (0.03 * SCALE) / 2, baseD / 2 + 0.001]}
      >
        <boxGeometry args={[0.02 * SCALE, 0.03 * SCALE, 0.005 * SCALE]} />
        <meshStandardMaterial
          color={doorColor}
          roughness={0.85}
          flatShading
        />
      </mesh>

      {/* finestre ai lati della porta — emettono luce calda */}
      <mesh
        position={[-baseW * 0.28, baseH * 0.6, baseD / 2 + 0.002]}
      >
        <planeGeometry args={[0.018 * SCALE, 0.02 * SCALE]} />
        <meshStandardMaterial
          ref={leftWinRef}
          color={PALETTE.sun}
          emissive={PALETTE.sun}
          emissiveIntensity={1.4}
          roughness={0.6}
          toneMapped={false}
        />
      </mesh>
      <mesh
        position={[baseW * 0.28, baseH * 0.6, baseD / 2 + 0.002]}
      >
        <planeGeometry args={[0.018 * SCALE, 0.02 * SCALE]} />
        <meshStandardMaterial
          ref={rightWinRef}
          color={PALETTE.sun}
          emissive={PALETTE.sun}
          emissiveIntensity={1.4}
          roughness={0.6}
          toneMapped={false}
        />
      </mesh>

      {/* piccolo alone caldo ai piedi del building dal flicker dei fuochi */}
      <pointLight
        color={PALETTE.sun}
        intensity={0.35}
        distance={2.8}
        decay={1.5}
        position={[0, baseH * 0.4, baseD / 2 + 0.3]}
      />
    </group>
  );
}

// ---------------------------------------------------------------------------
// B.2 Casa del Mattino
// ---------------------------------------------------------------------------

function CasaDelMattino({ x, y, z }: { x: number; y: number; z: number }) {
  // 8m × 5m × 8m  → 0.08 × 0.05 × 0.08 × SCALE(10) = 0.8 × 0.5 × 0.8
  const SCALE = 10;
  const w = 0.08 * SCALE;
  const h = 0.05 * SCALE;
  const d = 0.08 * SCALE;
  const roofH = 0.035 * SCALE;

  return (
    <group position={[x, y, z]}>
      <mesh position={[0, h / 2, 0]} castShadow receiveShadow>
        <boxGeometry args={[w, h, d]} />
        <meshStandardMaterial
          color={PALETTE.cream}
          roughness={0.85}
          flatShading
        />
      </mesh>
      {/* tetto prisma: due facce inclinate approssimate da un box appiattito */}
      <mesh
        position={[0, h + roofH / 2, 0]}
        rotation={[0, Math.PI / 4, 0]}
        castShadow
      >
        <coneGeometry args={[w * 0.75, roofH, 4]} />
        <meshStandardMaterial
          color={PALETTE.warmBrown}
          roughness={0.9}
          flatShading
        />
      </mesh>
      {/* singola finestra est (+x) */}
      <mesh position={[w / 2 + 0.002, h * 0.55, 0]}>
        <planeGeometry args={[0.018 * SCALE, 0.02 * SCALE]} />
        <meshStandardMaterial
          color={PALETTE.sun}
          emissive={PALETTE.sun}
          emissiveIntensity={0.55}
          roughness={0.7}
          toneMapped={false}
        />
      </mesh>
    </group>
  );
}

// ---------------------------------------------------------------------------
// B.3 Catasta di legna
// ---------------------------------------------------------------------------

function LegnaStack({ x, y, z }: { x: number; y: number; z: number }) {
  // 5m × 2m × 3m → 0.05 × 0.02 × 0.03 × SCALE = 0.5 × 0.2 × 0.3
  const SCALE = 10;
  const logs = useMemo(() => {
    // 6 pezzi impilati a fasce, rotazione deterministica per varietà.
    const out: Array<{
      px: number;
      py: number;
      pz: number;
      rx: number;
      ry: number;
      sx: number;
    }> = [];
    const rowHeights = [0.006, 0.018, 0.03]; // tre livelli
    for (let row = 0; row < 3; row++) {
      for (let i = 0; i < 2; i++) {
        out.push({
          px: (i - 0.5) * 0.012 * SCALE,
          py: rowHeights[row] * SCALE + 0.005 * SCALE,
          pz: 0,
          rx: 0,
          ry: ((row + i) % 2 === 0 ? 0.12 : -0.12),
          sx: 1 + (row * 0.03),
        });
      }
    }
    return out;
  }, []);

  return (
    <group position={[x, y, z]}>
      {logs.map((l, i) => (
        <mesh
          key={i}
          position={[l.px, l.py, l.pz]}
          rotation={[l.rx, l.ry, Math.PI / 2]}
          castShadow
        >
          <cylinderGeometry
            args={[0.005 * SCALE, 0.005 * SCALE, 0.05 * SCALE * l.sx, 6]}
          />
          <meshStandardMaterial
            color={PALETTE.warmBrown}
            roughness={0.95}
            flatShading
          />
        </mesh>
      ))}
    </group>
  );
}

// ---------------------------------------------------------------------------
// B.4 Alberi sparsi nel quartiere (warm_hill, density: sparse)
// ---------------------------------------------------------------------------

function ForestSparse({
  centerX,
  centerZ,
  groundY,
}: {
  centerX: number;
  centerZ: number;
  groundY: number;
}) {
  // 6 posizioni deterministiche attorno al centro del quartiere, evitando
  // il raggio immediato del forno (~0.6u). Distribuzione radiale poissoniana
  // approssimata a mano con offset angolari irregolari.
  const placements = useMemo(() => {
    const seeds = [
      { dx: -1.8, dz: -1.5, r: 0.9, h: 0.035 },
      { dx: 2.1, dz: -1.1, r: -0.4, h: 0.042 },
      { dx: -2.3, dz: 1.4, r: 1.8, h: 0.038 },
      { dx: 1.6, dz: 2.0, r: -2.1, h: 0.033 },
      { dx: -0.4, dz: -2.4, r: 0.6, h: 0.04 },
      { dx: 2.6, dz: 0.3, r: 2.5, h: 0.036 },
    ];
    return seeds;
  }, []);

  return (
    <group>
      {placements.map((p, i) => (
        <LowPolyTree
          key={i}
          position={[centerX + p.dx, groundY, centerZ + p.dz]}
          height={p.h * 10}
          rotationY={p.r}
        />
      ))}
    </group>
  );
}
