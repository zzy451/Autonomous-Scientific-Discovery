#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parent.parent
SQLITE_PATH = ROOT / 'Data' / 'papers.sqlite'

def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(SQLITE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def stringify(value: object) -> str:
    if value is None:
        return ''
    return str(value).replace('\n', ' ')

def truncate(value: str, width: int) -> str:
    if len(value) <= width:
        return value
    if width <= 3:
        return value[:width]
    return value[:width - 3] + '...'

def print_heading(title: str) -> None:
    print(title)
    print('=' * len(title))

def print_rows(rows: Sequence[sqlite3.Row], *, max_widths: dict[str, int] | None = None, default_max_width: int = 32) -> None:
    if not rows:
        print('No rows found.')
        return
    headers = list(rows[0].keys())
    max_widths = max_widths or {}
    rendered_rows = [{header: stringify(row[header]) for header in headers} for row in rows]
    widths = {}
    for header in headers:
        natural_width = max(len(header), *(len(row[header]) for row in rendered_rows))
        widths[header] = max(len(header), min(natural_width, max_widths.get(header, default_max_width)))

    print(' | '.join(truncate(header, widths[header]).ljust(widths[header]) for header in headers))
    print('-+-'.join('-' * widths[header] for header in headers))
    for row in rows:
        print(' | '.join(truncate(stringify(row[header]), widths[header]).ljust(widths[header]) for header in headers))

def print_status_breakdown(conn: sqlite3.Connection, field: str, *, active_only: bool) -> None:
    clause = 'WHERE active_confirmed_core = 1' if active_only else ''
    rows = conn.execute(f'''
        SELECT
            COALESCE(NULLIF(TRIM({field}), ''), '(blank)') AS {field},
            COUNT(*) AS paper_count
        FROM papers
        {clause}
        GROUP BY 1
        ORDER BY paper_count DESC, 1
    ''').fetchall()
    print_heading(field)
    print_rows(rows, max_widths={field: 64})
    print()

def summary(conn: sqlite3.Connection) -> None:
    print_heading('Canonical Summary')
    meta = {row['key']: row['value'] for row in conn.execute('SELECT key, value FROM metadata')}
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    print()
    rows = conn.execute('''SELECT module_code, active_confirmed_core_count FROM canonical_module_assignment_counts ORDER BY module_code''').fetchall()
    print_rows(rows)
    print()
    bucket_row = conn.execute('SELECT active_confirmed_core_count FROM canonical_bucket_0104_summary').fetchone()
    print_heading('Canonical 01.04 Bucket')
    print(json.dumps({'active_confirmed_core_count': bucket_row['active_confirmed_core_count']}, ensure_ascii=False, indent=2))

def module_distribution(conn: sqlite3.Connection) -> None:
    print_heading('Canonical Formal Module Distribution')
    meta = {row['key']: row['value'] for row in conn.execute('SELECT key, value FROM metadata')}
    active_record_count = int(meta['active_confirmed_core_count'])
    active_assignment_count = conn.execute(
        'SELECT COALESCE(SUM(active_confirmed_core_count), 0) AS total FROM canonical_module_assignment_counts'
    ).fetchone()['total']
    bucket_row = conn.execute('SELECT active_confirmed_core_count FROM canonical_bucket_0104_summary').fetchone()
    print(json.dumps({
        'active_confirmed_core_record_count': active_record_count,
        'active_formal_module_assignment_count': active_assignment_count,
        'active_general_method_bucket_0104_count': bucket_row['active_confirmed_core_count'],
    }, ensure_ascii=False, indent=2))
    print()
    rows = conn.execute('''
        SELECT
            c.module_code,
            t.label,
            c.active_confirmed_core_count,
            ROUND(100.0 * c.active_confirmed_core_count / ?, 2) AS share_within_active_formal_assignments_pct,
            ROUND(100.0 * c.active_confirmed_core_count / ?, 2) AS assignments_vs_active_record_count_pct
        FROM canonical_module_assignment_counts c
        JOIN taxonomy_index t ON t.code = c.module_code
        ORDER BY c.module_code
    ''', (active_assignment_count or 1, active_record_count or 1)).fetchall()
    print_rows(rows, max_widths={'label': 44})

def object_coverage_summary(conn: sqlite3.Connection, *, all_papers: bool) -> None:
    scope_label = 'all scopes' if all_papers else 'active_confirmed_core only'
    print_heading(f'Canonical Object Coverage Summary ({scope_label})')
    rows = conn.execute(f'''
        SELECT
            scope,
            object_coverage_mode,
            paper_count,
            local_pdf_count,
            note_count,
            source_limited_count
        FROM canonical_object_coverage_summary
        {'' if all_papers else "WHERE scope = 'active_confirmed_core'"}
        ORDER BY
            CASE object_coverage_mode
                WHEN 'single_module' THEN 1
                WHEN 'multi_module' THEN 2
                WHEN 'general_method_without_concrete_object_experiments' THEN 3
                ELSE 9
            END
    ''').fetchall()
    print_rows(rows, max_widths={'object_coverage_mode': 48})

def multi_module_combo_summary(
    conn: sqlite3.Connection, *, all_papers: bool, limit: int, module_count: int | None
) -> None:
    scope_label = 'all scopes' if all_papers else 'active_confirmed_core only'
    print_heading(f'Canonical Multi-Module Combination Summary ({scope_label})')
    filters = []
    params: list[object] = []
    if not all_papers:
        filters.append("scope = 'active_confirmed_core'")
    if module_count is not None:
        filters.append('module_count = ?')
        params.append(module_count)
    where_clause = f"WHERE {' AND '.join(filters)}" if filters else ''
    denominator = conn.execute(f'''
        SELECT COALESCE(SUM(paper_count), 0) AS total
        FROM canonical_multi_module_combo_summary
        {where_clause}
    ''', params).fetchone()['total']
    rows = conn.execute(f'''
        SELECT
            canonical_module_combo,
            module_count,
            paper_count,
            local_pdf_count,
            note_count,
            source_limited_count,
            ROUND(100.0 * paper_count / ?, 2) AS share_within_scope_multi_module_pct
        FROM canonical_multi_module_combo_summary
        {where_clause}
        ORDER BY paper_count DESC, module_count, canonical_module_combo
        LIMIT ?
    ''', (*params, denominator or 1, limit)).fetchall()
    print_rows(rows, max_widths={'canonical_module_combo': 28})

def module_pdf_coverage(conn: sqlite3.Connection, *, sort_by: str) -> None:
    print_heading('Canonical Formal Module PDF Coverage')
    order_clause = {
        'module': 'c.module_code',
        'coverage': 'c.active_local_pdf_coverage_rate DESC, c.active_assignment_count DESC, c.module_code',
        'missing': 'c.active_missing_local_pdf_count DESC, c.active_assignment_count DESC, c.module_code',
    }[sort_by]
    rows = conn.execute(f'''
        SELECT
            c.module_code,
            t.label,
            c.active_assignment_count,
            c.active_local_pdf_count,
            c.active_missing_local_pdf_count,
            c.active_local_pdf_coverage_rate,
            c.active_note_count,
            c.active_missing_note_count,
            c.active_source_limited_count
        FROM canonical_formal_module_pdf_coverage_summary c
        JOIN taxonomy_index t ON t.code = c.module_code
        ORDER BY {order_clause}
    ''').fetchall()
    print_rows(rows, max_widths={'label': 44})

def bucket_0104_summary(conn: sqlite3.Connection, *, details: bool, limit: int) -> None:
    print_heading('Canonical 01.04 General-Method Bucket Summary')
    row = conn.execute('SELECT * FROM canonical_bucket_0104_summary').fetchone()
    print(json.dumps(dict(row), ensure_ascii=False, indent=2))
    if not details:
        return
    print()
    detail_rows = conn.execute('''
        SELECT
            paper_id,
            title,
            year,
            source,
            pdf_exists,
            note_exists,
            source_limited,
            active_confirmed_core
        FROM canonical_bucket_0104_papers
        ORDER BY active_confirmed_core DESC, paper_id
        LIMIT ?
    ''', (limit,)).fetchall()
    print_heading(f'Canonical 01.04 Papers (first {limit})')
    print_rows(detail_rows, max_widths={'title': 56, 'source': 24})

def paper(conn: sqlite3.Connection, paper_id: str) -> None:
    row = conn.execute('SELECT * FROM papers WHERE paper_id = ?', (paper_id,)).fetchone()
    if row is None:
        print(f'Paper not found: {paper_id}')
        return
    payload = dict(row)
    for key in ('agent_type_json', 'research_workflow_role_json', 'validation_type_json', 'scientific_contribution_type_json', 'scientific_object_modules_json', 'final_modules_or_bucket_json'):
        payload[key] = json.loads(payload[key])
    payload['canonical_module_assignments'] = [
        dict(module_row)
        for module_row in conn.execute('SELECT module_code, module_kind, sort_order FROM canonical_paper_modules WHERE paper_id = ? ORDER BY sort_order', (paper_id,))
    ]
    payload['workflow_mirror_assignments'] = [
        dict(module_row)
        for module_row in conn.execute('SELECT module_code, module_kind, sort_order FROM workflow_mirror_paper_modules WHERE paper_id = ? ORDER BY sort_order', (paper_id,))
    ]
    print('Semantics: canonical classification fields = scientific_object_modules/general_method_bucket; workflow mirror fields = final_modules_or_bucket/workflow_mirror_assignments')
    print(json.dumps(payload, ensure_ascii=False, indent=2))

def missing_pdf(conn: sqlite3.Connection) -> None:
    print_heading('Missing Local PDF Inventory')
    rows = conn.execute('SELECT paper_id, title, doi, pdf_status, evidence_status, source_limited FROM missing_pdf_inventory ORDER BY paper_id').fetchall()
    print_rows(rows)

def multi_module(conn: sqlite3.Connection) -> None:
    print_heading('Canonical Multi-Module Papers')
    rows = conn.execute('''SELECT paper_id, title, primary_module_for_filing, scientific_object_modules_json FROM papers WHERE active_confirmed_core = 1 AND object_coverage_mode = 'multi_module' ORDER BY paper_id''').fetchall()
    print_rows(rows, max_widths={'title': 56, 'scientific_object_modules_json': 24})

def module(conn: sqlite3.Connection, code: str) -> None:
    print_heading(f'Canonical Module {code}')
    rows = conn.execute('''SELECT p.paper_id, p.title, p.primary_module_for_filing, p.pdf_exists, p.inclusion_status FROM canonical_paper_modules pm JOIN papers p ON p.paper_id = pm.paper_id WHERE pm.module_code = ? ORDER BY p.paper_id''', (code,)).fetchall()
    print_rows(rows, max_widths={'title': 56, 'inclusion_status': 24})

def status_summary(conn: sqlite3.Connection, *, all_papers: bool) -> None:
    scope_label = 'all papers' if all_papers else 'active_confirmed_core only'
    print_heading(f'Status Summary ({scope_label})')
    totals = conn.execute(f'''
        SELECT
            COUNT(*) AS paper_count,
            SUM(pdf_exists) AS local_pdf_count,
            SUM(note_exists) AS local_note_count,
            SUM(CASE WHEN lower(trim(COALESCE(source_limited, ''))) LIKE 'yes%' THEN 1 ELSE 0 END) AS source_limited_count
        FROM papers
        {'WHERE active_confirmed_core = 1' if not all_papers else ''}
    ''').fetchone()
    print(json.dumps(dict(totals), ensure_ascii=False, indent=2))
    print()
    print_status_breakdown(conn, 'pdf_status', active_only=not all_papers)
    print_status_breakdown(conn, 'evidence_status', active_only=not all_papers)
    print_status_breakdown(conn, 'note_status', active_only=not all_papers)

def year_summary(conn: sqlite3.Connection) -> None:
    rows = conn.execute('''
        SELECT
            CASE
                WHEN TRIM(COALESCE(year, '')) = '' THEN '(blank)'
                ELSE year
            END AS year,
            COUNT(*) AS total_papers,
            SUM(active_confirmed_core) AS active_confirmed_core_count,
            SUM(CASE WHEN active_confirmed_core = 1 AND pdf_exists = 1 THEN 1 ELSE 0 END) AS active_local_pdf_count,
            SUM(CASE WHEN active_confirmed_core = 1 AND note_exists = 1 THEN 1 ELSE 0 END) AS active_note_count,
            SUM(CASE WHEN active_confirmed_core = 1 AND lower(trim(COALESCE(source_limited, ''))) LIKE 'yes%' THEN 1 ELSE 0 END) AS active_source_limited_count
        FROM papers
        GROUP BY 1
        ORDER BY
            CASE WHEN year GLOB '[0-9][0-9][0-9][0-9]' THEN CAST(year AS INTEGER) ELSE -1 END DESC,
            year DESC
    ''').fetchall()
    print_rows(rows)

def source_summary(conn: sqlite3.Connection) -> None:
    rows = conn.execute('''
        SELECT
            CASE
                WHEN TRIM(COALESCE(source, '')) = '' THEN '(blank)'
                ELSE source
            END AS source,
            COUNT(*) AS total_papers,
            SUM(active_confirmed_core) AS active_confirmed_core_count,
            SUM(CASE WHEN active_confirmed_core = 1 AND pdf_exists = 1 THEN 1 ELSE 0 END) AS active_local_pdf_count,
            SUM(CASE WHEN active_confirmed_core = 1 AND note_exists = 1 THEN 1 ELSE 0 END) AS active_note_count,
            SUM(CASE WHEN active_confirmed_core = 1 AND lower(trim(COALESCE(source_limited, ''))) LIKE 'yes%' THEN 1 ELSE 0 END) AS active_source_limited_count
        FROM papers
        GROUP BY 1
        ORDER BY active_confirmed_core_count DESC, total_papers DESC, source
    ''').fetchall()
    print_rows(rows, max_widths={'source': 36})

def coverage_summary(conn: sqlite3.Connection, *, all_papers: bool) -> None:
    rows = conn.execute(f'''
        SELECT
            CASE
                WHEN active_confirmed_core = 1 THEN 'active_confirmed_core'
                ELSE 'inactive_or_non_core'
            END AS scope,
            coverage_state,
            paper_count,
            local_pdf_count,
            local_note_count,
            source_limited_count,
            missing_local_pdf_count,
            missing_note_count,
            needs_followup_count
        FROM coverage_status_summary
        {'' if all_papers else 'WHERE active_confirmed_core = 1'}
        ORDER BY active_confirmed_core DESC, paper_count DESC, coverage_state
    ''').fetchall()
    print_rows(rows)

def boundary_cases(conn: sqlite3.Connection, *, kind: str | None, limit: int, all_papers: bool) -> None:
    filters = []
    params: list[object] = []
    if not all_papers:
        filters.append('active_confirmed_core = 1')
    if kind:
        filters.append('boundary_case_kind = ?')
        params.append(kind)
    else:
        filters.append("drift_class IN ('semantic_drift', 'order_drift')")
    where_clause = ' AND '.join(filters)
    print_heading('Canonical-vs-Mirror Drift Audit')
    rows = conn.execute(f'''
        SELECT
            paper_id,
            title,
            year,
            source,
            scientific_modules_canonical,
            scientific_modules_declared_order,
            normalized_general_method_bucket,
            final_formal_modules_declared_order,
            final_assignments_canonical,
            drift_class,
            boundary_case_kind
        FROM classification_boundary_analysis
        WHERE {where_clause}
        ORDER BY boundary_case_kind, paper_id
        LIMIT ?
    ''', (*params, limit)).fetchall()
    print_rows(rows, max_widths={
        'title': 56,
        'source': 24,
        'scientific_modules_canonical': 28,
        'scientific_modules_declared_order': 28,
        'normalized_general_method_bucket': 30,
        'final_formal_modules_declared_order': 28,
        'final_assignments_canonical': 28,
        'drift_class': 16,
        'boundary_case_kind': 40,
    })

def bucket_summary(conn: sqlite3.Connection, *, limit: int, all_papers: bool) -> None:
    base_filter = '(has_general_method_bucket = 1 OR final_contains_bucket_0104 = 1)'
    if not all_papers:
        base_filter += ' AND active_confirmed_core = 1'

    totals = conn.execute(f'''
        SELECT
            COUNT(*) AS bucket_related_papers,
            SUM(has_general_method_bucket) AS raw_general_bucket_count,
            SUM(final_contains_bucket_0104) AS final_bucket_count,
            SUM(CASE WHEN boundary_case_kind = 'acceptable_mirror' THEN 1 ELSE 0 END) AS acceptable_mirror_count,
            SUM(CASE WHEN boundary_case_kind = 'bucket_replaced_by_formal_modules' THEN 1 ELSE 0 END) AS bucket_replaced_by_formal_modules_count,
            SUM(CASE WHEN boundary_case_kind = 'bucket_added_in_final' THEN 1 ELSE 0 END) AS bucket_added_in_final_count
        FROM classification_boundary_analysis
        WHERE {base_filter}
    ''').fetchone()
    print_heading('01.04 Canonical-vs-Mirror Audit Summary')
    print(json.dumps(dict(totals), ensure_ascii=False, indent=2))
    print()

    summary_rows = conn.execute(f'''
        SELECT
            drift_class,
            boundary_case_kind,
            COUNT(*) AS paper_count
        FROM classification_boundary_analysis
        WHERE {base_filter}
        GROUP BY drift_class, boundary_case_kind
        ORDER BY paper_count DESC, drift_class, boundary_case_kind
    ''').fetchall()
    print_rows(summary_rows, max_widths={'drift_class': 18, 'boundary_case_kind': 40})
    print()

    detail_rows = conn.execute(f'''
        SELECT
            paper_id,
            title,
            scientific_modules_canonical,
            normalized_general_method_bucket,
            final_assignments_canonical,
            drift_class,
            boundary_case_kind
        FROM classification_boundary_analysis
        WHERE {base_filter}
        ORDER BY boundary_case_kind, paper_id
        LIMIT ?
    ''', (limit,)).fetchall()
    print_heading(f'01.04 Bucket Examples (first {limit})')
    print_rows(detail_rows, max_widths={
        'title': 56,
        'scientific_modules_canonical': 28,
        'normalized_general_method_bucket': 30,
        'final_assignments_canonical': 28,
        'drift_class': 18,
        'boundary_case_kind': 40,
    })

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Query ASD analysis SQLite outputs. Default classification commands are canonical-only; workflow mirror/final fields should be interpreted only in explicit audit commands.')
    subparsers = parser.add_subparsers(dest='command', required=True)
    subparsers.add_parser('summary', help='Canonical-only formal module counts for the current structured snapshot')
    subparsers.add_parser('module-distribution', help='Canonical formal module distribution with assignment shares and active-record baseline')
    coverage_mode_parser = subparsers.add_parser('object-coverage-summary', help='Canonical object coverage modes at record level')
    coverage_mode_parser.add_argument('--all', action='store_true', help='Include inactive and non-core papers')
    combo_parser = subparsers.add_parser('multi-module-combo-summary', help='Canonical multi-module combination frequencies')
    combo_parser.add_argument('--all', action='store_true', help='Include inactive and non-core papers')
    combo_parser.add_argument('--limit', type=int, default=20)
    combo_parser.add_argument('--module-count', type=int, help='Filter one canonical module-count size, for example 2 or 3')
    pdf_cov_parser = subparsers.add_parser('module-pdf-coverage', help='Canonical formal-module PDF coverage summary')
    pdf_cov_parser.add_argument('--sort', choices=('module', 'coverage', 'missing'), default='module')
    bucket0104_parser = subparsers.add_parser('bucket-0104-summary', help='Canonical 01.04 bucket summary, separate from mirror audit')
    bucket0104_parser.add_argument('--details', action='store_true', help='Include a paper-level detail sample')
    bucket0104_parser.add_argument('--limit', type=int, default=20)
    paper_parser = subparsers.add_parser('paper', help='Paper detail view including both canonical and workflow-mirror fields for inspection')
    paper_parser.add_argument('paper_id')
    subparsers.add_parser('missing-pdf', help='Local PDF evidence inventory; not a canonical classification count')
    subparsers.add_parser('multi-module', help='Canonical-only active multi-module papers from scientific_object_modules')
    module_parser = subparsers.add_parser('module', help='Canonical-only papers assigned to one formal module code')
    module_parser.add_argument('code')
    status_parser = subparsers.add_parser('status-summary', help='Coverage/workflow status summary, not a canonical classification count')
    status_parser.add_argument('--all', action='store_true', help='Include inactive and non-core papers')
    subparsers.add_parser('year-summary', help='Corpus-level year summary, not a canonical classification count')
    subparsers.add_parser('source-summary', help='Corpus-level source summary, not a canonical classification count')
    coverage_parser = subparsers.add_parser('coverage-summary', help='Coverage/workflow state summary, not a canonical classification count')
    coverage_parser.add_argument('--all', action='store_true', help='Include inactive and non-core papers')
    boundary_parser = subparsers.add_parser('boundary-cases', help='Audit canonical-vs-mirror classification drift; defaults to real drift only')
    boundary_parser.add_argument('--kind', help='Filter a specific boundary_case_kind, including acceptable_mirror if needed')
    boundary_parser.add_argument('--limit', type=int, default=25)
    boundary_parser.add_argument('--all', action='store_true', help='Include inactive and non-core papers')
    bucket_parser = subparsers.add_parser('bucket-summary', help='Audit canonical-vs-mirror 01.04 bucket behavior')
    bucket_parser.add_argument('--limit', type=int, default=20)
    bucket_parser.add_argument('--all', action='store_true', help='Include inactive and non-core papers')
    return parser

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    conn = connect()
    try:
        if args.command == 'summary':
            summary(conn)
        elif args.command == 'module-distribution':
            module_distribution(conn)
        elif args.command == 'object-coverage-summary':
            object_coverage_summary(conn, all_papers=args.all)
        elif args.command == 'multi-module-combo-summary':
            multi_module_combo_summary(conn, all_papers=args.all, limit=args.limit, module_count=args.module_count)
        elif args.command == 'module-pdf-coverage':
            module_pdf_coverage(conn, sort_by=args.sort)
        elif args.command == 'bucket-0104-summary':
            bucket_0104_summary(conn, details=args.details, limit=args.limit)
        elif args.command == 'paper':
            paper(conn, args.paper_id)
        elif args.command == 'missing-pdf':
            missing_pdf(conn)
        elif args.command == 'multi-module':
            multi_module(conn)
        elif args.command == 'module':
            module(conn, args.code)
        elif args.command == 'status-summary':
            status_summary(conn, all_papers=args.all)
        elif args.command == 'year-summary':
            year_summary(conn)
        elif args.command == 'source-summary':
            source_summary(conn)
        elif args.command == 'coverage-summary':
            coverage_summary(conn, all_papers=args.all)
        elif args.command == 'boundary-cases':
            boundary_cases(conn, kind=args.kind, limit=args.limit, all_papers=args.all)
        elif args.command == 'bucket-summary':
            bucket_summary(conn, limit=args.limit, all_papers=args.all)
        else:
            parser.error(f'Unknown command: {args.command}')
    finally:
        conn.close()

if __name__ == '__main__':
    main()
