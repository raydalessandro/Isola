"use client";

import { useEffect, useRef, useState } from "react";
import { useWorldStore } from "@/lib/store";

/**
 * Hint di discoverability per il gesto di ritorno — C.3.
 *
 * Il gesto è uno "swipe-down a due dita" (vedi TwoFingerSwipeDownListener
 * in IslandScene). L'hint mostra un testo nell'header alto al primo arrivo
 * su L1: "due dita giù per tornare".
 *
 * Comportamento:
 *  - al PRIMO arrivo su L1 nella sessione, dopo la fine della transizione,
 *    mostriamo per 2 secondi un suggerimento centrato in alto.
 *  - fade-out dopo 2s.
 *  - non rimostrato nella stessa sessione (flag in sessionStorage).
 *
 * Impl: evitiamo setState-in-effect. Lo stato `showTick` viene aggiornato
 * solo da:
 *   - microtask queue (queueMicrotask) quando le condizioni scattano (non è
 *     un setState sincrono diretto nel body dell'effect);
 *   - setTimeout per l'auto-hide.
 *
 * Il componente vive FUORI dal Canvas (DOM overlay) perché è UI classica,
 * non un'animazione WebGL.
 */

const SESSION_FLAG = "itv:pinchOutHintShown";

export default function PinchOutHint() {
  const viewLevel = useWorldStore((s) => s.viewLevel);
  const transitioning = useWorldStore((s) => s.transitioning);
  const [show, setShow] = useState(false);
  const hideTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    if (typeof window === "undefined") return;
    if (viewLevel !== "quartiere") return;
    if (transitioning) return;

    let shown = false;
    try {
      shown = sessionStorage.getItem(SESSION_FLAG) === "1";
    } catch {
      // sessionStorage bloccato: ignoriamo, mostriamo ogni volta.
    }
    if (shown) return;

    try {
      sessionStorage.setItem(SESSION_FLAG, "1");
    } catch {
      /* ignore */
    }

    // queueMicrotask per evitare setState sincrono dentro l'effect body.
    // Il setState viene eseguito "after the current effect body completes",
    // rispettando react-hooks/set-state-in-effect.
    queueMicrotask(() => setShow(true));
    hideTimerRef.current = setTimeout(() => {
      setShow(false);
      hideTimerRef.current = null;
    }, 2000);

    return () => {
      if (hideTimerRef.current) {
        clearTimeout(hideTimerRef.current);
        hideTimerRef.current = null;
      }
    };
  }, [viewLevel, transitioning]);

  return (
    <div
      className={`pinch-hint center${show ? " show" : ""}`}
      aria-hidden
    >
      due dita giù per tornare ↓
    </div>
  );
}
