# Structured Data Catalog Round 106 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 `discipline_local_code_registry` 作为“当前快照表”应有的一组生命周期字段语义正式压进 SQLite schema 和 build 自检层，而不只依赖 export 逻辑或外部 checker。

对应方案要求：

- `discipline_local_code_registry` 只承载 current snapshot
- `pending_secondary` / `non_discipline_general_method` 是当前快照状态，而不是历史迁移状态
- lifecycle 字段必须与当前 status 语义一致
- derived snapshot 中的 `assigned_at` / `assigned_by` 也应保持基础可审计格式

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 收紧 registry 当前快照层的生命周期字段语义

为 SQLite `discipline_local_code_registry` 表新增 / 收紧以下 `CHECK`：

- `assignment_status = 'active_code'` 时：
  - `pending_reason IS NULL`
  - `retired_at IS NULL`
  - `redirected_to_code IS NULL`

- `assignment_status = 'pending_secondary'` 时：
  - `pending_reason IS NOT NULL`
  - `retired_at IS NULL`
  - `redirected_to_code IS NULL`

- `assignment_status = 'non_discipline_general_method'` 时：
  - `pending_reason IS NULL`
  - `retired_at IS NULL`
  - `redirected_to_code IS NULL`

这把 registry 进一步限定为“当前状态快照”，而不是混入历史 retired / redirected 生命周期信息的表。

### 2. 补 registry 审计字段的基础格式约束

为 `discipline_local_code_registry` 新增：

- `assigned_at` 必须匹配 `YYYY-MM-DD`
- `assigned_by` 必须满足 `trim(assigned_by) <> ''`

这样 registry 快照在保留账本审计元信息时，也具备基础格式约束。

### 3. build 自检补充 registry 生命周期语义查询

在 `validate_discipline_local_code_registry_outputs()` 中新增 SQLite 查询级自检：

- active row 是否错误携带 `pending_reason / retired_at / redirected_to_code`
- pending row 是否缺失 `pending_reason` 或错误携带 retired / redirected 字段
- non-discipline general-method row 是否错误携带 pending / retired / redirected 字段
- `assigned_at` / `assigned_by` 是否满足基础格式要求

任一违规即直接中止 build。

### 4. discipline SQLite schema 文本检查同步扩展

`validate_discipline_sqlite_constraints()` 现在也会验证上述 registry lifecycle / audit-field 约束片段已经真实写入 SQLite 建表 SQL 中，而不是只依赖查询级校验。

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
  - active row 生命周期字段违规数为 `0`
  - pending row 生命周期字段违规数为 `0`
  - non-discipline general-method row 生命周期字段违规数为 `0`
  - 非法 `assigned_at` 数为 `0`
  - 空白 `assigned_by` 数为 `0`

## 产出判断

本轮把 registry 当前快照层的生命周期边界进一步锁死，使它更明确地只表达“每篇 active paper 当前应展示的 code/状态快照”，而不是模糊地承载历史迁移字段。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
