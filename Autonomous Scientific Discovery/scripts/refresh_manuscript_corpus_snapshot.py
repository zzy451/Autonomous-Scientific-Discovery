"""Refresh the current manuscript's years/hashes without changing its corpus.

Membership or taxonomy changes require a separate classification review. This
command intentionally rejects them instead of silently rewriting the baseline.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'Manuscript/data'


def main():
    papers = ROOT / 'Data/papers.jsonl'
    owner = ROOT / 'Data/paper_module_taxonomy_assignments.jsonl'
    path = DATA / 'corpus_landscape_records_2026-11-01.json'
    frozen = json.loads(path.read_text(encoding='utf-8'))
    core = [r for line in papers.read_text(encoding='utf-8').splitlines() if (r := json.loads(line))['active_confirmed_core']]
    old = {r['paper_id']: r for r in frozen['records']}
    assert len(core) == len(old) == 662
    assert {r['paper_id'] for r in core} == set(old)
    for r in core:
        assert r['scientific_object_modules'] == old[r['paper_id']]['scientific_object_modules']
    frozen['records'] = [{k: r[k] for k in ('paper_id', 'year', 'active_confirmed_core', 'scientific_object_modules')} for r in core]
    frozen['source_papers_sha256'] = hashlib.sha256(papers.read_bytes()).hexdigest()
    frozen['source_module_assignments_sha256'] = hashlib.sha256(owner.read_bytes()).hexdigest()
    # Git may convert text line endings across Windows and Unix checkouts.
    frozen['source_papers_text_lf_sha256'] = hashlib.sha256(papers.read_bytes().replace(b'\r\n', b'\n')).hexdigest()
    frozen['source_module_assignments_text_lf_sha256'] = hashlib.sha256(owner.read_bytes().replace(b'\r\n', b'\n')).hexdigest()
    frozen['snapshot_revision'] = 'auxiliary_tag_and_cited_version_alignment'
    path.write_text(json.dumps(frozen, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Refreshed 662 records; core identities and domain memberships unchanged.')


if __name__ == '__main__': main()
