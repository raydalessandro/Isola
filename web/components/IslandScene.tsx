"use client";

import { Suspense, useEffect, useMemo, useRef } from "react";
import { Canvas, useFrame, useThree } from "@react-three/fiber";
import { MapControls, Sky } from "@react-three/drei";
import { MapControls as MapControlsImpl } from "three-stdlib";
import * as THREE from "three";
import Ocean from "./Ocean";
import Hotspot, { hotspotYOffset } from "./Hotspot";
import LocationName from "./LocationName";
import FingerPresence from "./FingerPresence";
import Breathing from "./Breathing";
import TerrainHeightmap from "./TerrainHeightmap";
import FiumeCheGira from "./FiumeCheGira";
import MontagneGemellePeaks from "./MontagneGemellePeaks";
import QuartiereForno from "./QuartiereForno";
import PinchOutHint from "./PinchOutHint";
import type {
  FeaturesDoc,
  IslandGeographyData,
  Location,
  Quartiere,
  TerrainDoc,
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
  features: FeaturesDoc;
  terrain: TerrainDoc;
};

export default function IslandScene({
  geography,
  locations,
  features,
  terrain,
}: Props) {
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
        {/* Fog spinta più lontana per il tilt a 42° + amplificazione relief:
            con camera (0,82,74) la distanza alla costa nord supera i 130u,
            serve near 170/far 520 per non appannare le Montagne Gemelle. */}
        <fog attach="fog" args={[PALETTE.sea, 170, 520]} />

        {/* Lighting — warm sun + soft sky ambient.
            Il sole è spostato verso sud-est con angolo RADENTE (altezza
            più bassa del zenith) così la luce sfiora le facce sud delle
            Montagne Gemelle (quartiere nord, z negativo) e le ombre
            disegnano nettamente i pendii. Ambient ridotto per lasciare
            stacco alle ombre — con RELIEF_AMPLIFICATION=2.5 la verticalità
            legge solo se il contrasto luce/ombra è marcato. */}
        <ambientLight intensity={0.32} color={PALETTE.cream} />
        <hemisphereLight args={[PALETTE.cream, PALETTE.sea, 0.25]} />
        <directionalLight
          position={[70, 55, 85]}
          intensity={2.1}
          color={PALETTE.sun}
          castShadow
          shadow-mapSize-width={1024}
          shadow-mapSize-height={1024}
          shadow-camera-left={-60}
          shadow-camera-right={60}
          shadow-camera-top={60}
          shadow-camera-bottom={-60}
          shadow-camera-near={1}
          shadow-camera-far={260}
        />

        <Suspense fallback={null}>
          <Sky
            sunPosition={[40, 40, 30]}
            turbidity={6}
            rayleigh={2}
            mieCoefficient={0.02}
            mieDirectionalG={0.85}
          />
          <TerrainHeightmap
            widthUnits={widthUnits}
            depthUnits={depthUnits}
            geography={geography}
            terrain={terrain}
          />
          <Ocean widthUnits={widthUnits} depthUnits={depthUnits} />

          <FiumeCheGira features={features} />

          <MontagneGemellePeaks terrain={terrain} />

          <QuartiereFornoGate locations={locations} />

          <Breathing quartieri={geography.quartieri} locations={locations} />

          <HotspotLayer
            quartieri={geography.quartieri}
            quartieriById={quartieriById}
            locations={locations}
          />

          <FingerPresence />
        </Suspense>

        <SceneCameraController />
        <TwoFingerSwipeDownListener />
      </Canvas>

      <PinchOutHint />

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
// QuartiereFornoGate: monta QuartiereForno solo se viewLevel === L1 sul
// quartiere "forno". Smonta appena risaliamo o passiamo ad altro quartiere.
// ---------------------------------------------------------------------------

function QuartiereFornoGate({ locations }: { locations: Location[] }) {
  const viewLevel = useWorldStore((s) => s.viewLevel);
  const currentQuartiere = useWorldStore((s) => s.currentQuartiere);
  if (viewLevel !== "quartiere") return null;
  if (currentQuartiere !== "forno") return null;
  return <QuartiereForno locations={locations} />;
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

  // L0: 5 quartieri come ring-luminosi a filo del terreno. Il quartiere
  // ha già identità visiva dal colore del terreno: il ring è un ancora
  // discreta per il tap-and-hold, pulsante, non invasiva.
  if (viewLevel === "island") {
    return (
      <>
        {quartieri.map((q, i) => (
          <Hotspot
            key={q.id}
            id={q.id}
            position={[
              metersToUnits(q.center.x),
              hotspotYOffset(q.elevation_m, 0.25),
              metersToUnits(q.center.z),
            ]}
            color={q.color}
            variant="ring"
            headRadius={1.1}
            stemHeight={0.25}
            hitRadius={2.4}
            emissive={0}
            floatAmp={0}
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
// TwoFingerSwipeDownListener: gesto di ritorno a L0 = swipe-down con DUE
// dita. Scelto al posto del pinch-out perché:
//  - il pinch-out collideva col normale pinch-zoom di MapControls (non si
//    riusciva più a zoomare in L1);
//  - la direzione e la velocità di uno swipe-down sono più univoche di un
//    cambio di distanza proporzionale, che invece è *proprio* la definizione
//    dello zoom;
//  - leggere "scendo con due dita = torno su" è un'affordance comune nei
//    game-UI / mappe illustrate (cfr. Gorogoa, Monument Valley).
//
// Regole del gesto (strette per evitare falsi positivi con pan due-dita):
//  - esattamente 2 touch attivi per tutta la durata;
//  - entrambi Δy > +MIN_DY_PX (verso il basso, coordinate schermo +y = giù);
//  - durata gesto <= MAX_MS (swipe, non pan lento);
//  - spostamento orizzontale medio <= MAX_DX_PX (niente pan laterale);
//  - ratio della distanza inter-dita tra 0.85..1.15: se la distanza cambia
//    molto è un pinch, non uno swipe — lasciamo gestire a MapControls.
//
// CRITICO: il listener è puramente osservativo. Nessun preventDefault,
// nessun stopPropagation: MapControls continua a ricevere i PointerEvent
// come pan/zoom normali. Triggeriamo `ascend()` solo a gesto completato.
// ---------------------------------------------------------------------------

const SWIPE_MIN_DY_PX = 100; // entrambi i touch devono scendere almeno 100px
const SWIPE_MAX_DX_PX = 80; // tolleranza orizzontale
const SWIPE_MAX_MS = 400; // deve essere uno swipe, non un pan
const SWIPE_PINCH_RATIO_TOL = 0.15; // |ratio-1| <= 0.15 → non è un pinch

function TwoFingerSwipeDownListener() {
  const { gl } = useThree();
  const viewLevel = useWorldStore((s) => s.viewLevel);
  const transitioning = useWorldStore((s) => s.transitioning);
  const ascend = useWorldStore((s) => s.ascend);

  useEffect(() => {
    if (viewLevel !== "quartiere") return;
    const canvas = gl.domElement;

    type P = { startX: number; startY: number; x: number; y: number };
    const pts = new Map<number, P>();
    let gestureStart: number | null = null;

    const interDistance = (a: P, b: P) =>
      Math.hypot(a.x - b.x, a.y - b.y);

    const onDown = (e: PointerEvent) => {
      if (e.pointerType !== "touch") return;
      pts.set(e.pointerId, {
        startX: e.clientX,
        startY: e.clientY,
        x: e.clientX,
        y: e.clientY,
      });
      if (pts.size === 2) {
        gestureStart = performance.now();
      } else if (pts.size > 2) {
        gestureStart = null;
      }
    };

    const onMove = (e: PointerEvent) => {
      const p = pts.get(e.pointerId);
      if (!p) return;
      p.x = e.clientX;
      p.y = e.clientY;
    };

    const evaluate = () => {
      if (transitioning) return;
      if (pts.size !== 2 || gestureStart == null) return;
      const now = performance.now();
      const elapsed = now - gestureStart;
      if (elapsed > SWIPE_MAX_MS) return;

      const arr = Array.from(pts.values());
      const a = arr[0];
      const b = arr[1];

      const dyA = a.y - a.startY;
      const dyB = b.y - b.startY;
      const dxA = Math.abs(a.x - a.startX);
      const dxB = Math.abs(b.x - b.startX);

      if (dyA < SWIPE_MIN_DY_PX) return;
      if (dyB < SWIPE_MIN_DY_PX) return;
      if (dxA > SWIPE_MAX_DX_PX) return;
      if (dxB > SWIPE_MAX_DX_PX) return;

      // Escludi pinch: se la distanza inter-dita è cambiata > tol → è un pinch.
      const startDist = Math.hypot(
        a.startX - b.startX,
        a.startY - b.startY,
      );
      const curDist = interDistance(a, b);
      if (startDist > 0) {
        const ratio = curDist / startDist;
        if (Math.abs(ratio - 1) > SWIPE_PINCH_RATIO_TOL) return;
      }

      // Gesto valido → ascend. Resetta per non ritriggerare.
      pts.clear();
      gestureStart = null;
      ascend();
    };

    const onMoveEvaluate = (e: PointerEvent) => {
      onMove(e);
      evaluate();
    };

    const onUp = (e: PointerEvent) => {
      pts.delete(e.pointerId);
      if (pts.size < 2) gestureStart = null;
    };

    // Listener PASSIVI: non catturiamo mai l'evento a MapControls.
    const opts: AddEventListenerOptions = { passive: true };
    canvas.addEventListener("pointerdown", onDown, opts);
    canvas.addEventListener("pointermove", onMoveEvaluate, opts);
    canvas.addEventListener("pointerup", onUp, opts);
    canvas.addEventListener("pointercancel", onUp, opts);
    canvas.addEventListener("pointerleave", onUp, opts);

    return () => {
      canvas.removeEventListener("pointerdown", onDown);
      canvas.removeEventListener("pointermove", onMoveEvaluate);
      canvas.removeEventListener("pointerup", onUp);
      canvas.removeEventListener("pointercancel", onUp);
      canvas.removeEventListener("pointerleave", onUp);
    };
  }, [gl, viewLevel, transitioning, ascend]);

  return null;
}
