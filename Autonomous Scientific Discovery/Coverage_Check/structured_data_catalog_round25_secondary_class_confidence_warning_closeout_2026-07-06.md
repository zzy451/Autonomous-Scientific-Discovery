# Structured Data Catalog Round 25 Closeout

日期：2026-07-06

## 本轮目标

继续把 `Data/check_policy.md` 里的显式 warning 做实，补上 `secondary_class_confidence=low` 这一类目前还没有进入 integrity report 的治理信号。

## 本轮实现

更新：

- `scripts/check_data_consistency.py`

本轮新增：

- `SECONDARY_CLASS_CONFIDENCE_LOW_SUMMARY`

实现方式：

- 不为每篇论文逐条刷出 warning
- 改为基于 `papers.jsonl.secondary_class_confidence` 生成一条汇总 warning
- 当前汇总内容包含：
  - 全库 `secondary_class_confidence=low` 的记录数
  - 其中 active confirmed-core 的记录数

这样做的原因是当前 low-confidence secondary-class 状态仍然非常普遍，若逐条写入 report，会让报告迅速失真成噪音；而汇总 warning 仍然保留了足够强的治理可见性。

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

- `SECONDARY_CLASS_CONFIDENCE_LOW_SUMMARY` 已进入 `Data/integrity_check_report.md`
- report 仍同时保留：
  - `PRIMARY_MODULE_CONFIDENCE_LOW`
  - `SUPPLEMENTARY_ONLY_SOURCE_STATE`
  - 先前已实现的其他 non-blocking findings

## 本轮结论

本轮继续把 `check_policy` 从“文档列举”推进成“真实报告输出”。现在 secondary-class 低置信度不再完全埋在字段值里，而是会通过 integrity report 的汇总 warning 直接暴露出来，更适合后续做二级 taxonomy review 和 legacy secondary-class 收敛。
