"use client";

import type { Quartiere } from "@/lib/geography";

type Props = {
  quartiere: Quartiere | null;
  onClose: () => void;
};

export default function HotspotPanel({ quartiere, onClose }: Props) {
  const open = quartiere !== null;
  return (
    <div
      aria-hidden={!open}
      className={[
        "fixed left-0 right-0 bottom-0 z-20",
        "pointer-events-none",
      ].join(" ")}
    >
      <div
        className={[
          "mx-auto max-w-[560px] w-full",
          "rounded-t-[28px]",
          "transition-transform duration-300 ease-out",
          open ? "translate-y-0" : "translate-y-[110%]",
          "pointer-events-auto",
        ].join(" ")}
        style={{
          backgroundColor: "var(--cream)",
          color: "var(--ink)",
          height: "42vh",
          minHeight: "260px",
          boxShadow: "0 -8px 32px rgba(42, 35, 25, 0.28)",
          borderTop: "1px solid rgba(107, 68, 35, 0.15)",
          paddingBottom: "env(safe-area-inset-bottom)",
        }}
      >
        <div className="flex items-center justify-center pt-3">
          <div
            style={{
              width: 44,
              height: 4,
              borderRadius: 2,
              background: "rgba(42, 35, 25, 0.25)",
            }}
          />
        </div>
        <div className="px-6 pt-4 pb-6 relative h-full flex flex-col">
          <button
            onClick={onClose}
            aria-label="Chiudi"
            className="absolute top-3 right-4 text-2xl leading-none"
            style={{
              color: "var(--warm-brown)",
              width: 36,
              height: 36,
              borderRadius: 18,
              background: "rgba(107, 68, 35, 0.08)",
            }}
          >
            ×
          </button>
          {quartiere && (
            <>
              <div
                className="font-hand"
                style={{
                  fontSize: 34,
                  fontWeight: 600,
                  color: quartiere.color,
                  lineHeight: 1.05,
                  letterSpacing: "0.01em",
                }}
              >
                {quartiere.label}
              </div>
              <div
                className="font-serif mt-3"
                style={{
                  fontSize: 18,
                  lineHeight: 1.5,
                  color: "var(--ink)",
                  opacity: 0.88,
                }}
              >
                {quartiere.descrizione}
              </div>
              <div
                className="font-serif mt-auto pt-4 italic"
                style={{
                  fontSize: 14,
                  color: "var(--warm-brown)",
                  opacity: 0.8,
                }}
              >
                Elevazione {quartiere.elevation_m} m · raggio{" "}
                {quartiere.radius_m} m
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
