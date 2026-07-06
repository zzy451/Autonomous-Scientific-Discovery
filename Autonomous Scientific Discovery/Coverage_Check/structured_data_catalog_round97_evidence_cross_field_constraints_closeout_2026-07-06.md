# Structured Data Catalog Round 97 Closeout

日期：2026-07-06

## 本轮目标

继续把 PDF/evidence/asset 这条线从“单字段值域约束”推进到“跨字段一致性约束”，让一些明显应该联动的状态关系在 SQLite 层正式固化。

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. `pdf_evidence_status` 跨字段约束

新增 `CHECK`：

- 不能同时 `is_main_text = 1` 且 `is_supplementary = 1`
- 若 `pdf_evidence_type = 'main_pdf'`
  - 则必须 `is_main_text = 1`
  - 且 `is_supplementary = 0`

- 若 `pdf_evidence_type = 'supplementary_pdf'`
  - 则必须 `is_main_text = 0`
  - 且 `is_supplementary = 1`

- 若 `pdf_check_status = 'source_limited'`
  - 则必须 `source_limited = 'yes'`

- 若 `source_limited = 'yes'`
  - 则必须 `pdf_check_status = 'source_limited'`

- 若 `pdf_check_status = 'full_text_checked'`
  - 则不得同时 `source_limited = 'yes'`

### 2. `paper_assets` 跨字段约束

新增 `CHECK`：

- 不能同时 `is_main_text = 1` 且 `is_supplementary = 1`
- 若 `asset_type = 'note'`
  - 则必须 `is_main_text = 0`
  - 且 `is_supplementary = 0`

### 3. build 自检扩展

扩展 `validate_evidence_sqlite_constraints()`：

- 检查 `pdf_evidence_status` 的上述跨字段 `CHECK` 片段
- 检查 `paper_assets` 的上述跨字段 `CHECK` 片段

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

本轮把 PDF/evidence/asset surfaces 的一部分关键逻辑从“脚本/人工理解上的一致性”推进成了“数据库显式约束的一致性”，这比只限制单字段枚举更接近长期方案里要的稳定结构底座。

## 后续状态

当前无代码级阻塞，worktree 在提交前可收口为干净状态。
