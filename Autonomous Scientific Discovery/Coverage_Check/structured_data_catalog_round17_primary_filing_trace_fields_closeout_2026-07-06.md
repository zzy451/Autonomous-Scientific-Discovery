# Structured Data Catalog Round 17 Closeout

日期：2026-07-06

## 本轮目标

把 `primary_filing_policy.md` 里建议保留的主排架 trace 字段真正结构化落地，而不再只停留在治理文件中。

目标字段：

- `primary_module_confidence`
- `primary_module_assignment_rule`
- `primary_module_override_reason`

## 本轮实现

### 1. 在 papers 导出层新增 primary filing trace 字段

更新：

- `scripts/export_structured_data.py`

新增导出字段：

- `primary_module_confidence`
- `primary_module_assignment_rule`
- `primary_module_override_reason`

当前派生规则：

- pure `01.04` general-method-only 记录
  - 三个字段均为空
- 单模块 formal record
  - `primary_module_confidence = high`
  - `primary_module_assignment_rule = main_scientific_object`
  - `primary_module_override_reason = ""`
- 多模块且由显式 `Remarks` 主排架 token 支撑
  - `primary_module_confidence = medium`
  - `primary_module_assignment_rule = manual_override`
  - `primary_module_override_reason = structured_remark_primary_module_for_filing`
- 多模块且主要依赖 legacy main-class fallback
  - `primary_module_confidence = low`
  - `primary_module_assignment_rule = manual_override`
  - `primary_module_override_reason = legacy_main_class_fallback_for_multi_module`

### 2. 接入 discipline registry / CSV / SQLite

更新：

- `scripts/export_structured_data.py`
- `scripts/build_analysis_db.py`

新增接入位置：

- `papers.jsonl`
- `papers.csv`
- SQLite `papers`
- `discipline_local_code_registry.jsonl`
- `discipline_local_code_registry.csv`
- SQLite `discipline_local_code_registry`

这意味着主排架 trace 现在已经贯通了 paper snapshot 与 discipline-local snapshot 两条结构化链路。

### 3. 接入 checker

更新：

- `scripts/check_data_consistency.py`

新增检查：

- `primary_module_confidence` 必须是字符串
- `primary_module_assignment_rule` 必须是字符串
- `primary_module_override_reason` 必须是字符串
- formal module records 中：
  - `primary_module_confidence` 必须属于 `high / medium / low`
  - `primary_module_assignment_rule` 必须属于 policy 中允许的受控值
- pure general-method-only 记录：
  - 三个字段都必须为空
- 单模块 record：
  - 必须使用
    - `primary_module_confidence = high`
    - `primary_module_assignment_rule = main_scientific_object`
    - 空 `primary_module_override_reason`
- 若 `primary_module_assignment_rule = manual_override`
  - 必须有非空 `primary_module_override_reason`
- discipline registry 中这三个字段必须与 `papers` snapshot 一致

### 4. 文档同步

更新：

- `Data/field_dictionary.md`

新增内容：

- primary filing trace 字段语义
- 当前受控枚举
- 当前导出层已使用的派生模式
- 这些字段属于 derived trace，而不是新的 owner facts

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

- `papers.csv` 已包含：
  - `primary_module_confidence`
  - `primary_module_assignment_rule`
  - `primary_module_override_reason`
- `discipline_local_code_registry.csv` 也已包含相同字段

示例：

- `ASD-0001`
  - `primary_module_for_filing = 04`
  - `primary_module_confidence = high`
  - `primary_module_assignment_rule = main_scientific_object`
- `ASD-0003`
  - `primary_module_for_filing = 03`
  - `primary_module_confidence = medium`
  - `primary_module_assignment_rule = manual_override`
  - `primary_module_override_reason = structured_remark_primary_module_for_filing`

## 本轮结论

本轮把主排架位的解释字段从“政策建议”推进到了“结构化导出 + registry 冗余 + SQLite 可查 + checker 强制”的状态。这样后续遇到多模块论文时，不再只能看到一个 `primary_module_for_filing` 结果，而可以在结构化数据层同时看到它的置信度、采用的分配规则和当前 override / fallback 理由。
