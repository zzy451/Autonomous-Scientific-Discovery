# Structured Data Catalog Round 86 Closeout

日期：2026-07-06

## 本轮目标

继续按长期方案推进真实落地，不只补 execution audit，而是把 discipline 相关的一部分逻辑约束真正推进到 SQLite 表层。

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. `discipline_code_assignments` SQLite 约束

新增表级约束：

- `assignment_status` 枚举限制：
  - `active_code`
  - `retired_code`
  - `redirected_code`
  - `pending_secondary`
  - `non_discipline_general_method`

- `schema_version = 1`

- 状态语义约束：
  - `active/retired/redirected` 必须有 `discipline_local_code` 与 `primary_taxonomy_code_2lvl`
  - `pending_secondary/non_discipline_general_method` 必须没有 `discipline_local_code` 与 `primary_taxonomy_code_2lvl`
  - `pending_secondary` 必须有 `pending_reason`
  - `non_discipline_general_method` 不得有 `pending_reason`
  - 非 `redirected_code` 不得携带 `redirected_to_code`

新增 partial unique indexes：

- `discipline_code_assignments_active_code_unique`
  - 保证 active `discipline_local_code` 唯一

- `discipline_code_assignments_one_active_per_paper`
  - 保证同一 `paper_id` 最多一条 `active_code`

### 2. `discipline_local_code_registry` SQLite 约束

新增表级约束：

- `assignment_status` 枚举限制：
  - `active_code`
  - `pending_secondary`
  - `non_discipline_general_method`

- `is_derived_snapshot = 1`

- 状态语义约束：
  - `active_code` 必须有 `discipline_local_code`、`discipline_local_rank`、`primary_taxonomy_code_2lvl`
  - `pending_secondary/non_discipline_general_method` 必须没有这些字段

### 3. build 自检

新增 `validate_discipline_sqlite_constraints()`：

- 检查 `discipline_code_assignments` 的关键 `CHECK` 约束 SQL 已写入
- 检查 `discipline_local_code_registry` 的关键 `CHECK` 约束 SQL 已写入
- 检查两个 partial unique indexes 已建成

### 4. blank-to-null 规范化

由于 registry JSONL 中 `discipline_local_rank` 的 pending/general-method 行当前使用空字符串表示“无值”，SQLite 插入阶段现在会先把空字符串规范化为 `NULL`，使实际入库值与新的状态约束一致。

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

- `discipline_code_assignments_active_code_unique`
- `discipline_code_assignments_one_active_per_paper`
- `discipline_code_assignments` table-level `CHECK`
- `discipline_local_code_registry` table-level `CHECK`

均已出现在 `sqlite_master` 中。

## 产出判断

本轮不是只补审计，而是把 discipline ledger / registry 的一部分关键约束真实推进到了 SQLite 层，并让 build 自身检查这些 schema guardrails 已存在。这更贴近长期方案里“SQLite 能承载的逻辑约束尽量落进去”的要求。

## 后续状态

当前无代码级阻塞，worktree 在提交前可收口为干净状态。
