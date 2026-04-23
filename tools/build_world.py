#!/usr/bin/env python3
"""Entrypoint della pipeline deterministica: content/ -> world/.

Scope di questo round: SOLO personaggi (+ avatar). Locations, objects,
winds, groups, spirits sono fuori scope.

Principi:
- Determinismo totale: nessun timestamp, nessuna iterazione su set/dict
  senza sort esplicito, nessuna dipendenza da env/locale variabile.
- Nessuna label framework in world/ (no Δ/⇄/⟳, no Pattern A, no semi,
  no quote_tracker, no fragments_budget).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

# consenti l'import del package sibling quando si esegue come script
_REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO_ROOT / "tools"))

from parse import bibbia, glossario, graph  # noqa: E402
from render.card import render_card  # noqa: E402


# ---------------------------------------------------------------------------
# Mapping statici — deterministici, derivati dalla Bibbia §2/§4 e dal grafo.
# ---------------------------------------------------------------------------

# Tre fratelli (avatar)
AVATAR_IDS = ["gabriel", "elias", "noah"]

# Partizione per categoria — coerente con l'inventario concordato (18 totali).
CATEGORIA_BY_ID: dict[str, str] = {
    # primari
    "bartolo": "primari",
    "fiamma": "primari",
    "rovo": "primari",
    "stria": "primari",
    "memolo": "primari",
    # testimoni
    "grunto": "testimoni",
    # secondari
    "salvia": "secondari",
    "nodo": "secondari",
    "amo": "secondari",
    "zolla": "secondari",
    # cuccioli
    "pun": "cuccioli",
    "toba": "cuccioli",
    "bru": "cuccioli",
    "cardo": "cuccioli",
    "liu": "cuccioli",
}

# Specie leggibile per il lettore (il grafo usa snake_case, noi vogliamo
# italiano naturale).
SPECIE_LEGGIBILE: dict[str, str] = {
    "bartolo": "tartaruga di mare anziana",
    "fiamma": "volpe rossa",
    "rovo": "tasso",
    "stria": "airone cenerino",
    "memolo": "riccio",
    "grunto": "stambecco verde vecchio",
    "salvia": "lepre",
    "nodo": "picchio",
    "amo": "cormorano",
    "zolla": "scoiattolo grigio anziano",
    "pun": "riccino",
    "toba": "tartarughina",
    "bru": "tassino",
    "cardo": "lupacchiotto",
    "liu": "libellulina",
    "gabriel": "umano",
    "elias": "umano",
    "noah": "umano",
}

# Ruolo pubblico (mestiere/posizione nel mondo) — nessuna etichetta framework.
RUOLO_PUBBLICO: dict[str, str] = {
    "bartolo": "traghettatore",
    "fiamma": "fornaia",
    "rovo": "guardiano dei margini della Foresta",
    "stria": "maestra della scuola del villaggio",
    "memolo": "abitante del villaggio centrale",
    "grunto": "solitario delle Montagne",
    "salvia": "cura con le erbe",
    "nodo": "ripara e costruisce",
    "amo": "pesca",
    "zolla": "raccoglie il cibo che cresce",
    "pun": "cucciolo della scuola",
    "toba": "cucciola della scuola",
    "bru": "cucciolo della scuola",
    "cardo": "cucciolo della scuola",
    "liu": "cucciola della scuola",
    "gabriel": "fratello maggiore",
    "elias": "fratello medio",
    "noah": "fratello piccolo",
}

# Quartiere pubblico — mapping da graph.quadrant al valore enum accettato
# dallo schema. "centro_villaggio" → "centro". I cuccioli senza quadrant
# esplicito ereditano null (vanno a scuola al centro ma non vi abitano).
QUADRANT_TO_QUARTIERE: dict[str, str] = {
    "fuoco_est": "fuoco",
    "acqua_sud": "acqua",
    "terra_ovest": "terra",
    "aria_nord": "aria",
    "centro_villaggio": "centro",
}

# Residenza leggibile — più pulita del campo home_location del grafo
# (che è snake_case). Dove home_location manca (cuccioli), descriviamo
# la residenza in termini di parentela: "con Mèmolo", "con Bartolo", ecc.
RESIDENZA_LEGGIBILE: dict[str, str] = {
    "bartolo": "Pontile, presso la Bocca (Quartiere d'Acqua)",
    "fiamma": "Forno del villaggio (Quartiere di Fuoco)",
    "rovo": "Tana ai margini della Foresta (Quartiere di Terra)",
    "stria": "Casa stretta e alta vicino alla scuola (centro del villaggio)",
    "memolo": "Casetta tonda sulla piazza centrale",
    "grunto": "Grotta nel Burrone tra le Montagne Gemelle (Quartiere d'Aria)",
    "salvia": "Casa-tana all'inizio degli Orti del Cerchio (Quartiere di Terra)",
    "nodo": "Casetta-bottega nel villaggio centrale",
    "amo": "Casa sulla scogliera della Spiaggia delle Conchiglie (Quartiere d'Acqua)",
    "zolla": "Casa-tana ai margini degli Orti, sul confine col bosco (Quartiere di Terra)",
    "pun": "Con il padre Mèmolo, in piazza centrale",
    "toba": "Con il padre Bartolo, al Pontile",
    "bru": "Con lo zio Rovo, ai margini della Foresta",
    "cardo": "Nel villaggio (genitori non in scena)",
    "liu": "Vola dovunque sull'isola (genitori non in scena)",
    "gabriel": "Con i fratelli, sull'isola",
    "elias": "Con i fratelli, sull'isola",
    "noah": "Con i fratelli, sull'isola",
}

# Porte socchiuse — dettagli di mondo dichiarati nella Bibbia come
# "mai spiegati". Mantenuti come elenchi stabili.
PORTE_SOCCHIUSE: dict[str, list[str]] = {
    "grunto": ["origine della cicatrice sul fianco sinistro"],
    "rovo": ["perché Bru è affidato a Rovo"],
    "bru": ["chi sono i suoi genitori e perché vive con Rovo"],
    "cardo": ["dove sono i suoi genitori"],
    "liu": ["dove sono i suoi genitori"],
}

# Relazioni pubbliche — derivate dal grafo (related_to, familial_role
# episodico dove è relazione concreta) e dalla Bibbia (scuola di Stria,
# protegge Bru, ecc.). Usiamo tipi dallo schema: parentela, mentore,
# protegge, vicino, porta_socchiusa, appartenenza_gruppo.
RELAZIONI_PUBBLICHE: dict[str, list[dict[str, str]]] = {
    "memolo": [
        {"tipo": "parentela", "target_id": "char.cuccioli.pun", "nota": "padre"},
    ],
    "bartolo": [
        {"tipo": "parentela", "target_id": "char.cuccioli.toba", "nota": "padre"},
    ],
    "rovo": [
        {"tipo": "parentela", "target_id": "char.cuccioli.bru", "nota": "zio che lo cresce"},
        {"tipo": "porta_socchiusa", "target_id": "char.cuccioli.bru", "nota": "perché Bru vive con Rovo non è raccontato"},
    ],
    "stria": [
        {"tipo": "mentore", "target_id": "char.cuccioli.pun", "nota": "maestra"},
        {"tipo": "mentore", "target_id": "char.cuccioli.toba", "nota": "maestra"},
        {"tipo": "mentore", "target_id": "char.cuccioli.bru", "nota": "maestra"},
        {"tipo": "mentore", "target_id": "char.cuccioli.cardo", "nota": "maestra"},
        {"tipo": "mentore", "target_id": "char.cuccioli.liu", "nota": "maestra"},
    ],
    "pun": [
        {"tipo": "parentela", "target_id": "char.primari.memolo", "nota": "figlio"},
        {"tipo": "mentore", "target_id": "char.primari.stria", "nota": "alunno"},
    ],
    "toba": [
        {"tipo": "parentela", "target_id": "char.primari.bartolo", "nota": "figlia"},
        {"tipo": "mentore", "target_id": "char.primari.stria", "nota": "alunna"},
    ],
    "bru": [
        {"tipo": "parentela", "target_id": "char.primari.rovo", "nota": "nipote affidato"},
        {"tipo": "mentore", "target_id": "char.primari.stria", "nota": "alunno"},
    ],
    "cardo": [
        {"tipo": "mentore", "target_id": "char.primari.stria", "nota": "alunno"},
    ],
    "liu": [
        {"tipo": "mentore", "target_id": "char.primari.stria", "nota": "alunna (a modo suo)"},
    ],
    "gabriel": [
        {"tipo": "parentela", "target_id": "avatar.elias", "nota": "fratello medio"},
        {"tipo": "parentela", "target_id": "avatar.noah", "nota": "fratello piccolo"},
    ],
    "elias": [
        {"tipo": "parentela", "target_id": "avatar.gabriel", "nota": "fratello maggiore"},
        {"tipo": "parentela", "target_id": "avatar.noah", "nota": "fratello piccolo"},
    ],
    "noah": [
        {"tipo": "parentela", "target_id": "avatar.gabriel", "nota": "fratello maggiore"},
        {"tipo": "parentela", "target_id": "avatar.elias", "nota": "fratello medio"},
    ],
}


# ---------------------------------------------------------------------------
# Fallback/override per descrizione_breve e firma_visiva.
# Priorità: Bibbia (bibbia.parse_inhabitants) → Glossario (fallback) →
# stringa vuota (`""`). Per gli avatar e per alcuni personaggi in cui la
# Bibbia usa formulazioni che includerebbero paratesto indesiderato,
# dichiariamo qui stringhe stabili.
# ---------------------------------------------------------------------------

DESCRIZIONE_BREVE_OVERRIDE: dict[str, str] = {
    "gabriel": "Il fratello maggiore. Vede i pericoli, fa le domande giuste; quando decide è netto.",
    "elias": "Il fratello medio. È il ponte tra gli altri due: trova cosa fare insieme, risolve con azioni più che con parole.",
    "noah": "Il fratello piccolo. Rompe gli equilibri quando le cose sono bloccate, vede l'insetto e il sentiero nascosto.",
    "grunto": (
        "Stambecco anziano dal pelo verde, solitario delle Montagne. "
        "Vive nel Burrone tra le Montagne Gemelle, dove nessun altro sale."
    ),
}

FIRMA_VISIVA_OVERRIDE: dict[str, str] = {
    "gabriel": "Il più alto dei tre, capelli corti lisci; toni blu scuro e viola.",
    "elias": "Capelli ricci; toni arancione e giallo.",
    "noah": "Il più piccolo, capelli via di mezzo; toni verde chiaro e turchese.",
}


# ---------------------------------------------------------------------------
# Costruzione record
# ---------------------------------------------------------------------------


def _quartiere_for(gid: str, char_data: dict[str, Any]) -> Any:
    """Ritorna il valore quartiere pubblico oppure None."""
    quad = char_data.get("quadrant")
    if quad and quad in QUADRANT_TO_QUARTIERE:
        return QUADRANT_TO_QUARTIERE[quad]
    return None


def _sorted_relazioni(rels: list[dict[str, str]]) -> list[dict[str, str]]:
    """Ordina stabilmente le relazioni per (tipo, target_id)."""
    return sorted(rels, key=lambda r: (r.get("tipo", ""), r.get("target_id", "")))


def build_character_record(
    gid: str,
    char_data: dict[str, Any],
    bible_extract: dict[str, str],
    glossario_line: str | None,
) -> dict[str, Any]:
    """Costruisce il frontmatter pubblico per un personaggio."""
    categoria = CATEGORIA_BY_ID[gid]
    cid = f"char.{categoria}.{gid}"

    firma = FIRMA_VISIVA_OVERRIDE.get(gid) or bible_extract.get("firma_visiva", "")
    descr = DESCRIZIONE_BREVE_OVERRIDE.get(gid) or bible_extract.get(
        "descrizione_breve", ""
    )
    if not descr and glossario_line:
        descr = glossario_line

    record: dict[str, Any] = {
        "id": cid,
        "nome_canonico": _display_name(gid),
        "categoria": categoria,
        "specie": SPECIE_LEGGIBILE[gid],
        "ruolo": RUOLO_PUBBLICO[gid],
        "quartiere": _quartiere_for(gid, char_data),
        "residenza": RESIDENZA_LEGGIBILE[gid],
        "firma_visiva": _sanitize_public(firma),
        "descrizione_breve": _sanitize_public(descr),
        "relazioni": _sorted_relazioni(RELAZIONI_PUBBLICHE.get(gid, [])),
        "porte_socchiuse": sorted(PORTE_SOCCHIUSE.get(gid, [])),
        "fonti": [
            "content/docs/ISOLA_TRE_VENTI_BIBLE_v2.md",
            "content/grafo/story_graph_v0_3_0.json",
            "content/worldbuilding/GLOSSARIO_ISOLA.md",
        ],
    }
    return record


def build_avatar_record(
    gid: str,
    char_data: dict[str, Any],
    bible_extract: dict[str, str],
) -> dict[str, Any]:
    cid = f"avatar.{gid}"
    firma = FIRMA_VISIVA_OVERRIDE[gid]
    descr = DESCRIZIONE_BREVE_OVERRIDE[gid]
    record: dict[str, Any] = {
        "id": cid,
        "nome_canonico": _display_name(gid),
        "categoria": "avatar",
        "specie": SPECIE_LEGGIBILE[gid],
        "ruolo": RUOLO_PUBBLICO[gid],
        "quartiere": None,
        "residenza": RESIDENZA_LEGGIBILE[gid],
        "firma_visiva": _sanitize_public(firma),
        "descrizione_breve": _sanitize_public(descr),
        "relazioni": _sorted_relazioni(RELAZIONI_PUBBLICHE.get(gid, [])),
        "porte_socchiuse": sorted(PORTE_SOCCHIUSE.get(gid, [])),
        "fonti": [
            "content/docs/ISOLA_TRE_VENTI_BIBLE_v2.md",
            "content/grafo/story_graph_v0_3_0.json",
            "content/worldbuilding/GLOSSARIO_ISOLA.md",
        ],
    }
    return record


_DISPLAY_NAME: dict[str, str] = {
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


def _display_name(gid: str) -> str:
    return _DISPLAY_NAME[gid]


_FRAMEWORK_CHARS_RE = None  # lazy


def _sanitize_public(text: str) -> str:
    """Rimuove dal testo pubblico le label framework (Δ/⇄/⟳) e loro
    residui tipici ('Δ.', '(Δ)', '— Δ.').

    Usato sulle stringhe provenienti da sorgenti in cui il framework può
    comparire come sigla secca (Glossario riga cast).
    """
    import re as _re

    t = text
    # rimuovi sequenze del tipo "X." alla fine con X ∈ {Δ,⇄,⟳}
    t = _re.sub(r"\s*[—\-–]\s*[Δ⇄⟳]\s*\.\s*$", ".", t)
    t = _re.sub(r"\s*[Δ⇄⟳]\s*\.\s*$", "", t)
    t = _re.sub(r"[Δ⇄⟳]", "", t)
    # normalizza doppi spazi e spazi prima punto
    t = _re.sub(r"\s+\.", ".", t)
    t = _re.sub(r"\s+", " ", t)
    return t.strip()


def _body_for(record: dict[str, Any], glossario_line: str | None) -> str:
    """Prosa pubblica del corpo: descrizione_breve + firma_visiva in chiaro.
    Mantiene una struttura stabile, senza framework."""
    parts: list[str] = []
    if record.get("descrizione_breve"):
        parts.append(_sanitize_public(record["descrizione_breve"]))
    if record.get("firma_visiva"):
        parts.append(f"**Firma visiva.** {_sanitize_public(record['firma_visiva'])}")
    if glossario_line:
        parts.append(f"*Dal Glossario.* {_sanitize_public(glossario_line)}")
    return "\n\n".join(parts).strip() + "\n"


# ---------------------------------------------------------------------------
# Scrittura
# ---------------------------------------------------------------------------


def _write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # determinismo: scrivi sempre in binario con LF, senza BOM
    with path.open("wb") as fh:
        fh.write(content.encode("utf-8"))


def build(repo_root: Path) -> dict[str, Any]:
    g = graph.load_graph(repo_root)
    chars = graph.characters(g)

    bible_text = bibbia.load_bible_text(repo_root)
    bible_inhabitants = bibbia.parse_inhabitants(bible_text)
    bible_avatars = bibbia.parse_avatars(bible_text)

    glossario_text = glossario.load_glossario_text(repo_root)
    gloss_map = glossario.parse_glossario(glossario_text)
    firme_visive_fallback = glossario.parse_firme_visive(glossario_text)

    # integra: se la Bibbia non ha firma_visiva, usa quella del Glossario §6
    for gid, firma in firme_visive_fallback.items():
        rec = bible_inhabitants.setdefault(gid, {})
        rec.setdefault("firma_visiva", firma)

    # Rimuovi world/characters/ e world/avatars/ in modo ordinato
    # (ma preserva _schema e README).
    world_dir = repo_root / "world"
    for sub in ("characters", "avatars"):
        subdir = world_dir / sub
        if subdir.exists():
            for p in sorted(subdir.rglob("*"), reverse=True):
                if p.is_file():
                    p.unlink()
                elif p.is_dir():
                    p.rmdir()

    index: dict[str, list[dict[str, str]]] = {"characters": [], "avatars": []}

    # --- Personaggi ---
    for gid in sorted(CATEGORIA_BY_ID.keys()):
        if gid not in chars:
            raise RuntimeError(
                f"Personaggio '{gid}' non presente in entities.characters del grafo."
            )
        bible_extract = bible_inhabitants.get(gid, {})
        gloss_line = gloss_map.get(gid)
        record = build_character_record(gid, chars[gid], bible_extract, gloss_line)
        categoria = record["categoria"]
        body = _body_for(record, gloss_line)
        card = render_card(record, record["nome_canonico"], body)
        rel = Path("world") / "characters" / categoria / f"{gid}.md"
        _write_file(repo_root / rel, card)
        index["characters"].append(
            {
                "id": record["id"],
                "nome_canonico": record["nome_canonico"],
                "categoria": categoria,
                "path": rel.as_posix(),
            }
        )

    # --- Avatar ---
    for gid in AVATAR_IDS:
        if gid not in chars:
            raise RuntimeError(
                f"Avatar '{gid}' non presente in entities.characters del grafo."
            )
        bible_extract = bible_avatars.get(gid, {})
        gloss_line = gloss_map.get(gid)
        record = build_avatar_record(gid, chars[gid], bible_extract)
        body = _body_for(record, gloss_line)
        card = render_card(record, record["nome_canonico"], body)
        rel = Path("world") / "avatars" / f"{gid}.md"
        _write_file(repo_root / rel, card)
        index["avatars"].append(
            {
                "id": record["id"],
                "nome_canonico": record["nome_canonico"],
                "categoria": "avatar",
                "path": rel.as_posix(),
            }
        )

    # ordina index deterministicamente per id
    index["characters"].sort(key=lambda r: r["id"])
    index["avatars"].sort(key=lambda r: r["id"])

    index_doc = {
        "version": "1",
        "avatars": index["avatars"],
        "characters": index["characters"],
    }
    index_json = json.dumps(index_doc, sort_keys=True, indent=2, ensure_ascii=False)
    _write_file(repo_root / "world" / "_index.json", index_json + "\n")

    # README auto-rigenerato
    readme_text = (
        "# world/ — output generato\n"
        "\n"
        "I file in questa cartella sono generati da `tools/build_world.py`.\n"
        "**Non editare a mano.** Per modificare il mondo: aggiorna `content/` e rirun `make world`.\n"
        "\n"
        "- `avatars/` — schede dei tre fratelli (vessel lettori-bambini).\n"
        "- `characters/` — schede abitanti, divise per categoria (primari, testimoni, secondari, cuccioli).\n"
        "- `_schema/` — JSON Schema del frontmatter.\n"
        "- `_index.json` — indice flat per la web app.\n"
    )
    _write_file(repo_root / "world" / "README.md", readme_text)

    return {
        "characters": len(index["characters"]),
        "avatars": len(index["avatars"]),
    }


def main() -> int:
    stats = build(_REPO_ROOT)
    print(
        f"world/ generato: {stats['characters']} personaggi + "
        f"{stats['avatars']} avatar."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
