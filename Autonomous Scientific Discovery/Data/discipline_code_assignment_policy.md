# Discipline Code Assignment Policy

日期：2026-07-05

本文件定义 `Data/discipline_code_assignments.jsonl` 的稳定管理码分配规则。`ASD-xxxx` 仍是唯一永久论文身份号；`discipline_local_code` 只是稳定排架 / 管理 / 展示码。

## 1. Assignment ID

- `assignment_id` 使用 `DCA-000001` 递增格式。
- 一旦分配永久不变。
- 不得因为排序、删除、`retired_code`、`redirected_code`、分类变化或文件移动而重排。
- 新增 assignment 使用当前最大编号 + 1。
- `assignment_id` 不依赖 `paper_id`、`discipline_local_code` 或分类位置。

## 2. Discipline Local Code

格式：

```text
MM-SS-NNN
```

- `MM`: 一级科学对象模块，如 `04`
- `SS`: 二级位，如 `03`
- `NNN`: 同一二级位下的稳定顺序号，如 `001`

规则：

- 同一 active `discipline_local_code` 不得指向多篇论文。
- 新增论文默认在对应二级位下追加最大 `NNN + 1`。
- 已分配 code 不因标题、年份、排序或新增论文而变化。
- `discipline_local_code` 不是永久主键，不替代 `paper_id`。

## 3. Assignment Status

允许值：

| assignment_status | Meaning | `discipline_local_code` |
|---|---|---|
| `active_code` | 当前有效学科管理码 | non-null |
| `retired_code` | 旧 code 不再使用，也不推荐自动跳转 | non-null |
| `redirected_code` | 旧 code 不再 active，但应跳转到新的 active code | non-null |
| `pending_secondary` | 二级位缺失或不确定，暂不分配普通 code | null |
| `non_discipline_general_method` | pure `01.04` general-method-only record，不进入普通学科排架 | null |

## 4. Retired vs Redirected

`retired_code`：

- 适用于误分配、撤销、记录不再适合学科排架。
- `redirected_to_code` 必须为 null。

`redirected_code`：

- 适用于论文主排架位改变、编码迁移、分类规范化后仍希望旧引用可追踪。
- `redirected_to_code` 必须指向合法 active `discipline_local_code`。
- `redirected_to_code` 指向 code，不指向 `paper_id`。

## 5. Per-Paper Constraints

- 一篇论文可以有多条 assignment 历史记录。
- 同一 `paper_id` 最多只能有一条 `active_code`。
- `active_code` / `retired_code` / `redirected_code` 必须有非空 `discipline_local_code`。
- `pending_secondary` / `non_discipline_general_method` 必须有空 `discipline_local_code`。

## 6. Initial Assignment Workflow

1. Generate `Data/discipline_code_initial_assignment_preview.csv`.
2. Review secondary class gaps, multi-module filing choices, pure general-method records, source-limited records, and legacy-class anomalies.
3. Fix owner files first: master, progress, or `classification_code_index.json`.
4. Generate `Data/discipline_code_assignments.jsonl` with `assignment_reason=initial_assignment`.
5. Freeze the initial ledger. Future additions append; existing active codes are not globally re-ranked.

## 7. Daily Maintenance Workflow

- Prefer `scripts/manage_discipline_code_assignments.py` for day-to-day owner-ledger changes so the ledger update and matching `change_log` row stay in sync.
- New paper with clear secondary position: append a new `active_code`.
- Missing or uncertain secondary position: append `pending_secondary` with `pending_reason`.
- Pure general-method-only record: append `non_discipline_general_method`.
- Filing position change: change old active assignment to `retired_code` or `redirected_code`, then append a new `active_code`.
- Classification array changes without filing-position change: keep the existing `active_code`.

Every ledger edit must be explainable in git diff and pass `check_data_consistency.py`.
