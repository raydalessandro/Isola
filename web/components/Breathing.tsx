"use client";

import { useMemo, useRef } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";
import type { Quartiere } from "@/lib/geography";
import { metersToUnits, PALETTE } from "@/lib/geography";

/**
 * Micro-animazioni ambient sui quartieri — "il mondo respira".
 *
 * Ogni sub-effetto è un piccolo <mesh>/<points> con meno di 30 vertici
 * e materiale basic trasparente. Nessuna shadow, nessun raycaster.
 *
 *  - forno     → colonna di fumo (4 particelle che salgono in loop 4s)
 *  - pontile   → già coperto dall'ondeggio dell'oceano (no-op)
 *  - orti      → spighe al vento (6 particelle che scorrono orizzontali)
 *  - montagne  → nuvola sottile che attraversa ogni 8s
 *  - centro    → nessun effetto (lasciamo respirare il silenzio)
 */

type Props = {
  quartieri: Quartiere[];
};

export default function Breathing({ quartieri }: Props) {
  const byId = useMemo(() => {
    const m = new Map<string, Quartiere>();
    for (const q of quartieri) m.set(q.id, q);
    return m;
  }, [quartieri]);

  return (
    <group>
      {byId.get("forno") && <Smoke quartiere={byId.get("forno")!} />}
      {byId.get("orti") && <WindWhispers quartiere={byId.get("orti")!} />}
      {byId.get("montagne") && <SlowCloud quartiere={byId.get("montagne")!} />}
    </group>
  );
}

// ---------------------------------------------------------------------------
// Forno: fumo
// ---------------------------------------------------------------------------

function Smoke({ quartiere }: { quartiere: Quartiere }) {
  const groupRef = useRef<THREE.Group>(null!);
  const bx = metersToUnits(quartiere.center.x);
  const bz = metersToUnits(quartiere.center.z);
  const by = metersToUnits(quartiere.elevation_m);

  // 4 particelle a fase sfalsata.
  const particles = useMemo(
    () => [0, 0.25, 0.5, 0.75].map((phase) => ({ phase })),
    [],
  );

  useFrame(({ clock }) => {
    if (!groupRef.current) return;
    const t = clock.getElapsedTime();
    const cycle = 4.0; // sec per particella
    groupRef.current.children.forEach((child, i) => {
      const phase = particles[i].phase;
      const local = ((t / cycle) + phase) % 1;
      const m = child as THREE.Mesh;
      // Sale da 0 a 8 unità, drift laterale sinusoidale.
      m.position.y = local * 8;
      m.position.x = Math.sin(local * Math.PI * 2 + i) * 0.4;
      m.position.z = Math.cos(local * Math.PI * 1.6 + i) * 0.3;
      const mat = m.material as THREE.MeshBasicMaterial;
      // Fade-out salendo, fade-in breve all'inizio.
      const opacity = Math.sin(local * Math.PI) * 0.45;
      mat.opacity = opacity;
      const scale = 0.4 + local * 1.6;
      m.scale.setScalar(scale);
    });
  });

  return (
    <group ref={groupRef} position={[bx, by + 2, bz]}>
      {particles.map((_, i) => (
        <mesh key={i}>
          <sphereGeometry args={[0.6, 8, 6]} />
          <meshBasicMaterial
            color={PALETTE.cream}
            transparent
            opacity={0}
            depthWrite={false}
          />
        </mesh>
      ))}
    </group>
  );
}

// ---------------------------------------------------------------------------
// Orti: bisbiglio orizzontale tipo spiga al vento
// ---------------------------------------------------------------------------

function WindWhispers({ quartiere }: { quartiere: Quartiere }) {
  const pointsRef = useRef<THREE.Points>(null!);
  const bx = metersToUnits(quartiere.center.x);
  const bz = metersToUnits(quartiere.center.z);
  const by = metersToUnits(quartiere.elevation_m);

  const { positions, basePositions, count } = useMemo(() => {
    const n = 16;
    const pos = new Float32Array(n * 3);
    const base = new Float32Array(n * 3);
    for (let i = 0; i < n; i++) {
      const a = (i / n) * Math.PI * 2;
      const r = 2 + (i % 3) * 0.8;
      const x = Math.cos(a) * r;
      const z = Math.sin(a) * r;
      const y = 0.8 + (i % 2) * 0.2;
      pos[i * 3] = x;
      pos[i * 3 + 1] = y;
      pos[i * 3 + 2] = z;
      base[i * 3] = x;
      base[i * 3 + 1] = y;
      base[i * 3 + 2] = z;
    }
    return { positions: pos, basePositions: base, count: n };
  }, []);

  useFrame(({ clock }) => {
    if (!pointsRef.current) return;
    const t = clock.getElapsedTime();
    const attr = pointsRef.current.geometry.attributes
      .position as THREE.BufferAttribute;
    for (let i = 0; i < count; i++) {
      const bxp = basePositions[i * 3];
      const bzp = basePositions[i * 3 + 2];
      // Drift orizzontale lento, fase per-vertice.
      attr.setX(i, bxp + Math.sin(t * 0.6 + i) * 0.4);
      attr.setZ(i, bzp + Math.cos(t * 0.5 + i * 1.3) * 0.25);
    }
    attr.needsUpdate = true;
  });

  return (
    <points ref={pointsRef} position={[bx, by, bz]}>
      <bufferGeometry>
        <bufferAttribute
          attach="attributes-position"
          args={[positions, 3]}
          count={count}
          itemSize={3}
          array={positions}
        />
      </bufferGeometry>
      <pointsMaterial
        color={PALETTE.oliveLight}
        size={0.22}
        sizeAttenuation
        transparent
        opacity={0.55}
        depthWrite={false}
      />
    </points>
  );
}

// ---------------------------------------------------------------------------
// Montagne: nuvola sottile che passa ogni 8s
// ---------------------------------------------------------------------------

function SlowCloud({ quartiere }: { quartiere: Quartiere }) {
  const meshRef = useRef<THREE.Mesh>(null!);
  const bx = metersToUnits(quartiere.center.x);
  const bz = metersToUnits(quartiere.center.z);
  const by = metersToUnits(quartiere.elevation_m);

  useFrame(({ clock }) => {
    if (!meshRef.current) return;
    const t = clock.getElapsedTime();
    const cycle = 8.0;
    const local = (t % cycle) / cycle; // 0..1
    // Attraversa da ovest (-10) a est (+10) sopra il picco.
    const xOffset = -10 + local * 20;
    meshRef.current.position.x = bx + xOffset;
    const mat = meshRef.current.material as THREE.MeshBasicMaterial;
    // Fade-in/out sui bordi, piena visibilità al centro.
    mat.opacity = Math.sin(local * Math.PI) * 0.5;
  });

  return (
    <mesh
      ref={meshRef}
      position={[bx, by + 4, bz]}
      rotation={[-Math.PI / 2, 0, 0]}
    >
      <planeGeometry args={[6, 2, 1, 1]} />
      <meshBasicMaterial
        color={PALETTE.cream}
        transparent
        opacity={0}
        depthWrite={false}
        side={THREE.DoubleSide}
      />
    </mesh>
  );
}
