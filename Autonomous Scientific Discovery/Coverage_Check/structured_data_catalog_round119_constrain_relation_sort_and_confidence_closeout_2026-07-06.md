# Structured Data Catalog Round 119 Closeout

日期：2026-07-06

## 本轮目标

继续把 module 关系表的“当前数据事实上如此”推进成“SQLite 原生保证如此”。本轮聚焦：

- `paper_modules`
- `workflow_mirror_paper_modules`

主要收口两类已经由当前导出稳定保证、但此前未显式写死的语义：

- `sort_order` 必须为正序号
- canonical relation 的 `confidence` 不能为空

## 本轮修改

修改：
- `scripts/build_analysis_db.py`

### 1. `paper_modules` 新增正序与非空 confidence 约束

本轮为 canonical formal-module 关系表新增：

- `sort_order >= 1`
- `confidence IS NOT NULL AND confidence <> ''`

这和当前 canonical row 构造逻辑一致：

- 每个 `scientific_object_modules` 行都是按 1 开始排序
- `confidence` 来自 `primary_module_confidence` 或 `classification_source_confidence`
- 现有 843 行数据里这两个事实都已经全量成立

### 2. `workflow_mirror_paper_modules` 新增正序约束

本轮为 workflow mirror relation table 新增：

- `sort_order >= 1`

这和当前 `final_modules_or_bucket` 导出行从 1 开始排序的规则一致，也让 workflow mirror 表不再依赖“默认不会写 0/负数”的隐含假设。

### 3. build 自检同步覆盖

`validate_relation_table_constraints()` 已同步检查：

- `paper_modules` 中新增的 `sort_order >= 1`
- `paper_modules` 中新增的非空 `confidence`
- `workflow_mirror_paper_modules` 中新增的 `sort_order >= 1`

所以这轮依旧是：

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

本轮把 module 关系表里排序与 confidence 这两类核心关系属性也正式推到了 SQLite 原生约束层。这进一步强化了“关系表是正式关系模型，不是松散字符串展开”的实现方向，也和长期方案里多对多关系表应支持稳定查询和分析的目标一致。

## 后续状态

当前无新的代码级阻塞点；可以继续沿 remaining SQLite guardrails、少量尚未显式量化的 metadata / mirror 语义，以及长期方案与当前执行定义之间剩余的小闭环项逐轮推进。
