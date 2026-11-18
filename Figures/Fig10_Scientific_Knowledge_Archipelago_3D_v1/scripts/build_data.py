"""Build data.json for the 3D archipelago from the v37 figure inputs in this repository.

Reads, from ../Fig10_Scientific_Knowledge_Archipelago_v37/ (or the folder given as the first argument):
  inputs/fields.csv            11 fields: code, English name, display records, colour
  inputs/themes.csv            top-4 tertiary categories per field (44 theme peaks) with record counts
  inputs/selected_seas.csv     the 11 exact field combinations shown as shared seas
  data/field_memberships.csv   record -> field assignments (1,489 records with a field)
Writes data.json: fields, themes, every field pair with its co-membership count, every exact multi-field
combination, and the selected seas.
Usage: python build_data.py [v37_folder] [out=data.json]
"""
import csv, json, sys, itertools, collections
from pathlib import Path

src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2] / "Fig10_Scientific_Knowledge_Archipelago_v37"
out = sys.argv[2] if len(sys.argv) > 2 else "data.json"
rows = lambda p: list(csv.DictReader(open(src / p, encoding="utf-8")))
F = rows("inputs/fields.csv"); T = rows("inputs/themes.csv")
mem = collections.defaultdict(set)
for r in rows("data/field_memberships.csv"):
    mem[r["paper_id"]].add(r["field_code"])
pair = collections.Counter(p for s in mem.values() for p in itertools.combinations(sorted(s), 2))
exact = collections.Counter(tuple(sorted(s)) for s in mem.values() if len(s) >= 2)
d = dict(fields=[dict(code=r["field_code"], name=r["name_en"], n=int(r["display_records"]), color=r["color"]) for r in F],
         themes=[dict(field=t["field_code"], rank=int(t["rank"]), name=t["name_en"], n=int(t["all_records"])) for t in T],
         pairs=[dict(a=a, b=b, n=n) for (a, b), n in pair.most_common()],
         exact=[dict(fields=list(k), n=n) for k, n in exact.most_common()],
         seas=rows("inputs/selected_seas.csv"))
json.dump(d, open(out, "w"), indent=1)
print(out, len(d["fields"]), "fields,", len(d["themes"]), "themes,", len(d["pairs"]), "pairs,", len(d["exact"]), "exact combinations")
