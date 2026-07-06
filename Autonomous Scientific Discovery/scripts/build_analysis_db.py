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
MIXED_SCOPE_PAPER_MODULES_CSV = DATA_DIR / 'mixed_scope_paper_modules.csv'
DISCIPLINE_LOCAL_CODE_REGISTRY_CSV = DATA_DIR / 'discipline_local_code_registry.csv'
SQLITE_PATH = DATA_DIR / 'papers.sqlite'
OWNER_GUARDED_PATHS = {
    CLASSIFICATION_CODE_INDEX_JSON.resolve(),
    CHANGE_LOG_JSONL.resolve(),
    DISCIPLINE_CODE_ASSIGNMENTS_JSONL.resolve(),
}
FORMAL_MODULES = {f'{idx:02d}' for idx in range(1, 12)}
MODULE_ROW_FIELDNAMES = [
    'paper_id', 'title', 'assignment_scope', 'module_code', 'module_kind', 'sort_order',
    'is_primary_for_filing', 'confidence', 'source', 'active_confirmed_core'
]
CSV_FIELDS = [
    'paper_id', 'title', 'authors', 'year', 'source', 'doi_or_url', 'doi', 'url', 'arxiv_id',
    'pdf_path', 'pdf_exists', 'note_path', 'note_exists', 'is_agent', 'inclusion_status',
    'exclusion_reason', 'legacy_main_class', 'legacy_secondary_class', 'legacy_tertiary_class',
    'secondary_class_source', 'secondary_class_confidence', 'secondary_class_review_status',
    'fourth_level_topic', 'new_fourth_level', 'agent_type', 'research_workflow_role',
    'validation_type', 'scientific_contribution_type', 'evidence_strength', 'citation_priority',
    'scientific_object_modules', 'general_method_bucket', 'object_coverage_mode',
    'primary_module_for_filing', 'primary_module_confidence', 'primary_module_assignment_rule',
    'primary_module_override_reason', 'classification_source_field', 'classification_source_confidence',
    'classification_parser_rule', 'first_hand_sources_checked', 'source_checked_at', 'progress_title', 'pdf_status',
    'evidence_status', 'note_status', 'master_status', 'final_modules_or_bucket',
    'source_limited', 'batch', 'closed', 'active_confirmed_core', 'record_status',
    'inclusion_decision', 'duplicate_of', 'last_reviewed_at', 'last_reviewed_by', 'exported_at',
]
DISCIPLINE_LOCAL_CODE_REGISTRY_FIELDS = [
    'paper_id', 'assignment_id', 'discipline_local_code', 'discipline_local_rank', 'discipline_display_order',
    'assignment_status', 'assigned_at', 'assigned_by', 'retired_at', 'redirected_to_code',
    'assignment_reason', 'pending_reason', 'primary_module_for_filing',
    'primary_module_confidence', 'primary_module_assignment_rule', 'primary_module_override_reason',
    'primary_taxonomy_code_2lvl', 'legacy_secondary_class', 'secondary_class_source', 'secondary_class_confidence', 'secondary_class_review_status', 'scientific_object_modules',
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

def blank_to_none(value: object) -> object:
    if value is None:
        return None
    if isinstance(value, str) and not value.strip():
        return None
    return value

def flatten_list(value: object) -> str:
    if isinstance(value, list):
        return ';'.join(str(item) for item in value)
    return '' if value is None else str(value)

def json_list(value: object) -> str:
    return json.dumps(value if isinstance(value, list) else [], ensure_ascii=False)

def assert_safe_output_paths(paths: list[Path]) -> None:
    conflicts = sorted(
        str(path.resolve().relative_to(ROOT))
        for path in paths
        if path.resolve() in OWNER_GUARDED_PATHS
    )
    if conflicts:
        raise RuntimeError(
            'build_analysis_db.py attempted to write owner fact source paths: '
            + ', '.join(conflicts)
        )

def assert_build_condition(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)

def write_papers_csv(papers: list[dict[str, object]]) -> None:
    with PAPERS_CSV.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for paper in papers:
            writer.writerow({field: flatten_list(paper.get(field)) for field in CSV_FIELDS})

def normalize_papers_csv_row(paper: dict[str, object]) -> dict[str, str]:
    return {field: flatten_list(paper.get(field)) for field in CSV_FIELDS}

def build_expected_papers_sqlite_rows(
    papers: list[dict[str, object]]
) -> list[tuple[object, ...]]:
    return sorted(
        [
            (
                paper['paper_id'], paper['title'], paper['authors'], paper['year'], paper['source'], paper['doi_or_url'], paper['doi'], paper['url'], paper['arxiv_id'],
                paper['pdf_path'], bool_to_int(paper['pdf_exists']), paper['note_path'], bool_to_int(paper['note_exists']), paper['is_agent'], paper['inclusion_status'], paper['exclusion_reason'],
                paper['legacy_main_class'], paper['legacy_secondary_class'], paper['legacy_tertiary_class'], paper['secondary_class_source'], paper['secondary_class_confidence'], paper['secondary_class_review_status'], paper['fourth_level_topic'], paper['new_fourth_level'],
                json_list(paper['agent_type']), json_list(paper['research_workflow_role']), json_list(paper['validation_type']), json_list(paper['scientific_contribution_type']),
                paper['evidence_strength'], paper['citation_priority'], paper['remarks'], json_list(paper['scientific_object_modules']), paper['general_method_bucket'], paper['object_coverage_mode'],
                blank_to_none(paper['primary_module_for_filing']), paper['primary_module_confidence'], paper['primary_module_assignment_rule'], paper['primary_module_override_reason'],
                paper['classification_source_field'], paper['classification_source_confidence'], paper['classification_parser_rule'],
                paper['first_hand_sources_checked'], paper['source_checked_at'], paper['progress_title'], paper['pdf_status'], paper['evidence_status'], paper['note_status'], paper['master_status'],
                paper['final_modules_or_bucket_raw'], json_list(paper['final_modules_or_bucket']), paper['source_limited'], paper['batch'], paper['closed'], bool_to_int(paper['active_confirmed_core']),
                paper['record_status'], paper['inclusion_decision'], blank_to_none(paper['duplicate_of']), paper['last_reviewed_at'], paper['last_reviewed_by'], paper['exported_at'],
            )
            for paper in papers
        ],
        key=lambda item: item[0],
    )

def validate_papers_outputs(papers: list[dict[str, object]]) -> None:
    expected_csv_rows = [normalize_papers_csv_row(paper) for paper in papers]
    actual_csv_rows = load_csv_rows(PAPERS_CSV)
    assert_build_condition(
        actual_csv_rows == expected_csv_rows,
        'papers.csv drifted from expected papers.jsonl snapshot rows',
    )

    expected_sqlite_rows = build_expected_papers_sqlite_rows(papers)
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        actual_sqlite_rows = conn.execute(
            '''
            SELECT
                paper_id, title, authors, year, source, doi_or_url, doi, url, arxiv_id,
                pdf_path, pdf_exists, note_path, note_exists, is_agent, inclusion_status, exclusion_reason,
                legacy_main_class, legacy_secondary_class, legacy_tertiary_class, secondary_class_source, secondary_class_confidence, secondary_class_review_status, fourth_level_topic, new_fourth_level,
                agent_type_json, research_workflow_role_json, validation_type_json, scientific_contribution_type_json,
                evidence_strength, citation_priority, remarks, scientific_object_modules_json, general_method_bucket, object_coverage_mode,
                primary_module_for_filing, primary_module_confidence, primary_module_assignment_rule, primary_module_override_reason,
                classification_source_field, classification_source_confidence, classification_parser_rule,
                first_hand_sources_checked, source_checked_at, progress_title, pdf_status, evidence_status, note_status, master_status,
                final_modules_or_bucket_raw, final_modules_or_bucket_json, source_limited, batch, closed, active_confirmed_core,
                record_status, inclusion_decision, duplicate_of, last_reviewed_at, last_reviewed_by, exported_at
            FROM papers
            ORDER BY paper_id
            '''
        ).fetchall()
        general_method_semantic_violations = conn.execute(
            '''
            SELECT COUNT(*)
            FROM papers
            WHERE
                (
                    general_method_bucket = '01.04_general_asd_methods_without_concrete_object_experiments'
                    AND NOT (
                        scientific_object_modules_json = '[]'
                        AND object_coverage_mode = 'general_method_without_concrete_object_experiments'
                        AND primary_module_for_filing IS NULL
                    )
                )
                OR (
                    object_coverage_mode = 'general_method_without_concrete_object_experiments'
                    AND NOT (
                        general_method_bucket = '01.04_general_asd_methods_without_concrete_object_experiments'
                        AND scientific_object_modules_json = '[]'
                        AND primary_module_for_filing IS NULL
                    )
                )
            '''
        ).fetchone()[0]
    finally:
        conn.close()
    assert_build_condition(
        actual_sqlite_rows == expected_sqlite_rows,
        'SQLite papers table drifted from expected papers.jsonl snapshot rows',
    )
    assert_build_condition(
        general_method_semantic_violations == 0,
        'SQLite papers table violated pure general-method cross-field semantics',
    )

def build_module_rows(papers: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for paper in papers:
        for scope in ('scientific_object_modules', 'final_modules_or_bucket'):
            modules = paper.get(scope, [])
            if not isinstance(modules, list):
                continue
            for sort_order, module_code in enumerate(modules, start=1):
                is_primary_for_filing = (
                    scope == 'scientific_object_modules'
                    and module_code == paper.get('primary_module_for_filing')
                )
                if scope == 'scientific_object_modules':
                    confidence = (
                        paper.get('primary_module_confidence')
                        if is_primary_for_filing
                        else paper.get('classification_source_confidence')
                    )
                    source = (
                        'primary_module_for_filing'
                        if is_primary_for_filing
                        else 'scientific_object_modules'
                    )
                else:
                    confidence = ''
                    source = 'final_modules_or_bucket'
                rows.append({
                    'paper_id': paper['paper_id'],
                    'title': paper['title'],
                    'assignment_scope': scope,
                    'module_code': module_code,
                    'module_kind': 'formal_module' if module_code in FORMAL_MODULES else 'general_bucket',
                    'sort_order': sort_order,
                    'is_primary_for_filing': bool_to_int(is_primary_for_filing),
                    'confidence': confidence or '',
                    'source': source,
                    'active_confirmed_core': bool_to_int(paper['active_confirmed_core']),
                })
    return rows

def write_module_csv(rows: list[dict[str, object]]) -> None:
    canonical_rows = [row for row in rows if row['assignment_scope'] == 'scientific_object_modules']
    workflow_rows = [row for row in rows if row['assignment_scope'] == 'final_modules_or_bucket']
    with PAPER_MODULES_CSV.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=MODULE_ROW_FIELDNAMES)
        writer.writeheader()
        writer.writerows(canonical_rows)
    with CANONICAL_PAPER_MODULES_CSV.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=MODULE_ROW_FIELDNAMES)
        writer.writeheader()
        writer.writerows(canonical_rows)
    with WORKFLOW_MIRROR_PAPER_MODULES_CSV.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=MODULE_ROW_FIELDNAMES)
        writer.writeheader()
        writer.writerows(workflow_rows)
    with MIXED_SCOPE_PAPER_MODULES_CSV.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=MODULE_ROW_FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

def normalize_module_csv_row(row: dict[str, object]) -> dict[str, str]:
    return {
        field: flatten_list(row.get(field))
        for field in MODULE_ROW_FIELDNAMES
    }

def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open('r', encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))

def validate_module_csv_outputs(rows: list[dict[str, object]]) -> None:
    canonical_expected = [
        normalize_module_csv_row(row)
        for row in rows
        if row['assignment_scope'] == 'scientific_object_modules'
    ]
    workflow_expected = [
        normalize_module_csv_row(row)
        for row in rows
        if row['assignment_scope'] == 'final_modules_or_bucket'
    ]
    mixed_expected = [normalize_module_csv_row(row) for row in rows]

    paper_modules_rows = load_csv_rows(PAPER_MODULES_CSV)
    canonical_alias_rows = load_csv_rows(CANONICAL_PAPER_MODULES_CSV)
    workflow_rows = load_csv_rows(WORKFLOW_MIRROR_PAPER_MODULES_CSV)
    mixed_rows = load_csv_rows(MIXED_SCOPE_PAPER_MODULES_CSV)

    assert_build_condition(
        paper_modules_rows == canonical_expected,
        'paper_modules.csv drifted from expected canonical module rows',
    )
    assert_build_condition(
        canonical_alias_rows == canonical_expected,
        'canonical_paper_modules.csv drifted from expected canonical module rows',
    )
    assert_build_condition(
        workflow_rows == workflow_expected,
        'workflow_mirror_paper_modules.csv drifted from expected workflow-mirror module rows',
    )
    assert_build_condition(
        mixed_rows == mixed_expected,
        'mixed_scope_paper_modules.csv drifted from expected mixed-scope module rows',
    )
    assert_build_condition(
        paper_modules_rows == canonical_alias_rows,
        'paper_modules.csv and canonical_paper_modules.csv must stay identical',
    )

def validate_sqlite_module_surfaces(rows: list[dict[str, object]]) -> None:
    canonical_expected_count = sum(
        1 for row in rows if row['assignment_scope'] == 'scientific_object_modules'
    )
    workflow_expected_count = sum(
        1 for row in rows if row['assignment_scope'] == 'final_modules_or_bucket'
    )
    mixed_expected_count = len(rows)

    conn = sqlite3.connect(SQLITE_PATH)
    try:
        paper_modules_count = conn.execute(
            'SELECT COUNT(*) FROM paper_modules'
        ).fetchone()[0]
        workflow_count = conn.execute(
            'SELECT COUNT(*) FROM workflow_mirror_paper_modules'
        ).fetchone()[0]
        mixed_count = conn.execute(
            'SELECT COUNT(*) FROM mixed_scope_paper_modules'
        ).fetchone()[0]
        canonical_alias_count = conn.execute(
            'SELECT COUNT(*) FROM canonical_paper_modules'
        ).fetchone()[0]
        canonical_count_view = conn.execute(
            'SELECT COALESCE(SUM(paper_count), 0) FROM module_assignment_counts'
        ).fetchone()[0]
        canonical_alias_count_view = conn.execute(
            'SELECT COALESCE(SUM(paper_count), 0) FROM canonical_module_assignment_counts'
        ).fetchone()[0]
        workflow_count_view = conn.execute(
            'SELECT COALESCE(SUM(paper_count), 0) FROM workflow_mirror_module_assignment_counts'
        ).fetchone()[0]
        mixed_count_view = conn.execute(
            'SELECT COALESCE(SUM(paper_count), 0) FROM mixed_scope_module_assignment_counts'
        ).fetchone()[0]
        paper_module_scopes = {
            row[0]
            for row in conn.execute(
                'SELECT DISTINCT assignment_scope FROM paper_modules ORDER BY assignment_scope'
            )
        }
        canonical_non_formal_count = conn.execute(
            "SELECT COUNT(*) FROM paper_modules WHERE module_kind <> 'formal_module'"
        ).fetchone()[0]
        canonical_source_mismatch_count = conn.execute(
            """
            SELECT COUNT(*)
            FROM paper_modules
            WHERE
                (is_primary_for_filing = 1 AND source <> 'primary_module_for_filing')
                OR (is_primary_for_filing = 0 AND source <> 'scientific_object_modules')
            """
        ).fetchone()[0]
        workflow_scopes = {
            row[0]
            for row in conn.execute(
                'SELECT DISTINCT assignment_scope FROM workflow_mirror_paper_modules ORDER BY assignment_scope'
            )
        }
        mixed_scopes = {
            row[0]
            for row in conn.execute(
                'SELECT DISTINCT assignment_scope FROM mixed_scope_paper_modules ORDER BY assignment_scope'
            )
        }
    finally:
        conn.close()

    expected_mixed_scopes = set()
    if canonical_expected_count:
        expected_mixed_scopes.add('scientific_object_modules')
    if workflow_expected_count:
        expected_mixed_scopes.add('final_modules_or_bucket')

    assert_build_condition(
        paper_modules_count == canonical_expected_count,
        'SQLite paper_modules row count drifted from expected canonical module rows',
    )
    assert_build_condition(
        workflow_count == workflow_expected_count,
        'SQLite workflow_mirror_paper_modules row count drifted from expected workflow module rows',
    )
    assert_build_condition(
        mixed_count == mixed_expected_count,
        'SQLite mixed_scope_paper_modules row count drifted from expected mixed-scope module rows',
    )
    assert_build_condition(
        canonical_alias_count == canonical_expected_count,
        'SQLite canonical_paper_modules alias row count drifted from canonical module rows',
    )
    assert_build_condition(
        canonical_count_view == canonical_expected_count,
        'SQLite module_assignment_counts drifted from canonical module rows',
    )
    assert_build_condition(
        canonical_alias_count_view == canonical_expected_count,
        'SQLite canonical_module_assignment_counts drifted from canonical module rows',
    )
    assert_build_condition(
        workflow_count_view == workflow_expected_count,
        'SQLite workflow_mirror_module_assignment_counts drifted from workflow module rows',
    )
    assert_build_condition(
        mixed_count_view == mixed_expected_count,
        'SQLite mixed_scope_module_assignment_counts drifted from mixed-scope module rows',
    )
    assert_build_condition(
        paper_module_scopes
        == ({'scientific_object_modules'} if canonical_expected_count else set()),
        'SQLite paper_modules must only expose canonical scientific_object_modules rows',
    )
    assert_build_condition(
        canonical_non_formal_count == 0,
        'SQLite paper_modules must not contain general_bucket rows; 01.04 belongs in paper_general_method_buckets',
    )
    assert_build_condition(
        canonical_source_mismatch_count == 0,
        'SQLite paper_modules primary/source semantics drifted from canonical filing rules',
    )
    assert_build_condition(
        workflow_scopes
        == ({'final_modules_or_bucket'} if workflow_expected_count else set()),
        'SQLite workflow_mirror_paper_modules must only expose workflow final_modules_or_bucket rows',
    )
    assert_build_condition(
        mixed_scopes == expected_mixed_scopes,
        'SQLite mixed_scope_paper_modules must expose the union of canonical and workflow scopes',
    )

def write_discipline_local_code_registry_csv(rows: list[dict[str, object]]) -> None:
    with DISCIPLINE_LOCAL_CODE_REGISTRY_CSV.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=DISCIPLINE_LOCAL_CODE_REGISTRY_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({
                field: flatten_list(row.get(field))
                for field in DISCIPLINE_LOCAL_CODE_REGISTRY_FIELDS
            })

def normalize_discipline_local_code_registry_csv_row(
    row: dict[str, object],
) -> dict[str, str]:
    return {
        field: flatten_list(row.get(field))
        for field in DISCIPLINE_LOCAL_CODE_REGISTRY_FIELDS
    }

def validate_discipline_local_code_registry_outputs(
    rows: list[dict[str, object]]
) -> None:
    expected_csv_rows = [
        normalize_discipline_local_code_registry_csv_row(row)
        for row in rows
    ]
    csv_rows = load_csv_rows(DISCIPLINE_LOCAL_CODE_REGISTRY_CSV)
    assert_build_condition(
        csv_rows == expected_csv_rows,
        'discipline_local_code_registry.csv drifted from expected registry snapshot rows',
    )

    expected_sqlite_rows = sorted(
        [
            (
                row['paper_id'],
                row['assignment_id'],
                blank_to_none(row['discipline_local_code']),
                blank_to_none(row['discipline_local_rank']),
                row['discipline_display_order'],
                row['assignment_status'],
                row['assigned_at'],
                row['assigned_by'],
                row['retired_at'],
                row['redirected_to_code'],
                row['assignment_reason'],
                row['pending_reason'],
                blank_to_none(row['primary_module_for_filing']),
                row['primary_module_confidence'],
                row['primary_module_assignment_rule'],
                row['primary_module_override_reason'],
                blank_to_none(row['primary_taxonomy_code_2lvl']),
                row['legacy_secondary_class'],
                row['secondary_class_source'],
                row['secondary_class_confidence'],
                row['secondary_class_review_status'],
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
            for row in rows
        ],
        key=lambda item: item[0],
    )
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        actual_sqlite_rows = conn.execute(
            '''
            SELECT
                paper_id,
                assignment_id,
                discipline_local_code,
                discipline_local_rank,
                discipline_display_order,
                assignment_status,
                assigned_at,
                assigned_by,
                retired_at,
                redirected_to_code,
                assignment_reason,
                pending_reason,
                primary_module_for_filing,
                primary_module_confidence,
                primary_module_assignment_rule,
                primary_module_override_reason,
                primary_taxonomy_code_2lvl,
                legacy_secondary_class,
                secondary_class_source,
                secondary_class_confidence,
                secondary_class_review_status,
                scientific_object_modules_json,
                general_method_bucket,
                title,
                note_path,
                pdf_path,
                active_confirmed_core,
                is_derived_snapshot,
                generated_at,
                generated_by,
                source_commit,
                worktree_dirty
            FROM discipline_local_code_registry
            ORDER BY paper_id
            '''
        ).fetchall()
        semantic_violations = conn.execute(
            '''
            SELECT COUNT(*)
            FROM discipline_local_code_registry
            WHERE
                (
                    assignment_status = 'active_code'
                    AND (
                        discipline_local_rank IS NULL
                        OR discipline_local_code IS NULL
                        OR discipline_local_rank <> substr(discipline_local_code, -3)
                        OR discipline_display_order <> discipline_local_code
                    )
                )
                OR (
                    assignment_status = 'pending_secondary'
                    AND (
                        discipline_local_code IS NOT NULL
                        OR discipline_local_rank IS NOT NULL
                        OR discipline_display_order NOT LIKE '%PENDING-ASD-%'
                    )
                )
                OR (
                    assignment_status = 'non_discipline_general_method'
                    AND (
                        discipline_local_code IS NOT NULL
                        OR discipline_local_rank IS NOT NULL
                        OR discipline_display_order NOT LIKE 'GM-PENDING-ASD-%'
                    )
                )
                OR (
                    assignment_status = 'active_code'
                    AND (
                        pending_reason IS NOT NULL
                        OR retired_at IS NOT NULL
                        OR redirected_to_code IS NOT NULL
                    )
                )
                OR (
                    assignment_status = 'pending_secondary'
                    AND (
                        pending_reason IS NULL
                        OR trim(pending_reason) = ''
                        OR retired_at IS NOT NULL
                        OR redirected_to_code IS NOT NULL
                    )
                )
                OR (
                    assignment_status = 'non_discipline_general_method'
                    AND (
                        pending_reason IS NOT NULL
                        OR retired_at IS NOT NULL
                        OR redirected_to_code IS NOT NULL
                    )
                )
                OR (assigned_at NOT GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
                OR (assigned_by IS NULL OR trim(assigned_by) = '')
                OR (generated_at NOT GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T*')
                OR (generated_by <> 'export_structured_data.py')
                OR (
                    source_commit IS NULL
                    OR length(source_commit) <> 40
                    OR source_commit GLOB '*[^0-9a-f]*'
                )
            '''
        ).fetchone()[0]
    finally:
        conn.close()
    assert_build_condition(
        actual_sqlite_rows == expected_sqlite_rows,
        'SQLite discipline_local_code_registry table drifted from expected registry snapshot rows',
    )
    assert_build_condition(
        semantic_violations == 0,
        'SQLite discipline_local_code_registry violated derived rank/display-order semantics',
    )

def validate_discipline_sqlite_constraints() -> None:
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        assignment_create_sql = conn.execute(
            "SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'discipline_code_assignments'"
        ).fetchone()
        registry_create_sql = conn.execute(
            "SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'discipline_local_code_registry'"
        ).fetchone()
        index_rows = conn.execute(
            "SELECT name, sql FROM sqlite_master WHERE type = 'index' AND tbl_name = 'discipline_code_assignments'"
        ).fetchall()
        assignment_fk_rows = conn.execute(
            "PRAGMA foreign_key_list(discipline_code_assignments)"
        ).fetchall()
        registry_fk_rows = conn.execute(
            "PRAGMA foreign_key_list(discipline_local_code_registry)"
        ).fetchall()
    finally:
        conn.close()

    assignment_sql = assignment_create_sql[0] if assignment_create_sql else ''
    registry_sql = registry_create_sql[0] if registry_create_sql else ''
    normalized_assignment_sql = " ".join(assignment_sql.split())
    normalized_registry_sql = " ".join(registry_sql.split())
    index_sql_by_name = {
        str(name): str(sql or '')
        for name, sql in index_rows
    }
    assignment_fk_targets = {(str(row[2]), str(row[3]), str(row[4])) for row in assignment_fk_rows}
    registry_fk_targets = {(str(row[2]), str(row[3]), str(row[4])) for row in registry_fk_rows}

    assert_build_condition(
        "assignment_status IN (" in normalized_assignment_sql
        and "schema_version = 1" in normalized_assignment_sql
        and "redirected_to_code IS NULL" in normalized_assignment_sql,
        'discipline_code_assignments SQLite table is missing expected status/schema/redirect guardrail CHECK constraints',
    )
    assert_build_condition(
        "is_derived_snapshot = 1" in normalized_registry_sql
        and "assignment_status = 'active_code'" in normalized_registry_sql
        and "discipline_local_rank IS NULL" in normalized_registry_sql,
        'discipline_local_code_registry SQLite table is missing expected derived/current-snapshot CHECK constraints',
    )
    assert_build_condition(
        'discipline_code_assignments_active_code_unique' in index_sql_by_name
        and "WHERE assignment_status = 'active_code'" in index_sql_by_name['discipline_code_assignments_active_code_unique'],
        'discipline_code_assignments_active_code_unique partial index is missing or malformed',
    )
    assert_build_condition(
        'discipline_code_assignments_one_active_per_paper' in index_sql_by_name
        and "WHERE assignment_status = 'active_code'" in index_sql_by_name['discipline_code_assignments_one_active_per_paper'],
        'discipline_code_assignments_one_active_per_paper partial index is missing or malformed',
    )
    for fragment in (
        "assignment_id GLOB 'DCA-[0-9][0-9][0-9][0-9][0-9][0-9]'",
        "assigned_at GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'",
        "retired_at IS NULL OR retired_at GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'",
        "trim(assigned_by) <> ''",
        "trim(assignment_reason) <> ''",
        "assignment_status NOT IN ('active_code', 'retired_code', 'redirected_code') OR pending_reason IS NULL",
        "assignment_status <> 'redirected_code' OR redirected_to_code GLOB '[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9]'",
        "source_legacy_secondary_class = primary_taxonomy_code_2lvl",
        "source_primary_module_for_filing = substr(discipline_local_code, 1, 2)",
        "source_primary_module_for_filing = substr(primary_taxonomy_code_2lvl, 1, 2)",
        "pending_reason = 'missing_primary_module_for_filing'",
        "assignment_status <> 'non_discipline_general_method' OR source_primary_module_for_filing IS NULL",
        "substr(discipline_local_code, 1, 2) = substr(primary_taxonomy_code_2lvl, 1, 2)",
        "substr(discipline_local_code, 4, 2) = substr(primary_taxonomy_code_2lvl, 4, 2)",
    ):
        assert_build_condition(
            fragment in normalized_assignment_sql,
            f'discipline_code_assignments SQLite table is missing expected CHECK constraint fragment: {fragment}',
        )
    for fragment in (
        "assigned_at GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'",
        "trim(assigned_by) <> ''",
        "generated_at GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T*'",
        "generated_by = 'export_structured_data.py'",
        "length(source_commit) = 40",
        "source_commit NOT GLOB '*[^0-9a-f]*'",
        "primary_module_confidence IS NULL OR primary_module_confidence IN ('', 'high', 'medium', 'low')",
        "primary_module_assignment_rule IS NULL OR primary_module_assignment_rule IN ('', 'main_scientific_object', 'main_validation_object', 'direct_contribution_target', 'substantive_application_object', 'manual_override')",
        "secondary_class_source IS NULL OR secondary_class_source IN ('legacy', 'normalized', 'manual_override')",
        "secondary_class_confidence IS NULL OR secondary_class_confidence IN ('high', 'medium', 'low')",
        "secondary_class_review_status IS NULL OR secondary_class_review_status IN ('unreviewed', 'reviewed', 'needs_split', 'needs_merge')",
        "general_method_bucket IS NULL OR general_method_bucket IN ('none', '01.04_general_asd_methods_without_concrete_object_experiments')",
        "active_confirmed_core IN (0, 1)",
        "worktree_dirty IN (0, 1)",
        "discipline_local_rank = substr(discipline_local_code, -3)",
        "discipline_display_order = discipline_local_code",
        "discipline_display_order LIKE '%PENDING-ASD-%'",
        "discipline_display_order LIKE 'GM-PENDING-ASD-%'",
        "assignment_status <> 'active_code' OR ( pending_reason IS NULL AND retired_at IS NULL AND redirected_to_code IS NULL )",
        "assignment_status <> 'pending_secondary' OR ( pending_reason IS NOT NULL AND retired_at IS NULL AND redirected_to_code IS NULL )",
        "assignment_status <> 'non_discipline_general_method' OR ( pending_reason IS NULL AND retired_at IS NULL AND redirected_to_code IS NULL )",
    ):
        assert_build_condition(
            fragment in normalized_registry_sql,
            f'discipline_local_code_registry SQLite table is missing expected CHECK constraint fragment: {fragment}',
        )
    assert_build_condition(
        ('papers', 'paper_id', 'paper_id') in assignment_fk_targets,
        'discipline_code_assignments SQLite table is missing expected foreign key to papers(paper_id)',
    )
    assert_build_condition(
        ('taxonomy_index', 'source_primary_module_for_filing', 'code') in assignment_fk_targets,
        'discipline_code_assignments SQLite table is missing expected foreign key to taxonomy_index(code) for source_primary_module_for_filing',
    )
    assert_build_condition(
        ('papers', 'paper_id', 'paper_id') in registry_fk_targets
        and ('discipline_code_assignments', 'assignment_id', 'assignment_id') in registry_fk_targets
        and ('taxonomy_index', 'primary_module_for_filing', 'code') in registry_fk_targets,
        'discipline_local_code_registry SQLite table is missing expected foreign keys to papers, discipline_code_assignments, or taxonomy_index',
    )

def validate_core_analysis_foreign_keys() -> None:
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        tables = (
            'papers',
            'paper_modules',
            'workflow_mirror_paper_modules',
            'paper_general_method_buckets',
            'pdf_evidence_status',
            'paper_assets',
            'notes',
            'pdf_inventory',
            'missing_pdf_inventory',
            'note_inventory',
        )
        fk_rows_by_table = {
            table: conn.execute(f'PRAGMA foreign_key_list({table})').fetchall()
            for table in tables
        }
    finally:
        conn.close()

    expected_papers_fk_tables = {
        'paper_modules',
        'workflow_mirror_paper_modules',
        'paper_general_method_buckets',
        'pdf_evidence_status',
        'paper_assets',
        'notes',
        'pdf_inventory',
        'missing_pdf_inventory',
        'note_inventory',
    }
    for table in expected_papers_fk_tables:
        fk_targets = {(str(row[2]), str(row[3]), str(row[4])) for row in fk_rows_by_table[table]}
        assert_build_condition(
            ('papers', 'paper_id', 'paper_id') in fk_targets,
            f'{table} SQLite table is missing expected foreign key to papers(paper_id)',
        )
    papers_fk_targets = {
        (str(row[2]), str(row[3]), str(row[4]))
        for row in fk_rows_by_table['papers']
    }
    assert_build_condition(
        ('taxonomy_index', 'primary_module_for_filing', 'code') in papers_fk_targets,
        'papers SQLite table is missing expected foreign key to taxonomy_index(code) for primary_module_for_filing',
    )
    assert_build_condition(
        ('papers', 'duplicate_of', 'paper_id') in papers_fk_targets,
        'papers SQLite table is missing expected self-referential foreign key for duplicate_of -> papers(paper_id)',
    )
    for table in ('paper_modules', 'workflow_mirror_paper_modules'):
        fk_targets = {(str(row[2]), str(row[3]), str(row[4])) for row in fk_rows_by_table[table]}
        assert_build_condition(
            ('taxonomy_index', 'module_code', 'code') in fk_targets,
            f'{table} SQLite table is missing expected foreign key to taxonomy_index(code) for module_code',
        )
    for table in ('pdf_evidence_status', 'pdf_inventory'):
        fk_targets = {(str(row[2]), str(row[3]), str(row[4])) for row in fk_rows_by_table[table]}
        assert_build_condition(
            ('taxonomy_index', 'primary_module_for_filing', 'code') in fk_targets,
            f'{table} SQLite table is missing expected foreign key to taxonomy_index(code) for primary_module_for_filing',
        )

def validate_module_sqlite_constraints() -> None:
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        table_sql_rows = {
            table: conn.execute(
                f"SELECT sql FROM sqlite_master WHERE type = 'table' AND name = '{table}'"
            ).fetchone()
            for table in (
                'papers',
                'paper_modules',
                'workflow_mirror_paper_modules',
                'paper_general_method_buckets',
            )
        }
    finally:
        conn.close()

    papers_sql = table_sql_rows['papers'][0] if table_sql_rows['papers'] else ''
    paper_modules_sql = table_sql_rows['paper_modules'][0] if table_sql_rows['paper_modules'] else ''
    workflow_modules_sql = table_sql_rows['workflow_mirror_paper_modules'][0] if table_sql_rows['workflow_mirror_paper_modules'] else ''
    general_method_sql = table_sql_rows['paper_general_method_buckets'][0] if table_sql_rows['paper_general_method_buckets'] else ''
    normalized_papers_sql = " ".join(papers_sql.split())
    normalized_paper_modules_sql = " ".join(paper_modules_sql.split())
    normalized_workflow_modules_sql = " ".join(workflow_modules_sql.split())
    normalized_general_method_sql = " ".join(general_method_sql.split())

    assert_build_condition(
        "general_method_bucket IN ('none', '01.04_general_asd_methods_without_concrete_object_experiments')" in normalized_papers_sql,
        'papers SQLite table is missing expected general_method_bucket CHECK constraint',
    )
    for fragment in (
        "assignment_scope = 'scientific_object_modules'",
        "module_kind = 'formal_module'",
        "is_primary_for_filing IN (0, 1)",
        "confidence IS NULL OR confidence IN ('', 'high', 'medium', 'low')",
        "source IN ('primary_module_for_filing', 'scientific_object_modules')",
        "(is_primary_for_filing = 1 AND source = 'primary_module_for_filing') OR (is_primary_for_filing = 0 AND source = 'scientific_object_modules')",
    ):
        assert_build_condition(
            fragment in normalized_paper_modules_sql,
            f'paper_modules SQLite table is missing expected CHECK constraint fragment: {fragment}',
        )
    for fragment in (
        "assignment_scope = 'final_modules_or_bucket'",
        "module_kind IN ('formal_module', 'general_bucket')",
        "is_primary_for_filing IN (0, 1)",
        "confidence IS NULL OR confidence IN ('', 'high', 'medium', 'low')",
        "source = 'final_modules_or_bucket'",
    ):
        assert_build_condition(
            fragment in normalized_workflow_modules_sql,
            f'workflow_mirror_paper_modules SQLite table is missing expected CHECK constraint fragment: {fragment}',
        )
    for fragment in (
        "general_method_bucket = '01.04_general_asd_methods_without_concrete_object_experiments'",
        "active_confirmed_core IN (0, 1)",
    ):
        assert_build_condition(
            fragment in normalized_general_method_sql,
            f'paper_general_method_buckets SQLite table is missing expected CHECK constraint fragment: {fragment}',
        )

def validate_evidence_sqlite_constraints() -> None:
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        table_sql_rows = {
            table: conn.execute(
                f"SELECT sql FROM sqlite_master WHERE type = 'table' AND name = '{table}'"
            ).fetchone()
            for table in (
                'pdf_evidence_status',
                'paper_assets',
                'notes',
                'pdf_inventory',
                'note_inventory',
            )
        }
    finally:
        conn.close()

    pdf_evidence_sql = table_sql_rows['pdf_evidence_status'][0] if table_sql_rows['pdf_evidence_status'] else ''
    paper_assets_sql = table_sql_rows['paper_assets'][0] if table_sql_rows['paper_assets'] else ''
    notes_sql = table_sql_rows['notes'][0] if table_sql_rows['notes'] else ''
    pdf_inventory_sql = table_sql_rows['pdf_inventory'][0] if table_sql_rows['pdf_inventory'] else ''
    note_inventory_sql = table_sql_rows['note_inventory'][0] if table_sql_rows['note_inventory'] else ''

    for fragment in (
        "pdf_exists IN (0, 1)",
        "pdf_evidence_type IS NULL OR pdf_evidence_type IN ('main_pdf', 'supplementary_pdf', 'html_full_text', 'abstract', 'official_page', 'project_page')",
        "pdf_check_status IS NULL OR pdf_check_status IN ('full_text_checked', 'source_limited', 'metadata_only')",
        "is_main_text IN (0, 1)",
        "is_supplementary IN (0, 1)",
        "source_limited IS NULL OR source_limited IN ('', 'no', 'yes')",
        "active_confirmed_core IN (0, 1)",
        "NOT (is_main_text = 1 AND is_supplementary = 1)",
        "pdf_evidence_type <> 'main_pdf'",
        "pdf_evidence_type <> 'supplementary_pdf'",
        "pdf_check_status <> 'source_limited'",
        "source_limited <> 'yes'",
        "pdf_check_status <> 'full_text_checked'",
    ):
        assert_build_condition(
            fragment in pdf_evidence_sql,
            f'pdf_evidence_status SQLite table is missing expected CHECK constraint fragment: {fragment}',
        )
    for fragment in (
        "asset_type IN ('note', 'primary_pdf')",
        "path TEXT NOT NULL",
        "asset_exists IN (0, 1)",
        "is_main_text IN (0, 1)",
        "is_supplementary IN (0, 1)",
        "source_limited IS NULL OR source_limited IN ('', 'no', 'yes')",
        "NOT (is_main_text = 1 AND is_supplementary = 1)",
        "asset_type <> 'note'",
    ):
        assert_build_condition(
            fragment in paper_assets_sql,
            f'paper_assets SQLite table is missing expected CHECK constraint fragment: {fragment}',
        )
    for fragment in (
        "note_path TEXT NOT NULL",
        "note_exists IN (0, 1)",
        "active_confirmed_core IN (0, 1)",
    ):
        assert_build_condition(
            fragment in notes_sql,
            f'notes SQLite table is missing expected CHECK constraint fragment: {fragment}',
        )
        assert_build_condition(
            fragment in note_inventory_sql,
            f'note_inventory SQLite table is missing expected CHECK constraint fragment: {fragment}',
        )
    assert_build_condition(
        "active_confirmed_core INTEGER NOT NULL CHECK (active_confirmed_core IN (0, 1))" in pdf_inventory_sql,
        'pdf_inventory SQLite table is missing expected active_confirmed_core CHECK constraint',
    )

def validate_papers_sqlite_constraints() -> None:
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        papers_sql_row = conn.execute(
            "SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'papers'"
        ).fetchone()
    finally:
        conn.close()

    papers_sql = papers_sql_row[0] if papers_sql_row else ''
    normalized_papers_sql = " ".join(papers_sql.split())
    required_fragments = (
        "pdf_exists IN (0, 1)",
        "note_exists IN (0, 1)",
        "active_confirmed_core IN (0, 1)",
        "secondary_class_source IN ('legacy', 'normalized', 'manual_override')",
        "secondary_class_confidence IN ('high', 'medium', 'low')",
        "secondary_class_review_status IN ('unreviewed', 'reviewed', 'needs_split', 'needs_merge')",
        "object_coverage_mode IN ('single_module', 'multi_module', 'general_method_without_concrete_object_experiments')",
        "primary_module_confidence IN ('', 'high', 'medium', 'low')",
        "primary_module_assignment_rule IN ('', 'main_scientific_object', 'main_validation_object', 'direct_contribution_target', 'substantive_application_object', 'manual_override')",
        "classification_source_confidence IN ('high', 'medium', 'low')",
        "classification_parser_rule IN ('structured_remark_token', 'legacy_general_method_fallback', 'legacy_main_class_fallback', 'needs_review')",
        "record_status IN ('candidate', 'active_confirmed_core', 'background_only', 'excluded', 'duplicate', 'retired')",
        "general_method_bucket <> '01.04_general_asd_methods_without_concrete_object_experiments' OR ( scientific_object_modules_json = '[]' AND object_coverage_mode = 'general_method_without_concrete_object_experiments' AND primary_module_for_filing IS NULL )",
        "object_coverage_mode <> 'general_method_without_concrete_object_experiments' OR ( general_method_bucket = '01.04_general_asd_methods_without_concrete_object_experiments' AND scientific_object_modules_json = '[]' AND primary_module_for_filing IS NULL )",
        "CHECK (duplicate_of IS NULL OR duplicate_of <> paper_id)",
    )
    for fragment in required_fragments:
        assert_build_condition(
            fragment in normalized_papers_sql,
            f'papers SQLite table is missing expected CHECK constraint fragment: {fragment}',
        )

def validate_reference_owner_foreign_keys() -> None:
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        change_log_fk_rows = conn.execute('PRAGMA foreign_key_list(change_log)').fetchall()
        classification_terms_fk_rows = conn.execute('PRAGMA foreign_key_list(classification_terms)').fetchall()
        change_log_sql_row = conn.execute(
            "SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'change_log'"
        ).fetchone()
        classification_terms_sql_row = conn.execute(
            "SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'classification_terms'"
        ).fetchone()
    finally:
        conn.close()

    change_log_fk_targets = {
        (str(row[2]), str(row[3]), str(row[4]))
        for row in change_log_fk_rows
    }
    classification_terms_fk_targets = {
        (str(row[2]), str(row[3]), str(row[4]))
        for row in classification_terms_fk_rows
    }
    classification_terms_sql = classification_terms_sql_row[0] if classification_terms_sql_row else ''

    assert_build_condition(
        ('papers', 'paper_id', 'paper_id') in change_log_fk_targets,
        'change_log SQLite table is missing expected foreign key to papers(paper_id)',
    )
    assert_build_condition(
        ('taxonomy_index', 'parent_primary_code', 'code') in classification_terms_fk_targets,
        'classification_terms SQLite table is missing expected foreign key to taxonomy_index(code) for parent_primary_code',
    )
    assert_build_condition(
        "term_level IN ('primary', 'secondary')" in classification_terms_sql
        and "term_level = 'primary'" in classification_terms_sql
        and "term_level = 'secondary'" in classification_terms_sql,
        'classification_terms SQLite table is missing expected term-level CHECK constraints',
    )
    for fragment in (
        "status IN ('active', 'deprecated', 'needs_review')",
        "review_status IS NULL OR review_status IN ('unreviewed', 'reviewed', 'needs_split', 'needs_merge')",
        "term_level = 'primary' AND review_status IS NULL",
        "term_level = 'secondary' AND review_status IS NOT NULL",
    ):
        assert_build_condition(
            fragment in classification_terms_sql,
            f'classification_terms SQLite table is missing expected CHECK constraint fragment: {fragment}',
        )
    change_log_sql = change_log_sql_row[0] if change_log_sql_row else ''
    for fragment in (
        "change_id GLOB 'CL-[0-9][0-9][0-9][0-9][0-9][0-9]'",
        "changed_at GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'",
        "related_commit IS NULL OR related_commit = '' OR related_commit GLOB '[0-9a-f][0-9a-f]*'",
    ):
        assert_build_condition(
            fragment in change_log_sql,
            f'change_log SQLite table is missing expected CHECK constraint fragment: {fragment}',
        )

def validate_auxiliary_analysis_tables(
    papers: list[dict[str, object]],
    pdf_archive_registry: list[dict[str, object]],
    asset_manifest: list[dict[str, object]],
    note_manifest: list[dict[str, object]],
) -> None:
    general_method_bucket_rows = build_general_method_bucket_rows(papers)
    expected_general_method_rows = sorted(
        [
            (
                row['paper_id'],
                row['general_method_bucket'],
                row['active_confirmed_core'],
                row['source_limited'],
            )
            for row in general_method_bucket_rows
        ],
        key=lambda item: item[0],
    )
    expected_pdf_evidence_rows = sorted(
        [
            (
                row['paper_id'],
                row['title'],
                row['pdf_path'],
                bool_to_int(row['pdf_exists']),
                row['pdf_status'],
                row['evidence_status'],
                row['pdf_evidence_type'],
                row['pdf_check_status'],
                bool_to_int(row['is_main_text']),
                bool_to_int(row['is_supplementary']),
                row['asset_size_bytes'],
                row['source_limited'],
                row.get('source_checked_at', ''),
                blank_to_none(row['primary_module_for_filing']),
                bool_to_int(row['active_confirmed_core']),
            )
            for row in pdf_archive_registry
        ],
        key=lambda item: item[0],
    )
    expected_asset_rows = sorted(
        [
            (
                row['asset_id'],
                row['paper_id'],
                row['title'],
                row['asset_type'],
                row['path'],
                bool_to_int(row['exists']),
                row['sha256'],
                row['asset_size_bytes'],
                row['asset_status'],
                bool_to_int(row['is_main_text']),
                bool_to_int(row['is_supplementary']),
                row['source_limited'],
                row.get('source_checked_at', ''),
                row['exported_at'],
            )
            for row in asset_manifest
        ],
        key=lambda item: item[0],
    )
    expected_note_rows = sorted(
        [
            (
                row['paper_id'],
                row['title'],
                row['note_path'],
                bool_to_int(row['note_exists']),
                bool_to_int(row['active_confirmed_core']),
                row['inclusion_status'],
            )
            for row in note_manifest
        ],
        key=lambda item: item[0],
    )

    conn = sqlite3.connect(SQLITE_PATH)
    try:
        actual_general_method_rows = conn.execute(
            '''
            SELECT
                paper_id,
                general_method_bucket,
                active_confirmed_core,
                source_limited
            FROM paper_general_method_buckets
            ORDER BY paper_id
            '''
        ).fetchall()
        actual_pdf_evidence_rows = conn.execute(
            '''
            SELECT
                paper_id,
                title,
                pdf_path,
                pdf_exists,
                pdf_status,
                evidence_status,
                pdf_evidence_type,
                pdf_check_status,
                is_main_text,
                is_supplementary,
                asset_size_bytes,
                source_limited,
                source_checked_at,
                primary_module_for_filing,
                active_confirmed_core
            FROM pdf_evidence_status
            ORDER BY paper_id
            '''
        ).fetchall()
        actual_asset_rows = conn.execute(
            '''
            SELECT
                asset_id,
                paper_id,
                title,
                asset_type,
                path,
                asset_exists,
                sha256,
                asset_size_bytes,
                asset_status,
                is_main_text,
                is_supplementary,
                source_limited,
                source_checked_at,
                exported_at
            FROM paper_assets
            ORDER BY asset_id
            '''
        ).fetchall()
        actual_note_rows = conn.execute(
            '''
            SELECT
                paper_id,
                title,
                note_path,
                note_exists,
                active_confirmed_core,
                inclusion_status
            FROM notes
            ORDER BY paper_id
            '''
        ).fetchall()
    finally:
        conn.close()

    assert_build_condition(
        actual_general_method_rows == expected_general_method_rows,
        'SQLite paper_general_method_buckets drifted from expected general-method rows',
    )
    assert_build_condition(
        actual_pdf_evidence_rows == expected_pdf_evidence_rows,
        'SQLite pdf_evidence_status drifted from expected PDF evidence rows',
    )
    assert_build_condition(
        actual_asset_rows == expected_asset_rows,
        'SQLite paper_assets drifted from expected asset manifest rows',
    )
    assert_build_condition(
        actual_note_rows == expected_note_rows,
        'SQLite notes table drifted from expected note manifest rows',
    )

def validate_owner_loaded_and_inventory_tables(
    classification_code_index: dict[str, object],
    discipline_code_assignments: list[dict[str, object]],
    pdf_manifest: list[dict[str, object]],
    missing_pdf_manifest: list[dict[str, object]],
    note_manifest: list[dict[str, object]],
) -> None:
    classification_term_rows = build_classification_term_rows(classification_code_index)
    change_log_rows = load_jsonl(CHANGE_LOG_JSONL) if CHANGE_LOG_JSONL.exists() else []

    expected_change_log_rows = sorted(
        [
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
        ],
        key=lambda item: item[0],
    )
    expected_classification_term_rows = sorted(
        [
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
        ],
        key=lambda item: (item[0], item[1]),
    )
    expected_discipline_assignment_rows = sorted(
        [
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
        ],
        key=lambda item: item[0],
    )
    expected_pdf_inventory_rows = sorted(
        [
            (
                row['paper_id'],
                row['title'],
                row['pdf_path'],
                row['sha256'],
                blank_to_none(row['primary_module_for_filing']),
                json_list(row['scientific_object_modules']),
                row['pdf_status'],
                row['evidence_status'],
                bool_to_int(row['active_confirmed_core']),
            )
            for row in pdf_manifest
        ],
        key=lambda item: item[0],
    )
    expected_missing_pdf_rows = sorted(
        [
            (
                row['paper_id'],
                row['title'],
                row['doi'],
                row['url'],
                row['pdf_status'],
                row['evidence_status'],
                row['source_limited'],
                row['access_note'],
            )
            for row in missing_pdf_manifest
        ],
        key=lambda item: item[0],
    )
    expected_note_inventory_rows = sorted(
        [
            (
                row['paper_id'],
                row['title'],
                row['note_path'],
                bool_to_int(row['note_exists']),
                bool_to_int(row['active_confirmed_core']),
                row['inclusion_status'],
            )
            for row in note_manifest
        ],
        key=lambda item: item[0],
    )

    conn = sqlite3.connect(SQLITE_PATH)
    try:
        actual_change_log_rows = conn.execute(
            '''
            SELECT
                change_id,
                paper_id,
                changed_at,
                changed_by,
                change_type,
                old_value_json,
                new_value_json,
                reason,
                related_commit
            FROM change_log
            ORDER BY change_id
            '''
        ).fetchall()
        actual_classification_term_rows = conn.execute(
            '''
            SELECT
                taxonomy_code,
                term_level,
                parent_primary_code,
                label,
                definition,
                include_json,
                exclude_json,
                status,
                source,
                review_status
            FROM classification_terms
            ORDER BY taxonomy_code, term_level
            '''
        ).fetchall()
        actual_discipline_assignment_rows = conn.execute(
            '''
            SELECT
                assignment_id,
                paper_id,
                discipline_local_code,
                primary_taxonomy_code_2lvl,
                assignment_status,
                assigned_at,
                assigned_by,
                retired_at,
                redirected_to_code,
                assignment_reason,
                pending_reason,
                source_primary_module_for_filing,
                source_legacy_secondary_class,
                schema_version
            FROM discipline_code_assignments
            ORDER BY assignment_id
            '''
        ).fetchall()
        actual_pdf_inventory_rows = conn.execute(
            '''
            SELECT
                paper_id,
                title,
                pdf_path,
                sha256,
                primary_module_for_filing,
                scientific_object_modules_json,
                pdf_status,
                evidence_status,
                active_confirmed_core
            FROM pdf_inventory
            ORDER BY paper_id
            '''
        ).fetchall()
        actual_missing_pdf_rows = conn.execute(
            '''
            SELECT
                paper_id,
                title,
                doi,
                url,
                pdf_status,
                evidence_status,
                source_limited,
                access_note
            FROM missing_pdf_inventory
            ORDER BY paper_id
            '''
        ).fetchall()
        actual_note_inventory_rows = conn.execute(
            '''
            SELECT
                paper_id,
                title,
                note_path,
                note_exists,
                active_confirmed_core,
                inclusion_status
            FROM note_inventory
            ORDER BY paper_id
            '''
        ).fetchall()
        discipline_assignment_semantic_violations = conn.execute(
            '''
            SELECT COUNT(*)
            FROM discipline_code_assignments
            WHERE
                (
                    assignment_id NOT GLOB 'DCA-[0-9][0-9][0-9][0-9][0-9][0-9]'
                )
                OR (
                    assigned_at NOT GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
                )
                OR (
                    retired_at IS NOT NULL
                    AND retired_at NOT GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
                )
                OR (
                    assigned_by IS NULL
                    OR trim(assigned_by) = ''
                )
                OR (
                    assignment_reason IS NULL
                    OR trim(assignment_reason) = ''
                )
                OR (
                    assignment_status IN ('active_code', 'retired_code', 'redirected_code')
                    AND pending_reason IS NOT NULL
                )
                OR (
                    assignment_status = 'redirected_code'
                    AND (
                        redirected_to_code IS NULL
                        OR redirected_to_code = ''
                        OR redirected_to_code NOT GLOB '[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9]'
                    )
                )
                OR (
                    assignment_status IN ('active_code', 'retired_code', 'redirected_code')
                    AND (
                        source_primary_module_for_filing IS NULL
                        OR source_primary_module_for_filing = ''
                        OR source_legacy_secondary_class IS NULL
                        OR source_legacy_secondary_class <> primary_taxonomy_code_2lvl
                        OR
                        substr(discipline_local_code, 1, 2) <> substr(primary_taxonomy_code_2lvl, 1, 2)
                        OR substr(discipline_local_code, 4, 2) <> substr(primary_taxonomy_code_2lvl, 4, 2)
                        OR source_primary_module_for_filing <> substr(discipline_local_code, 1, 2)
                        OR source_primary_module_for_filing <> substr(primary_taxonomy_code_2lvl, 1, 2)
                    )
                )
                OR (
                    assignment_status = 'pending_secondary'
                    AND (
                        (pending_reason = 'missing_primary_module_for_filing' AND source_primary_module_for_filing IS NOT NULL)
                        OR (pending_reason <> 'missing_primary_module_for_filing' AND (source_primary_module_for_filing IS NULL OR source_primary_module_for_filing = ''))
                    )
                )
                OR (
                    assignment_status = 'non_discipline_general_method'
                    AND source_primary_module_for_filing IS NOT NULL
                )
            '''
        ).fetchone()[0]
    finally:
        conn.close()

    assert_build_condition(
        actual_change_log_rows == expected_change_log_rows,
        'SQLite change_log table drifted from expected change_log rows',
    )
    assert_build_condition(
        actual_classification_term_rows == expected_classification_term_rows,
        'SQLite classification_terms table drifted from expected taxonomy term rows',
    )
    assert_build_condition(
        actual_discipline_assignment_rows == expected_discipline_assignment_rows,
        'SQLite discipline_code_assignments table drifted from expected owner ledger rows',
    )
    assert_build_condition(
        discipline_assignment_semantic_violations == 0,
        'SQLite discipline_code_assignments table violated pending/redirect/code-prefix semantics',
    )
    assert_build_condition(
        actual_pdf_inventory_rows == expected_pdf_inventory_rows,
        'SQLite pdf_inventory table drifted from expected pdf_manifest rows',
    )
    assert_build_condition(
        actual_missing_pdf_rows == expected_missing_pdf_rows,
        'SQLite missing_pdf_inventory table drifted from expected missing PDF manifest rows',
    )
    assert_build_condition(
        actual_note_inventory_rows == expected_note_inventory_rows,
        'SQLite note_inventory table drifted from expected note manifest rows',
    )

def validate_metadata_and_summary_tables(
    papers: list[dict[str, object]],
    taxonomy: dict[str, dict[str, str]],
    discipline_local_code_registry: list[dict[str, object]],
) -> None:
    active = [row for row in papers if row['active_confirmed_core']]
    active_local = [row for row in active if row['pdf_exists']]
    active_missing = [row for row in active if not row['pdf_exists']]
    papers_exported_at_values = sorted({str(row['exported_at']) for row in papers})
    registry_generated_at_values = sorted({str(row['generated_at']) for row in discipline_local_code_registry})
    registry_generated_by_values = sorted({str(row['generated_by']) for row in discipline_local_code_registry})
    registry_source_commit_values = sorted({str(row['source_commit']) for row in discipline_local_code_registry})
    registry_worktree_dirty_values = sorted({str(bool(row['worktree_dirty'])).lower() for row in discipline_local_code_registry})

    assert_build_condition(
        len(papers_exported_at_values) == 1,
        'papers.jsonl exported_at must be uniform for SQLite metadata build',
    )
    assert_build_condition(
        len(registry_generated_at_values) <= 1,
        'discipline_local_code_registry generated_at must be uniform for SQLite metadata build',
    )
    assert_build_condition(
        len(registry_generated_by_values) <= 1,
        'discipline_local_code_registry generated_by must be uniform for SQLite metadata build',
    )
    assert_build_condition(
        len(registry_source_commit_values) <= 1,
        'discipline_local_code_registry source_commit must be uniform for SQLite metadata build',
    )
    assert_build_condition(
        len(registry_worktree_dirty_values) <= 1,
        'discipline_local_code_registry worktree_dirty must be uniform for SQLite metadata build',
    )

    expected_taxonomy_rows = sorted(
        [
            (
                code,
                label,
                'formal_module' if code in FORMAL_MODULES else 'general_bucket',
            )
            for code, label in taxonomy['code_to_label'].items()
        ],
        key=lambda item: item[0],
    )
    expected_metadata_rows = sorted(
        [
            ('schema_version', '2026-07-01'),
            ('papers_jsonl_sha256', compute_sha256(PAPERS_JSONL)),
            ('papers_exported_at', papers_exported_at_values[0]),
            ('papers_record_count', str(len(papers))),
            ('active_confirmed_core_count', str(len(active))),
            ('active_local_pdf_count', str(len(active_local))),
            ('active_no_local_pdf_count', str(len(active_missing))),
            ('discipline_local_code_registry_row_count', str(len(discipline_local_code_registry))),
            ('discipline_local_code_registry_generated_at', registry_generated_at_values[0] if registry_generated_at_values else ''),
            ('discipline_local_code_registry_generated_by', registry_generated_by_values[0] if registry_generated_by_values else ''),
            ('discipline_local_code_registry_source_commit', registry_source_commit_values[0] if registry_source_commit_values else ''),
            ('discipline_local_code_registry_worktree_dirty', registry_worktree_dirty_values[0] if registry_worktree_dirty_values else 'false'),
        ],
        key=lambda item: item[0],
    )

    conn = sqlite3.connect(SQLITE_PATH)
    try:
        actual_taxonomy_rows = conn.execute(
            'SELECT code, label, kind FROM taxonomy_index ORDER BY code'
        ).fetchall()
        actual_metadata_rows = conn.execute(
            'SELECT key, value FROM metadata ORDER BY key'
        ).fetchall()
        actual_active_count = conn.execute(
            'SELECT COUNT(*) FROM active_confirmed_core_papers'
        ).fetchone()[0]
        actual_missing_count = conn.execute(
            'SELECT COUNT(*) FROM active_missing_local_pdf'
        ).fetchone()[0]
    finally:
        conn.close()

    assert_build_condition(
        actual_taxonomy_rows == expected_taxonomy_rows,
        'SQLite taxonomy_index table drifted from expected taxonomy rows',
    )
    assert_build_condition(
        actual_metadata_rows == expected_metadata_rows,
        'SQLite metadata table drifted from expected build metadata rows',
    )
    assert_build_condition(
        actual_active_count == len(active),
        'SQLite active_confirmed_core_papers view drifted from expected active paper count',
    )
    assert_build_condition(
        actual_missing_count == len(active_missing),
        'SQLite active_missing_local_pdf view drifted from expected active missing-PDF count',
    )

def build_analysis_object_scope_rows() -> list[tuple[str, str, str, str, str]]:
    return [
        (
            'active_confirmed_core_papers',
            'view',
            'derived_snapshot',
            'default active-paper subset',
            'Convenience view over papers WHERE active_confirmed_core = 1.',
        ),
        (
            'active_missing_local_pdf',
            'view',
            'workflow_status',
            'missing PDF follow-up subset',
            'Convenience view over active_confirmed_core papers with no local PDF.',
        ),
        (
            'analysis_object_scope_registry',
            'table',
            'registry_metadata',
            'object semantics lookup',
            'SQLite object semantics registry declared by build_analysis_db.py and validated against sqlite_master.',
        ),
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
            'metadata',
            'table',
            'build_metadata',
            'build/run metadata lookup',
            'Build metadata rows derived during build_analysis_db.py; not a paper-level fact source.',
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
            'taxonomy_index',
            'table',
            'taxonomy_lookup',
            'default code/label lookup',
            'SQLite copy of Data/taxonomy_index.json for compact code/label joins; use classification_terms for richer taxonomy owner semantics.',
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
            'pdf_inventory',
            'table',
            'derived_snapshot',
            'local PDF inventory lookup',
            'Per-paper local PDF inventory built from Data/pdf_manifest.json.',
        ),
        (
            'paper_assets',
            'table',
            'derived_snapshot',
            'default note/PDF asset lookup',
            'Per-asset snapshot loaded from Data/registry/asset_manifest.jsonl.',
        ),
        (
            'missing_pdf_inventory',
            'table',
            'workflow_status',
            'missing PDF follow-up lookup',
            'Active confirmed-core no-local-PDF inventory built from Data/missing_pdf_manifest.json.',
        ),
        (
            'notes',
            'table',
            'derived_snapshot',
            'default note inventory lookup',
            'Per-paper note snapshot loaded from Data/note_manifest.json.',
        ),
        (
            'note_inventory',
            'table',
            'derived_snapshot',
            'note inventory compatibility lookup',
            'Per-paper note inventory table built from Data/note_manifest.json.',
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
            'canonical_only',
            'default formal-module analysis',
            'Canonical scientific_object_modules many-to-many relation; this is the default formal-module analysis table.',
        ),
        (
            'mixed_scope_paper_modules',
            'view',
            'mixed_scope',
            'compatibility inspection only',
            'Compatibility union over canonical paper_modules plus workflow_mirror_paper_modules; use only when a mixed-scope audit surface is explicitly required.',
        ),
        (
            'canonical_paper_modules',
            'view',
            'canonical_only',
            'compatibility canonical alias',
            'Compatibility alias over paper_modules for older query/document surfaces that still reference canonical_paper_modules.',
        ),
        (
            'workflow_mirror_paper_modules',
            'table',
            'workflow_mirror_only',
            'audit only',
            'Workflow mirror assignments for audit/debugging only, not default statistics.',
        ),
        (
            'module_assignment_counts',
            'view',
            'canonical_only',
            'default formal-module analysis',
            'Canonical formal-module assignment counts derived from paper_modules.',
        ),
        (
            'mixed_scope_module_assignment_counts',
            'view',
            'mixed_scope',
            'compatibility inspection only',
            'Mixed-scope counts across canonical and workflow mirror assignments; use only for compatibility audits.',
        ),
        (
            'canonical_module_assignment_counts',
            'view',
            'canonical_only',
            'compatibility canonical alias',
            'Compatibility alias over module_assignment_counts for older query/document surfaces that still reference canonical_module_assignment_counts.',
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
            'canonical_bucket_0104_papers',
            'view',
            'canonical_only',
            'canonical 01.04 detail lookup',
            'Canonical paper-level 01.04 bucket detail view, separate from formal module tables.',
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
            'canonical_formal_module_pdf_coverage_summary',
            'view',
            'canonical_only',
            'formal-module PDF coverage summary',
            'Canonical formal-module PDF coverage summary derived from paper_modules and papers.',
        ),
        (
            'canonical_multi_module_combo_summary',
            'view',
            'canonical_only',
            'multi-module combo summary',
            'Canonical multi-module combination frequency summary derived from scientific_object_modules.',
        ),
        (
            'canonical_object_coverage_summary',
            'view',
            'canonical_only',
            'object coverage summary',
            'Canonical record-level object coverage mode summary derived from papers.',
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
    ]

def validate_analysis_object_scope_registry() -> None:
    expected_rows = sorted(build_analysis_object_scope_rows(), key=lambda item: item[0])
    expected_object_names = {row[0] for row in expected_rows}
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        actual_rows = conn.execute(
            '''
            SELECT
                object_name,
                object_type,
                scope_class,
                default_usage,
                warning
            FROM analysis_object_scope_registry
            ORDER BY object_name
            '''
        ).fetchall()
        sqlite_objects = {
            row[0]: row[1]
            for row in conn.execute(
                '''
                SELECT name, type
                FROM sqlite_master
                WHERE type IN ('table', 'view')
                '''
            ).fetchall()
        }
    finally:
        conn.close()
    assert_build_condition(
        actual_rows == expected_rows,
        'SQLite analysis_object_scope_registry drifted from expected declared object-scope rows',
    )
    actual_object_names = {
        object_name
        for object_name in sqlite_objects
        if not object_name.startswith('sqlite_')
    }
    assert_build_condition(
        actual_object_names == expected_object_names,
        'SQLite analysis_object_scope_registry must cover every current SQLite table/view; '
        f'missing_in_registry={sorted(actual_object_names - expected_object_names)!r}, '
        f'extra_registry_rows={sorted(expected_object_names - actual_object_names)!r}',
    )
    for object_name, object_type, _scope_class, _default_usage, _warning in expected_rows:
        actual_type = sqlite_objects.get(object_name)
        assert_build_condition(
            actual_type is not None,
            f'SQLite analysis_object_scope_registry references missing object: {object_name}',
        )
        assert_build_condition(
            actual_type == object_type,
            'SQLite analysis_object_scope_registry object_type mismatch for '
            f'{object_name}: declared {object_type!r}, actual {actual_type!r}',
        )

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
            term_level TEXT NOT NULL CHECK (term_level IN ('primary', 'secondary')),
            parent_primary_code TEXT REFERENCES taxonomy_index(code),
            label TEXT NOT NULL,
            definition TEXT NOT NULL,
            include_json TEXT NOT NULL,
            exclude_json TEXT NOT NULL,
            status TEXT NOT NULL CHECK (status IN ('active', 'deprecated', 'needs_review')),
            source TEXT NOT NULL,
            review_status TEXT CHECK (review_status IS NULL OR review_status IN ('unreviewed', 'reviewed', 'needs_split', 'needs_merge')),
            CHECK (
                (term_level = 'primary' AND parent_primary_code IS NULL)
                OR (term_level = 'secondary' AND parent_primary_code IS NOT NULL)
            ),
            CHECK (
                (term_level = 'primary' AND review_status IS NULL)
                OR (term_level = 'secondary' AND review_status IS NOT NULL)
            ),
            PRIMARY KEY (taxonomy_code, term_level)
        );
        CREATE TABLE change_log (
            change_id TEXT PRIMARY KEY CHECK (change_id GLOB 'CL-[0-9][0-9][0-9][0-9][0-9][0-9]'),
            paper_id TEXT NOT NULL REFERENCES papers(paper_id),
            changed_at TEXT NOT NULL CHECK (changed_at GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
            changed_by TEXT NOT NULL,
            change_type TEXT NOT NULL,
            old_value_json TEXT NOT NULL,
            new_value_json TEXT NOT NULL,
            reason TEXT NOT NULL,
            related_commit TEXT CHECK (related_commit IS NULL OR related_commit = '' OR related_commit GLOB '[0-9a-f][0-9a-f]*')
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
            pdf_path TEXT, pdf_exists INTEGER NOT NULL CHECK (pdf_exists IN (0, 1)), note_path TEXT, note_exists INTEGER NOT NULL CHECK (note_exists IN (0, 1)), is_agent TEXT, inclusion_status TEXT, exclusion_reason TEXT,
            legacy_main_class TEXT, legacy_secondary_class TEXT, legacy_tertiary_class TEXT, secondary_class_source TEXT CHECK (secondary_class_source IN ('legacy', 'normalized', 'manual_override')), secondary_class_confidence TEXT CHECK (secondary_class_confidence IN ('high', 'medium', 'low')), secondary_class_review_status TEXT CHECK (secondary_class_review_status IN ('unreviewed', 'reviewed', 'needs_split', 'needs_merge')), fourth_level_topic TEXT, new_fourth_level TEXT,
            agent_type_json TEXT NOT NULL, research_workflow_role_json TEXT NOT NULL, validation_type_json TEXT NOT NULL, scientific_contribution_type_json TEXT NOT NULL,
            evidence_strength TEXT, citation_priority TEXT, remarks TEXT, scientific_object_modules_json TEXT NOT NULL, general_method_bucket TEXT NOT NULL CHECK (general_method_bucket IN ('none', '01.04_general_asd_methods_without_concrete_object_experiments')),
            object_coverage_mode TEXT CHECK (object_coverage_mode IS NULL OR object_coverage_mode IN ('single_module', 'multi_module', 'general_method_without_concrete_object_experiments')), primary_module_for_filing TEXT REFERENCES taxonomy_index(code), primary_module_confidence TEXT CHECK (primary_module_confidence IS NULL OR primary_module_confidence IN ('', 'high', 'medium', 'low')), primary_module_assignment_rule TEXT CHECK (primary_module_assignment_rule IS NULL OR primary_module_assignment_rule IN ('', 'main_scientific_object', 'main_validation_object', 'direct_contribution_target', 'substantive_application_object', 'manual_override')), primary_module_override_reason TEXT,
            classification_source_field TEXT, classification_source_confidence TEXT CHECK (classification_source_confidence IS NULL OR classification_source_confidence IN ('high', 'medium', 'low')), classification_parser_rule TEXT CHECK (classification_parser_rule IS NULL OR classification_parser_rule IN ('structured_remark_token', 'legacy_general_method_fallback', 'legacy_main_class_fallback', 'needs_review')),
            first_hand_sources_checked TEXT, source_checked_at TEXT, progress_title TEXT, pdf_status TEXT, evidence_status TEXT,
            note_status TEXT, master_status TEXT, final_modules_or_bucket_raw TEXT, final_modules_or_bucket_json TEXT NOT NULL, source_limited TEXT, batch TEXT, closed TEXT,
            active_confirmed_core INTEGER NOT NULL CHECK (active_confirmed_core IN (0, 1)), record_status TEXT CHECK (record_status IS NULL OR record_status IN ('candidate', 'active_confirmed_core', 'background_only', 'excluded', 'duplicate', 'retired')), inclusion_decision TEXT, duplicate_of TEXT REFERENCES papers(paper_id) DEFERRABLE INITIALLY DEFERRED, last_reviewed_at TEXT, last_reviewed_by TEXT, exported_at TEXT NOT NULL,
            CHECK (
                general_method_bucket <> '01.04_general_asd_methods_without_concrete_object_experiments'
                OR (
                    scientific_object_modules_json = '[]'
                    AND object_coverage_mode = 'general_method_without_concrete_object_experiments'
                    AND primary_module_for_filing IS NULL
                )
            ),
            CHECK (
                object_coverage_mode <> 'general_method_without_concrete_object_experiments'
                OR (
                    general_method_bucket = '01.04_general_asd_methods_without_concrete_object_experiments'
                    AND scientific_object_modules_json = '[]'
                    AND primary_module_for_filing IS NULL
                )
            ),
            CHECK (duplicate_of IS NULL OR duplicate_of <> paper_id)
        );
        CREATE TABLE paper_modules (
            paper_id TEXT NOT NULL REFERENCES papers(paper_id),
            assignment_scope TEXT NOT NULL CHECK (assignment_scope = 'scientific_object_modules'),
            module_code TEXT NOT NULL REFERENCES taxonomy_index(code),
            module_kind TEXT NOT NULL CHECK (module_kind = 'formal_module'),
            sort_order INTEGER NOT NULL,
            is_primary_for_filing INTEGER NOT NULL CHECK (is_primary_for_filing IN (0, 1)),
            confidence TEXT CHECK (confidence IS NULL OR confidence IN ('', 'high', 'medium', 'low')),
            source TEXT NOT NULL CHECK (source IN ('primary_module_for_filing', 'scientific_object_modules')),
            CHECK (
                (is_primary_for_filing = 1 AND source = 'primary_module_for_filing')
                OR (is_primary_for_filing = 0 AND source = 'scientific_object_modules')
            ),
            PRIMARY KEY (paper_id, module_code)
        );
        CREATE TABLE workflow_mirror_paper_modules (
            paper_id TEXT NOT NULL REFERENCES papers(paper_id),
            assignment_scope TEXT NOT NULL CHECK (assignment_scope = 'final_modules_or_bucket'),
            module_code TEXT NOT NULL REFERENCES taxonomy_index(code),
            module_kind TEXT NOT NULL CHECK (module_kind IN ('formal_module', 'general_bucket')),
            sort_order INTEGER NOT NULL,
            is_primary_for_filing INTEGER NOT NULL CHECK (is_primary_for_filing IN (0, 1)),
            confidence TEXT CHECK (confidence IS NULL OR confidence IN ('', 'high', 'medium', 'low')),
            source TEXT NOT NULL CHECK (source = 'final_modules_or_bucket'),
            PRIMARY KEY (paper_id, module_code)
        );
        CREATE TABLE paper_general_method_buckets (
            paper_id TEXT PRIMARY KEY REFERENCES papers(paper_id),
            general_method_bucket TEXT NOT NULL CHECK (general_method_bucket = '01.04_general_asd_methods_without_concrete_object_experiments'),
            active_confirmed_core INTEGER NOT NULL CHECK (active_confirmed_core IN (0, 1)),
            source_limited TEXT
        );
        CREATE TABLE discipline_code_assignments (
            assignment_id TEXT PRIMARY KEY CHECK (assignment_id GLOB 'DCA-[0-9][0-9][0-9][0-9][0-9][0-9]'),
            paper_id TEXT NOT NULL REFERENCES papers(paper_id),
            discipline_local_code TEXT,
            primary_taxonomy_code_2lvl TEXT,
            assignment_status TEXT NOT NULL CHECK (
                assignment_status IN (
                    'active_code',
                    'retired_code',
                    'redirected_code',
                    'pending_secondary',
                    'non_discipline_general_method'
                )
            ),
            assigned_at TEXT NOT NULL CHECK (assigned_at GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
            assigned_by TEXT NOT NULL CHECK (trim(assigned_by) <> ''),
            retired_at TEXT CHECK (retired_at IS NULL OR retired_at GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
            redirected_to_code TEXT,
            assignment_reason TEXT NOT NULL CHECK (trim(assignment_reason) <> ''),
            pending_reason TEXT,
            source_primary_module_for_filing TEXT REFERENCES taxonomy_index(code),
            source_legacy_secondary_class TEXT,
            schema_version INTEGER NOT NULL CHECK (schema_version = 1),
            CHECK (
                (
                    assignment_status IN ('active_code', 'retired_code', 'redirected_code')
                    AND discipline_local_code IS NOT NULL
                    AND primary_taxonomy_code_2lvl IS NOT NULL
                )
                OR (
                    assignment_status IN ('pending_secondary', 'non_discipline_general_method')
                    AND discipline_local_code IS NULL
                    AND primary_taxonomy_code_2lvl IS NULL
                )
            ),
            CHECK (
                assignment_status <> 'pending_secondary'
                OR pending_reason IS NOT NULL
            ),
            CHECK (
                assignment_status <> 'non_discipline_general_method'
                OR pending_reason IS NULL
            ),
            CHECK (
                assignment_status NOT IN ('active_code', 'retired_code', 'redirected_code')
                OR pending_reason IS NULL
            ),
            CHECK (
                assignment_status = 'redirected_code'
                OR redirected_to_code IS NULL
            ),
            CHECK (
                assignment_status <> 'redirected_code'
                OR redirected_to_code GLOB '[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9]'
            ),
            CHECK (
                assignment_status NOT IN ('active_code', 'retired_code', 'redirected_code')
                OR (
                    source_primary_module_for_filing IS NOT NULL
                    AND source_primary_module_for_filing <> ''
                    AND source_legacy_secondary_class IS NOT NULL
                    AND source_legacy_secondary_class = primary_taxonomy_code_2lvl
                    AND
                    substr(discipline_local_code, 1, 2) = substr(primary_taxonomy_code_2lvl, 1, 2)
                    AND substr(discipline_local_code, 4, 2) = substr(primary_taxonomy_code_2lvl, 4, 2)
                    AND source_primary_module_for_filing = substr(discipline_local_code, 1, 2)
                    AND source_primary_module_for_filing = substr(primary_taxonomy_code_2lvl, 1, 2)
                )
            ),
            CHECK (
                assignment_status <> 'pending_secondary'
                OR (
                    (pending_reason = 'missing_primary_module_for_filing' AND source_primary_module_for_filing IS NULL)
                    OR (pending_reason <> 'missing_primary_module_for_filing' AND source_primary_module_for_filing IS NOT NULL AND source_primary_module_for_filing <> '')
                )
            ),
            CHECK (
                assignment_status <> 'non_discipline_general_method'
                OR source_primary_module_for_filing IS NULL
            )
        );
        CREATE UNIQUE INDEX discipline_code_assignments_active_code_unique
        ON discipline_code_assignments(discipline_local_code)
        WHERE assignment_status = 'active_code';
        CREATE UNIQUE INDEX discipline_code_assignments_one_active_per_paper
        ON discipline_code_assignments(paper_id)
        WHERE assignment_status = 'active_code';
        CREATE TABLE discipline_local_code_registry (
            paper_id TEXT PRIMARY KEY REFERENCES papers(paper_id),
            assignment_id TEXT NOT NULL REFERENCES discipline_code_assignments(assignment_id),
            discipline_local_code TEXT,
            discipline_local_rank TEXT,
            discipline_display_order TEXT NOT NULL,
            assignment_status TEXT NOT NULL CHECK (
                assignment_status IN (
                    'active_code',
                    'pending_secondary',
                    'non_discipline_general_method'
                )
            ),
            assigned_at TEXT NOT NULL,
            assigned_by TEXT NOT NULL,
            retired_at TEXT,
            redirected_to_code TEXT,
            assignment_reason TEXT NOT NULL,
            pending_reason TEXT,
            primary_module_for_filing TEXT REFERENCES taxonomy_index(code),
            primary_module_confidence TEXT CHECK (primary_module_confidence IS NULL OR primary_module_confidence IN ('', 'high', 'medium', 'low')),
            primary_module_assignment_rule TEXT CHECK (primary_module_assignment_rule IS NULL OR primary_module_assignment_rule IN ('', 'main_scientific_object', 'main_validation_object', 'direct_contribution_target', 'substantive_application_object', 'manual_override')),
            primary_module_override_reason TEXT,
            primary_taxonomy_code_2lvl TEXT,
            legacy_secondary_class TEXT,
            secondary_class_source TEXT CHECK (secondary_class_source IS NULL OR secondary_class_source IN ('legacy', 'normalized', 'manual_override')),
            secondary_class_confidence TEXT CHECK (secondary_class_confidence IS NULL OR secondary_class_confidence IN ('high', 'medium', 'low')),
            secondary_class_review_status TEXT CHECK (secondary_class_review_status IS NULL OR secondary_class_review_status IN ('unreviewed', 'reviewed', 'needs_split', 'needs_merge')),
            scientific_object_modules_json TEXT NOT NULL,
            general_method_bucket TEXT CHECK (general_method_bucket IS NULL OR general_method_bucket IN ('none', '01.04_general_asd_methods_without_concrete_object_experiments')),
            title TEXT NOT NULL,
            note_path TEXT,
            pdf_path TEXT,
            active_confirmed_core INTEGER NOT NULL CHECK (active_confirmed_core IN (0, 1)),
            is_derived_snapshot INTEGER NOT NULL CHECK (is_derived_snapshot = 1),
            generated_at TEXT NOT NULL CHECK (generated_at GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T*'),
            generated_by TEXT NOT NULL CHECK (generated_by = 'export_structured_data.py'),
            source_commit TEXT NOT NULL CHECK (
                length(source_commit) = 40
                AND source_commit NOT GLOB '*[^0-9a-f]*'
            ),
            worktree_dirty INTEGER NOT NULL CHECK (worktree_dirty IN (0, 1)),
            CHECK (
                (
                    assignment_status = 'active_code'
                    AND discipline_local_code IS NOT NULL
                    AND discipline_local_rank IS NOT NULL
                    AND primary_taxonomy_code_2lvl IS NOT NULL
                    AND discipline_local_rank = substr(discipline_local_code, -3)
                    AND discipline_display_order = discipline_local_code
                )
                OR (
                    assignment_status IN ('pending_secondary', 'non_discipline_general_method')
                    AND discipline_local_code IS NULL
                    AND discipline_local_rank IS NULL
                    AND primary_taxonomy_code_2lvl IS NULL
                )
            ),
            CHECK (
                assignment_status <> 'pending_secondary'
                OR discipline_display_order LIKE '%PENDING-ASD-%'
            ),
            CHECK (
                assignment_status <> 'non_discipline_general_method'
                OR discipline_display_order LIKE 'GM-PENDING-ASD-%'
            ),
            CHECK (assigned_at GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
            CHECK (trim(assigned_by) <> ''),
            CHECK (
                assignment_status <> 'active_code'
                OR (
                    pending_reason IS NULL
                    AND retired_at IS NULL
                    AND redirected_to_code IS NULL
                )
            ),
            CHECK (
                assignment_status <> 'pending_secondary'
                OR (
                    pending_reason IS NOT NULL
                    AND retired_at IS NULL
                    AND redirected_to_code IS NULL
                )
            ),
            CHECK (
                assignment_status <> 'non_discipline_general_method'
                OR (
                    pending_reason IS NULL
                    AND retired_at IS NULL
                    AND redirected_to_code IS NULL
                )
            )
        );
        CREATE TABLE pdf_evidence_status (
            paper_id TEXT PRIMARY KEY REFERENCES papers(paper_id),
            title TEXT NOT NULL,
            pdf_path TEXT,
            pdf_exists INTEGER NOT NULL CHECK (pdf_exists IN (0, 1)),
            pdf_status TEXT,
            evidence_status TEXT,
            pdf_evidence_type TEXT CHECK (pdf_evidence_type IS NULL OR pdf_evidence_type IN ('main_pdf', 'supplementary_pdf', 'html_full_text', 'abstract', 'official_page', 'project_page')),
            pdf_check_status TEXT CHECK (pdf_check_status IS NULL OR pdf_check_status IN ('full_text_checked', 'source_limited', 'metadata_only')),
            is_main_text INTEGER NOT NULL CHECK (is_main_text IN (0, 1)),
            is_supplementary INTEGER NOT NULL CHECK (is_supplementary IN (0, 1)),
            asset_size_bytes INTEGER,
            source_limited TEXT CHECK (source_limited IS NULL OR source_limited IN ('', 'no', 'yes')),
            source_checked_at TEXT,
            primary_module_for_filing TEXT REFERENCES taxonomy_index(code),
            active_confirmed_core INTEGER NOT NULL CHECK (active_confirmed_core IN (0, 1)),
            CHECK (NOT (is_main_text = 1 AND is_supplementary = 1)),
            CHECK (
                pdf_evidence_type <> 'main_pdf'
                OR (is_main_text = 1 AND is_supplementary = 0)
            ),
            CHECK (
                pdf_evidence_type <> 'supplementary_pdf'
                OR (is_main_text = 0 AND is_supplementary = 1)
            ),
            CHECK (
                pdf_check_status <> 'source_limited'
                OR source_limited = 'yes'
            ),
            CHECK (
                source_limited <> 'yes'
                OR pdf_check_status = 'source_limited'
            ),
            CHECK (
                pdf_check_status <> 'full_text_checked'
                OR IFNULL(source_limited, '') <> 'yes'
            )
        );
        CREATE TABLE paper_assets (
            asset_id TEXT PRIMARY KEY,
            paper_id TEXT NOT NULL REFERENCES papers(paper_id),
            title TEXT NOT NULL,
            asset_type TEXT NOT NULL CHECK (asset_type IN ('note', 'primary_pdf')),
            path TEXT NOT NULL,
            asset_exists INTEGER NOT NULL CHECK (asset_exists IN (0, 1)),
            sha256 TEXT,
            asset_size_bytes INTEGER,
            asset_status TEXT,
            is_main_text INTEGER NOT NULL CHECK (is_main_text IN (0, 1)),
            is_supplementary INTEGER NOT NULL CHECK (is_supplementary IN (0, 1)),
            source_limited TEXT CHECK (source_limited IS NULL OR source_limited IN ('', 'no', 'yes')),
            source_checked_at TEXT,
            exported_at TEXT,
            CHECK (NOT (is_main_text = 1 AND is_supplementary = 1)),
            CHECK (
                asset_type <> 'note'
                OR (is_main_text = 0 AND is_supplementary = 0)
            )
        );
        CREATE TABLE notes (
            paper_id TEXT PRIMARY KEY REFERENCES papers(paper_id),
            title TEXT NOT NULL,
            note_path TEXT NOT NULL,
            note_exists INTEGER NOT NULL CHECK (note_exists IN (0, 1)),
            active_confirmed_core INTEGER NOT NULL CHECK (active_confirmed_core IN (0, 1)),
            inclusion_status TEXT
        );
        CREATE TABLE pdf_inventory (paper_id TEXT PRIMARY KEY REFERENCES papers(paper_id), title TEXT NOT NULL, pdf_path TEXT NOT NULL, sha256 TEXT NOT NULL, primary_module_for_filing TEXT REFERENCES taxonomy_index(code), scientific_object_modules_json TEXT NOT NULL, pdf_status TEXT, evidence_status TEXT, active_confirmed_core INTEGER NOT NULL CHECK (active_confirmed_core IN (0, 1)));
        CREATE TABLE missing_pdf_inventory (paper_id TEXT PRIMARY KEY REFERENCES papers(paper_id), title TEXT NOT NULL, doi TEXT, url TEXT, pdf_status TEXT, evidence_status TEXT, source_limited TEXT, access_note TEXT);
        CREATE TABLE note_inventory (paper_id TEXT PRIMARY KEY REFERENCES papers(paper_id), title TEXT NOT NULL, note_path TEXT NOT NULL, note_exists INTEGER NOT NULL CHECK (note_exists IN (0, 1)), active_confirmed_core INTEGER NOT NULL CHECK (active_confirmed_core IN (0, 1)), inclusion_status TEXT);
        CREATE VIEW active_confirmed_core_papers AS SELECT * FROM papers WHERE active_confirmed_core = 1;
        CREATE VIEW active_missing_local_pdf AS SELECT * FROM papers WHERE active_confirmed_core = 1 AND pdf_exists = 0;
        CREATE VIEW canonical_paper_modules AS
        SELECT * FROM paper_modules;
        CREATE VIEW mixed_scope_paper_modules AS
        SELECT * FROM paper_modules
        UNION ALL
        SELECT * FROM workflow_mirror_paper_modules;
        CREATE VIEW module_assignment_counts AS
        SELECT
            module_code,
            COUNT(*) AS paper_count,
            SUM(CASE WHEN p.active_confirmed_core = 1 THEN 1 ELSE 0 END) AS active_confirmed_core_count
        FROM paper_modules pm
        JOIN papers p ON p.paper_id = pm.paper_id
        GROUP BY module_code;
        CREATE VIEW mixed_scope_module_assignment_counts AS
        SELECT
            assignment_scope,
            module_code,
            COUNT(*) AS paper_count,
            SUM(CASE WHEN p.active_confirmed_core = 1 THEN 1 ELSE 0 END) AS active_confirmed_core_count
        FROM mixed_scope_paper_modules pm
        JOIN papers p ON p.paper_id = pm.paper_id
        GROUP BY assignment_scope, module_code;
        CREATE VIEW canonical_module_assignment_counts AS
        SELECT * FROM module_assignment_counts;
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
            ('papers_exported_at', str(papers[0]['exported_at']) if papers else ''),
            ('papers_record_count', str(len(papers))),
            ('active_confirmed_core_count', str(len(active))),
            ('active_local_pdf_count', str(len(active_local))),
            ('active_no_local_pdf_count', str(len(active_missing))),
            ('discipline_local_code_registry_row_count', str(len(discipline_local_code_registry))),
            ('discipline_local_code_registry_generated_at', str(discipline_local_code_registry[0]['generated_at']) if discipline_local_code_registry else ''),
            ('discipline_local_code_registry_generated_by', str(discipline_local_code_registry[0]['generated_by']) if discipline_local_code_registry else ''),
            ('discipline_local_code_registry_source_commit', str(discipline_local_code_registry[0]['source_commit']) if discipline_local_code_registry else ''),
            ('discipline_local_code_registry_worktree_dirty', str(bool(discipline_local_code_registry[0]['worktree_dirty'])).lower() if discipline_local_code_registry else 'false'),
        ])
        conn.executemany(
            'INSERT INTO analysis_object_scope_registry(object_name, object_type, scope_class, default_usage, warning) VALUES(?, ?, ?, ?, ?)',
            build_analysis_object_scope_rows(),
        )
        conn.executemany('INSERT INTO taxonomy_index(code, label, kind) VALUES(?, ?, ?)', [
            (code, label, 'formal_module' if code in FORMAL_MODULES else 'general_bucket')
            for code, label in taxonomy['code_to_label'].items()
        ])
        classification_term_rows = build_classification_term_rows(classification_code_index)
        change_log_rows = load_jsonl(CHANGE_LOG_JSONL) if CHANGE_LOG_JSONL.exists() else []
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
        papers_insert_sql = f"INSERT INTO papers VALUES({', '.join(['?'] * 60)})"
        conn.executemany(papers_insert_sql, [
            (
                paper['paper_id'], paper['title'], paper['authors'], paper['year'], paper['source'], paper['doi_or_url'], paper['doi'], paper['url'], paper['arxiv_id'],
                paper['pdf_path'], bool_to_int(paper['pdf_exists']), paper['note_path'], bool_to_int(paper['note_exists']), paper['is_agent'], paper['inclusion_status'], paper['exclusion_reason'],
                paper['legacy_main_class'], paper['legacy_secondary_class'], paper['legacy_tertiary_class'], paper['secondary_class_source'], paper['secondary_class_confidence'], paper['secondary_class_review_status'], paper['fourth_level_topic'], paper['new_fourth_level'],
                json_list(paper['agent_type']), json_list(paper['research_workflow_role']), json_list(paper['validation_type']), json_list(paper['scientific_contribution_type']),
                paper['evidence_strength'], paper['citation_priority'], paper['remarks'], json_list(paper['scientific_object_modules']), paper['general_method_bucket'], paper['object_coverage_mode'],
                blank_to_none(paper['primary_module_for_filing']), paper['primary_module_confidence'], paper['primary_module_assignment_rule'], paper['primary_module_override_reason'],
                paper['classification_source_field'], paper['classification_source_confidence'], paper['classification_parser_rule'],
                paper['first_hand_sources_checked'], paper['source_checked_at'], paper['progress_title'], paper['pdf_status'], paper['evidence_status'], paper['note_status'], paper['master_status'],
                paper['final_modules_or_bucket_raw'], json_list(paper['final_modules_or_bucket']), paper['source_limited'], paper['batch'], paper['closed'], bool_to_int(paper['active_confirmed_core']),
                paper['record_status'], paper['inclusion_decision'], blank_to_none(paper['duplicate_of']), paper['last_reviewed_at'], paper['last_reviewed_by'], paper['exported_at'],
            )
            for paper in papers
        ])
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
        canonical_module_rows = [
            row for row in module_rows if row['assignment_scope'] == 'scientific_object_modules'
        ]
        workflow_module_rows = [
            row for row in module_rows if row['assignment_scope'] == 'final_modules_or_bucket'
        ]
        conn.executemany('INSERT INTO paper_modules(paper_id, assignment_scope, module_code, module_kind, sort_order, is_primary_for_filing, confidence, source) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', [
            (
                row['paper_id'],
                row['assignment_scope'],
                row['module_code'],
                row['module_kind'],
                row['sort_order'],
                row['is_primary_for_filing'],
                row['confidence'],
                row['source'],
            )
            for row in canonical_module_rows
        ])
        conn.executemany('INSERT INTO workflow_mirror_paper_modules(paper_id, assignment_scope, module_code, module_kind, sort_order, is_primary_for_filing, confidence, source) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', [
            (
                row['paper_id'],
                row['assignment_scope'],
                row['module_code'],
                row['module_kind'],
                row['sort_order'],
                row['is_primary_for_filing'],
                row['confidence'],
                row['source'],
            )
            for row in workflow_module_rows
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
        conn.executemany('INSERT INTO discipline_local_code_registry VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [
            (
                row['paper_id'],
                row['assignment_id'],
                blank_to_none(row['discipline_local_code']),
                blank_to_none(row['discipline_local_rank']),
                row['discipline_display_order'],
                row['assignment_status'],
                row['assigned_at'],
                row['assigned_by'],
                row['retired_at'],
                row['redirected_to_code'],
                row['assignment_reason'],
                row['pending_reason'],
                blank_to_none(row['primary_module_for_filing']),
                row['primary_module_confidence'],
                row['primary_module_assignment_rule'],
                row['primary_module_override_reason'],
                blank_to_none(row['primary_taxonomy_code_2lvl']),
                row['legacy_secondary_class'],
                row['secondary_class_source'],
                row['secondary_class_confidence'],
                row['secondary_class_review_status'],
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
        pdf_evidence_insert_sql = f"INSERT INTO pdf_evidence_status VALUES({', '.join(['?'] * 15)})"
        conn.executemany(pdf_evidence_insert_sql, [
            (
                row['paper_id'],
                row['title'],
                row['pdf_path'],
                bool_to_int(row['pdf_exists']),
                row['pdf_status'],
                row['evidence_status'],
                row['pdf_evidence_type'],
                row['pdf_check_status'],
                bool_to_int(row['is_main_text']),
                bool_to_int(row['is_supplementary']),
                row['asset_size_bytes'],
                row['source_limited'],
                row.get('source_checked_at', ''),
                blank_to_none(row['primary_module_for_filing']),
                bool_to_int(row['active_confirmed_core']),
            )
            for row in pdf_archive_registry
        ])
        paper_assets_insert_sql = f"INSERT INTO paper_assets VALUES({', '.join(['?'] * 14)})"
        conn.executemany(paper_assets_insert_sql, [
            (
                row['asset_id'],
                row['paper_id'],
                row['title'],
                row['asset_type'],
                row['path'],
                bool_to_int(row['exists']),
                row['sha256'],
                row['asset_size_bytes'],
                row['asset_status'],
                bool_to_int(row['is_main_text']),
                bool_to_int(row['is_supplementary']),
                row['source_limited'],
                row.get('source_checked_at', ''),
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
            (row['paper_id'], row['title'], row['pdf_path'], row['sha256'], blank_to_none(row['primary_module_for_filing']), json_list(row['scientific_object_modules']), row['pdf_status'], row['evidence_status'], bool_to_int(row['active_confirmed_core']))
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
    assert_safe_output_paths([
        PAPERS_CSV,
        PAPER_MODULES_CSV,
        CANONICAL_PAPER_MODULES_CSV,
        WORKFLOW_MIRROR_PAPER_MODULES_CSV,
        MIXED_SCOPE_PAPER_MODULES_CSV,
        DISCIPLINE_LOCAL_CODE_REGISTRY_CSV,
        SQLITE_PATH,
    ])
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
    canonical_module_rows = [
        row for row in module_rows if row['assignment_scope'] == 'scientific_object_modules'
    ]
    workflow_module_rows = [
        row for row in module_rows if row['assignment_scope'] == 'final_modules_or_bucket'
    ]
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
    validate_papers_outputs(papers)
    validate_module_csv_outputs(module_rows)
    validate_sqlite_module_surfaces(module_rows)
    validate_discipline_local_code_registry_outputs(discipline_local_code_registry)
    validate_discipline_sqlite_constraints()
    validate_core_analysis_foreign_keys()
    validate_module_sqlite_constraints()
    validate_evidence_sqlite_constraints()
    validate_papers_sqlite_constraints()
    validate_reference_owner_foreign_keys()
    validate_auxiliary_analysis_tables(
        papers,
        pdf_archive_registry,
        asset_manifest,
        note_manifest,
    )
    validate_owner_loaded_and_inventory_tables(
        classification_code_index,
        discipline_code_assignments,
        pdf_manifest,
        missing_pdf_manifest,
        note_manifest,
    )
    validate_metadata_and_summary_tables(
        papers,
        taxonomy,
        discipline_local_code_registry,
    )
    validate_analysis_object_scope_registry()
    print(f'Wrote {PAPERS_CSV}')
    print(f'Wrote {PAPER_MODULES_CSV}')
    print(f'Wrote {CANONICAL_PAPER_MODULES_CSV}')
    print(f'Wrote {WORKFLOW_MIRROR_PAPER_MODULES_CSV}')
    print(f'Wrote {MIXED_SCOPE_PAPER_MODULES_CSV}')
    print(f'Wrote {DISCIPLINE_LOCAL_CODE_REGISTRY_CSV}')
    print(f'Wrote {SQLITE_PATH}')
    print(f'papers rows: {len(papers)}')
    print(f'paper_modules rows: {len(canonical_module_rows)}')
    print(f'workflow_mirror_paper_modules rows: {len(workflow_module_rows)}')
    print(f'mixed_scope_paper_modules rows: {len(module_rows)}')
    print(f'discipline_code_assignments rows: {len(discipline_code_assignments)}')
    print(f'discipline_local_code_registry rows: {len(discipline_local_code_registry)}')

if __name__ == '__main__':
    main()
