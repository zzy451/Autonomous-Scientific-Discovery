"""Design study, group B: eight Nature/Science/Cell main-figure styles for one field's O x V x L x era data.
Shortlisted: b3, b8 (-> out/styles/shortlist/). Rejected: b1, b2, b4-b7 (kept; --all renders them to out/styles/rejected/).

  b1 horizon  : one horizon band per openness level over years, strong (V3-V4) and claim-only papers as two strips
  b2 beeswarm : x = openness, one dot per paper swarmed inside verification stripes; colour = autonomy, filled = strong
  b3 raincloud: one raincloud per verification level over openness (discrete bars + Tukey box + packed papers)
  b4 slope    : bump/slope chart, share of each openness level across 2013-2019, 2020-2023, 2024-2026 (all / strong)
  b5 stream   : streamgraph of openness over years, the strongly verified part of every level in red
  b6 mekko    : Marimekko, column width = papers per openness level, stacked height = verification share; autonomy strip
  b7 joint    : openness x verification heatmap with marginal histograms and each cell's autonomy composition
  b8 parallel : parallel coordinates as labelled nodes, one line per paper across era, O, V, L; red = strong
Data: fig_ovl_frontier_mountain.load (ov_coding/increment/classification_results_662.jsonl).
Usage: python3 fig_ovl_styles_B.py [field] [--all]   (default 03) -> out/styles/shortlist/B{n}_{name}_f{field}.png
"""
import sys, collections as C
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch
from matplotlib.lines import Line2D
from matplotlib.collections import LineCollection
from matplotlib.colors import to_hex
from scipy.interpolate import PchipInterpolator
import style as S
from fig_ovl_frontier_mountain import load, ERAS, ERA_TICK
from fig_ovl_surface import INK, MUTED, ACC, L_COL, L_NAME, FZH, ALT
from fig_ovl_modes import O_T, V_T, head, lkey

OUT = S.ROOT / "out" / "styles"
plt.rcParams.update({"font.family": ["Arial Unicode MS", "Arial"], "font.size": 11})
O_COL = ["#d8c99b", "#b8963e", "#6f9a72", "#3d7f8f", "#5b5296", "#2a2d4f"]   # O1-O6: ochre -> green -> teal -> indigo
CLAIM = "#56707f"                                   # claim-only (V0-V2) in single-hue charts
V_COL = ["#dcd7cd", "#b8c3c9", "#7d95a2", ACC, "#7a2418"]
GRID, FAINT, STRIPE = "#e4dfd6", "#b5ae9f", "#f6ece4"
YRS = np.arange(2013, 2027)


def save(fig, k, name, f):
    out = OUT / ("shortlist" if k in (3, 8) else "rejected")
    out.mkdir(parents=True, exist_ok=True)
    fig.savefig(out / f"B{k}_{name}_f{f}.png", dpi=160, facecolor="white"); plt.close(fig)


def status(pp):
    """Per openness level: 'none' (no papers), 'blank' (papers but no strong case) or ''."""
    return {o: "none" if not any(p["o"] == o for p in pp) else
            "blank" if not any(p["o"] == o and p["v"] >= 3 for p in pp) else "" for o in range(1, 7)}


def bare(ax):
    ax.spines[:].set_visible(False); ax.tick_params(length=0)


def spread(ys, gap, lo=None):
    """Push label positions apart to at least `gap`, keeping their mean (simple 1-D repel); optional floor `lo`."""
    ys = np.asarray(ys, float); idx = np.argsort(ys); y = ys[idx].copy()
    for _ in range(200):
        moved = False
        for i in range(1, len(y)):
            d = y[i] - y[i - 1]
            if d < gap:
                y[i - 1] -= (gap - d) / 2; y[i] += (gap - d) / 2; moved = True
        if not moved:
            break
    if lo is not None:
        y[0] = max(y[0], lo)
        for i in range(1, len(y)):
            y[i] = max(y[i], y[i - 1] + gap)
    out = np.empty_like(y); out[idx] = y
    return out


def mkey(fig, x, y, items, fs=11):
    """Marker key: items = [(handle, label)] drawn as a frameless legend at figure coords."""
    fig.legend([h for h, _ in items], [t for _, t in items], loc="lower left", bbox_to_anchor=(x, y), frameon=False,
               ncol=len(items), fontsize=fs, handletextpad=0.4, columnspacing=1.4, borderaxespad=0)


# ---------------------------------------------------------------- B1 horizon chart
def b1(pp, f):
    st = status(pp); NB = 4
    cnt = {(o, s): np.array([sum(p["o"] == o and (p["v"] >= 3) == s and p["year"] == y for p in pp) for y in YRS])
           for o in range(1, 7) for s in (True, False)}
    B = int(np.ceil(max(c.max() for c in cnt.values()) / NB))
    ramps = {True: [S.mix("#ffffff", ACC, t) for t in (0.35, 0.58, 0.8, 1.0)],
             False: [S.mix("#ffffff", CLAIM, t) for t in (0.3, 0.52, 0.76, 1.0)]}
    ramps[True][3] = "#7a2418"
    fig = plt.figure(figsize=(16, 10)); ax = fig.add_axes([0.16, 0.12, 0.7, 0.75])
    H, G = 1.0, 0.55                                   # strip height, gap between openness groups
    base = {}
    for o in range(1, 7):
        y0 = (o - 1) * (2 * H + G)
        base[(o, False)], base[(o, True)] = y0, y0 + H
    for (o, s), y0 in base.items():
        c = cnt[(o, s)]
        ax.add_patch(Rectangle((2012.5, y0), 14, H * 0.94, fc="#faf8f4", ec="none", zorder=0))
        for k in range(NB):
            seg = np.clip(c - k * B, 0, B) / B * H * 0.94
            ax.fill_between(YRS, y0, y0 + seg, step="mid", color=ramps[s][k], lw=0, zorder=1 + k)
        ax.text(2012.4, y0 + H * 0.47, "强验证" if s else "仅声明", ha="right", va="center", fontsize=10,
                color=ACC if s else CLAIM)
        if c.max() > NB * B:
            ax.plot(YRS[c > NB * B], [y0 + H] * int((c > NB * B).sum()), "v", color=INK, ms=5)
    for o in range(1, 7):
        yc = base[(o, False)] + H; n = sum(p["o"] == o for p in pp); k = sum(p["o"] == o and p["v"] >= 3 for p in pp)
        ax.text(2011.3, yc, O_T[o - 1], ha="right", va="center", fontsize=13, fontweight="bold",
                color=ACC if st[o] else INK)
        ax.text(2026.75, yc, f"强 {k} / 共 {n}", va="center", fontsize=12, color=INK if n else FAINT)
        if st[o] == "none":
            ax.text(2019.75, yc, f"本学科无 O{o} 论文 —— 空白", ha="center", va="center", fontsize=12, color=ACC)
        elif st[o] == "blank":
            ax.text(2016, base[(o, True)] + H * 0.47, f"空白：O{o} 有 {n} 篇但无一强验证", ha="center", va="center",
                    fontsize=12, color=ACC, fontweight="bold")
    top = 6 * (2 * H + G) - G
    for xs in (2019.5, 2023.5):
        ax.plot([xs, xs], [-0.2, top + 0.15], color="#cfc8bb", lw=1, ls=(0, (4, 3)), zorder=6)
    for t, (a, b) in zip(ERA_TICK[2:], [(2013, 2019), (2020, 2023), (2024, 2026)]):
        n = sum(a <= p["year"] <= b for p in pp)
        ax.text((a + b) / 2, top + 0.35, f"{t}　{n} 篇", ha="center", fontsize=12, color=INK, fontweight="bold")
    ax.set_xlim(2012.5, 2026.5); ax.set_ylim(-0.25, top + 0.9)
    ax.set_xticks(YRS, [str(y) for y in YRS], fontsize=11); ax.set_yticks([]); bare(ax)
    # band key
    kx, ky = 0.64, 0.035
    fig.text(kx - 0.01, ky + 0.005, f"色阶（每层 {B} 篇）：", ha="right", fontsize=11, color=MUTED)
    for i in range(NB):
        lo, hi = i * B + 1, (i + 1) * B
        for j, s in enumerate((True, False)):
            fig.patches.append(Rectangle((kx + 0.075 * i, ky + 0.022 * (1 - j) - 0.004), 0.022, 0.018,
                                         transform=fig.transFigure, fc=ramps[s][i], ec="none"))
        fig.text(kx + 0.075 * i + 0.026, ky + 0.01, f"{lo}–{hi}", fontsize=10.5, color=INK, va="center")
    fig.text(0.04, ky + 0.01, "上条 = 强验证（V3–V4），下条 = 仅声明（V0–V2）；高值折叠叠加，颜色越深 = 当年越多",
             fontsize=11, color=MUTED, va="center")
    head(fig, f, "地平线图：各开放度逐年论文数",
         "每个开放度两条：强验证 / 仅声明；折叠色阶在窄条内保留小数值　·　灵感：Heer, Kong & Agrawala 2009 (CHI)", pp)
    save(fig, 1, "horizon", f)


# ---------------------------------------------------------------- B2 beeswarm
def swarm_xy(n, dx, dy, width):
    """Hex-packed swarm positions for n dots, centre-out order, rows of at most width/dx dots."""
    if not n:
        return []
    per = max(1, int(width / dx)); rows = int(np.ceil(n / per)); per = int(np.ceil(n / rows))
    pts = []
    for r in range(rows):
        m = min(per, n - r * per)
        off = (r % 2) * dx / 2 if m < per else 0
        for i in range(m):
            pts.append(((i - (m - 1) / 2) * dx + off, (r - (rows - 1) / 2) * dy))
    pts.sort(key=lambda t: (t[0] / dx) ** 2 + (t[1] / dy) ** 2)
    return pts


def b2(pp, f):
    st = status(pp)
    fig = plt.figure(figsize=(16, 10)); ax = fig.add_axes([0.13, 0.15, 0.72, 0.69])
    for v in range(5):
        ax.axhspan(v - 0.5, v + 0.5, color=STRIPE if v >= 3 else ("#f7f6f3" if v % 2 == 0 else "white"), lw=0, zorder=0)
    ax.axhline(2.5, color=ACC, lw=1.4, zorder=1)
    ax.text(0.53, 2.56, "强验证 ↑", color=ACC, ha="left", va="bottom", fontsize=11, fontweight="bold")
    for o in range(2, 7):
        ax.axvline(o - 0.5, color=GRID, lw=0.8, zorder=0)
    cell = C.defaultdict(list)
    for p in pp:
        cell[(p["o"], p["v"])].append(p)
    w_in, h_in = 0.72 * 16 / 6, 0.69 * 10 / 5         # inches per data unit
    d = 0.19                                           # dot pitch, inches
    for (o, v), ps in cell.items():
        ps.sort(key=lambda p: (-p["l"], -p["year"]))
        for (x, y), p in zip(swarm_xy(len(ps), d / w_in, d * 0.88 / h_in, 0.86), ps):
            c = L_COL[p["l"]]
            if p["contested"]:
                ax.plot(o + x, v + y, "x", color=ACC, ms=7, mew=1.8, zorder=4)
            elif p["v"] >= 3:
                ax.plot(o + x, v + y, "o", color=c, ms=11.5, mec="white", mew=0.8, zorder=3)
            else:
                ax.plot(o + x, v + y, "o", mfc="white", mec=c, ms=10.3, mew=1.6, zorder=3)
        ax.text(o + 0.47, v - 0.46, str(len(ps)), ha="right", va="bottom", fontsize=9.5, color=MUTED, zorder=5)
    for v in range(5):
        if not any(p["v"] == v for p in pp):
            ax.text(3.5, v, f"本学科无 {V_T[v]} 论文", ha="center", va="center", color=FAINT, fontsize=13)
    for o in range(1, 7):
        n = sum(p["o"] == o for p in pp); k = sum(p["o"] == o and p["v"] >= 3 for p in pp)
        ax.text(o, 4.62, f"{n} 篇 · 强 {k}" if n else "0 篇", ha="center", fontsize=11.5,
                color=INK if n else FAINT, fontweight="bold")
        if st[o]:
            ax.text(o, -0.78, "空白（无论文）" if st[o] == "none" else "空白（仅声明）", ha="center", va="top",
                    fontsize=12, color=ACC, fontweight="bold")
    ax.set_xlim(0.5, 6.5); ax.set_ylim(-0.5, 4.5)
    ax.set_xticks(range(1, 7), O_T, fontsize=12); ax.set_yticks(range(5), V_T, fontsize=12)
    ax.tick_params(axis="x", pad=8)
    for t, v in zip(ax.get_yticklabels(), range(5)):
        t.set_color(ACC if v >= 3 else INK)
    bare(ax)
    lkey(fig)
    mkey(fig, 0.56, 0.022, [(Line2D([], [], ls="", marker="o", color=INK, ms=8), "实心 = 强验证"),
                            (Line2D([], [], ls="", marker="o", mfc="white", mec=INK, ms=8, mew=1.3), "空心 = 仅声明")])
    head(fig, f, "蜂群图：每篇论文一个点",
         "横轴 = 开放度，条带 = 验证强度（粉 = V3–V4）；点色 = 自主性；格角数字 = 论文数　·　灵感：beeswarm / Wilkinson 点图 1999", pp)
    save(fig, 2, "beeswarm", f)


# ---------------------------------------------------------------- B3 raincloud
def b3(pp, f):
    """Discrete raincloud per verification level: bars = papers per openness level (one scale for the whole figure),
    Tukey box (whiskers = most extreme value within 1.5 IQR, diamonds = outliers), packed dots = papers."""
    SMALL = 5
    st = status(pp); cnt = C.Counter((p["v"], p["o"]) for p in pp); gmax = max(cnt.values())
    fig = plt.figure(figsize=(16, 10)); ax = fig.add_axes([0.13, 0.15, 0.64, 0.69])
    w_in, h_in = 0.64 * 16 / 6.1, 0.69 * 10 / 5          # inches per data unit
    d = 0.1                                              # dot pitch (inches): shrink until the largest cell fits
    while np.ceil(gmax / max(1, int(0.62 * w_in / d))) * d * 0.9 > 0.27 * h_in:
        d *= 0.95
    ms = 6.2 * d / 0.1
    for o in range(1, 7):
        ax.axvline(o, color=GRID, lw=0.8, zorder=0)
    for v in range(5):
        ps = [p for p in pp if p["v"] == v]; n = len(ps); col = ACC if v >= 3 else CLAIM
        if v >= 3:
            ax.axhspan(v - 0.5, v + 0.5, color=STRIPE, lw=0, zorder=0)
        if not n:
            ax.text(3.5, v, f"本学科无 {V_T[v]} 论文", ha="center", va="center", color=FAINT, fontsize=12)
            ax.text(6.7, v, "n = 0", va="center", fontsize=12.5, color=FAINT, fontweight="bold")
            continue
        os_ = np.array([p["o"] for p in ps], float)
        if n >= SMALL:
            for o in range(1, 7):
                k = cnt.get((v, o), 0)
                if k:
                    h = max(k / gmax * 0.33, 0.012)
                    ax.add_patch(Rectangle((o - 0.3, v + 0.02), 0.6, h, fc=col, alpha=0.28, ec=col, lw=1.2, zorder=2))
                    ax.text(o, v + 0.035 + h, str(k), ha="center", va="bottom", fontsize=10.5, color=col, zorder=3)
            q1, med, q3 = np.percentile(os_, [25, 50, 75]); iqr = q3 - q1
            lo, hi = os_[os_ >= q1 - 1.5 * iqr].min(), os_[os_ <= q3 + 1.5 * iqr].max()
            for a, b in ((lo, q1), (q3, hi)):
                if b > a:
                    ax.plot([a, b], [v - 0.07] * 2, color=INK, lw=1.1, zorder=3)
            for x in {lo, hi}:
                ax.plot([x, x], [v - 0.1, v - 0.04], color=INK, lw=1.1, zorder=3)
            ax.add_patch(Rectangle((q1 - 0.03, v - 0.115), q3 - q1 + 0.06, 0.09, fc="white", ec=INK, lw=1.2, zorder=4))
            ax.plot([med, med], [v - 0.135, v - 0.005], color=col, lw=3.2, zorder=5)
            for x in sorted(set(os_[(os_ < lo) | (os_ > hi)])):
                ax.plot(x, v - 0.07, "D", mfc="white", mec=INK, ms=6, mew=1.1, zorder=5)
        for o in range(1, 7):
            cell = sorted([p for p in ps if p["o"] == o], key=lambda p: (-p["l"], -p["year"]))
            yc = v - 0.3 if n >= SMALL else v - 0.05              # small rows: dots alone, centred in the row
            for (x, y), p in zip(swarm_xy(len(cell), d / w_in, d * 0.9 / h_in, 0.62), cell):
                if p["v"] >= 3:
                    ax.plot(o + x, yc + y, "o", color=L_COL[p["l"]], ms=ms, mec="white", mew=0.5, zorder=6)
                else:
                    ax.plot(o + x, yc + y, "o", mfc="white", mec=L_COL[p["l"]], ms=ms * 0.9, mew=1.1 * d / 0.1, zorder=6)
        reach = sorted({p["o"] for p in ps})
        ax.text(6.7, v + 0.1, f"n = {n}", va="center", fontsize=12.5, color=col, fontweight="bold")
        ax.text(6.7, v - 0.17, (f"中位 O{np.median(os_):.0f} · 覆盖 O{reach[0]}–O{reach[-1]}" if n >= SMALL
                                else f"n < {SMALL}：只画论文点"), va="center", fontsize=11, color=MUTED)
    ax.axhline(2.5, color=ACC, lw=1.4, zorder=1)
    ax.text(0.5, 2.54, "强验证 ↑", color=ACC, ha="left", va="bottom", fontsize=11, fontweight="bold")
    for o in range(1, 7):
        if st[o]:
            ax.text(o, -0.85, "空白（无论文）" if st[o] == "none" else "空白（仅声明）", ha="center", va="top",
                    fontsize=12, color=ACC, fontweight="bold")
    ax.set_xlim(0.45, 6.55); ax.set_ylim(-0.5, 4.5)
    ax.set_xticks(range(1, 7), O_T, fontsize=12.5); ax.set_yticks(range(5), V_T, fontsize=12.5)
    ax.tick_params(axis="x", pad=8)
    for t, v in zip(ax.get_yticklabels(), range(5)):
        t.set_color(ACC if v >= 3 else INK)
    bare(ax)
    lkey(fig)
    mkey(fig, 0.54, 0.022, [(Line2D([], [], ls="", marker="o", color=INK, ms=7), "实心 = 强验证"),
                            (Line2D([], [], ls="", marker="o", mfc="white", mec=INK, ms=7, mew=1.1), "空心 = 仅声明"),
                            (Line2D([], [], ls="", marker="D", mfc="white", mec=INK, ms=6, mew=1.1), "离群值")])
    head(fig, f, "雨云图：每个验证强度下的开放度分布",
         f"云 = 各开放度篇数（全图同一尺度），箱 = 四分位，须 = 1.5×IQR，n < {SMALL} 只画点　·　灵感：Allen et al. 2019 (Wellcome Open Res)", pp)
    save(fig, 3, "raincloud", f)


# ---------------------------------------------------------------- B4 bump / slope chart
def b4(pp, f):
    st = status(pp); E = [2, 3, 4]
    fig = plt.figure(figsize=(16, 10))
    panels = [("a　全部论文中各开放度的占比", lambda p: True), ("b　强验证论文（V3–V4）中各开放度的占比", lambda p: p["v"] >= 3)]
    shown = [o for o in range(1, 7) if st[o] != "none"]
    for i, (ttl, keep) in enumerate(panels):
        ax = fig.add_axes([0.075 + 0.47 * i, 0.15, 0.25, 0.62])
        sub = [p for p in pp if keep(p)]
        N = [sum(p["era"] == e for p in sub) for e in E]
        cnt = {o: np.array([sum(p["era"] == e and p["o"] == o for p in sub) for e in E]) for o in shown}
        sh = {o: 100 * cnt[o] / np.maximum(N, 1) for o in shown}
        ymax = max(s.max() for s in sh.values()) * 1.08 + 4
        X = {o: np.arange(3.0) for o in shown}                 # dodge coincident points sideways
        for j in range(3):
            grp = sorted(shown, key=lambda o: sh[o][j]); cl = [[grp[0]]]
            for o in grp[1:]:
                (cl[-1].append(o) if sh[o][j] - sh[cl[-1][-1]][j] < ymax * 0.05 else cl.append([o]))
            for g in cl:
                for r, o in enumerate(g):
                    X[o][j] = j + (r - (len(g) - 1) / 2) * 0.2
        for j in range(3):
            order = sorted([o for o in shown if cnt[o][j]], key=lambda o: -sh[o][j])
            rank = {o: r + 1 for r, o in enumerate(order)}
            for o in shown:
                c = O_COL[o - 1]
                if cnt[o][j]:
                    ax.scatter(X[o][j], sh[o][j], s=430, color=c, edgecolor="white", lw=1.5, zorder=4)
                    ax.text(X[o][j], sh[o][j], str(rank[o]), ha="center", va="center", fontsize=10, color="white",
                            fontweight="bold", zorder=5)
                else:
                    ax.scatter(X[o][j], 0, s=90, color="white", edgecolor=c, lw=1.5, zorder=4)
        for o in shown:
            blank = not any(p["o"] == o for p in sub)
            ax.plot(X[o], sh[o], color=ACC if blank else O_COL[o - 1], lw=1.6 if blank else 3.2,
                    ls=(0, (4, 3)) if blank else "-", zorder=2 if blank else 3, solid_capstyle="round")
        ys = spread([sh[o][2] for o in shown], ymax * 0.07, lo=0)
        for o, y in zip(shown, ys):
            blank = not any(p["o"] == o for p in sub)
            ax.plot([X[o][2] + 0.14, 2.3], [sh[o][2], y], color=FAINT, lw=0.8)
            ax.text(2.33, y, f"{O_T[o - 1]}  {sh[o][2]:.0f}%（{cnt[o][2]}）" + (" 空白" if blank else ""),
                    va="center", fontsize=12, color=ACC if blank else INK, fontweight="bold" if blank else None)
        sh0 = [o for o in shown if cnt[o][0]]
        for o, y in zip(sh0, spread([sh[o][0] for o in sh0], ymax * 0.06)):
            ax.text(min(X[o][0], 0) - 0.17, y, f"{sh[o][0]:.0f}%", ha="right", va="center", fontsize=11.5,
                    color=O_COL[o - 1], fontweight="bold")
        ax.set_xlim(-0.5, 2.25); ax.set_ylim(-4, ymax)
        ax.set_xticks(range(3), [f"{ERA_TICK[e]}\nn = {n}" + ("（样本小）" if n < 10 else "") for e, n in zip(E, N)],
                      fontsize=12)
        ax.set_yticks([]); bare(ax)
        ax.axhline(0, color=GRID, lw=0.8, zorder=0)
        fig.text(0.075 + 0.47 * i, 0.82, ttl, fontsize=15, fontweight="bold", color=INK)
    fig.text(0.04, 0.035, "圈内数字 = 该时期内的排名；空心点 = 该时期无此开放度论文；红虚线 = 该开放度从无强验证（空白）"
             + "".join(f"；{O_T[o - 1]}：各时期均无论文" for o in range(1, 7) if st[o] == "none"),
             fontsize=11, color=MUTED)
    head(fig, f, "坡度排名图：开放度构成随时期的变化",
         "三个时期内各开放度占比与排名；a 为全部论文，b 仅强验证论文　·　灵感：Tufte slopegraph 1983 / bump chart", pp)
    save(fig, 4, "slope", f)


# ---------------------------------------------------------------- B5 streamgraph
def b5(pp, f):
    xg = np.linspace(2012.6, 2026.45, 800); xc = np.clip(xg, 2013, 2026)
    s_col = {o: S.mix(ACC, "#4a120a", max(0, o - 3) * 0.22) for o in range(1, 7)}
    layers = []
    for o in range(1, 7):
        for s in (False, True):
            c = np.array([sum(p["o"] == o and (p["v"] >= 3) == s and p["year"] == y for p in pp) for y in YRS], float)
            if c.sum():
                layers.append((o, s, int(c.sum()), np.clip(PchipInterpolator(YRS, c)(xc), 0, None)))
    F = np.array([d for *_, d in layers])
    g0 = -F.sum(0) / 2                                                   # symmetric (ThemeRiver) baseline
    tops = g0 + np.cumsum(F, 0); bots = np.vstack([g0, tops[:-1]])
    fig = plt.figure(figsize=(16, 10)); ax = fig.add_axes([0.06, 0.15, 0.7, 0.66])
    for (o, s, k, _), lo, hi in zip(layers, bots, tops):
        ax.fill_between(xg, lo, hi, color=s_col[o] if s else O_COL[o - 1], ec="white", lw=0.6, zorder=2)
    mids = [(lo[-1] + hi[-1]) / 2 for lo, hi in zip(bots, tops)]
    lab = spread(mids, (tops[-1][-1] - g0[-1]) * 0.062)
    for (o, s, k, _), m, y in zip(layers, mids, lab):
        ax.plot([2026.45, 2026.6, 2026.75], [m, m, y], color=FAINT, lw=0.8, zorder=3, clip_on=False)
        ax.text(2026.8, y, f"{O_T[o - 1]}　{'强验证' if s else '仅声明'} {k}", va="center", fontsize=11.5,
                color=ACC if s else INK, fontweight="bold" if s else None)
    hi_y = tops[-1].max(); lo_y = -hi_y
    for xs in (2019.5, 2023.5):
        ax.plot([xs, xs], [lo_y, hi_y + 1], color="#cfc8bb", lw=1, ls=(0, (4, 3)), zorder=1)
    for t, (a, b) in zip(ERA_TICK[2:], [(2013, 2019), (2020, 2023), (2024, 2026)]):
        nn = sum(a <= p["year"] <= b for p in pp); ns = sum(a <= p["year"] <= b and p["v"] >= 3 for p in pp)
        ax.text((a + b) / 2, hi_y + 2, f"{t}\n{nn} 篇 · 强 {ns}", ha="center", va="bottom", fontsize=12, color=INK,
                fontweight="bold")
    ax.plot([2013.3, 2013.3], [lo_y + 2, lo_y + 12], color=INK, lw=2.5)
    ax.text(2013.45, lo_y + 7, "10 篇/年", va="center", fontsize=11, color=INK)
    nyr = C.Counter(p["year"] for p in pp)
    ax.set_xticks(YRS, [f"{y}\n{nyr.get(y, 0)}" for y in YRS], fontsize=11)
    ax.text(2012.75, -0.052, "当年篇数", transform=ax.get_xaxis_transform(), ha="right", va="center", fontsize=10.5,
            color=MUTED)
    ax.set_xlim(2012.6, 2026.45); ax.set_ylim(lo_y - 1, hi_y + 9); ax.set_yticks([]); bare(ax)
    blanks = [o for o, s in status(pp).items() if s]
    fig.text(0.04, 0.035, "层宽 = 每年论文数（逐年计数，PCHIP 平滑连接）；红色层 = 该开放度的强验证（V3–V4）部分，其余为仅声明；空白："
             + "、".join(f"O{o}" for o in blanks) + "（无红色层）", fontsize=11, color=MUTED)
    head(fig, f, "河流图：各开放度的论文流量",
         "每条河道 = 一个开放度，红色支流 = 其中强验证；对称基线　·　灵感：Byron & Wattenberg 2008 (IEEE TVCG)", pp)
    save(fig, 5, "stream", f)


# ---------------------------------------------------------------- B6 Marimekko
def b6(pp, f):
    st = status(pp); N = len(pp); gap = 0.007
    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_axes([0.08, 0.27, 0.68, 0.55]); axl = fig.add_axes([0.08, 0.12, 0.68, 0.06])
    x, narrow = 0.0, []
    for o in range(1, 7):
        ps = [p for p in pp if p["o"] == o]; n = len(ps)
        if not n:
            ax.plot([x - gap, x - gap], [0, 1], color=ACC, lw=1.5, ls=(0, (3, 2)))
            ax.text(x - 2 * gap, 1.015, f"O{o}\n无论文", ha="right", va="bottom", fontsize=11, color=ACC, fontweight="bold")
            continue
        w = n / N; y = 0; k = sum(p["v"] >= 3 for p in ps)
        for v in range(5):
            m = sum(p["v"] == v for p in ps); h = m / n
            if m:
                ax.add_patch(Rectangle((x, y), w, h, fc=V_COL[v], ec="white", lw=1.5))
                if w > 0.05 and h > 0.05:
                    ax.text(x + w / 2, y + h / 2, f"{m}" + (f"\n{h:.0%}" if h > 0.12 else ""), ha="center", va="center",
                            fontsize=12 if h > 0.12 else 10, color="white" if v >= 2 else INK, fontweight="bold")
            y += h
        lw_ = 0
        for l in range(4):
            m = sum(p["l"] == l for p in ps)
            if m:
                axl.add_patch(Rectangle((x + lw_, 0), w * m / n, 1, fc=L_COL[l], ec="white", lw=1.2))
                if w * m / n > 0.03:
                    axl.text(x + lw_ + w * m / n / 2, 0.5, str(m), ha="center", va="center", fontsize=10.5, color="white",
                             fontweight="bold")
                lw_ += w * m / n
        if w > 0.05:
            ax.text(x + w / 2, 1.015, f"{O_T[o - 1]}\n{n} 篇", ha="center", va="bottom", fontsize=12.5, fontweight="bold",
                    color=ACC if st[o] else INK)
            ax.text(x + w / 2, -0.03, f"强验证 {k / n:.0%}" if k else "空白：无强验证", ha="center", va="top", fontsize=12,
                    color=ACC, fontweight="bold")
        else:
            narrow.append((o, x + w / 2, n, k))
        x += w + gap
    for j, (o, xc, n, k) in enumerate(narrow):
        yl = 0.97 - 0.1 * j
        ax.annotate(f"{O_T[o - 1]}　{n} 篇 · 强 {k}", (xc, 1.0), xytext=(x + 0.03, yl), textcoords="data", va="center",
                    fontsize=11.5, color=INK, fontweight="bold",
                    arrowprops=dict(arrowstyle="-", color=FAINT, lw=0.8, connectionstyle="angle,angleA=0,angleB=90,rad=0"),
                    annotation_clip=False)
    for v in range(5):
        yy = 0.08 + 0.13 * v
        ax.add_patch(Rectangle((x + 0.03, yy - 0.035), 0.022, 0.07, fc=V_COL[v], ec="none", clip_on=False))
        ax.text(x + 0.06, yy, V_T[v] + ("　强" if v >= 3 else ""), va="center", fontsize=12, color=ACC if v >= 3 else INK)
    ax.set_xlim(-0.04, x - gap); ax.set_ylim(0, 1); axl.set_xlim(-0.04, x - gap); axl.set_ylim(0, 1)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1], ["0", "25%", "50%", "75%", "100%"], fontsize=10, color=MUTED)
    ax.set_xticks([]); bare(ax); axl.set_xticks([]); axl.set_yticks([]); bare(axl)
    axl.text(-0.01, 0.5, "自主性", ha="right", va="center", fontsize=12, color=INK, fontweight="bold")
    lkey(fig)
    head(fig, f, "马赛克图：开放度的规模与验证构成",
         "列宽 ∝ 该开放度论文数，列内高度 = 验证强度构成（红 = V3–V4），下条 = 自主性构成　·　灵感：Hartigan & Kleiner 1981 mosaic / Marimekko", pp)
    save(fig, 6, "mekko", f)


# ---------------------------------------------------------------- B7 joint heatmap with marginals
def b7(pp, f):
    st = status(pp)
    fig = plt.figure(figsize=(16, 10.5))
    ax = fig.add_axes([0.13, 0.12, 0.56, 0.55]); axt = fig.add_axes([0.13, 0.69, 0.56, 0.17])
    axr = fig.add_axes([0.705, 0.12, 0.13, 0.55])
    cell = C.defaultdict(list)
    for p in pp:
        cell[(p["o"], p["v"])].append(p)
    mx = max(len(c) for c in cell.values())
    for o in range(1, 7):
        for v in range(5):
            ps = cell.get((o, v), []); n = len(ps); t = n / mx
            ax.add_patch(Rectangle((o - 0.47, v - 0.47), 0.94, 0.94, fc=ALT(0.1 + 0.6 * t) if n else "white",
                                   ec=GRID, lw=0.8, zorder=1))
            if not n:
                continue
            ax.text(o - 0.4, v + 0.4, str(n), ha="left", va="top", fontsize=16, fontweight="bold",
                    color="white" if t > 0.45 else INK, zorder=3)
            x0 = o - 0.4
            for l in range(4):
                m = sum(p["l"] == l for p in ps)
                if m:
                    ax.add_patch(Rectangle((x0, v - 0.36), 0.8 * m / n, 0.17, fc=L_COL[l], ec="white", lw=1, zorder=3))
                    if 0.8 * m / n > 0.13:
                        ax.text(x0 + 0.4 * m / n, v - 0.275, str(m), ha="center", va="center", fontsize=9.5,
                                color="white", fontweight="bold", zorder=4)
                    x0 += 0.8 * m / n
    ax.add_patch(Rectangle((0.5, 2.5), 6, 2, fc="none", ec=ACC, lw=2.2, zorder=5))
    ax.text(6.47, 4.44, "强验证区", ha="right", va="top", fontsize=11, color=ACC, fontweight="bold", zorder=6)
    ax.set_xlim(0.5, 6.5); ax.set_ylim(-0.5, 4.5)
    ax.set_xticks(range(1, 7), O_T, fontsize=12); ax.set_yticks(range(5), V_T, fontsize=12)
    for t, v in zip(ax.get_yticklabels(), range(5)):
        t.set_color(ACC if v >= 3 else INK)
    for t, o in zip(ax.get_xticklabels(), range(1, 7)):
        t.set_color(ACC if st[o] else INK)
    bare(ax)
    no = [sum(p["o"] == o for p in pp) for o in range(1, 7)]; so = [sum(p["o"] == o and p["v"] >= 3 for p in pp) for o in range(1, 7)]
    axt.bar(range(1, 7), np.array(no) - so, 0.6, color=CLAIM, alpha=0.55)
    axt.bar(range(1, 7), so, 0.6, bottom=np.array(no) - so, color=ACC)
    for o in range(1, 7):
        lab = f"{no[o - 1]}" + (f"（强 {so[o - 1]}）" if so[o - 1] else "") + ("　空白" if st[o] else "")
        axt.text(o, no[o - 1] + max(no) * 0.05, lab, ha="center", va="bottom", fontsize=11.5,
                 color=ACC if st[o] else INK, fontweight="bold" if st[o] else None)
    axt.set_xlim(0.5, 6.5); axt.set_ylim(0, max(no) * 1.35); axt.set_xticks([]); axt.set_yticks([]); bare(axt)
    axt.axhline(0, color=INK, lw=0.8)
    nv = [sum(p["v"] == v for p in pp) for v in range(5)]
    axr.barh(range(5), nv, 0.6, color=[ACC if v >= 3 else CLAIM for v in range(5)], alpha=1)
    for v in range(5):
        axr.text(nv[v] + max(nv) * 0.04, v, str(nv[v]), va="center", fontsize=11.5, color=ACC if v >= 3 else INK)
    axr.set_ylim(-0.5, 4.5); axr.set_xlim(0, max(nv) * 1.3); axr.set_xticks([]); axr.set_yticks([]); bare(axr)
    axr.axvline(0, color=INK, lw=0.8)
    fig.text(0.715, 0.80, "格内读法", fontsize=13, fontweight="bold", color=INK)
    fig.text(0.715, 0.70, "大数字 = 论文数（底色越深越多）\n下方色条 = 该格自主性构成\n上方边际 = 各开放度篇数（红 = 强验证）\n右侧边际 = 各验证强度篇数",
             fontsize=11, color=MUTED, linespacing=1.6)
    lkey(fig)
    head(fig, f, "联合热图：开放度 × 验证强度",
         "主图每格 = 一种（O, V）组合，附自主性构成；上、右为两条边际分布　·　灵感：seaborn jointplot / Nature Methods Points of View", pp)
    save(fig, 7, "joint", f)


# ---------------------------------------------------------------- B8 parallel coordinates
def b8(pp, f):
    """Parallel coordinates drawn as parallel sets: every category is a labelled node (empty ones compressed to a
    dashed stub), lines run node edge to node edge and never under a label; colour = strong vs claim, L = node colour."""
    st = status(pp)
    AX = [("时期", list(ERA_TICK)), ("开放度 O", O_T), ("验证强度 V", V_T), ("自主性 L", L_NAME)]
    XC, NW, EMPTY_W, FILL = [0.0, 1.3, 2.6, 3.9], 0.46, 0.55, 0.84
    vals = np.array([[p["era"], p["o"] - 1, p["v"], p["l"]] for p in pp]).reshape(-1, 4)
    strong = np.array([p["v"] >= 3 for p in pp], bool)
    slots = []
    for a, (_, ticks) in enumerate(AX):
        w = np.array([1.0 if (vals[:, a] == k).any() else EMPTY_W for k in range(len(ticks))])
        e = np.r_[0, np.cumsum(w)] / w.sum()                          # empty categories get a short stub
        slots.append([(e[k], e[k + 1]) for k in range(len(ticks))])
    Yin, Yout = np.zeros(vals.shape), np.zeros(vals.shape)
    for a in range(4):
        for Y, keys in ((Yin, (a - 1, a + 1)), (Yout, (a + 1, a - 1))):
            keys = [b for b in keys if 0 <= b < 4]
            for k, (lo, hi) in enumerate(slots[a]):
                idx = sorted(np.where(vals[:, a] == k)[0], key=lambda i: tuple(vals[i, b] for b in keys) + (int(strong[i]),))
                m = len(idx); c = (lo + hi) / 2; half = (hi - lo) * FILL / 2 * 0.86
                for r, i in enumerate(idx):
                    Y[i, a] = c + ((r - (m - 1) / 2) / (m - 1) * 2 * half if m > 1 else 0)
    t = np.linspace(0, 1, 40); s = 3 * t ** 2 - 2 * t ** 3
    paths = [np.concatenate([np.c_[XC[a] + NW / 2 + t * (XC[a + 1] - XC[a] - NW),
                                   Yout[i, a] + (Yin[i, a + 1] - Yout[i, a]) * s] for a in range(3)]) for i in range(len(pp))]
    fig = plt.figure(figsize=(16, 10)); ax = fig.add_axes([0.04, 0.1, 0.92, 0.74])
    for sel, col, lw, al, z in ((~strong, CLAIM, 0.9, 0.35, 2), (strong, ACC, 1.3, 0.75, 3)):
        ax.add_collection(LineCollection([paths[i] for i in np.where(sel)[0]], colors=col, linewidths=lw, alpha=al,
                                         zorder=z))
    for a, (name, ticks) in enumerate(AX):
        ax.text(XC[a], 1.035, name, ha="center", va="bottom", fontsize=15, fontweight="bold", color=INK)
        for k, lab in enumerate(ticks):
            lo, hi = slots[a][k]; h = (hi - lo) * FILL; y0 = lo + (hi - lo - h) / 2
            n = int((vals[:, a] == k).sum()); ns = int(((vals[:, a] == k) & strong).sum())
            fc, ec, tc, ls = "#f4f2ee", "#cfc8bb", INK, "-"
            if a == 2 and k >= 3:
                fc, ec, tc = STRIPE, ACC, ACC
            if not n:
                fc, ec, tc, ls = "white", FAINT, FAINT, (0, (3, 2))
            if a == 1 and st[k + 1]:
                tc = ACC
                lab += "\n空白（无论文）" if st[k + 1] == "none" else "\n空白（仅声明）"
            elif not n:
                lab += "\n无论文"
            if n:
                lab += f"\n{n} 篇" + (f" · 强 {ns}" if a != 2 else "")
            ax.add_patch(Rectangle((XC[a] - NW / 2, y0), NW, h, fc=fc, ec=ec, lw=1.2, ls=ls, zorder=5))
            if a == 3 and n:                                    # autonomy key colour as a band on the free edge
                ax.add_patch(Rectangle((XC[a] + NW / 2 - 0.05, y0), 0.05, h, fc=L_COL[k], ec="none", zorder=6))
            ax.text(XC[a], y0 + h / 2, lab, ha="center", va="center", fontsize=12, color=tc, zorder=6, linespacing=1.3,
                    fontweight="bold" if (a == 1 and st[k + 1]) or (a == 2 and k >= 3 and n) else None)
    ax.set_xlim(XC[0] - NW / 2 - 0.02, XC[-1] + NW / 2 + 0.02); ax.set_ylim(-0.01, 1.08); ax.axis("off")
    lkey(fig)
    mkey(fig, 0.56, 0.022, [(Line2D([], [], color=ACC, lw=2), "红线 = 强验证（V3–V4）"),
                            (Line2D([], [], color=CLAIM, lw=1.2, alpha=0.6), "蓝灰线 = 仅声明")])
    head(fig, f, "平行坐标：每篇论文一条路径",
         "时期 → 开放度 → 验证 → 自主性；节点两侧按相邻轴分别排序以减少交叉，虚线框 = 无论文　·　灵感：Inselberg 1985 / Kosara parallel sets 2006", pp)
    save(fig, 8, "parallel", f)


SHORTLIST = (b3, b8)                         # approved; the other six were rejected (kept, render with --all)
if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    f = (args or ["03"])[0]; pp = load(f)
    for fn in SHORTLIST + ((b1, b2, b4, b5, b6, b7) if "--all" in sys.argv else ()):
        fn(pp, f)
