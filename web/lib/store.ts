"use client";

import { create } from "zustand";

/**
 * Stato globale dell'interazione mappa/mondo.
 *
 * Due livelli di vista:
 *  - L0 "island"   → vista aerea con i 5 hotspot quartiere
 *  - L1 "quartiere" → camera scesa sul quartiere corrente; i suoi hotspot
 *                     location sono visibili come piccoli pin.
 *
 * Nessun popup, nessun pannello. L'unico "testo" ammesso è il nome-overlay
 * che appare durante un dwell (tap-and-hold). Lo stato del dwell vive qui
 * così Hotspot/LocationName/Breathing possono reagire senza prop-drilling.
 */

export type ViewLevel = "island" | "quartiere";

export interface WorldState {
  viewLevel: ViewLevel;
  /** id quartiere corrente quando viewLevel === "quartiere", altrimenti null. */
  currentQuartiere: string | null;
  /** id dell'hotspot su cui è in corso un dwell acquisito (>=500ms fermo). */
  dwellTargetId: string | null;
  /** ms epoch dell'inizio del dwell (per debug / future animazioni). */
  dwellStartedAt: number | null;
  /** true mentre la camera sta interpolando; MapControls è disabilitato. */
  transitioning: boolean;

  descend: (quartiereId: string) => void;
  ascend: () => void;
  setDwellTarget: (id: string | null) => void;
  setTransitioning: (value: boolean) => void;
}

export const useWorldStore = create<WorldState>((set, get) => ({
  viewLevel: "island",
  currentQuartiere: null,
  dwellTargetId: null,
  dwellStartedAt: null,
  transitioning: false,

  descend: (quartiereId: string) => {
    const state = get();
    if (state.transitioning) return;
    if (state.viewLevel === "quartiere" && state.currentQuartiere === quartiereId)
      return;
    set({
      viewLevel: "quartiere",
      currentQuartiere: quartiereId,
      transitioning: true,
      dwellTargetId: null,
      dwellStartedAt: null,
    });
  },

  ascend: () => {
    const state = get();
    if (state.transitioning) return;
    if (state.viewLevel === "island") return;
    set({
      viewLevel: "island",
      currentQuartiere: null,
      transitioning: true,
      dwellTargetId: null,
      dwellStartedAt: null,
    });
  },

  setDwellTarget: (id: string | null) => {
    if (id === null) {
      set({ dwellTargetId: null, dwellStartedAt: null });
    } else {
      set({ dwellTargetId: id, dwellStartedAt: Date.now() });
    }
  },

  setTransitioning: (value: boolean) => {
    set({ transitioning: value });
  },
}));
