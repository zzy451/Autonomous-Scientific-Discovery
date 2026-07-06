# structured_data_catalog_round126_audit_evidence_asset_and_note_inventory_surfaces_closeout_2026-07-06

## 本轮目标

继续按长期方案推进，把 PDF/source、asset、note 这一层已经存在的清单与 SQLite 查询面，补成 execution audit 的正式证明项。

本轮不修改方案文件，不改四类 owner fact source。

## 本轮修改

### 1. 扩展 `scripts/audit_execution_definition.py`

新增 `Item 23`，把 evidence / asset / note inventory surface 纳入 execution audit。

本项检查：

- `Data/pdf_manifest.json`
- `Data/missing_pdf_manifest.json`
- `Data/note_manifest.json`
- `Data/registry/asset_manifest.jsonl`

与 SQLite 下列表的一致性：

- `paper_assets`
- `notes`
- `pdf_inventory`
- `missing_pdf_inventory`
- `note_inventory`

同时检查 `query_analysis_db.py` 与 `Data/README.md` 都暴露并文档化了以下查询面：

- `missing-pdf`
- `source-limited`
- `coverage-summary`
- `paper-assets`
- `notes`

### 2. 刷新 derived outputs

运行 canonical pipeline 后，刷新了：

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
  - `pass=23`
  - `fail=0`

本轮新增直接证明的计数面为：

- `assets=1742`
- `notes=871`
- `pdf_inventory=426`
- `missing_pdf_inventory=25`

## 结论

本轮把长期方案中的“资料证据层 / asset 层 / note 层”继续补成了程序化可证明状态。现在 execution audit 不只证明分类、discipline code、lifecycle、provenance，也开始直接证明 PDF/source 清单、asset manifest、note inventory 与 SQLite 查询面的一致性。
