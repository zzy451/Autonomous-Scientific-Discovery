"""Design study, group D (GitHub / product-UI / tech-keynote styles) for one field's O x V x L x year data.

  D1 contrib   : GitHub contribution graph, rows = O1-O6, columns = years, green = papers, red dot = strong share
  D2 punchcard : GitHub punch card, O x V grid of dots sized by papers, coloured by the dominant autonomy level
  D3 bento     : Apple keynote bento grid, big-number tiles with mini charts
  D4 rings     : Apple Watch activity rings, one ring per O level, red arc = strong, grey = claims, outer sub-ring = L
                 (approved; the only style rendered by default)
  D5 swimlane  : swimlane timeline, lanes = O levels, one tick per paper at its year, tall = strong, colour = L
  D6 barcode   : barcode / DNA strip, per O row one bar per paper ordered by year, colour = V (V3-V4 red side)
  D7 radar     : radar small multiples, one radar per autonomy level, O profile + strong profile
  D8 badges    : README badge infographic, shields-style badges, per-O sparklines and language-bar of L
Strong = V3-V4. Blank (空白) = an O level with no strong case (in field 03: O1 has no papers, O2 only claims).
Data: fig_ovl_frontier_mountain.load (ov_coding/increment/classification_results_662.jsonl).
Usage: python3 fig_ovl_styles_D.py [field] [--all]   (default 03; d4 only -> out/styles/shortlist/D4_rings_f{field}.png;
       --all also renders the rejected D1-D3, D5-D8 -> out/styles/rejected/)
"""
import sys, collections as C
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Wedge, Circle, Rectangle, Polygon
import style as S
from fig_ovl_frontier_mountain import load, ERAS, ERA_TICK
from fig_ovl_surface import INK, MUTED, ACC, L_COL, L_NAME, FZH, ALT
from fig_ovl_modes import O_T, V_T, head, lkey

OUT = S.ROOT / "out" / "styles"
GH = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]          # GitHub contribution greens
V_COL = ["#2b5c8a", "#5f8fb8", "#a9c6de", "#e58a72", "#b2412f"]       # diverging: claims cool, strong red
LINE = "#e5e3df"
YRS = list(range(2013, 2027))
plt.rcParams.update({"font.family": ["Arial Unicode MS", "Arial"], "font.size": 11})


def stats(pp):
    n = C.Counter(p["o"] for p in pp); s = C.Counter(p["o"] for p in pp if p["v"] >= 3)
    blank = [o for o in range(1, 7) if not s[o]]
    return n, s, blank


def blank_tag(o, n):
    return "空白 · 无论文" if not n[o] else "空白 · 仅声明"


SHORT = {4}                                                          # styles the user approved


def save(fig, k, name, field):
    d = OUT / ("shortlist" if k in SHORT else "rejected"); d.mkdir(parents=True, exist_ok=True)
    fig.savefig(d / f"D{k}_{name}_f{field}.png", dpi=160, facecolor="white"); plt.close(fig)


def rbox(ax, x, y, w, h, fc, r=0.1, ec="none", lw=0, z=1, **kw):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=lw, zorder=z, **kw))


def d1(pp, f):
    """GitHub contribution graph."""
    n, s, blank = stats(pp)
    fig, ax = plt.subplots(figsize=(16, 7.6)); fig.subplots_adjust(0.11, 0.15, 0.99, 0.83)
    cnt = C.Counter((p["o"], p["year"]) for p in pp); st = C.Counter((p["o"], p["year"]) for p in pp if p["v"] >= 3)
    lvl = lambda k: 0 if k == 0 else 1 if k == 1 else 2 if k <= 3 else 3 if k <= 9 else 4
    for o in range(1, 7):
        y = 6 - o
        for j, yr in enumerate(YRS):
            k = cnt[(o, yr)]
            rbox(ax, j + 0.06, y + 0.06, 0.88, 0.88, GH[lvl(k)], r=0.14)
            if k:
                ax.text(j + 0.12, y + 0.14, str(k), fontsize=10, color="white" if lvl(k) >= 3 else INK, fontweight="bold")
            if st[(o, yr)]:
                sh = st[(o, yr)] / k
                ax.add_patch(Circle((j + 0.76, y + 0.76), 0.06 + 0.1 * np.sqrt(sh), fc=ACC, ec="white", lw=1.2, zorder=3))
        # right: totals and an autonomy bar (GitHub language bar)
        ax.text(14.35, y + 0.5, f"{n[o]}", va="center", fontsize=14, fontweight="bold", color=INK)
        ax.text(15.05, y + 0.5, f"强 {s[o]}" if s[o] else blank_tag(o, n), va="center", fontsize=12,
                color=ACC, fontweight="bold")
        x0 = 16.9
        for l in range(4):
            w = 2.2 * sum(p["o"] == o and p["l"] == l for p in pp) / max(n[o], 1)
            if w:
                ax.add_patch(Rectangle((x0, y + 0.38), w, 0.24, fc=L_COL[l], ec="white", lw=0.8))
            x0 += w
        if not n[o]:
            ax.add_patch(Rectangle((16.9, y + 0.38), 2.2, 0.24, fc=GH[0], ec="none"))
    ax.text(14.35, 6.15, "篇", fontsize=11, color=MUTED); ax.text(15.05, 6.15, "强验证", fontsize=11, color=MUTED)
    ax.text(16.9, 6.15, "自主性构成", fontsize=11, color=MUTED)
    for t, (a, b) in zip(ERA_TICK[2:], [(2013, 2019), (2020, 2023), (2024, 2026)]):
        x0, x1 = a - 2013 + 0.08, b - 2013 + 0.92
        ax.plot([x0, x1], [6.32, 6.32], color=MUTED, lw=1.5); ax.text((x0 + x1) / 2, 6.45, t, ha="center", fontsize=12,
                                                                      color=INK, fontweight="bold")
    ax.set_xlim(-0.1, 19.2); ax.set_ylim(-0.1, 6.9); ax.set_aspect("equal")
    ax.set_yticks([5.5 - k for k in range(6)], O_T, fontsize=12); ax.set_xticks([j + 0.5 for j in range(14)], YRS, fontsize=11)
    ax.tick_params(length=0); ax.spines[:].set_visible(False)
    # legend row, GitHub style
    lx = 0.11
    fig.text(lx, 0.075, "少", fontsize=11, color=MUTED, va="center")
    for k, c in enumerate(GH):
        fig.patches.append(FancyBboxPatch((lx + 0.018 + k * 0.017, 0.064), 0.013, 0.024, boxstyle="round,pad=0,rounding_size=0.002",
                                          fc=c, ec="none", transform=fig.transFigure, figure=fig))
    fig.text(lx + 0.108, 0.075, "多　（0 / 1 / 2–3 / 4–9 / ≥10 篇）", fontsize=11, color=MUTED, va="center")
    fig.text(lx + 0.33, 0.075, "●", color=ACC, fontsize=15, va="center")
    fig.text(lx + 0.345, 0.075, "红点 = 该格有强验证，点越大强验证占比越高；格内数字 = 论文数　·　≤2012 本学科无论文", fontsize=11, color=MUTED, va="center")
    lkey(fig, x=0.11, y=0.025)
    head(fig, f, "贡献热力图：每个开放度一行", "列 = 年份，绿色深浅 = 论文数，红点 = 强验证；右侧 = 合计与自主性构成　·　灵感：GitHub contribution graph", pp)
    save(fig, 1, "contrib", f)


def d2(pp, f):
    """GitHub punch card."""
    n, s, blank = stats(pp)
    fig, ax = plt.subplots(figsize=(16, 10)); fig.subplots_adjust(0.15, 0.1, 0.84, 0.82)
    cell = C.defaultdict(list)
    for p in pp:
        cell[(p["o"], p["v"])].append(p["l"])
    top = max(len(v) for v in cell.values())
    ax.add_patch(Rectangle((2.5, 0.45), 2.1, 6.5, fc="#fbefeb", ec="none", zorder=0))
    ax.text(3.5, 0.25, "强验证 V3–V4", ha="center", color=ACC, fontsize=12, fontweight="bold")
    for o in range(1, 7):
        ax.plot([-0.6, 4.6], [o, o], color=LINE, lw=1, zorder=1)
        for v in range(5):
            ax.plot([v, v], [o - 0.09, o + 0.09], color="#c9c6c0", lw=1, zorder=1)
            ls = cell.get((o, v))
            if not ls:
                continue
            cc = C.Counter(ls); dom = cc.most_common(1)[0][0]
            area = 6500 * len(ls) / top; rp = np.sqrt(area / np.pi)          # radius in points
            ax.scatter([v], [o], s=area, c=L_COL[dom], edgecolors="white", linewidths=1.5, zorder=3)
            ax.annotate(f"{len(ls)}", (v, o), xytext=(rp + 5, 0), textcoords="offset points", fontsize=12,
                        va="center", color=INK, fontweight="bold", zorder=4)
            if cc[dom] < len(ls):
                ax.annotate(f"其余 {len(ls) - cc[dom]}", (v, o), xytext=(rp + 5, -15), textcoords="offset points",
                            fontsize=9, va="center", color=MUTED, zorder=4)
        ax.text(4.95, o, f"{s[o]}/{n[o]}" if s[o] else f"0/{n[o]}  {blank_tag(o, n)}", va="center", fontsize=12,
                color=ACC if not s[o] else INK, fontweight="bold")
    ax.text(4.95, 0.25, "强验证 / 全部", fontsize=11, color=MUTED)
    for v in range(5):
        nv = sum(p["v"] == v for p in pp)
        ax.text(v, 6.75, f"{nv} 篇", ha="center", fontsize=11, color=ACC if v >= 3 else MUTED)
    ax.set_xlim(-0.6, 6.4)
    ax.set_xticks(range(5), V_T, fontsize=12); ax.set_yticks(range(1, 7), O_T, fontsize=12)
    ax.xaxis.tick_top(); ax.tick_params(length=0, pad=22); ax.set_ylim(7.0, 0.0)
    ax.spines[:].set_visible(False)
    lkey(fig)
    fig.text(0.6, 0.035, "圆面积 ∝ 论文数，颜色 = 该格占多数的自主性；“其余” = 其他自主性的篇数", fontsize=11, color=MUTED)
    head(fig, f, "打卡图：开放度 × 验证强度", "每个点 = 一格的论文；粉色带 = 强验证　·　灵感：GitHub punch card", pp)
    save(fig, 2, "punchcard", f)


TILE = "#f5f5f7"                                                     # Apple tile grey


def tile(fig, c, r, w, h, nc=4, nr=3, box=(0.04, 0.05, 0.96, 0.86), gap=0.012):
    """Axes for a bento tile spanning columns c..c+w-1, rows r..r+h-1 (row 0 = top), with a rounded grey card."""
    x0, y0, x1, y1 = box; cw = (x1 - x0 - gap * (nc - 1)) / nc; rh = (y1 - y0 - gap * (nr - 1)) / nr
    L = x0 + c * (cw + gap); B = y1 - (r + h) * rh - (r + h - 1) * gap; W = w * cw + (w - 1) * gap; H = h * rh + (h - 1) * gap
    fig.patches.append(FancyBboxPatch((L, B), W, H, boxstyle="round,pad=0,rounding_size=0.012", fc=TILE, ec="none",
                                      transform=fig.transFigure, figure=fig, zorder=-10, mutation_aspect=1.6))
    ax = fig.add_axes([L, B, W, H]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off"); ax.patch.set_alpha(0)
    return ax


def d3(pp, f):
    """Apple keynote bento grid."""
    n, s, blank = stats(pp); N = len(pp); ns = sum(s.values())
    fig = plt.figure(figsize=(16, 10))
    # hero: total + papers per year
    ax = tile(fig, 0, 0, 2, 2)
    ax.text(0.06, 0.88, "化学 · 论文", fontsize=16, color=MUTED, va="top")
    ax.text(0.05, 0.80, f"{N}", fontsize=110, fontweight="bold", color=INK, va="top")
    ax.text(0.41, 0.62, "篇", fontsize=30, fontweight="bold", color=INK)
    cy = C.Counter(p["year"] for p in pp); cs = C.Counter(p["year"] for p in pp if p["v"] >= 3)
    top = max(cy.values()); bw = 0.88 / len(YRS)
    for j, y in enumerate(YRS):
        x = 0.06 + j * bw; h = 0.46 * cy[y] / top; hs = 0.46 * cs[y] / top
        if cy[y]:
            rbox(ax, x, 0.1, bw * 0.78, h, "#d2d2d7", r=0.006)
        if cs[y]:
            rbox(ax, x, 0.1, bw * 0.78, hs, ACC, r=0.006, z=2)
        if y in (2013, 2020, 2024, 2026):
            ax.text(x + bw * 0.39, 0.05, str(y), ha="center", fontsize=10, color=MUTED)
    ax.text(0.94, 0.88, f"2024–2026 占 {sum(p['year'] >= 2024 for p in pp) / N:.0%}", ha="right", va="top",
            fontsize=14, color=INK, fontweight="bold")
    ax.text(0.94, 0.82, "灰 = 全部　红 = 强验证", ha="right", va="top", fontsize=11, color=MUTED)
    # strong: donut
    ax = tile(fig, 2, 0, 1, 1)
    ax.text(0.08, 0.86, "强验证 V3–V4", fontsize=14, color=MUTED, va="top")
    ax.text(0.08, 0.66, f"{ns}", fontsize=64, fontweight="bold", color=ACC, va="top")
    ax.text(0.08, 0.14, f"占全部 {ns / N:.0%}", fontsize=14, color=INK, fontweight="bold")
    ax2 = ax.inset_axes([0.55, 0.12, 0.42, 0.66]); ax2.set_aspect("equal"); ax2.axis("off")
    ax2.add_patch(Wedge((0, 0), 1, 0, 360, width=0.26, fc="#e3e3e8"))
    ax2.add_patch(Wedge((0, 0), 1, 90 - 360 * ns / N, 90, width=0.26, fc=ACC))
    ax2.set_xlim(-1.05, 1.05); ax2.set_ylim(-1.05, 1.05)
    # blanks
    ax = tile(fig, 3, 0, 1, 1)
    ax.text(0.08, 0.86, "空白（无强验证）", fontsize=14, color=MUTED, va="top")
    ax.text(0.08, 0.66, "·".join(f"O{o}" for o in blank), fontsize=56, fontweight="bold", color=ACC, va="top")
    for k, o in enumerate(blank):
        ax.text(0.08, 0.26 - 0.13 * k, f"O{o} {O_T[o - 1][3:]}　" + ("无论文" if not n[o] else f"{n[o]} 篇，全为声明"),
                fontsize=12.5, color=INK)
    # O bars
    ax = tile(fig, 2, 1, 2, 1)
    ax.text(0.04, 0.86, "开放度分布", fontsize=14, color=MUTED, va="top")
    mo = max(n.values())
    for o in range(1, 7):
        y = 0.70 - (o - 1) * 0.122
        ax.text(0.04, y, O_T[o - 1], fontsize=12, va="center", color=INK)
        rbox(ax, 0.25, y - 0.04, 0.6, 0.08, "#e3e3e8", r=0.01)
        if n[o]:
            rbox(ax, 0.25, y - 0.04, 0.6 * n[o] / mo, 0.08, "#86868b", r=0.01, z=2)
        if s[o]:
            rbox(ax, 0.25, y - 0.04, 0.6 * s[o] / mo, 0.08, ACC, r=0.01, z=3)
        ax.text(0.87, y, f"{s[o]}/{n[o]}" if s[o] else "空白", fontsize=12, va="center", fontweight="bold",
                color=ACC if not s[o] else INK)
    # autonomy
    ax = tile(fig, 0, 2, 1, 1)
    nl = C.Counter(p["l"] for p in pp); dl = nl.most_common(1)[0][0]
    ax.text(0.08, 0.86, "主流自主性", fontsize=14, color=MUTED, va="top")
    ax.text(0.08, 0.68, f"L{dl}", fontsize=56, fontweight="bold", color=L_COL[dl], va="top")
    ax.text(0.47, 0.50, f"{nl[dl] / N:.0%}\n{L_NAME[dl][3:]}", fontsize=15, color=INK, fontweight="bold", va="center")
    x = 0.08
    for l in range(4):
        w = 0.84 * nl[l] / N
        if w:
            ax.add_patch(Rectangle((x, 0.14), w, 0.08, fc=L_COL[l], ec=TILE, lw=1.5))
            if w > 0.08:
                ax.text(x + w / 2, 0.06, f"L{l} {nl[l]}", ha="center", fontsize=10.5, color=L_COL[l], fontweight="bold")
        x += w
    # frontier
    ax = tile(fig, 1, 2, 1, 1)
    fo = max(o for o in range(1, 7) if s[o]); fy = min(p["year"] for p in pp if p["o"] == fo and p["v"] >= 3)
    ax.text(0.08, 0.86, "强验证前沿", fontsize=14, color=MUTED, va="top")
    ax.text(0.08, 0.68, f"O{fo}", fontsize=56, fontweight="bold", color=INK, va="top")
    ax.text(0.47, 0.50, f"{O_T[fo - 1][3:]}\n{s[fo]} 篇 · 首次 {fy}", fontsize=14, color=INK, fontweight="bold", va="center")
    for o in range(1, 7):
        ax.scatter([0.12 + (o - 1) * 0.15], [0.17], s=420, c=ACC if s[o] else "#d2d2d7", edgecolors="none")
        ax.text(0.12 + (o - 1) * 0.15, 0.04, f"O{o}", ha="center", fontsize=10, color=MUTED)
    # verification
    ax = tile(fig, 2, 2, 1, 1)
    nv = C.Counter(p["v"] for p in pp)
    ax.text(0.08, 0.86, "验证强度", fontsize=14, color=MUTED, va="top")
    mv = max(nv.values())
    for v in range(5):
        h = 0.5 * nv[v] / mv; x = 0.1 + v * 0.17
        rbox(ax, x, 0.14, 0.12, max(h, 0.005), ACC if v >= 3 else "#86868b", r=0.012)
        ax.text(x + 0.06, 0.16 + h, str(nv[v]), ha="center", fontsize=12, fontweight="bold", color=ACC if v >= 3 else INK)
        ax.text(x + 0.06, 0.05, f"V{v}", ha="center", fontsize=11, color=MUTED)
    # eras
    ax = tile(fig, 3, 2, 1, 1)
    ne = C.Counter(p["era"] for p in pp); se = C.Counter(p["era"] for p in pp if p["v"] >= 3)
    ax.text(0.08, 0.86, "时代", fontsize=14, color=MUTED, va="top")
    for k, e in enumerate(range(2, 5)):
        y = 0.62 - k * 0.2
        ax.text(0.08, y, ERA_TICK[e], fontsize=12, va="center", color=INK)
        ax.text(0.92, y, f"{ne[e]} 篇 · 强 {se[e]}", fontsize=12.5, va="center", ha="right", fontweight="bold",
                color=INK)
    ax.text(0.08, 0.08, "≤2012：本学科无论文", fontsize=11, color=MUTED)
    head(fig, f, "一页看懂", "主题演讲式便当格：一格一个数字　·　灵感：Apple keynote bento grid", pp)
    save(fig, 3, "bento", f)


CLAIM, TRACK = "#bdb8ae", "#efede8"                                  # claims arc, empty track (house neutrals)
RP, RW, SW, SG = 0.15, 0.1, 0.024, 0.008                            # ring pitch, ring width, L sub-ring width and gap


def ring(ax, cx, cy, r, w, a0, a1, col, z=2, caps=True):
    """Arc from fraction a0 to a1 of a full turn, clockwise from 12 o'clock, optionally with round caps."""
    if a1 <= a0:
        return
    t0, t1 = 90 - 360 * min(a1, 0.999), 90 - 360 * a0
    ax.add_patch(Wedge((cx, cy), r + w / 2, t0, t1, width=w, fc=col, ec="none", zorder=z))
    if caps:
        for a in (t0, t1):
            t = np.deg2rad(a)
            ax.add_patch(Circle((cx + r * np.cos(t), cy + r * np.sin(t)), w / 2, fc=col, ec="none", zorder=z))


def nice_full(m):
    """Papers in a full turn: the largest ring stops at <= 85% so the 12 o'clock gap can carry the O labels."""
    step = 10 if m > 20 else 5 if m > 5 else 1
    return max(1, int(np.ceil(m / 0.85 / step)) * step)


def rings(ax, pp, full, labels=True):
    """One ring per O level (O6 outermost): grey = claims, red = strong (drawn first, from 12 o'clock).
    A thin outer sub-ring is aligned paper by paper with the main ring and coloured by autonomy."""
    for o in range(1, 7):
        r = 1.0 - (6 - o) * RP
        ps = sorted((p for p in pp if p["o"] == o), key=lambda p: (p["v"] < 3, p["l"]))
        k = len(ps); ks = sum(p["v"] >= 3 for p in ps)
        ax.add_patch(Wedge((0, 0), r + RW / 2, 0, 360, width=RW, fc=TRACK, ec="none", zorder=1))
        ring(ax, 0, 0, r, RW, 0, k / full, CLAIM, z=2)
        ring(ax, 0, 0, r, RW, 0, ks / full, ACC, z=3)
        rs = r + RW / 2 + SG + SW / 2; i = 0                          # L sub-ring, run-length by (strong, L)
        while i < k:
            j = i
            while j < k and (ps[j]["v"] >= 3, ps[j]["l"]) == (ps[i]["v"] >= 3, ps[i]["l"]):
                j += 1
            ring(ax, 0, 0, rs, SW, i / full, j / full, L_COL[ps[i]["l"]], z=2, caps=False)
            i = j
        if labels:                                                    # O label in the 12 o'clock gap
            th = np.deg2rad(90 + np.rad2deg((RW / 2 + 0.07) / r))
            ax.text(r * np.cos(th), r * np.sin(th), f"O{o}", ha="center", va="center", fontsize=12,
                    fontweight="bold", color=INK if k else "#a8a397", zorder=5)


def d4(pp, f):
    """Activity rings, house palette: red = strong, grey = claims, thin outer sub-ring = autonomy."""
    n, s, blank = stats(pp); full = nice_full(max(n.values()) if n else 1)
    tag = lambda o: "无论文" if not n[o] else "空白（仅声明）" if not s[o] else ""
    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_axes([0.02, 0.07, 0.52, 0.8]); ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(-1.12, 1.12); ax.set_ylim(-1.12, 1.12)
    rings(ax, pp, full)
    ax.text(0, 0.035, f"{len(pp)}", ha="center", va="center", fontsize=30, fontweight="bold", color=INK)
    ax.text(0, -0.1, "篇", ha="center", va="center", fontsize=13, color=MUTED)
    # Fitness-style list
    X0 = 0.565
    fig.text(X0, 0.865, "开放度", fontsize=12, color=MUTED); fig.text(0.715, 0.865, "强验证 / 全部", fontsize=12, color=MUTED)
    for o in range(6, 0, -1):
        y = 0.81 - (6 - o) * 0.066
        fig.text(X0, y, O_T[o - 1], fontsize=15, fontweight="bold", color=INK if n[o] else "#a8a397", va="center")
        fig.text(0.715, y, f"{s[o]}", fontsize=24, fontweight="bold", color=ACC if s[o] else "#a8a397", va="center")
        fig.text(0.715 + 0.012 * len(str(s[o])) + 0.006, y, f"/ {n[o]} 篇", fontsize=15, color=MUTED, va="center")
        if tag(o):
            fig.text(0.815, y, tag(o), fontsize=13, fontweight="bold", color=ACC if n[o] else MUTED, va="center")
    # encoding key
    y = 0.425
    for col, t in [(ACC, "强验证（V3–V4）"), (CLAIM, "仅声明（V0–V2）"), (TRACK, f"空轨道（整圈 {full} 篇）")]:
        fig.patches.append(FancyBboxPatch((X0, y - 0.008), 0.02, 0.016, boxstyle="round,pad=0,rounding_size=0.006",
                                          fc=col, ec="#d8d4cc" if col == TRACK else "none", lw=0.6,
                                          transform=fig.transFigure, figure=fig))
        fig.text(X0 + 0.026, y, t, fontsize=12.5, color=INK, va="center"); X0 += 0.128
    X0 = 0.565; fig.text(X0, 0.385, "外侧细环 = 自主性，与主环逐篇对齐（红弧下方即强验证论文的自主性）", fontsize=12.5,
                         color=INK, va="center")
    for l in range(4):
        fig.text(X0 + 0.098 * l, 0.35, f"● {L_NAME[l]}", fontsize=12.5, fontweight="bold", color=L_COL[l], va="center")
    # era rings, cumulative
    fig.text(X0, 0.3, "累计到各时代末", fontsize=13, color=INK, fontweight="bold", va="center")
    for k, e in enumerate(range(2, 5)):
        a = fig.add_axes([X0 - 0.01 + k * 0.145, 0.05, 0.145, 0.19]); a.set_aspect("equal"); a.axis("off")
        a.set_xlim(-1.12, 1.12); a.set_ylim(-1.12, 1.12)
        sub = [p for p in pp if p["era"] <= e]
        rings(a, sub, full, labels=False)
        a.text(0, 0, f"{len(sub)}", ha="center", va="center", fontsize=13, fontweight="bold", color=INK)
        nsub = sum(p["v"] >= 3 for p in sub)
        fig.text(X0 - 0.01 + k * 0.145 + 0.0725, 0.255, f"截至 {ERA_TICK[e][-4:]}", ha="center", fontsize=13, color=INK,
                 va="center")
        fig.text(X0 - 0.01 + k * 0.145 + 0.0725, 0.03, f"强 {nsub} / {len(sub)} 篇", ha="center", fontsize=12,
                 color=ACC if nsub else MUTED, va="center", fontweight="bold")
    head(fig, f, "活动圆环：每个开放度一环",
         "外环 O6 → 内环 O1；红弧 = 强验证，灰弧 = 仅声明，外侧细环 = 自主性　·　灵感：Apple Watch activity rings", pp)
    save(fig, 4, "rings", f)


def d5(pp, f):
    """Swimlane timeline."""
    n, s, blank = stats(pp)
    fig, ax = plt.subplots(figsize=(16, 9.5)); fig.subplots_adjust(0.12, 0.1, 0.84, 0.85)
    ppy = 0.72 * 16 * 72 / 14.2                                        # points per year on the x axis
    cell = C.defaultdict(list)
    for p in pp:
        cell[(p["o"], p["year"])].append(p)
    for o in range(1, 7):
        y = 6 - o
        rbox(ax, 2012.45, y + 0.06, 14.1, 0.88, "#f7f7f5" if o % 2 else "#efeeeb", r=0.08, z=0)
        ax.text(2026.75, y + 0.62, f"{n[o]} 篇", fontsize=13, fontweight="bold", color=INK, va="center")
        ax.text(2026.75, y + 0.32, f"强验证 {s[o]}" if s[o] else blank_tag(o, n), fontsize=11.5, fontweight="bold",
                color=ACC, va="center")
    for (o, yr), ps in cell.items():
        ps.sort(key=lambda p: (-(p["v"] >= 3), p["l"], -p["v"]))
        k = len(ps); W = min(0.84, 0.12 * k)
        for i, p in enumerate(ps):
            x = yr - W / 2 + (i + 0.5) * W / k; y = 6 - o + 0.14
            h = 0.6 if p["v"] >= 3 else 0.26
            ax.plot([x, x], [y, y + h], color=L_COL[p["l"]], lw=min(2.4, 0.6 * ppy * W / k), solid_capstyle="butt", zorder=3)
        if k >= 5:
            ax.text(yr, 6 - o + 0.93, str(k), ha="center", va="top", fontsize=8.5, color=MUTED, zorder=4)
    for t, (a, b) in zip(ERA_TICK[2:], [(2013, 2019), (2020, 2023), (2024, 2026)]):
        rbox(ax, a - 0.45, 6.18, b - a + 0.9, 0.34, "#1d1d1b", r=0.12, z=2)
        ax.text((a + b) / 2, 6.35, t, ha="center", va="center", fontsize=11.5, color="white", fontweight="bold", zorder=3)
        if a > 2013:
            ax.axvline(a - 0.5, color="#cfccc6", lw=1, ls=(0, (2, 3)), zorder=1, ymax=0.9)
    ax.text(2012.5, 6.72, "≤2012：本学科无论文", fontsize=10.5, color="#a8a397")
    ax.set_xlim(2012.4, 2026.6); ax.set_ylim(-0.05, 6.9)
    ax.set_xticks(YRS, YRS, fontsize=11); ax.set_yticks([5.5 - k for k in range(6)], O_T, fontsize=12.5)
    ax.tick_params(length=0); ax.spines[:].set_visible(False); ax.set_clip_on(False)
    lkey(fig)
    fig.text(0.56, 0.035, "▌高竖线 = 强验证（V3–V4）　╻矮竖线 = 仅声明　·　格上数字 = 当年该泳道篇数", fontsize=11, color=MUTED)
    head(fig, f, "泳道时间线：一篇论文一根刻线", "泳道 = 开放度，横轴 = 年份；高刻线 = 强验证，颜色 = 自主性　·　灵感：swimlane timeline / Linear roadmap", pp)
    save(fig, 5, "swimlane", f)


def d6(pp, f):
    """Barcode / DNA strip."""
    n, s, blank = stats(pp)
    fig, ax = plt.subplots(figsize=(16, 9.5)); fig.subplots_adjust(0.12, 0.12, 0.97, 0.82)
    G = 2.0                                                            # gap between eras, in bars

    def strip(ps, y, h, label_eras):
        ps = sorted(ps, key=lambda p: (p["year"], p["v"])); x = 0.0; last = None; seg = {}
        for p in ps:
            if last is not None and p["era"] != last:
                x += G
            seg.setdefault(p["era"], [x, x]); seg[p["era"]][1] = x + 1
            ax.add_patch(Rectangle((x + 0.08, y), 0.84, h, fc=V_COL[p["v"]], ec="none", zorder=2))
            x += 1; last = p["era"]
        if label_eras:
            for e, (a, b) in seg.items():
                ax.plot([a + 0.1, b - 0.1], [y - 0.08, y - 0.08], color=MUTED, lw=1.2)
                if b - a >= 4:
                    ax.text((a + b) / 2, y - 0.14, ERA_TICK[e], ha="center", va="top", fontsize=9.5, color=MUTED)
        return x

    end = strip(pp, 6.35, 0.75, True)
    ax.text(end + 1.5, 6.73, f"全部 {len(pp)} 篇", fontsize=13, fontweight="bold", va="center", color=INK)
    ax.text(end + 1.5, 6.47, f"强验证 {sum(s.values())}", fontsize=11.5, fontweight="bold", va="center", color=ACC)
    for o in range(1, 7):
        y = 5.6 - o * 0.92
        ps = [p for p in pp if p["o"] == o]
        if ps:
            e = strip(ps, y, 0.62, True)
        else:
            ax.plot([0, 6], [y + 0.31, y + 0.31], color="#d8d4cc", lw=1.2, ls=(0, (2, 2))); e = 6
        ax.text(e + 1.5, y + 0.45, f"{n[o]} 篇", fontsize=12.5, fontweight="bold", va="center", color=INK)
        ax.text(e + 1.5, y + 0.17, f"强验证 {s[o]}（{s[o] / n[o]:.0%}）" if s[o] else blank_tag(o, n), fontsize=11,
                fontweight="bold", va="center", color=ACC)
    ax.set_xlim(-1, end + 14); ax.set_ylim(-0.15, 7.2)
    ax.set_yticks([6.72] + [5.6 - o * 0.92 + 0.31 for o in range(1, 7)], ["全部"] + O_T, fontsize=12.5)
    ax.set_xticks([]); ax.tick_params(length=0); ax.spines[:].set_visible(False)
    for v in range(5):
        x = 0.12 + v * 0.13
        fig.patches.append(Rectangle((x, 0.045), 0.012, 0.035, fc=V_COL[v], ec="none", transform=fig.transFigure, figure=fig))
        fig.text(x + 0.017, 0.062, V_T[v], fontsize=11.5, va="center", color=ACC if v >= 3 else INK,
                 fontweight="bold" if v >= 3 else "normal")
    fig.text(0.79, 0.062, "一根竖条 = 一篇，按年份排序", fontsize=11, color=MUTED, va="center")
    head(fig, f, "条形码：每个开放度一条 DNA", "竖条颜色 = 验证强度（蓝 = 仅声明，红 = 强验证），时代之间留空　·　灵感：barcode / DNA strip", pp)
    save(fig, 6, "barcode", f)


def radar(ax, ps, col, title):
    N = len(ps)
    a = np.array([sum(p["o"] == o for p in ps) for o in range(1, 7)]) / max(N, 1)
    b = np.array([sum(p["o"] == o and p["v"] >= 3 for p in ps) for o in range(1, 7)]) / max(N, 1)
    rmax = max(np.ceil(a.max() * 4) / 4, 0.25)
    th = np.pi / 2 - np.arange(6) * 2 * np.pi / 6; th_c = np.r_[th, th[:1]]
    ax.set_theta_zero_location("E"); ax.set_ylim(0, rmax); ax.set_xticks(th % (2 * np.pi))
    ax.set_xticklabels([f"O{k}" for k in range(1, 7)], fontsize=11, color=INK)
    ax.set_yticks(np.arange(0.25, rmax + 0.01, 0.25)); ax.set_yticklabels([]); ax.spines["polar"].set_color(LINE)
    ax.grid(color=LINE, lw=0.8)
    ax.set_title(title, fontsize=14, color=col, fontweight="bold", pad=32)
    if not N:
        ax.text(0, 0, "无论文", ha="center", va="center", fontsize=14, color="#a8a397"); return
    ax.text(np.deg2rad(75), rmax * 1.0, f"{rmax:.0%}", fontsize=8.5, color=MUTED, ha="left", va="bottom")
    ax.fill(th_c, np.r_[a, a[:1]], color=col, alpha=0.18, zorder=2); ax.plot(th_c, np.r_[a, a[:1]], color=col, lw=2.2, zorder=3)
    ax.fill(th_c, np.r_[b, b[:1]], color=ACC, alpha=0.55, zorder=4); ax.plot(th_c, np.r_[b, b[:1]], color=ACC, lw=1.4, zorder=5)
    ax.scatter(th, a, s=22, color=col, zorder=6)


def d7(pp, f):
    """Radar small multiples, one per autonomy level."""
    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_axes([0.05, 0.12, 0.38, 0.62], projection="polar")
    ns = sum(p["v"] >= 3 for p in pp)
    radar(ax, pp, INK, f"全部　{len(pp)} 篇 · 强验证 {ns}")
    for l in range(4):
        r, c = divmod(l, 2)
        a = fig.add_axes([0.5 + c * 0.25, 0.5 - r * 0.42, 0.2, 0.27], projection="polar")
        ps = [p for p in pp if p["l"] == l]
        radar(a, ps, L_COL[l], f"{L_NAME[l]}　{len(ps)} 篇 · 强 {sum(p['v'] >= 3 for p in ps)}")
    fig.text(0.05, 0.04, f"半径 = 该组论文落在各开放度的占比（同心圈每 25%，外圈数值标在 O1–O2 之间，各图刻度不同）；"
             "彩色轮廓 = 全部论文，红色填充 = 其中强验证（V3–V4）", fontsize=11.5, color=MUTED)
    head(fig, f, "雷达小图：每种自主性的开放度轮廓", "红色 = 强验证；O1、O2 方向没有红色即空白　·　灵感：radar small multiples / 游戏角色能力图", pp)
    save(fig, 7, "radar", f)


MONO = ["Menlo", "Arial Unicode MS"]
SH_L = "#555555"                                                      # shields.io label grey
SH = dict(green="#4c1", yellowgreen="#a4a61d", yellow="#dfb317", orange="#fe7d37", red="#e05d44", blue="#007ec6",
          grey="#9f9f9f")


def tw(s, fs):
    """Approximate text width in inches (CJK = 1 em, other glyphs ~0.6 em)."""
    return sum(1.0 if ord(c) > 0x2E80 else 0.6 for c in s) * fs / 72


def badge(ax, x, y, left, right, col, fs=11, h=0.3):
    """A shields.io flat badge at (x, y) in inches (bottom-left); returns its right edge."""
    pad = 0.09; wl = tw(left, fs) + 2 * pad; wr = tw(right, fs) + 2 * pad
    rbox(ax, x, y, wl + wr, h, col, r=0.05, z=2)
    rbox(ax, x, y, wl, h, SH_L, r=0.05, z=3); ax.add_patch(Rectangle((x + wl - 0.06, y), 0.06, h, fc=SH_L, ec="none", zorder=3))
    ax.text(x + wl / 2, y + h / 2, left, ha="center", va="center", fontsize=fs, color="white", zorder=4)
    ax.text(x + wl + wr / 2, y + h / 2, right, ha="center", va="center", fontsize=fs, color="white", zorder=4,
            fontweight="bold")
    return x + wl + wr


def cover(share):
    return SH["red"] if share == 0 else SH["orange"] if share < 0.3 else SH["yellow"] if share < 0.5 else \
        SH["yellowgreen"] if share < 0.7 else SH["green"]


def d8(pp, f):
    """README badge infographic."""
    n, s, blank = stats(pp); N = len(pp); ns = sum(s.values())
    fig = plt.figure(figsize=(16, 10)); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 16); ax.set_ylim(0, 10); ax.axis("off")
    # repo header
    ax.text(0.64, 8.25, f"agent-science / {FZH[f]}", fontsize=17, fontweight="bold", color="#0969da", fontfamily=MONO)
    nl = C.Counter(p["l"] for p in pp); dl = nl.most_common(1)[0][0]
    fo = max(o for o in range(1, 7) if s[o])
    x = 0.64
    for l_, r_, c_ in [("papers", f"{N}", SH["blue"]), ("强验证 V3–V4", f"{ns} · {ns / N:.0%}", cover(ns / N)),
                       ("空白", " · ".join(f"O{o}" for o in blank), SH["red"]), ("前沿", f"O{fo}", SH["green"]),
                       ("自主性", f"L{dl} · {nl[dl] / N:.0%}", L_COL[dl]),
                       ("2024–2026", f"{sum(p['year'] >= 2024 for p in pp) / N:.0%}", SH["grey"])]:
        x = badge(ax, x, 7.62, l_, r_, c_, fs=12, h=0.36) + 0.14
    # language bar = autonomy mix
    x = 0.64; W = 14.7
    for l in range(4):
        w = W * nl[l] / N
        if w:
            ax.add_patch(Rectangle((x, 7.2), w, 0.12, fc=L_COL[l], ec="white", lw=1.5, zorder=2))
        x += w
    x = 0.64
    for l in range(4):
        ax.add_patch(Circle((x + 0.07, 6.93), 0.06, fc=L_COL[l], ec="none"))
        ax.text(x + 0.2, 6.93, f"{L_NAME[l]}", fontsize=11.5, fontweight="bold", color=INK, va="center")
        ax.text(x + 0.2 + tw(L_NAME[l], 11.5) + 0.1, 6.93, f"{nl[l] / N:.1%}", fontsize=11.5, color=MUTED, va="center")
        x += 2.6
    # terminal line
    ax.add_patch(Rectangle((0.64, 6.38), W, 0.012, fc=LINE, ec="none"))
    ax.text(0.64, 6.08, f"$ ovl stats --field {f} --by openness --since 2013", fontsize=12, color=MUTED, fontfamily=MONO, va="center")
    cols = [0.64, 3.35, 5.0, 8.0, 12.6]
    for c_, t_ in zip(cols, ["开放度", "论文", "强验证", f"每年论文 2013 → 2026（红 = 强验证）", "自主性构成"]):
        ax.text(c_, 5.68, t_, fontsize=11, color=MUTED, va="center")
    cy = {o: C.Counter(p["year"] for p in pp if p["o"] == o) for o in range(1, 7)}
    cs = {o: C.Counter(p["year"] for p in pp if p["o"] == o and p["v"] >= 3) for o in range(1, 7)}
    top = max(max(c.values()) for c in cy.values() if c)
    for o in range(1, 7):
        y = 5.0 - (o - 1) * 0.82
        ax.add_patch(Rectangle((0.64, y - 0.2), W, 0.008, fc="#f0efec", ec="none"))
        badge(ax, 0.64, y, f"O{o}", O_T[o - 1][3:], "#24292f", fs=11.5)
        badge(ax, 3.35, y, "papers", f"{n[o]}", SH["blue"] if n[o] else SH["grey"], fs=11.5)
        badge(ax, 5.0, y, "strong", f"{s[o]} · {s[o] / n[o]:.0%}" if s[o] else ("空白 · 无论文" if not n[o] else "空白 · 仅声明"),
              cover(s[o] / n[o]) if n[o] else SH["red"], fs=11.5)
        # sparkline bars per year
        bw = 4.2 / len(YRS)
        for j, yr in enumerate(YRS):
            bx = 8.0 + j * bw; k = cy[o][yr]; ks = cs[o][yr]
            ax.add_patch(Rectangle((bx, y + 0.02), bw * 0.7, 0.012, fc="#d0d7de", ec="none"))
            if k:
                hh = 0.55 * np.sqrt(k / top)
                ax.add_patch(Rectangle((bx, y + 0.02), bw * 0.7, hh, fc="#8c959f", ec="none", zorder=2))
                if ks:
                    ax.add_patch(Rectangle((bx, y + 0.02), bw * 0.7, hh * ks / k, fc=ACC, ec="none", zorder=3))
        # autonomy bar
        xx = 12.6
        for l in range(4):
            w = 2.7 * sum(p["o"] == o and p["l"] == l for p in pp) / max(n[o], 1)
            if w:
                ax.add_patch(Rectangle((xx, y + 0.09), w, 0.12, fc=L_COL[l], ec="white", lw=1.2, zorder=2))
            xx += w
        if not n[o]:
            ax.add_patch(Rectangle((12.6, y + 0.09), 2.7, 0.12, fc="#eaeef2", ec="none"))
    for yr in (2013, 2020, 2024, 2026):
        ax.text(8.0 + (yr - 2013) * 4.2 / len(YRS) + 0.1, 0.62, str(yr), fontsize=9.5, color=MUTED, ha="center",
                fontfamily=MONO)
    ax.text(0.64, 0.3, "徽章颜色按强验证占比：红 = 0（空白）· 橙 <30% · 黄 <50% · 黄绿 <70% · 绿 ≥70%；柱高 ∝ √篇数",
            fontsize=11, color=MUTED)
    head(fig, f, "README 徽章：一行一个开放度", "shields 风格徽章 + 每年迷你柱 + 自主性语言条　·　灵感：GitHub README badges (shields.io) / language bar", pp)
    save(fig, 8, "badges", f)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--all"]; f = (args or ["03"])[0]; pp = load(f)
    for d in ((d1, d2, d3, d4, d5, d6, d7, d8) if "--all" in sys.argv else (d4,)):
        d(pp, f)
