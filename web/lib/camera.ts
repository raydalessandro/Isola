/**
 * Helper per il calcolo dei target-camera ai due livelli di vista
 * e per l'interpolazione con easing cubico.
 *
 * Coordinate in unità Three.js (1 unità = 100 m; vedi geography.ts).
 * L'origine è l'Albero Vecchio. X=est, Z=sud, Y=up.
 */

import type { Quartiere } from "./geography";
import { metersToUnits } from "./geography";
import * as THREE from "three";

export type CameraTarget = {
  /** Posizione della camera in world space. */
  position: THREE.Vector3;
  /** Punto guardato dalla camera (target di MapControls). */
  target: THREE.Vector3;
};

/**
 * Vista L0 — aerea sull'isola intera.
 * Polar angle ~42° (camera inclinata), così la verticalità delle montagne
 * (amplificata da TerrainHeightmap::RELIEF_AMPLIFICATION) si legge molto
 * meglio di una quasi-top-down.
 */
export function islandCameraTarget(): CameraTarget {
  // Con RELIEF_AMPLIFICATION=2.5 le vette arrivano a ~10.5u: serve tilt
  // sostanziale per farne leggere il volume. Teniamo la distanza 3D vicina
  // al valore precedente ma ridistribuiamo tra height e offset.
  //   distance = sqrt(y^2 + z^2) ≈ 110
  //   polar = atan2(z, y) → y = 110 * cos(42°) ≈ 81.7
  //                        z = 110 * sin(42°) ≈ 73.6
  return {
    position: new THREE.Vector3(0, 82, 74),
    target: new THREE.Vector3(0, 0, 0),
  };
}

/**
 * Vista L1 — camera scesa 3/4 sul quartiere richiesto.
 * Polar angle ≈ 35°, distanza calibrata sul radius_m (40-60 unità).
 * Elevazione targetizzata sulla superficie amplificata (RELIEF=2.5 in
 * TerrainHeightmap), così i quartieri di montagna non finiscono dietro
 * il picco invece che sopra.
 */
const RELIEF_AMPLIFICATION = 2.5;

export function quartiereCameraTarget(q: Quartiere): CameraTarget {
  const cx = metersToUnits(q.center.x);
  const cz = metersToUnits(q.center.z);
  const cy = metersToUnits(q.elevation_m) * RELIEF_AMPLIFICATION;

  // Raggio in unità → distanza cam. Scala morbida: per un quartiere di
  // 500 m (centro) → ~42 u; per 900 m (montagne) → ~55 u.
  const radiusU = metersToUnits(q.radius_m);
  const distance = THREE.MathUtils.clamp(32 + radiusU * 2.5, 40, 60);

  // Polar angle ≈ 35°: height = distance * cos(35°) ≈ 0.82 * distance.
  // Offset orizzontale verso sud (positive Z) per inquadratura 3/4.
  const theta = THREE.MathUtils.degToRad(35);
  const height = distance * Math.cos(theta);
  const offsetZ = distance * Math.sin(theta);

  return {
    position: new THREE.Vector3(cx, cy + height, cz + offsetZ),
    target: new THREE.Vector3(cx, cy, cz),
  };
}

/** Easing cubico ease-out: lineare all'inizio, frenata alla fine. */
export function easeOutCubic(t: number): number {
  const c = Math.min(1, Math.max(0, t));
  return 1 - Math.pow(1 - c, 3);
}

/** Durata in ms di descend (L0→L1). */
export const DESCEND_MS = 2000;
/** Durata in ms di ascend (L1→L0). */
export const ASCEND_MS = 1500;
