# Structured Data Catalog Round 117 Closeout

日期：2026-07-06

## 本轮目标

继续把 analysis DB 的关系表语义从“当前导出逻辑事实上如此”推进到“SQLite 结构层显式写死”。本轮聚焦：

- `workflow_mirror_paper_modules`
- `paper_general_method_buckets`

这两张表此前虽然已经有基本字段和行集校验，但仍有一部分关键语义只在导出代码里隐含成立。本轮把它们正式下沉到 SQLite。

## 本轮修改

修改：
- `scripts/build_analysis_db.py`

### 1. `workflow_mirror_paper_modules` 明确锁定为非主排架 mirror 表

本轮新增 / 固化：

- `is_primary_for_filing = 0`
- `IFNULL(confidence, '') = ''`

这和当前 workflow mirror 的真实角色一致：

- 来源是 `final_modules_or_bucket`
- 不是 canonical filing relation
- 不承载 canonical confidence

之前这层语义主要依赖导出代码和 build 行集对齐；现在 SQLite 本身也会拒绝偏离。

### 2. `paper_general_method_buckets` 补 `source_limited` 值域约束

本轮新增：

- `source_limited IS NULL OR source_limited IN ('', 'no', 'yes')`

这样 general-method bucket 关系表在 source-limited 表达上也和 papers / PDF / asset / missing-PDF 等其他证据链派生层保持统一。

### 3. build 自检同步覆盖新约束

`validate_relation_table_constraints()` 已同步检查：

- `workflow_mirror_paper_modules` 的非主排架约束
- `workflow_mirror_paper_modules` 的空 confidence 约束
- `paper_general_method_buckets` 的 `source_limited` 值域约束

因此这轮不是只改建表 SQL，而是把：

- 建表
- build 自检

两层一起收口。

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

本轮把 relation-table 这条线继续从“逻辑正确”推进到“结构上也写死正确”：

- workflow mirror 更明确地保持 mirror 身份
- general-method bucket 的 source-limited 语义更正式

这和长期方案里分析数据库中的关系表要作为正式关系层、而不是松散中间产物的方向一致。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 remaining SQLite guardrails、metadata 边缘语义、以及长期方案与执行定义之间剩余的少量闭环项逐轮推进。
