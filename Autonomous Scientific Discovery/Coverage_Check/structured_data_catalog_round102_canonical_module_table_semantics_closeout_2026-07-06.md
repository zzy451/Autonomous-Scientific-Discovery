# Structured Data Catalog Round 102 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 canonical formal-module 关系表 `paper_modules` 的语义边界正式锁死，避免它在 schema 层误容纳 `01.04` general-method bucket 或其他非 formal-module 关系。

对应方案要求：

- `scientific_object_modules` 只承载 formal `01-11` 模块
- `01.04` 只能留在 `general_method_bucket`
- SQLite 中 `paper_modules` 必须是 canonical formal-module 多对多关系表
- general-method 关系应单独走 `paper_general_method_buckets`

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 收紧 `paper_modules` 表的 `module_kind` 约束

原先 `paper_modules` 的表结构允许：

- `module_kind IN ('formal_module', 'general_bucket')`

本轮改为：

- `module_kind = 'formal_module'`

这让 canonical `paper_modules` 在 schema 层就不再可能吸入 `general_bucket` 行。

### 2. 增加 canonical primary/source 联动约束

为 `paper_modules` 新增 cross-field `CHECK`：

- `is_primary_for_filing = 1` 时，`source` 必须是 `primary_module_for_filing`
- `is_primary_for_filing = 0` 时，`source` 必须是 `scientific_object_modules`

这样 canonical module 表中的“主排架位来源”与“普通 formal-module 事实来源”被明确区分，不再只依赖建表时的约定。

### 3. build 自检补充 canonical module 语义检查

在 `validate_sqlite_module_surfaces()` 中新增 SQLite 自检：

- `paper_modules` 中 `module_kind <> 'formal_module'` 的记录数必须为 `0`
- `paper_modules` 中 `is_primary_for_filing` 与 `source` 的联动语义不得漂移

### 4. module-constraint SQL 文本检查改为白空白归一化

`validate_module_sqlite_constraints()` 现在会先归一化 `sqlite_master` 中的 SQL 文本空白，再匹配关键约束片段，避免因为换行或多空格导致误报。

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

- 当前 `paper_modules` 中 `module_kind <> 'formal_module'` 的记录数为 `0`
- 当前 `paper_modules` 中 `is_primary_for_filing / source` 语义错配记录数为 `0`

## 产出判断

本轮把 canonical formal-module 关系表与 general-method bucket 关系表的边界进一步压实，使 `paper_modules` 更接近方案中“formal scientific-object assignment table”的精确定义，而不是语义上过宽的通用模块表。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
