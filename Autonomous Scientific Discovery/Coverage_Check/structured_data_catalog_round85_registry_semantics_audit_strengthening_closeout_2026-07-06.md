# Structured Data Catalog Round 85 Closeout

日期：2026-07-06

## 本轮目标

继续补强 execution audit 的 registry snapshot 证据，让 `discipline_local_code_registry` 不再只做“文件存在 + metadata 对齐”检查，而是验证其确实由当前 ledger 与 paper snapshot 正确派生。

## 本轮修改

修改：

- `scripts/audit_execution_definition.py`

第 9 项新增检查内容：

- 每条 registry row 必须能回连：
  - active paper snapshot
  - current ledger snapshot row

- 关键镜像字段必须一致：
  - `assignment_status`
  - `assignment_id`
  - `title`
  - `scientific_object_modules`
  - `general_method_bucket`
  - `primary_module_for_filing`
  - `note_path`
  - `pdf_path`
  - `active_confirmed_core`

- `is_derived_snapshot` 必须为 `true`
- `generated_by` 必须是 `export_structured_data.py`

- 对不同状态增加显式规则：

1. `active_code`
   - `discipline_local_code` 必须合法
   - `discipline_local_rank` 必须等于 code 末段
   - `discipline_display_order` 必须等于 code 本身
   - `primary_taxonomy_code_2lvl` 必须合法

2. `pending_secondary`
   - 不得携带普通 code / rank / 二级位
   - `discipline_display_order` 必须按主模块前缀构造

3. `non_discipline_general_method`
   - 不得携带普通 code / rank / 二级位
   - `discipline_display_order` 必须以 `GM-PENDING-` 开头

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

第 9 项当前输出为：

> discipline_local_code_registry is present in JSONL / CSV / SQLite with aligned derived snapshot metadata and current-snapshot semantics (active=423, pending=15, general_method=9).

## 产出判断

本轮把 registry snapshot 的 execution audit 从“derived 文件存在”推进成“derived 文件确实按 ledger + paper snapshot 规则派生”，更贴近长期方案里对 registry 作为 derived snapshot 的角色定义。

## 后续状态

当前无代码级阻塞，可继续沿仍偏浅的执行定义证据项推进。
