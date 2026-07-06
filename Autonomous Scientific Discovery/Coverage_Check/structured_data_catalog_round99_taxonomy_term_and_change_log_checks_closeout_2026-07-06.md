# Structured Data Catalog Round 99 Closeout

日期：2026-07-06

## 本轮目标

继续把 owner / taxonomy 这条线的结构语义推进到 SQLite，不只保留外键，还把 `classification_terms` 和 `change_log` 的稳定值域与层级规则正式固化。

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. `classification_terms` 约束增强

新增 / 固化：

- `status IN ('active', 'deprecated', 'needs_review')`
- `review_status IN ('unreviewed', 'reviewed', 'needs_split', 'needs_merge')` 或 `NULL`
- `term_level = 'primary'` 时必须 `review_status IS NULL`
- `term_level = 'secondary'` 时必须 `review_status IS NOT NULL`

这和当前 taxonomy owner schema 的语义保持一致，也让 primary / secondary term 的层级差异在数据库层更明确。

### 2. `change_log` 约束增强

新增 / 固化：

- `change_id` 格式约束：
  - `CL-000001` 风格

- `changed_at` 日期格式约束：
  - `YYYY-MM-DD`

- `related_commit` 约束：
  - 可为空
  - 若非空，则必须匹配当前使用的十六进制 commit hash 形式

### 3. build 自检扩展

扩展 `validate_reference_owner_foreign_keys()`：

- 读取 `change_log` 与 `classification_terms` 的建表 SQL
- 检查上述关键 `CHECK` 片段都真实写入 `sqlite_master`

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

本轮把 taxonomy owner 和 change-log owner 这两条线从“有表、有关系”继续推进成“有关系且有稳定值域边界”，让 owner layer 的导入表在 SQLite 中更接近正式数据模型，而不是仅作为松散载体。

## 后续状态

当前无代码级阻塞，worktree 在提交前可收口为干净状态。
