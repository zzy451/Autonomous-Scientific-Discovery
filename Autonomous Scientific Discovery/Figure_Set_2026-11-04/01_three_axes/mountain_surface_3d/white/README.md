# One mountain, four autonomy cuts: openness × verification × autonomy (3D) · white

**Classification:** content `01_three_axes` › form `mountain_surface_3d` › version `white`

White background.

## Files
- `fig_ovl_surface.pdf` (vector) and `fig_ovl_surface.png` (600 dpi)
- `fig_ovl_surface_fields.pdf` (vector) and `fig_ovl_surface_fields.png` (600 dpi)
- a copy of the generating script
- `ovl_cube_counts.csv`

## Caption
The proposal's three-way classification as one continuous mountain. The surface spans verification V0–V4 (front) × autonomy L0–L3 (right); its altitude is problem openness, the highest O1–O6 actually reached at each (V, L), joined by shape-preserving PCHIP interpolation so it never overshoots the data. Surface colour is the Gaussian-smoothed paper density. Four coloured planes cut the mountain along the right-hand axis at L0–L3; each cut is that level's ridge, and the number where a cut meets a verification class is the paper count of that (V, L) combination. The floor right of the dashed line is strong verification (V3–V4). The sheet repeats the mountain for all papers and each field.

## Regenerate
```bash
cd code && python3 fig_ovl_surface.py --all
```
