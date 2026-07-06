# structured_data_catalog_round125_audit_lifecycle_and_snapshot_provenance_surfaces_closeout_2026-07-06

## 本轮目标

继续按长期方案推进，把已经落地但尚未被 execution audit 直接证明的两块面补齐：

1. 生命周期字段链：
   - `record_status`
   - `inclusion_decision`
   - `duplicate_of`
   - `last_reviewed_at`
   - `last_reviewed_by`
2. SQLite snapshot provenance / metadata 查询面。

本轮仍不修改方案文件，不改四类 owner fact source。

## 本轮修改

### 1. 补 `Data/README.md` 的 lifecycle 查询说明

在查询命令说明中补入并解释：

- `lifecycle-summary`
- `lifecycle-records`

这样 README 终于把已经存在于 `query_analysis_db.py` 的生命周期查询面正式写出来，避免“脚本有、文档没有”的漂移。

### 2. 扩展 `scripts/audit_execution_definition.py`

新增两条 execution audit 检查项：

- `Item 21`
  - 检查所有 `papers.jsonl` 记录都带有 lifecycle 字段：
    - `record_status`
    - `inclusion_decision`
    - `duplicate_of`
    - `last_reviewed_at`
    - `last_reviewed_by`
  - 检查 `active_confirmed_core -> record_status=active_confirmed_core -> inclusion_decision=confirmed_core`
  - 检查 `duplicate_of` 如非空，必须是合法 `ASD-xxxx`
  - 检查 `papers.jsonl` 与 SQLite `papers` 行数一致
  - 检查 `query_analysis_db.py` 与 `README.md` 同时暴露：
    - `lifecycle-summary`
    - `lifecycle-records`

- `Item 22`
  - 检查 SQLite `metadata` 中存在当前 papers / registry provenance 所需 key：
    - `papers_exported_at`
    - `discipline_local_code_registry_generated_at`
    - `discipline_local_code_registry_generated_by`
    - `discipline_local_code_registry_source_commit`
    - `discipline_local_code_registry_worktree_dirty`
    - `discipline_local_code_registry_row_count`
  - 检查 `query_analysis_db.py` 与 `README.md` 同时暴露：
    - `metadata`
    - `discipline-registry-metadata`
    - `snapshot-provenance`

### 3. 刷新 derived outputs

重新执行 canonical pipeline 后，刷新了本轮相关 derived outputs 与 execution audit 报告，包括：

- `Coverage_Check/structured_data_execution_definition_audit_latest.md`
- `Data/README.md`
- `Data/papers.jsonl`
- `Data/papers.csv`
- `Data/papers.sqlite`
- `Data/discipline_local_code_registry.jsonl`
- `Data/discipline_local_code_registry.csv`
- `Data/registry/*.jsonl`
- `Data/registry/taxonomy_registry.json`

## 验证

运行：

```powershell
python scripts/run_structured_data_pipeline.py --with-execution-audit
```

结果：

- `export -> check -> build -> execution-audit` 全流程通过
- `check_data_consistency.py` 通过
- `audit_execution_definition.py` 输出：
  - `pass=22`
  - `fail=0`

## 本轮结论

本轮把长期方案中的 lifecycle lane 和 snapshot provenance lane 继续补成了“可查询、可文档化、可执行审计证明”的状态。现在 execution audit 不只证明 discipline code、taxonomy、owner guardrail 和 change log，也开始直接证明 lifecycle 字段链与 metadata/provenance 查询面。

## 额外说明

当前 worktree 仍存在一个与本轮无关的现有改动：

- `Coverage_Check/representative_reading_shortlist_by_module_2026-07-06.md`

本轮不会修改或提交它；本轮提交仅包含 lifecycle / metadata 审计增强与 pipeline 刷新的相关 derived outputs。
