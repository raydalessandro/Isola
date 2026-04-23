"""Estrae il cast §2-§4 dalla Bibbia (content/docs/ISOLA_TRE_VENTI_BIBLE_v2.md).

Per ogni abitante nominato con sezione ### §4.N NOME, colleziona:
- firma_visiva (dal bullet 'Firma visiva:' dentro il paragrafo 'Aspetto')
- descrizione_breve (le prime 1-2 frasi del paragrafo 'Specie, ruolo, residenza.')

Per i tre fratelli (§2.2, §2.3, §2.4), colleziona una descrizione pubblica
derivata dai campi Funzione narrativa / Voce (deliberatamente senza label
framework — il build emetterà solo la parte *in azione*, non 'Δ incarnato').
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any


BIBLE_PATH = Path("content/docs/ISOLA_TRE_VENTI_BIBLE_v2.md")

# id grafo → id nome nella Bibbia (heading §4.N)
# (gli heading sono in MAIUSCOLO)
_BIBLE_NAME_BY_GRAPH_ID = {
    "bartolo": "BARTOLO",
    "fiamma": "FIAMMA",
    "rovo": "ROVO",
    "stria": "STRIA",
    "memolo": "MÈMOLO",
    "grunto": "GRUNTO",
    "salvia": "SALVIA",
    "nodo": "NODO",
    "amo": "AMO",
    "zolla": "ZOLLA",
    "pun": "PUN",
    "toba": "TOBA",
    "bru": "BRU",
    "cardo": "CARDO",
    "liu": "LIÙ",
}


def load_bible_text(repo_root: Path) -> str:
    return (repo_root / BIBLE_PATH).read_text(encoding="utf-8")


def _split_sections(text: str) -> dict[str, str]:
    """Spezza il testo in blocchi ### §N.M NOME → testo fino alla successiva ###."""
    lines = text.splitlines()
    sections: dict[str, str] = {}
    current_key: str | None = None
    buf: list[str] = []
    heading_re = re.compile(r"^### §\d+\.\d+\s+(.+?)\s*$")
    for line in lines:
        m = heading_re.match(line)
        if m:
            if current_key is not None:
                sections[current_key] = "\n".join(buf).strip()
            current_key = m.group(1).strip()
            buf = []
        else:
            if current_key is not None:
                buf.append(line)
    if current_key is not None:
        sections[current_key] = "\n".join(buf).strip()
    return sections


def _first_sentences(paragraph: str, n: int = 2) -> str:
    """Prime n frasi (punto/esclamativo/interrogativo) di un paragrafo."""
    # rimuovi bold markdown
    p = re.sub(r"\*\*([^*]+)\*\*", r"\1", paragraph)
    p = p.strip()
    sentences = re.split(r"(?<=[.!?])\s+", p)
    chosen = sentences[:n]
    return " ".join(s.strip() for s in chosen).strip()


def _find_paragraph_starting_with(block: str, bold_label: str) -> str | None:
    """Ritorna il paragrafo che inizia con **label.** all'inizio riga."""
    pattern = re.compile(
        r"^\*\*" + re.escape(bold_label) + r"[^*]*\*\*\s*(.*?)(?=\n\n|\Z)",
        re.DOTALL | re.MULTILINE,
    )
    m = pattern.search(block)
    if not m:
        return None
    return m.group(1).strip()


def _extract_firma_visiva(aspetto: str) -> str | None:
    """Il paragrafo 'Aspetto' contiene '**Firma visiva:** testo ...'."""
    m = re.search(
        r"\*\*Firma visiva[^*]*\*\*\s*(.*?)(?:\n\n|\Z)",
        aspetto,
        re.DOTALL,
    )
    if not m:
        return None
    raw = m.group(1).strip()
    # prendi solo la prima frase (fino al primo punto)
    first = re.split(r"(?<=[.!?])\s+", raw)[0]
    return first.strip().rstrip(".") + "."


def parse_inhabitant(block: str) -> dict[str, str]:
    """Ritorna dict con 'descrizione_breve', 'firma_visiva' se trovati."""
    out: dict[str, str] = {}
    specie_par = _find_paragraph_starting_with(block, "Specie, ruolo, residenza.")
    if specie_par is None:
        # cuccioli Bibbia §4.13-§4.17 usano la forma corta
        specie_par = _find_paragraph_starting_with(block, "Specie, ruolo.")
    if specie_par:
        out["descrizione_breve"] = _first_sentences(specie_par, n=2)
    aspetto_par = _find_paragraph_starting_with(block, "Aspetto.")
    if aspetto_par:
        fv = _extract_firma_visiva(aspetto_par)
        if fv:
            out["firma_visiva"] = fv
    return out


def parse_inhabitants(text: str) -> dict[str, dict[str, str]]:
    """Ritorna {graph_id: {'descrizione_breve': ..., 'firma_visiva': ...}}."""
    sections = _split_sections(text)
    result: dict[str, dict[str, str]] = {}
    for graph_id, bible_name in _BIBLE_NAME_BY_GRAPH_ID.items():
        if bible_name in sections:
            result[graph_id] = parse_inhabitant(sections[bible_name])
    return result


# --- Avatar / tre fratelli ---

# Per i tre fratelli estraiamo dalla sezione §2.N una descrizione
# rigorosamente "di azione" senza label framework.
_AVATAR_BIBLE_HEADING = {
    "gabriel": re.compile(r"### §2\.2 Gabriel[^\n]*\n(.*?)(?=\n### |\Z)", re.DOTALL),
    "elias": re.compile(r"### §2\.3 Elias[^\n]*\n(.*?)(?=\n### |\Z)", re.DOTALL),
    "noah": re.compile(r"### §2\.4 Noah[^\n]*\n(.*?)(?=\n### |\Z)", re.DOTALL),
}


def _strip_framework_labels(text: str) -> str:
    """Rimuove token framework: Δ, ⇄, ⟳, 'Δ incarnato', 'tratto N', ecc."""
    t = text
    # rimuovi parentetiche tipo "(osserva, distingue, decide)" quando seguono un simbolo framework
    t = re.sub(r"\s*[ΔΔ⇄⟳][^.\n]*?(?:incarnato|in azione)[^.\n]*\.", "", t, flags=re.IGNORECASE)
    t = re.sub(r"\s*[ΔΔ⇄⟳][^.\n]*\.", "", t)
    t = re.sub(r"\s*[ΔΔ⇄⟳]\s*", " ", t)
    # rimuovi eventuali "(…EAR…)"
    t = re.sub(r"\s*\([^)]*EAR[^)]*\)", "", t, flags=re.IGNORECASE)
    # normalizza spazi
    t = re.sub(r"\s+", " ", t).strip()
    return t


def parse_avatars(text: str) -> dict[str, dict[str, str]]:
    """Ritorna {graph_id: {'descrizione_breve': ..., 'firma_visiva': ...}}.

    firma_visiva per i fratelli è un aspetto fisico (capelli/altezza) —
    estratto dalla prima riga descrittiva dopo l'heading.
    descrizione_breve è la Funzione narrativa, ripulita dalle label framework.
    """
    result: dict[str, dict[str, str]] = {}
    for aid, rx in _AVATAR_BIBLE_HEADING.items():
        m = rx.search(text)
        if not m:
            continue
        block = m.group(1).strip()
        # firma_visiva: prima riga (Nato ... capelli ...)
        first_line = block.splitlines()[0].strip()
        # es: "Nato 28 ottobre 2021. Scorpione (acqua fissa). Capelli corti lisci, il più alto."
        # prendi dopo "Capelli" se c'è
        m2 = re.search(r"(Capelli[^.]*\.)", first_line)
        if m2:
            result_fv = m2.group(1).strip()
        else:
            result_fv = first_line
        # descrizione_breve: paragrafo Funzione narrativa
        fn = _find_paragraph_starting_with(block, "Funzione narrativa:")
        if fn is None:
            fn = ""
        desc = _first_sentences(_strip_framework_labels(fn), n=2)
        # fallback: se vuoto, usa la prima frase del block
        if not desc:
            desc = _first_sentences(block, n=1)
        result[aid] = {
            "firma_visiva": result_fv,
            "descrizione_breve": desc,
        }
    return result
