# Structured Data Catalog Round 101 Closeout

日期：2026-07-06

## 本轮目标

继续沿着 discipline current snapshot 的纪律前移，把上一轮已经落到 SQLite 的 registry 唯一性约束同步前推到 `check_data_consistency.py`，避免问题只能在 build 建库阶段才暴露。

## 本轮修改

修改：
- `scripts/check_data_consistency.py`

### 1. 前移 `discipline_local_code_registry` 的 `assignment_id` 唯一性检查

在 `validate_discipline_local_code_registry()` 中新增：

- `assignment_id` 不能在 registry snapshot 中重复

如果 registry 里出现重复 `assignment_id`，现在会在 check 阶段直接失败，而不是等到 SQLite 侧唯一索引报错。

### 2. 前移 active registry 的 `discipline_local_code` 唯一性检查

在 `validate_discipline_local_code_registry()` 中新增：

- `assignment_status = active_code` 时，`discipline_local_code` 不能重复

这和上一轮新增的 SQLite partial unique index 保持一致，让同一条纪律在 derived JSONL 层和 SQLite 层同时成立。

### 3. 补齐 registry 对当前快照 assignment 覆盖的集合级校验

新增：

- `seen_assignment_ids == current_snapshot_assignment_ids`

此前已检查：

- row count 与 current snapshot 数量一致
- 每一行 assignment 必须属于 current snapshot

但本轮进一步把它提升为集合完全相等检查，避免“数量相同但集合不完全一致”的边界情况漏过。

## 验证

运行：

```bash
python scripts/run_structured_data_pipeline.py --with-execution-audit
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

本轮没有扩展需求范围，只把已经在 SQLite 层落实的 registry 唯一性纪律前移到 `check` 阶段，减少导出快照漂移时的发现滞后。当前 discipline current snapshot 这条链路已经形成：

- export 派生
- check 前移拦截
- SQLite 原生唯一索引再兜底

三层一致的收口。

## 后续状态

当前无新的代码级阻塞点；可以继续沿剩余未前移的 discipline / analysis 约束逐轮补齐。
