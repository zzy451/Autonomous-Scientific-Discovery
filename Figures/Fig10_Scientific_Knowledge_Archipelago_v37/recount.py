"""Verify every displayed count against the bundled deduplicated label snapshot."""
from pathlib import Path
import collections
import csv
import json

ROOT=Path(__file__).resolve().parent


def table(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))


def audit_inputs(root=ROOT):
    population=table(root/'data/population.csv')
    ids={r['paper_id'] for r in population}
    assert len(ids)==len(population)==1492,'Unexpected population'
    research={r['paper_id'] for r in population if r['primary_record_type']=='research_paper'}
    assert len(research)==1114
    fields=table(root/'inputs/fields.csv');themes=table(root/'inputs/themes.csv');seas=table(root/'inputs/selected_seas.csv')
    assert len(fields)==11 and len(themes)==44 and len(seas)==11
    valid_fields={r['field_code'] for r in fields}
    per_record=collections.defaultdict(set)
    field_pairs=table(root/'data/field_memberships.csv')
    assert len(field_pairs)==len({(r['paper_id'],r['field_code']) for r in field_pairs})==1981
    for r in field_pairs:
        assert r['paper_id'] in ids and r['field_code'] in valid_fields
        per_record[r['paper_id']].add(r['field_code'])
    field_counts=collections.Counter(f for fs in per_record.values() for f in fs)
    for r in fields:assert field_counts[r['field_code']]==int(r['display_records']),(r,field_counts)
    vocab={r['tertiary_code']:r for r in table(root/'data/tertiary_vocabulary.csv')}
    assert len(vocab)==350
    class_ids=collections.defaultdict(set)
    tertiary_pairs=table(root/'data/tertiary_memberships.csv')
    assert len(tertiary_pairs)==len({(r['paper_id'],r['tertiary_code']) for r in tertiary_pairs})==2073
    for r in tertiary_pairs:
        p,c=r['paper_id'],r['tertiary_code']
        assert p in ids and c in vocab and c[:2] in per_record[p]
        class_ids[c].add(p)
    for field in sorted(valid_fields):
        ranked=sorted([c for c in vocab if c[:2]==field],key=lambda c:(-len(class_ids[c]),-len(class_ids[c]&research),c))[:4]
        picked=sorted([r for r in themes if r['field_code']==field],key=lambda r:int(r['rank']))
        assert [r['tertiary_code'] for r in picked]==ranked,(field,ranked,picked)
        for r in picked:
            c=r['tertiary_code']
            assert len(class_ids[c])==int(r['all_records'])
            assert len(class_ids[c]&research)==int(r['research_papers'])
            assert r['name_zh']==vocab[c]['name_zh']
    exact_combinations=collections.Counter(tuple(sorted(fs)) for fs in per_record.values())
    for r in seas:
        combo=tuple(sorted(r['members'].split(';')))
        assert len(combo) in [2,3] and exact_combinations[combo]==int(r['records']),(r,exact_combinations[combo])
    return dict(population=1492,research_papers=1114,other_records=378,formal_domain_records=len(per_record),field_memberships=1981,tertiary_memberships=2073,displayed_fields=11,displayed_tertiary_classes=44,verified_exact_shared_seas=11,all_displayed_counts_match=True,top4_ranking_matches=True)


if __name__=='__main__':print(json.dumps(audit_inputs(),indent=2))
