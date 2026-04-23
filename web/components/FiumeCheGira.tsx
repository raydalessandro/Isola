"use client";

import { useMemo, useRef } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";
import type { FeaturesDoc } from "@/lib/geography";
import { PALETTE } from "@/lib/geography";

type Props = {
  features: FeaturesDoc;
  /** Scala metri → unità Three (1 u = 100 m). */
  scale?: number;
};

/**
 * Fiume che Gira — anello d'acqua visibile a L0.
 *
 * Consumiamo `features.json::fiume_che_gira` (polyline_closed, 15 waypoints).
 * Renderizziamo come TubeGeometry (CatmullRomCurve3 chiusa) → linea
 * liscia e con spessore visibile anche dalla vista aerea a ~120u di camera.
 *
 * Scelta Tube vs Line:
 *   - Line (THREE.Line) ha spessore 1px a schermo, indipendente dalla
 *     scena. A L0 il fiume sparirebbe su mobile.
 *   - LineGeometry/Line2 avrebbe richiesto l'import di addons. TubeGeometry
 *     è in core e produce volume reale, ombre, continuità, UV per animazione.
 *
 * Animazione "scorre": lievissimo offset UV sul materiale ogni frame → l'acqua
 * ha un senso di direzione antiorario senza essere vistosa.
 *
 * Elevazione: i waypoints hanno y in metri già coerente col terreno (2..20m).
 * Alziamo ulteriormente di ~1m (0.01u) per evitare z-fighting con la
 * heightmap; il tube ha radius 0.25u (25m) che emerge visibilmente.
 *
 * Source + Delta (rendering-only, canone intatto):
 *   - la polyline_closed narrativa si "apre" alla Bocca a sud — questa
 *     apertura è già tra last_waypoint (-200,2700) e first_waypoint (200,2700)
 *     nei dati features.json, quindi il delta è una continuazione naturale
 *     verso il mare a sud (z>2700), NON una modifica dei dati.
 *     Bibbia §3: "sfocia nel mare a sud attraverso La Bocca".
 *   - la sorgente alle Montagne Gemelle: aggiungiamo un piccolo cuneo di
 *     schiuma bianco-crema trasparente sul waypoint più a nord (z più
 *     negativo), dove nascono i ruscelli delle Gemelle.
 */

/** Waypoint index della sorgente (più a nord = z più negativo). */
function findSourceIndex(pts: THREE.Vector3[]): number {
  let idx = 0;
  let minZ = Infinity;
  for (let i = 0; i < pts.length; i++) {
    if (pts[i].z < minZ) {
      minZ = pts[i].z;
      idx = i;
    }
  }
  return idx;
}

export default function FiumeCheGira({ features, scale = 100 }: Props) {
  const materialRef = useRef<THREE.MeshStandardMaterial>(null!);

  const data = useMemo(() => {
    const river = features.features["fiume_che_gira"];
    if (!river || !river.waypoints || river.waypoints.length < 3) {
      return null;
    }

    // RELIEF: il terreno in scena è scalato rispetto ai metri canonici
    // (vedi TerrainHeightmap::RELIEF_AMPLIFICATION). La y del fiume deve
    // seguire la stessa amplificazione, altrimenti la tube affonda sotto
    // la superficie nei tratti più in alto (es. i waypoint sopra i 15m
    // vicino al bordo montano).
    const RELIEF = 2.5;
    const pts: THREE.Vector3[] = river.waypoints.map((w) => {
      return new THREE.Vector3(
        w.x / scale,
        ((w.y ?? 2) / scale) * RELIEF + 0.15, // +1m per anti-z-fight + lift
        w.z / scale,
      );
    });

    // Polyline chiusa: CatmullRom closed=true chiude automaticamente.
    const curve = new THREE.CatmullRomCurve3(pts, true, "catmullrom", 0.25);
    // tubularSegments 240, radialSegments 6 → 240*6*2=~2880 triangoli.
    const tube = new THREE.TubeGeometry(curve, 240, 0.22, 6, true);

    // Halo di umidità: stesso curve ma tubo più largo, basso sotto il fiume.
    // radialSegments 5 per contenere triangoli (~240*5*2=2400 tri).
    const halo = new THREE.TubeGeometry(curve, 200, 0.45, 5, true);

    // Source position: waypoint più a nord (più vicino alle Montagne Gemelle).
    const sourceIdx = findSourceIndex(pts);
    const sourcePos = pts[sourceIdx].clone();

    // Delta/Bocca: tra l'ultimo e il primo waypoint c'è lo spazio sud
    // narrativo della Bocca. Il midpoint (circa x=0, z=27 in unità, ~2700m)
    // proiettato oltre verso il mare (z+3) dà il delta.
    const first = pts[0];
    const last = pts[pts.length - 1];
    const mouthMid = new THREE.Vector3(
      (first.x + last.x) / 2,
      (first.y + last.y) / 2,
      (first.z + last.z) / 2,
    );
    // Direzione verso il mare = approssimativamente +z (sud).
    const deltaEnd = new THREE.Vector3(
      mouthMid.x,
      0.08, // leggermente sopra il mare
      mouthMid.z + 4.5, // +450m verso il mare = sfociata visibile a L0
    );

    return { tube, halo, sourcePos, mouthMid, deltaEnd };
  }, [features, scale]);

  // Leggerissimo UV offset per suggerire scorrimento.
  useFrame((_, dt) => {
    const mat = materialRef.current;
    if (!mat) return;
    if (mat.map) {
      mat.map.offset.x -= dt * 0.04;
    } else {
      // Senza map, moduliamo leggermente l'emissive per dare "respiro".
      mat.emissiveIntensity =
        0.15 + Math.sin(performance.now() * 0.0015) * 0.05;
    }
  });

  if (!data) return null;

  return (
    <group>
      {/* Alone umidità sotto il fiume: tubo più largo e basso, blu-verde
          scuro semitrasparente, rende l'idea di riva bagnata. */}
      <mesh
        geometry={data.halo}
        position={[0, -0.08, 0]}
        castShadow={false}
        receiveShadow={false}
      >
        <meshBasicMaterial
          color={PALETTE.seaDeep}
          transparent
          opacity={0.28}
          depthWrite={false}
          toneMapped={false}
        />
      </mesh>

      {/* Fiume principale — tube chiusa a anello. */}
      <mesh geometry={data.tube} castShadow={false} receiveShadow={false}>
        <meshStandardMaterial
          ref={materialRef}
          color={PALETTE.sea}
          emissive={PALETTE.seaLight}
          emissiveIntensity={0.18}
          roughness={0.35}
          metalness={0.1}
          flatShading
        />
      </mesh>

      <RiverSource position={data.sourcePos} />
      <RiverDelta mouthMid={data.mouthMid} deltaEnd={data.deltaEnd} />
    </group>
  );
}

// ---------------------------------------------------------------------------
// RiverSource: cuneo di schiuma cream alle Montagne (sorgente canonica).
// ~3 segmenti triangolari = ~6 triangoli. Sale dal punto di nascita verso
// l'alto dei picchi (nord-ovest), suggerendo una cascata in miniatura.
// ---------------------------------------------------------------------------

function RiverSource({ position }: { position: THREE.Vector3 }) {
  // Cuneo = cono molto sottile, 3 segmenti radiali → 3 tri laterali × 2 facce
  // = 6 tri (+ 1 per il fondo = 7). Flat-shading.
  // Orientato con la punta verso il basso-sud (verso il waypoint sorgente)
  // e la base verso l'alto-nord (verso i picchi, z più negativo).
  const height = 1.2; // unità Three
  const radius = 0.5;

  // Il cuneo sale dal sourcePos verso -z (nord) e +y (alto).
  const basePos = position.clone();
  basePos.y += height * 0.6;
  basePos.z -= 0.6;

  return (
    <group
      position={[basePos.x, basePos.y, basePos.z]}
      rotation={[Math.PI * 0.35, 0, 0]}
    >
      <mesh>
        <coneGeometry args={[radius, height, 3, 1, true]} />
        <meshStandardMaterial
          color={PALETTE.cream}
          transparent
          opacity={0.72}
          roughness={0.7}
          flatShading
          depthWrite={false}
        />
      </mesh>
    </group>
  );
}

// ---------------------------------------------------------------------------
// RiverDelta: breve tratto che sfocia nel mare a sud (la Bocca canonica) +
// piccola area sabbiosa triangolare al punto di confluenza.
// Canone: la polyline_closed si "apre" narrativamente alla Bocca — questa
// geometria estende visivamente quella apertura, come descritto in
// features.json (type: polyline_closed, "la 'bocca' reale è la sezione
// tra l'ultimo e il primo vertice").
// ---------------------------------------------------------------------------

function RiverDelta({
  mouthMid,
  deltaEnd,
}: {
  mouthMid: THREE.Vector3;
  deltaEnd: THREE.Vector3;
}) {
  // Un piccolo tubo dritto dal midpoint al mare.
  const geo = useMemo(() => {
    const curve = new THREE.CatmullRomCurve3(
      [mouthMid.clone(), deltaEnd.clone()],
      false,
      "catmullrom",
      0.5,
    );
    // 20 segmenti × 6 radial × 2 = 240 tri.
    return new THREE.TubeGeometry(curve, 20, 0.22, 6, false);
  }, [mouthMid, deltaEnd]);

  // Area sabbiosa triangolare alla confluenza — plane fan di 4 tri.
  const sandGeo = useMemo(() => {
    const g = new THREE.BufferGeometry();
    // Triangolo con vertice al mouthMid e base verso il mare larga 2.4u.
    const y = 0.05;
    const cx = deltaEnd.x;
    const cz = deltaEnd.z;
    const verts = new Float32Array([
      mouthMid.x, y, mouthMid.z,
      cx - 1.2, y, cz + 0.4,
      cx + 1.2, y, cz + 0.4,
      mouthMid.x, y, mouthMid.z,
      cx + 1.2, y, cz + 0.4,
      cx, y, cz + 1.2,
    ]);
    g.setAttribute("position", new THREE.BufferAttribute(verts, 3));
    g.computeVertexNormals();
    return g;
  }, [mouthMid, deltaEnd]);

  return (
    <group>
      {/* Area sabbiosa al delta (sotto il fiume). */}
      <mesh geometry={sandGeo} receiveShadow>
        <meshStandardMaterial
          color={PALETTE.sand}
          roughness={0.95}
          flatShading
        />
      </mesh>
      {/* Tratto di fiume che sfocia nel mare. */}
      <mesh geometry={geo} castShadow={false} receiveShadow={false}>
        <meshStandardMaterial
          color={PALETTE.sea}
          emissive={PALETTE.seaLight}
          emissiveIntensity={0.15}
          roughness={0.4}
          metalness={0.08}
          flatShading
        />
      </mesh>
    </group>
  );
}
