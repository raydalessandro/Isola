#!/usr/bin/env python3
"""
Audit tecnico del grafo narrativo.
Verifica:
1. Integrità referenziale (tutti gli ID citati esistono)
2. Coerenza schema (stessi campi, stessi tipi, stessi pattern di nomenclatura)
3. Navigabilità (si può camminare seed→story→callback→entity senza buchi)
4. Simmetria (debts_opened hanno un closure path potenziale; seeds hanno bloom_target coerenti)
5. Drift (differenze strutturali tra nodi delle diverse chat)
"""

import json
from collections import defaultdict, Counter

with open('/home/claude/b3/story_graph_v0_3_0.json') as f:
    g = json.load(f)

# Raccolgo tutti gli ID esistenti per verificare referenze
all_char_ids = set(g['entities']['characters'].keys())
all_loc_ids = set(g['entities']['locations'].keys())
all_obj_ids = set(g['entities']['objects'].keys())
all_wind_ids = set(k for k in g['entities']['winds'].keys() if not k.startswith('_'))
all_story_ids = set(g['stories'].keys())
all_seed_ids = set(g['seeds'].keys())
all_callback_ids = set(g.get('callbacks', {}).keys())

# sub_groups dentro characters (es. vecchie_del_mercato)
all_subgroup_ids = set()
for cid, c in g['entities']['characters'].items():
    for sgid in c.get('sub_groups', {}).keys():
        all_subgroup_ids.add(sgid)

issues = defaultdict(list)

print("="*75)
print("AUDIT TECNICO — story_graph_v0_3_0.json")
print("="*75)
print(f"\nID totali censiti:")
print(f"  characters: {len(all_char_ids)}")
print(f"  sub_groups: {len(all_subgroup_ids)} (dentro characters)")
print(f"  locations:  {len(all_loc_ids)}")
print(f"  objects:    {len(all_obj_ids)}")
print(f"  winds:      {len(all_wind_ids)}")
print(f"  stories:    {len(all_story_ids)}")
print(f"  seeds:      {len(all_seed_ids)}")
print(f"  callbacks:  {len(all_callback_ids)}")


# ================================================================
# 1. INTEGRITÀ REFERENZIALE — ID citati devono esistere
# ================================================================
print("\n" + "="*75)
print("1. INTEGRITÀ REFERENZIALE")
print("="*75)

for sid, s in g['stories'].items():
    # characters_in_scene
    for ch in s.get('characters_in_scene', []):
        cid = ch.get('id')
        if cid and cid not in all_char_ids and cid not in all_subgroup_ids:
            issues['char_ref_broken'].append(f"{sid}.characters_in_scene: {cid} non trovato")
    # characters offscreen
    for ch in s.get('characters_offscreen_or_background', []):
        cid = ch.get('id')
        if cid and cid not in all_char_ids and cid not in all_subgroup_ids:
            issues['char_ref_broken'].append(f"{sid}.offscreen: {cid} non trovato")
    # location primary
    loc_id = s.get('location_primary', {}).get('id')
    if loc_id and loc_id not in all_loc_ids:
        issues['loc_ref_broken'].append(f"{sid}.location_primary: {loc_id} non trovato")
    # locations secondary
    for loc in s.get('locations_secondary', []):
        lid = loc.get('id')
        if lid and lid not in all_loc_ids:
            issues['loc_ref_broken'].append(f"{sid}.location_secondary: {lid} non trovato")
    # wind_active
    w = s.get('wind_active')
    if w and w not in all_wind_ids:
        issues['wind_ref_broken'].append(f"{sid}.wind_active: {w} non trovato")
    # seeds_planted, seeds_picked_up, seeds_bloomed_here, seeds_maturing_here
    for field in ['seeds_planted', 'seeds_picked_up', 'seeds_bloomed_here', 'seeds_maturing_here']:
        for seed_id in s.get(field, []):
            if seed_id not in all_seed_ids:
                issues['seed_ref_broken'].append(f"{sid}.{field}: {seed_id} non trovato")
    # callbacks.from_story
    for cb in s.get('callbacks_made', []):
        from_s = cb.get('from_story')
        if from_s and from_s not in all_story_ids:
            issues['cb_story_ref_broken'].append(f"{sid}.callback {cb.get('callback_id')}: from_story={from_s} non esiste")

# Seeds: bloom_target_stories devono esistere
for seed_id, seed in g['seeds'].items():
    for target in seed.get('bloom_target_stories', []):
        if target not in all_story_ids and not target.startswith('s0') and not target.startswith('s1'):
            issues['seed_bloom_target_invalid'].append(f"{seed_id}: bloom_target={target} non è uno story ID valido")
    for mat in seed.get('maturing_planned_stories', []):
        if mat not in all_story_ids and not (mat.startswith('s0') or mat.startswith('s1')):
            issues['seed_maturing_target_invalid'].append(f"{seed_id}: maturing_planned={mat}")

for k, v in issues.items():
    print(f"\n[{k}] — {len(v)} issue:")
    for msg in v[:8]:
        print(f"  ✗ {msg}")
    if len(v) > 8:
        print(f"  ...e altri {len(v)-8}")

if not issues:
    print("\n  ✓ Tutti gli ID citati nei nodi-storia e nei semi esistono come entità.")
