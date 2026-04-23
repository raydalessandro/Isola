#!/usr/bin/env python3
"""
bootstrap_graph.py — crea story_graph.json iniziale con:
- schema metadata
- entità anagrafiche (characters, locations, objects, winds) popolate da file canonici Bible v2 + Glossario
- sezioni vuote per seeds, callbacks, stories

Eseguito UNA VOLTA all'inizio di B3.
Dopo, i nodi-storia si aggiungono via add_story_node.py.
"""

import json
from pathlib import Path
from datetime import date

# --- METADATA ---
graph = {
    "schema_version": "0.1",
    "graph_version": "0.1.0",
    "last_updated": str(date.today()),
    "phase": "B3",
    "description": (
        "Grafo narrativo saga Isola dei Tre Venti. "
        "Entità anagrafiche = costanti strutturali. "
        "Dettagli di scena nei nodi-storia (visual_anchors, characters_in_scene.role/mode). "
        "Layer 0 visivo/comportamentale da estrarre in B3.5 (post-S12)."
    ),

    # --- ENTITÀ ANAGRAFICHE ---
    "entities": {
        "characters": {
            # --- TRE FRATELLI ---
            "gabriel": {
                "species": "umano",
                "type": "protagonista",
                "attribute_ear": "delta",
                "age_band": "maggiore_dei_tre",
                "birth": "2021-10-28",
                "role_saga": "protagonista",
                "narrative_function": "vede i pericoli, fa domande giuste, decide",
                "voice_notes": "frasi piene, verbi riflessivi, 'forse'/'non so'; quando decide è netto",
                "fear_arc": {
                    "fear_id": "fratelli_crescono_diversi",
                    "first_emergence_planned": "s09",
                    "resolution_story": "s12",
                    "resolution_mode": "tenere"
                },
                "state_by_story": {}
            },
            "elias": {
                "species": "umano",
                "type": "protagonista",
                "attribute_ear": "connettere",
                "age_band": "medio",
                "birth": "2024-02-08",
                "role_saga": "protagonista",
                "narrative_function": "ponte tra gli altri due, risolve con azioni non parole",
                "voice_notes": "frasi che aprono ad altri ('Possiamo...', 'E se...'), cita altri, ricorda cose dette",
                "fear_arc": {
                    "fear_id": "non_essere_abbastanza",
                    "first_emergence_planned": "s02",
                    "resolution_story": "s11",
                    "resolution_mode": "accettare"
                },
                "state_by_story": {}
            },
            "noah": {
                "species": "umano",
                "type": "protagonista",
                "attribute_ear": "cambiare",
                "age_band": "piccolo",
                "birth": "2026-06-06",
                "role_saga": "protagonista",
                "narrative_function": "rompe equilibri, imprevisto, percezione sensoriale",
                "voice_notes": "frasi spezzate, esclamative, percezione fisica prima, ripete parole",
                "fear_arc": {
                    "fear_id": "buio",
                    "first_emergence_planned": "s01",
                    "resolution_story": "s10",
                    "resolution_mode": "dire"
                },
                "state_by_story": {}
            },

            # --- ABITANTI MAGGIORI ---
            "fiamma": {
                "species": "volpe_rossa",
                "type": "abitante_maggiore",
                "role_saga": "cammeo_ricorrente_cornice_s1_s12",
                "home_location": "forno",
                "quadrant": "fuoco_est",
                "narrative_function": "calore del villaggio",
                "voice_modes": ["chiacchiera", "ferma", "brace"],
                "constraints": [
                    "unica_detentrice_detti_popolari",
                    "detti_solo_in_modalita_chiacchiera",
                    "max_2_detti_per_storia",
                    "non_madre_default",
                    "mai_morale_in_corsivo",
                    "mai_sotto_albero_vecchio_solenne"
                ],
                "familial_role_episodic": "madre_episodica_sopratutto_per_noah"
            },
            "bartolo": {
                "species": "tartaruga_di_mare_anziana",
                "type": "abitante_maggiore",
                "role_saga": "dilatazione_del_tempo",
                "home_location": "pontile_bocca",
                "quadrant": "acqua_sud",
                "narrative_function": "abbassa il battito delle storie, traghettatore",
                "constraints": [
                    "mai_morale",
                    "mai_correre",
                    "mai_arrabbiato_visibile",
                    "mai_traghetta_abitanti_nominati_con_fratelli"
                ],
                "familial_role_episodic": "nonno"
            },
            "rovo": {
                "species": "tasso",
                "type": "abitante_maggiore",
                "role_saga": "resistenza_che_protegge",
                "home_location": "tana_margini_foresta",
                "quadrant": "terra_ovest",
                "narrative_function": "guardiano scontroso, fonte informazione data male",
                "constraints": [
                    "tenerezza_sempre_mediata",
                    "mai_confidenza_calorosa",
                    "mai_compagno_viaggio_prolungato_fratelli",
                    "mai_spiegare_perche_bru_con_lui"
                ],
                "familial_role_episodic": "zio_severo",
                "related_to": ["bru"]
            },
            "stria": {
                "species": "airone_cenerino",
                "type": "abitante_maggiore",
                "role_saga": "autorita_calma_scambio_asimmetrico",
                "home_location": "casa_stretta_alta_vicino_scuola",
                "quadrant": "centro_villaggio",
                "narrative_function": "maestra, memoria del villaggio",
                "constraints": [
                    "mai_lezione_morale_esplicita",
                    "mai_due_risposte_stessa_scena",
                    "mai_sopra_o_sotto_albero_vecchio",
                    "mai_commuovere_visibilmente"
                ],
                "familial_role_episodic": "maestra_zia"
            },
            "memolo": {
                "species": "riccio",
                "type": "abitante_maggiore",
                "role_saga": "cambio_di_registro_colpo_di_coda",
                "home_location": "casetta_tonda_piazza_centrale",
                "quadrant": "centro_villaggio",
                "narrative_function": "abbassa quando serio, dice intuizione precisa una volta a storia",
                "constraints": [
                    "mai_sapiente_confuso_didattico",
                    "mai_due_frasi_precise_stessa_storia",
                    "mai_risolve_trama_chiudendo"
                ],
                "familial_role_episodic": "zio_buffo",
                "related_to": ["pun"]
            },

            # --- FIGURA DI CONFRONTO ---
            "grunto": {
                "species": "stambecco_verde_vecchio",
                "type": "testimone_unico_pre_vento",
                "role_saga": "architrave_strato_3",
                "home_location": "grotta_burrone_montagne_gemelle",
                "quadrant": "aria_nord",
                "narrative_function": "ponte unico tra Epoca Mitica e Presente",
                "constraints": [
                    "no_nomi_propri_ariete_ondina_tempesta",
                    "mai_racconto_pieno_pre_vento",
                    "mai_nostalgia",
                    "mai_apertura_storia",
                    "mai_chiusura_storia",
                    "mai_preannunciare_rivelazione"
                ],
                "fragments_budget": {
                    "total_saga": 2,
                    "used": 0,
                    "planned_stories": ["s12"]
                },
                "familial_role_episodic": "ombra_dello_zio_misterioso"
            },

            # --- ABITANTI MINORI / MESTIERI ---
            "salvia": {
                "species": "lepre",
                "type": "abitante_minore_mestiere",
                "role_saga": "cura_concreta_che_educa",
                "home_location": "casa_tana_inizio_orti",
                "quadrant": "terra_ovest",
                "narrative_function": "cura con piante, micro-azione replicabile a casa",
                "constraints": [
                    "max_1_pianta_nominata_per_apparizione",
                    "mai_spiega_perche_pianta_funziona",
                    "mai_risolve_emotivamente"
                ],
                "familial_role_episodic": "madre_pratica"
            },
            "nodo": {
                "species": "picchio",
                "type": "abitante_minore_mestiere",
                "role_saga": "mano_che_fa",
                "home_location": "casetta_bottega_villaggio_centrale",
                "quadrant": "centro_villaggio",
                "narrative_function": "ripara, costruisce, insegna facendo",
                "signature_sound": "TOK-TOK-TOK",
                "constraints": [
                    "mai_spiega_perche_nodo_funziona",
                    "mai_fa_nodo_al_posto_di_chi_impara",
                    "mai_parla_di_sentimenti",
                    "tok_tok_tok_quota_4_5_storie_saga"
                ],
                "familial_role_episodic": "padre_pratico_zio_pratico"
            },
            "amo": {
                "species": "cormorano",
                "type": "abitante_minore_mestiere",
                "role_saga": "pazienza_acqua_silenzio_che_insegna",
                "home_location": "casa_scogliera_spiaggia_conchiglie",
                "quadrant": "acqua_sud",
                "narrative_function": "pesca, insegna col silenzio",
                "constraints": [
                    "mai_spiega_pesca_a_parole",
                    "mai_in_scene_villaggio_salvo_mercato",
                    "mai_nostalgico_o_malinconico",
                    "mai_conflitto_aperto"
                ],
                "familial_role_episodic": "zio_silenzioso"
            },
            "zolla": {
                "species": "scoiattolo_grigio_anziano",
                "type": "abitante_minore_mestiere",
                "role_saga": "stagione_e_parsimonia",
                "home_location": "casa_tana_margini_orti_bosco",
                "quadrant": "terra_ovest",
                "narrative_function": "raccoglie, conta in stagioni, educa al cibo che cresce",
                "constraints": [
                    "mai_lezioni_ecologia",
                    "mai_nostalgia_ambientalista",
                    "mai_scene_veloci_o_concitate"
                ],
                "familial_role_episodic": "nonno_pratico"
            },

            # --- CUCCIOLI SCUOLA STRIA ---
            "pun": {
                "species": "riccino",
                "type": "cucciolo_scuola",
                "role_saga": "memoria_pratica_intuizione_laterale",
                "related_to": ["memolo"],
                "constraints": ["mai_corregge_padre_con_tono_adulto", "mai_sapientello"]
            },
            "toba": {
                "species": "tartarughina",
                "type": "cucciolo_scuola",
                "role_saga": "domanda_che_apre",
                "related_to": ["bartolo"],
                "constraints": ["mai_domanda_filosofica", "mai_sola_al_pontile", "mai_corre"]
            },
            "bru": {
                "species": "tassino",
                "type": "cucciolo_scuola",
                "role_saga": "presenza_silenziosa_che_custodisce",
                "related_to": ["rovo"],
                "constraints": [
                    "mai_racconta_sua_storia",
                    "mai_centro_attenzione_in_gruppo",
                    "mai_piange_visibile",
                    "mai_eroe"
                ]
            },
            "cardo": {
                "species": "lupacchiotto",
                "type": "cucciolo_scuola",
                "role_saga": "frizione_necessaria",
                "constraints": [
                    "mai_modalita_predatore",
                    "mai_si_redime_visibile",
                    "mai_punito",
                    "mai_tradisce_davvero",
                    "punzecchia_max_2_3_storie_su_12"
                ]
            },
            "liu": {
                "species": "libellulina",
                "type": "cucciolo_scuola",
                "role_saga": "presenza_aerea_discreta",
                "constraints": []
            },

            # --- GRUPPI ISTITUZIONI ---
            "coltivatori_del_cerchio": {
                "type": "gruppo_istituzione",
                "home_location": "orti_del_cerchio",
                "quadrant": "terra_ovest",
                "signature_object": "zappa_col_manico_curvo",
                "signature_sound": "TUM-tum",
                "role_saga": "coralita_del_lavoro_agricolo"
            },
            "mercato_del_mezzogiorno": {
                "type": "gruppo_istituzione",
                "home_location": "piazza_centrale_villaggio",
                "quadrant": "centro_villaggio",
                "role_saga": "luogo_di_scambio_voci_e_cose",
                "note": "nessun oggetto simbolo — il Mercato è luogo",
                "sub_groups": {
                    "vecchie_del_mercato": {
                        "type": "sotto_gruppo_episodico",
                        "species": "umane",
                        "role_saga": "riconoscimento_muto_per_elias_s11",
                        "representation_constraint": (
                            "sono umane come i fratelli ma NON devono sembrare umane come personaggi — "
                            "funzionano come istituzione corale silente. "
                            "Mai trattate come vecchiette-personaggio individuali, "
                            "sempre come presenza di gruppo."
                        ),
                        "constraints": [
                            "mai_risolutrici_esplicite",
                            "cornice_non_agenti_per_paura_elias",
                            "mai_antropomorfizzate_come_vecchiette_personaggio",
                            "sempre_coralita_non_individualita"
                        ]
                    }
                }
            },
            "mantenitori": {
                "type": "gruppo_istituzione",
                "signature_object": "scala_a_pioli",
                "role_saga": "cura_delle_cose_del_villaggio"
            },
            "camminanti": {
                "type": "gruppo_istituzione",
                "signature_object": "carriola_di_vimini",
                "role_saga": "movimento_tra_quartieri"
            }
        },

        "winds": {
            "_shared": {
                "canonical_reference": "MITI_FONDATORI_BREVI_v1.md",
                "ontological_role": "spiriti_fondatori_ritirati_in_respiro_saga_presente",
                "when_asleep": {
                    "context": "scena_notturna",
                    "visual_constraint": "aria_ferma_fumo_dritto_foglie_immobili_capelli_fermi"
                },
                "scene_presence_rule": (
                    "i venti sono sempre presenti come ambiente secondo fascia oraria, "
                    "ma risaltano visivamente solo quando la scena lo richiede narrativamente "
                    "(es. Taglio che pulisce la nebbia in S1). "
                    "Non forzarli in ogni illustrazione."
                )
            },
            "vento_taglio": {
                "time_of_day": "alba",
                "direction": "da_est",
                "effect": "taglia_la_nebbia_rende_nitido",
                "origin_spirit": "ariete",
                "attribute_ear": "delta",
                "mirrors_brother": "gabriel",
                "visual_profile": {
                    "color_canonical": "giallo",
                    "manifestation": "luce_netta_che_taglia_nebbia_ombre_lunghe_definite_linee_dritte",
                    "when_visible": "linee_di_luce_gialla_tra_nebbia_o_in_controluce_alba",
                    "canonical_source": "mito_stampato_libro_0"
                }
            },
            "vento_intreccio": {
                "time_of_day": "giorno",
                "direction": "diffuso",
                "effect": "caldo_avvolgente_porta_odori_e_notizie",
                "origin_spirit": "ondina",
                "attribute_ear": "connettere",
                "mirrors_brother": "elias",
                "visual_profile": {
                    "color_canonical": "azzurro",
                    "manifestation": "movimento_caldo_diffuso_foglie_sospese_capelli_mossi_piu_direzioni",
                    "when_visible": "velature_azzurre_nell_aria_tra_rami_e_tra_case_odori_come_sfumature",
                    "canonical_source": "mito_stampato_libro_0"
                }
            },
            "vento_mulinello": {
                "time_of_day": "sera",
                "direction": "imprevedibile",
                "effect": "sposta_cose_cambia_direzione",
                "origin_spirit": "tempesta",
                "attribute_ear": "cambiare",
                "mirrors_brother": "noah",
                "visual_profile": {
                    "color_canonical": "viola",
                    "manifestation": "vortici_foglie_in_spirale_capelli_scompigliati_oggetti_che_si_muovono_imprevedibili",
                    "when_visible": "screziature_viola_nel_cielo_della_sera_o_nei_vortici_di_polvere_e_foglie",
                    "canonical_source": "mito_stampato_libro_0"
                }
            }
        },

        "locations": {
            # --- CENTRO ---
            "villaggio_centrale": {
                "type": "zona",
                "quadrant": "centro",
                "contains": ["albero_vecchio", "piazza_centrale", "casa_memolo", "bottega_nodo", "scuola_stria"],
                "role_saga": "centro_mandala_silenzioso"
            },
            "albero_vecchio": {
                "type": "landmark",
                "quadrant": "centro",
                "role_saga": "centro_mandala",
                "constraints": ["nessun_abitante_sotto_o_sopra_in_modo_solenne"]
            },

            # --- QUARTIERE FUOCO EST ---
            "forno": {
                "type": "edificio",
                "quadrant": "fuoco_est",
                "inhabitant": "fiamma",
                "features": ["camino_fuma_prima_alba", "cortile_legna_catastata_retro"],
                "role_saga": "cornice_s1_s12"
            },
            "case_del_mattino": {
                "type": "quartiere_parziale",
                "quadrant": "fuoco_est",
                "features": ["fabbro", "conceria", "essiccatoio_frutta_autunno"]
            },
            "via_dell_alba": {
                "type": "via",
                "quadrant": "fuoco_est"
            },

            # --- QUARTIERE ACQUA SUD ---
            "pontile_bocca": {
                "type": "struttura",
                "quadrant": "acqua_sud",
                "inhabitant": "bartolo",
                "features": ["assi_scure", "pali_nell_acqua", "capanna_in_cima"]
            },
            "bocca": {
                "type": "foce",
                "quadrant": "acqua_sud",
                "description": "foce del Fiume che Gira nel mare"
            },
            "spiaggia_conchiglie": {
                "type": "spiaggia",
                "quadrant": "acqua_sud",
                "position": "costa_mare_oltre_bocca"
            },
            "casa_amo": {
                "type": "casa",
                "quadrant": "acqua_sud",
                "inhabitant": "amo",
                "features": ["legno_scavato_roccia", "scaletta_pietra_fino_acqua"]
            },
            "case_basse_pescatori": {
                "type": "quartiere_parziale",
                "quadrant": "acqua_sud"
            },
            "via_del_pontile": {
                "type": "via",
                "quadrant": "acqua_sud"
            },

            # --- QUARTIERE TERRA OVEST ---
            "orti_del_cerchio": {
                "type": "zona_coltivata",
                "quadrant": "terra_ovest",
                "features": ["tre_fasce_concentriche"]
            },
            "foresta_intrecciata": {
                "type": "foresta",
                "quadrant": "terra_ovest",
                "features": ["tracce_non_sentieri", "radici_connesse_sotto_terra", "entrata_graduale"]
            },
            "tana_rovo": {
                "type": "tana",
                "quadrant": "terra_ovest",
                "inhabitant": "rovo",
                "features": ["sotto_ceppo_coperto_muschio", "tre_uscite"]
            },
            "casa_salvia": {
                "type": "casa_tana",
                "quadrant": "terra_ovest",
                "inhabitant": "salvia",
                "features": ["giardino_erbe_ordinate_per_file"]
            },
            "casa_zolla": {
                "type": "casa_tana",
                "quadrant": "terra_ovest",
                "inhabitant": "zolla",
                "features": ["tre_dispense"]
            },
            "via_degli_orti": {
                "type": "via",
                "quadrant": "terra_ovest"
            },

            # --- QUARTIERE ARIA NORD ---
            "pascoli_alti": {
                "type": "prato_in_pendenza",
                "quadrant": "aria_nord",
                "features": ["capre_pecore", "capanne_stagionali_pastori_estate"]
            },
            "roccia_alta": {
                "type": "sperone_panoramico",
                "quadrant": "aria_nord",
                "features": ["due_ore_cammino", "vista_tutta_isola"]
            },
            "montagne_gemelle": {
                "type": "rilievo",
                "quadrant": "aria_nord",
                "features": ["due_cime", "burrone_profondo_tra_loro"]
            },
            "burrone": {
                "type": "gola",
                "quadrant": "aria_nord",
                "position": "tra_montagne_gemelle"
            },
            "grotta_grunto": {
                "type": "grotta",
                "quadrant": "aria_nord",
                "inhabitant": "grunto",
                "position": "cengia_burrone"
            },
            "via_che_sale": {
                "type": "via",
                "quadrant": "aria_nord"
            },

            # --- PERIMETRO ---
            "fiume_che_gira": {
                "type": "fiume_anello",
                "position": "perimetro_terra_interna",
                "features": ["sorgente_montagne", "foce_bocca_sud", "anello_quasi_chiuso"]
            },
            "fascia_costiera": {
                "type": "fascia",
                "features": ["tra_fiume_e_mare", "larga_500_800m"]
            }
        },

        "objects": {
            "pagnotta_forno": {
                "category": "oggetto_ricorrente",
                "origin_location": "forno",
                "saga_role": "cornice_s1_s12"
            },
            "braccialetto_s9": {
                "category": "oggetto_significativo_nascosto",
                "origin_story": "s09",
                "description_constraint": "mai_descritto_dopo_s09",
                "appears_in_stories_planned": ["s09", "s12"]
            },
            "grembiule_fiamma": {
                "category": "firma_visiva_personaggio",
                "owner": "fiamma",
                "description": "tela ruvida color terracotta sempre infarinato"
            },
            "bandana_rovo": {
                "category": "firma_visiva_personaggio",
                "owner": "rovo",
                "description": "scura marrone-grigio legata sulla fronte"
            },
            "scialle_stria": {
                "category": "firma_visiva_personaggio",
                "owner": "stria",
                "description": "color cenere chiaro sulle spalle, lungo le ali"
            },
            "sciarpa_memolo": {
                "category": "firma_visiva_personaggio",
                "owner": "memolo",
                "description": "annodata male sul collo, sistemata di continuo"
            },
            "cesto_salvia": {
                "category": "firma_visiva_personaggio",
                "owner": "salvia",
                "description": "tracolla vimini sottile piccolo con erbe"
            },
            "corda_nodo": {
                "category": "firma_visiva_personaggio",
                "owner": "nodo",
                "description": "arrotolata sul braccio, sempre, spessore variabile"
            },
            "conchiglia_amo": {
                "category": "firma_visiva_personaggio",
                "owner": "amo",
                "description": "collana una sola conchiglia conica scura"
            },
            "bisaccia_zolla": {
                "category": "firma_visiva_personaggio",
                "owner": "zolla",
                "description": "pelle morbida di traverso, sempre piena"
            },
            "cicatrice_grunto": {
                "category": "firma_visiva_personaggio",
                "owner": "grunto",
                "description": "lunga sul fianco sinistro, striscia senza pelo",
                "constraint": "mai_spiegata_mai_nominata_nel_testo"
            }
        },

        "visual_signatures": {
            "_note": "Firme visive di saga non legate ai venti. Questo blocco è aperto: nuove firme si aggiungono quando emergono durante la scrittura. I profili visivi dei Tre Venti sono in entities.winds, non qui.",
            "quando_acqua_trema": {
                "type": "firma_visiva_saga",
                "description": "immagine ricorrente legata al Pattern A",
                "constraint": "mai_dichiarata_nel_testo",
                "pattern_a_linked": True
            }
        }
    },

    # --- TRACKING GLOBALE ---
    "seeds": {},
    "callbacks": {},
    "stories": {},

    # --- QUOTE TRACKER GLOBALE ---
    "quote_tracker": {
        "fiamma_detti_per_storia": {},
        "grunto_fragments_used": 0,
        "grunto_fragments_planned_stories": ["s12"],
        "tok_tok_tok_stories": [],
        "night_scenes": [],
        "pattern_a_stories": [],
        "when_water_trembles_stories": [],
        "addresses_to_reader": [],
        "narrator_signature_phrases": []
    },

    # --- VINCOLI GLOBALI ATTIVI ---
    "active_constraints_global": [
        "ear_framework_invisible",
        "no_explicit_morals",
        "grunto_max_2_fragments_saga",
        "fiamma_detti_max_2_per_story",
        "night_not_personified",
        "no_narrator_reveal_preannouncement",
        "pattern_a_never_named_in_text",
        "fears_resolved_by_brothers_only",
        "s1_s12_frame_at_forno"
    ]
}

# --- SCRITTURA ---
output_path = Path("/home/claude/b3/story_graph.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(graph, f, ensure_ascii=False, indent=2)

print(f"Bootstrap completato: {output_path}")
print(f"File size: {output_path.stat().st_size} bytes")
print(f"Entities: {len(graph['entities']['characters'])} characters, {len(graph['entities']['locations'])} locations, {len(graph['entities']['objects'])} objects")
