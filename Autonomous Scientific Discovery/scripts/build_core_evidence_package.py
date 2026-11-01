"""Rebuild the dated core manifest and coding inventory from existing owners.

This inventory measures recorded information, not the scientific truth of tags.
It never changes owners and never infers an unrecorded capability from a title.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
OUT = ROOT / 'Coverage_Check/core_tag_alignment_2026-11-01'
MANUSCRIPT = ROOT / 'Manuscript'
FIELDS = ('agent_type', 'research_workflow_role', 'validation_type', 'scientific_contribution_type')
SCHEMA = ROOT / 'paper_note_templates_and_prompts/ASD_annotation_schema.md'
NOTE_LABELS = {
    'agent_type': 'Agent 类型', 'research_workflow_role': '科研流程角色',
    'autonomy': '自主能力', 'validation_type': '验证方式',
    'cross_attributes': '交叉属性', 'scientific_contribution_type': '科学贡献类型',
}
ROLE_GROUPS = {
    'knowledge': ['literature_search_and_reading', 'knowledge_extraction_and_organization'],
    'hypothesis': ['scientific_question_formulation', 'hypothesis_generation'],
    'design': ['experimental_design'],
    'execution': ['simulation_modeling', 'tool_use_and_code_execution', 'experiment_execution'],
    'analysis': ['data_analysis', 'result_interpretation'],
    'validation_and_communication': ['evidence_assessment_and_validation', 'paper_writing'],
}


def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8-sig').splitlines() if line.strip()]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def write_csv(path, rows):
    assert rows
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        for row in rows:
            w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in row.items()})


def vocabularies():
    # Read the established controlled lists, rather than maintaining another schema.
    text = SCHEMA.read_text(encoding='utf-8')
    sections = re.split(r'(?m)^## ', text)
    result = {}
    section_for = {'agent_type': 4, 'research_workflow_role': 5, 'autonomy': 6,
                   'validation_type': 7, 'cross_attributes': 8, 'scientific_contribution_type': 9}
    for field, number in section_for.items():
        section = next(s for s in sections if re.match(fr'{number}[.\s]', s))
        result[field] = re.findall(r'(?m)^- `([^`]+)`', section)
        assert result[field], field
    return result


def parse_bib(text):
    # Bib entries in this project use balanced brace values; keep the original
    # entry bytes in the subset so accents and the audited metadata are retained.
    entries = {}
    matches = list(re.finditer(r'(?m)^@(\w+)\{([^,\n]+),', text))
    for i, match in enumerate(matches):
        raw = text[match.start():matches[i+1].start() if i+1 < len(matches) else len(text)].strip()
        values = {}
        for m in re.finditer(r'(?m)^\s*(\w+)\s*=\s*\{', raw):
            start = m.end(); pos = start; depth = 1
            while depth:
                if raw[pos] == '\\': pos += 2; continue
                depth += (raw[pos] == '{') - (raw[pos] == '}'); pos += 1
            values[m[1]] = raw[start:pos-1]
        entries[match[2]] = (raw, values)
    return entries


def note_summary(path):
    if not path.is_file(): return {}
    result = {}
    for line_no, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
        for field, label in NOTE_LABELS.items():
            match = re.match(r'^\s*(?:[-*]\s*)?' + re.escape(label) + r'\s*[:：]\s*(.+?)\s*$', line)
            if match:
                value = match[1].strip(' *`')
                if value:
                    result[field] = {'raw': value, 'line': line_no}
    return result


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    core = [r for r in jsonl(ROOT / 'Data/papers.jsonl') if r['active_confirmed_core']]
    assert len(core) == 662
    vocab = vocabularies()
    assignments = [r for r in jsonl(ROOT / 'Data/paper_module_taxonomy_assignments.jsonl') if r['paper_id'] in {p['paper_id'] for p in core}]
    assert len(assignments) == 935
    tex_root = WORKSPACE / 'Agent_for_Science_Review_Overleaf'
    if not (tex_root / 'main.tex').exists():
        tex_root = MANUSCRIPT
    bib_path = tex_root / 'references.bib'
    entries = parse_bib(bib_path.read_text(encoding='utf-8'))
    with (ROOT / 'Coverage_Check/bibliography_2026-10-30/paper_citation_keys.csv').open(encoding='utf-8-sig') as f:
        bridge = {r['paper_id']: r['citation_key'] for r in csv.DictReader(f)}
    cited = set()
    for f in tex_root.rglob('*.tex'):
        if 'build' in f.parts: continue
        for group in re.findall(r'\\cite\w*\s*(?:\[[^\]]*\])*\{([^}]+)\}', f.read_text(encoding='utf-8')):
            cited.update(k.strip() for k in group.split(','))
    cases = load(MANUSCRIPT / 'data/illustrative_domain_profiles.json')['cases']
    case_ids = {r['id'] for r in cases}
    reviewed = load(OUT / 'applied_changes.json') if (OUT / 'applied_changes.json').exists() else {'records': []}
    reviewed_fields = {(r['paper_id'], c['field']) for r in reviewed['records'] for c in r['changes']}
    findings = []
    for name in ('reviewer_0001_0350.json', 'reviewer_0351_0750.json', 'reviewer_0751_1133.json'):
        data = load(OUT / name)
        for r in data.get('records', data.get('papers', [])):
            for issue in r.get('unresolved', []):
                findings.append({'paper_id': r['paper_id'], 'reviewer_artifact': name, 'finding': issue})
        for list_key in ('existing_nonempty_risk_queue', 'note_summary_conflict_risk_queue'):
            for issue in data.get(list_key, []):
                findings.append({'paper_id': issue['paper_id'], 'reviewer_artifact': name, 'finding': issue})
    write_json(OUT / 'reviewer_unresolved_findings.json', findings)
    finding_counts = Counter(r['paper_id'] for r in findings)
    versions = load(OUT / 'reviewer_versions.json') if (OUT / 'reviewer_versions.json').exists() else {}
    version_by_id = {r['id']: r for r in versions.get('year_decisions', [])}
    manifest = []; matrix = []; queue = []; note_index = []; subset = []
    for p in core:
        pid = p['paper_id']; key = bridge[pid]
        assert key in entries, (pid, key)
        raw_entry, bib = entries[key]; subset.append(raw_entry)
        note = note_summary(ROOT / p['note_path'])
        maps = [a for a in assignments if a['paper_id'] == pid]
        manifest.append({
            'paper_id': pid, 'title': p['title'], 'authors': p['authors'], 'year': p['year'],
            'source': p['source'], 'doi_or_url': p['doi_or_url'], 'doi': p['doi'], 'arxiv_id': p['arxiv_id'],
            'citation_key': key, 'cited_in_manuscript': key in cited, 'reference_year': bib.get('year', ''),
            'reference_authors': bib.get('author', ''),
            'reference_doi': bib.get('doi', ''), 'reference_eprint': bib.get('eprint', ''), 'reference_url': bib.get('url', ''),
            'reference_venue': bib.get('journal', bib.get('booktitle', '')),
            'version_note': bib.get('note', ''),
            'selected_version_this_round': version_by_id.get(pid, {}).get('selected_version', ''),
            'version_evidence_this_round': version_by_id.get(pid, {}).get('evidence', {}),
            'version_limit': 'Reference identifies the selected record; an unversioned URL does not establish the exact PDF revision.',
            'inclusion_status': p['inclusion_status'], 'inclusion_trace': p['remarks'],
            'scientific_object_modules': p['scientific_object_modules'], 'general_method_bucket': p['general_method_bucket'],
            'module_assignments': maps, 'classification_parser_rule': p['classification_parser_rule'],
            'note_path': p['note_path'], 'pdf_path': p['pdf_path'], 'pdf_exists': p['pdf_exists'],
            'evidence_status': p['evidence_status'], 'source_checked_at': p['source_checked_at'],
            'first_hand_sources_checked': p['first_hand_sources_checked'],
        })
        row = {'paper_id': pid, 'scientific_object_modules': p['scientific_object_modules'],
               'general_method_bucket': p['general_method_bucket'],
               'domain_secondary_complete': all(a.get('secondary_taxonomy_code') for a in maps) if maps else '',
               'domain_tertiary_complete': all(a.get('tertiary_taxonomy_code') for a in maps) if maps else '',
               'note_exists': p['note_exists'], 'pdf_exists': p['pdf_exists'],
               'source_workflow_evidence_status': p['evidence_status'],
               'first_hand_source_field_populated': bool(p['first_hand_sources_checked']),
               'purposive_case': pid in case_ids,
               'reviewer_unresolved_findings': finding_counts[pid],
               'filing_topic_raw': p['fourth_level_topic'],
               'object_task_result_corpus_coded': False,
               'decision_paradigms_corpus_coded': False,
               'organization_topology_corpus_coded': False,
               'human_decision_ownership_corpus_coded': False,
               'contribution_attribution_corpus_coded': False,
               'validation_independence_corpus_coded': False,
               'external_validity_corpus_coded': False,
               'all_four_tags_primary_source_rechecked_this_round': False}
        for field in FIELDS:
            values = p[field]; unknown = [t for t in values if t not in vocab[field]]
            row.update({field + '_raw': p[field + '_raw'], field + '_populated': bool(values),
                        field + '_all_tokens_in_schema': bool(values) and not unknown,
                        field + '_unresolved_tokens': unknown,
                        field + '_note_summary': note.get(field, {}).get('raw', ''),
                        field + '_note_summary_line': note.get(field, {}).get('line', ''),
                        field + '_aligned_to_note_this_round': (pid, field) in reviewed_fields})
            if not values or unknown:
                queue.append({'paper_id': pid, 'field': field, 'raw': p[field + '_raw'],
                              'issue': 'empty_owner_field' if not values else 'legacy_or_unresolved_tokens',
                              'unresolved_tokens': unknown, 'note_path': p['note_path'],
                              'action': 'Check specific source evidence; do not infer absence or force a schema label.'})
        for field in ('autonomy', 'cross_attributes'):
            row[field + '_note_summary_present'] = field in note
            row[field + '_note_summary_raw'] = note.get(field, {}).get('raw', '')
            row[field + '_note_summary_line'] = note.get(field, {}).get('line', '')
        for field, item in note.items():
            note_index.append({'paper_id': pid, 'field': field, 'note_path': p['note_path'], **item,
                               'independently_verified_this_round': False})
        matrix.append(row)
    assert len({r['citation_key'] for r in manifest}) == 662
    write_csv(OUT / 'core_corpus_manifest.csv', manifest)
    (OUT / 'core_corpus_manifest.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in manifest), encoding='utf-8')
    (OUT / 'core_references.bib').write_text('\n\n'.join(subset) + '\n', encoding='utf-8')
    write_csv(OUT / 'coding_coverage_matrix.csv', matrix)
    write_csv(OUT / 'tag_evidence_review_queue.csv', queue)
    write_csv(OUT / 'note_tag_source_index.csv', note_index)
    write_csv(OUT / 'core_reference_bridge.csv', [{k: r[k] for k in ('paper_id', 'citation_key', 'cited_in_manuscript', 'reference_year')} for r in manifest])
    write_json(OUT / 'role_aggregation_mapping.json', {
        'source_schema': str(SCHEMA.relative_to(ROOT)), 'mapping': ROLE_GROUPS,
        'end_to_end_research_automation': 'Kept as an integrative descriptor; never expands automatically into six role observations.',
        'decision_paradigms': 'Six analytical mechanisms are coded only in the eleven selected cases, not inferred from agent_type.',
        'organization': 'Multi-Agent System and Human-in-the-loop Agent are existing type tags; they do not establish topology or decision ownership.',
        'note_fields': 'autonomy and cross_attributes remain note-owned descriptions in this inventory; raw summaries are indexed without automatic scientific validation.'})
    searches = []; source_paths = [SCHEMA, ROOT / 'Paper_Lists/agent_master_paper_list.md', ROOT / 'Data/papers.jsonl',
        ROOT / 'Data/paper_module_taxonomy_assignments.jsonl', bib_path]
    for name in ('A_general', 'B_chem_materials', 'C_life_health', 'D_formal_physics', 'E_earth_agri_engineering', 'f_knowledge'):
        path = ROOT / f'Coverage_Check/october_round2_{name}.json'; data = load(path); source_paths.append(path)
        for list_key in ('search_log', 'searches'):
            for i, record in enumerate(data.get(list_key, [])):
                searches.append({'source_path': str(path.relative_to(ROOT)), 'source_sha256': sha(path),
                                 'json_location': f'{list_key}[{i}]', 'record': record})
    write_json(OUT / 'recoverable_search_records.json', {'search_cutoff': '2026-10-22', 'records': searches,
        'limitation': 'Recoverable historical records only; overlapping query hits and capped returns are not a screening denominator.'})
    summary = {'snapshot_date': '2026-11-01', 'core_works': len(core), 'formal_domain_works': sum(bool(p['scientific_object_modules']) for p in core),
               'module_memberships': len(assignments), 'secondary_coded_memberships': sum(bool(a.get('secondary_taxonomy_code')) for a in assignments),
               'tertiary_coded_memberships': sum(bool(a.get('tertiary_taxonomy_code')) for a in assignments),
               'notes': sum(p['note_exists'] for p in core), 'local_pdfs': sum(p['pdf_exists'] for p in core),
               'directly_cited_core_works': sum(r['cited_in_manuscript'] for r in manifest), 'manuscript_citation_keys': len(cited),
               'bibliography_entries': len(entries), 'purposive_cases': len(cases), 'recoverable_search_records': len(searches),
               'tag_coverage': {field: {'owner_populated': sum(r[field + '_populated'] for r in matrix),
                                      'all_tokens_in_schema': sum(r[field + '_all_tokens_in_schema'] for r in matrix),
                                      'note_aligned_this_round': sum(r[field + '_aligned_to_note_this_round'] for r in matrix)} for field in FIELDS},
               'note_summary_coverage': {field: sum(r['field'] == field for r in note_index) for field in NOTE_LABELS},
               'primary_source_rechecked_for_all_four_tags_this_round': 0,
               'interpretation': 'Occupancy, vocabulary conformance, note alignment, and original-source verification are different measures. No full-corpus paradigm, organization-topology, contribution-attribution, or human-decision prevalence is estimated.',
               'source_hashes': {str(p.relative_to(WORKSPACE)): sha(p) for p in source_paths}}
    write_json(OUT / 'coverage_summary.json', summary)
    lines = ['# 核心库标签对齐与编码覆盖（2026-11-01）', '',
        '本轮沿用既有 annotation schema、主表和笔记。覆盖矩阵是派生盘点，不另设分类事实源。空值表示未记录；旧扩展值保留原文进入核查队列，不表示该能力不存在。', '',
        f'核心工作{len(core)}篇，正式领域660篇，独立通用方法桶2篇；学科归属935项，二级933项，三级931项。笔记662份，本地PDF635份。', '',
        '| 副标签字段 | 主表有值 | 全部词元符合既有schema | 本轮逐字段笔记对齐 |', '|---|---:|---:|---:|']
    for field, counts in summary['tag_coverage'].items():
        lines.append(f"| {field} | {counts['owner_populated']} | {counts['all_tokens_in_schema']} | {counts['note_aligned_this_round']} |")
    lines += ['', '词表符合不等于原文核实；本轮笔记对齐不冒充独立全文复核。自主能力与交叉属性在既有笔记内，其原始值和行号见note_tag_source_index.csv，不能因主表无专栏而报告为零覆盖。', '',
        '六类科研角色是既有13个细标签的正文聚合，映射见role_aggregation_mapping.json。六种决策机制、协作拓扑、科学贡献归因与人类决策职责尚未完成全库编码；11个目的性案例仅支持定性比较。', '',
        'ASD-0547/04、ASD-0919/05、ASD-0919/11、ASD-0925/02仍缺三级；其中0919/05与0925/02也缺二级。既有证据不足，本轮保持原判。', '',
        '入口：core_corpus_manifest.csv/jsonl（662行）、core_references.bib（662条）、core_reference_bridge.csv、coding_coverage_matrix.csv、tag_evidence_review_queue.csv。详细变更证据见applied_changes.json与reviewer_*.json。', '',
        '清单、矩阵与检索索引等派生输出可运行 scripts/build_core_evidence_package.py 从当前owner和留存审阅记录重建；reviewer文件及原文核查记录保留为本轮证据。核心成员或快照变化时须另建日期包，不能把本日期作为后续变动的隐式容器。', '']
    (OUT / 'README.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps({k:v for k,v in summary.items() if k != 'source_hashes'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
