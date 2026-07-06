# structured_data_catalog_round130_audit_corpus_and_review_query_execution_surfaces_closeout_2026-07-06

## 本轮目标

继续按长期方案推进，把一批已经实现但还没有被 execution audit 真正执行过的 corpus/review 查询面补成硬证据。

本轮重点覆盖：

- `paper`
- `module`
- `multi-module`
- `module-pdf-coverage`
- `status-summary`
- `year-summary`
- `source-summary`
- `pdf-evidence-status`

本轮不修改方案文件，不改四类 owner fact source。

## 本轮修改

### 1. 补 `Data/README.md` 的查询命令说明

新增命令示例：

- `status-summary`
- `year-summary`
- `source-summary`
- `pdf-evidence-status --missing-only`

并补充 operational notes：

- `status-summary` / `year-summary` / `source-summary` 属于 corpus/workflow review surface，不是 canonical classification count
- `pdf-evidence-status` 对应 SQLite `pdf_evidence_status` 的逐篇证据查询面

### 2. 扩展 `scripts/audit_execution_definition.py`

新增 `Item 27`，把 representative corpus/review query execution surface 纳入 execution audit。

本项检查两层：

1. 文档/命令面
   - README 已文档化：
     - `paper ASD-0001`
     - `multi-module`
     - `module-pdf-coverage`
     - `status-summary`
     - `year-summary`
     - `source-summary`
     - `pdf-evidence-status`
   - `query_analysis_db.py` 仍暴露这些命令

2. 实际执行面
   - execution audit 内部实际运行以下 representative queries：
     - `paper ASD-0001`
     - `module 04`
     - `multi-module`
     - `module-pdf-coverage`
     - `status-summary`
     - `year-summary`
     - `source-summary`
     - `pdf-evidence-status --missing-only`
   - 要求命令成功返回
   - 要求输出非空
   - 要求输出中不存在 `Traceback`

## 验证

运行：

```powershell
python scripts/run_structured_data_pipeline.py --with-execution-audit
```

结果：

- `export -> check -> build -> execution-audit` 全流程通过
- `check_data_consistency.py` 通过
- `audit_execution_definition.py` 输出：
  - `pass=27`
  - `fail=0`

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

本轮把长期方案中的一批 corpus/review query surface 从“命令存在”推进到了“文档存在且 execution audit 实际执行通过”的状态。现在 execution audit 已不只是验证数据层和治理层，还开始直接验证分析查询层的代表性命令能否在当前仓库状态下运行并返回内容。
