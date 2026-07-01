#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / 'Data'
PAPERS_JSONL = DATA_DIR / 'papers.jsonl'
TAXONOMY_JSON = DATA_DIR / 'taxonomy_index.json'
PDF_MANIFEST_JSON = DATA_DIR / 'pdf_manifest.json'
MISSING_PDF_JSON = DATA_DIR / 'missing_pdf_manifest.json'
NOTE_MANIFEST_JSON = DATA_DIR / 'note_manifest.json'
PAPERS_CSV = DATA_DIR / 'papers.csv'
PAPER_MODULES_CSV = DATA_DIR / 'paper_modules.csv'
SQLITE_PATH = DATA_DIR / 'papers.sqlite'
FORMAL_MODULES = {f'{idx:02d}' for idx in range(1, 12)}
CSV_FIELDS = [
    'paper_id', 'title', 'authors', 'year', 'source', 'doi_or_url', 'doi', 'url', 'arxiv_id',
    'pdf_path', 'pdf_exists', 'note_path', 'note_exists', 'is_agent', 'inclusion_status',
    'exclusion_reason', 'legacy_main_class', 'legacy_secondary_class', 'legacy_tertiary_class',
    'fourth_level_topic', 'new_fourth_level', 'agent_type', 'research_workflow_role',
    'validation_type', 'scientific_contribution_type', 'evidence_strength', 'citation_priority',
    'scientific_object_modules', 'general_method_bucket', 'object_coverage_mode',
    'primary_module_for_filing', 'first_hand_sources_checked', 'progress_title', 'pdf_status',
    'evidence_status', 'note_status', 'master_status', 'final_modules_or_bucket',
    'source_limited', 'batch', 'closed', 'active_confirmed_core', 'exported_at',
]

def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

def load_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]

def compute_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()

def bool_to_int(value: object) -> int:
    return 1 if bool(value) else 0

def flatten_list(value: object) -> str:
    if isinstance(value, list):
        return ';'.join(str(item) for item in value)
    return '' if value is None else str(value)

def json_list(value: object) -> str:
    return json.dumps(value if isinstance(value, list) else [], ensure_ascii=False)

def write_papers_csv(papers: list[dict[str, object]]) -> None:
    with PAPERS_CSV.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for paper in papers:
            writer.writerow({field: flatten_list(paper.get(field)) for field in CSV_FIELDS})

def build_module_rows(papers: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for paper in papers:
        for scope in ('scientific_object_modules', 'final_modules_or_bucket'):
            modules = paper.get(scope, [])
            if not isinstance(modules, list):
                continue
            for sort_order, module_code in enumerate(modules, start=1):
                rows.append({
                    'paper_id': paper['paper_id'],
                    'title': paper['title'],
                    'assignment_scope': scope,
                    'module_code': module_code,
                    'module_kind': 'formal_module' if module_code in FORMAL_MODULES else 'general_bucket',
                    'sort_order': sort_order,
                    'active_confirmed_core': bool_to_int(paper['active_confirmed_core']),
                })
    return rows

def write_module_csv(rows: list[dict[str, object]]) -> None:
    fieldnames = ['paper_id', 'title', 'assignment_scope', 'module_code', 'module_kind', 'sort_order', 'active_confirmed_core']
    with PAPER_MODULES_CSV.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def build_sqlite(papers: list[dict[str, object]], taxonomy: dict[str, dict[str, str]], pdf_manifest: list[dict[str, object]], missing_pdf_manifest: list[dict[str, object]], note_manifest: list[dict[str, object]], module_rows: list[dict[str, object]]) -> None:
    if SQLITE_PATH.exists():
        SQLITE_PATH.unlink()
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        conn.executescript('''
        PRAGMA foreign_keys = ON;
        CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
        CREATE TABLE taxonomy_index (code TEXT PRIMARY KEY, label TEXT NOT NULL, kind TEXT NOT NULL);
        CREATE TABLE papers (
            paper_id TEXT PRIMARY KEY, title TEXT NOT NULL, authors TEXT, year TEXT, source TEXT, doi_or_url TEXT, doi TEXT, url TEXT, arxiv_id TEXT,
            pdf_path TEXT, pdf_exists INTEGER NOT NULL, note_path TEXT, note_exists INTEGER NOT NULL, is_agent TEXT, inclusion_status TEXT, exclusion_reason TEXT,
            legacy_main_class TEXT, legacy_secondary_class TEXT, legacy_tertiary_class TEXT, fourth_level_topic TEXT, new_fourth_level TEXT,
            agent_type_json TEXT NOT NULL, research_workflow_role_json TEXT NOT NULL, validation_type_json TEXT NOT NULL, scientific_contribution_type_json TEXT NOT NULL,
            evidence_strength TEXT, citation_priority TEXT, remarks TEXT, scientific_object_modules_json TEXT NOT NULL, general_method_bucket TEXT NOT NULL,
            object_coverage_mode TEXT, primary_module_for_filing TEXT, first_hand_sources_checked TEXT, progress_title TEXT, pdf_status TEXT, evidence_status TEXT,
            note_status TEXT, master_status TEXT, final_modules_or_bucket_raw TEXT, final_modules_or_bucket_json TEXT NOT NULL, source_limited TEXT, batch TEXT, closed TEXT,
            active_confirmed_core INTEGER NOT NULL, exported_at TEXT NOT NULL
        );
        CREATE TABLE paper_modules (paper_id TEXT NOT NULL, assignment_scope TEXT NOT NULL, module_code TEXT NOT NULL, module_kind TEXT NOT NULL, sort_order INTEGER NOT NULL, PRIMARY KEY (paper_id, assignment_scope, module_code));
        CREATE TABLE pdf_inventory (paper_id TEXT PRIMARY KEY, title TEXT NOT NULL, pdf_path TEXT NOT NULL, sha256 TEXT NOT NULL, primary_module_for_filing TEXT, scientific_object_modules_json TEXT NOT NULL, pdf_status TEXT, evidence_status TEXT, active_confirmed_core INTEGER NOT NULL);
        CREATE TABLE missing_pdf_inventory (paper_id TEXT PRIMARY KEY, title TEXT NOT NULL, doi TEXT, url TEXT, pdf_status TEXT, evidence_status TEXT, source_limited TEXT, access_note TEXT);
        CREATE TABLE note_inventory (paper_id TEXT PRIMARY KEY, title TEXT NOT NULL, note_path TEXT, note_exists INTEGER NOT NULL, active_confirmed_core INTEGER NOT NULL, inclusion_status TEXT);
        CREATE VIEW active_confirmed_core_papers AS SELECT * FROM papers WHERE active_confirmed_core = 1;
        CREATE VIEW active_missing_local_pdf AS SELECT * FROM papers WHERE active_confirmed_core = 1 AND pdf_exists = 0;
        CREATE VIEW module_assignment_counts AS SELECT assignment_scope, module_code, COUNT(*) AS paper_count, SUM(CASE WHEN p.active_confirmed_core = 1 THEN 1 ELSE 0 END) AS active_confirmed_core_count FROM paper_modules pm JOIN papers p ON p.paper_id = pm.paper_id GROUP BY assignment_scope, module_code;
        ''')
        active = [row for row in papers if row['active_confirmed_core']]
        active_local = [row for row in active if row['pdf_exists']]
        active_missing = [row for row in active if not row['pdf_exists']]
        conn.executemany('INSERT INTO metadata(key, value) VALUES(?, ?)', [
            ('schema_version', '2026-07-01'),
            ('papers_jsonl_sha256', compute_sha256(PAPERS_JSONL)),
            ('papers_record_count', str(len(papers))),
            ('active_confirmed_core_count', str(len(active))),
            ('active_local_pdf_count', str(len(active_local))),
            ('active_no_local_pdf_count', str(len(active_missing))),
        ])
        conn.executemany('INSERT INTO taxonomy_index(code, label, kind) VALUES(?, ?, ?)', [
            (code, label, 'formal_module' if code in FORMAL_MODULES else 'general_bucket')
            for code, label in taxonomy['code_to_label'].items()
        ])
        conn.executemany('INSERT INTO papers VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [
            (
                paper['paper_id'], paper['title'], paper['authors'], paper['year'], paper['source'], paper['doi_or_url'], paper['doi'], paper['url'], paper['arxiv_id'],
                paper['pdf_path'], bool_to_int(paper['pdf_exists']), paper['note_path'], bool_to_int(paper['note_exists']), paper['is_agent'], paper['inclusion_status'], paper['exclusion_reason'],
                paper['legacy_main_class'], paper['legacy_secondary_class'], paper['legacy_tertiary_class'], paper['fourth_level_topic'], paper['new_fourth_level'],
                json_list(paper['agent_type']), json_list(paper['research_workflow_role']), json_list(paper['validation_type']), json_list(paper['scientific_contribution_type']),
                paper['evidence_strength'], paper['citation_priority'], paper['remarks'], json_list(paper['scientific_object_modules']), paper['general_method_bucket'], paper['object_coverage_mode'],
                paper['primary_module_for_filing'], paper['first_hand_sources_checked'], paper['progress_title'], paper['pdf_status'], paper['evidence_status'], paper['note_status'], paper['master_status'],
                paper['final_modules_or_bucket_raw'], json_list(paper['final_modules_or_bucket']), paper['source_limited'], paper['batch'], paper['closed'], bool_to_int(paper['active_confirmed_core']), paper['exported_at'],
            )
            for paper in papers
        ])
        conn.executemany('INSERT INTO paper_modules(paper_id, assignment_scope, module_code, module_kind, sort_order) VALUES(?, ?, ?, ?, ?)', [
            (row['paper_id'], row['assignment_scope'], row['module_code'], row['module_kind'], row['sort_order'])
            for row in module_rows
        ])
        conn.executemany('INSERT INTO pdf_inventory VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', [
            (row['paper_id'], row['title'], row['pdf_path'], row['sha256'], row['primary_module_for_filing'], json_list(row['scientific_object_modules']), row['pdf_status'], row['evidence_status'], bool_to_int(row['active_confirmed_core']))
            for row in pdf_manifest
        ])
        conn.executemany('INSERT INTO missing_pdf_inventory VALUES(?, ?, ?, ?, ?, ?, ?, ?)', [
            (row['paper_id'], row['title'], row['doi'], row['url'], row['pdf_status'], row['evidence_status'], row['source_limited'], row['access_note'])
            for row in missing_pdf_manifest
        ])
        conn.executemany('INSERT INTO note_inventory VALUES(?, ?, ?, ?, ?, ?)', [
            (row['paper_id'], row['title'], row['note_path'], bool_to_int(row['note_exists']), bool_to_int(row['active_confirmed_core']), row['inclusion_status'])
            for row in note_manifest
        ])
        conn.commit()
    finally:
        conn.close()

def main() -> None:
    papers = load_jsonl(PAPERS_JSONL)
    taxonomy = load_json(TAXONOMY_JSON)
    pdf_manifest = load_json(PDF_MANIFEST_JSON)
    missing_pdf_manifest = load_json(MISSING_PDF_JSON)
    note_manifest = load_json(NOTE_MANIFEST_JSON)
    module_rows = build_module_rows(papers)
    write_papers_csv(papers)
    write_module_csv(module_rows)
    build_sqlite(papers, taxonomy, pdf_manifest, missing_pdf_manifest, note_manifest, module_rows)
    print(f'Wrote {PAPERS_CSV}')
    print(f'Wrote {PAPER_MODULES_CSV}')
    print(f'Wrote {SQLITE_PATH}')
    print(f'papers rows: {len(papers)}')
    print(f'paper_modules rows: {len(module_rows)}')

if __name__ == '__main__':
    main()
