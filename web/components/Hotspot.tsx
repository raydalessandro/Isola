"use client";

import { useRef, useState } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";
import type { Quartiere } from "@/lib/geography";
import { metersToUnits } from "@/lib/geography";

type Props = {
  quartiere: Quartiere;
  onSelect: (q: Quartiere) => void;
};

/**
 * A placeholder low-poly marker: cylinder pin + small flag sphere on top.
 * Colored per-quartiere. Gently floats so it reads as interactive.
 */
export default function Hotspot({ quartiere, onSelect }: Props) {
  const groupRef = useRef<THREE.Group>(null!);
  const [hover, setHover] = useState(false);

  const xU = metersToUnits(quartiere.center.x);
  const zU = metersToUnits(quartiere.center.z);
  const yU = metersToUnits(quartiere.elevation_m) + 2.0;

  useFrame(({ clock }) => {
    if (!groupRef.current) return;
    const t = clock.getElapsedTime();
    groupRef.current.position.y =
      yU + Math.sin(t * 1.2 + quartiere.center.x * 0.01) * 0.15;
  });

  return (
    <group
      ref={groupRef}
      position={[xU, yU, zU]}
      onPointerOver={(e) => {
        e.stopPropagation();
        setHover(true);
        if (typeof document !== "undefined")
          document.body.style.cursor = "pointer";
      }}
      onPointerOut={() => {
        setHover(false);
        if (typeof document !== "undefined") document.body.style.cursor = "";
      }}
      onClick={(e) => {
        e.stopPropagation();
        onSelect(quartiere);
      }}
    >
      {/* pin stem */}
      <mesh position={[0, -0.9, 0]} castShadow>
        <cylinderGeometry args={[0.12, 0.18, 1.8, 8]} />
        <meshStandardMaterial
          color="#2a2319"
          roughness={0.7}
          flatShading
        />
      </mesh>
      {/* head */}
      <mesh castShadow>
        <icosahedronGeometry args={[hover ? 0.75 : 0.6, 0]} />
        <meshStandardMaterial
          color={quartiere.color}
          emissive={quartiere.color}
          emissiveIntensity={hover ? 0.6 : 0.25}
          roughness={0.45}
          flatShading
        />
      </mesh>
      {/* larger invisible hit target for touch */}
      <mesh>
        <sphereGeometry args={[1.8, 8, 8]} />
        <meshBasicMaterial transparent opacity={0} depthWrite={false} />
      </mesh>
    </group>
  );
}
