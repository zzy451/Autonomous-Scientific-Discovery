# structured_data_catalog_round138_source_category_charts_closeout_2026-07-06

## 本轮目标

把 447 篇已收录文献的 `source` 字段正式压缩为 10 个稳定的来源展示类，并直接复用现有画图脚本生成两张可用于后续综述展示的基础图：

1. 来源类别年度曲线图
2. 来源类别总量柱状图

## 本轮修改

### 1. 在 `scripts/generate_review_figures.py` 中固化 10 类来源分类规则

新增来源展示层分类：

- `arXiv-Linked Preprints`
- `Other Preprint Servers`
- `Nature Portfolio`
- `Science Family`
- `Cell Press`
- `ACS and Chemistry Journals`
- `Materials and Advanced Science Journals`
- `AI/ML Conferences and Workshops`
- `IEEE, Robotics, and Aerospace Venues`
- `Other Journals and Venues`

新增 `categorize_source(source)` 规则，把当前 `papers.source` 映射到上述 10 类。

特别说明：

- `arXiv`, `arXiv / ...`, `... / arXiv` 一律并入 `arXiv-Linked Preprints`
- `bioRxiv`, `medRxiv`, `ChemRxiv`, `Research Square`, `Preprints.org`, `SSRN` 并入 `Other Preprint Servers`
- 最后一条边界修正后，`Photonic and Phononic Properties of Engineered Nanostructures XVI` 被并入 `Other Journals and Venues`，从而与当前冻结的展示口径完全一致

### 2. 新增两张来源结构图

新增导出：

- `Data/figures/review_charts/source_category_year_trend.png`
- `Data/figures/review_charts/source_category_counts_bar.png`

以及对应 CSV：

- `Data/figures/review_charts/source_category_year_trend.csv`
- `Data/figures/review_charts/source_category_counts_bar.csv`

图的口径说明：

- 统计对象：`active_confirmed_core = 1` 的 447 篇已收录文献
- 统计层级：paper-level，不做多模块展开
- 年度图：按文献 `year` 和来源类别计数，使用平滑曲线并保留真实年份数据点
- 柱状图：按 10 个来源类别汇总总量

## 验证

运行：

```powershell
python scripts/generate_review_figures.py
```

校验结果：

- 脚本执行成功
- 新图和 CSV 均已生成
- `source_category_counts_bar.csv` 当前计数为：
  - `arXiv-Linked Preprints` = 234
  - `Other Preprint Servers` = 30
  - `Nature Portfolio` = 68
  - `Science Family` = 21
  - `Cell Press` = 6
  - `ACS and Chemistry Journals` = 23
  - `Materials and Advanced Science Journals` = 17
  - `AI/ML Conferences and Workshops` = 16
  - `IEEE, Robotics, and Aerospace Venues` = 19
  - `Other Journals and Venues` = 13

上述 10 类总和为 `447`，与当前已收录文献总数一致。

## owner / derived 边界

本轮没有修改四类 owner fact source：

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- `Data/discipline_code_assignments.jsonl`
- `Data/classification_code_index.json`

本轮变化全部位于：

- `scripts/generate_review_figures.py`
- `Data/figures/review_charts/*`

## 结论

到本轮为止，来源结构已经不再依赖碎片化的 107 个原始 `source` 值，而是被稳定压缩为 10 个适合正文图展示的来源类别，并且已经有现成的年度曲线图和总量柱状图可直接复用。
