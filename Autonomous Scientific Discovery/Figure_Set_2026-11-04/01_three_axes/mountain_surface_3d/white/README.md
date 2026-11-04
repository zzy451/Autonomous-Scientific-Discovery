# One mountain through the 3D scatter: openness × verification × autonomy · white

**Classification:** content `01_three_axes` › form `mountain_surface_3d` › version `white`

White background.

## Files
- `fig_ovl_surface.pdf` (vector) and `fig_ovl_surface.png` (600 dpi)
- `fig_ovl_surface_cut.pdf` (vector) and `fig_ovl_surface_cut.png` (600 dpi)
- `fig_ovl_surface_fields.pdf` (vector) and `fig_ovl_surface_fields.png` (600 dpi)
- a copy of the generating script
- `ovl_cube_counts.csv`

## Caption
Every (V, L, O) combination is a point in the three-axis space: verification V0–V4 (front), autonomy L0–L3 (right) and problem openness O1–O6 (up). Point area is proportional to papers and colour gives the autonomy level. The mountain is the Gaussian-smooth surface through all the points, a paper-weighted Gaussian-kernel regression of openness over (V, L) (σ = 0.55 class steps) that settles onto the plain far from the data. Dotted stems show each point's offset from the surface, and white contours mark O1–O6. The cut view slices the same surface with four coloured planes at L0–L3 along the right-hand axis. The number where a cut meets a verification class is that (V, L) column's paper count. The floor right of the dashed line is strong verification (V3–V4).

## Regenerate
```bash
cd code && python3 fig_ovl_surface.py --all
```
