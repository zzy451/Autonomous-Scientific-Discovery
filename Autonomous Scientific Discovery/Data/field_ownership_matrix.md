# ASD Field Ownership Matrix

日期：2026-07-05

本文档锁定 ASD 结构化数据的字段 owner。任何 registry、CSV、SQLite、manifest 或 derived snapshot 若与 owner 冲突，必须回到 owner 文件修正后重新导出。

## 1. Fact Source Classes

| Source class | Owner file | Scope |
|---|---|---|
| Paper and classification facts | `Paper_Lists/agent_master_paper_list.md` | Paper identity, metadata, inclusion status, legacy class fields, canonical classification overlay, filing module |
| Source / PDF / progress facts | `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md` | PDF/source/evidence workflow state, source-limited state, progress closeout |
| Discipline code assignment facts | `Data/discipline_code_assignments.jsonl` | Stable discipline-local code assignments and assignment lifecycle state |
| Taxonomy vocabulary facts | `Data/classification_code_index.json` | Primary and secondary taxonomy term labels, definitions, include/exclude boundaries, term status |

## 2. Core Field Owners

| Field family | Canonical owner | Derived consumers | Notes |
|---|---|---|---|
| `paper_id` | master | all Data outputs, notes, SQLite | Permanent key; never changes after assignment |
| title, authors, year, venue/source, DOI/URL | master | registries, CSV, SQLite, notes | Registry copies are display snapshots |
| `inclusion_status`, active/core record state | master-derived lane | `papers.jsonl`, SQLite | Lifecycle may later receive a dedicated owner, but first pass remains master-derived |
| `legacy_main_class`, `legacy_secondary_class`, `legacy_tertiary_class` | master | code preview, classification index seeding | First-pass source for secondary filing position |
| `scientific_object_modules` | master-derived canonical lane | `classification_assignments.jsonl`, `paper_modules`, SQLite | Array of formal `01-11` modules only |
| `general_method_bucket` | master-derived canonical lane | registry, SQLite | `01.04` only lives here, never in `scientific_object_modules` |
| `object_coverage_mode` | master-derived canonical lane | registry, SQLite | Expected values: `single_module`, `multi_module`, `general_method_without_concrete_object_experiments` |
| `primary_module_for_filing` | master-derived canonical lane | notes directory policy, discipline code assignment | Filing convenience, not full classification fact |
| `primary_module_confidence`, `primary_module_assignment_rule`, `primary_module_override_reason` | master-derived canonical lane or future policy note | registry / check report | Required when filing choice is ambiguous |
| `pdf_status`, `evidence_status`, `source_limited`, `closed` | progress | PDF registry, manifests, SQLite | Do not infer full-text status from `pdf_path` alone |
| `pdf_evidence_type`, `pdf_check_status`, `source_checked_at` | generated PDF/evidence layer from progress + remarks provenance + change-log fallback | PDF registry, manifests, SQLite | Derived evidence-layer fields; repair owner records first, then regenerate |
| `note_path` | export resolution from master/progress | note manifest, registry | Fallback order must remain explicit in export code |
| `pdf_path` | export resolution from progress/master | PDF registry, asset manifest | Fallback order must remain explicit in export code |
| `assignment_id` | `discipline_code_assignments.jsonl` | registry, SQLite | `DCA-000001` monotonic ledger ID; never reused |
| `discipline_local_code` | `discipline_code_assignments.jsonl` | registry, CSV, SQLite | Stable shelf/display code; not permanent paper key |
| `assignment_status` | `discipline_code_assignments.jsonl` | registry, check report, SQLite | Controlled values defined in `discipline_code_assignment_policy.md` |
| `assigned_at`, `assigned_by`, `retired_at`, `redirected_to_code`, `assignment_reason`, `pending_reason` | `discipline_code_assignments.jsonl` | registry, SQLite | Assignment lifecycle metadata |
| `discipline_local_rank` | derived from `discipline_local_code` | registry, CSV, SQLite | `parse_NNN(discipline_local_code)` only; never hand-maintained |
| taxonomy term label, definition, include/exclude boundary, status, source | `classification_code_index.json` | registry, check report, SQLite `classification_terms` | Taxonomy vocabulary facts, not derived from papers |
| `asset_sha256`, `asset_size_bytes`, `asset_type`, `is_main_text`, `is_supplementary` | generated asset/PDF registry from files + progress | manifests, SQLite | Hash/size come from local files; semantic type comes from progress/export rules |

## 3. Master-Derived Canonical Lane

Current first-pass parser order:

```text
source_file: Paper_Lists/agent_master_paper_list.md
fallback_order:
  1. explicit canonical field when present
  2. structured remark token
  3. legacy class fallback
  4. mark as needs_review
required_trace_fields:
  - source_field
  - source_confidence
  - parser_rule
```

Until master rows receive explicit canonical columns, export code must preserve source trace metadata for any classification value inferred from remarks or legacy fallback.

## 4. Derived Layer Guardrails

- `Data/registry/*.jsonl`, `papers.jsonl`, CSV exports, manifests, and SQLite tables are derived unless explicitly listed above as owner files.
- `discipline_code_assignments.jsonl` and `classification_code_index.json` are exceptions inside `Data/`: they own management-code and taxonomy-vocabulary facts.
- Do not fix derived drift by hand-editing derived outputs.
- If a field conflict is found, repair the owner file, then rerun `export -> check -> build`.
