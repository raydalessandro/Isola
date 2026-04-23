"use client";

import { useMemo } from "react";
import * as THREE from "three";
import { PALETTE } from "@/lib/geography";

type Props = {
  /** Posizione in unità Three (già convertita da metri). */
  position: [number, number, number];
  /** Altezza totale albero in unità Three. Default: 0.04 (≈ 4 m). */
  height?: number;
  /** Rotazione Y per evitare cloni perfettamente identici. */
  rotationY?: number;
  /** Tinta chioma (hex). Default: olive. */
  canopyColor?: string;
};

/**
 * Albero low-poly riutilizzabile — tronco cilindrico + cono chioma.
 *
 * Due mesh, flat-shaded, niente ombre auto per contenere i draw call del
 * quartiere (le 5-8 chiome generano ombre che al mobile costano). Il tronco
 * è cortissimo ed affusolato, la chioma è un cono a 6 segmenti radiali.
 * Poly count per albero: ~24 (cilindro 8*3) + ~24 (cono 6*2+fondo) ≈ 48 tri.
 */
export default function LowPolyTree({
  position,
  height = 0.04,
  rotationY = 0,
  canopyColor = PALETTE.olive,
}: Props) {
  const trunkH = height * 0.35;
  const canopyH = height * 0.75;
  const canopyR = height * 0.4;

  const trunkMat = useMemo(
    () =>
      new THREE.MeshStandardMaterial({
        color: PALETTE.warmBrown,
        roughness: 0.9,
        flatShading: true,
      }),
    [],
  );
  const canopyMat = useMemo(
    () =>
      new THREE.MeshStandardMaterial({
        color: canopyColor,
        roughness: 0.7,
        flatShading: true,
      }),
    [canopyColor],
  );

  return (
    <group position={position} rotation={[0, rotationY, 0]}>
      <mesh position={[0, trunkH / 2, 0]} material={trunkMat}>
        <cylinderGeometry
          args={[trunkH * 0.2, trunkH * 0.3, trunkH, 8]}
        />
      </mesh>
      <mesh position={[0, trunkH + canopyH / 2, 0]} material={canopyMat}>
        <coneGeometry args={[canopyR, canopyH, 6]} />
      </mesh>
    </group>
  );
}
