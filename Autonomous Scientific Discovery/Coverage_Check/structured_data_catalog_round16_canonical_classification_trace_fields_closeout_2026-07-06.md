# Structured Data Catalog Round 16 Closeout

日期：2026-07-06

## 本轮目标

把 `master-derived canonical lane` 的 trace 字段真正结构化落到导出层，而不再只停留在治理文件里。

对应来源要求：

- `Data/field_ownership_matrix.md`
- 长期方案中 `required_trace_fields`：
  - `source_field`
  - `source_confidence`
  - `parser_rule`

## 本轮实现

### 1. 在 papers 导出层新增 canonical classification trace 字段

更新：

- `scripts/export_structured_data.py`

新增导出字段：

- `classification_source_field`
- `classification_source_confidence`
- `classification_parser_rule`

当前 trace 规则：

- 若 canonical classification lane 来自 `Remarks` 中的结构化 token：
  - `classification_source_field = "Remarks"`
  - `classification_source_confidence = "high"`
  - `classification_parser_rule = "structured_remark_token"`
- 若走 `01 / 01.04` 的 legacy general-method fallback：
  - `classification_source_field = "Main class;Secondary class"`
  - `classification_source_confidence = "medium"`
  - `classification_parser_rule = "legacy_general_method_fallback"`
- 若走 formal module 的 legacy main-class fallback：
  - `classification_source_field = "Main class"`
  - `classification_source_confidence = "medium"`
  - `classification_parser_rule = "legacy_main_class_fallback"`
- 若未来出现当前规则无法稳定解释的情况：
  - `classification_source_confidence = "low"`
  - `classification_parser_rule = "needs_review"`

### 2. 接入 papers.csv 与 SQLite

更新：

- `scripts/build_analysis_db.py`

新增接入位置：

- `papers.csv`
- SQLite `papers` 表

这样 trace 字段已经贯通：

- `papers.jsonl`
- `papers.csv`
- `papers.sqlite`

### 3. 接入 checker

更新：

- `scripts/check_data_consistency.py`

新增检查：

- `classification_source_field` 必须是字符串
- `classification_source_confidence` 必须属于：
  - `high`
  - `medium`
  - `low`
- `classification_parser_rule` 必须属于：
  - `structured_remark_token`
  - `legacy_general_method_fallback`
  - `legacy_main_class_fallback`
  - `needs_review`
- 若 `classification_parser_rule = structured_remark_token`
  - 则必须：
    - `classification_source_field = Remarks`
    - `classification_source_confidence = high`
- 若 `classification_parser_rule = needs_review`
  - 则必须：
    - `classification_source_confidence = low`

### 4. 文档同步

更新：

- `Data/field_dictionary.md`

补充内容：

- canonical classification trace 字段的语义
- 当前受控枚举
- 它们是 trace fields，不是新的 owner facts

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

spot check：

- `papers.jsonl` 已出现：
  - `classification_source_field`
  - `classification_source_confidence`
  - `classification_parser_rule`
- `papers.csv` 也已包含上述字段

示例：

- `ASD-0001`
  - `classification_source_field = Main class`
  - `classification_source_confidence = medium`
  - `classification_parser_rule = legacy_main_class_fallback`

## 本轮结论

本轮把 canonical classification lane 的来源追踪从“治理要求”推进到了“结构化导出 + checker gate + CSV/SQLite 可用字段”。这样后续分析、排错、review 和 owner 维护时，不再只能从代码里反推当前分类是怎么来的，而可以直接在结构化数据层看到来源与推导规则。
