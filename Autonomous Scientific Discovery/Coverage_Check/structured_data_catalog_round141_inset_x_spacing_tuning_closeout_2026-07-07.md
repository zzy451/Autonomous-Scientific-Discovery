# structured_data_catalog_round141_inset_x_spacing_tuning_closeout_2026-07-07

## 本轮目标

继续优化来源分类年度曲线图右侧 inset 的可读性，在不改变数据、不改成折线的前提下，让局部放大面板的横轴显得不那么拥挤。

## 本轮修改

针对：

- `Data/figures/review_charts/source_category_year_trend.png`

做了两项局部版式调整：

### 1. 加宽右侧 inset 面板

把右侧放大面板的横向宽度进一步增大，同时略微压缩左侧主图宽度，使 inset 内部的年份点横向间距更大。

### 2. 降低 inset 横轴标签密度

在 inset 中把年份刻度改为隔年显示，而不是每年都标注：

- 原来：`2004, 2005, 2006, ... 2026`
- 现在：`2004, 2006, 2008, ... 2026`

这样做不会影响曲线本身的完整性，只是减少文字标签密度。

## 保持不变的部分

本轮明确保持不变：

- 仍然是“主图 + 局部放大 inset”结构
- 主图和 inset 都仍然使用平滑曲线
- 不改成折线
- 统计口径不变，仍是 10 类来源分类

## 验证

运行：

```powershell
python scripts/generate_review_figures.py
```

结果：

- 脚本执行成功
- `source_category_year_trend.png` 已刷新
- 右侧 inset 横轴明显比上一版更疏朗

## owner / derived 边界

本轮未修改任何 owner fact source。

本轮仅涉及：

- `scripts/generate_review_figures.py`
- `Data/figures/review_charts/source_category_year_trend.png`

## 结论

到本轮为止，来源分类年度图的局部放大面板已经在不牺牲平滑曲线和完整年份范围的前提下，进一步改善了横轴拥挤问题。
