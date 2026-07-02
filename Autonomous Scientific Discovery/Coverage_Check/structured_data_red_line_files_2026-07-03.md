# ASD structured-data 红线文件清单

日期：2026-07-03
对应阶段：`structured_data_post_phase2_execution_plan_2026-07-02.md` 的 `Phase 5`

本文档把“哪些文件不能当修事实入口、哪些文件必须由 Main Controller 单写、哪些文件只能重建”单点列清，供协作者和子 Agent 直接引用。

## 1. authoritative pair

只有以下两份文件可以产生 structured facts：

1. `Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md`
2. `Autonomous Scientific Discovery/Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`

## 2. Main Controller 单写红线

以下文件默认只能由 Main Controller 收口：

- `Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md`
- `Autonomous Scientific Discovery/Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- `Autonomous Scientific Discovery/Coverage_Check/*report*.md`
- `Autonomous Scientific Discovery/Coverage_Check/*audit*.md`
- `Autonomous Scientific Discovery/Coverage_Check/*closeout*.md`
- `Autonomous Scientific Discovery/Coverage_Check/*launch_status*.md`

子 Agent 不得直接修改以上文件。

## 3. 只能重建、不能手改的派生层

以下文件或目录只能由脚本重建，不能手改来“修事实”：

- `Autonomous Scientific Discovery/Data/papers.jsonl`
- `Autonomous Scientific Discovery/Data/papers.csv`
- `Autonomous Scientific Discovery/Data/paper_modules.csv`
- `Autonomous Scientific Discovery/Data/canonical_paper_modules.csv`
- `Autonomous Scientific Discovery/Data/workflow_mirror_paper_modules.csv`
- `Autonomous Scientific Discovery/Data/papers.sqlite`
- `Autonomous Scientific Discovery/Data/pdf_manifest.json`
- `Autonomous Scientific Discovery/Data/missing_pdf_manifest.json`
- `Autonomous Scientific Discovery/Data/note_manifest.json`
- `Autonomous Scientific Discovery/Data/taxonomy_index.json`
- `Autonomous Scientific Discovery/Data/registry/`

## 4. mixed-scope 警告对象

以下对象不是默认 canonical-only 统计入口：

- `Autonomous Scientific Discovery/Data/paper_modules.csv`
- SQLite `paper_modules`
- SQLite `module_assignment_counts`

它们同时包含 canonical 与 workflow mirror assignment 信息。若必须使用，必须先按 `assignment_scope` 过滤；默认统计优先使用 `canonical_*` 视图或 `canonical_paper_modules.csv`。

## 5. 常见错误红线

- 不要把 `final_modules_or_bucket` 当 canonical classification source。
- 不要把 `primary_module_for_filing` 当完整分类事实。
- 不要把 `pdf_path` 非空或 “读过全文” 直接当作本地真 PDF。
- 不要从 `Data/`、CSV、SQLite、manifest 反推并手改 baseline。
- 不要让子 Agent 改 master / progress / report。

## 6. 固定重建顺序

只要 authoritative pair 或派生脚本发生变化，默认重建顺序是：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```
