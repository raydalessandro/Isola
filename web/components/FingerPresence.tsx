"use client";

import { useEffect, useMemo, useRef } from "react";
import { useFrame, useThree } from "@react-three/fiber";
import * as THREE from "three";
import { PALETTE } from "@/lib/geography";

/**
 * Alone del dito/puntatore nel world space — omaggio a Tearaway.
 *
 * Un cerchio semi-trasparente crema che segue il puntatore con un lieve
 * lag (lerp). Quando non c'è tocco, l'alone fa fade-out (opacità → 0).
 *
 * Implementazione: plane circolare orizzontale proiettato sul piano y=0
 * via raycaster dalla camera. Nessun depth-test pesante. Semplicissimo.
 */
export default function FingerPresence() {
  const meshRef = useRef<THREE.Mesh>(null!);
  const { camera, gl } = useThree();

  // Obiettivi di posizione/opacità che la mesh insegue con lerp.
  const targetPos = useRef(new THREE.Vector3(0, 0.02, 0));
  const targetOpacity = useRef(0);

  const plane = useMemo(
    () => new THREE.Plane(new THREE.Vector3(0, 1, 0), 0),
    [],
  );
  const raycaster = useMemo(() => new THREE.Raycaster(), []);
  const ndc = useMemo(() => new THREE.Vector2(), []);
  const hit = useMemo(() => new THREE.Vector3(), []);

  useEffect(() => {
    const canvas = gl.domElement;

    const updateFromEvent = (e: PointerEvent) => {
      const rect = canvas.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
      const y = -((e.clientY - rect.top) / rect.height) * 2 + 1;
      ndc.set(x, y);
      raycaster.setFromCamera(ndc, camera);
      const p = raycaster.ray.intersectPlane(plane, hit);
      if (p) {
        targetPos.current.set(p.x, 0.05, p.z);
      }
    };

    const onMove = (e: PointerEvent) => {
      updateFromEvent(e);
      // Se il puntatore è in movimento con pulsante/touch giù, rendiamolo
      // pienamente visibile. Al move puro (mouse) teniamo una presenza
      // discreta per feedback.
      targetOpacity.current = e.pressure > 0 || e.buttons > 0 ? 0.35 : 0.12;
    };

    const onDown = (e: PointerEvent) => {
      updateFromEvent(e);
      targetOpacity.current = 0.35;
    };

    const onUp = () => {
      targetOpacity.current = 0;
    };

    canvas.addEventListener("pointermove", onMove);
    canvas.addEventListener("pointerdown", onDown);
    canvas.addEventListener("pointerup", onUp);
    canvas.addEventListener("pointercancel", onUp);
    canvas.addEventListener("pointerleave", onUp);

    return () => {
      canvas.removeEventListener("pointermove", onMove);
      canvas.removeEventListener("pointerdown", onDown);
      canvas.removeEventListener("pointerup", onUp);
      canvas.removeEventListener("pointercancel", onUp);
      canvas.removeEventListener("pointerleave", onUp);
    };
  }, [camera, gl, ndc, plane, raycaster, hit]);

  useFrame((_, dt) => {
    if (!meshRef.current) return;
    const lag = 0.3;
    meshRef.current.position.lerp(targetPos.current, lag);
    const mat = meshRef.current.material as THREE.MeshBasicMaterial;
    // Smooth opacity convergence. dt in seconds; 400ms fade-out → k≈2.5/s.
    const k = 6;
    mat.opacity += (targetOpacity.current - mat.opacity) * Math.min(1, k * dt);
  });

  return (
    <mesh
      ref={meshRef}
      rotation={[-Math.PI / 2, 0, 0]}
      position={[0, 0.05, 0]}
      renderOrder={999}
    >
      <circleGeometry args={[2, 32]} />
      <meshBasicMaterial
        color={PALETTE.cream}
        transparent
        opacity={0}
        depthWrite={false}
        toneMapped={false}
      />
    </mesh>
  );
}
