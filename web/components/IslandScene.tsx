"use client";

import { Suspense, useEffect, useMemo, useRef } from "react";
import { Canvas, useFrame, useThree } from "@react-three/fiber";
import { MapControls, Sky } from "@react-three/drei";
import { MapControls as MapControlsImpl } from "three-stdlib";
import * as THREE from "three";
import Island from "./Island";
import Ocean from "./Ocean";
import Hotspot, { hotspotYOffset } from "./Hotspot";
import LocationName from "./LocationName";
import FingerPresence from "./FingerPresence";
import Breathing from "./Breathing";
import type {
  IslandGeographyData,
  Location,
  Quartiere,
} from "@/lib/geography";
import { PALETTE, metersToUnits } from "@/lib/geography";
import { useWorldStore } from "@/lib/store";
import {
  ASCEND_MS,
  DESCEND_MS,
  easeOutCubic,
  islandCameraTarget,
  quartiereCameraTarget,
  type CameraTarget,
} from "@/lib/camera";

type Props = {
  geography: IslandGeographyData;
  locations: Location[];
};

export default function IslandScene({ geography, locations }: Props) {
  const widthUnits =
    geography.island.bounds.width_m /
    geography.island.bounds.unit_scale_three;
  const depthUnits =
    geography.island.bounds.depth_m /
    geography.island.bounds.unit_scale_three;

  const quartieriById = useMemo(() => {
    const m = new Map<string, Quartiere>();
    for (const q of geography.quartieri) m.set(q.id, q);
    return m;
  }, [geography.quartieri]);

  const initialCam = useMemo(() => islandCameraTarget(), []);

  return (
    <div className="fixed inset-0" style={{ background: PALETTE.sea }}>
      <Canvas
        shadows
        dpr={[1, 2]}
        camera={{
          position: [
            initialCam.position.x,
            initialCam.position.y,
            initialCam.position.z,
          ],
          fov: 40,
          near: 0.5,
          far: 2000,
        }}
        gl={{
          antialias: true,
          powerPreference: "high-performance",
          toneMapping: THREE.ACESFilmicToneMapping,
        }}
      >
        <color attach="background" args={[PALETTE.sea]} />
        <fog attach="fog" args={[PALETTE.sea, 140, 420]} />

        {/* Lighting — warm sun + soft sky ambient */}
        <ambientLight intensity={0.55} color={PALETTE.cream} />
        <hemisphereLight args={[PALETTE.cream, PALETTE.sea, 0.35]} />
        <directionalLight
          position={[40, 80, 30]}
          intensity={1.25}
          color={PALETTE.sun}
          castShadow
          shadow-mapSize-width={1024}
          shadow-mapSize-height={1024}
          shadow-camera-left={-60}
          shadow-camera-right={60}
          shadow-camera-top={60}
          shadow-camera-bottom={-60}
          shadow-camera-near={1}
          shadow-camera-far={220}
        />

        <Suspense fallback={null}>
          <Sky
            sunPosition={[40, 40, 30]}
            turbidity={6}
            rayleigh={2}
            mieCoefficient={0.02}
            mieDirectionalG={0.85}
          />
          <Island widthUnits={widthUnits} depthUnits={depthUnits} />
          <Ocean widthUnits={widthUnits} depthUnits={depthUnits} />

          <Breathing quartieri={geography.quartieri} />

          <HotspotLayer
            quartieri={geography.quartieri}
            quartieriById={quartieriById}
            locations={locations}
          />

          <FingerPresence />
        </Suspense>

        <SceneCameraController />
        <PinchOutListener />
      </Canvas>

      {/* Title — paper-map style, discreet */}
      <div
        className="fixed top-0 left-0 right-0 z-10 flex justify-center pointer-events-none"
        style={{ paddingTop: "calc(env(safe-area-inset-top) + 12px)" }}
      >
        <div
          className="font-hand"
          style={{
            fontSize: 26,
            fontWeight: 600,
            color: PALETTE.cream,
            textShadow:
              "0 1px 2px rgba(0,0,0,0.35), 0 0 14px rgba(15, 58, 72, 0.55)",
            letterSpacing: "0.02em",
          }}
        >
          L&apos;Isola dei Tre Venti
        </div>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Camera controller: MapControls + transizioni L0↔L1 con lerp in useFrame.
// ---------------------------------------------------------------------------

function SceneCameraController() {
  const viewLevel = useWorldStore((s) => s.viewLevel);
  const currentQuartiere = useWorldStore((s) => s.currentQuartiere);
  const transitioning = useWorldStore((s) => s.transitioning);
  const setTransitioning = useWorldStore((s) => s.setTransitioning);

  // Stato dell'animazione corrente (ref, non serve rerender).
  const animRef = useRef<{
    fromPos: THREE.Vector3;
    toPos: THREE.Vector3;
    fromTarget: THREE.Vector3;
    toTarget: THREE.Vector3;
    startedAt: number;
    durationMs: number;
  } | null>(null);

  const { camera } = useThree();
  const controlsRef = useRef<MapControlsImpl | null>(null);

  // Cache dell'ultima viewLevel/quartiere applicati → triggera lo "start" dell'anim
  // solo quando transitioning passa a true.
  useEffect(() => {
    if (!transitioning) return;

    let to: CameraTarget;
    let durationMs: number;
    if (viewLevel === "island") {
      to = islandCameraTarget();
      durationMs = ASCEND_MS;
    } else {
      // Nota: il quartiere target lo deduciamo via store/island geography
      // ma qui abbiamo solo l'id. Pesca dalla mappa globale (DOM attr).
      const q = findQuartiereById(currentQuartiere);
      if (!q) {
        setTransitioning(false);
        return;
      }
      to = quartiereCameraTarget(q);
      durationMs = DESCEND_MS;
    }

    // Disabilita MapControls durante l'animazione.
    if (controlsRef.current) {
      controlsRef.current.enabled = false;
    }

    animRef.current = {
      fromPos: camera.position.clone(),
      toPos: to.position.clone(),
      fromTarget: controlsRef.current
        ? controlsRef.current.target.clone()
        : new THREE.Vector3(0, 0, 0),
      toTarget: to.target.clone(),
      startedAt: performance.now(),
      durationMs,
    };
  }, [transitioning, viewLevel, currentQuartiere, camera, setTransitioning]);

  useFrame(() => {
    const anim = animRef.current;
    if (!anim) return;
    const now = performance.now();
    const raw = (now - anim.startedAt) / anim.durationMs;
    const t = easeOutCubic(Math.min(1, Math.max(0, raw)));

    camera.position.lerpVectors(anim.fromPos, anim.toPos, t);
    if (controlsRef.current) {
      controlsRef.current.target.lerpVectors(
        anim.fromTarget,
        anim.toTarget,
        t,
      );
      controlsRef.current.update();
    } else {
      camera.lookAt(
        anim.fromTarget.clone().lerp(anim.toTarget, t),
      );
    }

    if (raw >= 1) {
      animRef.current = null;
      if (controlsRef.current) {
        controlsRef.current.enabled = true;
      }
      setTransitioning(false);
    }
  });

  return (
    <MapControls
      ref={controlsRef}
      enableDamping
      dampingFactor={0.12}
      minDistance={15}
      maxDistance={220}
      maxPolarAngle={Math.PI * 0.48}
      minPolarAngle={Math.PI * 0.08}
      target={[0, 0, 0]}
      screenSpacePanning={false}
    />
  );
}

// Minuscolo side channel per ritrovare il quartiere dal solo id nell'effetto
// sopra (evitiamo di legare lo useEffect alla geography, che è stabile).
let __quartieriRegistry: Quartiere[] = [];
function findQuartiereById(id: string | null): Quartiere | null {
  if (!id) return null;
  return __quartieriRegistry.find((q) => q.id === id) ?? null;
}

// ---------------------------------------------------------------------------
// HotspotLayer: decide cosa renderizzare in base a viewLevel/currentQuartiere.
// Include nome-overlay durante dwell e registra i quartieri per camera lookup.
// ---------------------------------------------------------------------------

function HotspotLayer({
  quartieri,
  quartieriById,
  locations,
}: {
  quartieri: Quartiere[];
  quartieriById: Map<string, Quartiere>;
  locations: Location[];
}) {
  // Registra i quartieri per findQuartiereById (SceneCameraController).
  useEffect(() => {
    __quartieriRegistry = quartieri;
    return () => {
      __quartieriRegistry = [];
    };
  }, [quartieri]);

  const viewLevel = useWorldStore((s) => s.viewLevel);
  const currentQuartiere = useWorldStore((s) => s.currentQuartiere);
  const dwellTargetId = useWorldStore((s) => s.dwellTargetId);
  const descend = useWorldStore((s) => s.descend);
  const setDwellTarget = useWorldStore((s) => s.setDwellTarget);
  const transitioning = useWorldStore((s) => s.transitioning);

  const handleQuartiereDwell = (id: string) => {
    if (transitioning) return;
    descend(id);
  };

  const handleLocationDwell = (id: string) => {
    if (transitioning) return;
    setDwellTarget(id);
  };

  const handleLocationDwellEnd = () => {
    setDwellTarget(null);
  };

  // L0: 5 quartieri, hotspot grandi.
  if (viewLevel === "island") {
    return (
      <>
        {quartieri.map((q, i) => (
          <Hotspot
            key={q.id}
            id={q.id}
            position={[
              metersToUnits(q.center.x),
              hotspotYOffset(q.elevation_m, 2.0),
              metersToUnits(q.center.z),
            ]}
            color={q.color}
            headRadius={0.75}
            stemHeight={1.8}
            hitRadius={2.2}
            emissive={0.3}
            floatAmp={0.18}
            floatPhase={q.center.x * 0.01 + i}
            onDwell={handleQuartiereDwell}
          />
        ))}
      </>
    );
  }

  // L1: quartiere corrente. Hotspot quartiere più piccolo + location pins.
  const cq = currentQuartiere ? quartieriById.get(currentQuartiere) : null;
  if (!cq) return null;

  // Location visibili:
  //   - tutte quelle con location.quartiere === currentQuartiere
  //   - se currentQuartiere !== "centro", includi anche le location del centro
  //     (così i bambini vedono che il villaggio è lì accanto).
  //   - escludi porta_socchiusa === true
  //   - escludi quartiere === null (tranne fiume_che_gira, che NON mostriamo
  //     come hotspot — potrebbe essere disegnato come linea in futuro).
  const visibleLocations = locations.filter((l) => {
    if (l.porta_socchiusa) return false;
    if (l.quartiere === null) return false;
    if (l.quartiere === currentQuartiere) return true;
    if (currentQuartiere !== "centro" && l.quartiere === "centro") return true;
    return false;
  });

  return (
    <>
      {/* Hotspot del quartiere corrente, più piccolo ma ancora riconoscibile.
          Dwell su di esso NON fa niente (siamo già qui); manteniamolo per
          coerenza visiva. */}
      <Hotspot
        id={cq.id}
        position={[
          metersToUnits(cq.center.x),
          hotspotYOffset(cq.elevation_m, 2.0),
          metersToUnits(cq.center.z),
        ]}
        color={cq.color}
        headRadius={0.5}
        stemHeight={1.4}
        hitRadius={1.6}
        emissive={0.2}
        floatAmp={0.12}
        floatPhase={0}
        onDwell={() => {
          /* no-op: già su questo quartiere */
        }}
      />

      {visibleLocations.map((l) => {
        const posX = metersToUnits(l.coords.x);
        const posY = hotspotYOffset(l.coords.y, 1.0);
        const posZ = metersToUnits(l.coords.z);
        const color = inheritColor(l.quartiere, quartieriById);
        const isDwelling = dwellTargetId === l.id;
        return (
          <group key={l.id}>
            <Hotspot
              id={l.id}
              position={[posX, posY, posZ]}
              color={color}
              headRadius={0.28}
              stemHeight={0.9}
              hitRadius={1.1}
              emissive={0.2}
              floatAmp={0.08}
              floatPhase={l.coords.x * 0.02 + l.coords.z * 0.013}
              onDwell={handleLocationDwell}
              onDwellEnd={handleLocationDwellEnd}
            />
            <LocationName
              label={l.nome_canonico}
              position={[posX, posY + 1.2, posZ]}
              visible={isDwelling}
            />
          </group>
        );
      })}
    </>
  );
}

function inheritColor(
  quartiereId: string | null,
  byId: Map<string, Quartiere>,
): string {
  if (!quartiereId) return PALETTE.warmBrown;
  return byId.get(quartiereId)?.color ?? PALETTE.warmBrown;
}

// ---------------------------------------------------------------------------
// PinchOutListener: al pinch-out (due dita che si allontanano) risaliamo a L0.
// ---------------------------------------------------------------------------

function PinchOutListener() {
  const { gl } = useThree();
  const viewLevel = useWorldStore((s) => s.viewLevel);
  const transitioning = useWorldStore((s) => s.transitioning);
  const ascend = useWorldStore((s) => s.ascend);

  useEffect(() => {
    if (viewLevel !== "quartiere") return;
    const canvas = gl.domElement;

    // Tracciamo fino a 2 puntatori attivi e la loro distanza iniziale.
    type P = { x: number; y: number };
    const pts = new Map<number, P>();
    let baseDist: number | null = null;

    const distance = (): number | null => {
      if (pts.size < 2) return null;
      const arr = Array.from(pts.values());
      const dx = arr[0].x - arr[1].x;
      const dy = arr[0].y - arr[1].y;
      return Math.sqrt(dx * dx + dy * dy);
    };

    const onDown = (e: PointerEvent) => {
      pts.set(e.pointerId, { x: e.clientX, y: e.clientY });
      if (pts.size === 2) {
        baseDist = distance();
      }
    };

    const onMove = (e: PointerEvent) => {
      if (!pts.has(e.pointerId)) return;
      pts.set(e.pointerId, { x: e.clientX, y: e.clientY });
      if (pts.size === 2 && baseDist != null) {
        const cur = distance();
        if (cur != null && baseDist > 0) {
          const ratio = cur / baseDist;
          // pinch-OUT = dita si allontanano = ratio cresce.
          // In L1 riguadagniamo la vista → ascend.
          // Soglia: +35% rispetto alla distanza iniziale.
          if (ratio <= 0.7 && !transitioning) {
            // Pinch-IN in L1? Per ora lo ignoriamo (zoom naturale gestito
            // da MapControls sul loro OrbitControls inner).
            baseDist = cur;
          } else if (ratio >= 1.35 && !transitioning) {
            ascend();
            baseDist = null;
            pts.clear();
          }
        }
      }
    };

    const onUp = (e: PointerEvent) => {
      pts.delete(e.pointerId);
      if (pts.size < 2) baseDist = null;
    };

    canvas.addEventListener("pointerdown", onDown);
    canvas.addEventListener("pointermove", onMove);
    canvas.addEventListener("pointerup", onUp);
    canvas.addEventListener("pointercancel", onUp);
    canvas.addEventListener("pointerleave", onUp);

    // Fallback: wheel con deltaY molto negativo (zoom-out) in L1 = ascend.
    const onWheel = (e: WheelEvent) => {
      if (transitioning) return;
      // deltaY > 0 = scroll giù = zoom-out in OrbitControls di Three.
      if (e.deltaY > 60) {
        ascend();
      }
    };
    canvas.addEventListener("wheel", onWheel, { passive: true });

    return () => {
      canvas.removeEventListener("pointerdown", onDown);
      canvas.removeEventListener("pointermove", onMove);
      canvas.removeEventListener("pointerup", onUp);
      canvas.removeEventListener("pointercancel", onUp);
      canvas.removeEventListener("pointerleave", onUp);
      canvas.removeEventListener("wheel", onWheel);
    };
  }, [gl, viewLevel, transitioning, ascend]);

  return null;
}
