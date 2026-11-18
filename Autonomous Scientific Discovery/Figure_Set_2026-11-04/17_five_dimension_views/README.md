# One paper, five dimensions: openness O × verification V × autonomy L × time T × field C

Each core paper carries five coordinates. The four views place O, V, L and T on different visual channels; field C is faceting: every view is drawn once per field, here six fields (化学, 材料, 生命科学, 医学与健康, 形式与计算科学, 社会与知识系统). `OVL_Four_Views.pdf` collects all 24 figures with how to read each view. Strong verification = V3–V4 (red); a *blank* is an openness level with papers but no strong case, and a level with no papers is marked 无论文 instead.

| View | Where O, V, L and T go (C = one figure per field) | Script |
|---|---|---|
| `ridges/` | T = one row per year, O = horizontal axis, V = red fill for V3–V4, L = colour of the tick under each paper | `fig_ovl_modes.py` |
| `relief/` | O × V = oblique shaded relief of paper density, red coastline between V2 and V3, L = composition bars on the summit labels; no T | `fig_ovl_styles_C.py` |
| `parallel/` | T → O → V → L as four parallel axes, one path per paper, red = strong verification | `fig_ovl_styles_B.py` |
| `rings/` | O = one ring per level, V = red arc for strong, L = thin outer sub-ring, T = cumulative mini rings at 2019, 2023, 2026 | `fig_ovl_styles_D.py` |

Rebuild: `cd code && python3 build_ovl_views_report.py`.
