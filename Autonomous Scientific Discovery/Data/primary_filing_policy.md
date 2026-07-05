# Primary Filing Policy

日期：2026-07-05

本文档定义多模块论文如何选择唯一 `primary_module_for_filing`。事实分类仍由 `scientific_object_modules` 数组和 `general_method_bucket` 表示；主排架位只负责目录、GitHub 管理和 discipline-local code assignment。

## 1. Core Principle

- 事实分类可以多选。
- 排架位置只能有一个。
- Note 路径和 PDF 路径不能反推完整分类事实。
- `primary_module_for_filing` 不能压扁 `scientific_object_modules` 的多模块事实。

## 2. Decision Priority

按以下优先级选择主排架位：

1. 论文实际解决的科学对象问题。
2. 实验验证、benchmark task 或 case study 的主要对象。
3. 论文贡献最直接服务的学科对象。
4. 通用平台 / 方法论文以最实质的应用对象为准。
5. 仍无法判断时，标记低置信度并写明 override reason。

## 3. Required Trace Fields

建议 export / registry 保留以下派生或记录字段：

- `primary_module_confidence`
- `primary_module_assignment_rule`
- `primary_module_override_reason`

Controlled values:

- `primary_module_confidence`: `high`, `medium`, `low`
- `primary_module_assignment_rule`: `main_scientific_object`, `main_validation_object`, `direct_contribution_target`, `substantive_application_object`, `manual_override`

## 4. Multi-Module Handling

Example:

```text
scientific_object_modules = ["06", "07"]
primary_module_for_filing = "06"
discipline_local_code = "06-03-017"
```

The code follows `primary_module_for_filing`; the complete scientific-object fact remains the full module array.

## 5. General-Method-Only Handling

If:

```text
scientific_object_modules = []
general_method_bucket = 01.04
```

Then:

- Do not force `primary_module_for_filing = 01`.
- Do not create a normal `MM-SS-NNN` code.
- Use `assignment_status=non_discipline_general_method` in the assignment ledger.

## 6. Override Discipline

Use `manual_override` only when the standard priorities do not resolve the filing position. Every override must include a concrete reason that can be reviewed later.
