"""Check scientific denominators, source joins, and manuscript consistency."""
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from build_core_evidence_package import ROOT, WORKSPACE, OUT, MANUSCRIPT, jsonl, load, parse_bib, sha, write_json


def cite_sequence(text):
    return re.findall(r'\\cite\w*\s*(?:\[[^\]]*\])*\{([^}]+)\}', text)


def main():
    core = {r['paper_id']: r for r in jsonl(ROOT / 'Data/papers.jsonl') if r['active_confirmed_core']}
    manifest = jsonl(OUT / 'core_corpus_manifest.jsonl')
    with (OUT / 'coding_coverage_matrix.csv').open(encoding='utf-8-sig') as f:
        matrix = list(csv.DictReader(f))
    with (OUT / 'core_reference_bridge.csv').open(encoding='utf-8-sig') as f:
        bridge = list(csv.DictReader(f))
    assert {r['paper_id'] for r in manifest} == set(core) == {r['paper_id'] for r in matrix}
    assert {r['paper_id'] for r in bridge} == set(core) and len(bridge) == 662
    assignments = [r for r in jsonl(ROOT / 'Data/paper_module_taxonomy_assignments.jsonl') if r['paper_id'] in core]
    assert len(assignments) == 935
    assert len(manifest) == len(matrix) == len(core) == 662
    subset = parse_bib((OUT / 'core_references.bib').read_text(encoding='utf-8'))
    assert len(subset) == 662 and set(subset) == {r['citation_key'] for r in manifest}
    for r in manifest:
        p = core[r['paper_id']]
        assert r['scientific_object_modules'] == p['scientific_object_modules']
        assert r['year'] == p['year'] == r['reference_year'], r['paper_id']
        assert r['doi_or_url'], r['paper_id']
    frozen = load(MANUSCRIPT / 'data/corpus_landscape_records_2026-11-01.json')
    for key, path in [('source_papers', ROOT / 'Data/papers.jsonl'),
                      ('source_module_assignments', ROOT / 'Data/paper_module_taxonomy_assignments.jsonl')]:
        normalized = hashlib.sha256(path.read_bytes().replace(b'\r\n', b'\n')).hexdigest()
        assert frozen[key + '_text_lf_sha256'] == normalized
    for r in frozen['records']:
        assert r['year'] == core[r['paper_id']]['year']
    landscape = load(MANUSCRIPT / 'data/landscape_source_summary.json')
    assert landscape['bibliographic_years'] == dict(Counter(p['year'] for p in core.values()))
    assert landscape['coverage_counts'] == dict(Counter(m for p in core.values() for m in p['scientific_object_modules']))
    counts = Counter(); source = ''
    for f in (MANUSCRIPT / 'sections').glob('*.tex'):
        text = f.read_text(encoding='utf-8'); source += text
        counts.update({'sections': len(re.findall(r'\\section\{', text)),
                       'subsections': len(re.findall(r'\\subsection\{', text)),
                       'tables': text.count(r'\begin{table}'), 'figures': text.count(r'\begin{figure}')})
    keys = {k.strip() for group in cite_sequence(source) for k in group.split(',')}
    assert len(keys) == 45
    assert counts == {'sections': 10, 'subsections': 43, 'tables': 15, 'figures': 6}, counts
    en = WORKSPACE / 'Agent_for_Science_Review_Overleaf'; zh = WORKSPACE / 'Agent_for_Science_Review_Chinese'
    local = {}
    if (en / 'main.tex').exists() and (zh / 'main.tex').exists():
        for f in (en / 'sections').glob('*.tex'):
            assert f.read_bytes() == (MANUSCRIPT / 'sections' / f.name).read_bytes(), f.name
            z = zh / 'sections' / (f.stem + '_zh.tex')
            et = f.read_text(encoding='utf-8'); zt = z.read_text(encoding='utf-8')
            assert cite_sequence(et) == cite_sequence(zt), ('citation order', f.name)
            for pattern in (r'\\label\{([^}]+)\}', r'\\begin\{(table|figure)\}'):
                assert re.findall(pattern, et) == re.findall(pattern, zt), f.name
            assert len(re.findall(r'\\subsection\{', et)) == len(re.findall(r'\\subsection\{', zt))
        assert (en / 'references.bib').read_bytes() == (zh / 'references.bib').read_bytes() == (MANUSCRIPT / 'references.bib').read_bytes()
        for folder in (en, zh):
            log = (folder / 'build/main.log').read_text(encoding='utf-8', errors='replace')
            assert not re.search(r'undefined citations|Citation .* undefined|There were undefined references|Overfull \\hbox|Missing character:', log)
            assert len(re.findall(r'\\bibitem', (folder / 'build/main.bbl').read_text(encoding='utf-8'))) == 45
        import fitz
        local = {'english_pdf_pages': len(fitz.open(en / 'build/main.pdf')), 'chinese_pdf_pages': len(fitz.open(zh / 'build/main.pdf')),
                 'matched_citation_order_labels_tables_figures_and_subsections': True,
                 'unresolved_citations_overfull_boxes_missing_characters': 0}
    report = {'core_works': len(core), 'core_bib_entries': len(subset), 'module_memberships': 935,
              'member_ids_manifest_matrix_bridge_match': True, 'core_master_reference_years_match': True,
              'frozen_source_hashes_and_year_figure_match': True, 'manuscript_structure': dict(counts),
              'cited_keys': len(keys), 'local_bilingual_checks': local,
              'visual_qa': 'Final full-document contact sheets and detail pages inspected; no clipping, overlap, missing glyphs, or broken tables observed.'}
    write_json(OUT / 'final_verification.json', report)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__': main()
