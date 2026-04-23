"""Carica il grafo narrativo di content/grafo/story_graph_v0_3_0.json.

Il grafo è la sorgente più strutturata: ID stabili, specie, quartiere, ruolo
saga, home_location. Bibbia e Glossario si usano solo per arricchire
firma_visiva e descrizione_breve.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


GRAPH_PATH = Path("content/grafo/story_graph_v0_3_0.json")


def load_graph(repo_root: Path) -> dict[str, Any]:
    """Carica e ritorna l'intero grafo come dict."""
    with (repo_root / GRAPH_PATH).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def characters(graph: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Ritorna il dict entities.characters."""
    return graph["entities"]["characters"]
