"""The proposal's three-way classification as one continuous mountain fitted through the 3D scatter.

Every (V, L, O) combination is a point in the three-axis space (verification V0-V4 front, autonomy L0-L3
right, openness O1-O6 up), weighted by its papers. The mountain is the Gaussian-smooth surface through all
the points: a paper-weighted Gaussian-kernel (Nadaraya-Watson) regression of openness over (V, L), settling
onto the plain far from the data; an autonomy level with no papers (L0) sits at 0. The line view draws the
L0-L3 lines on the surface with the paper count of each (V, L) column; the quantile view adds, per level, the
25-75% band and median of openness, because a mean surface alone hides the spread.
Data: ov_coding/increment/classification_results_662.jsonl. White background only.

  fig_ovl_surface          : all 662 papers, surface with its scatter
  fig_ovl_surface_cut      : the same surface with its L0-L3 lines and (V, L) counts
  fig_ovl_surface_quantiles: the lines plus each level's 25-75% openness band and median
  fig_ovl_surface_fNN      : one per field 01-11 (a cross-field paper counts in every field it has)
  fig_ovl_surface_fields   : all papers plus the 11 fields as small multiples
  derived/ovl_cube_counts.csv : every (O, V, L) count, all papers and each field
Usage: python3 fig_ovl_surface.py [--all]
"""
import sys, json, collections as C
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, LightSource, Normalize, to_rgb
from matplotlib.cm import ScalarMappable
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import style as S

INC = S.ROOT / "ov_coding" / "increment" / "classification_results_662.jsonl"
INK, MUTED, ACC = "#1d1d1b", "#6b665c", "#b2412f"
O_TICK = ["O1 规则世界", "O2 既定基准", "O3 新实例", "O4 需物理检验", "O5 开放数学", "O6 开放科学"]
V_TICK = ["V0 声明", "V1 基准", "V2 计算/仿真", "V3 物理实验", "V4 证明/复现"]
L_NAME = ["L0 工具", "L1 任务助手", "L2 闭环执行者", "L3 自主研究者"]
L_COL = ["#8e8a82", "#3f7fa0", "#d6903f", "#c4472f"]
FZH = {"01": "形式与计算科学", "02": "物理与天文", "03": "化学", "04": "材料", "05": "地球与环境", "06": "生命科学",
       "07": "医学与健康", "08": "农业与食品", "09": "工程与工业", "10": "航空航天、海洋与交通", "11": "社会与知识系统"}
BASE = 0.0                                                  # altitude of the plain: no papers
VX, LY = (-1.0, 5.0), (-1.0, 4.0)
RES = 24                                                    # surface samples per class step
plt.rcParams.update({"font.family": ["Arial Unicode MS", "Arial"], "font.size": 9})


def load():
    rows = [json.loads(l) for l in open(INC, encoding="utf-8")]
    return [(int(r["openness"][1]), int(r["verification"][1]), int(r["autonomy"][1]), r["paper_id"])
            for r in rows if r["coded"]]


SIG_S, SIG_L, W0 = 0.55, 0.22, 0.15  # kernel width along V and along L (class steps); weight of the plain
# SIG_L is narrow so a line at one autonomy level reflects that level, not its much larger neighbour
ALT = LinearSegmentedColormap.from_list("alt", ["#f3efe6", "#d9cdb0", "#a9b08f", "#6f9184", "#3f6b78", "#2b4a63"])


def cells(pts):
    return C.Counter((v, L, o) for o, v, L, _ in pts)


def height(cell, V, L):
    """The surface through the scatter: Gaussian-kernel (Nadaraya-Watson) mean openness over (V, L), each
    (V, L, O) point weighted by its papers; far from the data it settles onto the plain at BASE."""
    num = np.full(np.shape(V), W0 * BASE, float); den = np.full(np.shape(V), W0, float)
    for (v, l, o), c in cell.items():
        w = c * np.exp(-(V - v) ** 2 / (2 * SIG_S ** 2) - (L - l) ** 2 / (2 * SIG_L ** 2))
        num += w * o; den += w
    z = num / den
    used = {l for _, l, _ in cell}
    for e in set(range(4)) - used:                              # an autonomy level with no papers sits at 0,
        dl = np.asarray(L, float) - e                           # and so does the side of it with no data
        if all(l > e for l in used):
            dl = np.clip(dl, 0, None)
        elif all(l < e for l in used):
            dl = np.clip(-dl, 0, None)
        d = np.clip(np.abs(dl) / 0.7, 0, 1)
        z = BASE + (z - BASE) * d * d * (3 - 2 * d)
    return z, den - W0


ZMAX = 6.2
QSIG = 0.35                    # spread given to each paper's openness when forming quantiles (class steps)


def quantiles(cell, L, x, qs=(0.25, 0.5, 0.75)):
    """Paper-weighted quantiles of openness along the autonomy line L, smoothed in V like the surface."""
    og = np.linspace(-1, 8, 901)
    row = [(v, o, c) for (v, l, o), c in cell.items() if l == L]
    out = np.full((len(qs), len(x)), np.nan); wsum = np.zeros(len(x))
    for k, xv in enumerate(x):
        w = np.array([c * np.exp(-(xv - v) ** 2 / (2 * SIG_S ** 2)) for v, o, c in row])
        wsum[k] = w.sum()
        if w.sum() < 0.3:
            continue
        pdf = sum(wi * np.exp(-(og - o) ** 2 / (2 * QSIG ** 2)) for wi, (v, o, c) in zip(w, row))
        cdf = np.cumsum(pdf); cdf /= cdf[-1]
        out[:, k] = np.interp(qs, cdf, og)
    return out, wsum


def surface_axes(ax, pts, small=False, cut=False, quant=False):
    cell = cells(pts)
    gv = np.linspace(*VX, int((VX[1] - VX[0]) * RES) + 1)
    gl = np.linspace(*LY, int((LY[1] - LY[0]) * RES) + 1)
    VV, LL = np.meshgrid(gv, gl, indexing="ij")
    zz, wt = height(cell, VV, LL)
    ls = LightSource(azdeg=300, altdeg=38)
    rgb = ALT(np.clip((zz - BASE) / (ZMAX - BASE), 0, 1))[:, :, :3]
    rgb = ls.shade_rgb(rgb, zz * 2.5, blend_mode="soft", fraction=0.9)
    fc = np.dstack([rgb, np.full(zz.shape, 0.88)])
    ax.plot_surface(VV, LL, zz, facecolors=fc, rstride=2, cstride=2, linewidth=0, antialiased=True, shade=False,
                    zorder=1)
    ax.contour(VV, LL, zz, levels=np.arange(1, 7), colors="white", linewidths=0.4, alpha=0.7, zorder=2)
    top = max(cell.values())
    if not cut:
        # the scatter the surface is fitted through: one point per (V, L, O), area proportional to papers
        for (v, l, o), c in sorted(cell.items(), key=lambda t: t[0][1]):
            zs, _ = height(cell, np.array(v, float), np.array(l, float))
            ax.plot([v, v], [l, l], [o, float(zs)], color=INK, lw=0.4, alpha=0.5, ls=":", zorder=9)
            ax.scatter([v], [l], [o], s=(4 if small else 8) + (90 if small else 420) * c / top, c=L_COL[l],
                       edgecolors="white", linewidths=0.6, alpha=0.95, depthshade=False, zorder=10)
            if c >= (20 if small else 8):
                ax.text(v, l, o + (0.25 if small else 0.3), str(c), fontsize=5.5 if small else 8, color=INK,
                        ha="center", fontweight="bold", zorder=21)
    else:
        col_n = C.Counter()
        for (v, l, o), c in cell.items():
            col_n[(v, l)] += c
        for L in (3, 2, 1, 0):                                      # far cut first
            col = to_rgb(L_COL[L])
            z, _ = height(cell, gv, np.full_like(gv, L))
            ax.plot(gv, [L] * len(gv), z, color=L_COL[L], lw=1.2 if small else 2.4, zorder=6)
            if quant and any(l == L for _, l, _ in cell):
                q, ws = quantiles(cell, L, gv)
                ok = ~np.isnan(q[0])
                for seg in np.split(np.arange(len(gv)), np.nonzero(np.diff(ok.astype(int)))[0] + 1):
                    seg = seg[ok[seg]]
                    if len(seg) < 2:
                        continue
                    band = list(zip(gv[seg], [L] * len(seg), q[2, seg])) + \
                        list(zip(gv[seg][::-1], [L] * len(seg), q[0, seg][::-1]))
                    ax.add_collection3d(Poly3DCollection([band], facecolor=(*col, 0.3), edgecolor=(*col, 0.8),
                                                         linewidth=0.4), zs=None)
                    ax.plot(gv[seg], [L] * len(seg), q[1, seg], color=L_COL[L], lw=1.0, ls="--", zorder=7)
            for v in range(5):
                c = col_n.get((v, L), 0)
                zt, _ = height(cell, np.array(v, float), np.array(L, float))
                ax.scatter([v], [L], [float(zt)], s=5 if small else 16, c=L_COL[L] if c else "white",
                           edgecolors="white" if c else L_COL[L], linewidths=0.7, depthshade=False, zorder=20)
                ax.text(v, L, float(zt) + (0.28 if small else 0.32), str(c), fontsize=5.5 if small else 8.5,
                        color=INK, ha="center", fontweight="bold", zorder=21)
    # strong-verification zone on the plain
    ax.plot([2.5, 2.5], [LY[0], LY[1]], [BASE, BASE], color=ACC, lw=0.7, ls="--", zorder=2)
    if not small:
        ax.text(3.75, LY[0] + 0.3, BASE, "强验证区 V3–V4", fontsize=7.5, color=ACC, ha="center", zorder=30)
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
    ax.view_init(elev=24, azim=-45)


FOOT = ("散点 = 三维坐标系中每个 (V, L, O) 组合，点面积 ∝ 论文数，颜色 = 自主性等级；山体 = 穿过全部散点的高斯光滑曲面"
        "（按论文数加权的高斯核回归，σ_V = 0.55、σ_L = 0.22 级），海拔为该处论文的平均开放度 O；\n虚线 = 散点到曲面的偏离；白色等高线为 O1–O6；"
        "远离数据处曲面回落到平原；红色虚线以右为强验证（V3–V4）· 快照 2026-11-01")
FOOT_CUT = ("山体 = 穿过全部 (V, L, O) 散点的高斯光滑曲面（按论文数加权的高斯核回归，σ_V = 0.55、σ_L = 0.22 级），海拔为该处论文的平均开放度 O，"
            "没有论文的自主性等级（L0）为 0；\n四条彩色线 = 山体表面上 L0–L3 处的等自主性线；线上数字 = 该 (V, L) 组合的论文数"
            "（空心点 = 0 篇）；红色虚线以右为强验证（V3–V4）· 快照 2026-11-01")
FOOT_Q = ("山体与彩色实线 = 按论文数加权的平均开放度（高斯核回归，σ_V = 0.55、σ_L = 0.22 级）；色带 = 同一自主性等级下开放度的 25%–75% 分位区间，"
          "虚线 = 中位数（每篇论文的 O 按 σ = 0.35 级平滑后取加权分位）；\n线上数字 = 该 (V, L) 组合的论文数（空心点 = 0 篇）；"
          "L0 没有论文，海拔为 0；红色虚线以右为强验证（V3–V4）· 快照 2026-11-01")


def colorbar(fig, rect, fs=8):
    cax = fig.add_axes(rect)
    cb = fig.colorbar(ScalarMappable(norm=Normalize(BASE, ZMAX), cmap=ALT), cax=cax)
    cb.set_ticks(range(0, 7), labels=["0 无论文"] + [f"O{k}" for k in range(1, 7)], fontsize=fs)
    cb.outline.set_visible(False)
    cax.set_title("山体海拔\n开放度 O", fontsize=fs, color=INK, loc="left")
    return cb


def figure(pts, name, title, sub, cut=False, quant=False):
    fig = plt.figure(figsize=(10.5, 8.6), facecolor="white")
    ax = fig.add_axes([0.0, 0.07, 0.94, 0.84], projection="3d", computed_zorder=False)
    surface_axes(ax, pts, cut=cut or quant, quant=quant)
    colorbar(fig, [0.925, 0.3, 0.014, 0.36])
    ax.set_xlabel("验证强度 V", labelpad=14); ax.set_ylabel("系统自主性 L", labelpad=8)
    ax.set_zlabel("问题开放度 O（海拔）", labelpad=18)
    n_s = sum(v >= 3 for _, v, _, _ in pts)
    fig.text(0.06, 0.955, title, fontsize=16, fontweight="bold", color=INK)
    fig.text(0.06, 0.925, f"{sub}　·　{len(pts)} 篇，强验证（V3–V4）{n_s} 篇（{100 * n_s / len(pts):.0f}%）",
             fontsize=9, color=MUTED)
    fig.text(0.06, 0.02, FOOT_Q if quant else FOOT_CUT if cut else FOOT, fontsize=7.2, color=MUTED, linespacing=1.6)
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
    fig.subplots_adjust(left=0.0, right=0.935, top=0.9, bottom=0.05, wspace=0.0, hspace=0.06)
    fig.text(0.03, 0.955, "问题开放度 × 验证强度 × 系统自主性：按学科的山体", fontsize=15, fontweight="bold", color=INK)
    fig.text(0.03, 0.928, "散点 = 各 (V, L, O) 组合（面积 ∝ 论文数，颜色 = 自主性）；山体 = 穿过全部散点的高斯光滑曲面，海拔为开放度 O；"
             "数字为较大组合的论文数；跨学科论文在每个所属学科各计一次。", fontsize=9, color=MUTED)
    fig.text(0.03, 0.02, f"{len(pts)} 篇核心论文，{sum(len(s) for _, s in sets[1:])} 个论文—学科归属 · 快照 2026-11-01",
             fontsize=8, color=MUTED)
    for k, L in enumerate((0, 1, 2, 3)):
        fig.text(0.62 + 0.09 * k, 0.02, f"■ {L_NAME[L]}", fontsize=8.5, color=L_COL[L], fontweight="bold")
    colorbar(fig, [0.945, 0.35, 0.008, 0.3], fs=7)
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
    figure(pts, "fig_ovl_surface_cut", "问题开放度 × 验证强度 × 系统自主性", "全部核心论文", cut=True)
    figure(pts, "fig_ovl_surface_quantiles", "问题开放度 × 验证强度 × 系统自主性：分位区间", "全部核心论文", quant=True)
    if "--all" in sys.argv:
        fields = {c["paper_id"]: set(c["fields"]) for c in S.papercards()}
        for f in S.FIELDS:
            sub = [p for p in pts if f in fields[p[3]]]
            figure(sub, f"fig_ovl_surface_f{f}", f"{FZH[f]}：开放度 × 验证强度 × 自主性", f"学科 {f} {FZH[f]}")
        fields_sheet(pts, fields)
        write_counts(pts, fields)
