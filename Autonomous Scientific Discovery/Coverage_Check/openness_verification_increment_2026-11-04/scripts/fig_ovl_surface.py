"""The proposal's three-way classification as one continuous mountain, cut by four autonomy planes.

The mountain is a single surface over the base plane verification V0-V4 (front) x autonomy L0-L3 (right).
Its altitude is problem openness: at each (V, L) the highest openness O1-O6 actually reached, joined by a
shape-preserving (PCHIP) interpolation so it never overshoots the data; colour on the surface is the
Gaussian-smoothed paper density. Four coloured planes cut the mountain along the right-hand axis at L0-L3;
where a cut meets a verification class the paper count of that (V, L) column is printed.
Data: ov_coding/increment/classification_results_662.jsonl. White background only.

  fig_ovl_surface          : all 662 papers
  fig_ovl_surface_fNN      : one per field 01-11 (a cross-field paper counts in every field it has)
  fig_ovl_surface_fields   : all papers plus the 11 fields as small multiples
  derived/ovl_cube_counts.csv : every (O, V, L) count, all papers and each field
Usage: python3 fig_ovl_surface.py [--all]
"""
import sys, json, collections as C
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, LightSource, to_rgb
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.interpolate import RegularGridInterpolator
from scipy.ndimage import gaussian_filter
import style as S

INC = S.ROOT / "ov_coding" / "increment" / "classification_results_662.jsonl"
INK, MUTED, ACC = "#1d1d1b", "#6b665c", "#b2412f"
O_TICK = ["O1 规则世界", "O2 既定基准", "O3 新实例", "O4 需物理检验", "O5 开放数学", "O6 开放科学"]
V_TICK = ["V0 声明", "V1 基准", "V2 计算/仿真", "V3 物理实验", "V4 证明/复现"]
L_NAME = ["L0 工具", "L1 任务助手", "L2 闭环执行者", "L3 自主研究者"]
L_COL = ["#8e8a82", "#3f7fa0", "#d6903f", "#c4472f"]
FZH = {"01": "形式与计算科学", "02": "物理与天文", "03": "化学", "04": "材料", "05": "地球与环境", "06": "生命科学",
       "07": "医学与健康", "08": "农业与食品", "09": "工程与工业", "10": "航空航天、海洋与交通", "11": "社会与知识系统"}
BASE = 0.4                                                  # altitude of the plain (below O1)
VX, LY = (-1.0, 5.0), (-1.0, 4.0)
RES = 24                                                    # surface samples per class step
DENS = LinearSegmentedColormap.from_list("d", ["#f7f4ee", "#e6dccb", "#c9b79a", "#9c8463", "#5e4b34"])
plt.rcParams.update({"font.family": ["Arial Unicode MS", "Arial"], "font.size": 9})


def load():
    rows = [json.loads(l) for l in open(INC, encoding="utf-8")]
    return [(int(r["openness"][1]), int(r["verification"][1]), int(r["autonomy"][1]), r["paper_id"])
            for r in rows if r["coded"]]


def surface(pts):
    """Altitude (highest O reached) and paper count on the (V, L) lattice, then the continuous surface."""
    hi, n = C.defaultdict(lambda: BASE), C.Counter()
    for o, v, L, _ in pts:
        hi[(v, L)] = max(hi[(v, L)], o); n[(v, L)] += 1
    lv, ll = np.arange(-1, 6), np.arange(-1, 5)                     # one class of plain around the data
    Z = np.array([[hi[(v, L)] for L in ll] for v in lv], float)
    gv = np.linspace(*VX, int((VX[1] - VX[0]) * RES) + 1)
    gl = np.linspace(*LY, int((LY[1] - LY[0]) * RES) + 1)
    VV, LL = np.meshgrid(gv, gl, indexing="ij")
    zz = RegularGridInterpolator((lv, ll), Z, method="pchip")(np.stack([VV, LL], -1))
    D = np.zeros_like(VV)
    for (v, L), c in n.items():
        D[np.abs(gv - v).argmin(), np.abs(gl - L).argmin()] += c
    s = 0.4 * RES
    D = gaussian_filter(D, s, mode="constant") * 2 * np.pi * s * s          # peak ~ papers in the column
    return VV, LL, zz, D, hi, n, RegularGridInterpolator((lv, ll), Z, method="pchip")


def surface_axes(ax, pts, small=False):
    VV, LL, zz, D, hi, n, f = surface(pts)
    top = max(n.values())
    w = np.sqrt(np.clip(D, 0, None) / top)
    ls = LightSource(azdeg=300, altdeg=35)
    rgb = DENS(np.clip(w, 0, 1))[:, :, :3]
    rgb = ls.shade_rgb(rgb, zz * 3, blend_mode="soft", fraction=0.8)
    fc = np.dstack([rgb, np.full(zz.shape, 0.78)])
    ax.plot_surface(VV, LL, zz, facecolors=fc, rstride=2, cstride=2, linewidth=0, antialiased=True, shade=False,
                    zorder=1)
    gv = VV[:, 0]
    for L in (3, 2, 1, 0):                                          # far cut first
        col = to_rgb(L_COL[L])
        z = f(np.stack([gv, np.full_like(gv, L)], -1))
        nL = sum(c for (v, l), c in n.items() if l == L)
        # the cutting plane, and the mountain's section on it
        ax.add_collection3d(Poly3DCollection([[(VX[0], L, BASE), (VX[1], L, BASE), (VX[1], L, 6.8), (VX[0], L, 6.8)]],
                                             facecolor=(*col, 0.05), edgecolor=(*col, 0.5), linewidth=0.5), zs=None)
        sec = list(zip(gv, [L] * len(gv), z)) + [(gv[-1], L, BASE), (gv[0], L, BASE)]
        ax.add_collection3d(Poly3DCollection([sec], facecolor=(*col, 0.2), edgecolor="none"), zs=None)
        ax.plot(gv, [L] * len(gv), z, color=L_COL[L], lw=1.2 if small else 2.4, zorder=6)
        # numbers where the cut meets each verification class
        for v in range(5):
            c = n.get((v, L), 0)
            if not c:
                continue
            zt = hi[(v, L)]
            ax.scatter([v], [L], [zt], s=5 if small else 16, c=L_COL[L], edgecolors="white", linewidths=0.7,
                       depthshade=False, zorder=20)
            ax.text(v, L, zt + (0.28 if small else 0.32), str(c), fontsize=5.5 if small else 8.5, color=INK,
                    ha="center", fontweight="bold", zorder=21)
    # strong-verification zone on the plain
    ax.plot([2.5, 2.5], [LY[0], LY[1]], [BASE, BASE], color=ACC, lw=0.7, ls="--", zorder=2)
    if not small:
        ax.text(3.75, LY[1], BASE, "强验证区 V3–V4", fontsize=7.5, color=ACC, ha="center", zorder=30)
    fs = 5.2 if small else 8
    ax.set_xticks(range(5), [f"V{k}" for k in range(5)] if small else V_TICK, fontsize=fs)
    ax.set_yticks(range(4), [f"L{k}" for k in range(4)], fontsize=fs)
    ax.set_zticks(range(1, 7), [f"O{k}" for k in range(1, 7)] if small else O_TICK, fontsize=fs)
    ax.set_xlim(*VX); ax.set_ylim(*LY); ax.set_zlim(BASE, 7.2)
    ax.tick_params(pad=-2 if small else 1)
    for a in (ax.xaxis, ax.yaxis, ax.zaxis):
        a.pane.set_facecolor((0.99, 0.988, 0.982, 1)); a.pane.set_edgecolor("#e4dfd6")
        a._axinfo["grid"].update(color="#ece8e1", linewidth=0.4)
    ax.set_box_aspect((1.45, 1.2, 0.95))
    ax.view_init(elev=24, azim=-57)


FOOT = ("山体 = (V, L) 平面上的连续曲面：海拔为该处实际达到的最高问题开放度 O，用保形插值（PCHIP）连续化，不超出数据；"
        "山体颜色由浅到深 = 平滑后的论文密度。\n四个颜色平面沿右轴在 L0–L3 处切开山体，切线即该自主性等级的山脊；"
        "交点数字 = 该 (V, L) 组合的论文数；红色虚线以右为强验证（V3–V4）· 快照 2026-11-01")


def figure(pts, name, title, sub):
    fig = plt.figure(figsize=(10.5, 8.6), facecolor="white")
    ax = fig.add_axes([0.0, 0.07, 1.0, 0.84], projection="3d", computed_zorder=False)
    surface_axes(ax, pts)
    ax.set_xlabel("验证强度 V", labelpad=14); ax.set_ylabel("系统自主性 L", labelpad=8)
    ax.set_zlabel("问题开放度 O（海拔）", labelpad=18)
    n_s = sum(v >= 3 for _, v, _, _ in pts)
    fig.text(0.06, 0.955, title, fontsize=16, fontweight="bold", color=INK)
    fig.text(0.06, 0.925, f"{sub}　·　{len(pts)} 篇，强验证（V3–V4）{n_s} 篇（{100 * n_s / len(pts):.0f}%）",
             fontsize=9, color=MUTED)
    fig.text(0.06, 0.02, FOOT, fontsize=7.2, color=MUTED, linespacing=1.6)
    for k, L in enumerate((3, 2, 1, 0)):
        nL = sum(L == l for _, _, l, _ in pts)
        st = sum(L == l and v >= 3 for _, v, l, _ in pts)
        fig.text(0.06, 0.885 - 0.024 * k, f"■ {L_NAME[L]}　{nL} 篇" + (f"　强验证 {100 * st / nL:.0f}%" if nL else ""),
                 fontsize=8.5, color=L_COL[L], fontweight="bold")
    S.save(fig, name); plt.close(fig)


def fields_sheet(pts, fields):
    fig = plt.figure(figsize=(13.5, 10.8), facecolor="white")
    sets = [("全部", pts)] + [(FZH[f], [p for p in pts if f in fields[p[3]]]) for f in S.FIELDS]
    for i, (lab, sub) in enumerate(sets):
        ax = fig.add_subplot(3, 4, i + 1, projection="3d", computed_zorder=False)
        surface_axes(ax, sub, small=True)
        ns = sum(v >= 3 for _, v, _, _ in sub)
        ax.set_title(f"{lab}　n = {len(sub)}　强验证 {100 * ns / len(sub):.0f}%", fontsize=8.5, color=INK,
                     fontweight="bold", pad=-12)
    fig.subplots_adjust(left=0.0, right=1.0, top=0.9, bottom=0.05, wspace=0.0, hspace=0.06)
    fig.text(0.03, 0.955, "问题开放度 × 验证强度 × 系统自主性：按学科的山体", fontsize=15, fontweight="bold", color=INK)
    fig.text(0.03, 0.928, "山体海拔 = 各 (V, L) 实际达到的最高开放度 O；颜色深浅 = 论文密度；四个颜色平面在 L0–L3 处切开山体，"
             "交点数字为该 (V, L) 组合的论文数；跨学科论文在每个所属学科各计一次。", fontsize=9, color=MUTED)
    fig.text(0.03, 0.02, f"{len(pts)} 篇核心论文，{sum(len(s) for _, s in sets[1:])} 个论文—学科归属 · 快照 2026-11-01",
             fontsize=8, color=MUTED)
    for k, L in enumerate((0, 1, 2, 3)):
        fig.text(0.62 + 0.09 * k, 0.02, f"■ {L_NAME[L]}", fontsize=8.5, color=L_COL[L], fontweight="bold")
    S.save(fig, "fig_ovl_surface_fields"); plt.close(fig)


def write_counts(pts, fields):
    """derived/ovl_cube_counts.csv: papers in every (O, V, L) cell, for all papers and each field (zeros kept)."""
    import csv
    with open(S.DER / "ovl_cube_counts.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["scope", "field_code", "field_name", "openness", "verification", "autonomy", "papers"])
        scopes = [("all", "", "全部", pts)] + [("field", f, FZH[f], [p for p in pts if f in fields[p[3]]])
                                               for f in S.FIELDS]
        for sc, code, nm, sub in scopes:
            cnt = C.Counter((o, v, L) for o, v, L, _ in sub)
            for o in range(1, 7):
                for v in range(5):
                    for L in range(4):
                        w.writerow([sc, code, nm, f"O{o}", f"V{v}", f"L{L}", cnt.get((o, v, L), 0)])


if __name__ == "__main__":
    pts = load()
    figure(pts, "fig_ovl_surface", "问题开放度 × 验证强度 × 系统自主性", "全部核心论文")
    if "--all" in sys.argv:
        fields = {c["paper_id"]: set(c["fields"]) for c in S.papercards()}
        for f in S.FIELDS:
            sub = [p for p in pts if f in fields[p[3]]]
            figure(sub, f"fig_ovl_surface_f{f}", f"{FZH[f]}：开放度 × 验证强度 × 自主性", f"学科 {f} {FZH[f]}")
        fields_sheet(pts, fields)
        write_counts(pts, fields)
