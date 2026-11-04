# Mountain cross-sections: openness × verification × autonomy (3D) · white

**Classification:** content `01_three_axes` › form `mountain_3d` › version `white`

White background.

## Files
- `fig_ovl_mountain.pdf` (vector) and `fig_ovl_mountain.png` (600 dpi)
- `fig_ovl_mountain_fields.pdf` (vector) and `fig_ovl_mountain_fields.png` (600 dpi)
- a copy of the generating script
- `ovl_cube_counts.csv`

## Caption
The proposal's three-way classification as a mountain cut along its right-hand axis. Each autonomy level (L0–L3, the axis with the fewest classes) is one translucent wall. On a wall, the horizontal axis is verification strength V0–V4 and the altitude is problem openness O1–O6. The wall's papers are smoothed into strata (darker bands mean 0.5, 2, 5, 10, 20, 40, 80 and 160 papers), and the ridge line is the highest openness actually reached at each verification strength. Peaks carry the paper count of their (O, V, L) cell, and the floor right of the dashed line is strong verification (V3–V4). The sheet repeats the cut for all papers and for each of the 11 fields.

## Regenerate
```bash
cd code && python3 fig_ovl_mountain.py --all
```
