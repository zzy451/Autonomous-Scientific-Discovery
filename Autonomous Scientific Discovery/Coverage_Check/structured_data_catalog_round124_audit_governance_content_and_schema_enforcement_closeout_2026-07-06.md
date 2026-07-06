# structured_data_catalog_round124_audit_governance_content_and_schema_enforcement_closeout_2026-07-06

## 本轮目标

继续按长期方案补 execution audit 的证明力度，把此前“治理文件存在即可通过”的弱证据，推进成“治理文件内容和 enforcement hook 都达标”的强证据。

本轮仍然不修改方案文件，不扩第二阶段需求，也不改四类 owner fact source。

## 本轮修改

### 1. 扩展 `scripts/audit_execution_definition.py`

新增两条 execution audit 检查项：

- `Item 19`
  - 检查 `Data/field_ownership_matrix.md` 是否包含冻结方案要求的 canonical lane 语义
  - 重点核对：
    - `source_file: Paper_Lists/agent_master_paper_list.md`
    - `fallback_order:`
    - `required_trace_fields:`
    - `source_confidence`
    - `parser_rule`
    - `discipline_code_assignments.jsonl`
    - `classification_code_index.json`
    - “冲突先修 owner file，再 rerun `export -> check -> build`”规则

- `Item 20`
  - 检查 `Data/check_policy.md` 是否明确写出：
    - `ERROR`
    - `WARNING`
    - `INFO`
    - build / commit 阻断语义
  - 同时检查 `scripts/check_data_consistency.py` 是否实际挂接了：
    - `validate_classification_code_index_owner(...)`
    - `validate_discipline_code_assignments_owner(...)`
    - `validate_payload_against_schema_file(...)`
    - `validate_jsonl_rows_against_schema_file(...)`
    - `severity_order = ("ERROR", "WARNING", "INFO")`

### 2. 刷新 derived outputs

重新执行 canonical pipeline 后，刷新了当前 derived outputs 与最新 execution audit 报告，包括：

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
  - `pass=20`
  - `fail=0`

## 额外说明

当前 worktree 里还有一个与本轮无关的现有改动：

- `Coverage_Check/representative_reading_shortlist_by_module_2026-07-06.md`

本轮不会改它，也不会把它混入本轮提交；本轮提交仅包含 execution audit 增强和由 pipeline 刷新的相关 derived outputs。

## 结论

本轮把长期方案中的治理层证据继续做实：现在 execution audit 不仅验证治理文档“在”，还开始验证它们“写对了”，并且 `check_data_consistency.py` 已经把 schema-backed owner validation 与 severity policy 真正接起来。
