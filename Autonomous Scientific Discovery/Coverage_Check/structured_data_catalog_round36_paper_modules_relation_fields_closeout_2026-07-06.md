# Structured Data Catalog Round 36 Closeout

日期：2026-07-06

## 本轮目标

补齐长期方案里 `paper_modules` 关系层的核心字段，使它不再只是最小 mixed-scope 展开表，而是带上：

- `is_primary_for_filing`
- `confidence`
- `source`

## 本轮实现

更新：

- `scripts/build_analysis_db.py`
- `Data/README.md`

### 1. 扩展 `paper_modules` 行构造

当前对每条 module assignment row，会额外写入：

- `is_primary_for_filing`
  - 对 canonical `scientific_object_modules` 行，若 `module_code == primary_module_for_filing`，则为 `1`
  - 对 workflow-mirror `final_modules_or_bucket` 行，为 `0`
- `confidence`
  - canonical 主排架行使用 `primary_module_confidence`
  - canonical 非主排架行使用 `classification_source_confidence`
  - workflow-mirror 行当前为空字符串
- `source`
  - canonical 主排架行：
    - `primary_module_for_filing`
  - canonical 非主排架行：
    - `scientific_object_modules`
  - workflow-mirror 行：
    - `final_modules_or_bucket`

### 2. CSV 与 SQLite 同步升级

本轮已同步更新：

- `Data/paper_modules.csv`
- `Data/canonical_paper_modules.csv`
- `Data/workflow_mirror_paper_modules.csv`
- SQLite `paper_modules`

SQLite `paper_modules` 现在新增列：

- `is_primary_for_filing`
- `confidence`
- `source`

### 3. README 同步

更新：

- `Data/README.md`

补充说明：

- `paper_modules.csv` 现在除了 mixed-scope assignment 展开外，也带有 `is_primary_for_filing / confidence / source` trace columns

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
- `Data/discipline_code_initial_assignment_preview.csv` 成功生成 447 行 preview

额外 spot check：

- `paper_modules.csv` 已包含：
  - `is_primary_for_filing`
  - `confidence`
  - `source`
- preview 规则检查通过：
  - `pending_secondary` 行不会生成假 `MM-SS-NNN` code
  - `non_discipline_general_method` 行不会生成普通学科 code
  - `discipline_local_rank` 只在有真实 `proposed_discipline_local_code` 的 `active_code` 行出现
- SQLite `paper_modules` 已包含相同三列
- canonical 主排架行示例：
  - `ASD-0001 / scientific_object_modules / 04 / is_primary_for_filing=1 / confidence=high / source=primary_module_for_filing`
  - `ASD-0003 / scientific_object_modules / 03 / is_primary_for_filing=1 / confidence=medium / source=primary_module_for_filing`

## 本轮结论

本轮把 `paper_modules` 从“只是把模块数组拆开”推进到了“能表达主排架关系和来源置信度”的关系层，更接近长期方案里给出的目标骨架。这样后续围绕主排架与多模块事实的 SQL/CSV 分析会更直接，不必再反查 `papers` 表拼装这些信息。
