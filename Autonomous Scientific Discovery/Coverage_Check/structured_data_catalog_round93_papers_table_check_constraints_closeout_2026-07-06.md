# Structured Data Catalog Round 93 Closeout

日期：2026-07-06

## 本轮目标

继续把 `papers` 主表从“字段齐全”推进到“字段语义受数据库约束”，把一批已经冻结语义的枚举字段和 duplicate linkage 约束正式固化到 SQLite。

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. `papers` 主表新增 / 固化的 `CHECK` 约束

以下字段现在在 SQLite 中受显式枚举约束：

- `secondary_class_source`
  - `legacy`
  - `normalized`
  - `manual_override`

- `secondary_class_confidence`
  - `high`
  - `medium`
  - `low`

- `secondary_class_review_status`
  - `unreviewed`
  - `reviewed`
  - `needs_split`
  - `needs_merge`

- `object_coverage_mode`
  - `single_module`
  - `multi_module`
  - `general_method_without_concrete_object_experiments`

- `primary_module_confidence`
  - `high`
  - `medium`
  - `low`
  - 允许空字符串 / `NULL`

- `primary_module_assignment_rule`
  - `main_scientific_object`
  - `main_validation_object`
  - `direct_contribution_target`
  - `substantive_application_object`
  - `manual_override`
  - 允许空字符串 / `NULL`

- `classification_source_confidence`
  - `high`
  - `medium`
  - `low`

- `classification_parser_rule`
  - `structured_remark_token`
  - `legacy_general_method_fallback`
  - `legacy_main_class_fallback`
  - `needs_review`

- `record_status`
  - `candidate`
  - `active_confirmed_core`
  - `background_only`
  - `excluded`
  - `duplicate`
  - `retired`

### 2. `duplicate_of` 约束

在上一轮自引用外键的基础上，本轮再新增：

- `CHECK (duplicate_of IS NULL OR duplicate_of <> paper_id)`

即：duplicate linkage 不能自指向自己。

### 3. blank-to-null 兼容

继续在 SQLite 期望值和插入值中对 `duplicate_of` 使用 `blank_to_none()`，避免空字符串触发不必要的关系问题。

### 4. build 自检扩展

新增 `validate_papers_sqlite_constraints()`：

- 直接读取 `sqlite_master` 中 `papers` 的建表 SQL
- 检查上述关键 `CHECK` 片段都真实存在

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

额外 SQLite 证据：

`sqlite_master` 中 `papers` 的建表 SQL 已包含：

- secondary class source/confidence/review status 枚举
- object coverage mode 枚举
- primary module confidence / assignment rule 枚举
- classification source confidence / parser rule 枚举
- `record_status` 枚举
- `duplicate_of` 自引用外键
- `CHECK (duplicate_of IS NULL OR duplicate_of <> paper_id)`

## 产出判断

本轮把 `papers` 主表的一批“已经在治理文件中冻结语义”的字段正式推进为数据库约束，使主表本身更像长期稳定的数据模型，而不是单纯的平铺快照。

## 后续状态

当前无代码级阻塞，worktree 在提交前可收口为干净状态。
