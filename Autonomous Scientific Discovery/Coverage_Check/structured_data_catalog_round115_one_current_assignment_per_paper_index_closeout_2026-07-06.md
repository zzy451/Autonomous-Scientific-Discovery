# Structured Data Catalog Round 115 Closeout

日期：2026-07-06

## 本轮目标

继续按冻结方案推进，把 `discipline_code_assignments` 的“每篇论文最多一条 current snapshot 行”从 checker/build 级规则推进成 SQLite 索引级约束。

对应方案要求：

- 一篇论文可以有多条 assignment 历史记录
- 但同一篇论文最多只能有一条 current snapshot 行：
  - `active_code`
  - `pending_secondary`
  - `non_discipline_general_method`

## 本轮修改

修改：

- `scripts/build_analysis_db.py`

### 1. 新增 ledger current-snapshot 唯一性部分索引

为 SQLite `discipline_code_assignments` 新增：

```sql
CREATE UNIQUE INDEX discipline_code_assignments_one_current_snapshot_per_paper
ON discipline_code_assignments(paper_id)
WHERE assignment_status IN ('active_code', 'pending_secondary', 'non_discipline_general_method');
```

这让“每篇论文最多一条 current row”从外层逻辑要求，正式变成 SQLite 自身可强制执行的约束。

### 2. discipline SQLite schema 校验同步扩展

`validate_discipline_sqlite_constraints()` 现在会检查：

- `discipline_code_assignments_one_current_snapshot_per_paper`
- 且它确实是针对 current snapshot 三种状态的部分唯一索引

### 3. build 自检补充 duplicate-current-row 查询

在 `validate_discipline_local_code_registry_outputs()` 的 SQLite current-snapshot 覆盖检查中，新增显式查询：

- 同一 `paper_id` 是否出现多条 current assignment

如果有，build 直接失败。

这样 current snapshot 唯一性现在同时由：

- SQLite 唯一索引
- build 查询级自检

双重保证。

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

- 当前 SQLite 中：
  - current assignment duplicate-per-paper 数为 `0`
  - active papers / current assignments / registry rows 仍全部为 `447`

## 产出判断

本轮把 ledger current snapshot 的单行唯一性推进成了数据库层正式约束，为后续第一次出现更复杂的历史迁移记录前先把最关键的唯一性边界锁死。

## 后续状态

当前无新增代码级阻塞，worktree 可在提交后恢复干净状态。
