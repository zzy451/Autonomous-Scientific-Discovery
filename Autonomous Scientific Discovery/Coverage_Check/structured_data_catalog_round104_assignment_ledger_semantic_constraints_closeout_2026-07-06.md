# Structured Data Catalog Round 104 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 `discipline_code_assignments` 账本中已经由检查器维护的几条核心生命周期语义，正式压进 SQLite owner-load 层与 build 自检层。

对应方案要求：

- `active_code` / `retired_code` / `redirected_code` 不应携带 `pending_reason`
- `redirected_code` 必须有合法的 `redirected_to_code`
- `discipline_local_code = MM-SS-NNN`
- `primary_taxonomy_code_2lvl = MM.SS`
- 对于已分配普通 code 的行，这两套前缀必须稳定对应

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 收紧 `discipline_code_assignments` 的 pending / redirect 语义

为 SQLite `discipline_code_assignments` 表新增更强的 `CHECK`：

- `assignment_status IN ('active_code', 'retired_code', 'redirected_code')`
  时，`pending_reason` 必须为 `NULL`

- `assignment_status = 'redirected_code'`
  时，`redirected_to_code` 必须匹配合法 code 形式：
  - `MM-SS-NNN`

这样账本生命周期字段不再只由 `check_data_consistency.py` 间接保证。

### 2. 收紧 code 与 2-level taxonomy 的前缀对齐

对已分配普通 code 的账本行新增 `CHECK`：

- `substr(discipline_local_code, 1, 2) = substr(primary_taxonomy_code_2lvl, 1, 2)`
- `substr(discipline_local_code, 4, 2) = substr(primary_taxonomy_code_2lvl, 4, 2)`

也就是：

- `04-03-017` 必须对应 `04.03`

这把方案中的 `MM-SS-NNN` / `MM.SS` 对齐关系正式压进账本导入表。

### 3. build 自检补充 ledger 语义查询

在 `validate_owner_loaded_and_inventory_tables()` 中新增 SQLite 查询级自检：

- 已分配普通 code 的账本行若仍携带 `pending_reason`，直接报错
- `redirected_code` 若缺失合法 `redirected_to_code`，直接报错
- `discipline_local_code` 与 `primary_taxonomy_code_2lvl` 前缀不一致，直接报错

### 4. discipline SQLite schema 文本检查同步扩展

`validate_discipline_sqlite_constraints()` 现在也会检查上述新约束片段确实写进了 `discipline_code_assignments` 建表 SQL 中，而不是只依赖运行时查询。

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
  - 已分配普通 code 却携带 `pending_reason` 的违规数为 `0`
  - 非法 `redirected_to_code` 的违规数为 `0`
  - `discipline_local_code` / `primary_taxonomy_code_2lvl` 前缀错配数为 `0`

## 产出判断

本轮把 discipline-code 账本的一组关键“生命周期字段语义”和“code-prefix / taxonomy-prefix 对齐语义”推进到了 SQLite owner-load 层，使账本不再只是被动存放字段，而是开始真正承担稳定管理码账本的结构化约束角色。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
