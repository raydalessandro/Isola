"use client";

import { useMemo } from "react";
import * as THREE from "three";
import { createNoise2D } from "simplex-noise";
import type {
  IslandGeographyData,
  TerrainDoc,
} from "@/lib/geography";
import { PALETTE } from "@/lib/geography";

type Props = {
  widthUnits: number; // es. 80 = 8 km
  depthUnits: number; // es. 70 = 7 km
  geography: IslandGeographyData;
  terrain: TerrainDoc;
};

/**
 * Heightmap anchor-based + colori per quartiere (vertex color blend).
 *
 * Strategia elevazione (A.1):
 *  - lettura di `terrain.json::heightmap_anchors` (13 punti in metri).
 *  - per ogni vertice della PlaneGeometry calcoliamo IDW (inverse-distance
 *    weighting, p=2) sui 4 anchor più vicini — questo produce una quota
 *    "scultorea" coerente col canone (Montagne ~450m, Pascoli ~200m,
 *    Villaggio ~10m, costa ~0m).
 *  - sommiamo ~15% di simplex-noise a due ottave come micro-rugosità
 *    organica, attenuato verso i bordi dell'isola e sulle coste piatte.
 *  - smoothstep falloff sul bordo per terminare a y=0 al margine della
 *    PlaneGeometry (evita muri verticali alla coast).
 *
 * Strategia colore (A.2):
 *  - per ogni vertice calcoliamo "appartenenza" morbida ai 5 quartieri
 *    con peso gaussiano centrato su `quartiere.center` e sigma=radius_m.
 *  - vertex_color = weighted blend dei `base_color` (da terrain.json).
 *  - sulla fascia fuori dai 5 quartieri fade verso sand costiero
 *    (#d8bd8a) e poi verso il sea-teal ai bordi del plane.
 *
 * Determinismo: seed noise fisso (1337); output identico a ogni reload.
 * Scala: 1 unità Three = 100 m (island.json::unit_scale_three).
 */
export default function TerrainHeightmap({
  widthUnits,
  depthUnits,
  geography,
  terrain,
}: Props) {
  const scale = geography.island.bounds.unit_scale_three; // 100

  const material = useMemo(
    () =>
      new THREE.MeshStandardMaterial({
        vertexColors: true,
        flatShading: true,
        roughness: 0.92,
        metalness: 0,
      }),
    [],
  );

  const geometry = useMemo(() => {
    const segX = 96;
    const segZ = 84;
    const geo = new THREE.PlaneGeometry(widthUnits, depthUnits, segX, segZ);
    geo.rotateX(-Math.PI / 2);

    // Deterministic seed → stessa isola ogni load.
    let seed = 1337;
    const rng = () => {
      seed = (seed * 9301 + 49297) % 233280;
      return seed / 233280;
    };
    const n1 = createNoise2D(rng);
    const n2 = createNoise2D(rng);

    // Anchor points in metri — convertiti in unità Three.
    const anchors = terrain.heightmap_anchors.map((a) => ({
      x: a.x / scale,
      z: a.z / scale,
      y: a.y / scale, // in unità Three (450m → 4.5 u)
    }));

    const pos = geo.attributes.position as THREE.BufferAttribute;
    const halfW = widthUnits / 2;
    const halfD = depthUnits / 2;

    // Per ogni vertice: IDW sulle 4 anchor più vicine (power p=2) + noise
    // residuo (~15% dell'ampiezza totale osservata).
    const K = 4;
    const P = 2; // potenza IDW

    for (let i = 0; i < pos.count; i++) {
      const x = pos.getX(i);
      const z = pos.getZ(i);

      // Falloff ovale morbido sul margine: 1 al centro, 0 al bordo.
      // Usato per assicurare che il terreno termini a y=0 alla shore.
      const nx = x / halfW;
      const nz = z / halfD;
      const r = Math.sqrt(nx * nx + nz * nz);
      const edgeFade = Math.max(0, 1 - r);
      const edgeMask = edgeFade * edgeFade * (3 - 2 * edgeFade); // smoothstep

      // Trova le K anchor più vicine (sorted by dist ascending).
      const ranked: Array<{ d: number; y: number }> = [];
      for (const a of anchors) {
        const dx = x - a.x;
        const dz = z - a.z;
        const d = Math.sqrt(dx * dx + dz * dz);
        ranked.push({ d, y: a.y });
      }
      ranked.sort((u, v) => u.d - v.d);

      // IDW sui primi K.
      let yIdw: number;
      if (ranked[0].d < 1e-4) {
        // Sulla anchor: copia il valore esatto.
        yIdw = ranked[0].y;
      } else {
        let num = 0;
        let den = 0;
        for (let k = 0; k < K && k < ranked.length; k++) {
          const w = 1 / Math.pow(ranked[k].d, P);
          num += w * ranked[k].y;
          den += w;
        }
        yIdw = num / den;
      }

      // Noise residuo a due ottave — ampiezza piccola (~15% di 4.5u ≈ 0.7u).
      const noise =
        n1(x * 0.18, z * 0.18) * 0.4 + n2(x * 0.55, z * 0.55) * 0.2;
      const noiseAmp = 0.45; // unità Three, ~45m di rugosità max
      const microRelief = noise * noiseAmp * (0.3 + 0.7 * edgeMask);

      // Quota finale: IDW + micro-relief, gently clampata a ≥0 tramite
      // edgeMask alla costa per evitare terreno "impiccato" fuori dal bordo.
      const y = yIdw * edgeMask + microRelief * edgeMask;

      pos.setY(i, y);
    }

    pos.needsUpdate = true;
    geo.computeVertexNormals();
    return geo;
  }, [widthUnits, depthUnits, terrain, scale]);

  // A.2: vertex color per quartiere — blend gaussiano sul centro di ciascuno.
  const coloredGeometry = useMemo(() => {
    const colors = new Float32Array(geometry.attributes.position.count * 3);
    const pos = geometry.attributes.position as THREE.BufferAttribute;

    // Prepara palette per ogni quartiere (da terrain.json se presente,
    // altrimenti fallback a island.json). Sigma = radius_m / scale.
    const halfW = widthUnits / 2;
    const halfD = depthUnits / 2;

    const quartieriInfo = geography.quartieri.map((q) => {
      const profile = terrain.quartieri_profiles[q.id];
      const hex = profile?.base_color ?? q.color;
      return {
        id: q.id,
        cx: q.center.x / scale,
        cz: q.center.z / scale,
        sigma: q.radius_m / scale, // unità Three
        color: new THREE.Color(hex),
      };
    });

    const sand = new THREE.Color(PALETTE.sand);
    const seaTeal = new THREE.Color(PALETTE.sea);

    const tmp = new THREE.Color();
    for (let i = 0; i < pos.count; i++) {
      const x = pos.getX(i);
      const z = pos.getZ(i);

      // Peso gaussiano su ciascun quartiere — soft appartenenza.
      let totalW = 0;
      const weights: number[] = [];
      for (const q of quartieriInfo) {
        const dx = x - q.cx;
        const dz = z - q.cz;
        const d2 = dx * dx + dz * dz;
        // Gaussian: exp(-d^2 / (2*sigma^2)); con sigma=radius_m il peso a
        // d=radius cade a ~0.6 → morbido overlap tra quartieri vicini.
        const w = Math.exp(-d2 / (2 * q.sigma * q.sigma));
        weights.push(w);
        totalW += w;
      }

      // Peso complessivo "dentro qualche quartiere" 0..1 (monotone, clampato).
      // Usa il max (non la somma) perché una somma di overlap gonfia il valore.
      const membership = Math.min(1, Math.max(...weights));

      // Blend dei colori quartiere pesato.
      let qR = 0;
      let qG = 0;
      let qB = 0;
      if (totalW > 0) {
        for (let k = 0; k < quartieriInfo.length; k++) {
          const w = weights[k] / totalW;
          qR += w * quartieriInfo[k].color.r;
          qG += w * quartieriInfo[k].color.g;
          qB += w * quartieriInfo[k].color.b;
        }
      }

      // Fuori dai quartieri: fade a sand e poi a sea verso il bordo.
      const nx = x / halfW;
      const nz = z / halfD;
      const r = Math.sqrt(nx * nx + nz * nz);
      // shore band: 0 all'interno (r<0.75), 1 al bordo r≥1.
      const shoreT = THREE.MathUtils.clamp((r - 0.75) / 0.25, 0, 1);
      const shoreSmooth = shoreT * shoreT * (3 - 2 * shoreT);

      // Color pipeline:
      //   base = blend quartieri (se membership > 0), altrimenti sand.
      //   poi lerp verso sand in funzione di (1 - membership) (zona "fuori").
      //   infine lerp verso sea in funzione di shoreSmooth.
      // Risultato: quartieri chiari, fascia costiera sabbiosa, bordo teal.
      const r0 = qR * membership + sand.r * (1 - membership);
      const g0 = qG * membership + sand.g * (1 - membership);
      const b0 = qB * membership + sand.b * (1 - membership);

      tmp.setRGB(
        r0 + (seaTeal.r - r0) * shoreSmooth * 0.85,
        g0 + (seaTeal.g - g0) * shoreSmooth * 0.85,
        b0 + (seaTeal.b - b0) * shoreSmooth * 0.85,
      );

      colors[i * 3] = tmp.r;
      colors[i * 3 + 1] = tmp.g;
      colors[i * 3 + 2] = tmp.b;
    }

    geometry.setAttribute("color", new THREE.BufferAttribute(colors, 3));
    return geometry;
  }, [geometry, geography, terrain, scale, widthUnits, depthUnits]);

  return (
    <mesh
      geometry={coloredGeometry}
      material={material}
      castShadow
      receiveShadow
    />
  );
}
