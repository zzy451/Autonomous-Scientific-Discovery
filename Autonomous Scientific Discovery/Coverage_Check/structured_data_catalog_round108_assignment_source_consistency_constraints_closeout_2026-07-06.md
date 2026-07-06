# Structured Data Catalog Round 108 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 `discipline_code_assignments` 一阶段来源字段的内部一致性正式压进 SQLite owner-load 层，而不只依赖外层 schema / checker。

对应方案要求：

- 第一阶段二级位来源来自当前 `legacy Secondary class`
- `primary_taxonomy_code_2lvl` 与稳定 code 前缀要一致
- `source_primary_module_for_filing` 是当前主排架位来源记录，不应与最终 code / taxonomy 前缀脱钩
- `assignment_reason` 是账本可审计字段，不应只是空壳字符串

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 收紧 ledger 的 `assignment_reason` 语义

为 SQLite `discipline_code_assignments` 表新增：

- `assignment_reason TEXT NOT NULL CHECK (trim(assignment_reason) <> '')`

这样账本解释字段不再允许以空字符串占位。

### 2. 收紧 assigned-code 行的来源一致性

对 `assignment_status IN ('active_code', 'retired_code', 'redirected_code')` 的行新增更强 `CHECK`：

- `source_primary_module_for_filing` 必须非空
- `source_legacy_secondary_class` 必须非空
- `source_legacy_secondary_class = primary_taxonomy_code_2lvl`
- `source_primary_module_for_filing = substr(discipline_local_code, 1, 2)`
- `source_primary_module_for_filing = substr(primary_taxonomy_code_2lvl, 1, 2)`

这把第一阶段“二级位来自 legacy secondary class、一级位来自 filing primary” 的关系正式压进账本导入表。

### 3. 收紧 pending / general-method 的 source-primary 语义

新增：

- `pending_secondary` 行：
  - 若 `pending_reason = 'missing_primary_module_for_filing'`，则 `source_primary_module_for_filing IS NULL`
  - 否则 `source_primary_module_for_filing` 必须非空

- `non_discipline_general_method` 行：
  - `source_primary_module_for_filing IS NULL`

这样 pending / pure general-method 两类 current state 在账本里也有更明确的来源字段边界。

### 4. build 自检补充来源一致性查询

在 `validate_owner_loaded_and_inventory_tables()` 中新增 SQLite 查询级自检：

- 空白 `assignment_reason`
- assigned-code 行缺失或错配 `source_primary_module_for_filing`
- assigned-code 行 `source_legacy_secondary_class <> primary_taxonomy_code_2lvl`
- pending 行与 `missing_primary_module_for_filing` 之间的 source-primary 关系错误
- general-method 行错误携带 `source_primary_module_for_filing`

任一出现即直接中止 build。

### 5. discipline SQLite schema 文本检查同步扩展

`validate_discipline_sqlite_constraints()` 现在也会检查上述来源一致性约束片段已经真实写入 `discipline_code_assignments` 建表 SQL 中，而不是只依赖运行时查询。

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

补充核对：

- 当前 `discipline_code_assignments` 中：
  - 空白 `assignment_reason` 数为 `0`
  - assigned-code 行 source-primary / code-prefix 错配数为 `0`
  - assigned-code 行 `source_legacy_secondary_class <> primary_taxonomy_code_2lvl` 数为 `0`
  - pending 行 source-primary 语义错配数为 `0`
  - general-method 行错误携带 source-primary 数为 `0`

## 产出判断

本轮把 discipline ledger 的“一阶段来源字段”推进成了真正受约束的结构化字段，而不是仅仅作为旁注保存。这让 ledger 更接近方案中所要求的“稳定管理码账本 + 可解释来源记录”。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
