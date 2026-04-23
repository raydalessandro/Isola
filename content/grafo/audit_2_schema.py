#!/usr/bin/env python3
"""
Audit 2: coerenza schema tra nodi-storia.
- Tutti i nodi hanno gli stessi campi obbligatori?
- Gli stessi campi hanno tipi coerenti tra storie?
- Il naming (snake_case, underscore vs trattino) è uniforme?
"""
import json
from collections import defaultdict, Counter

with open('/home/claude/b3/story_graph_v0_3_0.json') as f:
    g = json.load(f)

print("="*75)
print("2. COERENZA SCHEMA TRA NODI-STORIA")
print("="*75)

# Raccolgo set di campi per ogni storia
fields_per_story = {}
field_types_per_story = defaultdict(dict)

for sid, s in g['stories'].items():
    fields_per_story[sid] = set(s.keys())
    for k, v in s.items():
        field_types_per_story[k][sid] = type(v).__name__

# Campi presenti in ogni storia vs campi che variano
all_fields = set()
for fs in fields_per_story.values():
    all_fields |= fs

universal_fields = set.intersection(*fields_per_story.values())
variable_fields = all_fields - universal_fields

print(f"\nCampi totali visti nei nodi-storia: {len(all_fields)}")
print(f"Campi universali (presenti in tutte le 5 storie): {len(universal_fields)}")
print(f"Campi variabili (presenti solo in alcune): {len(variable_fields)}")

if variable_fields:
    print("\n--- CAMPI NON UNIFORMI TRA STORIE ---")
    for f in sorted(variable_fields):
        present_in = [sid for sid, fs in fields_per_story.items() if f in fs]
        print(f"  '{f}' → presente in: {sorted(present_in)}")

# Tipi inconsistenti per stesso campo
print("\n--- TIPI INCONSISTENTI (stesso campo, tipi diversi tra storie) ---")
type_issues = []
for field, types in field_types_per_story.items():
    unique_types = set(types.values())
    if len(unique_types) > 1:
        type_issues.append((field, types))
        print(f"  '{field}': {dict(types)}")
if not type_issues:
    print("  ✓ nessuna inconsistenza di tipo")

# Naming: underscore vs trattino nei valori stringa
print("\n--- NAMING CONVENTION (snake_case uniforme?) ---")
all_string_values = []
for sid, s in g['stories'].items():
    def collect_strings(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                collect_strings(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                collect_strings(v, f"{path}[{i}]")
        elif isinstance(obj, str):
            all_string_values.append((sid, path, obj))
    collect_strings(s, sid)

# Verifico: ci sono valori con trattino - dove dovrebbero essere snake_case?
dash_in_value = [v for v in all_string_values if '-' in v[2] and len(v[2]) < 60 and ' ' not in v[2] and not v[2].startswith('http') and not any(c.isupper() for c in v[2])]
# Escludo i veri nomi (Vento-Taglio, Montagne-Gemelle) e le frasi narrative
snake_violations = []
for v in dash_in_value:
    # Se contiene solo [a-z0-9_-] e ha un trattino, è sospetto
    if all(c.isalnum() or c in '_-' for c in v[2]) and '-' in v[2]:
        snake_violations.append(v)

if snake_violations:
    print(f"  ⚠ {len(snake_violations)} valori con trattino in posizioni tipo-ID (dovrebbero essere snake_case?):")
    for sid, path, val in snake_violations[:15]:
        print(f"    [{sid}] {path}: '{val}'")
else:
    print("  ✓ naming convention consistente")

# Verifico i seed IDs
print("\n--- NAMING SEED ID ---")
seed_patterns = Counter()
for seed_id in g['seeds']:
    if seed_id.startswith('seed_s0') or seed_id.startswith('seed_s1'):
        seed_patterns['seed_sNN_*'] += 1
    elif seed_id.startswith('seed_'):
        seed_patterns['seed_*'] += 1
    else:
        seed_patterns['altro'] += 1
for p, n in seed_patterns.most_common():
    print(f"  {p}: {n}")

# Story IDs: tutti sNN con zero padding?
print("\n--- NAMING STORY ID ---")
for sid in sorted(g['stories'].keys()):
    expected = len(sid) == 3 and sid.startswith('s') and sid[1:].isdigit()
    print(f"  '{sid}' → {'✓ conforme' if expected else '✗ non conforme'}")
