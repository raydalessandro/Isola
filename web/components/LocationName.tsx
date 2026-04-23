"use client";

import { Html } from "@react-three/drei";
import { useEffect, useRef, useState } from "react";

/**
 * Nome-overlay che appare solo durante un dwell acquisito.
 *
 * Niente background box, niente bordi: solo il nome in Caveat color ink
 * con un leggero text-shadow crema per tenere leggibilità su sfondi vari.
 * Fade-in 200ms su `visible=true`, fade-out 500ms su `visible=false` con
 * linger di 500ms dopo il rilascio (così non "scappa" appena alzi il dito).
 *
 * La posizione è 3D (world-space): il genitore passa già un position
 * leggermente sopra il pallino; noi lo spostiamo ulteriormente in screen
 * space di ~50px verso l'alto via marginTop, così il dito non copre il
 * testo durante il dwell (polish C.1).
 *
 * Implementazione stato:
 *   - `displayVisible` in React state, controllato da callback di
 *     setTimeout/queueMicrotask (mai setState sincrono nel body di
 *     useEffect → rispettiamo react-hooks/set-state-in-effect).
 *   - timer ref tenuto in useRef ma SEMPRE scritto/letto solo da
 *     callback (mai in render).
 */

type Props = {
  /** Testo del nome canonico. */
  label: string;
  /** world-space position — dove sta il nome nello spazio 3D. */
  position: [number, number, number];
  /** true = visibile (fade-in), false = nascosto (fade-out). */
  visible: boolean;
}

const LINGER_MS = 500;

export default function LocationName({ label, position, visible }: Props) {
  const [displayVisible, setDisplayVisible] = useState(false);
  const hideTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    if (visible) {
      // Annulla hide in coda e porta a visibile dopo il microtask corrente.
      if (hideTimerRef.current) {
        clearTimeout(hideTimerRef.current);
        hideTimerRef.current = null;
      }
      queueMicrotask(() => setDisplayVisible(true));
    } else {
      // Linger: dopo 500ms togliamo la classe visibile → CSS fa fade-out.
      if (hideTimerRef.current) clearTimeout(hideTimerRef.current);
      hideTimerRef.current = setTimeout(() => {
        hideTimerRef.current = null;
        setDisplayVisible(false);
      }, LINGER_MS);
    }
    return () => {
      if (hideTimerRef.current) {
        clearTimeout(hideTimerRef.current);
        hideTimerRef.current = null;
      }
    };
  }, [visible]);

  return (
    <Html
      position={position}
      center
      distanceFactor={10}
      pointerEvents="none"
      zIndexRange={[60, 40]}
    >
      <div
        className={`location-name ${displayVisible ? "visible" : ""}`}
        style={{
          pointerEvents: "none",
          // 50px sopra il pallino: l'anchor Html è già al centro del
          // punto, marginTop:-50px porta il testo fuori dalla zona
          // coperta dal dito durante il dwell. Usiamo marginTop invece
          // di transform così le CSS transition su transform (fade-in
          // con translateY) continuano a funzionare.
          marginTop: -50,
        }}
      >
        {label}
      </div>
    </Html>
  );
}
