"use client";

import { useRef, useMemo } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";
import { PALETTE } from "@/lib/geography";

type Props = {
  widthUnits: number;
  depthUnits: number;
};

/**
 * Flat plane with a simple sin-based vertex wave. No shader file, no extras
 * dependencies — we animate positions in useFrame to keep mobile GPUs cool.
 *
 * Base Y values are stored alongside the geometry (closed over in useMemo),
 * never accessed during render.
 */
export default function Ocean({ widthUnits, depthUnits }: Props) {
  const meshRef = useRef<THREE.Mesh>(null!);

  const { geometry, baseY } = useMemo(() => {
    // Ocean is ~3x the island footprint so the horizon looks convincing.
    const g = new THREE.PlaneGeometry(
      widthUnits * 3,
      depthUnits * 3,
      64,
      64,
    );
    g.rotateX(-Math.PI / 2);
    const pos = g.attributes.position as THREE.BufferAttribute;
    const b = new Float32Array(pos.count);
    for (let i = 0; i < pos.count; i++) b[i] = pos.getY(i);
    return { geometry: g, baseY: b };
  }, [widthUnits, depthUnits]);

  const material = useMemo(
    () =>
      new THREE.MeshStandardMaterial({
        color: new THREE.Color(PALETTE.sea),
        roughness: 0.6,
        metalness: 0.1,
        flatShading: true,
        transparent: true,
        opacity: 0.95,
      }),
    [],
  );

  useFrame(({ clock }) => {
    if (!meshRef.current) return;
    const t = clock.getElapsedTime();
    const pos = meshRef.current.geometry.attributes
      .position as THREE.BufferAttribute;
    for (let i = 0; i < pos.count; i++) {
      const x = pos.getX(i);
      const z = pos.getZ(i);
      const w =
        Math.sin(x * 0.2 + t * 0.8) * 0.06 +
        Math.cos(z * 0.25 + t * 0.6) * 0.05;
      pos.setY(i, baseY[i] + w);
    }
    pos.needsUpdate = true;
  });

  return (
    <mesh
      ref={meshRef}
      geometry={geometry}
      material={material}
      position={[0, -0.6, 0]}
      receiveShadow
    />
  );
}
