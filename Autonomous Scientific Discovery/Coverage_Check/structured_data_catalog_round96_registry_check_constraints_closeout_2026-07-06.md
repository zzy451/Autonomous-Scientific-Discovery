# Structured Data Catalog Round 96 Closeout

日期：2026-07-06

## 本轮目标

继续把 `discipline_local_code_registry` 从“derived snapshot 有字段”推进到“derived snapshot 的冻结语义受数据库约束”，让 registry 表本身更像长期稳定的数据模型。

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. `discipline_local_code_registry` 新增 `CHECK` 约束

新增 / 固化：

- `primary_module_confidence`
  - `'' / high / medium / low / NULL`

- `primary_module_assignment_rule`
  - `'' / main_scientific_object / main_validation_object / direct_contribution_target / substantive_application_object / manual_override / NULL`

- `secondary_class_source`
  - `legacy / normalized / manual_override / NULL`

- `secondary_class_confidence`
  - `high / medium / low / NULL`

- `secondary_class_review_status`
  - `unreviewed / reviewed / needs_split / needs_merge / NULL`

- `general_method_bucket`
  - `none / 01.04_general_asd_methods_without_concrete_object_experiments / NULL`

- `active_confirmed_core IN (0, 1)`
- `worktree_dirty IN (0, 1)`

这些约束建立在当前 governance 语义和现有导出值分布之上，覆盖了 registry 里最核心的一批枚举与布尔字段。

### 2. build 自检扩展

扩展 `validate_discipline_sqlite_constraints()`：

- 直接检查 `discipline_local_code_registry` 的建表 SQL 中是否包含上述关键 `CHECK` 片段

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

本轮把 registry 表中一批已经冻结的语义正式推进成 SQLite 约束，使 `discipline_local_code_registry` 更接近长期方案里“derived snapshot 也要有稳定结构边界”的要求，而不是只靠脚本约定保持字段值域。

## 后续状态

当前无代码级阻塞，worktree 在提交前可收口为干净状态。
