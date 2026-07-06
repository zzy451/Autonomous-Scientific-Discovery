# Structured Data Catalog Round 109 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 `discipline_local_code_registry` 里 current snapshot 的主排架位、二级位和 pure general-method 语义关系正式压进 SQLite schema 与 build 自检，而不只依赖 export 逻辑或上层 checker。

对应方案要求：

- active current row 的 `discipline_local_code`、`primary_taxonomy_code_2lvl`、`primary_module_for_filing` 必须相互对齐
- 第一阶段二级位仍显式来自 `legacy_secondary_class`
- pending current row 的 `primary_module_for_filing` 应与 `pending_reason` 语义一致
- pure `01.04` general-method-only current row 不应携带 formal filing module，且应保持 `general_method_bucket=01.04` 与空 scientific-object array

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 收紧 active current row 的 primary/secondary 对齐语义

为 SQLite `discipline_local_code_registry` 的 active row 新增更强 `CHECK`：

- `primary_module_for_filing` 必须非空
- `primary_module_for_filing = substr(discipline_local_code, 1, 2)`
- `primary_module_for_filing = substr(primary_taxonomy_code_2lvl, 1, 2)`
- `legacy_secondary_class = primary_taxonomy_code_2lvl`

这让 current snapshot 不再只是“把 paper facts 和 ledger facts拼在一起”，而是明确要求它们在 active row 上保持一致。

### 2. 收紧 pending current row 的 primary-module 语义

新增：

- `pending_reason = 'missing_primary_module_for_filing'` 时：
  - `primary_module_for_filing IS NULL`

- 其他 `pending_secondary` 行：
  - `primary_module_for_filing` 必须非空

这把 pending row 的当前排架位不确定性表达得更精确。

### 3. 收紧 pure general-method current row 的对象字段语义

新增：

- `assignment_status = 'non_discipline_general_method'` 时：
  - `primary_module_for_filing IS NULL`
  - `general_method_bucket = '01.04_general_asd_methods_without_concrete_object_experiments'`
  - `scientific_object_modules_json = '[]'`

这让 current snapshot 中的 pure general-method row 也显式保持和方案一致。

### 4. build 自检补充 current-snapshot 对齐查询

在 `validate_discipline_local_code_registry_outputs()` 中新增 SQLite 查询级自检：

- active row 的 `primary_module_for_filing / discipline_local_code / primary_taxonomy_code_2lvl / legacy_secondary_class` 对齐违规
- pending row 与 `missing_primary_module_for_filing` 之间的 primary-module 语义违规
- non-discipline general-method row 的 formal-module / bucket / object-array 语义违规

任一出现即直接中止 build。

### 5. discipline SQLite schema 文本检查同步扩展

`validate_discipline_sqlite_constraints()` 现在也会检查上述 registry alignment 约束片段已经真实写入 SQLite 建表 SQL 中，而不是只依赖运行时查询。

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

- 当前 `discipline_local_code_registry` 中：
  - active row primary/secondary 对齐违规数为 `0`
  - pending row primary-module 语义违规数为 `0`
  - non-discipline general-method row 对象字段语义违规数为 `0`

## 产出判断

本轮把 registry current snapshot 里最关键的“主排架位-二级位-通用方法例外”三类对齐关系进一步锁死，使 current snapshot 更接近方案中要求的可审计展示快照，而不是松散的字段拼接结果。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
