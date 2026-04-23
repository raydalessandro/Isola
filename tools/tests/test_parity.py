"""Test di parità fra il modulo Python (tools/geography.py) e il mirror
TypeScript (web/lib/geography.ts).

Esegue le stesse query in entrambi gli ambienti e verifica che i risultati
numerici combacino entro tolleranza 0.01 (m / min).

Il ponte verso TS è `tools/tests/parity_runner.mts`, eseguito via
`node --experimental-strip-types`. Se `node` non è disponibile (ambiente
CI minimale), i test sono skippati senza fallire.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import unittest
from pathlib import Path

from tools.geography import IslandGeography

REPO_ROOT = Path(__file__).resolve().parents[2]
RUNNER = Path(__file__).resolve().parent / "parity_runner.mts"

NODE = shutil.which("node")
# Richiediamo Node >= 22 per --experimental-strip-types di default.
NODE_OK = False
if NODE:
    try:
        out = subprocess.check_output([NODE, "--version"], text=True).strip()
        # "v22.x.y"
        major = int(out.lstrip("v").split(".")[0])
        NODE_OK = major >= 22
    except (subprocess.SubprocessError, ValueError):
        NODE_OK = False


def _run_ts(queries: list[dict]) -> list[dict]:
    """Esegue la lista di query nel runner TS e ritorna i risultati."""
    assert NODE is not None
    payload = json.dumps(queries)
    proc = subprocess.run(
        [NODE, "--experimental-strip-types", str(RUNNER)],
        input=payload,
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
        timeout=30,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"parity_runner fallito (exit {proc.returncode}):\n"
            f"stdout: {proc.stdout}\nstderr: {proc.stderr}"
        )
    return json.loads(proc.stdout)


# 10 query standard. Copre: distance, walking_time per i 4 preset,
# path, path_distance, nearby, quartiere_of, elevation.
PARITY_QUERIES: list[dict] = [
    {"type": "distance", "a": "forno_di_fiamma", "b": "grotta_di_grunto"},
    {"type": "walking_time", "a": "albero_vecchio", "b": "roccia_alta",
     "speed": "adult_walk"},
    {"type": "walking_time", "a": "albero_vecchio", "b": "roccia_alta",
     "speed": "child_walk"},
    {"type": "walking_time", "a": "albero_vecchio", "b": "grotta_di_grunto",
     "speed": "bartolo_walk"},
    {"type": "walking_time", "a": "pontile_di_bartolo", "b": "casa_tana_di_rovo",
     "speed": "child_run"},
    {"type": "path", "a": "orti_del_cerchio", "b": "pontile_di_bartolo"},
    {"type": "path_distance", "a": "albero_vecchio", "b": "casa_tana_di_rovo"},
    {"type": "nearby", "loc": "albero_vecchio", "radius_m": 250},
    {"type": "quartiere_of", "loc": "forno_di_fiamma"},
    {"type": "elevation", "loc": "grotta_di_grunto"},
    # nuove query: feature enrichment
    {"type": "distance_to_river", "loc": "albero_vecchio"},
    {"type": "distance_to_river", "loc": "casa_del_mattino"},
    {"type": "terrain_profile", "quartiere": "pontile"},
    {"type": "anchor_points_count"},
]


@unittest.skipUnless(
    NODE_OK,
    "Node.js >= 22 non disponibile: skip parity test",
)
class TestPythonTsParity(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.geo = IslandGeography()
        cls.ts_results = _run_ts(PARITY_QUERIES)

    def _py_run(self, q: dict) -> dict:
        t = q["type"]
        if t == "distance":
            return {"value_m": self.geo.distance(q["a"], q["b"])}
        if t == "walking_time":
            return {
                "value_min": self.geo.walking_time(q["a"], q["b"], speed=q["speed"])
            }
        if t == "path":
            return {"route": self.geo.path(q["a"], q["b"])}
        if t == "path_distance":
            return {"value_m": self.geo.path_distance(q["a"], q["b"])}
        if t == "nearby":
            return {"ids": self.geo.nearby(q["loc"], radius_m=q["radius_m"])}
        if t == "quartiere_of":
            return {"quartiere": self.geo.quartiere_of(q["loc"])}
        if t == "elevation":
            return {"value_m": self.geo.elevation(q["loc"])}
        if t == "distance_to_river":
            return {"value_m": self.geo.distance_to_river(q["loc"])}
        if t == "terrain_profile":
            return {"profile": self.geo.terrain_profile(q["quartiere"])}
        if t == "anchor_points_count":
            return {"count": len(self.geo.anchor_points())}
        raise ValueError(f"query sconosciuta: {t}")

    def _assert_match(self, py_out: dict, ts_out: dict, q: dict) -> None:
        if "value_m" in py_out:
            self.assertAlmostEqual(
                py_out["value_m"], ts_out["value_m"], delta=0.01,
                msg=f"query={q}",
            )
        elif "value_min" in py_out:
            self.assertAlmostEqual(
                py_out["value_min"], ts_out["value_min"], delta=0.01,
                msg=f"query={q}",
            )
        elif "route" in py_out:
            self.assertEqual(py_out["route"], ts_out["route"], msg=f"query={q}")
        elif "ids" in py_out:
            self.assertEqual(py_out["ids"], ts_out["ids"], msg=f"query={q}")
        elif "quartiere" in py_out:
            self.assertEqual(
                py_out["quartiere"], ts_out["quartiere"], msg=f"query={q}"
            )
        elif "profile" in py_out:
            self.assertEqual(
                py_out["profile"], ts_out["profile"], msg=f"query={q}"
            )
        elif "count" in py_out:
            self.assertEqual(py_out["count"], ts_out["count"], msg=f"query={q}")
        else:
            self.fail(f"output Python non riconosciuto: {py_out}")

    def test_results_have_same_length(self) -> None:
        self.assertEqual(len(self.ts_results), len(PARITY_QUERIES))

    def test_parity_distance(self) -> None:
        q = PARITY_QUERIES[0]
        self._assert_match(self._py_run(q), self.ts_results[0], q)

    def test_parity_walking_time_adult(self) -> None:
        q = PARITY_QUERIES[1]
        self._assert_match(self._py_run(q), self.ts_results[1], q)

    def test_parity_walking_time_child(self) -> None:
        q = PARITY_QUERIES[2]
        self._assert_match(self._py_run(q), self.ts_results[2], q)

    def test_parity_walking_time_bartolo(self) -> None:
        q = PARITY_QUERIES[3]
        self._assert_match(self._py_run(q), self.ts_results[3], q)

    def test_parity_walking_time_run(self) -> None:
        q = PARITY_QUERIES[4]
        self._assert_match(self._py_run(q), self.ts_results[4], q)

    def test_parity_path(self) -> None:
        q = PARITY_QUERIES[5]
        self._assert_match(self._py_run(q), self.ts_results[5], q)

    def test_parity_path_distance(self) -> None:
        q = PARITY_QUERIES[6]
        self._assert_match(self._py_run(q), self.ts_results[6], q)

    def test_parity_nearby(self) -> None:
        q = PARITY_QUERIES[7]
        self._assert_match(self._py_run(q), self.ts_results[7], q)

    def test_parity_quartiere_of(self) -> None:
        q = PARITY_QUERIES[8]
        self._assert_match(self._py_run(q), self.ts_results[8], q)

    def test_parity_elevation(self) -> None:
        q = PARITY_QUERIES[9]
        self._assert_match(self._py_run(q), self.ts_results[9], q)

    def test_parity_distance_to_river_albero(self) -> None:
        q = PARITY_QUERIES[10]
        self._assert_match(self._py_run(q), self.ts_results[10], q)

    def test_parity_distance_to_river_casa_mattino(self) -> None:
        q = PARITY_QUERIES[11]
        self._assert_match(self._py_run(q), self.ts_results[11], q)

    def test_parity_terrain_profile(self) -> None:
        q = PARITY_QUERIES[12]
        self._assert_match(self._py_run(q), self.ts_results[12], q)

    def test_parity_anchor_points_count(self) -> None:
        q = PARITY_QUERIES[13]
        self._assert_match(self._py_run(q), self.ts_results[13], q)


if __name__ == "__main__":
    unittest.main()
