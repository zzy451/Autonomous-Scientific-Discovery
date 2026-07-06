# structured_data_catalog_round135_review_chart_generation_closeout_2026-07-06

## 本轮目标

在不改动四类 owner fact source 的前提下，基于当前已经冻结的结构化 SQLite 输出，建立一套可重复运行的基础画图入口，并先生成一组综述写作与汇报最常用的折线图 / 柱状图。

## 本轮修改

### 1. 新增 `scripts/generate_review_figures.py`

新增独立画图脚本：

- 输入：`Data/papers.sqlite`
- 输出目录：`Data/figures/review_charts/`
- 当前首批导出图：
  - `year_trend_records.png`
  - `formal_module_assignment_counts.png`
  - `primary_filing_counts.png`
  - `primary_filing_pdf_coverage.png`
- 同时导出对应 CSV：
  - `year_trend_records.csv`
  - `formal_module_assignment_counts.csv`
  - `primary_filing_counts.csv`
  - `primary_filing_pdf_coverage.csv`

脚本当前遵守的口径：

- 年度趋势图：
  - 使用 `papers` 表
  - 同时画 `all records` 与 `active_confirmed_core`
- formal module 分布图：
  - 使用 `paper_modules`
  - 口径为 `scientific_object_modules` 展开后的 canonical formal-module assignment count
- primary filing 分布图：
  - 使用 `papers.primary_module_for_filing`
  - 口径为每篇论文唯一主排架位
- PDF 覆盖图：
  - 使用 `papers.pdf_exists + primary_module_for_filing`
  - 口径为唯一主排架位下的本地 PDF 覆盖

### 2. 修正 11 大类图的可读性

初版纵向柱状图在 11 个长标签场景下可读性一般，因此本轮直接把 3 张模块相关图改成横向条形图：

- `formal_module_assignment_counts.png`
- `primary_filing_counts.png`
- `primary_filing_pdf_coverage.png`

这样后续放入正文、PPT 或汇报文档时更稳定，不需要再手工调整坐标轴标签。

## 验证

运行：

```powershell
python scripts/generate_review_figures.py
```

结果：

- 脚本执行成功
- `Data/figures/review_charts/` 已生成 4 张 PNG 与 4 个对应 CSV
- 抽查图片后，当前横向条形图版式可读

## owner / derived 边界

本轮没有修改以下 owner fact source：

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- `Data/discipline_code_assignments.jsonl`
- `Data/classification_code_index.json`

本轮新增内容全部属于 derived layer：

- `scripts/generate_review_figures.py`
- `Data/figures/review_charts/*`

## 结论

到本轮为止，仓库已经具备“从当前结构化分析库直接批量生成基础折线图 / 柱状图”的能力。后续如果要继续补图，可以在这个脚本上继续增加：

- 二级类分布图
- 年份 x 模块趋势图
- source-limited / PDF coverage 对比图
- 单模块口径 vs 多模块口径对照图
