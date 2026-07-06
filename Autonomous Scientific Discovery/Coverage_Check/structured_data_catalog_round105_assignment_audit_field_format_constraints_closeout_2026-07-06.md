# Structured Data Catalog Round 105 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 `discipline_code_assignments` 账本里一组基础审计字段的格式语义正式压进 SQLite owner-load 层，而不只依赖 JSON schema 或 `check_data_consistency.py`。

对应方案要求：

- `assignment_id` 使用 `DCA-000001` 递增格式
- `assigned_at` / `retired_at` 作为可审计日期字段，格式应稳定
- `assigned_by` 不能是空值或空白占位
- 账本导入表应对这些基础审计字段本身承担结构化约束责任

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 收紧 `discipline_code_assignments` 的审计字段格式

为 SQLite `discipline_code_assignments` 表新增 / 收紧以下 `CHECK`：

- `assignment_id` 必须匹配：
  - `DCA-[0-9]{6}`

- `assigned_at` 必须匹配：
  - `YYYY-MM-DD`

- `retired_at` 若非空，必须匹配：
  - `YYYY-MM-DD`

- `assigned_by` 必须满足：
  - `trim(assigned_by) <> ''`

这让账本在进入 SQLite owner-load 表时，就会先被基础审计字段格式过滤一次。

### 2. build 自检补充 assignment 审计字段查询

在 `validate_owner_loaded_and_inventory_tables()` 中新增 SQLite 查询级自检：

- 非法 `assignment_id`
- 非法 `assigned_at`
- 非法 `retired_at`
- 空白 `assigned_by`

任一出现即直接报错，防止 owner ledger 在 build 阶段静默带入脏审计字段。

### 3. discipline SQLite schema 文本检查同步扩展

`validate_discipline_sqlite_constraints()` 现在也会检查这些新格式约束片段已经真实写入 `discipline_code_assignments` 建表 SQL 中，而不是只依赖运行时数据查询。

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
  - 非法 `assignment_id` 数为 `0`
  - 非法 `assigned_at` 数为 `0`
  - 非法 `retired_at` 数为 `0`
  - 空白 `assigned_by` 数为 `0`

## 产出判断

本轮把 discipline ledger 的一组基础审计字段从“外层约束”推进成“owner-load 表内生约束”，让 SQLite 中的 `discipline_code_assignments` 更接近长期稳定账本，而不只是对 JSONL 的被动镜像。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
