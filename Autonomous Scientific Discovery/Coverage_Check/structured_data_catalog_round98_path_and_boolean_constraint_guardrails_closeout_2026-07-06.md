# Structured Data Catalog Round 98 Closeout

日期：2026-07-06

## 本轮目标

继续把已经落进 SQLite 的结构约束做实到 build 自检里，尤其补上 `papers` 主表布尔位，以及 `notes` / `paper_assets` 路径非空这类“应该成立”的 guardrail。

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. `papers` 主表布尔位约束纳入自检

前面已经把以下约束写进 `papers` 表定义：

- `pdf_exists IN (0, 1)`
- `note_exists IN (0, 1)`
- `active_confirmed_core IN (0, 1)`

本轮把这些片段正式纳入 `validate_papers_sqlite_constraints()`，避免只在建表 SQL 里出现却无人验证。

### 2. `paper_assets.path` 非空约束纳入自检

前面 `paper_assets` 已经使用：

- `path TEXT NOT NULL`

本轮把该片段纳入 `validate_evidence_sqlite_constraints()`。

### 3. `notes` / `note_inventory.note_path` 非空约束纳入自检

前面 `notes` 和 `note_inventory` 已经使用：

- `note_path TEXT NOT NULL`

本轮把该片段纳入 `validate_evidence_sqlite_constraints()`。

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

## 产出判断

本轮不是新增很多新 schema，而是把前面已经加入 SQLite 的一批 guardrail 真正接进 build 自检闭环里，减少“约束写了但没人检查”的风险。

## 后续状态

当前无代码级阻塞，worktree 在提交前可收口为干净状态。
