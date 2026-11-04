# One mountain, four autonomy cuts: openness × verification × autonomy (3D)

**Classification:** content `01_three_axes` › form `mountain_surface_3d`

## Caption
The proposal's three-way classification as one continuous mountain. The surface spans verification V0–V4 (front) × autonomy L0–L3 (right); its altitude is problem openness, the highest O1–O6 actually reached at each (V, L), joined by shape-preserving PCHIP interpolation so it never overshoots the data. Surface colour is the Gaussian-smoothed paper density. Four coloured planes cut the mountain along the right-hand axis at L0–L3; each cut is that level's ridge, and the number where a cut meets a verification class is the paper count of that (V, L) combination. The floor right of the dashed line is strong verification (V3–V4). The sheet repeats the mountain for all papers and each field.

## How it is generated
fig_ovl_surface.py (matplotlib mplot3d; scipy PCHIP on the (V, L) lattice; density σ = 0.4 class steps); every count is in derived/ovl_cube_counts.csv. Scripts: `fig_ovl_surface.py` (run from `code/`).

## Versions

- `white/`: White background.
