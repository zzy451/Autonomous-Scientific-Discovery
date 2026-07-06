# structured_data_catalog_round132_audit_registry_taxonomy_and_lifecycle_query_execution_surfaces_closeout_2026-07-06

## 本轮目标

继续按长期方案推进，把 registry / taxonomy / audit / lifecycle 这批已文档化但尚未被 execution audit 真正执行过的查询面补成硬证据。

本轮重点覆盖：

- `discipline-code-summary`
- `discipline-code <code>`
- `secondary-class-summary`
- `secondary-class-pdf-coverage`
- `classification-terms --level secondary`
- `general-method-buckets`
- `change-log-summary`
- `change-log`
- `lifecycle-summary`
- `lifecycle-records`

本轮不修改方案文件，不改四类 owner fact source。

## 本轮修改

### 1. 扩展 `scripts/audit_execution_definition.py`

新增 `Item 29`，在 execution audit 中实际运行一组 representative registry/taxonomy/audit 查询：

```powershell
python scripts/query_analysis_db.py discipline-code-summary
python scripts/query_analysis_db.py discipline-code 04-04-001
python scripts/query_analysis_db.py secondary-class-summary
python scripts/query_analysis_db.py secondary-class-pdf-coverage
python scripts/query_analysis_db.py classification-terms --level secondary
python scripts/query_analysis_db.py general-method-buckets
python scripts/query_analysis_db.py change-log-summary
python scripts/query_analysis_db.py change-log --limit 5
python scripts/query_analysis_db.py lifecycle-summary
python scripts/query_analysis_db.py lifecycle-records --record-status duplicate --limit 5
```

其中 `discipline-code` 的代表性 code 不再硬编码依赖外部说明，而是从当前 `discipline_local_code_registry.jsonl` 中动态选择第一条 active `discipline_local_code`，以降低脆弱性。

### 2. 审计判定标准

`Item 29` 要求：

- README 已文档化上述查询面
- `query_analysis_db.py` 仍暴露对应命令
- 所有 representative query 都成功返回
- 所有 query 输出非空
- 所有 query 输出中都不得出现 `Traceback`

这样 execution audit 现在不只知道这些 registry/taxonomy/audit query “有命令、有 README”，而是知道它们在当前仓库状态下能真实执行并给出结果。

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
  - `pass=29`
  - `fail=0`

## 结论

本轮把长期方案中的 registry/taxonomy/audit query surface 又推进了一层：现在 execution audit 不只验证 representative corpus/review queries，也开始直接验证 discipline-code、secondary filing、taxonomy term、change-log、lifecycle 这些结构化查询面能在当前仓库状态下成功执行并返回内容。
