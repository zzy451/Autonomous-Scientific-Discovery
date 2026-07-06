# structured_data_catalog_round128_audit_0104_boundary_and_canonical_mirror_surfaces_closeout_2026-07-06

## 本轮目标

继续按长期方案推进，把 `01.04` 与 formal scientific-object module 的硬边界，以及 canonical-vs-mirror boundary audit 查询面，补成 execution audit 的直接证明项。

本轮不修改方案文件，不改四类 owner fact source。

## 本轮修改

### 1. 补 `Data/README.md` 的 boundary audit 命令示例

新增两个显式查询示例：

- `boundary-cases --real-only`
- `bucket-summary`

这样 README 不再只在说明段提到这两个 audit surface，而是把可执行命令一并写出来。

### 2. 扩展 `scripts/audit_execution_definition.py`

新增 `Item 25`，把 `01.04` 分离边界和 canonical-vs-mirror audit surface 纳入 execution audit。

本项检查：

- `papers.jsonl` 的 `scientific_object_modules` 中不允许出现 formal `01.04`
- SQLite `paper_modules` 中 `module_code='01.04'` 的行数必须为 `0`
- SQLite `paper_general_method_buckets` 行数必须与 `papers.jsonl` 中 `general_method_bucket != none` 的记录数一致
- active confirmed-core 的 pure general-method 记录数必须与 SQLite `canonical_bucket_0104_summary.active_confirmed_core_count` 一致
- SQLite `workflow_mirror_paper_modules` 中的 `01.04` 行数与上述 active canonical `01.04` 计数一致
- SQLite `classification_boundary_summary` 已装载，且可产出 canonical-vs-mirror boundary 审计统计
- `query_analysis_db.py` 与 `Data/README.md` 同时暴露：
  - `boundary-cases`
  - `bucket-summary`

## 验证

运行：

```powershell
python scripts/run_structured_data_pipeline.py --with-execution-audit
```

结果：

- `export -> check -> build -> execution-audit` 全流程通过
- `check_data_consistency.py` 通过
- `audit_execution_definition.py` 输出：
  - `pass=25`
  - `fail=0`

本轮新纳入直接证明的关键边界计数为：

- `formal_0104_rows=0`
- `workflow_0104_rows=9`
- `paper_general_method_buckets=169`
- `boundary_rows=4`
- `real_drift_rows=3`

## 刷新文件

本轮随 pipeline 刷新的相关 derived outputs 包括：

- `Coverage_Check/structured_data_execution_definition_audit_latest.md`
- `Data/README.md`
- `Data/papers.jsonl`
- `Data/papers.csv`
- `Data/papers.sqlite`
- `Data/discipline_local_code_registry.jsonl`
- `Data/discipline_local_code_registry.csv`
- `Data/registry/*.jsonl`
- `Data/registry/taxonomy_registry.json`

本轮没有改动以下 owner fact source：

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- `Data/discipline_code_assignments.jsonl`
- `Data/classification_code_index.json`

## 结论

本轮把长期方案里最关键的一条分类硬边界继续补成了程序化可证明状态：`01.04` 现在不只是“规则上应当独立”，而是 execution audit 直接证明它没有混入 formal module、确实独立落在 general-method bucket，并且 canonical-vs-mirror 的边界审计查询面已经可执行、可文档化、可复核。
