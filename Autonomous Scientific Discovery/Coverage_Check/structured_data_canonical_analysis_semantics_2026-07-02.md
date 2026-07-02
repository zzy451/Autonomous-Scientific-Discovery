# ASD canonical-only 分析口径固化说明

日期：2026-07-02
对应阶段：`structured_data_post_phase2_execution_plan_2026-07-02.md` 的 `Phase 4`

本文档把当前 structured-data 的默认分析口径固定为 canonical-only，并明确哪些命令属于正式统计面，哪些命令只属于 audit / inspection。

## 1. 默认原则

从本文件起，凡是没有明确标注 `audit` / `mirror` 的分类统计命令，默认都只解释为 canonical-only。

这里的 canonical classification 只认：

- `scientific_object_modules`
- `general_method_bucket`

这里的 workflow mirror 只认：

- `final_modules_or_bucket`

因此：

- `scientific_object_modules` 支撑 formal `01-11` 统计
- `general_method_bucket` 单独支撑 canonical `01.04` bucket 统计
- `final_modules_or_bucket` 只用于 drift / boundary / mirror audit

## 2. 固定指标表头

本轮之后，默认分析时优先使用以下固定指标名：

- `active_confirmed_core_record_count`
  - 含义：当前 active confirmed-core 的 unique paper record 数
- `active_records_with_formal_modules_count`
  - 含义：当前 active confirmed-core 中，至少带一个 canonical formal module 的 record 数
- `active_general_method_bucket_record_count`
  - 含义：当前 active confirmed-core 中，处于 canonical `01.04` bucket 的 record 数
- `active_single_module_record_count`
  - 含义：当前 active confirmed-core 中，`object_coverage_mode = single_module` 的 record 数
- `active_multi_module_record_count`
  - 含义：当前 active confirmed-core 中，`object_coverage_mode = multi_module` 的 record 数
- `active_general_method_record_count`
  - 含义：当前 active confirmed-core 中，`object_coverage_mode = general_method_without_concrete_object_experiments` 的 record 数
- `active_single_or_general_record_count`
  - 含义：`active_single_module_record_count + active_general_method_record_count`
- `active_formal_module_assignment_count`
  - 含义：当前 active confirmed-core 中，expanded canonical formal-module assignment 总数
- `active_general_method_bucket_assignment_count`
  - 含义：当前 active confirmed-core 中，expanded canonical `01.04` bucket assignment 总数
- `active_total_canonical_assignment_count`
  - 含义：`active_formal_module_assignment_count + active_general_method_bucket_assignment_count`

## 3. record count 与 assignment count 的固定区别

后续所有统计必须显式区分：

### 3.1 record count

record count 统计的是 unique papers。

例如：

- `active_confirmed_core_record_count = 447`

### 3.2 assignment count

assignment count 统计的是 canonical 分类展开后的 assignment 总数。

例如：

- 一篇 single-module `03` 论文贡献 `1` 个 formal assignment
- 一篇 multi-module `03;04;07` 论文贡献 `3` 个 formal assignments
- 一篇 canonical `01.04` bucket 论文不贡献 formal assignment，但贡献 `1` 个 general-bucket assignment

因此：

- formal `01-11` 分布图默认使用 `active_formal_module_assignment_count` 作为 assignment 分母
- 任何把 assignment count 直接读成 unique-paper count 的做法，都是错误解读

## 4. `01.04` 的固定统计位置

`01.04` 必须始终保持为独立 canonical bucket：

- 它不进入 formal `01-11` 的 module-distribution 分母
- 它不进入 formal `01-11` 的 per-module assignment 行
- 它应通过单独的 `bucket-0104-summary` 读取
- 若需要 total canonical assignment count，则把 formal assignments 与 `01.04` bucket assignments 相加，但仍需分开列出

## 5. 命令分层

### 5.1 canonical-only 默认统计命令

以下命令默认属于 canonical-only：

- `summary`
- `analysis-baseline`
- `module-distribution`
- `object-coverage-summary`
- `multi-module`
- `multi-module-combo-summary`
- `module`
- `module-pdf-coverage`
- `bucket-0104-summary`

### 5.2 audit / mirror 命令

以下命令不属于默认 canonical 分类统计，而属于 audit / mirror：

- `boundary-cases`
- `bucket-summary`

### 5.3 mixed inspection 命令

以下命令用于 inspection，不应直接被当成 canonical count report：

- `paper`
  - 同时显示 canonical fields 与 workflow mirror fields

### 5.4 非分类统计命令

以下命令可用于 coverage / corpus 描述，但不应被误解为 canonical classification counts：

- `missing-pdf`
- `source-limited`
- `status-summary`
- `year-summary`
- `source-summary`
- `coverage-summary`

## 6. `paper_modules.csv` 的固定警告

`paper_modules.csv` 是 mixed-scope flat table。

它同时包含：

- canonical `scientific_object_modules`
- workflow mirror `final_modules_or_bucket`

因此：

- 它不是默认可直接聚合的 canonical-only 统计表
- 做正式分类统计时，应优先走 SQLite 的 `canonical_*` 视图
- 若必须使用 `paper_modules.csv`，必须先按 `assignment_scope` 过滤

## 7. 本轮固定结论

本轮之后，项目里的默认分析解释应收口为：

1. 默认分类统计 = canonical-only
2. `01.04` = 独立 bucket，不并入 formal `01-11`
3. formal module 分布 = assignment distribution，不等于 unique-paper distribution
4. unique-paper baseline 与 expanded assignment baseline 必须同时展示
5. workflow mirror 只在 audit / inspection 语境中出现
