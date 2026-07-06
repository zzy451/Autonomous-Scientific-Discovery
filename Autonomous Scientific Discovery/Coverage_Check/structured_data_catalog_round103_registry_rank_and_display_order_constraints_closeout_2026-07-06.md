# Structured Data Catalog Round 103 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 `discipline_local_code_registry` 中本应纯派生的字段语义正式锁到 SQLite 层，而不只依赖 export 代码习惯。

对应方案要求：

- `discipline_local_rank = parse_NNN(discipline_local_code)`，只能派生，不允许人工维护
- `discipline_display_order` 只作为展示排序，不替代稳定 code
- `pending_secondary` 不生成普通 code，但要保留明确的 pending 展示顺序
- `non_discipline_general_method` 不进入普通学科 code，但要保留单独展示顺序

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 收紧 `discipline_local_code_registry` 的 active-code 派生语义

为 SQLite `discipline_local_code_registry` 表补充更强的 `CHECK`：

- `assignment_status = 'active_code'` 时：
  - `discipline_local_rank` 必须非空
  - `discipline_local_rank` 必须等于 `substr(discipline_local_code, -3)`
  - `discipline_display_order` 必须等于 `discipline_local_code`

这把“rank 只能由 code 后缀派生”的规则正式压进了 registry 表结构。

### 2. 收紧 pending / general-method 的 display-order 语义

新增 SQLite `CHECK`：

- `assignment_status = 'pending_secondary'` 时：
  - `discipline_display_order` 必须匹配 pending 风格：包含 `PENDING-ASD-`

- `assignment_status = 'non_discipline_general_method'` 时：
  - `discipline_display_order` 必须匹配 general-method 风格：`GM-PENDING-ASD-...`

这样 pending/general-method 行的展示顺序格式也不再只是 export 约定。

### 3. build 自检补充 registry 语义查询

在 `validate_discipline_local_code_registry_outputs()` 中新增 SQLite 查询级自检：

- active row 的 rank / display-order 是否与 code 派生关系一致
- pending row 是否仍错误携带 code/rank 或缺失 pending-style display order
- non-discipline general-method row 是否仍错误携带 code/rank 或缺失 `GM-PENDING-...` display order

若存在违规行，build 直接失败。

### 4. discipline SQLite schema 文本检查改为更稳的归一化匹配

`validate_discipline_sqlite_constraints()` 现在会先对 `discipline_code_assignments` 和 `discipline_local_code_registry` 的建表 SQL 做空白归一化，再检查关键约束片段，避免因换行或空格差异导致误报。

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
  - active row 的 rank 派生违规数为 `0`
  - active row 的 display-order 违规数为 `0`
  - pending row 的 display-order / code-rank 违规数为 `0`
  - non-discipline general-method row 的 display-order / code-rank 违规数为 `0`

## 产出判断

本轮把 registry 中最关键的“稳定 code 字段”和“纯展示字段”边界进一步压实，使 `discipline_local_rank` 真正只能作为 code 派生字段存在，`discipline_display_order` 也被限定在当前 status 语义允许的范围内。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
