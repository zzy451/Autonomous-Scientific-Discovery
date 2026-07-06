# Structured Data Catalog Round 116 Closeout

日期：2026-07-06

## 本轮目标

继续把 analysis DB 中的关系表语义从“由导出代码事实保证”推进到“SQLite 原生结构也显式写死”。本轮聚焦两张关系表：

- `workflow_mirror_paper_modules`
- `paper_general_method_buckets`

这两张表都已经有行集对齐和基础字段约束，但其中一部分关键语义此前还停留在“当前导出正好这样写”的层面。本轮把这部分下沉到 SQLite。

## 本轮修改

修改：
- `scripts/build_analysis_db.py`

### 1. `workflow_mirror_paper_modules` 明确锁定为非主排架镜像行

本轮为 `workflow_mirror_paper_modules` 新增 / 固化：

- `is_primary_for_filing = 0`
- `IFNULL(confidence, '') = ''`

这和当前导出逻辑完全一致：

- workflow mirror 行来自 `final_modules_or_bucket`
- 它不是 canonical filing relation
- 也不携带 canonical confidence

这两条约束现在不再只是“代码这么写”，而是数据库结构本身也会拒绝偏离。

### 2. `paper_general_method_buckets` 补 `source_limited` 值域约束

本轮为 `paper_general_method_buckets` 新增：

- `source_limited IS NULL OR source_limited IN ('', 'no', 'yes')`

这让 general-method bucket 关系表也和其他 evidence / inventory 线保持统一的 source-limited 值域规则。

### 3. build 自检同步覆盖新约束

`validate_relation_table_constraints()` 已同步检查：

- `workflow_mirror_paper_modules` 中新增的 `is_primary_for_filing = 0`
- `workflow_mirror_paper_modules` 中新增的空 confidence 约束
- `paper_general_method_buckets` 中新增的 `source_limited` 值域约束

因此这轮不是只改建表 SQL，而是：

- 建表
- build 自检

两层同时收口。

## 验证

运行：

```bash
python scripts/run_structured_data_pipeline.py --with-execution-audit
```

结果：

- `export_structured_data.py` 通过
- `check_data_consistency.py` 通过
- `build_analysis_db.py` 通过
- `audit_execution_definition.py` 通过

执行定义审计结果：

- `PASS=12`
- `FAIL=0`

## 产出判断

本轮把 canonical module 关系表旁边的两条“辅助关系层”也往正式数据模型方向再推了一步：

- workflow mirror 明确是 mirror，不冒充 canonical filing
- general-method bucket 也具备稳定的 source-limited 语义边界

这和长期方案里“关系表是分析数据库中的正式关系层，不是临时字符串展开结果”的方向一致。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 remaining SQLite guardrails、少量尚未显式化的 derived metadata 语义、以及执行定义与长期方案之间剩余的小闭环项逐轮推进。
