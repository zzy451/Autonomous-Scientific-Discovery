# structured_data_catalog_round133_audit_core_metadata_baseline_boundary_query_execution_surfaces_closeout_2026-07-06

## 本轮目标

继续按长期方案推进，把剩余核心 metadata / baseline / boundary 查询面也补成 execution audit 的真实执行证明。

本轮重点覆盖：

- `summary`
- `metadata`
- `discipline-registry-metadata`
- `snapshot-provenance`
- `analysis-baseline`
- `object-scope-registry`
- `module-distribution`
- `object-coverage-summary`
- `multi-module-combo-summary`
- `bucket-0104-summary`
- `missing-pdf`
- `source-limited`
- `coverage-summary`
- `boundary-cases --real-only`
- `bucket-summary`

本轮不修改方案文件，不改四类 owner fact source。

## 本轮修改

### 1. 扩展 `scripts/audit_execution_definition.py`

新增 `Item 30`，在 execution audit 中实际运行上述 15 条 representative metadata / baseline / boundary 查询。

判定标准与前几轮 query execution audit 一致：

- 命令成功返回
- 输出非空
- 输出中不存在 `Traceback`

### 2. 修复 `query_analysis_db.py` 的 CLI 兼容性缺口

本轮在 `boundary-cases` 命令上补了：

```text
--real-only
```

这个参数是显式 no-op alias，因为当前 `boundary-cases` 本来就默认只看 real drift。

之所以要补，是因为：

- README 里已经给出 `boundary-cases --real-only` 的命令示例
- execution audit 本轮也用这个命令作为 representative query
- 但此前脚本并未接受这个参数，导致 README / CLI / audit 三者之间存在真实漂移

现在这三层已重新对齐。

### 3. 刷新 derived outputs

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
  - `pass=30`
  - `fail=0`

## 结论

本轮把 structured-data query surface 的最后一批核心面也推进成了“execution audit 真正执行过”的状态。同时修掉了一个真实的 CLI/README 偏差点，让 `boundary-cases --real-only` 从文档示例变成了脚本支持的稳定调用。到这一轮为止，metadata、baseline、boundary、registry、taxonomy、lifecycle、owner-maintenance、owner-initialization、evidence inventory 等主要运行面都已经被 execution audit 直接触达。
