export type Quartiere = {
  id: string;
  label: string;
  center: { x: number; z: number };
  radius_m: number;
  elevation_m: number;
  color: string;
  descrizione: string;
};

export type IslandGeography = {
  version: string;
  island: {
    bounds: {
      width_m: number;
      depth_m: number;
      unit_scale_three: number;
    };
    shape: "oval" | "circle" | "rect";
  };
  quartieri: Quartiere[];
  notes?: string;
};

/**
 * Convert a world coordinate (meters) to Three.js scene units.
 * 1 Three.js unit = 100 m (unit_scale_three). Three.js Y is up;
 * our canonical x = east, z = south (positive), y = elevation.
 */
export function metersToUnits(meters: number, scale = 100): number {
  return meters / scale;
}

/**
 * Palette — mirror of legacy/index.html CSS variables so the 3D scene
 * stays coherent with the paper-map prototype.
 */
export const PALETTE = {
  cream: "#f5ead5",
  creamShade: "#ebdebe",
  creamDeep: "#e0ceaa",
  terracotta: "#c8532c",
  terracottaDeep: "#9c3d1e",
  olive: "#5c6b3b",
  oliveLight: "#8a9a6b",
  sea: "#1e5d6e",
  seaLight: "#4a8595",
  seaDeep: "#0f3a48",
  ink: "#2a2319",
  warmBrown: "#6b4423",
  sun: "#e8a547",
  sand: "#d8bd8a",
} as const;
