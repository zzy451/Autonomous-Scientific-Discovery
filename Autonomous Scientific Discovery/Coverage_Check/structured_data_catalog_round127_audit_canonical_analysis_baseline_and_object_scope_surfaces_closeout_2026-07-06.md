# structured_data_catalog_round127_audit_canonical_analysis_baseline_and_object_scope_surfaces_closeout_2026-07-06

## 本轮目标

继续按长期方案推进，把 canonical analysis/query layer 中已经存在、但尚未被 execution audit 直接证明的基线查询面补齐，重点是：

- `analysis-baseline`
- `summary`
- `object-scope-registry`
- `module-distribution`
- `object-coverage-summary`
- `bucket-0104-summary`
- `general-method-buckets`

本轮不修改方案文件，不改四类 owner fact source。

## 本轮修改

### 1. 扩展 `scripts/audit_execution_definition.py`

新增 `Item 24`，把 canonical analysis baseline / object scope / `01.04` 分离查询面纳入 execution audit。

本项检查：

- `Data/taxonomy_index.json` 与 SQLite `taxonomy_index` 行数一致
- SQLite `analysis_object_scope_registry` 非空且已装载
- SQLite 视图与当前 `papers.jsonl` 派生计数一致：
  - `active_confirmed_core_papers`
  - `active_missing_local_pdf`
  - `canonical_bucket_0104_summary`
- `query_analysis_db.py` 与 `Data/README.md` 同时暴露：
  - `analysis-baseline`
  - `summary`
  - `object-scope-registry`
  - `module-distribution`
  - `object-coverage-summary`
  - `bucket-0104-summary`
  - `general-method-buckets`

### 2. 刷新 derived outputs

重新执行 canonical pipeline 后，刷新了：

- `Coverage_Check/structured_data_execution_definition_audit_latest.md`
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

## 验证

运行：

```powershell
python scripts/run_structured_data_pipeline.py --with-execution-audit
```

结果：

- `export -> check -> build -> execution-audit` 全流程通过
- `check_data_consistency.py` 通过
- `audit_execution_definition.py` 输出：
  - `pass=24`
  - `fail=0`

本轮新纳入直接证明的 canonical analysis 计数为：

- `taxonomy_index=12`
- `analysis_object_scope_registry=35`
- `active_core_view=447`
- `active_missing_pdf_view=25`
- `canonical_01_04_active=9`

## 结论

本轮把长期方案中的 canonical analysis baseline、object scope registry 与 `01.04` 分离查询面进一步补成了程序化可证明状态。现在 execution audit 不只证明 owner、ledger、registry、lifecycle、evidence inventory，也开始直接证明分析层的基线视图和 canonical-vs-bucket 分离逻辑。

## 额外说明

当前 worktree 中还存在一个与本轮无关的现有修改：

- `Coverage_Check/representative_reading_shortlist_by_module_2026-07-06.md`

本轮不会修改或提交它；本轮提交仅包含 canonical analysis/object-scope 审计增强与 pipeline 刷新的相关 derived outputs。
