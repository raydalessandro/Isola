"use client";

import { Html } from "@react-three/drei";

/**
 * Nome-overlay che appare solo durante un dwell acquisito.
 *
 * Niente background box, niente bordi: solo il nome in Caveat color ink
 * con un leggero text-shadow crema per tenere leggibilità su sfondi vari.
 * Fade-in 200ms su `visible=true`, fade-out 300ms su `visible=false`
 * (entrambi via CSS transition, vedi globals.css `.location-name`).
 *
 * La posizione è 3D (world-space): il genitore decide `position`; il
 * centraggio HTML è gestito da `center` su <Html>.
 */

type Props = {
  /** Testo del nome canonico. */
  label: string;
  /** world-space position — dove sta il nome nello spazio 3D. */
  position: [number, number, number];
  /** true = visibile (fade-in), false = nascosto (fade-out). */
  visible: boolean;
};

export default function LocationName({ label, position, visible }: Props) {
  return (
    <Html
      position={position}
      center
      distanceFactor={10}
      pointerEvents="none"
      zIndexRange={[60, 40]}
    >
      <div
        className={`location-name ${visible ? "visible" : ""}`}
        style={{ pointerEvents: "none" }}
      >
        {label}
      </div>
    </Html>
  );
}
