"""Apply the controller-reviewed, source-linked auxiliary-tag decisions once.

No inclusion, scientific-object assignment, or note/PDF path may be changed.
The accepted decision file is an audit artifact; master remains the owner.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from append_change_log import current_commit, load_rows, next_change_id
from manage_master_paper_list import parse_master_table, rebuild_master_file
from build_core_evidence_package import ROOT, OUT, FIELDS, vocabularies, write_json, sha

HEADER = dict(zip(FIELDS, ('Agent type', 'Research workflow role', 'Validation type', 'Scientific contribution type')))
HEADER.update({'year': 'Year', 'authors': 'Authors', 'source': 'Source', 'doi_or_url': 'DOI / arXiv / URL'})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    decisions = json.loads((OUT / 'accepted_decisions.json').read_text(encoding='utf-8'))
    lines, start, rows = parse_master_table(); byid = {r['ID']: r for r in rows}
    vocab = vocabularies(); changes = []; logs = load_rows(); initial_logs = len(logs)
    before = sha(ROOT / 'Paper_Lists/agent_master_paper_list.md')
    commit = current_commit()
    for record in decisions['records']:
        pid = record['paper_id']; row = byid[pid]; applied = []
        assert row['Inclusion status'] in ('to_read', 'included'), pid
        for change in record['changes']:
            field = change['field']; assert field in HEADER, field
            column = HEADER[field]; value = change['new_value']
            if field in FIELDS:
                assert isinstance(value, list) and value and len(set(value)) == len(value)
                assert all(v in vocab[field] for v in value), (pid, field, value)
                value = '; '.join(value)
            value = str(value)
            assert '|' not in value and '\n' not in value
            if row[column] == value: continue
            if 'expected_old_raw' in change:
                assert row[column] == change['expected_old_raw'], (pid, column, 'concurrent owner drift')
            evidence_path = ROOT / change['evidence_path']
            assert evidence_path.is_file(), evidence_path
            applied.append({**change, 'old_raw': row[column], 'new_raw': value})
            row[column] = value
        if applied:
            old = {HEADER[c['field']]: c['old_raw'] for c in applied}
            new = {HEADER[c['field']]: c['new_raw'] for c in applied}
            logs.append({'change_id': next_change_id(logs), 'paper_id': pid, 'changed_at': '2026-11-01',
                         'changed_by': 'codex', 'change_type': 'master_owner_update',
                         'old_value': old, 'new_value': new,
                         'reason': '沿用既有schema，对齐已审阅的笔记副标签或指定引用版本元数据；不改变核心成员与学科分类。',
                         'related_commit': commit, 'evidence': applied})
            changes.append({'paper_id': pid, 'changes': applied})
    print(json.dumps({'apply': args.apply, 'works_changed': len(changes), 'fields_changed': sum(len(r['changes']) for r in changes)}, ensure_ascii=False))
    if args.apply and changes:
        (ROOT / 'Paper_Lists/agent_master_paper_list.md').write_text(rebuild_master_file(lines, start, rows), encoding='utf-8')
        with (ROOT / 'Data/change_log.jsonl').open('a', encoding='utf-8') as f:
            for row in logs[initial_logs:]: f.write(json.dumps(row, ensure_ascii=False) + '\n')
        write_json(OUT / 'applied_changes.json', {'before_master_sha256': before,
            'after_master_sha256': sha(ROOT / 'Paper_Lists/agent_master_paper_list.md'),
            'records': changes, 'independent_primary_source_reaudit_of_all_tags': False})


if __name__ == '__main__': main()
