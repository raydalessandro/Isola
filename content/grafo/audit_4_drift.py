#!/usr/bin/env python3
"""
Audit 4: DRIFT tra nodi prodotti in chat diverse.
Confronto struttura fine (sub-campi, forme dei valori) tra S1-S3 (chat blocco A da me)
e S4-S5 (chat blocco B con revisore esterno).
"""
import json

with open('/home/claude/b3/story_graph_v0_3_0.json') as f:
    g = json.load(f)

print("="*75)
print("4. DRIFT — confronto nodi S1-S3 (chat A) vs S4-S5 (chat B)")
print("="*75)

chat_a = ['s01', 's02', 's03']
chat_b = ['s04', 's05']

def node_shape(s):
    """Profilo strutturale di un nodo: campi + subcampi dei visual_anchors.scene_hooks"""
    shape = {
        'top_fields': sorted(s.keys()),
        'hook_fields': [],
        'char_in_scene_fields': [],
    }
    # hook fields
    for h in s.get('visual_anchors', {}).get('scene_hooks', []):
        shape['hook_fields'].append(sorted(h.keys()))
    # character_in_scene fields
    for ch in s.get('characters_in_scene', []):
        shape['char_in_scene_fields'].append(sorted(ch.keys()))
    return shape

# Campi top-level
a_fields = set()
for sid in chat_a:
    a_fields |= set(g['stories'][sid].keys())
b_fields = set()
for sid in chat_b:
    b_fields |= set(g['stories'][sid].keys())

new_in_b = b_fields - a_fields
removed_in_b = a_fields - b_fields

print("\n--- TOP-LEVEL FIELDS ---")
if new_in_b:
    print(f"  Nuovi campi introdotti in chat B (S4-S5): {sorted(new_in_b)}")
else:
    print("  ✓ Nessun nuovo campo top-level introdotto in chat B")
if removed_in_b:
    print(f"  Campi spariti in chat B: {sorted(removed_in_b)}")
else:
    print("  ✓ Nessun campo sparito")

# Hook fields — confronto tra S1-S3 e S4-S5
print("\n--- HOOK FIELDS (visual_anchors.scene_hooks) ---")
a_hook_fields = set()
for sid in chat_a:
    for h in g['stories'][sid].get('visual_anchors', {}).get('scene_hooks', []):
        a_hook_fields |= set(h.keys())
b_hook_fields = set()
for sid in chat_b:
    for h in g['stories'][sid].get('visual_anchors', {}).get('scene_hooks', []):
        b_hook_fields |= set(h.keys())

new_hook_in_b = b_hook_fields - a_hook_fields
removed_hook_in_b = a_hook_fields - b_hook_fields
print(f"  Chat A — campi hook: {sorted(a_hook_fields)}")
print(f"  Chat B — campi hook: {sorted(b_hook_fields)}")
print(f"  Nuovi campi hook introdotti in B: {sorted(new_hook_in_b)}")
print(f"  Campi hook spariti in B: {sorted(removed_hook_in_b)}")

# Character_in_scene fields
print("\n--- CHARACTERS_IN_SCENE FIELDS ---")
a_ch_fields = set()
for sid in chat_a:
    for ch in g['stories'][sid].get('characters_in_scene', []):
        a_ch_fields |= set(ch.keys())
b_ch_fields = set()
for sid in chat_b:
    for ch in g['stories'][sid].get('characters_in_scene', []):
        b_ch_fields |= set(ch.keys())
print(f"  Chat A: {sorted(a_ch_fields)}")
print(f"  Chat B: {sorted(b_ch_fields)}")
print(f"  Nuovi in B: {sorted(b_ch_fields - a_ch_fields)}")
print(f"  Spariti in B: {sorted(a_ch_fields - b_ch_fields)}")

# Seed fields
print("\n--- SEED FIELDS ---")
a_seed_fields = set()
for sid, s in g['seeds'].items():
    if s.get('origin_story') in chat_a:
        a_seed_fields |= set(s.keys())
b_seed_fields = set()
for sid, s in g['seeds'].items():
    if s.get('origin_story') in chat_b:
        b_seed_fields |= set(s.keys())
print(f"  Chat A — campi seme: {sorted(a_seed_fields)}")
print(f"  Chat B — campi seme: {sorted(b_seed_fields)}")
print(f"  Nuovi in B: {sorted(b_seed_fields - a_seed_fields)}")
print(f"  Spariti in B: {sorted(a_seed_fields - b_seed_fields)}")

# Callback fields
print("\n--- CALLBACK FIELDS (inline nei nodi) ---")
a_cb_fields = set()
for sid in chat_a:
    for cb in g['stories'][sid].get('callbacks_made', []):
        a_cb_fields |= set(cb.keys())
b_cb_fields = set()
for sid in chat_b:
    for cb in g['stories'][sid].get('callbacks_made', []):
        b_cb_fields |= set(cb.keys())
print(f"  Chat A: {sorted(a_cb_fields)}")
print(f"  Chat B: {sorted(b_cb_fields)}")
print(f"  Nuovi in B: {sorted(b_cb_fields - a_cb_fields)}")
print(f"  Spariti in B: {sorted(a_cb_fields - b_cb_fields)}")
