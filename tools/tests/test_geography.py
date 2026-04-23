"""Test della libreria geografia.

Usa unittest stdlib (pytest non è richiesto). Eseguibile con:
    python -m unittest tools.tests.test_geography
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.geography import (
    DIFFICULTY_MULTIPLIER,
    WALKING_SPEEDS_MPS,
    IslandGeography,
    Location,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
GEO_DIR = REPO_ROOT / "world" / "geography"


class TestGeographyBasics(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.geo = IslandGeography()

    def test_all_locations_loaded(self) -> None:
        locs = self.geo.all_locations()
        # ci sono almeno 26 luoghi canonici (il task ne prevede 26+)
        self.assertGreaterEqual(len(locs), 26)
        # tutti gli id unici
        ids = [l.id for l in locs]
        self.assertEqual(len(ids), len(set(ids)))

    def test_location_returns_expected_type(self) -> None:
        loc = self.geo.location("albero_vecchio")
        self.assertIsInstance(loc, Location)
        self.assertEqual(loc.id, "albero_vecchio")
        self.assertEqual(loc.quartiere, "centro")

    def test_unknown_location_raises(self) -> None:
        with self.assertRaises(KeyError):
            self.geo.location("non_esiste")

    def test_quartieri_present(self) -> None:
        qs = self.geo.quartieri()
        ids = {q["id"] for q in qs}
        self.assertEqual(
            ids, {"centro", "forno", "pontile", "orti", "montagne"}
        )

    def test_quartiere_of(self) -> None:
        self.assertEqual(
            self.geo.quartiere_of("forno_di_fiamma"), "forno"
        )
        self.assertEqual(
            self.geo.quartiere_of("grotta_di_grunto"), "montagne"
        )
        # fiume/guado/isole non hanno quartiere
        self.assertIsNone(self.geo.quartiere_of("fiume_che_gira"))
        self.assertIsNone(self.geo.quartiere_of("guado_di_pietre_piatte"))
        self.assertIsNone(self.geo.quartiere_of("piccole_isole_allorizzonte"))


class TestDistance(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.geo = IslandGeography()

    def test_distance_self_is_zero(self) -> None:
        self.assertEqual(self.geo.distance("albero_vecchio", "albero_vecchio"), 0)

    def test_distance_is_symmetric(self) -> None:
        pairs = [
            ("albero_vecchio", "forno_di_fiamma"),
            ("pontile_di_bartolo", "grotta_di_grunto"),
            ("casa_tana_di_rovo", "roccia_alta"),
        ]
        for a, b in pairs:
            with self.subTest(pair=(a, b)):
                d_ab = self.geo.distance(a, b)
                d_ba = self.geo.distance(b, a)
                self.assertAlmostEqual(d_ab, d_ba, places=6)

    def test_distance_positive_for_different_points(self) -> None:
        d = self.geo.distance("albero_vecchio", "forno_di_fiamma")
        self.assertGreater(d, 0)

    def test_elevation_accessor(self) -> None:
        self.assertEqual(self.geo.elevation("albero_vecchio"), 10)
        self.assertGreater(self.geo.elevation("montagne_gemelle"), 100)


class TestWalkingTime(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.geo = IslandGeography()

    def test_walking_time_scales_inversely_with_speed(self) -> None:
        # child_run 2.0 m/s, adult_walk 1.2 m/s → rapporto 2.0/1.2 = 5/3
        t_slow = self.geo.walking_time(
            "albero_vecchio", "forno_di_fiamma", speed="adult_walk"
        )
        t_fast = self.geo.walking_time(
            "albero_vecchio", "forno_di_fiamma", speed="child_run"
        )
        ratio = t_slow / t_fast
        expected = WALKING_SPEEDS_MPS["child_run"] / WALKING_SPEEDS_MPS["adult_walk"]
        self.assertAlmostEqual(ratio, expected, places=5)

    def test_walking_time_double_speed_halves_time(self) -> None:
        # adult_walk 1.2, bartolo_walk 0.4 → bartolo impiega 3x
        t_adult = self.geo.walking_time(
            "albero_vecchio", "pontile_di_bartolo", speed="adult_walk"
        )
        t_bartolo = self.geo.walking_time(
            "albero_vecchio", "pontile_di_bartolo", speed="bartolo_walk"
        )
        self.assertAlmostEqual(t_bartolo, t_adult * 3.0, places=5)

    def test_unknown_speed_preset_raises(self) -> None:
        with self.assertRaises(ValueError):
            self.geo.walking_time(
                "albero_vecchio", "forno_di_fiamma", speed="turbo"  # type: ignore[arg-type]
            )


class TestPath(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.geo = IslandGeography()

    def test_path_starts_and_ends_correctly(self) -> None:
        route = self.geo.path("orti_del_cerchio", "pontile_di_bartolo")
        self.assertEqual(route[0], "orti_del_cerchio")
        self.assertEqual(route[-1], "pontile_di_bartolo")

    def test_path_self_is_single_node(self) -> None:
        route = self.geo.path("albero_vecchio", "albero_vecchio")
        self.assertEqual(route, ["albero_vecchio"])

    def test_path_goes_via_center(self) -> None:
        # dai pontile agli orti il cammino più breve passa per il villaggio
        route = self.geo.path("pontile_di_bartolo", "orti_del_cerchio")
        self.assertIn("albero_vecchio", route)

    def test_path_distance_non_negative(self) -> None:
        d = self.geo.path_distance("albero_vecchio", "grotta_di_grunto")
        self.assertGreater(d, 0)


class TestNearby(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.geo = IslandGeography()

    def test_nearby_excludes_self(self) -> None:
        ids = self.geo.nearby("albero_vecchio", radius_m=500)
        self.assertNotIn("albero_vecchio", ids)

    def test_nearby_includes_obvious_neighbors(self) -> None:
        ids = self.geo.nearby("albero_vecchio", radius_m=200)
        # il pozzo e la panca di pietra sono a pochi metri
        self.assertIn("il_pozzo", ids)
        self.assertIn("panca_di_pietra", ids)

    def test_nearby_zero_radius_is_empty(self) -> None:
        ids = self.geo.nearby("albero_vecchio", radius_m=0)
        self.assertEqual(ids, [])

    def test_nearby_sorted_by_distance(self) -> None:
        ids = self.geo.nearby("albero_vecchio", radius_m=500)
        dists = [self.geo.distance("albero_vecchio", i) for i in ids]
        self.assertEqual(dists, sorted(dists))


class TestVisibility(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.geo = IslandGeography()

    def test_high_vantage_sees_far(self) -> None:
        # Roccia Alta (y=250) vede tutta l'isola (bibbia §8.5)
        visible = self.geo.visible_from("roccia_alta")
        # include il villaggio e i punti bassi vicini
        self.assertIn("albero_vecchio", visible)

    def test_porta_socchiusa_not_visible(self) -> None:
        # isole/guado non emergono come "visibili" (porta socchiusa)
        visible = self.geo.visible_from("roccia_alta")
        self.assertNotIn("piccole_isole_allorizzonte", visible)
        self.assertNotIn("guado_di_pietre_piatte", visible)

    def test_low_point_does_not_see_mountain_peak(self) -> None:
        visible = self.geo.visible_from("pontile_di_bartolo")
        self.assertNotIn("montagne_gemelle", visible)


class TestSchemaValidation(unittest.TestCase):
    """Validazione stretta dei JSON sorgente."""

    def test_locations_schema(self) -> None:
        with (GEO_DIR / "locations.json").open(encoding="utf-8") as fh:
            doc = json.load(fh)
        self.assertIn("locations", doc)
        allowed_categorie = {
            "edificio", "sentiero", "paesaggio", "landmark",
            "soglia", "acqua", "offshore",
        }
        allowed_quartieri = {
            None, "centro", "forno", "pontile", "orti", "montagne",
        }
        bounds_half_w = 4000  # 8 km ampia est-ovest
        bounds_half_d = 3500  # 7 km profonda nord-sud
        seen_ids: set[str] = set()
        for loc in doc["locations"]:
            with self.subTest(loc=loc["id"]):
                # campi obbligatori
                for key in (
                    "id", "nome_canonico", "categoria", "quartiere",
                    "coords", "descrizione_breve", "fonti", "porta_socchiusa",
                ):
                    self.assertIn(key, loc)
                # id unici
                self.assertNotIn(loc["id"], seen_ids)
                seen_ids.add(loc["id"])
                # categoria ammessa
                self.assertIn(loc["categoria"], allowed_categorie)
                # quartiere ammesso
                self.assertIn(loc["quartiere"], allowed_quartieri)
                # coords
                c = loc["coords"]
                for axis in ("x", "z", "y"):
                    self.assertIn(axis, c)
                    self.assertIsInstance(c[axis], (int, float))
                # porta_socchiusa bool
                self.assertIsInstance(loc["porta_socchiusa"], bool)
                # bounds: se non porta_socchiusa deve essere dentro l'isola
                if not loc["porta_socchiusa"]:
                    self.assertLessEqual(abs(c["x"]), bounds_half_w)
                    self.assertLessEqual(abs(c["z"]), bounds_half_d)
                # fonti: almeno una, tutte stringhe
                self.assertGreaterEqual(len(loc["fonti"]), 1)
                for s in loc["fonti"]:
                    self.assertIsInstance(s, str)

    def test_paths_schema(self) -> None:
        with (GEO_DIR / "paths.json").open(encoding="utf-8") as fh:
            doc = json.load(fh)
        with (GEO_DIR / "locations.json").open(encoding="utf-8") as fh:
            loc_doc = json.load(fh)
        known_ids = {l["id"] for l in loc_doc["locations"]}
        known_routes = {r["id"] for r in doc.get("named_routes", [])}
        allowed_difficulty = {"easy", "steep", "sandy"}
        self.assertIn("edges", doc)
        self.assertGreaterEqual(len(doc["edges"]), 4)
        for e in doc["edges"]:
            with self.subTest(edge=(e.get("from"), e.get("to"))):
                self.assertIn(e["from"], known_ids)
                self.assertIn(e["to"], known_ids)
                self.assertNotEqual(e["from"], e["to"])
                self.assertGreater(e["distance_m"], 0)
                self.assertIn(e["difficulty"], allowed_difficulty)
                if e.get("via") is not None:
                    self.assertIn(e["via"], known_routes)

    def test_named_routes_cover_four_vie(self) -> None:
        with (GEO_DIR / "paths.json").open(encoding="utf-8") as fh:
            doc = json.load(fh)
        ids = {r["id"] for r in doc.get("named_routes", [])}
        self.assertEqual(
            ids,
            {"via_dellalba", "via_del_pontile", "via_degli_orti", "via_che_sale"},
        )


class TestCanonicalExpectations(unittest.TestCase):
    """Alcune property derivate dal canone narrativo (bibbia/glossario)."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.geo = IslandGeography()

    def test_grotta_is_high(self) -> None:
        # La grotta di Grunto è nel Burrone sulle Montagne Gemelle
        self.assertGreater(self.geo.elevation("grotta_di_grunto"), 100)

    def test_pontile_is_at_sea_level(self) -> None:
        self.assertLess(self.geo.elevation("pontile_di_bartolo"), 5)

    def test_bartolo_slower_than_child_run(self) -> None:
        t_b = self.geo.walking_time(
            "pontile_di_bartolo", "albero_vecchio", speed="bartolo_walk"
        )
        t_c = self.geo.walking_time(
            "pontile_di_bartolo", "albero_vecchio", speed="child_run"
        )
        self.assertGreater(t_b, t_c)


# =============================================================================
#  Tempi canonici (Bibbia §8.1 — atlante)
# =============================================================================


class TestCanonicalTimes(unittest.TestCase):
    """Verifica che i tempi Bibbia §8.1 siano rispettati a meno di 0.01 min."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.geo = IslandGeography()

    def test_forno_thirty_min_adult(self) -> None:
        t = self.geo.walking_time(
            "albero_vecchio", "forno_di_fiamma", speed="adult_walk"
        )
        self.assertAlmostEqual(t, 30.0, places=2)

    def test_pontile_forty_min_adult(self) -> None:
        t = self.geo.walking_time(
            "albero_vecchio", "pontile_di_bartolo", speed="adult_walk"
        )
        self.assertAlmostEqual(t, 40.0, places=2)

    def test_rovo_thirtyfive_min_adult(self) -> None:
        t = self.geo.walking_time(
            "albero_vecchio", "casa_tana_di_rovo", speed="adult_walk"
        )
        self.assertAlmostEqual(t, 35.0, places=2)

    def test_roccia_alta_two_hours_adult(self) -> None:
        # Bibbia §8.1: "Roccia Alta: 2 ore"
        t = self.geo.walking_time(
            "albero_vecchio", "roccia_alta", speed="adult_walk"
        )
        self.assertAlmostEqual(t, 120.0, places=2)

    def test_grotta_four_five_hours_adult(self) -> None:
        # Bibbia §8.1: "Grotta di Grunto: 4-5 ore (mezza giornata)" → midpoint 270
        t = self.geo.walking_time(
            "albero_vecchio", "grotta_di_grunto", speed="adult_walk"
        )
        self.assertAlmostEqual(t, 270.0, places=2)

    def test_child_walk_scaling(self) -> None:
        # child_walk 0.8 vs adult_walk 1.2 → rapporto 1.5
        t_adult = self.geo.walking_time(
            "albero_vecchio", "roccia_alta", speed="adult_walk"
        )
        t_child = self.geo.walking_time(
            "albero_vecchio", "roccia_alta", speed="child_walk"
        )
        self.assertAlmostEqual(t_child / t_adult, 1.5, places=5)

    def test_bartolo_walk_scaling(self) -> None:
        # bartolo 0.4 vs adult 1.2 → rapporto 3x
        t_adult = self.geo.walking_time(
            "albero_vecchio", "roccia_alta", speed="adult_walk"
        )
        t_bartolo = self.geo.walking_time(
            "albero_vecchio", "roccia_alta", speed="bartolo_walk"
        )
        self.assertAlmostEqual(t_bartolo / t_adult, 3.0, places=5)

    def test_child_run_scaling(self) -> None:
        # child_run 2.0 vs adult 1.2 → rapporto 0.6
        t_adult = self.geo.walking_time(
            "albero_vecchio", "roccia_alta", speed="adult_walk"
        )
        t_run = self.geo.walking_time(
            "albero_vecchio", "roccia_alta", speed="child_run"
        )
        self.assertAlmostEqual(t_run / t_adult, 0.6, places=5)

    def test_walking_time_symmetric(self) -> None:
        pairs = [
            ("albero_vecchio", "forno_di_fiamma"),
            ("albero_vecchio", "grotta_di_grunto"),
            ("pontile_di_bartolo", "casa_tana_di_rovo"),
            ("spiaggia_delle_conchiglie", "roccia_alta"),
        ]
        for a, b in pairs:
            for speed in ("adult_walk", "child_walk", "bartolo_walk", "child_run"):
                with self.subTest(pair=(a, b), speed=speed):
                    t_ab = self.geo.walking_time(a, b, speed=speed)  # type: ignore[arg-type]
                    t_ba = self.geo.walking_time(b, a, speed=speed)  # type: ignore[arg-type]
                    self.assertAlmostEqual(t_ab, t_ba, places=5)

    def test_walking_time_self_is_zero(self) -> None:
        for loc in ("albero_vecchio", "roccia_alta", "fiume_che_gira"):
            with self.subTest(loc=loc):
                self.assertEqual(
                    self.geo.walking_time(loc, loc, speed="adult_walk"), 0.0
                )

    def test_walking_time_unknown_id_raises(self) -> None:
        with self.assertRaises(KeyError):
            self.geo.walking_time(
                "non_esiste", "albero_vecchio", speed="adult_walk"
            )
        with self.assertRaises(KeyError):
            self.geo.walking_time(
                "albero_vecchio", "non_esiste", speed="adult_walk"
            )

    def test_mixed_path_sums_canonical_plus_mechanical(self) -> None:
        # albero_vecchio -> pontile -> capanna_di_bartolo
        # primo edge canonical 40 min, secondo edge mechanical 22 m easy.
        expected_mechanical = (22.0 / WALKING_SPEEDS_MPS["adult_walk"]) / 60.0
        expected = 40.0 + expected_mechanical
        t = self.geo.walking_time(
            "albero_vecchio", "capanna_di_bartolo", speed="adult_walk"
        )
        self.assertAlmostEqual(t, expected, places=4)

    def test_difficulty_multiplier_sandy_vs_easy(self) -> None:
        # Prendiamo due edges non canonical con distance_m simile
        # e difficulty diversa. Spiaggia→Amo (256m steep) vs
        # orti→salvia (250m easy). Confrontiamo il rapporto ~= 2.5.
        t_steep = self.geo.walking_time(
            "spiaggia_delle_conchiglie", "casa_di_amo", speed="adult_walk"
        )
        t_easy = self.geo.walking_time(
            "orti_del_cerchio", "casa_tana_di_salvia", speed="adult_walk"
        )
        ratio = (t_steep / 256.0) / (t_easy / 250.0)
        self.assertAlmostEqual(ratio, 2.5, places=3)

    def test_sandy_multiplier_applied(self) -> None:
        # pontile→spiaggia = 532m sandy, no canonical. Aspettato: *1.3
        expected = (532.0 / WALKING_SPEEDS_MPS["adult_walk"]) / 60.0 * 1.3
        t = self.geo.walking_time(
            "pontile_di_bartolo", "spiaggia_delle_conchiglie", speed="adult_walk"
        )
        self.assertAlmostEqual(t, expected, places=4)

    def test_difficulty_multipliers_table(self) -> None:
        self.assertEqual(DIFFICULTY_MULTIPLIER["easy"], 1.0)
        self.assertEqual(DIFFICULTY_MULTIPLIER["steep"], 2.5)
        self.assertEqual(DIFFICULTY_MULTIPLIER["sandy"], 1.3)


# =============================================================================
#  Integrità del grafo
# =============================================================================


class TestGraphIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.geo = IslandGeography()
        with (GEO_DIR / "paths.json").open(encoding="utf-8") as fh:
            cls.paths_doc = json.load(fh)
        with (GEO_DIR / "locations.json").open(encoding="utf-8") as fh:
            cls.loc_doc = json.load(fh)

    def test_all_non_porta_reachable_from_village(self) -> None:
        # Costruiamo il set dei nodi raggiungibili via BFS sulla adiacenza reale
        # (non via path() che ritorna un cammino virtuale [a,b] se i due
        # nodi non sono connessi — sarebbe un falso positivo).
        adj: dict[str, set[str]] = {}
        for e in self.paths_doc["edges"]:
            adj.setdefault(e["from"], set()).add(e["to"])
            adj.setdefault(e["to"], set()).add(e["from"])
        seen = {"albero_vecchio"}
        stack = ["albero_vecchio"]
        while stack:
            u = stack.pop()
            for v in adj.get(u, ()):
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        # Fiume e Guado sono connessi via la_bocca, raggiungibili attraverso
        # pontile → la_bocca → fiume → guado. Le uniche esclusioni
        # legittime sono le porte socchiuse esplicite e le offshore.
        for loc in self.geo.all_locations():
            if loc.porta_socchiusa:
                continue
            with self.subTest(loc=loc.id):
                self.assertIn(
                    loc.id,
                    seen,
                    f"{loc.id} non raggiungibile dal Villaggio via sentieri",
                )

    def test_no_self_loops(self) -> None:
        for e in self.paths_doc["edges"]:
            with self.subTest(edge=(e["from"], e["to"])):
                self.assertNotEqual(e["from"], e["to"])

    def test_every_edge_endpoint_is_known_location(self) -> None:
        known = {l["id"] for l in self.loc_doc["locations"]}
        for e in self.paths_doc["edges"]:
            with self.subTest(edge=(e["from"], e["to"])):
                self.assertIn(e["from"], known)
                self.assertIn(e["to"], known)

    def test_every_via_is_known_named_route(self) -> None:
        known = {r["id"] for r in self.paths_doc["named_routes"]}
        for e in self.paths_doc["edges"]:
            if e.get("via") is None:
                continue
            with self.subTest(edge=(e["from"], e["to"])):
                self.assertIn(e["via"], known)

    def test_every_named_route_has_at_least_one_edge(self) -> None:
        edge_vie = {e.get("via") for e in self.paths_doc["edges"] if e.get("via")}
        for r in self.paths_doc["named_routes"]:
            with self.subTest(route=r["id"]):
                self.assertIn(r["id"], edge_vie)

    def test_edge_distance_non_negative(self) -> None:
        for e in self.paths_doc["edges"]:
            with self.subTest(edge=(e["from"], e["to"])):
                self.assertGreaterEqual(e["distance_m"], 0)

    def test_canonical_time_positive_if_present(self) -> None:
        for e in self.paths_doc["edges"]:
            if "canonical_time_min" in e:
                with self.subTest(edge=(e["from"], e["to"])):
                    self.assertGreater(e["canonical_time_min"], 0)

    def test_path_dijkstra_deterministic(self) -> None:
        # Ripetuti due chiamate stesso risultato
        for _ in range(3):
            r1 = self.geo.path("pontile_di_bartolo", "grotta_di_grunto")
            r2 = self.geo.path("pontile_di_bartolo", "grotta_di_grunto")
            self.assertEqual(r1, r2)


# =============================================================================
#  Bounds coordinate
# =============================================================================


class TestCoordinateBounds(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.geo = IslandGeography()

    def test_non_porta_inside_box(self) -> None:
        # Bounds: 8km x 7km
        for loc in self.geo.all_locations():
            if loc.porta_socchiusa:
                continue
            with self.subTest(loc=loc.id):
                self.assertLessEqual(abs(loc.coords.x), 4000)
                self.assertLessEqual(abs(loc.coords.z), 3500)

    def test_elevation_in_plausible_range(self) -> None:
        for loc in self.geo.all_locations():
            with self.subTest(loc=loc.id):
                self.assertGreaterEqual(loc.coords.y, 0)
                self.assertLessEqual(loc.coords.y, 400 + 100)  # tolleranza cime

    def test_pontile_and_bocca_at_sea_level(self) -> None:
        self.assertLess(self.geo.elevation("pontile_di_bartolo"), 5)
        self.assertLess(self.geo.elevation("la_bocca"), 5)

    def test_grotta_and_roccia_alta_are_elevated(self) -> None:
        self.assertGreater(self.geo.elevation("roccia_alta"), 100)
        self.assertGreater(self.geo.elevation("grotta_di_grunto"), 100)


# =============================================================================
#  API edge cases
# =============================================================================


class TestApiEdgeCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.geo = IslandGeography()

    def test_distance_self_zero_for_all(self) -> None:
        for loc in self.geo.all_locations():
            with self.subTest(loc=loc.id):
                self.assertEqual(self.geo.distance(loc.id, loc.id), 0)

    def test_path_self_single_node(self) -> None:
        for loc_id in (
            "albero_vecchio",
            "grotta_di_grunto",
            "piccole_isole_allorizzonte",
        ):
            with self.subTest(loc=loc_id):
                self.assertEqual(self.geo.path(loc_id, loc_id), [loc_id])

    def test_nearby_zero_radius_empty(self) -> None:
        for loc_id in ("albero_vecchio", "pontile_di_bartolo", "orti_del_cerchio"):
            with self.subTest(loc=loc_id):
                self.assertEqual(self.geo.nearby(loc_id, radius_m=0), [])

    def test_quartiere_of_samples(self) -> None:
        samples = {
            "forno_di_fiamma": "forno",
            "grotta_di_grunto": "montagne",
            "casa_tana_di_rovo": "orti",
            "spiaggia_delle_conchiglie": "pontile",
            "albero_vecchio": "centro",
        }
        for loc, expected in samples.items():
            with self.subTest(loc=loc):
                self.assertEqual(self.geo.quartiere_of(loc), expected)

    def test_quartiere_of_unknown_raises(self) -> None:
        with self.assertRaises(KeyError):
            self.geo.quartiere_of("non_esiste")

    def test_path_unknown_raises(self) -> None:
        with self.assertRaises(KeyError):
            self.geo.path("albero_vecchio", "non_esiste")


if __name__ == "__main__":
    unittest.main()
