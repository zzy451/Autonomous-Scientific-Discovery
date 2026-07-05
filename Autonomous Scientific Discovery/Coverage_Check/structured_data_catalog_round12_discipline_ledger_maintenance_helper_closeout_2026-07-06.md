# Structured Data Catalog Round 12 Closeout

日期：2026-07-06

## 本轮目标

补齐 `Data/discipline_code_assignments.jsonl` 的日常 owner 维护入口，使后续 discipline code 变更不再依赖手工直接改 ledger，并且让 ledger 变更和 `Data/change_log.jsonl` 审计记录同步发生。

## 本轮实现

### 1. 新增 owner-ledger 日常维护脚本

新增：

- `scripts/manage_discipline_code_assignments.py`

能力范围：

- 对单篇论文维护当前 discipline-code snapshot
- 支持三类 current target：
  - `active_code`
  - `pending_secondary`
  - `non_discipline_general_method`
- 如果当前行是 `pending_secondary` / `non_discipline_general_method`
  - 允许原地改写该 current row
- 如果当前行是 `active_code`
  - 必须先用 `retired_code` 或 `redirected_code` 关闭旧 current row
  - 再追加新的 current row
- 自动按二级位分配下一个未使用的 `MM-SS-NNN`
- 拒绝复用历史上已经出现过的 `discipline_local_code`
- 默认自动追加一条对应 `change_log` 审计记录
- 提供 `--dry-run`，可先模拟 ledger 变更而不写盘

### 2. 补强 ledger 一致性检查

更新：

- `scripts/check_data_consistency.py`

新增硬约束：

- `discipline_local_code` 在 owner ledger 中必须全局唯一
- 不仅 active code 不能重复，历史 `retired_code` / `redirected_code` 也不得被后续复用

这一步把 policy 里“旧 code 不复用”的规则真正变成了 checker 的阻断项。

### 3. 文档同步

更新：

- `Data/README.md`
- `Data/discipline_code_assignment_policy.md`

同步内容：

- 明确 `scripts/manage_discipline_code_assignments.py` 是 day-to-day owner ledger 维护入口
- 说明它与 `change_log` 的配套关系

## 本轮验证

### 1. 新脚本帮助输出

执行：

```bash
python "Autonomous Scientific Discovery/scripts/manage_discipline_code_assignments.py" --help
```

结果：

- 帮助输出正常
- 参数面向日常 ledger 维护而非 export

### 2. dry-run 维护流程演练

执行：

```bash
python "Autonomous Scientific Discovery/scripts/manage_discipline_code_assignments.py" ^
  --paper-id ASD-0060 ^
  --target-status active_code ^
  --assignment-reason resolve_pending_secondary ^
  --change-reason "Dry-run test for pending-secondary resolution workflow" ^
  --effective-date 2026-07-06 ^
  --primary-taxonomy-code-2lvl 04.04 ^
  --close-current-as retired_code ^
  --dry-run
```

结果：

- 成功模拟将 `ASD-0060` 的 current row 从 `pending_secondary` 解析为 `active_code`
- 自动给出候选新 code：`04-04-070`
- 未写盘，符合 dry-run 预期

### 3. 全链验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- export 成功
- check 成功
- build 成功

当前主链状态：

- `papers.jsonl` records: 871
- `active confirmed-core`: 447
- `discipline_code_assignments` rows: 447
- `discipline_local_code_registry` rows: 447

## 本轮结论

本轮把 discipline code 账本从“已初始化但缺少正式维护入口”的状态，推进到“已有日常 owner 维护脚本 + checker 阻断旧 code 复用 + 文档同步”的状态。这样后续真正发生 pending 解析、主排架位迁移、old code retired / redirected 时，已经有正式脚本路径可走。
