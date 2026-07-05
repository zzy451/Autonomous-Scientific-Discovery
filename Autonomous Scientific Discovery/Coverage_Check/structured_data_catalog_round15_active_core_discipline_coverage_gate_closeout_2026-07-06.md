# Structured Data Catalog Round 15 Closeout

日期：2026-07-06

## 本轮目标

补上 discipline ledger / registry 对 `active_confirmed_core` 覆盖完整性的硬约束，避免后续出现“active core 已新增或已确认，但 discipline code current snapshot 漏写”的静默漂移。

## 本轮实现

更新：

- `scripts/check_data_consistency.py`

新增阻断性检查：

### 1. discipline ledger current snapshot 覆盖必须完整

对 `Data/discipline_code_assignments.jsonl` 新增约束：

- `current snapshot` 状态集合仍定义为：
  - `active_code`
  - `pending_secondary`
  - `non_discipline_general_method`
- 每个 `paper_id` 最多只能有一条 current snapshot row
- current snapshot rows 的 `paper_id` 集合必须与 `papers.jsonl` 中 `active_confirmed_core=true` 的 `paper_id` 集合完全一致

这意味着：

- 如果新增了 active confirmed-core 论文却没有补 ledger row，check 会失败
- 如果 ledger 中出现了不属于当前 active confirmed-core 基线的 current snapshot row，check 也会失败

### 2. discipline registry 覆盖必须完整

对 `Data/discipline_local_code_registry.jsonl` 新增约束：

- registry `paper_id` 集合必须与 `active_confirmed_core` 集合完全一致

这使 derived snapshot 与 owner ledger / active baseline 之间的覆盖关系被明确锁死，而不只是检查 row 数量相等。

## 本轮验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- export 成功
- check 成功
- build 成功

当前状态：

- `papers.jsonl` records: 871
- `active confirmed-core`: 447
- `discipline_code_assignments` current snapshot rows: 447
- `discipline_local_code_registry` rows: 447

结合本轮新约束，这说明当前 discipline ledger / registry 对 active confirmed-core 基线的覆盖是完整且一一对应的。

## 本轮结论

本轮把“discipline code current snapshot 必须覆盖所有 active confirmed-core 论文”从隐含要求推进成了显式 gate。这样后续如果 master/progress active baseline 增长而 owner ledger 没有同步，系统会在 check 阶段第一时间暴露出来，而不会等到下游 registry / SQLite / 写作统计时才发现遗漏。
