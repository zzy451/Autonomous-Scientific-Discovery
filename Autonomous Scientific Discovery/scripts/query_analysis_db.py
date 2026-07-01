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

def print_rows(rows: Sequence[sqlite3.Row]) -> None:
    if not rows:
        print('No rows found.')
        return
    headers = rows[0].keys()
    print('\t'.join(headers))
    for row in rows:
        print('\t'.join('' if value is None else str(value) for value in row))

def summary(conn: sqlite3.Connection) -> None:
    meta = {row['key']: row['value'] for row in conn.execute('SELECT key, value FROM metadata')}
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    print()
    rows = conn.execute('''SELECT module_code, active_confirmed_core_count FROM module_assignment_counts WHERE assignment_scope = 'scientific_object_modules' ORDER BY module_code''').fetchall()
    print_rows(rows)

def paper(conn: sqlite3.Connection, paper_id: str) -> None:
    row = conn.execute('SELECT * FROM papers WHERE paper_id = ?', (paper_id,)).fetchone()
    if row is None:
        print(f'Paper not found: {paper_id}')
        return
    payload = dict(row)
    for key in ('agent_type_json', 'research_workflow_role_json', 'validation_type_json', 'scientific_contribution_type_json', 'scientific_object_modules_json', 'final_modules_or_bucket_json'):
        payload[key] = json.loads(payload[key])
    payload['paper_modules'] = [
        dict(module_row)
        for module_row in conn.execute('SELECT assignment_scope, module_code, module_kind, sort_order FROM paper_modules WHERE paper_id = ? ORDER BY assignment_scope, sort_order', (paper_id,))
    ]
    print(json.dumps(payload, ensure_ascii=False, indent=2))

def missing_pdf(conn: sqlite3.Connection) -> None:
    rows = conn.execute('SELECT paper_id, title, doi, pdf_status, evidence_status, source_limited FROM missing_pdf_inventory ORDER BY paper_id').fetchall()
    print_rows(rows)

def multi_module(conn: sqlite3.Connection) -> None:
    rows = conn.execute('''SELECT paper_id, title, primary_module_for_filing, scientific_object_modules_json FROM papers WHERE active_confirmed_core = 1 AND object_coverage_mode = 'multi_module' ORDER BY paper_id''').fetchall()
    print_rows(rows)

def module(conn: sqlite3.Connection, code: str) -> None:
    rows = conn.execute('''SELECT p.paper_id, p.title, p.primary_module_for_filing, p.pdf_exists, p.inclusion_status FROM paper_modules pm JOIN papers p ON p.paper_id = pm.paper_id WHERE pm.assignment_scope = 'scientific_object_modules' AND pm.module_code = ? ORDER BY p.paper_id''', (code,)).fetchall()
    print_rows(rows)

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Query ASD analysis SQLite outputs')
    subparsers = parser.add_subparsers(dest='command', required=True)
    subparsers.add_parser('summary')
    paper_parser = subparsers.add_parser('paper')
    paper_parser.add_argument('paper_id')
    subparsers.add_parser('missing-pdf')
    subparsers.add_parser('multi-module')
    module_parser = subparsers.add_parser('module')
    module_parser.add_argument('code')
    return parser

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    conn = connect()
    try:
        if args.command == 'summary':
            summary(conn)
        elif args.command == 'paper':
            paper(conn, args.paper_id)
        elif args.command == 'missing-pdf':
            missing_pdf(conn)
        elif args.command == 'multi-module':
            multi_module(conn)
        elif args.command == 'module':
            module(conn, args.code)
        else:
            parser.error(f'Unknown command: {args.command}')
    finally:
        conn.close()

if __name__ == '__main__':
    main()
