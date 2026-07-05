# Structured Data Catalog Round 24 Closeout

日期：2026-07-06

## 本轮目标

继续落实长期方案里的 `check_policy`，把已经写进 policy 的部分 `WARNING / INFO` 真实产出到 `Data/integrity_check_report.md`，而不是继续只停留在文档说明里。

## 本轮实现

### 1. 补齐更多 non-blocking findings

更新：

- `scripts/check_data_consistency.py`

本轮新增的报告项：

- `PRIMARY_MODULE_CONFIDENCE_LOW`
  - 对 active confirmed-core 且 `primary_module_confidence=low` 的记录给出 `WARNING`
- `MISSING_LOCAL_PDF_WITH_ALTERNATE_SOURCE`
  - 对 active confirmed-core、无本地 PDF、但仍有 `official_page / project_page / html_full_text / abstract` 等替代一手来源的记录给出 `WARNING`
- `SUPPLEMENTARY_ONLY_SOURCE_STATE`
  - 对 active confirmed-core 且当前 `pdf_evidence_type=supplementary_pdf` 的记录给出 `INFO`

这几类都对应长期方案和 `Data/check_policy.md` 里已经明确提到的非阻断状态。

### 2. 保持当前已实现的 non-blocking lifecycle / evidence 语义

本轮没有改动四类事实源，也没有改动 export/build 语义，只增强 checker 报告层。

当前 integrity report 里已经覆盖的代表性非阻断状态包括：

- `SOURCE_LIMITED`
- `PENDING_SECONDARY`
- `NON_DISCIPLINE_GENERAL_METHOD`
- `BACKGROUND_ONLY_RECORD`
- `DUPLICATE_RECORD`
- `SECONDARY_TERM_NEEDS_REVIEW`
- 本轮新增的 3 类 report item

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

- `PRIMARY_MODULE_CONFIDENCE_LOW` 已进入 integrity report
- `SUPPLEMENTARY_ONLY_SOURCE_STATE` 已进入 integrity report
- `MISSING_LOCAL_PDF_WITH_ALTERNATE_SOURCE` 已进入 integrity report

## 本轮结论

本轮没有增加新的 owner / derived 文件，而是把已有治理方案里的 `check_policy` 进一步做实。这样后续看 `integrity_check_report.md` 时，low-confidence filing、supplementary-only、以及“没本地 PDF 但仍有替代一手来源”的状态会更直接暴露出来，不需要再靠人工读 policy 才知道这些情况应该被关注。
