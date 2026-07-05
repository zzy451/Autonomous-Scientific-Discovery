#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / 'Data'
REGISTRY_DIR = DATA_DIR / 'registry'
PAPERS_JSONL = DATA_DIR / 'papers.jsonl'
TAXONOMY_JSON = DATA_DIR / 'taxonomy_index.json'
CLASSIFICATION_CODE_INDEX_JSON = DATA_DIR / 'classification_code_index.json'
CHANGE_LOG_JSONL = DATA_DIR / 'change_log.jsonl'
PDF_MANIFEST_JSON = DATA_DIR / 'pdf_manifest.json'
MISSING_PDF_JSON = DATA_DIR / 'missing_pdf_manifest.json'
NOTE_MANIFEST_JSON = DATA_DIR / 'note_manifest.json'
DISCIPLINE_CODE_ASSIGNMENTS_JSONL = DATA_DIR / 'discipline_code_assignments.jsonl'
DISCIPLINE_LOCAL_CODE_REGISTRY_JSONL = DATA_DIR / 'discipline_local_code_registry.jsonl'
ASSET_MANIFEST_JSONL = REGISTRY_DIR / 'asset_manifest.jsonl'
PDF_ARCHIVE_REGISTRY_JSONL = REGISTRY_DIR / 'pdf_archive_registry.jsonl'
PAPERS_CSV = DATA_DIR / 'papers.csv'
PAPER_MODULES_CSV = DATA_DIR / 'paper_modules.csv'
CANONICAL_PAPER_MODULES_CSV = DATA_DIR / 'canonical_paper_modules.csv'
WORKFLOW_MIRROR_PAPER_MODULES_CSV = DATA_DIR / 'workflow_mirror_paper_modules.csv'
DISCIPLINE_LOCAL_CODE_REGISTRY_CSV = DATA_DIR / 'discipline_local_code_registry.csv'
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
    'source_limited', 'batch', 'closed', 'active_confirmed_core', 'record_status',
    'inclusion_decision', 'duplicate_of', 'last_reviewed_at', 'last_reviewed_by', 'exported_at',
]
DISCIPLINE_LOCAL_CODE_REGISTRY_FIELDS = [
    'paper_id', 'assignment_id', 'discipline_local_code', 'discipline_local_rank',
    'assignment_status', 'assigned_at', 'assigned_by', 'retired_at', 'redirected_to_code',
    'assignment_reason', 'pending_reason', 'primary_module_for_filing',
    'primary_taxonomy_code_2lvl', 'legacy_secondary_class', 'scientific_object_modules',
    'general_method_bucket', 'title', 'note_path', 'pdf_path', 'active_confirmed_core',
    'is_derived_snapshot', 'generated_at', 'generated_by', 'source_commit', 'worktree_dirty',
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
    with CANONICAL_PAPER_MODULES_CSV.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows([row for row in rows if row['assignment_scope'] == 'scientific_object_modules'])
    with WORKFLOW_MIRROR_PAPER_MODULES_CSV.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows([row for row in rows if row['assignment_scope'] == 'final_modules_or_bucket'])

def write_discipline_local_code_registry_csv(rows: list[dict[str, object]]) -> None:
    with DISCIPLINE_LOCAL_CODE_REGISTRY_CSV.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=DISCIPLINE_LOCAL_CODE_REGISTRY_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({
                field: flatten_list(row.get(field))
                for field in DISCIPLINE_LOCAL_CODE_REGISTRY_FIELDS
            })

def build_general_method_bucket_rows(papers: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for paper in papers:
        bucket = paper.get('general_method_bucket')
        if not bucket or bucket == 'none':
            continue
        rows.append({
            'paper_id': paper['paper_id'],
            'general_method_bucket': bucket,
            'active_confirmed_core': bool_to_int(paper['active_confirmed_core']),
            'source_limited': paper['source_limited'],
        })
    return rows

def build_classification_term_rows(classification_code_index: dict[str, object]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for term in classification_code_index.get('primary_terms', []):
        rows.append({
            'taxonomy_code': term['primary_code'],
            'term_level': 'primary',
            'parent_primary_code': None,
            'label': term['label'],
            'definition': term['definition'],
            'include_json': json.dumps(term.get('include', []), ensure_ascii=False),
            'exclude_json': json.dumps(term.get('exclude', []), ensure_ascii=False),
            'status': term['status'],
            'source': term['source'],
            'review_status': None,
        })
    for term in classification_code_index.get('secondary_terms', []):
        rows.append({
            'taxonomy_code': term['secondary_code'],
            'term_level': 'secondary',
            'parent_primary_code': term['parent_primary_code'],
            'label': term['label'],
            'definition': term['definition'],
            'include_json': json.dumps(term.get('include', []), ensure_ascii=False),
            'exclude_json': json.dumps(term.get('exclude', []), ensure_ascii=False),
            'status': term['status'],
            'source': term['source'],
            'review_status': term.get('review_status'),
        })
    return rows

def build_sqlite(
    papers: list[dict[str, object]],
    taxonomy: dict[str, dict[str, str]],
    classification_code_index: dict[str, object],
    pdf_manifest: list[dict[str, object]],
    missing_pdf_manifest: list[dict[str, object]],
    note_manifest: list[dict[str, object]],
    module_rows: list[dict[str, object]],
    discipline_code_assignments: list[dict[str, object]],
    discipline_local_code_registry: list[dict[str, object]],
    asset_manifest: list[dict[str, object]],
    pdf_archive_registry: list[dict[str, object]],
) -> None:
    if SQLITE_PATH.exists():
        SQLITE_PATH.unlink()
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        conn.executescript('''
        PRAGMA foreign_keys = ON;
        CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
        CREATE TABLE taxonomy_index (code TEXT PRIMARY KEY, label TEXT NOT NULL, kind TEXT NOT NULL);
        CREATE TABLE classification_terms (
            taxonomy_code TEXT NOT NULL,
            term_level TEXT NOT NULL,
            parent_primary_code TEXT,
            label TEXT NOT NULL,
            definition TEXT NOT NULL,
            include_json TEXT NOT NULL,
            exclude_json TEXT NOT NULL,
            status TEXT NOT NULL,
            source TEXT NOT NULL,
            review_status TEXT,
            PRIMARY KEY (taxonomy_code, term_level)
        );
        CREATE TABLE change_log (
            change_id TEXT PRIMARY KEY,
            paper_id TEXT NOT NULL,
            changed_at TEXT NOT NULL,
            changed_by TEXT NOT NULL,
            change_type TEXT NOT NULL,
            old_value_json TEXT NOT NULL,
            new_value_json TEXT NOT NULL,
            reason TEXT NOT NULL,
            related_commit TEXT
        );
        CREATE TABLE analysis_object_scope_registry (
            object_name TEXT PRIMARY KEY,
            object_type TEXT NOT NULL,
            scope_class TEXT NOT NULL,
            default_usage TEXT NOT NULL,
            warning TEXT NOT NULL
        );
        CREATE TABLE papers (
            paper_id TEXT PRIMARY KEY, title TEXT NOT NULL, authors TEXT, year TEXT, source TEXT, doi_or_url TEXT, doi TEXT, url TEXT, arxiv_id TEXT,
            pdf_path TEXT, pdf_exists INTEGER NOT NULL, note_path TEXT, note_exists INTEGER NOT NULL, is_agent TEXT, inclusion_status TEXT, exclusion_reason TEXT,
            legacy_main_class TEXT, legacy_secondary_class TEXT, legacy_tertiary_class TEXT, fourth_level_topic TEXT, new_fourth_level TEXT,
            agent_type_json TEXT NOT NULL, research_workflow_role_json TEXT NOT NULL, validation_type_json TEXT NOT NULL, scientific_contribution_type_json TEXT NOT NULL,
            evidence_strength TEXT, citation_priority TEXT, remarks TEXT, scientific_object_modules_json TEXT NOT NULL, general_method_bucket TEXT NOT NULL,
            object_coverage_mode TEXT, primary_module_for_filing TEXT, first_hand_sources_checked TEXT, progress_title TEXT, pdf_status TEXT, evidence_status TEXT,
            note_status TEXT, master_status TEXT, final_modules_or_bucket_raw TEXT, final_modules_or_bucket_json TEXT NOT NULL, source_limited TEXT, batch TEXT, closed TEXT,
            active_confirmed_core INTEGER NOT NULL, record_status TEXT, inclusion_decision TEXT, duplicate_of TEXT, last_reviewed_at TEXT, last_reviewed_by TEXT, exported_at TEXT NOT NULL
        );
        CREATE TABLE paper_modules (paper_id TEXT NOT NULL, assignment_scope TEXT NOT NULL, module_code TEXT NOT NULL, module_kind TEXT NOT NULL, sort_order INTEGER NOT NULL, PRIMARY KEY (paper_id, assignment_scope, module_code));
        CREATE TABLE paper_general_method_buckets (
            paper_id TEXT PRIMARY KEY,
            general_method_bucket TEXT NOT NULL,
            active_confirmed_core INTEGER NOT NULL,
            source_limited TEXT
        );
        CREATE TABLE discipline_code_assignments (
            assignment_id TEXT PRIMARY KEY,
            paper_id TEXT NOT NULL,
            discipline_local_code TEXT,
            primary_taxonomy_code_2lvl TEXT,
            assignment_status TEXT NOT NULL,
            assigned_at TEXT NOT NULL,
            assigned_by TEXT NOT NULL,
            retired_at TEXT,
            redirected_to_code TEXT,
            assignment_reason TEXT NOT NULL,
            pending_reason TEXT,
            source_primary_module_for_filing TEXT,
            source_legacy_secondary_class TEXT,
            schema_version INTEGER NOT NULL
        );
        CREATE TABLE discipline_local_code_registry (
            paper_id TEXT PRIMARY KEY,
            assignment_id TEXT NOT NULL,
            discipline_local_code TEXT,
            discipline_local_rank TEXT,
            assignment_status TEXT NOT NULL,
            assigned_at TEXT NOT NULL,
            assigned_by TEXT NOT NULL,
            retired_at TEXT,
            redirected_to_code TEXT,
            assignment_reason TEXT NOT NULL,
            pending_reason TEXT,
            primary_module_for_filing TEXT,
            primary_taxonomy_code_2lvl TEXT,
            legacy_secondary_class TEXT,
            scientific_object_modules_json TEXT NOT NULL,
            general_method_bucket TEXT,
            title TEXT NOT NULL,
            note_path TEXT,
            pdf_path TEXT,
            active_confirmed_core INTEGER NOT NULL,
            is_derived_snapshot INTEGER NOT NULL,
            generated_at TEXT NOT NULL,
            generated_by TEXT NOT NULL,
            source_commit TEXT,
            worktree_dirty INTEGER NOT NULL
        );
        CREATE TABLE pdf_evidence_status (
            paper_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            pdf_path TEXT,
            pdf_exists INTEGER NOT NULL,
            pdf_status TEXT,
            evidence_status TEXT,
            source_limited TEXT,
            primary_module_for_filing TEXT,
            active_confirmed_core INTEGER NOT NULL
        );
        CREATE TABLE paper_assets (
            asset_id TEXT PRIMARY KEY,
            paper_id TEXT NOT NULL,
            title TEXT NOT NULL,
            asset_type TEXT NOT NULL,
            path TEXT,
            asset_exists INTEGER NOT NULL,
            sha256 TEXT,
            asset_status TEXT,
            source_limited TEXT,
            exported_at TEXT
        );
        CREATE TABLE notes (
            paper_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            note_path TEXT,
            note_exists INTEGER NOT NULL,
            active_confirmed_core INTEGER NOT NULL,
            inclusion_status TEXT
        );
        CREATE TABLE pdf_inventory (paper_id TEXT PRIMARY KEY, title TEXT NOT NULL, pdf_path TEXT NOT NULL, sha256 TEXT NOT NULL, primary_module_for_filing TEXT, scientific_object_modules_json TEXT NOT NULL, pdf_status TEXT, evidence_status TEXT, active_confirmed_core INTEGER NOT NULL);
        CREATE TABLE missing_pdf_inventory (paper_id TEXT PRIMARY KEY, title TEXT NOT NULL, doi TEXT, url TEXT, pdf_status TEXT, evidence_status TEXT, source_limited TEXT, access_note TEXT);
        CREATE TABLE note_inventory (paper_id TEXT PRIMARY KEY, title TEXT NOT NULL, note_path TEXT, note_exists INTEGER NOT NULL, active_confirmed_core INTEGER NOT NULL, inclusion_status TEXT);
        CREATE VIEW active_confirmed_core_papers AS SELECT * FROM papers WHERE active_confirmed_core = 1;
        CREATE VIEW active_missing_local_pdf AS SELECT * FROM papers WHERE active_confirmed_core = 1 AND pdf_exists = 0;
        CREATE VIEW canonical_paper_modules AS
        SELECT * FROM paper_modules WHERE assignment_scope = 'scientific_object_modules';
        CREATE VIEW workflow_mirror_paper_modules AS
        SELECT * FROM paper_modules WHERE assignment_scope = 'final_modules_or_bucket';
        CREATE VIEW mixed_scope_paper_modules AS
        SELECT * FROM paper_modules;
        CREATE VIEW module_assignment_counts AS
        SELECT
            assignment_scope,
            module_code,
            COUNT(*) AS paper_count,
            SUM(CASE WHEN p.active_confirmed_core = 1 THEN 1 ELSE 0 END) AS active_confirmed_core_count
        FROM paper_modules pm
        JOIN papers p ON p.paper_id = pm.paper_id
        GROUP BY assignment_scope, module_code;
        CREATE VIEW mixed_scope_module_assignment_counts AS
        SELECT * FROM module_assignment_counts;
        CREATE VIEW canonical_module_assignment_counts AS
        SELECT
            module_code,
            COUNT(*) AS paper_count,
            SUM(CASE WHEN p.active_confirmed_core = 1 THEN 1 ELSE 0 END) AS active_confirmed_core_count
        FROM canonical_paper_modules pm
        JOIN papers p ON p.paper_id = pm.paper_id
        GROUP BY module_code;
        CREATE VIEW workflow_mirror_module_assignment_counts AS
        SELECT
            module_code,
            COUNT(*) AS paper_count,
            SUM(CASE WHEN p.active_confirmed_core = 1 THEN 1 ELSE 0 END) AS active_confirmed_core_count
        FROM workflow_mirror_paper_modules pm
        JOIN papers p ON p.paper_id = pm.paper_id
        GROUP BY module_code;
        CREATE VIEW canonical_object_coverage_summary AS
        SELECT
            CASE
                WHEN active_confirmed_core = 1 THEN 'active_confirmed_core'
                ELSE 'inactive_or_non_core'
            END AS scope,
            object_coverage_mode,
            COUNT(*) AS paper_count,
            SUM(pdf_exists) AS local_pdf_count,
            SUM(note_exists) AS note_count,
            SUM(CASE WHEN lower(trim(COALESCE(source_limited, ''))) LIKE 'yes%' THEN 1 ELSE 0 END) AS source_limited_count
        FROM papers
        WHERE trim(COALESCE(object_coverage_mode, '')) <> ''
        GROUP BY scope, object_coverage_mode;
        CREATE VIEW canonical_multi_module_combo_summary AS
        WITH combos AS (
            SELECT
                CASE
                    WHEN p.active_confirmed_core = 1 THEN 'active_confirmed_core'
                    ELSE 'inactive_or_non_core'
                END AS scope,
                p.paper_id,
                COALESCE((
                    SELECT GROUP_CONCAT(module_code, '+')
                    FROM (
                        SELECT DISTINCT value AS module_code
                        FROM json_each(p.scientific_object_modules_json)
                        ORDER BY module_code
                    )
                ), '') AS canonical_module_combo,
                json_array_length(p.scientific_object_modules_json) AS module_count,
                p.pdf_exists,
                p.note_exists,
                CASE WHEN lower(trim(COALESCE(p.source_limited, ''))) LIKE 'yes%' THEN 1 ELSE 0 END AS source_limited_flag
            FROM papers p
            WHERE p.object_coverage_mode = 'multi_module'
        )
        SELECT
            scope,
            module_count,
            canonical_module_combo,
            COUNT(*) AS paper_count,
            SUM(pdf_exists) AS local_pdf_count,
            SUM(note_exists) AS note_count,
            SUM(source_limited_flag) AS source_limited_count
        FROM combos
        GROUP BY scope, module_count, canonical_module_combo;
        CREATE VIEW canonical_formal_module_pdf_coverage_summary AS
        SELECT
            pm.module_code,
            COUNT(*) AS total_assignment_count,
            SUM(CASE WHEN p.active_confirmed_core = 1 THEN 1 ELSE 0 END) AS active_assignment_count,
            SUM(CASE WHEN p.active_confirmed_core = 1 AND p.pdf_exists = 1 THEN 1 ELSE 0 END) AS active_local_pdf_count,
            SUM(CASE WHEN p.active_confirmed_core = 1 AND p.pdf_exists = 0 THEN 1 ELSE 0 END) AS active_missing_local_pdf_count,
            SUM(CASE WHEN p.active_confirmed_core = 1 AND p.note_exists = 1 THEN 1 ELSE 0 END) AS active_note_count,
            SUM(CASE WHEN p.active_confirmed_core = 1 AND p.note_exists = 0 THEN 1 ELSE 0 END) AS active_missing_note_count,
            SUM(CASE WHEN p.active_confirmed_core = 1 AND lower(trim(COALESCE(p.source_limited, ''))) LIKE 'yes%' THEN 1 ELSE 0 END) AS active_source_limited_count,
            CASE
                WHEN SUM(CASE WHEN p.active_confirmed_core = 1 THEN 1 ELSE 0 END) = 0 THEN 0.0
                ELSE ROUND(
                    100.0 * SUM(CASE WHEN p.active_confirmed_core = 1 AND p.pdf_exists = 1 THEN 1 ELSE 0 END)
                    / SUM(CASE WHEN p.active_confirmed_core = 1 THEN 1 ELSE 0 END),
                    2
                )
            END AS active_local_pdf_coverage_rate
        FROM canonical_paper_modules pm
        JOIN papers p ON p.paper_id = pm.paper_id
        GROUP BY pm.module_code;
        CREATE VIEW canonical_bucket_0104_papers AS
        SELECT *
        FROM papers
        WHERE lower(trim(COALESCE(general_method_bucket, ''))) LIKE '01.04%';
        CREATE VIEW canonical_bucket_0104_summary AS
        SELECT
            '01.04' AS general_method_bucket_code,
            COUNT(*) AS total_paper_count,
            SUM(active_confirmed_core) AS active_confirmed_core_count,
            SUM(CASE WHEN active_confirmed_core = 1 AND pdf_exists = 1 THEN 1 ELSE 0 END) AS active_local_pdf_count,
            SUM(CASE WHEN active_confirmed_core = 1 AND pdf_exists = 0 THEN 1 ELSE 0 END) AS active_missing_local_pdf_count,
            SUM(CASE WHEN active_confirmed_core = 1 AND note_exists = 1 THEN 1 ELSE 0 END) AS active_note_count,
            SUM(CASE WHEN active_confirmed_core = 1 AND note_exists = 0 THEN 1 ELSE 0 END) AS active_missing_note_count,
            SUM(CASE WHEN active_confirmed_core = 1 AND lower(trim(COALESCE(source_limited, ''))) LIKE 'yes%' THEN 1 ELSE 0 END) AS active_source_limited_count
        FROM canonical_bucket_0104_papers;
        CREATE VIEW canonical_analysis_baseline AS
        WITH active_papers AS (
            SELECT *
            FROM papers
            WHERE active_confirmed_core = 1
        ),
        formal_assignment_counts AS (
            SELECT COUNT(*) AS active_formal_module_assignment_count
            FROM canonical_paper_modules pm
            JOIN active_papers p ON p.paper_id = pm.paper_id
        ),
        record_counts AS (
            SELECT
                COUNT(*) AS active_confirmed_core_record_count,
                SUM(CASE WHEN json_array_length(scientific_object_modules_json) > 0 THEN 1 ELSE 0 END) AS active_records_with_formal_modules_count,
                SUM(CASE WHEN lower(trim(COALESCE(general_method_bucket, ''))) LIKE '01.04%' THEN 1 ELSE 0 END) AS active_general_method_bucket_record_count,
                SUM(CASE WHEN object_coverage_mode = 'single_module' THEN 1 ELSE 0 END) AS active_single_module_record_count,
                SUM(CASE WHEN object_coverage_mode = 'multi_module' THEN 1 ELSE 0 END) AS active_multi_module_record_count,
                SUM(CASE WHEN object_coverage_mode = 'general_method_without_concrete_object_experiments' THEN 1 ELSE 0 END) AS active_general_method_record_count
            FROM active_papers
        )
        SELECT
            r.active_confirmed_core_record_count,
            r.active_records_with_formal_modules_count,
            r.active_general_method_bucket_record_count,
            r.active_single_module_record_count,
            r.active_multi_module_record_count,
            r.active_general_method_record_count,
            r.active_single_module_record_count + r.active_general_method_record_count AS active_single_or_general_record_count,
            f.active_formal_module_assignment_count,
            r.active_general_method_bucket_record_count AS active_general_method_bucket_assignment_count,
            f.active_formal_module_assignment_count + r.active_general_method_bucket_record_count AS active_total_canonical_assignment_count
        FROM record_counts r
        CROSS JOIN formal_assignment_counts f;
        CREATE VIEW coverage_status_analysis AS
        WITH normalized AS (
            SELECT
                p.*,
                CASE
                    WHEN lower(trim(COALESCE(p.source_limited, ''))) LIKE 'yes%' THEN 1
                    ELSE 0
                END AS source_limited_flag
            FROM papers p
        )
        SELECT
            paper_id,
            title,
            year,
            source,
            active_confirmed_core,
            pdf_exists,
            note_exists,
            source_limited,
            source_limited_flag,
            pdf_status,
            evidence_status,
            note_status,
            CASE
                WHEN active_confirmed_core = 0 THEN 'inactive_or_non_core'
                WHEN pdf_exists = 1 AND note_exists = 1 AND source_limited_flag = 1 THEN 'active_complete_source_limited'
                WHEN pdf_exists = 1 AND note_exists = 1 THEN 'active_complete_local'
                WHEN pdf_exists = 1 AND note_exists = 0 THEN 'active_pdf_only'
                WHEN pdf_exists = 0 AND note_exists = 1 THEN 'active_note_only'
                ELSE 'active_missing_pdf_and_note'
            END AS coverage_state,
            CASE WHEN active_confirmed_core = 1 AND pdf_exists = 0 THEN 1 ELSE 0 END AS needs_local_pdf,
            CASE WHEN active_confirmed_core = 1 AND note_exists = 0 THEN 1 ELSE 0 END AS needs_note,
            CASE
                WHEN active_confirmed_core = 1 AND (pdf_exists = 0 OR note_exists = 0 OR source_limited_flag = 1) THEN 1
                ELSE 0
            END AS needs_followup
        FROM normalized;
        CREATE VIEW coverage_status_summary AS
        SELECT
            active_confirmed_core,
            coverage_state,
            COUNT(*) AS paper_count,
            SUM(pdf_exists) AS local_pdf_count,
            SUM(note_exists) AS local_note_count,
            SUM(source_limited_flag) AS source_limited_count,
            SUM(needs_local_pdf) AS missing_local_pdf_count,
            SUM(needs_note) AS missing_note_count,
            SUM(needs_followup) AS needs_followup_count
        FROM coverage_status_analysis
        GROUP BY active_confirmed_core, coverage_state;
        CREATE VIEW classification_boundary_analysis AS
        WITH normalized AS (
            SELECT
                p.*,
                CASE
                    WHEN trim(COALESCE(p.general_method_bucket, '')) = '' THEN 'none'
                    WHEN lower(trim(p.general_method_bucket)) LIKE '01.04%' THEN '01.04'
                    WHEN lower(trim(p.general_method_bucket)) LIKE 'none%' THEN 'none'
                    ELSE trim(p.general_method_bucket)
                END AS normalized_general_method_bucket,
                COALESCE((
                    SELECT GROUP_CONCAT(module_code, ';')
                    FROM (
                        SELECT value AS module_code, CAST(key AS INTEGER) AS sort_key
                        FROM json_each(p.scientific_object_modules_json)
                        ORDER BY sort_key
                    )
                ), '') AS scientific_modules_declared_order,
                COALESCE((
                    SELECT GROUP_CONCAT(module_code, ';')
                    FROM (
                        SELECT DISTINCT value AS module_code
                        FROM json_each(p.scientific_object_modules_json)
                        ORDER BY module_code
                    )
                ), '') AS scientific_modules_canonical,
                COALESCE((
                    SELECT GROUP_CONCAT(module_code, ';')
                    FROM (
                        SELECT value AS module_code, CAST(key AS INTEGER) AS sort_key
                        FROM json_each(p.final_modules_or_bucket_json)
                        WHERE value <> '01.04'
                        ORDER BY sort_key
                    )
                ), '') AS final_formal_modules_declared_order,
                COALESCE((
                    SELECT GROUP_CONCAT(module_code, ';')
                    FROM (
                        SELECT DISTINCT value AS module_code
                        FROM json_each(p.final_modules_or_bucket_json)
                        ORDER BY module_code
                    )
                ), '') AS final_assignments_canonical,
                COALESCE((
                    SELECT GROUP_CONCAT(module_code, ';')
                    FROM (
                        SELECT DISTINCT value AS module_code
                        FROM json_each(p.final_modules_or_bucket_json)
                        WHERE value <> '01.04'
                        ORDER BY module_code
                    )
                ), '') AS final_formal_modules_canonical,
                json_array_length(p.scientific_object_modules_json) AS scientific_module_count,
                json_array_length(p.final_modules_or_bucket_json) AS final_assignment_count,
                COALESCE((
                    SELECT COUNT(*)
                    FROM json_each(p.final_modules_or_bucket_json)
                    WHERE value <> '01.04'
                ), 0) AS final_formal_module_count,
                CASE
                    WHEN EXISTS (
                        SELECT 1
                        FROM json_each(p.final_modules_or_bucket_json)
                        WHERE value = '01.04'
                    ) THEN 1
                    ELSE 0
                END AS final_contains_bucket_0104,
                CASE
                    WHEN EXISTS (
                        SELECT 1
                        FROM json_each(p.final_modules_or_bucket_json)
                        WHERE value <> '01.04'
                    ) THEN 1
                    ELSE 0
                END AS final_contains_formal_modules
            FROM papers p
        )
        SELECT
            paper_id,
            title,
            year,
            source,
            active_confirmed_core,
            scientific_object_modules_json,
            scientific_modules_declared_order,
            scientific_modules_canonical,
            scientific_module_count,
            general_method_bucket AS general_method_bucket_raw,
            normalized_general_method_bucket,
            final_modules_or_bucket_raw,
            final_modules_or_bucket_json,
            final_formal_modules_declared_order,
            final_assignments_canonical,
            final_formal_modules_canonical,
            final_assignment_count,
            final_formal_module_count,
            CASE WHEN normalized_general_method_bucket = '01.04' THEN 1 ELSE 0 END AS has_general_method_bucket,
            final_contains_bucket_0104,
            final_contains_formal_modules,
            CASE
                WHEN scientific_modules_canonical = final_formal_modules_canonical THEN 1
                ELSE 0
            END AS scientific_matches_final_formal_modules,
            CASE
                WHEN scientific_modules_declared_order = final_formal_modules_declared_order THEN 1
                ELSE 0
            END AS scientific_matches_final_formal_order,
            CASE
                WHEN normalized_general_method_bucket NOT IN ('none', '01.04') THEN 'dirty_general_method_bucket'
                WHEN final_contains_bucket_0104 = 1 AND final_contains_formal_modules = 1 THEN 'mixed_final_bucket_and_formal_modules'
                WHEN normalized_general_method_bucket = '01.04' AND final_contains_bucket_0104 = 1 AND scientific_module_count = 0 AND final_formal_module_count = 0 THEN 'acceptable_mirror'
                WHEN normalized_general_method_bucket = '01.04' AND final_contains_bucket_0104 = 0 AND final_formal_module_count > 0 THEN 'bucket_replaced_by_formal_modules'
                WHEN normalized_general_method_bucket = 'none' AND final_contains_bucket_0104 = 1 THEN 'bucket_added_in_final'
                WHEN scientific_module_count = 0 AND final_formal_module_count > 0 THEN 'final_formal_without_scientific_modules'
                WHEN scientific_module_count > 0 AND final_formal_module_count = 0 AND final_contains_bucket_0104 = 0 THEN 'scientific_modules_missing_in_final'
                WHEN scientific_module_count > 0 AND scientific_modules_canonical <> final_formal_modules_canonical THEN 'final_formal_differs_from_scientific_modules'
                WHEN scientific_module_count > 0 AND scientific_modules_declared_order <> final_formal_modules_declared_order THEN 'formal_module_order_drift'
                ELSE 'aligned'
            END AS boundary_case_kind,
            CASE
                WHEN normalized_general_method_bucket NOT IN ('none', '01.04') THEN 'semantic_drift'
                WHEN final_contains_bucket_0104 = 1 AND final_contains_formal_modules = 1 THEN 'semantic_drift'
                WHEN normalized_general_method_bucket = '01.04' AND final_contains_bucket_0104 = 1 AND scientific_module_count = 0 AND final_formal_module_count = 0 THEN 'acceptable_mirror'
                WHEN normalized_general_method_bucket = '01.04' AND final_contains_bucket_0104 = 0 AND final_formal_module_count > 0 THEN 'semantic_drift'
                WHEN normalized_general_method_bucket = 'none' AND final_contains_bucket_0104 = 1 THEN 'semantic_drift'
                WHEN scientific_module_count = 0 AND final_formal_module_count > 0 THEN 'semantic_drift'
                WHEN scientific_module_count > 0 AND final_formal_module_count = 0 AND final_contains_bucket_0104 = 0 THEN 'semantic_drift'
                WHEN scientific_module_count > 0 AND scientific_modules_canonical <> final_formal_modules_canonical THEN 'semantic_drift'
                WHEN scientific_module_count > 0 AND scientific_modules_declared_order <> final_formal_modules_declared_order THEN 'order_drift'
                ELSE 'aligned'
            END AS drift_class
        FROM normalized;
        CREATE VIEW classification_boundary_summary AS
        SELECT
            active_confirmed_core,
            drift_class,
            boundary_case_kind,
            COUNT(*) AS paper_count,
            SUM(has_general_method_bucket) AS general_bucket_count,
            SUM(final_contains_bucket_0104) AS final_bucket_count,
            SUM(final_contains_formal_modules) AS final_formal_count
        FROM classification_boundary_analysis
        GROUP BY active_confirmed_core, drift_class, boundary_case_kind;
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
        conn.executemany(
            'INSERT INTO analysis_object_scope_registry(object_name, object_type, scope_class, default_usage, warning) VALUES(?, ?, ?, ?, ?)',
            [
                (
                    'change_log',
                    'table',
                    'audit_owner',
                    'change audit lookup',
                    'Lightweight audit trail loaded from Data/change_log.jsonl for change history and maintenance review.',
                ),
                (
                    'classification_terms',
                    'table',
                    'taxonomy_owner_snapshot',
                    'default taxonomy term lookup',
                    'Normalized taxonomy owner snapshot built from Data/classification_code_index.json.',
                ),
                (
                    'discipline_code_assignments',
                    'table',
                    'owner_snapshot',
                    'management-code owner inspection',
                    'Stable discipline code assignment owner table loaded from Data/discipline_code_assignments.jsonl; changes must originate in the owner file, not SQLite.',
                ),
                (
                    'paper_general_method_buckets',
                    'table',
                    'canonical_only',
                    'default 01.04 bucket lookup',
                    'One-row-per-paper canonical general-method bucket table; empty for non-bucket papers.',
                ),
                (
                    'discipline_local_code_registry',
                    'table',
                    'derived_snapshot',
                    'default discipline filing review',
                    'Derived one-row-per-ledger-entry snapshot joining assignment owner data with paper facts; rebuild from export instead of editing in SQLite.',
                ),
                (
                    'pdf_evidence_status',
                    'table',
                    'workflow_status',
                    'default PDF/source status lookup',
                    'Per-paper PDF/source evidence table derived from the authoritative paper/progress lane.',
                ),
                (
                    'paper_assets',
                    'table',
                    'derived_snapshot',
                    'default note/PDF asset lookup',
                    'Per-asset snapshot loaded from Data/registry/asset_manifest.jsonl.',
                ),
                (
                    'notes',
                    'table',
                    'derived_snapshot',
                    'default note inventory lookup',
                    'Per-paper note snapshot loaded from Data/note_manifest.json.',
                ),
                (
                    'papers',
                    'table',
                    'mixed_with_workflow_fields',
                    'record inspection only',
                    'Contains canonical classification fields plus workflow mirror/status columns; do not treat final_modules_or_bucket as canonical classification.',
                ),
                (
                    'paper_modules',
                    'table',
                    'mixed_scope',
                    'compatibility inspection only',
                    'Contains both canonical scientific_object_modules and workflow final_modules_or_bucket rows; filter assignment_scope before aggregation.',
                ),
                (
                    'mixed_scope_paper_modules',
                    'view',
                    'mixed_scope',
                    'compatibility inspection only',
                    'Alias view naming the mixed-scope nature explicitly; prefer canonical_paper_modules or workflow_mirror_paper_modules for analysis.',
                ),
                (
                    'canonical_paper_modules',
                    'view',
                    'canonical_only',
                    'default formal-module analysis',
                    'Canonical-only formal 01-11 assignments for default statistics.',
                ),
                (
                    'workflow_mirror_paper_modules',
                    'view',
                    'workflow_mirror_only',
                    'audit only',
                    'Workflow mirror assignments for audit/debugging only, not default statistics.',
                ),
                (
                    'module_assignment_counts',
                    'view',
                    'mixed_scope',
                    'compatibility inspection only',
                    'Mixed-scope counts across canonical and workflow mirror assignments; not a default canonical summary.',
                ),
                (
                    'mixed_scope_module_assignment_counts',
                    'view',
                    'mixed_scope',
                    'compatibility inspection only',
                    'Alias view naming the mixed-scope nature explicitly; prefer canonical_module_assignment_counts or workflow_mirror_module_assignment_counts.',
                ),
                (
                    'canonical_module_assignment_counts',
                    'view',
                    'canonical_only',
                    'default formal-module analysis',
                    'Canonical-only formal-module assignment counts for default statistics.',
                ),
                (
                    'workflow_mirror_module_assignment_counts',
                    'view',
                    'workflow_mirror_only',
                    'audit only',
                    'Workflow mirror assignment counts for audit/debugging only.',
                ),
                (
                    'canonical_analysis_baseline',
                    'view',
                    'canonical_only',
                    'default baseline glossary',
                    'Use together with summary before writing module statistics.',
                ),
                (
                    'classification_boundary_analysis',
                    'view',
                    'audit_only',
                    'drift inspection only',
                    'Canonical-vs-mirror inspection view; not a default classification summary.',
                ),
                (
                    'classification_boundary_summary',
                    'view',
                    'audit_only',
                    'drift inspection only',
                    'Boundary/drift summary; not a default classification count.',
                ),
                (
                    'canonical_bucket_0104_summary',
                    'view',
                    'canonical_only',
                    'default 01.04 bucket analysis',
                    'Separate canonical 01.04 bucket summary; do not merge into formal 01-11 counts.',
                ),
                (
                    'coverage_status_analysis',
                    'view',
                    'workflow_status',
                    'coverage follow-up analysis',
                    'Coverage/progress analysis, not canonical classification counting.',
                ),
                (
                    'coverage_status_summary',
                    'view',
                    'workflow_status',
                    'coverage follow-up analysis',
                    'Coverage/progress summary, not canonical classification counting.',
                ),
            ],
        )
        conn.executemany('INSERT INTO taxonomy_index(code, label, kind) VALUES(?, ?, ?)', [
            (code, label, 'formal_module' if code in FORMAL_MODULES else 'general_bucket')
            for code, label in taxonomy['code_to_label'].items()
        ])
        classification_term_rows = build_classification_term_rows(classification_code_index)
        change_log_rows = load_jsonl(CHANGE_LOG_JSONL) if CHANGE_LOG_JSONL.exists() else []
        conn.executemany('INSERT INTO change_log VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', [
            (
                row['change_id'],
                row['paper_id'],
                row['changed_at'],
                row['changed_by'],
                row['change_type'],
                json.dumps(row.get('old_value'), ensure_ascii=False),
                json.dumps(row.get('new_value'), ensure_ascii=False),
                row['reason'],
                row.get('related_commit'),
            )
            for row in change_log_rows
        ])
        conn.executemany('INSERT INTO classification_terms VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [
            (
                row['taxonomy_code'],
                row['term_level'],
                row['parent_primary_code'],
                row['label'],
                row['definition'],
                row['include_json'],
                row['exclude_json'],
                row['status'],
                row['source'],
                row['review_status'],
            )
            for row in classification_term_rows
        ])
        conn.executemany('INSERT INTO papers VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [
            (
                paper['paper_id'], paper['title'], paper['authors'], paper['year'], paper['source'], paper['doi_or_url'], paper['doi'], paper['url'], paper['arxiv_id'],
                paper['pdf_path'], bool_to_int(paper['pdf_exists']), paper['note_path'], bool_to_int(paper['note_exists']), paper['is_agent'], paper['inclusion_status'], paper['exclusion_reason'],
                paper['legacy_main_class'], paper['legacy_secondary_class'], paper['legacy_tertiary_class'], paper['fourth_level_topic'], paper['new_fourth_level'],
                json_list(paper['agent_type']), json_list(paper['research_workflow_role']), json_list(paper['validation_type']), json_list(paper['scientific_contribution_type']),
                paper['evidence_strength'], paper['citation_priority'], paper['remarks'], json_list(paper['scientific_object_modules']), paper['general_method_bucket'], paper['object_coverage_mode'],
                paper['primary_module_for_filing'], paper['first_hand_sources_checked'], paper['progress_title'], paper['pdf_status'], paper['evidence_status'], paper['note_status'], paper['master_status'],
                paper['final_modules_or_bucket_raw'], json_list(paper['final_modules_or_bucket']), paper['source_limited'], paper['batch'], paper['closed'], bool_to_int(paper['active_confirmed_core']),
                paper['record_status'], paper['inclusion_decision'], paper['duplicate_of'], paper['last_reviewed_at'], paper['last_reviewed_by'], paper['exported_at'],
            )
            for paper in papers
        ])
        conn.executemany('INSERT INTO paper_modules(paper_id, assignment_scope, module_code, module_kind, sort_order) VALUES(?, ?, ?, ?, ?)', [
            (row['paper_id'], row['assignment_scope'], row['module_code'], row['module_kind'], row['sort_order'])
            for row in module_rows
        ])
        general_method_bucket_rows = build_general_method_bucket_rows(papers)
        conn.executemany('INSERT INTO paper_general_method_buckets VALUES(?, ?, ?, ?)', [
            (
                row['paper_id'],
                row['general_method_bucket'],
                row['active_confirmed_core'],
                row['source_limited'],
            )
            for row in general_method_bucket_rows
        ])
        conn.executemany('INSERT INTO discipline_code_assignments VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [
            (
                row['assignment_id'],
                row['paper_id'],
                row['discipline_local_code'],
                row['primary_taxonomy_code_2lvl'],
                row['assignment_status'],
                row['assigned_at'],
                row['assigned_by'],
                row['retired_at'],
                row['redirected_to_code'],
                row['assignment_reason'],
                row['pending_reason'],
                row['source_primary_module_for_filing'],
                row['source_legacy_secondary_class'],
                row['schema_version'],
            )
            for row in discipline_code_assignments
        ])
        conn.executemany('INSERT INTO discipline_local_code_registry VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [
            (
                row['paper_id'],
                row['assignment_id'],
                row['discipline_local_code'],
                row['discipline_local_rank'],
                row['assignment_status'],
                row['assigned_at'],
                row['assigned_by'],
                row['retired_at'],
                row['redirected_to_code'],
                row['assignment_reason'],
                row['pending_reason'],
                row['primary_module_for_filing'],
                row['primary_taxonomy_code_2lvl'],
                row['legacy_secondary_class'],
                json_list(row['scientific_object_modules']),
                row['general_method_bucket'],
                row['title'],
                row['note_path'],
                row['pdf_path'],
                bool_to_int(row['active_confirmed_core']),
                bool_to_int(row['is_derived_snapshot']),
                row['generated_at'],
                row['generated_by'],
                row['source_commit'],
                bool_to_int(row['worktree_dirty']),
            )
            for row in discipline_local_code_registry
        ])
        conn.executemany('INSERT INTO pdf_evidence_status VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', [
            (
                row['paper_id'],
                row['title'],
                row['pdf_path'],
                bool_to_int(row['pdf_exists']),
                row['pdf_status'],
                row['evidence_status'],
                row['source_limited'],
                row['primary_module_for_filing'],
                bool_to_int(row['active_confirmed_core']),
            )
            for row in pdf_archive_registry
        ])
        conn.executemany('INSERT INTO paper_assets VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [
            (
                row['asset_id'],
                row['paper_id'],
                row['title'],
                row['asset_type'],
                row['path'],
                bool_to_int(row['exists']),
                row['sha256'],
                row['asset_status'],
                row['source_limited'],
                row['exported_at'],
            )
            for row in asset_manifest
        ])
        conn.executemany('INSERT INTO notes VALUES(?, ?, ?, ?, ?, ?)', [
            (
                row['paper_id'],
                row['title'],
                row['note_path'],
                bool_to_int(row['note_exists']),
                bool_to_int(row['active_confirmed_core']),
                row['inclusion_status'],
            )
            for row in note_manifest
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
    classification_code_index = load_json(CLASSIFICATION_CODE_INDEX_JSON)
    pdf_manifest = load_json(PDF_MANIFEST_JSON)
    missing_pdf_manifest = load_json(MISSING_PDF_JSON)
    note_manifest = load_json(NOTE_MANIFEST_JSON)
    discipline_code_assignments = load_jsonl(DISCIPLINE_CODE_ASSIGNMENTS_JSONL)
    discipline_local_code_registry = load_jsonl(DISCIPLINE_LOCAL_CODE_REGISTRY_JSONL)
    asset_manifest = load_jsonl(ASSET_MANIFEST_JSONL)
    pdf_archive_registry = load_jsonl(PDF_ARCHIVE_REGISTRY_JSONL)
    module_rows = build_module_rows(papers)
    write_papers_csv(papers)
    write_module_csv(module_rows)
    write_discipline_local_code_registry_csv(discipline_local_code_registry)
    build_sqlite(
        papers,
        taxonomy,
        classification_code_index,
        pdf_manifest,
        missing_pdf_manifest,
        note_manifest,
        module_rows,
        discipline_code_assignments,
        discipline_local_code_registry,
        asset_manifest,
        pdf_archive_registry,
    )
    print(f'Wrote {PAPERS_CSV}')
    print(f'Wrote {PAPER_MODULES_CSV}')
    print(f'Wrote {CANONICAL_PAPER_MODULES_CSV}')
    print(f'Wrote {WORKFLOW_MIRROR_PAPER_MODULES_CSV}')
    print(f'Wrote {DISCIPLINE_LOCAL_CODE_REGISTRY_CSV}')
    print(f'Wrote {SQLITE_PATH}')
    print(f'papers rows: {len(papers)}')
    print(f'paper_modules rows: {len(module_rows)}')
    print(f'discipline_code_assignments rows: {len(discipline_code_assignments)}')
    print(f'discipline_local_code_registry rows: {len(discipline_local_code_registry)}')

if __name__ == '__main__':
    main()
