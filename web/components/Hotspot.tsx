"use client";

import { useEffect, useRef, useState } from "react";
import { useFrame, type ThreeEvent } from "@react-three/fiber";
import * as THREE from "three";
import { metersToUnits } from "@/lib/geography";

/**
 * Hotspot generico con dwell-detection (tap-and-hold 500ms fermo).
 *
 * Comportamento gesture:
 *   pointerDown  → parte un timer da 500ms, memorizza xy schermo.
 *   pointerMove  → se il movimento schermo supera 10px, timer annullato
 *                  e il gesto diventa pan (MapControls lo riceverà come
 *                  drag, perché non stoppiamo la propagation prima del
 *                  dwell acquisito).
 *   pointerUp / pointerLeave → annulla il timer; se dwell era acquisito,
 *                  chiama onDwellEnd() così l'overlay nome può uscire.
 *   timer 500ms scaduto senza movimento → dwell acquisito: chiamiamo
 *                  onDwell(id); da qui in poi stopPropagation così
 *                  MapControls non interpreta il frame come drag.
 *
 * Non c'è onClick. Tap secco = niente.
 */

type Props = {
  id: string;
  position: [number, number, number];
  color: string;
  /** Raggio della "testa" del pin (unità Three). */
  headRadius?: number;
  /** Altezza dello stelo (unità Three). */
  stemHeight?: number;
  /** Raggio del collider invisibile per il tocco (unità Three). */
  hitRadius?: number;
  /** Intensità emissiva a riposo (0-1). */
  emissive?: number;
  /** Float ambient: ampiezza in unità. 0 = immobile. */
  floatAmp?: number;
  /** Offset fase del float (per desync tra hotspot). */
  floatPhase?: number;
  /** Chiamato quando il dwell è acquisito (≥500ms fermo). */
  onDwell: (id: string) => void;
  /** Chiamato al rilascio del puntatore dopo un dwell acquisito. */
  onDwellEnd?: (id: string) => void;
};

const DWELL_MS = 500;
const MOVE_THRESHOLD_PX = 10;

export default function Hotspot({
  id,
  position,
  color,
  headRadius = 0.6,
  stemHeight = 1.8,
  hitRadius = 1.8,
  emissive = 0.25,
  floatAmp = 0.15,
  floatPhase = 0,
  onDwell,
  onDwellEnd,
}: Props) {
  const groupRef = useRef<THREE.Group>(null!);
  const [hover, setHover] = useState(false);
  const [dwellActive, setDwellActive] = useState(false);

  // Stato gesture locale (non serve lo re-render, teniamolo in ref).
  const pointerDownRef = useRef<{
    pointerId: number;
    x: number;
    y: number;
    timer: ReturnType<typeof setTimeout> | null;
    acquired: boolean;
  } | null>(null);

  // Sicurezza: se il componente si smonta a dwell attivo, pulisci il timer.
  useEffect(() => {
    return () => {
      const p = pointerDownRef.current;
      if (p?.timer) clearTimeout(p.timer);
      pointerDownRef.current = null;
    };
  }, []);

  useFrame(({ clock }) => {
    if (!groupRef.current) return;
    if (floatAmp <= 0) return;
    const t = clock.getElapsedTime();
    groupRef.current.position.y =
      position[1] + Math.sin(t * 1.2 + floatPhase) * floatAmp;
  });

  const cancelDwell = (runEnd: boolean) => {
    const p = pointerDownRef.current;
    if (!p) return;
    if (p.timer) clearTimeout(p.timer);
    const wasAcquired = p.acquired;
    pointerDownRef.current = null;
    if (wasAcquired && runEnd) {
      setDwellActive(false);
      onDwellEnd?.(id);
    } else if (wasAcquired) {
      setDwellActive(false);
    }
  };

  const handlePointerDown = (e: ThreeEvent<PointerEvent>) => {
    // Due dita: pinch/pan, non è un dwell. Non catturare.
    const ne = e.nativeEvent as PointerEvent & { isPrimary?: boolean };
    if (ne.isPrimary === false) return;

    // Pulisci eventuale dwell precedente.
    cancelDwell(true);

    const timer = setTimeout(() => {
      const p = pointerDownRef.current;
      if (!p) return;
      p.acquired = true;
      setDwellActive(true);
      onDwell(id);
    }, DWELL_MS);

    pointerDownRef.current = {
      pointerId: e.pointerId,
      x: e.clientX,
      y: e.clientY,
      timer,
      acquired: false,
    };
  };

  const handlePointerMove = (e: ThreeEvent<PointerEvent>) => {
    const p = pointerDownRef.current;
    if (!p) return;
    if (e.pointerId !== p.pointerId) return;
    if (p.acquired) {
      // Dwell già acquisito: consumiamo lo stop così MapControls non prova
      // a iniziare un drag tardivo.
      e.stopPropagation();
      return;
    }
    const dx = e.clientX - p.x;
    const dy = e.clientY - p.y;
    if (dx * dx + dy * dy > MOVE_THRESHOLD_PX * MOVE_THRESHOLD_PX) {
      // Il gesto è diventato un pan. Molliamo il dwell e NON stopPropagation,
      // così MapControls gestisce il resto del drag normalmente.
      cancelDwell(false);
    }
  };

  const handlePointerUp = (e: ThreeEvent<PointerEvent>) => {
    const p = pointerDownRef.current;
    if (!p || e.pointerId !== p.pointerId) return;
    if (p.acquired) {
      // Stop propagation solo se il dwell era attivo (sicurezza: niente
      // click fantasma sotto di noi).
      e.stopPropagation();
    }
    cancelDwell(true);
  };

  const handlePointerLeave = (e: ThreeEvent<PointerEvent>) => {
    const p = pointerDownRef.current;
    if (!p) return;
    if (e.pointerId !== p.pointerId) return;
    cancelDwell(true);
  };

  const visualScale = hover || dwellActive ? 1.25 : 1.0;
  const headR = headRadius * visualScale;

  return (
    <group
      ref={groupRef}
      position={position}
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
      onPointerDown={handlePointerDown}
      onPointerMove={handlePointerMove}
      onPointerUp={handlePointerUp}
      onPointerLeave={handlePointerLeave}
      onPointerCancel={handlePointerLeave}
    >
      {/* stelo */}
      <mesh position={[0, -stemHeight / 2, 0]} castShadow>
        <cylinderGeometry args={[0.12, 0.18, stemHeight, 8]} />
        <meshStandardMaterial color="#2a2319" roughness={0.7} flatShading />
      </mesh>
      {/* testa */}
      <mesh castShadow>
        <icosahedronGeometry args={[headR, 0]} />
        <meshStandardMaterial
          color={color}
          emissive={color}
          emissiveIntensity={dwellActive ? 0.9 : hover ? 0.6 : emissive}
          roughness={0.45}
          flatShading
        />
      </mesh>
      {/* collider invisibile, dimensione generosa per il touch */}
      <mesh>
        <sphereGeometry args={[hitRadius, 8, 8]} />
        <meshBasicMaterial transparent opacity={0} depthWrite={false} />
      </mesh>
    </group>
  );
}

export function hotspotYOffset(elevationMeters: number, lift = 2.0): number {
  return metersToUnits(elevationMeters) + lift;
}
