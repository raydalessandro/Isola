"""Estrae voci personaggi dal GLOSSARIO_ISOLA.md.

Il Glossario è una tabella secca di voci sintetiche. Lo usiamo come
arricchimento secondario: se la Bibbia non ha `firma_visiva` o
`descrizione_breve`, proviamo a ricavarli qui.
"""
from __future__ import annotations

import re
from pathlib import Path


GLOSSARIO_PATH = Path("content/worldbuilding/GLOSSARIO_ISOLA.md")

# id grafo → pattern nome nel glossario
_GLOSSARIO_NAME_BY_GRAPH_ID = {
    "bartolo": "Bartolo",
    "fiamma": "Fiamma",
    "rovo": "Rovo",
    "stria": "Stria",
    "memolo": "Mèmolo",
    "grunto": "Grunto",
    "salvia": "Salvia",
    "nodo": "Nodo",
    "amo": "Amo",
    "zolla": "Zolla",
    "pun": "Pun",
    "toba": "Toba",
    "bru": "Bru",
    "cardo": "Cardo",
    "liu": "Liù",
    "gabriel": "Gabriel",
    "elias": "Elias",
    "noah": "Noah",
}


def load_glossario_text(repo_root: Path) -> str:
    return (repo_root / GLOSSARIO_PATH).read_text(encoding="utf-8")


def parse_glossario(text: str) -> dict[str, str]:
    """Ritorna {graph_id: bullet_line} dove bullet_line è il testo del
    bullet '- **Nome** — testo' (prima occorrenza nel Glossario,
    tipicamente §3 cast)."""
    result: dict[str, str] = {}
    for gid, name in _GLOSSARIO_NAME_BY_GRAPH_ID.items():
        pattern = re.compile(
            r"^-\s+\*\*" + re.escape(name) + r"\*\*\s*[—-]\s*(.+?)$",
            re.MULTILINE,
        )
        m = pattern.search(text)
        if m:
            result[gid] = m.group(1).strip()
    return result


def _section_text(text: str, heading: str) -> str:
    """Ritorna il testo di una sezione identificata dall'heading esatto."""
    rx = re.compile(
        r"^" + re.escape(heading) + r"\s*$(.*?)(?=^#{1,6}\s|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = rx.search(text)
    return m.group(1) if m else ""


def parse_firme_visive(text: str) -> dict[str, str]:
    """Ritorna {graph_id: firma_visiva} estratto da §6.2 + §6.3.

    Serve soprattutto per i cuccioli, che nella Bibbia §4 non hanno un
    bullet '**Firma visiva:**' separato.
    """
    result: dict[str, str] = {}
    for section_heading in (
        "### §6.2 Firme visive personaggi nominati",
        "### §6.3 Firme visive cuccioli",
    ):
        sec = _section_text(text, section_heading)
        if not sec:
            continue
        for gid, name in _GLOSSARIO_NAME_BY_GRAPH_ID.items():
            pattern = re.compile(
                r"^-\s+\*\*" + re.escape(name) + r"\*\*\s*[—-]\s*(.+?)$",
                re.MULTILINE,
            )
            m = pattern.search(sec)
            if m:
                firma = m.group(1).strip()
                # ometti note parentetiche tipo "(porta socchiusa)"
                firma = re.sub(r"\s*\([^)]*porta socchiusa[^)]*\)\s*", "", firma)
                result[gid] = firma.strip().rstrip(".") + "."
    return result
