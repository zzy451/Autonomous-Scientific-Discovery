# Structured Data Catalog Round 38 Closeout

日期：2026-07-06

## 本轮目标

把 `paper_modules` 关系层从当前的 mixed-scope 兼容语义，重新对齐回长期方案里的 canonical 语义：

- `paper_modules` 默认代表 canonical `scientific_object_modules` 多对多关系
- workflow mirror 单独放在 `workflow_mirror_paper_modules`
- canonical + workflow 的 combined surface 只保留在显式的 `mixed_scope_*` 兼容对象里

## 本轮实现

更新：

- `scripts/build_analysis_db.py`
- `scripts/query_analysis_db.py`
- `Data/README.md`

并重建：

- `Data/paper_modules.csv`
- `Data/canonical_paper_modules.csv`
- `Data/workflow_mirror_paper_modules.csv`
- `Data/mixed_scope_paper_modules.csv`
- `Data/papers.sqlite`
- 以及本轮 `export -> check -> build` 触达的常规 derived snapshot

### 1. 默认 `paper_modules` 改回 canonical 关系层

SQLite 里现在：

- `paper_modules` 是 canonical table
- 主键对齐为：
  - `(paper_id, module_code)`
- 它只承载 `scientific_object_modules` 这一条 canonical lane

这样它终于和方案里“`paper_modules` 必须是多对多关系表，不是 mixed-scope 兼容层”的语义一致。

### 2. workflow mirror 独立拆出

新增 / 明确：

- `workflow_mirror_paper_modules`

它只承载：

- `final_modules_or_bucket`

因此 canonical 事实层和 workflow mirror 审计层不再默认混在同一个 `paper_modules` 对象里。

### 3. mixed-scope surface 改成显式兼容对象

保留兼容审计面，但名字改为显式：

- SQLite:
  - `mixed_scope_paper_modules`
  - `mixed_scope_module_assignment_counts`
- CSV:
  - `Data/mixed_scope_paper_modules.csv`

这样如果以后有人真的需要 canonical-vs-workflow 对照面，仍然有入口；但默认对象名不再误导。

### 4. canonical aliases 保留兼容

为减少已有调用面震荡，保留：

- `canonical_paper_modules`
- `canonical_module_assignment_counts`

但它们现在只是兼容 alias：

- `canonical_paper_modules` -> alias over `paper_modules`
- `canonical_module_assignment_counts` -> alias over `module_assignment_counts`

### 5. README 与查询 guardrail 同步

更新：

- `Data/README.md`
- `scripts/query_analysis_db.py`

同步说明：

- `paper_modules.csv` 已改为 canonical-only
- `mixed_scope_paper_modules.csv` 才是 combined surface
- `paper_modules` / `module_assignment_counts` 现在是默认 canonical SQL 面
- 只有 `mixed_scope_*` 才需要 mixed-scope guardrail

## 本轮验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- `export` 成功
- `check` 成功
- `build` 成功

额外 spot check：

### SQLite 行数

- `paper_modules = 843`
- `workflow_mirror_paper_modules = 592`
- `mixed_scope_paper_modules = 1435`

### CSV 行数

- `paper_modules.csv = 843`
- `canonical_paper_modules.csv = 843`
- `workflow_mirror_paper_modules.csv = 592`
- `mixed_scope_paper_modules.csv = 1435`

### 语义检查

- `paper_modules.csv` 首行 `assignment_scope = scientific_object_modules`
- `workflow_mirror_paper_modules.csv` 首行 `assignment_scope = final_modules_or_bucket`
- build 输出计数现在分别打印 canonical / workflow / mixed-scope 三组行数，不再把 mixed-scope 总行数误报成 `paper_modules rows`

## 本轮结论

这一轮把 `paper_modules` 这块最关键的默认语义重新对齐回长期方案：canonical 关系层和 workflow mirror 审计层不再默认混装，mixed-scope surface 仍保留，但被清楚地放进显式兼容对象里。这样后续继续落实方案时，`paper_modules` 终于可以直接当作“正式 canonical 多对多关系层”来理解和使用，而不是再依赖 README 警告去防误用。
