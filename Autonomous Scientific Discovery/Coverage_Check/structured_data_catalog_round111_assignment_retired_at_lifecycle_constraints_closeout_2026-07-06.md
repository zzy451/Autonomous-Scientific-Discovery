# Structured Data Catalog Round 111 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 `discipline_code_assignments` 中历史状态字段 `retired_at` 的生命周期语义正式压进 SQLite owner-load 层和 build 自检，而不只依赖外层 checker。

对应方案要求：

- 旧 code 进入 `retired_code` / `redirected_code` 后应保留历史状态
- 当前状态行不应伪装成“已退休”的历史行
- 历史状态行应显式带有可审计的 retired 日期

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 收紧 ledger 的 `retired_at` 生命周期约束

为 SQLite `discipline_code_assignments` 新增：

- `assignment_status IN ('retired_code', 'redirected_code') OR retired_at IS NULL`
- `assignment_status NOT IN ('retired_code', 'redirected_code') OR retired_at IS NOT NULL`

也就是：

- `active_code` / `pending_secondary` / `non_discipline_general_method` 行必须 `retired_at IS NULL`
- `retired_code` / `redirected_code` 行必须显式带 `retired_at`

### 2. build 自检补充 retired-at 生命周期查询

在 `validate_owner_loaded_and_inventory_tables()` 中新增 SQLite 查询级自检：

- 历史状态行若缺失 `retired_at`，直接报错
- 当前状态行若错误携带 `retired_at`，直接报错

这让 `retired_at` 不再只是“可选日期字段”，而是开始承担明确的生命周期语义。

### 3. discipline SQLite schema 文本检查同步扩展

`validate_discipline_sqlite_constraints()` 现在也会检查这两条 `retired_at` 生命周期约束片段已经真实写入 `discipline_code_assignments` 建表 SQL 中，而不是只依赖运行时查询。

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
  - 历史状态行缺失 `retired_at` 的违规数为 `0`
  - 当前状态行错误携带 `retired_at` 的违规数为 `0`

## 产出判断

本轮把 `retired_at` 从“字段存在”推进成“真正表达历史状态”的账本字段，为后续第一次出现真实 retired / redirected 记录前先把边界锁死。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
