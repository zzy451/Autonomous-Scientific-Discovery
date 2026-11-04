# One mountain through the 3D scatter: openness × verification × autonomy · white

**Classification:** content `01_three_axes` › form `mountain_surface_3d` › version `white`

White background.

## Files
- `fig_ovl_surface.pdf` (vector) and `fig_ovl_surface.png` (600 dpi)
- `fig_ovl_surface_cut.pdf` (vector) and `fig_ovl_surface_cut.png` (600 dpi)
- `fig_ovl_surface_quantiles.pdf` (vector) and `fig_ovl_surface_quantiles.png` (600 dpi)
- `fig_ovl_surface_fields.pdf` (vector) and `fig_ovl_surface_fields.png` (600 dpi)
- a copy of the generating script
- `ovl_cube_counts.csv`

## Caption
Every (V, L, O) combination is a point in the three-axis space: verification V0–V4 (front), autonomy L0–L3 (right) and problem openness O1–O6 (up). Point area is proportional to papers and colour gives the autonomy level. The mountain is the Gaussian-smooth surface through all the points, a paper-weighted Gaussian-kernel regression of openness over (V, L) (σ = 0.55 class steps along V and 0.22 along L, so each autonomy level keeps its own mean). The colour bar gives altitude, and L0, which has no papers, sits at 0. The line view draws the L0–L3 lines on the surface and labels each (V, L) column with its paper count, hollow dots marking 0. Because a mean surface hides the spread, the quantile view adds each level's 25–75% openness band and median. The floor right of the dashed line is strong verification (V3–V4).

## Regenerate
```bash
cd code && python3 fig_ovl_surface.py --all
```
