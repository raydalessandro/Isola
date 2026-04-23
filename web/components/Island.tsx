"use client";

import { useMemo } from "react";
import * as THREE from "three";
import { createNoise2D } from "simplex-noise";
import { PALETTE } from "@/lib/geography";

type Props = {
  widthUnits: number; // 80 for 8km at scale 100
  depthUnits: number; // 70 for 7km
};

/**
 * Low-poly flat-shaded heightmap.
 *
 * Terrain model (procedural, deterministic seed):
 *   base = oval falloff → elevation 0 at edges, 1 at center
 *   mountains = north bias (negative z) lifts significantly
 *   plains = center is a gentle plateau (~villaggio at y≈0.5)
 *   noise = 2 octaves of simplex for organic micro-relief
 *
 * Flat shading on the mesh gives each triangle its own normal, producing the
 * faceted "paper-origami" look that matches the book's illustrated palette.
 */
export default function Island({ widthUnits, depthUnits }: Props) {
  const geometry = useMemo(() => {
    const segX = 96;
    const segZ = 84;
    const geo = new THREE.PlaneGeometry(
      widthUnits,
      depthUnits,
      segX,
      segZ,
    );
    geo.rotateX(-Math.PI / 2);

    // Deterministic seed — same island every load.
    let seed = 1337;
    const rng = () => {
      seed = (seed * 9301 + 49297) % 233280;
      return seed / 233280;
    };
    const n1 = createNoise2D(rng);
    const n2 = createNoise2D(rng);

    const pos = geo.attributes.position as THREE.BufferAttribute;
    const halfW = widthUnits / 2;
    const halfD = depthUnits / 2;
    const maxElevation = 7.5; // ≈ 750 m at the mountain ridge

    for (let i = 0; i < pos.count; i++) {
      const x = pos.getX(i);
      const z = pos.getZ(i);

      // Oval falloff: 1 at center, 0 at bounds, smooth.
      const nx = x / halfW;
      const nz = z / halfD;
      const r = Math.sqrt(nx * nx + nz * nz);
      const falloff = Math.max(0, 1 - r);
      const mask = falloff * falloff * (3 - 2 * falloff); // smoothstep

      // Mountain bias in the north (z negative).
      const northBias = Math.max(0, -nz);
      const mountain = Math.pow(northBias, 1.4) * 0.75;

      // Organic noise.
      const noise =
        n1(x * 0.05, z * 0.05) * 0.5 + n2(x * 0.15, z * 0.15) * 0.25;

      let y = mask * (0.25 + mountain + noise * 0.35) * maxElevation;

      // Central plateau (villaggio): flatten gently within ~5 units of origin.
      const centerDist = Math.sqrt(x * x + z * z);
      if (centerDist < 6) {
        const k = 1 - centerDist / 6;
        y = y * (1 - k * 0.55) + 0.35 * k;
      }

      // Below zero near shore gets clipped to a thin beach.
      if (mask < 0.04) y = -0.4;

      pos.setY(i, y);
    }

    pos.needsUpdate = true;
    geo.computeVertexNormals();
    return geo;
  }, [widthUnits, depthUnits]);

  // Two-tone vertex coloring: grass on slopes, sand near the water,
  // stone on the peaks. Also low-saturation to stay inside the cream palette.
  const material = useMemo(() => {
    const mat = new THREE.MeshStandardMaterial({
      vertexColors: true,
      flatShading: true,
      roughness: 0.95,
      metalness: 0,
    });
    return mat;
  }, []);

  const coloredGeometry = useMemo(() => {
    const colors = new Float32Array(geometry.attributes.position.count * 3);
    const pos = geometry.attributes.position as THREE.BufferAttribute;

    const grass = new THREE.Color(PALETTE.oliveLight);
    const sand = new THREE.Color(PALETTE.sand);
    const stone = new THREE.Color(PALETTE.warmBrown);
    const cream = new THREE.Color(PALETTE.creamDeep);

    for (let i = 0; i < pos.count; i++) {
      const y = pos.getY(i);
      const c = new THREE.Color();
      if (y < 0) {
        c.copy(sand);
      } else if (y < 1) {
        c.lerpColors(sand, cream, y);
      } else if (y < 3.5) {
        c.lerpColors(cream, grass, (y - 1) / 2.5);
      } else {
        c.lerpColors(grass, stone, Math.min(1, (y - 3.5) / 3));
      }
      colors[i * 3] = c.r;
      colors[i * 3 + 1] = c.g;
      colors[i * 3 + 2] = c.b;
    }

    geometry.setAttribute("color", new THREE.BufferAttribute(colors, 3));
    return geometry;
  }, [geometry]);

  return (
    <mesh
      geometry={coloredGeometry}
      material={material}
      castShadow
      receiveShadow
    />
  );
}
