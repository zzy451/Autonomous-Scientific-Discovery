# Structured Data Catalog Round 94 Closeout

日期：2026-07-06

## 本轮目标

继续把 module / bucket 这批核心 analysis surfaces 从“字段能存值”推进到“字段值受数据库语义约束”，让 canonical module rows、workflow mirror rows 和 general-method bucket rows 的结构语义在 SQLite 层固定下来。

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. `papers.general_method_bucket` 约束

新增 `CHECK`：

- `general_method_bucket IN ('none', '01.04_general_asd_methods_without_concrete_object_experiments')`

这让 `papers` 主表中 general-method bucket 的当前冻结语义在数据库层正式固化。

### 2. `paper_modules` 约束

新增 `CHECK`：

- `assignment_scope = 'scientific_object_modules'`
- `module_kind IN ('formal_module', 'general_bucket')`
- `is_primary_for_filing IN (0, 1)`
- `confidence IN ('', 'high', 'medium', 'low')` 或 `NULL`
- `source IN ('primary_module_for_filing', 'scientific_object_modules')`

### 3. `workflow_mirror_paper_modules` 约束

新增 `CHECK`：

- `assignment_scope = 'final_modules_or_bucket'`
- `module_kind IN ('formal_module', 'general_bucket')`
- `is_primary_for_filing IN (0, 1)`
- `confidence IN ('', 'high', 'medium', 'low')` 或 `NULL`
- `source = 'final_modules_or_bucket'`

### 4. `paper_general_method_buckets` 约束

新增 `CHECK`：

- `general_method_bucket = '01.04_general_asd_methods_without_concrete_object_experiments'`
- `active_confirmed_core IN (0, 1)`

这让 general-method bucket surface 不再只是“某个字符串列”，而是明确限定为当前项目冻结的单一 bucket 语义。

### 5. build 自检扩展

新增 `validate_module_sqlite_constraints()`：

- 从 `sqlite_master` 读取：
  - `papers`
  - `paper_modules`
  - `workflow_mirror_paper_modules`
  - `paper_general_method_buckets`

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

额外 SQLite 证据：

`sqlite_master` 当前已包含：

- `papers.general_method_bucket` 的固定枚举约束
- `paper_modules` 的 canonical-scope / source / confidence 约束
- `workflow_mirror_paper_modules` 的 mirror-scope / source / confidence 约束
- `paper_general_method_buckets` 的固定 bucket 约束

## 产出判断

本轮把 module / bucket surfaces 的若干关键语义正式推进成数据库约束，使 canonical module rows、workflow mirror rows 和 general-method bucket rows 更接近长期方案里的稳定结构，而不是只靠脚本生成约定。

## 后续状态

当前无代码级阻塞，worktree 在提交前可收口为干净状态。
