"""The proposal's three-way classification as a mountain cross-section (white background only).

Each autonomy level L0-L3 (the right-hand axis, fewest classes) is one translucent wall, a cut through the
mountain. On a wall, the horizontal axis is verification strength V0-V4 and the vertical axis (altitude) is
problem openness O1-O6. The wall's paper counts are smoothed into a density, drawn as strata (darker = more
papers); the ridge line is the highest openness actually reached at each verification strength. Peaks carry the
paper count of their (O, V, L) cell. Data: ov_coding/increment/classification_results_662.jsonl.

  fig_ovl_mountain          : all 662 papers
  fig_ovl_mountain_fNN      : one per field 01-11 (a cross-field paper counts in every field it has)
  fig_ovl_mountain_fields   : all papers plus the 11 fields as small multiples
  derived/ovl_cube_counts.csv : every (O, V, L) count, all papers and each field
Usage: python3 fig_ovl_mountain.py --all
"""
import json, collections as C
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_rgb
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.ndimage import gaussian_filter
from scipy.interpolate import PchipInterpolator
import style as S

INC = S.ROOT / "ov_coding" / "increment" / "classification_results_662.jsonl"
INK, MUTED, ACC = "#1d1d1b", "#6b665c", "#b2412f"
O_TICK = ["O1 规则世界", "O2 既定基准", "O3 新实例", "O4 需物理检验", "O5 开放数学", "O6 开放科学"]
V_TICK = ["V0 声明", "V1 基准", "V2 计算/仿真", "V3 物理实验", "V4 证明/复现"]
L_NAME = ["L0 工具", "L1 任务助手", "L2 闭环执行者", "L3 自主研究者"]
L_COL = ["#9a958c", "#4f86a3", "#d39a5c", "#c4553f"]        # as the reference: teal -> sand -> coral
FZH = {"01": "形式与计算科学", "02": "物理与天文", "03": "化学", "04": "材料", "05": "地球与环境", "06": "生命科学",
       "07": "医学与健康", "08": "农业与食品", "09": "工程与工业", "10": "航空航天、海洋与交通", "11": "社会与知识系统"}
VX, OZ = (-0.9, 4.9), (0.5, 6.7)                           # wall extent: verification (x) and openness (z)
RES, SIG = 16, 0.36                                         # grid cells per class step; smoothing (class steps)
LEVELS = [0.5, 2, 5, 10, 20, 40, 80, 160, 320]              # strata, in papers
plt.rcParams.update({"font.family": ["Arial Unicode MS", "Arial"], "font.size": 9})


def load():
    rows = [json.loads(l) for l in open(INC, encoding="utf-8")]
    return [(int(r["openness"][1]), int(r["verification"][1]), int(r["autonomy"][1]), r["paper_id"])
            for r in rows if r["coded"]]


def wall_density(cnt):
    """Smoothed counts over (V, O) for one wall, scaled so a cell of n papers peaks at about n."""
    gv = np.linspace(*VX, int((VX[1] - VX[0]) * RES) + 1)
    go = np.linspace(*OZ, int((OZ[1] - OZ[0]) * RES) + 1)
    f = np.zeros((len(gv), len(go)))
    for (v, o), n in cnt.items():
        f[np.abs(gv - v).argmin(), np.abs(go - o).argmin()] += n
    s = SIG * RES
    return gv, go, gaussian_filter(f, s, mode="constant") * 2 * np.pi * s * s


def ridge(cnt, gv):
    """The ridge: the highest openness actually reached at each verification class, joined by a monotone
    (non-overshooting) curve; columns with no papers drop to the base."""
    hi = {}
    for (v, o) in cnt:
        hi[v] = max(hi.get(v, 0), o)
    v0, v1 = min(hi), max(hi)
    xs = [v0 - 0.85] + list(range(v0, v1 + 1)) + [v1 + 0.85]
    zs = [OZ[0]] + [hi.get(v, OZ[0]) for v in range(v0, v1 + 1)] + [OZ[0]]
    top = PchipInterpolator(xs, zs)(np.clip(gv, xs[0], xs[-1]))
    top[(gv < xs[0]) | (gv > xs[-1])] = OZ[0]
    return top


def mountain_axes(ax, pts, small=False):
    lay = {L: C.Counter((v, o) for o, v, l, _ in pts if l == L) for L in range(4)}
    for L in (3, 2, 1, 0):                                  # far wall first
        col = np.array(to_rgb(L_COL[L]))
        n = sum(lay[L].values())
        # wall frame
        ax.plot([VX[0], VX[1], VX[1], VX[0], VX[0]], [L] * 5, [OZ[0], OZ[0], OZ[1], OZ[1], OZ[0]],
                color=L_COL[L], lw=0.5, alpha=0.5, ls="-" if n else "--", zorder=1)
        lab = f"{L_NAME[L]} · {n} 篇" if small else (f"{L_NAME[L]} · {n} 篇 · 强验证 "
                                                     f"{100 * sum(c for (v, _), c in lay[L].items() if v >= 3) / n:.0f}%"
                                                     if n else f"{L_NAME[L]} · 0 篇")
        ax.text(VX[0], L, OZ[1] + 0.25, lab, fontsize=5.5 if small else 8.5, color=L_COL[L], fontweight="bold",
                ha="left", zorder=30)
        if not n:
            continue
        gv, go, f = wall_density(lay[L])
        top = ridge(lay[L], gv)
        f = np.where(go[None, :] <= top[:, None] + 0.12, f, 0)          # strata stay inside the mountain
        ok = top > OZ[0] + 0.01
        # mountain body: translucent fill under the ridge
        xs, zs = gv[ok], np.maximum(top[ok], OZ[0])
        body = [list(zip(xs, [L] * len(xs), zs)) + [(xs[-1], L, OZ[0]), (xs[0], L, OZ[0])]]
        ax.add_collection3d(Poly3DCollection(body, facecolor=(*col, 0.16), edgecolor="none"), zs=None)
        # strata: filled density contours on the wall plane
        cm = LinearSegmentedColormap.from_list(f"w{L}", [(*col * 0.25 + 0.75, 0.25), (*col, 0.6), (*col * 0.55, 0.92)])
        lv = [x for x in LEVELS if x <= f.max()] + [f.max() + 1]
        VV, OO = np.meshgrid(gv, go, indexing="ij")
        if len(lv) >= 2:
            ax.contourf(VV, f, OO, levels=lv, zdir="y", offset=L, cmap=cm, zorder=3)
            ax.contour(VV, f, OO, levels=lv[:-1], zdir="y", offset=L, colors="white", linewidths=0.35, zorder=4)
        # ridge line
        ax.plot(xs, [L] * len(xs), zs, color=L_COL[L], lw=1.0 if small else 2.0, zorder=5)
        # peaks
        for (v, o), c in lay[L].most_common(2 if small else 3):
            if c < (6 if small else 5):
                continue
            ax.scatter([v], [L], [o], s=6 if small else 14, c="white", edgecolors=INK, linewidths=0.6,
                       depthshade=False, zorder=20)
            dz, ha = (-0.5, "center") if L == 1 else (0.22, "left" if L == 3 else "center")   # keep walls apart
            ax.text(v, L, o + dz, str(c), fontsize=5.5 if small else 8.5, color=INK, ha=ha,
                    fontweight="bold", zorder=21)
    # strong-verification zone on the floor
    ax.add_collection3d(Poly3DCollection([[(2.5, -0.4, OZ[0]), (VX[1], -0.4, OZ[0]), (VX[1], 3.4, OZ[0]),
                                           (2.5, 3.4, OZ[0])]], facecolor=(*to_rgb(ACC), 0.07), edgecolor="none"))
    ax.plot([2.5, 2.5], [-0.4, 3.4], [OZ[0], OZ[0]], color=ACC, lw=0.6, ls="--", zorder=2)
    if not small:
        ax.text(3.55, 3.45, OZ[0], "强验证区 V3–V4", fontsize=7.5, color=ACC, ha="center", zorder=30)
    fs = 5.2 if small else 8
    ax.set_xticks(range(5), [f"V{k}" for k in range(5)] if small else V_TICK, fontsize=fs)
    ax.set_yticks(range(4), [f"L{k}" for k in range(4)] if small else [n.split()[0] for n in L_NAME], fontsize=fs)
    ax.set_zticks(range(1, 7), [f"O{k}" for k in range(1, 7)] if small else O_TICK, fontsize=fs)
    ax.set_xlim(*VX); ax.set_ylim(-0.4, 3.4); ax.set_zlim(OZ[0], OZ[1] + 0.3)
    ax.tick_params(pad=-2 if small else 1)
    for a in (ax.xaxis, ax.yaxis, ax.zaxis):
        a.pane.set_facecolor((0.985, 0.982, 0.975, 1)); a.pane.set_edgecolor("#e4dfd6")
        a._axinfo["grid"].update(color="#ece8e1", linewidth=0.4)
    ax.set_box_aspect((1.45, 1.25, 1.0))
    ax.view_init(elev=20, azim=-56)


FOOT = ("每面墙 = 一个自主性等级（沿右轴切面）；墙上横轴为验证强度 V，纵轴（海拔）为问题开放度 O；"
        "色带由浅到深 = 0.5、2、5、10、20、40、80、160 篇的平滑密度；\n山脊线 = 各验证强度下实际达到的最高开放度（单调插值连接）；"
        "数字 = 该 (O, V, L) 组合的论文数；红色虚线以右为强验证（V3–V4）· 快照 2026-11-01")


def mountain(pts, name, title, sub):
    fig = plt.figure(figsize=(10.5, 8.6), facecolor="white")
    ax = fig.add_axes([0.0, 0.07, 1.0, 0.84], projection="3d", computed_zorder=False)
    mountain_axes(ax, pts)
    ax.set_xlabel("验证强度 V", labelpad=14); ax.set_ylabel("系统自主性 L（切面）", labelpad=10)
    ax.set_zlabel("问题开放度 O（海拔）", labelpad=18)
    n_s = sum(v >= 3 for _, v, _, _ in pts)
    fig.text(0.06, 0.955, title, fontsize=16, fontweight="bold", color=INK)
    fig.text(0.06, 0.925, f"{sub}　·　{len(pts)} 篇，强验证（V3–V4）{n_s} 篇（{100 * n_s / len(pts):.0f}%）",
             fontsize=9, color=MUTED)
    fig.text(0.06, 0.02, FOOT, fontsize=7.3, color=MUTED, linespacing=1.6)
    S.save(fig, name); plt.close(fig)


def mountain_fields(pts, fields):
    fig = plt.figure(figsize=(13.5, 10.8), facecolor="white")
    sets = [("全部", pts)] + [(FZH[f], [p for p in pts if f in fields[p[3]]]) for f in S.FIELDS]
    for i, (lab, sub) in enumerate(sets):
        ax = fig.add_subplot(3, 4, i + 1, projection="3d", computed_zorder=False)
        mountain_axes(ax, sub, small=True)
        ns = sum(v >= 3 for _, v, _, _ in sub)
        ax.set_title(f"{lab}　n = {len(sub)}　强验证 {100 * ns / len(sub):.0f}%", fontsize=8.5, color=INK,
                     fontweight="bold", pad=-12)
    fig.subplots_adjust(left=0.0, right=1.0, top=0.9, bottom=0.05, wspace=0.0, hspace=0.06)
    fig.text(0.03, 0.955, "问题开放度 × 验证强度 × 系统自主性：按学科的山体切面", fontsize=15, fontweight="bold", color=INK)
    fig.text(0.03, 0.928, "每面墙 = 一个自主性等级（L0–L3）；墙上横轴 V0–V4，纵轴（海拔）O1–O6；色带越深论文越多，"
             "数字为峰值组合的论文数；跨学科论文在每个所属学科各计一次。", fontsize=9, color=MUTED)
    fig.text(0.03, 0.02, f"{len(pts)} 篇核心论文，{sum(len(s) for _, s in sets[1:])} 个论文—学科归属 · 快照 2026-11-01",
             fontsize=8, color=MUTED)
    S.save(fig, "fig_ovl_mountain_fields"); plt.close(fig)


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
    import sys
    pts = load()
    mountain(pts, "fig_ovl_mountain", "问题开放度 × 验证强度 × 系统自主性", "全部核心论文")
    if "--all" in sys.argv:
        fields = {c["paper_id"]: set(c["fields"]) for c in S.papercards()}
        for f in S.FIELDS:
            sub = [p for p in pts if f in fields[p[3]]]
            mountain(sub, f"fig_ovl_mountain_f{f}", f"{FZH[f]}：开放度 × 验证强度 × 自主性", f"学科 {f} {FZH[f]}")
        mountain_fields(pts, fields)
        write_counts(pts, fields)
