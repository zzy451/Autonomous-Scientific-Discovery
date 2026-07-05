# Structured Data Catalog Round 84 Closeout

日期：2026-07-06

## 本轮目标

继续补强 execution audit 的 ledger 证据，把 `discipline_code_assignments.jsonl` 从“覆盖 active papers + 状态存在”推进到“current snapshot 语义 + 账本审计字段”显式检查。

## 本轮修改

修改：

- `scripts/audit_execution_definition.py`

本轮补强内容：

1. 第 5 项
   - 不再只检查 current snapshot 是否覆盖全部 active papers
   - 现在额外要求：
     - `active_code` 行必须有合法 `MM-SS-NNN`
     - `primary_taxonomy_code_2lvl` 必须有合法 `MM.SS`
     - code 与二级位的 `MM/SS` 必须一致
     - `source_primary_module_for_filing` 必须与 code 主模块一致
     - `pending_secondary` 行不得携带普通 code / 二级位，且 `pending_reason` 必须是允许值
     - `non_discipline_general_method` 行不得携带普通 code / 二级位，且必须对应 pure general-method-only 论文

2. 第 6 项
   - 不再只检查 ledger 文件存在和状态是否合法
   - 现在额外要求：
     - `assignment_id` 必须符合 `DCA-000001` 风格
     - `assignment_id` 全库唯一
     - `assigned_at` 必须符合日期格式
     - `assigned_by` 非空
     - `assignment_reason` 非空
     - `schema_version == 1`

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

第 5 / 6 项当前输出为：

> discipline_code_assignments current snapshot covers all 447 active papers with valid current-status semantics (active=423, pending=15, general_method=9).

> Stable discipline code assignment ledger exists with unique DCA assignment IDs, valid assignment statuses, and auditable assignment metadata fields.

## 产出判断

本轮把 stable ledger 的 execution audit 从“有没有账本”推进为“账本当前状态和审计字段都符合规则”，更贴近长期方案里对 `discipline_code_assignments.jsonl` 的 owner/ledger 角色定义。

## 后续状态

当前无代码级阻塞，可继续沿 registry snapshot 和 remaining execution-definition evidence gaps 往下推进。
