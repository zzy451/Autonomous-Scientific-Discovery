# Mountain cross-sections: openness × verification × autonomy (3D)

**Classification:** content `01_three_axes` › form `mountain_3d`

## Caption
The proposal's three-way classification as a mountain cut along its right-hand axis. Each autonomy level (L0–L3, the axis with the fewest classes) is one translucent wall. On a wall, the horizontal axis is verification strength V0–V4 and the altitude is problem openness O1–O6. The wall's papers are smoothed into strata (darker bands mean 0.5, 2, 5, 10, 20, 40, 80 and 160 papers), and the ridge line is the highest openness actually reached at each verification strength. Peaks carry the paper count of their (O, V, L) cell, and the floor right of the dashed line is strong verification (V3–V4). The sheet repeats the cut for all papers and for each of the 11 fields.

## How it is generated
fig_ovl_mountain.py (matplotlib mplot3d; Gaussian smoothing σ = 0.36 class steps; monotone PCHIP ridge); every count is in derived/ovl_cube_counts.csv. Scripts: `fig_ovl_mountain.py` (run from `code/`).

## Versions

- `white/`: White background.
