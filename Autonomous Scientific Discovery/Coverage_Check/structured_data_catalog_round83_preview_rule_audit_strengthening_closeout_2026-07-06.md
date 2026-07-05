# Structured Data Catalog Round 83 Closeout

日期：2026-07-06

## 本轮目标

继续补强 execution audit 的 preview 审计能力，让 `discipline_code_initial_assignment_preview.csv` 不再只做存在性与覆盖面检查，而是校验关键分配规则。

## 本轮修改

修改：

- `scripts/audit_execution_definition.py`

第 8 项新增检查内容：

- preview `paper_id` 覆盖必须与全部 active papers 一致
- `proposed_assignment_status` 只能是：
  - `active_code`
  - `pending_secondary`
  - `non_discipline_general_method`

- `pending_secondary` 行必须满足：
  - `proposed_discipline_local_code` 为空
  - `discipline_local_rank` 为空
  - `proposed_primary_taxonomy_code_2lvl` 为空
  - `pending_reason` 只能是：
    - `missing_primary_module_for_filing`
    - `missing_or_uncertain_secondary_class`
    - `secondary_primary_mismatch`

- `non_discipline_general_method` 行必须满足：
  - `general_method_bucket != none`
  - `scientific_object_modules = []`
  - 不携带 proposed code / rank / secondary / pending_reason

- `active_code` 行必须满足：
  - `proposed_discipline_local_code` 符合 `MM-SS-NNN`
  - `discipline_local_rank` 与 code 末段一致
  - `proposed_primary_taxonomy_code_2lvl` 符合 `MM.SS`
  - code 与 secondary 的 `MM/SS` 必须一致
  - 不携带 `pending_reason`

## 验证

运行：

```bash
python "Autonomous Scientific Discovery/scripts/run_structured_data_pipeline.py" --with-execution-audit
```

结果：

- `export_structured_data.py` 通过
- `check_data_consistency.py` 通过
- `build_analysis_db.py` 通过
- `audit_execution_definition.py` 通过

执行定义审计结果：

- `PASS=12`
- `FAIL=0`

第 8 项当前输出为：

> discipline_code_initial_assignment_preview.csv matches the active-paper review surface and obeys preview assignment rules (active=423, pending=15, general_method=9).

## 产出判断

本轮把 preview 从“文件存在、行数对得上”推进成“关键 preview 规则已经被 execution audit 显式检查”，更贴近长期方案里对 initial assignment preview 的作用定义。

## 后续状态

当前无代码级阻塞，可继续沿 ledger / registry 等仍偏浅的执行定义条目推进。
