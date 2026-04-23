"use client";

import { useState, Suspense } from "react";
import { Canvas } from "@react-three/fiber";
import { MapControls, Sky } from "@react-three/drei";
import * as THREE from "three";
import Island from "./Island";
import Ocean from "./Ocean";
import Hotspot from "./Hotspot";
import HotspotPanel from "./HotspotPanel";
import type { IslandGeography, Quartiere } from "@/lib/geography";
import { PALETTE } from "@/lib/geography";

type Props = {
  geography: IslandGeography;
};

export default function IslandScene({ geography }: Props) {
  const [selected, setSelected] = useState<Quartiere | null>(null);

  const widthUnits =
    geography.island.bounds.width_m /
    geography.island.bounds.unit_scale_three;
  const depthUnits =
    geography.island.bounds.depth_m /
    geography.island.bounds.unit_scale_three;

  return (
    <div className="fixed inset-0" style={{ background: PALETTE.sea }}>
      <Canvas
        shadows
        dpr={[1, 2]}
        camera={{
          position: [0, 90, 90],
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
        <hemisphereLight
          args={[PALETTE.cream, PALETTE.sea, 0.35]}
        />
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

          {geography.quartieri.map((q) => (
            <Hotspot
              key={q.id}
              quartiere={q}
              onSelect={(qq) => setSelected(qq)}
            />
          ))}
        </Suspense>

        {/* Google-Earth-ish camera: rotate w/ drag, zoom w/ pinch,
            two-finger pan. Tilt clamped so you can't flip under the island. */}
        <MapControls
          enableDamping
          dampingFactor={0.12}
          minDistance={15}
          maxDistance={220}
          maxPolarAngle={Math.PI * 0.48}
          minPolarAngle={Math.PI * 0.08}
          target={[0, 0, 0]}
          screenSpacePanning={false}
        />
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

      {/* Hint on first load */}
      {!selected && (
        <div
          className="fixed left-0 right-0 z-10 flex justify-center pointer-events-none"
          style={{
            bottom: "calc(env(safe-area-inset-bottom) + 16px)",
          }}
        >
          <div
            className="font-serif"
            style={{
              fontSize: 14,
              color: PALETTE.cream,
              opacity: 0.8,
              textShadow: "0 1px 2px rgba(0,0,0,0.4)",
            }}
          >
            Tocca un segnaposto per esplorare
          </div>
        </div>
      )}

      <HotspotPanel
        quartiere={selected}
        onClose={() => setSelected(null)}
      />
    </div>
  );
}
