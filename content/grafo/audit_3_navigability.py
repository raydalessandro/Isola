#!/usr/bin/env python3
"""
Audit 3: NAVIGABILITÀ e simmetria tracking.
- Un seme bloomato ha una storia che lo registra in seeds_bloomed_here?
- Uno status 'maturing' ha un seeds_maturing_here che lo registra?
- Le quote_tracker sono coerenti con quello che dichiarano le storie?
- I debts_opened trovano destinazione nei debts_closed o nei semi bloomati?
"""
import json
from collections import defaultdict, Counter

with open('/home/claude/b3/story_graph_v0_3_0.json') as f:
    g = json.load(f)

print("="*75)
print("3. NAVIGABILITÀ & SIMMETRIA TRACKING")
print("="*75)

# --- A. Seed bloomed VS seeds_bloomed_here ---
print("\n--- A. Seed con status='bloomed' devono comparire in seeds_bloomed_here di qualche storia ---")
bloomed_seeds = {sid: s for sid, s in g['seeds'].items() if s.get('status') == 'bloomed'}
for sid, s in bloomed_seeds.items():
    bloomed_in = s.get('bloomed_in_story')
    if bloomed_in:
        story = g['stories'].get(bloomed_in, {})
        if sid in story.get('seeds_bloomed_here', []):
            print(f"  ✓ {sid} bloomed in {bloomed_in}, registrato nella storia")
        else:
            print(f"  ✗ {sid} bloomed in {bloomed_in} ma NON in story.seeds_bloomed_here")
    else:
        print(f"  ⚠ {sid} status=bloomed ma manca bloomed_in_story")

# --- B. Seed maturing ---
print("\n--- B. Seed con status='maturing' ---")
maturing_seeds = {sid: s for sid, s in g['seeds'].items() if s.get('status') == 'maturing'}
print(f"Totale: {len(maturing_seeds)}")
for sid, s in maturing_seeds.items():
    mat_list = s.get('maturing_in_stories', [])
    mat_stories = [m.get('story') if isinstance(m, dict) else m for m in mat_list]
    print(f"  {sid}")
    print(f"    maturato in storie: {mat_stories}")
    # verifico simmetria: ogni storia ha questo seme in seeds_maturing_here?
    for st in mat_stories:
        if st in g['stories']:
            if sid in g['stories'][st].get('seeds_maturing_here', []):
                print(f"      ✓ {st}.seeds_maturing_here lo contiene")
            else:
                print(f"      ✗ {st}.seeds_maturing_here NON lo contiene")

# --- C. Seed status — whitelist post-B3.0.5 ---
print("\n--- C. Seed status (whitelist: active/seminato/maturing/bloomed/closed) ---")
ALLOWED_STATUS = {"active", "seminato", "maturing", "bloomed", "closed"}
non_std = {sid: s for sid, s in g['seeds'].items() if s.get('status') not in ALLOWED_STATUS}
for sid, s in non_std.items():
    print(f"  ⚠ {sid} status='{s.get('status')}' — fuori whitelist")
if not non_std:
    print("  ✓ tutti gli status seme sono nella whitelist")

# --- D. Tipi seme — whitelist post-B3.0.5 ---
print("\n--- D. Seed type (whitelist estesa con 'luogo', senza 'frame_pattern_a') ---")
STANDARD = {"fisico", "gesto", "capacita", "relazionale", "ritmo", "spatial_echo", "pattern", "fenomeno", "paura", "frame", "luogo"}
non_std_types = defaultdict(list)
for sid, s in g['seeds'].items():
    t = s.get('type')
    if t not in STANDARD:
        non_std_types[t].append(sid)
for t, sids in non_std_types.items():
    print(f"  ⚠ tipo '{t}' usato in: {sids}")
if not non_std_types:
    print("  ✓ tutti i type seme sono nella whitelist")

# --- E. Coerenza quote_tracker ---
print("\n--- E. QUOTE TRACKER vs stato dichiarato nelle storie ---")
qt = g.get('quote_tracker', {})

# grunto_fragments_used vs somma di fragment_used nei nodi
grunto_frags_declared = qt.get('grunto_fragments_used', 0)
grunto_frags_actual = 0
for sid, s in g['stories'].items():
    for ch in s.get('characters_in_scene', []):
        if ch.get('id') == 'grunto' and ch.get('fragment_used'):
            grunto_frags_actual += 1
print(f"  grunto_fragments_used: qt={grunto_frags_declared} actual={grunto_frags_actual} {'✓' if grunto_frags_declared == grunto_frags_actual else '✗'}")

# fiamma_detti: somma
fiamma_detti_qt = sum(qt.get('fiamma_detti_per_storia', {}).values())
fiamma_detti_actual = 0
for sid, s in g['stories'].items():
    for ch in s.get('characters_in_scene', []):
        if ch.get('id') == 'fiamma' and ch.get('mode') == 'chiacchiera':
            fiamma_detti_actual += ch.get('detti_count', 0)
print(f"  fiamma_detti totali: qt={fiamma_detti_qt} actual={fiamma_detti_actual} {'✓' if fiamma_detti_qt == fiamma_detti_actual else '✗'}")

# night_scenes
night_qt = set(qt.get('night_scenes', []))
night_actual = set(sid for sid, s in g['stories'].items() if s.get('night_scene') is True)
print(f"  night_scenes: qt={sorted(night_qt)} actual={sorted(night_actual)} {'✓' if night_qt == night_actual else '✗'}")

# pattern_a_stories — nuova semantica post-B3.0.5:
# qt.pattern_a_stories contiene SOLO storie con pattern_a_active in {attivo, bloomed}
# Seminato e pre_eco vanno in tracker separati
pa_qt = set(qt.get('pattern_a_stories', []))
pa_actual = set()
pa_seminato_actual = set()
pa_pre_eco_actual = set()
for sid, s in g['stories'].items():
    pa = s.get('pattern_a_active')
    if pa in ('attivo', 'bloomed'):
        pa_actual.add(sid)
    elif pa == 'seminato':
        pa_seminato_actual.add(sid)
    elif pa == 'pre_eco':
        pa_pre_eco_actual.add(sid)
print(f"  pattern_a_stories (attivo/bloomed): qt={sorted(pa_qt)} actual={sorted(pa_actual)} {'✓' if pa_qt == pa_actual else '✗'}")

pa_sem_qt = set(qt.get('pattern_a_seminato_stories', []))
print(f"  pattern_a_seminato_stories: qt={sorted(pa_sem_qt)} actual={sorted(pa_seminato_actual)} {'✓' if pa_sem_qt == pa_seminato_actual else '✗'}")

pa_pe_qt = set(qt.get('pattern_a_pre_eco_stories', []))
print(f"  pattern_a_pre_eco_stories: qt={sorted(pa_pe_qt)} actual={sorted(pa_pre_eco_actual)} {'✓' if pa_pe_qt == pa_pre_eco_actual else '✗'}")

# --- F. DEBT TRACKING simmetria ---
print("\n--- F. DEBT TRACKING ---")
# Ogni debt_closed dovrebbe poter essere rintracciato a un debt_opened in una storia precedente.
# Ma i debt_opened sono liberi-testo, difficile matching automatico.
# Conto invece: debts_opened totali cumulativi vs debts_closed cumulativi (saldo narrativo)
total_opened = 0
total_closed = 0
for sid in sorted(g['stories'].keys()):
    s = g['stories'][sid]
    opened = len(s.get('debts_opened', []))
    closed = len(s.get('debts_closed', []))
    total_opened += opened
    total_closed += closed
    print(f"  {sid}: +{opened} aperti, -{closed} chiusi → saldo cumulativo aperti={total_opened-total_closed}")
print(f"  Totale: {total_opened} aperti, {total_closed} chiusi, saldo={total_opened - total_closed}")
print(f"  (Saldo alto è normale a metà saga — dovrebbe diminuire da S6 in poi)")

# --- G. CALLBACK registry ---
print("\n--- G. CALLBACK REGISTRY ---")
# callbacks è un dict dedicato nel grafo
cb_registry = g.get('callbacks', {})
cb_inline = []  # tutti i callback_id dichiarati dentro callbacks_made delle storie
for sid, s in g['stories'].items():
    for cb in s.get('callbacks_made', []):
        if cb.get('callback_id'):
            cb_inline.append((sid, cb['callback_id']))

print(f"  Registry g['callbacks']: {len(cb_registry)} voci")
print(f"  Callback inline nei nodi-storia: {len(cb_inline)}")
if len(cb_registry) == 0 and len(cb_inline) > 0:
    print(f"  ⚠ I callback vivono SOLO inline nei nodi-storia, il registry globale g['callbacks'] è vuoto.")
    print(f"  → Vuol dire che una query 'mostrami tutti i callback della saga' non funziona via registry,")
    print(f"     bisogna scansionare tutte le storie. Inefficienza o scelta di design?")
