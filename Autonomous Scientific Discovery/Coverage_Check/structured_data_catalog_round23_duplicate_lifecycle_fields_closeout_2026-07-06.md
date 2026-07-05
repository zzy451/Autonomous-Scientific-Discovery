# Structured Data Catalog Round 23 Closeout

日期：2026-07-06

## 本轮目标

继续落实长期方案中的 lifecycle 状态层，把当前已经存在于 `Exclusion reason` 文本里的 duplicate 线索结构化为：

- `record_status = duplicate`
- `inclusion_decision = duplicate`
- `duplicate_of = ASD-xxxx`

而不是继续把这些记录一律压成普通 `excluded`。

## 本轮实现

### 1. 在 export 层新增 duplicate 派生

更新：

- `scripts/export_structured_data.py`

新增派生逻辑：

- 只对 `exclusion_reason` 中明确包含 `duplicate` 且能提取出 `ASD-xxxx` 引用的记录派生 `duplicate_of`
- 当前规则不做模糊猜测：
  - 没有明确 duplicate 语义 -> 不派生
  - 没有明确 `ASD-xxxx` -> 不派生

当 `duplicate_of` 非空时：

- `record_status` 改派生为 `duplicate`
- `inclusion_decision` 改派生为 `duplicate`

否则保持原有 lifecycle 逻辑：

- `active_confirmed_core`
- `background_only`
- `excluded`
- `candidate`

### 2. 把 duplicate lifecycle 写入 analysis 输出

本轮不需要新增新表，现有 analysis 层已经有字段位：

- `papers.jsonl`
- `papers.csv`
- SQLite `papers`

因此本轮重点是把值真正写实，而不是继续保留空字符串。

### 3. 接入 checker

更新：

- `scripts/check_data_consistency.py`

新增检查：

- `duplicate_of` 必须与 `exclusion_reason` 中 duplicate 语义按当前规则重算后的结果一致
- 若 `duplicate_of` 非空：
  - 必须符合 `ASD-xxxx`
  - 不得自指
  - 必须能回连到现有 `papers.jsonl.paper_id`
  - `record_status` 必须为 `duplicate`
  - `inclusion_decision` 必须为 `duplicate`

另外，本轮把方案里点名的部分 `INFO` 也补得更完整：

- `background_only` 记录现在会进入 integrity report 的 `INFO`
- `duplicate` 记录现在也会进入 integrity report 的 `INFO`

### 4. 文档同步

更新：

- `Data/README.md`
- `Data/field_dictionary.md`
- `Data/field_ownership_matrix.md`

补充内容：

- lifecycle derived lane 现在明确包括：
  - `record_status`
  - `inclusion_decision`
  - `duplicate_of`
- duplicate linkage 目前来自 master `Exclusion reason` 中的明确文本证据，不是新的 owner fact source

## 本轮验证

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

额外 spot check：

- `papers.jsonl` 中 `record_status = duplicate` 的记录数：`31`
- `duplicate_of` 非空记录数：`31`
- SQLite `papers` 中：
  - `record_status = duplicate` 记录数：`31`
  - `duplicate_of <> ''` 记录数：`31`

示例：

- `ASD-0026`
  - `exclusion_reason` 明确写有：
    - `Duplicate journal-upgrade record of ASD-0522`
  - 当前导出为：
    - `record_status = duplicate`
    - `inclusion_decision = duplicate`
    - `duplicate_of = ASD-0522`

## 本轮结论

本轮把 lifecycle 层里最明显的一块“文本里已经说明是 duplicate，但结构化字段里还看不出来”的落差补上了。这样后续做 duplicate inventory、排除原因统计、canonical lineage 抽查时，不再只能重新读 `Exclusion reason` 自然语言。
