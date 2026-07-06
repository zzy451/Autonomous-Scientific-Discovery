# structured_data_catalog_round136_multimodule_chart_label_and_curve_refine_closeout_2026-07-06

## 本轮目标

继续沿用已经建立的多模块口径画图入口，按最新明确的展示要求修正两张基础图：

1. 不再显示 `01` 到 `11` 代码，统一改为一级类英文全称。
2. 将多模块年度折线图改为更圆润的曲线图。

## 本轮修改

### 1. 扩展 `scripts/generate_review_figures.py`

对多模块图相关逻辑做了以下调整：

- 新增 `numpy` 与 `scipy.interpolate.PchipInterpolator`
- 多模块年度图：
  - 保持统计口径不变，仍是 `paper_modules` 中 `scientific_object_modules` 的 expanded count
  - 从当前最早年份 `2004` 连到 `2026`
  - 使用 `PCHIP` 生成 shape-preserving 平滑曲线
  - 仍保留每个真实年份节点的圆点 marker，避免把平滑曲线误读成额外观测值
- 多模块柱状图：
  - 横轴标签由 `01`-`11` 改为一级类英文全称
  - 为了维持可读性，增加自动换行和更宽画布

### 2. 刷新图片输出

重新生成并保留以下多模块基础图：

- `Data/figures/review_charts/multimodule_year_trend_by_module.png`
- `Data/figures/review_charts/multimodule_module_counts_bar.png`

同时保留对应 CSV：

- `Data/figures/review_charts/multimodule_year_trend_by_module.csv`
- `Data/figures/review_charts/multimodule_module_counts_bar.csv`

由于一级类标签字典改为英文全称，现有若干基础图也同步刷新了显示文本：

- `formal_module_assignment_counts.png`
- `primary_filing_counts.png`
- `primary_filing_pdf_coverage.png`

## 验证

运行：

```powershell
python scripts/generate_review_figures.py
```

结果：

- 脚本执行成功
- 多模块曲线图与柱状图均已重新生成
- 抽查图片后确认：
  - 不再显示 `01`-`11`
  - 曲线图为圆润曲线并保留真实年份节点
  - 柱状图横轴为英文全称，当前可读

## owner / derived 边界

本轮没有修改四类 owner fact source：

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- `Data/discipline_code_assignments.jsonl`
- `Data/classification_code_index.json`

本轮变化全部属于 derived layer 或脚本层：

- `scripts/generate_review_figures.py`
- `Data/figures/review_charts/*`

## 结论

到本轮为止，当前多模块口径的两张基础图已经符合后续批量扩展的展示规范：

- 年度图：11 条英文全称曲线共图
- 总量图：11 个一级类英文全称柱状图

后续如果继续补同类型图，可以直接沿用这套颜色、标签、平滑和 CSV 导出逻辑。
