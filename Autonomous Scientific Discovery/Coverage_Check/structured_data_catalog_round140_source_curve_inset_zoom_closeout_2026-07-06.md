# structured_data_catalog_round140_source_curve_inset_zoom_closeout_2026-07-06

## 本轮目标

把来源分类年度图从“断轴压缩”改成更接近示例图的“主图 + 局部放大 inset”形式，并明确保持：

- 主图仍为平滑曲线
- 放大图也为平滑曲线
- 不改成折线

## 本轮修改

### 1. 恢复并重建 `scripts/generate_review_figures.py`

当前本地 `scripts/` 目录中已经没有 `generate_review_figures.py`，因此本轮先把画图脚本重新补回到：

- `scripts/generate_review_figures.py`

脚本当前至少覆盖以下来源分类图导出：

- `source_category_year_trend.png`
- `source_category_counts_bar.png`

### 2. 把来源分类年度图改成局部放大 inset

`source_category_year_trend.png` 不再使用断轴压缩，而是改为：

- 左侧主图：保留所有 10 个来源类别的全尺度平滑曲线
- 右侧 inset：局部放大 `0-25` 区间
- inset 中移除主导性的 `arXiv-Linked Preprints`，专门比较其余小类别

图面新增说明：

- 主图标题：`Full scale: all categories`
- inset 标题：`Zoomed comparison of smaller categories (Excludes arXiv-Linked Preprints)`
- 主图虚线：标出 `0-25` 的放大范围
- 底部注释：说明 inset 只是放大比较，原始数据未改

### 3. 保持平滑曲线

主图和 inset 都继续使用 `PchipInterpolator` 生成平滑曲线，并保留真实年份节点 marker。

因此本轮明确避免了：

- 将曲线退回为折线
- 用断轴造成视觉上的“截断”感

## 验证

运行：

```powershell
python scripts/generate_review_figures.py
```

结果：

- 脚本执行成功
- `Data/figures/review_charts/source_category_year_trend.png` 已刷新
- 抽查后确认当前图片为“主图 + 局部放大 inset”的平滑曲线版本

## owner / derived 边界

本轮未修改任何 owner fact source。

本轮改动仅涉及：

- `scripts/generate_review_figures.py`
- `Data/figures/review_charts/source_category_year_trend.png`

## 结论

到本轮为止，本地来源分类年度图已经不再是断轴图，而是按示例风格改成了更适合正文展示的局部放大平滑曲线图。
