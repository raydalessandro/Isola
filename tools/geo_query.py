"""CLI di interrogazione della geografia dell'isola.

Esempi:
    python -m tools.geo_query distance forno_di_fiamma grotta_di_grunto
    python -m tools.geo_query walking-time forno_di_fiamma grotta_di_grunto --speed child_walk
    python -m tools.geo_query path orti_del_cerchio pontile_di_bartolo
    python -m tools.geo_query nearby albero_vecchio --radius 200
    python -m tools.geo_query list
    python -m tools.geo_query list --quartiere pontile

Usa --json per output strutturato.
"""
from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from tools.geography import (
    WALKING_SPEEDS_MPS,
    IslandGeography,
)


def _emit(value: Any, as_json: bool) -> None:
    if as_json:
        json.dump(value, sys.stdout, ensure_ascii=False, indent=2, sort_keys=True)
        sys.stdout.write("\n")
    else:
        if isinstance(value, str):
            sys.stdout.write(value + "\n")
        else:
            sys.stdout.write(str(value) + "\n")


def cmd_distance(geo: IslandGeography, args: argparse.Namespace) -> int:
    meters = geo.distance(args.a, args.b)
    if args.json:
        _emit(
            {"from": args.a, "to": args.b, "distance_m": round(meters, 1)},
            True,
        )
    else:
        _emit(f"{meters:.0f} m", False)
    return 0


def cmd_walking_time(geo: IslandGeography, args: argparse.Namespace) -> int:
    minutes = geo.walking_time(args.a, args.b, speed=args.speed)
    if args.json:
        _emit(
            {
                "from": args.a,
                "to": args.b,
                "speed": args.speed,
                "minutes": round(minutes, 1),
            },
            True,
        )
    else:
        _emit(f"{minutes:.1f} min ({args.speed})", False)
    return 0


def cmd_path(geo: IslandGeography, args: argparse.Namespace) -> int:
    route = geo.path(args.a, args.b)
    total_m = geo.path_distance(args.a, args.b)
    if args.json:
        _emit(
            {
                "from": args.a,
                "to": args.b,
                "route": route,
                "hops": max(0, len(route) - 1),
                "distance_m": round(total_m, 1),
            },
            True,
        )
    else:
        hops = max(0, len(route) - 1)
        arrow = " -> ".join(route)
        _emit(f"{arrow} ({hops} archi, {total_m/1000:.2f} km)", False)
    return 0


def cmd_nearby(geo: IslandGeography, args: argparse.Namespace) -> int:
    ids = geo.nearby(args.loc, radius_m=args.radius)
    if args.json:
        items = []
        for oid in ids:
            d = geo.distance(args.loc, oid)
            items.append({"id": oid, "distance_m": round(d, 1)})
        _emit({"center": args.loc, "radius_m": args.radius, "nearby": items}, True)
    else:
        if not ids:
            _emit(f"(nessun luogo entro {args.radius} m)", False)
        else:
            for oid in ids:
                d = geo.distance(args.loc, oid)
                loc = geo.location(oid)
                sys.stdout.write(
                    f"{loc.nome_canonico} [{oid}] ({d:.0f} m)\n"
                )
    return 0


def cmd_list(geo: IslandGeography, args: argparse.Namespace) -> int:
    locs = geo.all_locations()
    if args.quartiere:
        locs = [l for l in locs if l.quartiere == args.quartiere]
    if args.json:
        items = []
        for loc in locs:
            items.append(
                {
                    "id": loc.id,
                    "nome_canonico": loc.nome_canonico,
                    "categoria": loc.categoria,
                    "quartiere": loc.quartiere,
                    "coords": {
                        "x": loc.coords.x,
                        "z": loc.coords.z,
                        "y": loc.coords.y,
                    },
                    "porta_socchiusa": loc.porta_socchiusa,
                }
            )
        _emit(items, True)
    else:
        if not locs:
            _emit("(nessuna location)", False)
            return 0
        # colonne: id, nome, quartiere, coords
        w_id = max(len(l.id) for l in locs)
        w_nome = max(len(l.nome_canonico) for l in locs)
        for loc in locs:
            q = loc.quartiere if loc.quartiere else "—"
            coords = (
                f"(x={loc.coords.x:>6.0f} z={loc.coords.z:>6.0f} "
                f"y={loc.coords.y:>4.0f})"
            )
            mark = " [porta socchiusa]" if loc.porta_socchiusa else ""
            sys.stdout.write(
                f"{loc.id.ljust(w_id)}  "
                f"{loc.nome_canonico.ljust(w_nome)}  "
                f"[{q}]  {coords}{mark}\n"
            )
    return 0


def cmd_quartiere_of(geo: IslandGeography, args: argparse.Namespace) -> int:
    q = geo.quartiere_of(args.loc)
    if args.json:
        _emit({"loc": args.loc, "quartiere": q}, True)
    else:
        _emit(q if q else "(nessun quartiere)", False)
    return 0


def cmd_distance_to_river(
    geo: IslandGeography, args: argparse.Namespace
) -> int:
    meters = geo.distance_to_river(args.loc)
    if args.json:
        _emit(
            {"loc": args.loc, "distance_to_river_m": round(meters, 1)},
            True,
        )
    else:
        _emit(f"{meters:.0f} m dal Fiume che Gira", False)
    return 0


def cmd_visible_from(geo: IslandGeography, args: argparse.Namespace) -> int:
    ids = geo.visible_from(args.loc, elevation_bonus_m=args.bonus)
    if args.json:
        items = []
        for oid in ids:
            d = geo.distance(args.loc, oid)
            items.append({"id": oid, "distance_m": round(d, 1)})
        _emit(
            {
                "observer": args.loc,
                "elevation_bonus_m": args.bonus,
                "visible": items,
                "note": "Euristica approssimata, non true line-of-sight.",
            },
            True,
        )
    else:
        if not ids:
            _emit("(niente visibile)", False)
            return 0
        for oid in ids:
            d = geo.distance(args.loc, oid)
            loc = geo.location(oid)
            sys.stdout.write(f"{loc.nome_canonico} [{oid}] ({d:.0f} m)\n")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="python -m tools.geo_query",
        description=(
            "Interroga la geografia dell'Isola dei Tre Venti "
            "(world/geography/*.json)."
        ),
    )
    p.add_argument(
        "--json",
        action="store_true",
        help="Output strutturato JSON invece di testo leggibile.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("distance", help="distanza in linea retta (m)")
    s.add_argument("a")
    s.add_argument("b")
    s.set_defaults(func=cmd_distance)

    s = sub.add_parser(
        "walking-time",
        help="tempo di percorrenza in minuti lungo la rete sentieri",
    )
    s.add_argument("a")
    s.add_argument("b")
    s.add_argument(
        "--speed",
        choices=sorted(WALKING_SPEEDS_MPS.keys()),
        default="adult_walk",
        help="preset di velocità (default: adult_walk)",
    )
    s.set_defaults(func=cmd_walking_time)

    s = sub.add_parser("path", help="cammino nella rete sentieri (Dijkstra)")
    s.add_argument("a")
    s.add_argument("b")
    s.set_defaults(func=cmd_path)

    s = sub.add_parser("nearby", help="luoghi entro un raggio")
    s.add_argument("loc")
    s.add_argument("--radius", type=float, default=500.0)
    s.set_defaults(func=cmd_nearby)

    s = sub.add_parser("list", help="elenca tutte le location")
    s.add_argument(
        "--quartiere",
        help="filtra per quartiere (centro/forno/pontile/orti/montagne)",
    )
    s.set_defaults(func=cmd_list)

    s = sub.add_parser("quartiere-of", help="quartiere contenente un luogo")
    s.add_argument("loc")
    s.set_defaults(func=cmd_quartiere_of)

    s = sub.add_parser(
        "distance-to-river",
        help="distanza minima in metri dal Fiume che Gira",
    )
    s.add_argument("loc")
    s.set_defaults(func=cmd_distance_to_river)

    s = sub.add_parser(
        "visible-from",
        help="euristica (approssimata) di visibilità da un luogo",
    )
    s.add_argument("loc")
    s.add_argument(
        "--bonus",
        type=float,
        default=0.0,
        help="bonus altezza osservatore (es. tetto/albero)",
    )
    s.set_defaults(func=cmd_visible_from)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    geo = IslandGeography()
    return int(args.func(geo, args))


if __name__ == "__main__":
    sys.exit(main())
