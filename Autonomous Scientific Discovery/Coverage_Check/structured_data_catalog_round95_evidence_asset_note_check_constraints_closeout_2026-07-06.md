# Structured Data Catalog Round 95 Closeout

日期：2026-07-06

## 本轮目标

继续把 PDF/evidence/asset/notes 这条结构线从“字段能存值”推进到“字段值受数据库语义约束”，让这批 analysis surfaces 不再只靠脚本默认值域成立。

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. `pdf_evidence_status` 约束

新增 `CHECK`：

- `pdf_exists IN (0, 1)`
- `pdf_evidence_type IN (...)`
  - `main_pdf`
  - `supplementary_pdf`
  - `html_full_text`
  - `abstract`
  - `official_page`
  - `project_page`

- `pdf_check_status IN (...)`
  - `full_text_checked`
  - `source_limited`
  - `metadata_only`

- `is_main_text IN (0, 1)`
- `is_supplementary IN (0, 1)`
- `source_limited IN ('', 'no', 'yes')` 或 `NULL`
- `active_confirmed_core IN (0, 1)`

### 2. `paper_assets` 约束

新增 `CHECK`：

- `asset_type IN ('note', 'primary_pdf')`
- `asset_exists IN (0, 1)`
- `is_main_text IN (0, 1)`
- `is_supplementary IN (0, 1)`
- `source_limited IN ('', 'no', 'yes')` 或 `NULL`

### 3. `notes` / `note_inventory` / `pdf_inventory` 约束

新增 `CHECK`：

- `notes.note_exists IN (0, 1)`
- `notes.active_confirmed_core IN (0, 1)`
- `note_inventory.note_exists IN (0, 1)`
- `note_inventory.active_confirmed_core IN (0, 1)`
- `pdf_inventory.active_confirmed_core IN (0, 1)`

### 4. build 自检扩展

新增 `validate_evidence_sqlite_constraints()`：

- 从 `sqlite_master` 读取：
  - `pdf_evidence_status`
  - `paper_assets`
  - `notes`
  - `pdf_inventory`
  - `note_inventory`

- 检查上述关键 `CHECK` 片段都真实写入表定义

## 验证

运行：

```bash
python "Autonomous Scientific Discovery/scripts/run_structured_data_pipeline.py" --with-execution-audit
```

结果：

- `export_structured_data.py` 通过
- `check_data_consistency.py` 通过
- `build_analysis_db.py` 通过
- `audit_execution_definition.py` 通过

执行定义审计结果：

- `PASS=12`
- `FAIL=0`

## 产出判断

本轮把 PDF/evidence/asset/notes surfaces 的一批固定值域正式推进为 SQLite 约束，使：

- evidence type
- evidence check depth
- asset type
- 各类布尔位
- `source_limited`

都不再只是脚本生成约定，而是在数据库层具备正式边界。

## 后续状态

当前无代码级阻塞，worktree 在提交前可收口为干净状态。
