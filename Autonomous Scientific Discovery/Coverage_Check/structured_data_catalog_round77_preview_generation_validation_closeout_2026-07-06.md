# Structured Data Catalog Round 77 Closeout

日期：2026-07-06

## 本轮目标

按既定顺序复核治理文件与现有脚本，重点验证 `scripts/export_structured_data.py` 是否已经按冻结方案生成 `Data/discipline_code_initial_assignment_preview.csv`，且不覆盖 owner fact source。

## 本轮执行

已重新阅读并对齐以下治理文件：

- `Coverage_Check/structured_data_long_term_catalog_and_index_plan_2026-07-05.md`
- `Data/field_ownership_matrix.md`
- `Data/discipline_code_assignment_policy.md`
- `Data/primary_filing_policy.md`
- `Data/check_policy.md`
- `Data/README.md`

已检查以下脚本的当前实现：

- `scripts/export_structured_data.py`
- `scripts/check_data_consistency.py`
- `scripts/build_analysis_db.py`

结论：

- `export_structured_data.py` 已显式读取：
  - `Paper_Lists/agent_master_paper_list.md`
  - `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
  - `Data/classification_code_index.json`
- preview 生成逻辑已覆盖第一阶段关键规则：
  - pure general-method-only 记录使用 `non_discipline_general_method`
  - `pending_secondary` 不生成假 `MM-SS-NNN` code
  - `discipline_local_rank` 仅由 proposed code 的尾段派生
  - owner guardrail 继续阻止 export 覆盖 `classification_code_index.json`、`discipline_code_assignments.jsonl` 等事实源
- 本轮未发现需要额外修改脚本的结构性冲突，因此未对 Python 源码做改动

## 验证

运行：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- `export_structured_data.py` 成功导出 `447` 行 `discipline_code_initial_assignment_preview.csv`
- `check_data_consistency.py` 全部通过
- `build_analysis_db.py` 全部通过

本轮 preview 统计：

- `active_code`: 423
- `pending_secondary`: 15
- `non_discipline_general_method`: 9

当前 `pending_secondary` 全部来自：

- `secondary_primary_mismatch`: 15

## 产出判断

第一优先任务“preview 生成逻辑跑通并通过现有校验链”已完成。

本轮没有新增第二阶段 owner 写入逻辑，也没有让日常 export 覆盖：

- `Data/discipline_code_assignments.jsonl`
- `Data/classification_code_index.json`

## 后续状态

当前无代码级阻塞。

需要继续推进时，可在后续轮次围绕 preview 审查结果处理具体 owner facts，但这不属于本轮范围。
