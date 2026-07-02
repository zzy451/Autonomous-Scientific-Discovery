# ASD 结构化数据 Phase 4 第一轮执行记录

日期：2026-07-02

对应方案：

- `Coverage_Check/structured_data_post_phase2_execution_plan_2026-07-02.md`

本轮目标：

- 将默认查询与默认统计进一步显式收紧为 `canonical-only`
- 将 workflow mirror 保留为显式 audit 语义，而不是默认分类统计入口

## 1. 本轮完成的改动

### 1.1 SQLite 视图层

在 `scripts/build_analysis_db.py` 中补充了显式 scope-separated 视图：

- `canonical_paper_modules`
- `workflow_mirror_paper_modules`
- `canonical_module_assignment_counts`
- `workflow_mirror_module_assignment_counts`

这意味着后续默认分类统计不再需要依赖“从混合表里手写 `assignment_scope` 过滤”才能站稳 canonical 口径。

### 1.2 boundary audit 语义

在 `classification_boundary_analysis` 中补充了：

- `scientific_modules_declared_order`
- `final_formal_modules_declared_order`
- `scientific_matches_final_formal_order`
- `drift_class`

并把原先的 `bucket_only_consistent` 收紧为 `acceptable_mirror`。

这样：

- `semantic_drift`
- `order_drift`
- `acceptable_mirror`
- `aligned`

这几类语义在 SQLite 审计层已经能明确分开。

### 1.3 CLI 默认语义

在 `scripts/query_analysis_db.py` 中完成了以下收口：

- `summary` 明确打印 `Canonical Summary`
- `module` 与 `multi-module` 明确走 canonical 入口
- `paper` 输出前先打印 canonical / workflow mirror 语义提示
- `boundary-cases` 默认只显示真实 drift，不再把 `acceptable_mirror` 当作默认异常
- `bucket-summary` 标题改为 `01.04 Canonical-vs-Mirror Audit Summary`
- CLI 顶层与子命令 help 补入 canonical-only / audit-only 提示

### 1.4 文档层

在 `Data/README.md` 中补充了：

- `paper_modules.csv` 同时包含 canonical 与 mirror 两类 assignment，使用前必须按 `assignment_scope` 过滤
- SQLite 中优先使用显式 scope-separated 视图
- 默认查询语义解释：除非命令显式标注 `audit/mirror`，否则分类输出应理解为 canonical-only

## 2. 本轮验证

### 已执行命令

```text
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" summary
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" boundary-cases --limit 10
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" bucket-summary --limit 5
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" paper ASD-0715
```

### 验证结果

1. `summary` 现在明确输出 `Canonical Summary`，模块统计继续保持当前 baseline。
2. `boundary-cases --limit 10` 当前返回 `No rows found.`，符合“当前 drift 已清零”的状态。
3. `bucket-summary` 仍可审计 `01.04`，但输出已明确属于 canonical-vs-mirror audit。
4. `paper ASD-0715` 会先打印语义提醒，并把：
   - `canonical_module_assignments`
   - `workflow_mirror_assignments`
   显式分开。

## 3. 本轮结论

本轮可以认为 Phase 4 的第一段已经完成：

- 默认分类查询入口已经进一步向 `canonical-only` 收紧
- workflow mirror 已经在模式层、CLI 层、文档层被更明确地降为 audit 语义
- 当前数据库查询语义比上一轮更不容易发生“把 mirror 当 canonical”的误用

## 4. 下一步建议

继续按方案推进时，最合适的下一步是：

1. 固化一套常用 canonical 统计模板
2. 视需要增加一个更显式的 mirror audit summary 命令
3. 开始准备面向协作者的简明 SOP，把 baseline 更新纪律和查询语义一起写进协作规则
