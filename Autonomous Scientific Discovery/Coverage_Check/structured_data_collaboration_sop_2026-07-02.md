# ASD structured-data 协作 SOP

日期：2026-07-02
对应阶段：`structured_data_post_phase2_execution_plan_2026-07-02.md` 的 `Phase 5`

本文档面向协作者，解决一个具体问题：当你准备新增论文、改分类、补 PDF、改 note path、重建 Data、提交 PR 时，第一步到底该改哪里，哪些文件绝不能手改，改完后还必须跑什么。

## 1. 适用范围与红线

本 SOP 适用于当前 `Autonomous Scientific Discovery` structured-data 协作。

当前只有两份 authoritative pair 可以产生 structured facts：

1. `Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md`
2. `Autonomous Scientific Discovery/Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`

红线：

- 不要把 `Data/*.json*`、`Data/*.csv`、`Data/*.sqlite` 当成修事实入口
- 不要把 `final_modules_or_bucket` 当 canonical classification source
- 不要把 `primary_module_for_filing` 当完整分类事实
- 不要把 `pdf_path` 非空或 “看过全文” 当成本地真 PDF 证据
- 不要让子 Agent 改 master / progress / report

独立红线文件清单见：

- `Coverage_Check/structured_data_red_line_files_2026-07-03.md`

## 2. 先判断你在改哪一层

### 2.1 master 层

以下改动默认先落到 master：

- 新增论文主记录
- 改 `inclusion_status`
- 改 canonical classification
- 改 `Note path`
- 改论文元信息、DOI / URL、legacy filing fields

### 2.2 progress 层

以下改动默认先落到 progress：

- 改 `pdf_status`
- 改 `pdf_path`
- 改 `evidence_status`
- 改 `source_limited`
- 改 `final_modules_or_bucket`
- 改 `note_status` / `master_status` / `batch` / `closed`

### 2.3 derived 层

以下文件只能重建，不能手改来“修事实”：

- `Data/papers.jsonl`
- `Data/papers.csv`
- `Data/paper_modules.csv`
- `Data/canonical_paper_modules.csv`
- `Data/workflow_mirror_paper_modules.csv`
- `Data/papers.sqlite`
- `Data/registry/*`
- `Data/*manifest*.json`

## 3. 六类高频动作速查表

| 动作 | 第一落点 | 不应先改的地方 | 改完后必须做什么 |
|---|---|---|---|
| 新增论文 | master | `Data/`、SQLite、CSV | `export -> check -> build` |
| 改分类 | master remarks overlay | `paper_modules.csv`、`final_modules_or_bucket` | `export -> check -> build` |
| 改 PDF 状态 | progress | master `PDF path`、manifest | `export -> check -> build` |
| 改 note path | master `Note path` | `note_manifest.json` | `export -> check -> build` |
| 重建 Data | scripts | 手改 Data | 按固定顺序重建 |
| 提交 PR | PR 模板 | 口头说明替代模板 | 填完整模板并附验证输出 |

## 4. 动作 A：新增论文

1. 先在 `agent_master_paper_list.md` 新增主记录。
2. 若该条目进入当前 workflow，再补 progress 对应行。
3. 不要先写 `Data/`、SQLite、CSV。
4. 运行：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

## 5. 动作 B：改分类

默认先改 master `Remarks` 中的 canonical classification overlay：

- `scientific_object_modules=...`
- `general_method_bucket=...`
- `object_coverage_mode=...`
- `primary_module_for_filing=...`

不要把这些改动先落到：

- `Data/papers.jsonl`
- `Data/paper_modules.csv`
- `Data/canonical_paper_modules.csv`
- `papers.sqlite`
- progress `final_modules_or_bucket`

说明：

- `scientific_object_modules + general_method_bucket` 才是 canonical classification
- `final_modules_or_bucket` 只是 workflow mirror

## 6. 动作 C：改 PDF 状态

默认先改 progress：

- `pdf_status`
- `pdf_path`
- `evidence_status`
- `source_limited`

注意：

- `pdf_path` 只是路径字段，不等于本地真 PDF
- 本地真 PDF 判断最终看导出后的 `pdf_exists`、`pdf_manifest.json`、实际文件可读性

## 7. 动作 D：改 note path

默认先改 master 的 `Note path`。

当前导出虽然允许 `progress.note_path or master.Note path` 的兼容性回退，但这不改变 master 仍是默认主 ownership。

## 8. 动作 E：重建 Data

固定顺序只能是：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

不要只跑 `build_analysis_db.py`。

## 9. 动作 F：提交 PR

提交前至少完成：

1. 填 `.github/PULL_REQUEST_TEMPLATE.md`
2. 说明是否改了 authoritative pair
3. 若 baseline 变化，按 `structured_data_baseline_update_rules_2026-07-02.md` 补完整证据
4. 粘贴 `check_data_consistency.py` 关键输出
5. 说明实际跑过的 `query_analysis_db.py` 命令

## 10. 提交前 30 秒检查清单

- 我这次改动的第一落点是不是在 authoritative pair，而不是 `Data/`
- 我有没有把 canonical classification 和 workflow mirror 混用
- 我有没有把 `01.04` 混回 formal `01-11`
- 我有没有把 `pdf_path` 非空误当作真 PDF
- 我有没有按 `export -> check -> build` 重建
- `check_data_consistency.py` 是否严格通过
- PR 模板是否填完整

## 11. 常见误操作与纠正方式

### 误操作 1

直接改 `Data/papers.jsonl` 修分类。

纠正：

回到 master `Remarks` 改 canonical overlay，再重建。

### 误操作 2

直接改 `paper_modules.csv` 做模块统计修正。

纠正：

回到 authoritative pair 修事实，再重建；正式统计优先走 SQLite `canonical_*` 视图。

### 误操作 3

把 `final_modules_or_bucket` 当“最终分类”。

纠正：

把它当 workflow mirror；真正分类只看 `scientific_object_modules + general_method_bucket`。

### 误操作 4

只跑 `build_analysis_db.py`。

纠正：

必须重跑 `export -> check -> build`。
