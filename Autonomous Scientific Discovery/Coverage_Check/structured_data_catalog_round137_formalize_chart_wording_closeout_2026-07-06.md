# structured_data_catalog_round137_formalize_chart_wording_closeout_2026-07-06

## 本轮目标

在不改变多模块统计口径、不改变图形结构的前提下，进一步把当前两张核心图的标题、坐标轴标题与图例标题改成更适合直接放入综述正文的正式书面表达。

## 本轮修改

### 1. 收紧 `scripts/generate_review_figures.py` 的图面文案

本轮主要修改多模块口径的两张核心图：

- `multimodule_year_trend_by_module.png`
- `multimodule_module_counts_bar.png`

具体调整如下：

#### 多模块年度曲线图

- 图标题由较工具化的：
  - `Multi-Module Formal Module Year Trend`
- 改为更正文式的：
  - `Annual Distribution of Included Agent Publications Across Primary Scientific Domains`

- 横轴标题由：
  - `Year`
- 改为：
  - `Publication Year`

- 纵轴标题由：
  - `Expanded paper count`
- 改为：
  - `Number of Publications (Multi-Domain Counting)`

- 图例标题由：
  - `Primary-level class`
- 改为：
  - `Primary Scientific Domain`

#### 多模块柱状图

- 图标题由：
  - `Multi-Module Formal Module Counts`
- 改为：
  - `Distribution of Included Agent Publications Across Primary Scientific Domains`

- 横轴标题由：
  - `Primary-level class`
- 改为：
  - `Primary Scientific Domain`

- 纵轴标题由：
  - `Expanded paper count`
- 改为：
  - `Number of Publications (Multi-Domain Counting)`

### 2. 刷新图片输出

重新运行：

```powershell
python scripts/generate_review_figures.py
```

刷新后的图片仍输出到：

- `Data/figures/review_charts/multimodule_year_trend_by_module.png`
- `Data/figures/review_charts/multimodule_module_counts_bar.png`

## 验证

本轮验证结论：

- 脚本执行成功
- 两张核心图均已重新生成
- 抽查后确认标题、坐标轴和图例已改为更正式的论文式表述
- 统计口径未变化，仍为多模块展开计数

## owner / derived 边界

本轮没有修改四类 owner fact source：

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- `Data/discipline_code_assignments.jsonl`
- `Data/classification_code_index.json`

本轮仅修改：

- `scripts/generate_review_figures.py`
- `Data/figures/review_charts/*`

## 结论

到本轮为止，当前两张多模块基础图不仅在统计口径和视觉结构上稳定，而且在图题、坐标轴和图例层面也已经更接近综述正文可直接使用的书面化表达。
