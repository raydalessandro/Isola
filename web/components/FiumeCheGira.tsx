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
 */
export default function FiumeCheGira({ features, scale = 100 }: Props) {
  const materialRef = useRef<THREE.MeshStandardMaterial>(null!);

  const geometry = useMemo(() => {
    const river = features.features["fiume_che_gira"];
    if (!river || !river.waypoints || river.waypoints.length < 3) {
      return null;
    }

    const pts: THREE.Vector3[] = river.waypoints.map((w) => {
      return new THREE.Vector3(
        w.x / scale,
        (w.y ?? 2) / scale + 0.12, // +1m ~ 0.01u di anti-z-fight + piccolo lift
        w.z / scale,
      );
    });

    // Polyline chiusa: CatmullRom closed=true chiude automaticamente.
    const curve = new THREE.CatmullRomCurve3(pts, true, "catmullrom", 0.25);
    // Segment count generoso — il fiume è lungo e vogliamo curve morbide.
    // tubularSegments 240, radialSegments 6 → 240*6*2=~2880 triangoli.
    const tube = new THREE.TubeGeometry(curve, 240, 0.22, 6, true);
    return tube;
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

  if (!geometry) return null;

  return (
    <mesh geometry={geometry} castShadow={false} receiveShadow={false}>
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
  );
}
