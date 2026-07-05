# Structured Data Catalog Round 34 Closeout

日期：2026-07-06

## 本轮目标

补齐 `change_log` 这条审计链的“解释与消费”层：

- `field_dictionary.md` 里给 `Data/change_log.jsonl` 一个正式字段说明
- `query_analysis_db.py` 增加按 `change_type` 汇总的查询入口

## 本轮实现

### 1. 为 `Data/change_log.jsonl` 补正式字段说明

更新：

- `Data/field_dictionary.md`

新增条目：

- `### 4.2D Data/change_log.jsonl`

当前说明覆盖：

- `change_id`
- `paper_id`
- `changed_at`
- `changed_by`
- `change_type`
- `old_value`
- `new_value`
- `reason`
- `related_commit`

并明确：

- `change_log` 是轻量审计账本，不是新的内容事实 owner
- 它优先记录 classification / PDF-source / lifecycle 相关 owner 变更
- `last_reviewed_at / last_reviewed_by` 等 derived review 字段可以从这里回投，但它不能反向覆盖 owner fact source

### 2. 为 query 增加 `change-log-summary`

更新：

- `scripts/query_analysis_db.py`
- `Data/README.md`

新增命令：

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" change-log-summary
```

当前输出按 `change_type` 汇总：

- `change_count`
- `paper_count`
- `first_changed_at`
- `last_changed_at`

现有 `change-log` 明细命令仍保留，用于逐行追查。

## 本轮验证

执行：

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" change-log-summary
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

结果：

- `change-log-summary` 可正常输出
- export 成功
- check 成功
- build 成功

当前 summary 结果可见：

- `taxonomy_owner_add_secondary`
  - `change_count = 13`
  - `paper_count = 13`
  - `first_changed_at = 2026-07-06`
  - `last_changed_at = 2026-07-06`

## 本轮结论

本轮没有新增新的 owner 文件或数据表，而是把 `change_log` 从“已经能写入的审计层”推进到“有正式字段定义、并且能在查询层按类型汇总”的状态。这样后续 owner-maintenance 动作不只是可追溯，也更容易被整体审查。
