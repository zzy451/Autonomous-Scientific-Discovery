# ASD 结构化数据 Phase 4 第二轮执行记录

日期：2026-07-02

对应方案：

- `Coverage_Check/structured_data_post_phase2_execution_plan_2026-07-02.md`

本轮目标：

- 将常用 canonical 统计模板固化成稳定查询出口
- 让后续综述写作、图表统计和 spot-check 不再依赖临时 SQL

## 1. 本轮新增的 canonical 统计出口

### 1.1 数据库视图

在 `scripts/build_analysis_db.py` 中新增：

- `canonical_object_coverage_summary`
- `canonical_multi_module_combo_summary`
- `canonical_formal_module_pdf_coverage_summary`
- `canonical_bucket_0104_papers`
- `canonical_bucket_0104_summary`

这些视图都只面向 canonical 口径，不读取 workflow mirror 作为默认分类事实。

### 1.2 查询命令

在 `scripts/query_analysis_db.py` 中新增：

- `module-distribution`
- `object-coverage-summary`
- `multi-module-combo-summary`
- `module-pdf-coverage`
- `bucket-0104-summary`

同时保留此前已有的：

- `summary`
- `module`
- `multi-module`
- `boundary-cases`
- `bucket-summary`

其中：

- 新增命令全部面向 canonical 统计模板
- `boundary-cases` 与 `bucket-summary` 继续保留为 audit 命令

## 2. 本轮验证命令

本轮实际执行：

```text
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" module-distribution
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" object-coverage-summary
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" multi-module-combo-summary --limit 10
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" module-pdf-coverage --sort missing
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" bucket-0104-summary --details --limit 5
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
```

## 3. 本轮确认下来的关键 canonical 数值

### 3.1 formal module 分布

通过 `module-distribution` 固定下来的基线：

- active confirmed-core record count：`447`
- active formal module assignment count：`577`
- active general-method `01.04` count：`9`

### 3.2 object coverage 模式分布

通过 `object-coverage-summary` 固定下来的 active confirmed-core record-level 分布：

- `single_module = 334`
- `multi_module = 104`
- `general_method_without_concrete_object_experiments = 9`

### 3.3 multi-module 组合分布

通过 `multi-module-combo-summary --limit 10` 固定下来的头部组合：

- `06+07 = 25`
- `03+04 = 16`
- `05+10 = 13`
- `03+07 = 12`

这已经足够直接服务共现图、组合条形图和边界讨论。

### 3.4 按 formal module 的 PDF coverage

通过 `module-pdf-coverage --sort missing` 固定下来的头部缺口模块：

- `04: 117 / 109 / 8`
- `03: 90 / 83 / 7`
- `07: 80 / 76 / 4`
- `06: 78 / 74 / 4`
- `05: 37 / 33 / 4`

这里分别对应：

- `active_assignment_count`
- `active_local_pdf_count`
- `active_missing_local_pdf_count`

### 3.5 独立 `01.04` canonical bucket

通过 `bucket-0104-summary` 固定下来的 canonical bucket 基线：

- total paper count：`169`
- active confirmed-core count：`9`
- active local PDF count：`9`
- active missing local PDF count：`0`
- active note count：`9`
- active source-limited count：`3`

## 4. 本轮结果解释

本轮完成后，Phase 4 不再只有“默认查询必须 canonical-only”的语义约束，而是已经拥有一组可直接复用的 canonical 统计模板：

1. formal module 分布
2. object coverage 模式分布
3. multi-module 组合分布
4. 按模块 PDF coverage
5. 独立 `01.04` bucket 统计

这意味着后续正文写作、图表绘制和模块对比，已经可以复用固定命令，而不是临时拼接 SQL。

## 5. 与上一轮的衔接

上一轮 Phase 4 第一轮解决的是：

- 默认查询 = canonical-only
- mirror = audit-only

本轮解决的是：

- canonical 统计模板固化

两轮合在一起，已经把“默认语义”和“高频统计出口”都推进到稳定状态。

## 6. 下一步建议

按当前总方案，下一步最合适进入的是：

1. 面向协作者的简明 SOP
2. baseline 更新纪律的协作化写法
3. 在协作规则稳定后，再启动 note revision queue / follow-up queue 的并行生产准备
