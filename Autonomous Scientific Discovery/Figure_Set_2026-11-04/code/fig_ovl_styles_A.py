"""Group A design study: eight data-art / design-studio styles for one field's openness x verification x autonomy data.

  a1 flowers  : one flower per paper (Lupi, data humanism): petals = O, stem height = V, colour = L, in year order
  a2 spiral   : radial spiral timeline (Bremer): papers along a spiral in time order, lane = O, filled = strong
  a3 pods     : organic pods per O level (Fragapane): pods above the waterline = strong (V3-V4), below = claims
  a4 isotype  : Isotype pictogram rows (Neurath): rows = O, one page icon per paper, solid = strong, outline = claim
  a5 packing  : circle packing O -> V -> papers, papers coloured by L; inside every O circle V increases left to right
  a6 treemap  : squarified treemap O -> V -> L, strong blocks saturated with a red border
  a7 sunburst : sunburst O -> V -> L, red outer arcs = strongly verified share, dashed = blank
  a8 hexes    : hex mosaic O x V, a donut of L composition inside each hex, red coast = strong verification
Data: ov_coding/increment/classification_results_662.jsonl via fig_ovl_frontier_mountain.load.
Only a5 was shortlisted. Usage: python3 fig_ovl_styles_A.py [field] (default 03) -> out/styles/shortlist/A5_packing_f{field}.png;
add --all to also render the seven rejected styles to out/styles/A{n}_{name}_f{field}.png
"""
import sys, itertools as IT, collections as C
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Circle, Wedge, Rectangle, RegularPolygon, PathPatch
from matplotlib.path import Path
from matplotlib.lines import Line2D
import style as S
from fig_ovl_frontier_mountain import load, ERAS, ERA_TICK
from fig_ovl_surface import INK, MUTED, ACC, L_COL, L_NAME, FZH, ALT
from fig_ovl_modes import O_T, V_T, head, lkey

OUT = S.ROOT / "out" / "styles"
FAINT, CLAIM = "#b5ae9f", "#8fa6b3"
plt.rcParams.update({"font.family": ["Arial Unicode MS", "Arial"], "font.size": 11})


def stat(pp):
    """o -> (papers, strongly verified papers)."""
    return {o: (sum(p["o"] == o for p in pp), sum(p["o"] == o and p["v"] >= 3 for p in pp)) for o in range(1, 7)}


def tag(n, st):
    return "无论文" if n == 0 else "空白" if st == 0 else ""


def otxt(o, n, st):
    """'强验证/全部' plus the blank tag, and its colour."""
    t = tag(n, st)
    return (f"{st}/{n}" + (f"  {t}" if t else "")), (ACC if t == "空白" else FAINT if t else INK)


def save(fig, k, name, f, sub=""):
    d = OUT / sub; d.mkdir(parents=True, exist_ok=True)
    fig.savefig(d / f"A{k}_{name}_f{f}.png", dpi=160, facecolor="white"); plt.close(fig)


# ---------------------------------------------------------------- A1 flowers
def flower(ax, x, y, o, v, l, strong, s=1.0, contested=False):
    h = s * (0.7 + 0.62 * v)
    ax.plot([x, x], [y, y + h], color=ACC if strong else "#a8a294", lw=1.3 if strong else 0.9, zorder=1,
            solid_capstyle="round")
    for k in range(v):                                     # one small leaf per verification step
        yy = y + s * 0.35 + k * s * 0.55; sd = 1 if k % 2 else -1
        ax.add_patch(Ellipse((x + sd * 0.11 * s, yy), 0.22 * s, 0.08 * s, angle=sd * 35,
                             fc=ACC if strong else "#cfc9bd", ec="none", zorder=1))
    cx, cy = x, y + h + 0.36 * s
    for k in range(o):
        a = np.pi / 2 + 2 * np.pi * k / o
        ax.add_patch(Ellipse((cx + 0.21 * s * np.cos(a), cy + 0.21 * s * np.sin(a)), 0.42 * s, 0.18 * s,
                             angle=np.degrees(a), fc=L_COL[l] if strong else "white", ec=L_COL[l],
                             lw=0.6 if strong else 1.1, alpha=0.95, zorder=2))
    ax.add_patch(Circle((cx, cy), 0.045 * s, fc=INK, ec="none", zorder=3))
    if contested:
        ax.plot(cx, cy, "x", color=ACC, ms=7, mew=1.8, zorder=4)


def a1(pp, f):
    fig = plt.figure(figsize=(16, 13.5))
    ax = fig.add_axes([0.03, 0.06, 0.72, 0.8]); kx = fig.add_axes([0.77, 0.12, 0.21, 0.72])
    ps = sorted(pp, key=lambda p: (p["year"], p["o"], p["v"], p["l"]))
    K, R = 24, 4.7
    for i, p in enumerate(ps):
        r, c = divmod(i, K)
        flower(ax, c, -r * R, p["o"], p["v"], p["l"], p["v"] >= 3, contested=p["contested"])
    nr = (len(ps) - 1) // K + 1
    for r in range(nr):
        row = ps[r * K:(r + 1) * K]
        ax.plot([-0.5, len(row) - 0.5], [-r * R] * 2, color="#d8d2c6", lw=1, zorder=0)
        i0 = 0
        for y, g in IT.groupby(row, key=lambda p: p["year"]):
            n = len(list(g))
            ax.plot([i0 - 0.35, i0 + n - 0.65], [-r * R - 0.28] * 2, color=MUTED, lw=1.6, solid_capstyle="butt")
            ax.text(i0 + (n - 1) / 2, -r * R - 0.42, str(y), ha="center", va="top", fontsize=10 if n > 1 else 8.5,
                    color=INK)
            i0 += n
    ax.set_xlim(-0.8, K - 0.2); ax.set_ylim(-(nr - 1) * R - 1.0, 4.0); ax.set_aspect("equal"); ax.axis("off")
    # key
    kx.set_xlim(0, 6); kx.set_ylim(-1.5, 15.5); kx.axis("off")
    kx.text(0, 15.1, "如何读一朵花", fontsize=14, fontweight="bold", color=INK)
    kx.text(0, 14.3, "花瓣数 = 开放度 O", fontsize=11, color=INK)
    for o in range(1, 7):
        flower(kx, 0.4 + (o - 1) * 1.0, 11.6, o, 0, 1, False, s=0.95)
        kx.text(0.4 + (o - 1) * 1.0, 11.0, f"O{o}", ha="center", va="top", fontsize=10, color=MUTED)
    kx.text(0, 10.0, "茎高与叶数 = 验证强度 V（红茎 = V3–V4）", fontsize=11, color=INK)
    for v in range(5):
        flower(kx, 0.6 + v * 1.2, 5.6, 3, v, 2, v >= 3, s=0.95)
        kx.text(0.6 + v * 1.2, 5.3, f"V{v}", ha="center", va="top", fontsize=10, color=ACC if v >= 3 else MUTED)
    kx.text(0, 4.2, "实心 = 强验证，空心 = 仅声明；颜色 = 自主性", fontsize=11, color=INK)
    for l in range(4):
        kx.text(0, 3.3 - 0.75 * l, f"● {L_NAME[l]}", color=L_COL[l], fontsize=11, fontweight="bold")
    head(fig, f, "数据花园：一朵花一篇论文",
         "按发表年排列（每行 24 朵）；花瓣 = 开放度，茎高 = 验证强度，颜色 = 自主性　·　灵感：Giorgia Lupi《Data Humanism》/ Dear Data", pp)
    ostrip(fig, pp, 0.04, 0.03)
    save(fig, 1, "flowers", f)


def ostrip(fig, pp, x, y):
    """One line at the bottom: per-O strong/total with blanks in red."""
    st = stat(pp)
    fig.text(x, y, "各开放度 强验证/全部：", fontsize=11, color=INK, fontweight="bold")
    for o in range(1, 7):
        t, c = otxt(o, *st[o])
        fig.text(x + 0.14 + 0.135 * (o - 1), y, f"O{o}  {t}", fontsize=11, color=c,
                 fontweight="bold" if c == ACC else "normal")


# ---------------------------------------------------------------- A2 spiral
def a2(pp, f):
    fig = plt.figure(figsize=(16, 12.5))
    ax = fig.add_axes([0.02, 0.03, 0.66, 0.85]); kx = fig.add_axes([0.70, 0.2, 0.28, 0.6])
    ps = sorted(pp, key=lambda p: (p["year"], p["o"], p["v"], p["l"]))
    N, b, w = len(ps), 1 / (2 * np.pi), 0.1                 # one turn = 1 unit; lane width w
    th0, th1 = 2 * np.pi * 1.0, 2 * np.pi * 4.0
    th = np.sqrt(th0 ** 2 + np.arange(N) / (N - 1) * (th1 ** 2 - th0 ** 2))   # equal arc length
    xy = lambda t, r: (r * np.cos(np.pi / 2 - t), r * np.sin(np.pi / 2 - t))  # clockwise from 12 o'clock
    st = stat(pp); tg = np.linspace(th0 - 0.15, th1 + 0.15, 900)
    for o in range(1, 7):
        n, s = st[o]; x, y = xy(tg, b * tg + (o - 3.5) * w)
        if n and not s:
            ax.plot(x, y, color=ACC, lw=1.0, ls=(0, (4, 3)), alpha=0.7, zorder=1)
        else:
            ax.plot(x, y, color="#e6e1d8" if n else "#f1eee8", lw=0.9, zorder=1)
    for k in range(1, N):
        if ps[k]["year"] != ps[k - 1]["year"]:
            tm = (th[k] + th[k - 1]) / 2; r = b * tm
            ax.plot(*xy(np.array([tm, tm]), np.array([r - 0.31, r + 0.31])), color=MUTED, lw=0.9, zorder=1)
            a = np.pi / 2 - tm; x, y = xy(tm, r + 0.43)
            ax.text(x, y, str(ps[k]["year"]), ha="center", va="center", fontsize=10, color=INK,
                    rotation=(np.degrees(a) - 90 + 90) % 180 - 90)
    x, y = xy(th0, b * th0 - 0.43)
    ax.text(x, y, f"{ps[0]['year']} 起", ha="center", va="center", fontsize=10, color=INK)
    for p, t in zip(ps, th):
        x, y = xy(t, b * t + (p["o"] - 3.5) * w)
        if p["v"] >= 3:
            ax.plot(x, y, "o", color=L_COL[p["l"]], ms=8.5, mec="white", mew=0.7, zorder=3)
        else:
            ax.plot(x, y, "o", mfc="white", mec=L_COL[p["l"]], ms=7.5, mew=1.3, zorder=2)
        if p["contested"]:
            ax.plot(x, y, "x", color=ACC, ms=6, mew=1.5, zorder=4)
    ax.text(0, 0.15, f"{N}", ha="center", va="center", fontsize=30, fontweight="bold", color=INK)
    ax.text(0, -0.25, "篇论文\n由内向外 = 时间", ha="center", va="center", fontsize=11, color=MUTED, linespacing=1.4)
    R = b * th1 + 0.5; ax.set_xlim(-R, R); ax.set_ylim(-R, R); ax.set_aspect("equal"); ax.axis("off")
    # key: the six lanes straightened out
    kx.set_xlim(0, 10); kx.set_ylim(-5.6, 6.2); kx.axis("off")
    kx.text(0, 5.8, "螺旋带内的六条车道（由内到外）", fontsize=13, fontweight="bold", color=INK)
    for o in range(1, 7):
        y = 1.1 + (o - 1) * 0.72; n, s = st[o]; t, c = otxt(o, n, s)
        kx.plot([0, 2.2], [y, y], color=ACC if (n and not s) else "#cfc9bd", lw=1.2, ls=(0, (4, 3)) if (n and not s) else "-")
        kx.text(2.5, y, O_T[o - 1], va="center", fontsize=11, color=INK if n else FAINT)
        kx.text(6.6, y, t, va="center", fontsize=11, color=c, fontweight="bold" if c == ACC else "normal")
    kx.text(6.6, 5.2, "强验证/全部", fontsize=10, color=MUTED, va="center")
    kx.text(0, 0.2, "红色虚线车道 = 有论文但无强验证（空白）", fontsize=10, color=ACC, va="center")
    kx.plot(0.3, -1.0, "o", color=L_COL[2], ms=9, mec="white"); kx.text(0.8, -1.0, "实心 = 强验证（V3–V4）", va="center", fontsize=11)
    kx.plot(0.3, -1.8, "o", mfc="white", mec=L_COL[2], ms=8, mew=1.3); kx.text(0.8, -1.8, "空心 = 仅声明 / 弱验证（V0–V2）", va="center", fontsize=11)
    for l in range(4):
        kx.text(0, -2.9 - 0.65 * l, f"● {L_NAME[l]}", color=L_COL[l], fontsize=11, fontweight="bold", va="center")
    head(fig, f, "时间螺旋：从第一篇到最新一篇",
         "每个点一篇论文，按发表时间沿螺旋排列（等弧长），所在车道 = 开放度，颜色 = 自主性　·　灵感：Nadieh Bremer 径向/螺旋叙事图", pp)
    save(fig, 2, "spiral", f)


# ---------------------------------------------------------------- A3 pods
def pod(ax, x, y0, ls, up, strong, ds=0.15, W=0.17, sway=0.05):
    n = len(ls); m = int(np.ceil(n / 2)); Lp = m * ds + 0.2; sg = 1 if up else -1
    t = np.linspace(0, 1, 120); half = W * np.sin(np.pi * t) ** 0.55 * (0.75 if n == 1 else 1)
    sw = lambda tt: sway * np.sin(np.pi * tt) * np.sin(3 * x)
    yy = y0 + sg * t * Lp
    ax.add_patch(Polygon(np.r_[np.c_[x + sw(t) + half, yy], np.c_[(x + sw(t) - half)[::-1], yy[::-1]]],
                         fc="#f5dcd4" if strong else "#e4eaed", ec=ACC if strong else CLAIM, lw=1.1, alpha=0.95, zorder=2))
    for i, l in enumerate(sorted(ls)):
        k, side = divmod(i, 2); s = 0.1 + (k + 0.5) * ds; tt = s / Lp
        dx = 0 if (n == 1 or (k == m - 1 and n % 2)) else (-0.06 if side == 0 else 0.06)
        ax.add_patch(Circle((x + sw(tt) + dx, y0 + sg * s), 0.052, fc=L_COL[l], ec="white", lw=0.5, zorder=3))
    return Lp


def a3(pp, f):
    fig = plt.figure(figsize=(16, 11))
    ax = fig.add_axes([0.03, 0.03, 0.7, 0.84]); kx = fig.add_axes([0.75, 0.25, 0.23, 0.5])
    st = stat(pp); cell = C.defaultdict(list); SP = 1.25
    for p in pp:
        cell[(p["o"], p["v"])].append(p["l"])
    lo, hi = 0, 0
    for o in range(1, 7):
        x = (o - 1) * SP; n, s = st[o]
        for up, vs in ((True, (3, 4)), (False, (2, 1, 0))):
            y = 0.06 if up else -0.06; sg = 1 if up else -1; y_start = y
            for v in vs:
                ls = cell.get((o, v))
                if not ls:
                    continue
                Lp = pod(ax, x, y, ls, up, v >= 3)
                ax.text(x + 0.27, y + sg * Lp / 2, f"V{v}  {len(ls)}", va="center", fontsize=10,
                        color=ACC if v >= 3 else MUTED)
                y += sg * (Lp + 0.08)
            if y != y_start:
                ax.plot([x, x], [0, y - sg * 0.08], color=ACC if up else CLAIM, lw=0.6, zorder=1)
            lo, hi = min(lo, y), max(hi, y)
            if up and n and not s:
                t = np.linspace(0, 1, 60); hw = 0.17 * np.sin(np.pi * t) ** 0.55
                ax.add_patch(Polygon(np.r_[np.c_[x + hw, 0.06 + t * 0.9], np.c_[(x - hw)[::-1], (0.06 + t * 0.9)[::-1]]],
                                     fc="none", ec=ACC, lw=1.2, ls=(0, (3, 2)), zorder=2))
                ax.text(x, 1.1, "空白", ha="center", va="bottom", fontsize=13, color=ACC, fontweight="bold")
        if not n:
            ax.text(x, 0.35, "无论文", ha="center", va="bottom", fontsize=12, color=FAINT)
    top = hi + 0.35; bot = lo - 0.25
    ax.plot([-0.5, 5 * SP + 2.4], [0, 0], color=ACC, lw=1.4, zorder=1)
    for o in range(1, 7):
        x = (o - 1) * SP; n, s = st[o]
        ax.text(x, bot, O_T[o - 1].replace(" ", "\n"), ha="center", va="top", fontsize=12, color=INK if n else FAINT,
                fontweight="bold", linespacing=1.3)
        if n:
            ax.text(x, top, f"{s}/{n}", ha="center", va="bottom", fontsize=12, color=ACC if not s else INK, fontweight="bold")
    ax.text(5 * SP + 2.4, 0.12, "↑ 强验证\n（V3–V4）", ha="right", va="bottom", fontsize=11, color=ACC, fontweight="bold")
    ax.text(5 * SP + 2.4, -0.12, "↓ 声明 / 弱验证\n（V0–V2）", ha="right", va="top", fontsize=11, color=CLAIM, fontweight="bold")
    ax.text(5 * SP + 0.45, top, "强验证/全部", ha="left", va="bottom", fontsize=10, color=MUTED)
    ax.set_xlim(-0.6, 5 * SP + 2.5); ax.set_ylim(bot - 0.75, top + 0.4); ax.set_aspect("equal"); ax.axis("off")
    kx.set_xlim(0, 10); kx.set_ylim(0, 10); kx.axis("off")
    kx.text(0, 9.6, "如何读", fontsize=14, fontweight="bold", color=INK)
    rows = ["每一列 = 一个开放度", "红线 = 水线；向上长的豆荚 = 强验证，", "向下垂的豆荚 = 仅声明或弱验证",
            "一个豆荚 = 一个验证等级，长度 ∝ 论文数", "一粒种子 = 一篇论文，颜色 = 自主性",
            "红色虚线空荚 = 有论文却无强验证（空白）"]
    for i, r in enumerate(rows):
        kx.text(0, 8.6 - 0.75 * i, r, fontsize=11, color=ACC if "空白" in r else INK)
    for l in range(4):
        kx.text(0, 3.6 - 0.7 * l, f"● {L_NAME[l]}", color=L_COL[l], fontsize=11, fontweight="bold")
    head(fig, f, "豆荚：每个开放度长出的证据",
         "水线以上 = 强验证（V3–V4），水线以下 = 声明与弱验证；种子 = 论文，颜色 = 自主性　·　灵感：Federica Fragapane 有机形态", pp)
    save(fig, 3, "pods", f)


# ---------------------------------------------------------------- A4 isotype
def page(ax, x, y, col, solid, w=0.6, h=0.8, c=0.2):
    ax.add_patch(Polygon([(x, y), (x + w, y), (x + w, y + h - c), (x + w - c, y + h), (x, y + h)],
                         fc=col if solid else "white", ec=col, lw=0 if solid else 1.2, joinstyle="miter", zorder=2))
    ax.add_patch(Polygon([(x + w - c, y + h), (x + w - c, y + h - c), (x + w, y + h - c)],
                         fc="white" if solid else col, ec=col if not solid else "white", lw=0.6, zorder=3))
    if solid:
        for k, fr in enumerate((0.22, 0.42, 0.62)):
            ax.plot([x + 0.11, x + w - (0.26 if k == 2 else 0.11)], [y + fr * h] * 2, color="white", lw=1.0,
                    solid_capstyle="butt", zorder=3)


def a4(pp, f):
    fig = plt.figure(figsize=(16, 8.4)); ax = fig.add_axes([0.03, 0.09, 0.95, 0.76])
    st = stat(pp); U, B = 0.78, 2.9
    for o in range(1, 7):
        yb = -(6 - o) * B; n, s = st[o]
        ax.text(-9.3, yb - 0.05, O_T[o - 1], fontsize=14, fontweight="bold", color=INK if n else FAINT, va="center")
        t, c = otxt(o, n, s)
        ax.text(-9.3, yb - 0.85, f"强验证/全部 {t}", fontsize=11, color=c, va="center",
                fontweight="bold" if c == ACC else "normal")
        for li, (strong, lab) in enumerate(((True, "强验证"), (False, "仅声明"))):
            y = yb - li * 1.05
            ps = sorted([p for p in pp if p["o"] == o and (p["v"] >= 3) == strong], key=lambda p: (p["l"], -p["v"]))
            n and ax.text(-0.35, y + 0.0, lab, ha="right", va="center", fontsize=10, color=ACC if strong else MUTED)
            for i, p in enumerate(ps):
                page(ax, i * U, y - 0.4, L_COL[p["l"]], strong)
            if ps:
                ax.text(len(ps) * U + 0.15, y, str(len(ps)), va="center", fontsize=10, color=MUTED)
            elif strong and n:
                ax.text(0.05, y, "空白 — 没有一篇强验证", va="center", fontsize=12, color=ACC, fontweight="bold")
            elif not n and strong:
                ax.text(0.05, y - 0.5, "本学科无论文", va="center", fontsize=11, color=FAINT)
        if o > 1:
            ax.plot([-9.3, 44 * U], [yb + 0.95] * 2, color="#ece8e0", lw=0.8)
    ax.set_xlim(-9.5, 47 * U); ax.set_ylim(-5 * B - 1.7, 0.95); ax.set_aspect("equal"); ax.axis("off")
    head(fig, f, "图形统计：一张纸一篇论文",
         "每个开放度两行：上行实心 = 强验证（V3–V4），下行空心 = 仅声明 / 弱验证；颜色 = 自主性　·　灵感：Otto Neurath / Gerd Arntz Isotype", pp)
    lkey(fig, y=0.03); save(fig, 4, "isotype", f)


# ---------------------------------------------------------------- A5 circle packing (approved; refined)
FS5 = 12                                        # label size in pt; the scale U (inches per dot radius) adapts


def vogel(n, rd):
    """Sunflower (Vogel) spiral of n dots of radius rd; returns offsets and the enclosing radius."""
    if n == 1:
        return np.zeros((1, 2)), rd * 2.0
    k = np.arange(n); c = 1.12 * rd; r = c * np.sqrt(k + 0.5); a = k * np.pi * (3 - np.sqrt(5))
    return np.c_[r * np.cos(a), r * np.sin(a)], c * np.sqrt(n) + rd * 1.35


def greedy(rs, order, g):
    """Front packing: circles in the given order, each tangent to two placed ones, closest to their centroid."""
    pos = {}
    for idx, i in enumerate(order):
        r = rs[i]
        if idx == 0:
            pos[i] = np.zeros(2); continue
        if idx == 1:
            j = order[0]; pos[i] = np.array([rs[j] + r + g, 0.0]); continue
        cen = np.mean(list(pos.values()), axis=0); best = None
        for a in pos:
            for b in pos:
                if a >= b:
                    continue
                A, B, ra, rb = pos[a], pos[b], rs[a] + r + g, rs[b] + r + g
                d = np.linalg.norm(B - A)
                if d > ra + rb or d < abs(ra - rb):
                    continue
                m = (ra ** 2 - rb ** 2 + d ** 2) / (2 * d); h = np.sqrt(max(ra ** 2 - m ** 2, 0)); u = (B - A) / d
                for sg in (1, -1):
                    q = A + m * u + sg * h * np.array([-u[1], u[0]])
                    if all(np.linalg.norm(q - pos[c]) >= rs[c] + r + g - 1e-6 for c in pos):
                        dd = np.linalg.norm(q - cen)
                        if best is None or dd < best[0]:
                            best = (dd, q)
        pos[i] = best[1]
    return pos


def vrow(rs, g, lw=None):
    """A straight row V-low -> V-high for sparse O levels (few papers); neighbours sit far enough apart for
    their labels (widths lw) to clear. Returns centres and the enclosing radius."""
    vs = sorted(rs); xs, x = [], 0.0; lw = lw or {}
    for k, v in enumerate(vs):
        if k:
            a = vs[k - 1]; x = max(x, xs[-1] + (lw.get(a, 0) + lw.get(v, 0)) / 2 + 0.8 - rs[v])
        xs.append(x + rs[v]); x += 2 * rs[v] + g
    xs = np.array(xs) - (x - g) / 2
    return {v: np.array([xs[k], 0.0]) for k, v in enumerate(vs)}, (x - g) / 2


def vpack(rs, g=1.0):
    """Pack the V circles of one O level compactly AND in reading order: try every placement order and every
    rotation, keep those where every step V_k -> V_k+1 heads right at most 45 deg off horizontal (relaxed only if
    nothing qualifies), and take the smallest enclosing circle (ties: flatter steps, flatter row). Returns centres relative to the enclosing centre and its radius."""
    import itertools
    vs = sorted(rs); cands = []
    for order in itertools.permutations(vs):
        pos = greedy(rs, list(order), g)
        P = np.array([pos[v] for v in vs]); R = np.array([rs[v] for v in vs])
        for th in np.radians(np.arange(0, 360, 3)):
            c, s_ = np.cos(th), np.sin(th); Q = P @ np.array([[c, s_], [-s_, c]])
            dx, dy = np.diff(Q[:, 0]), np.abs(np.diff(Q[:, 1]))     # each step V_k -> V_k+1 must go rightwards,
            gap = (dx / np.maximum(dy, 1e-9)).min() if len(vs) > 1 else 9.0   # no steeper than 1/gap
            ctr = (np.min(Q - R[:, None], 0) + np.max(Q + R[:, None], 0)) / 2
            enc = max(np.linalg.norm(Q - ctr, axis=1) + R)
            cands.append((gap, (round(enc, 1), -gap, np.ptp(Q[:, 1])), {v: Q[k] - ctr for k, v in enumerate(vs)}, enc))
    R = np.array([rs[v] for v in vs]); angs = np.radians(np.arange(-45, 46, 5))
    def chain(P):                                           # each next V tangent to the previous, <= 45 deg off
        k = len(P)
        if k == len(vs):
            Q = np.array(P); ctr = (np.min(Q - R[:, None], 0) + np.max(Q + R[:, None], 0)) / 2
            enc = max(np.linalg.norm(Q - ctr, axis=1) + R)
            cands.append((9.0, (round(enc, 1), 0.0, np.ptp(Q[:, 1])), {v: Q[i] - ctr for i, v in enumerate(vs)}, enc))
            return
        for t in angs:
            q = P[-1] + (R[k - 1] + R[k] + g) * np.array([np.cos(t), np.sin(t)])
            if all(np.linalg.norm(q - P[i]) >= R[i] + R[k] + g - 1e-6 for i in range(k - 1)):
                chain(P + [q])
    chain([np.zeros(2)])
    for thr in (1.0, 0.6, 0.2, -np.inf):
        ok = [c for c in cands if c[0] > thr]
        if ok:
            best = min(ok, key=lambda c: c[1]); return best[2], best[3]


def tw(t, fs, U):
    """Approximate text width in data units at scale U (inches per unit)."""
    return sum(1.0 if ord(ch) > 0x2E80 else 0.6 for ch in t) * fs / 72 / U


def vlabels(pos, rads, txts, U, up=False):
    """One label per V circle: above (or below, for circles low in the cluster), else the other side, else left /
    right, taking the first side whose box clears every other V circle."""
    out = {}
    for v in pos:
        first = np.array([0.0, 1.0 if up or pos[v][1] >= -0.5 else -1.0])
        for u in (first, -first, np.array([-1.0, 0]), np.array([1.0, 0])):
            lab = vlabel(pos[v], rads[v], txts[v], U, u); (x0, y0), (x1, y1) = lab[4][0], lab[4][3]
            if all(np.hypot(max(x0 - pos[w][0], 0, pos[w][0] - x1), max(y0 - pos[w][1], 0, pos[w][1] - y1)) > rads[w] + 0.2
                   for w in pos if w != v):
                break
        out[v] = lab
    return out


def vlabel(c, rv, txt, U, u):
    """Anchor just outside a V circle on side u; returns (x, y, ha, va, box corners)."""
    x, y = c + u * (rv + 0.35); w, h = tw(txt, FS5, U) + 0.4, FS5 * 1.3 / 72 / U
    ha = "left" if u[0] > 0.3 else "right" if u[0] < -0.3 else "center"
    va = "bottom" if u[1] > 0.3 else "top" if u[1] < -0.3 else "center"
    x0 = x if ha == "left" else x - w if ha == "right" else x - w / 2
    y0 = y if va == "bottom" else y - h if va == "top" else y - h / 2
    return x, y, ha, va, [(x0, y0), (x0 + w, y0), (x0, y0 + h), (x0 + w, y0 + h)]


def a5(pp, f):
    st = stat(pp); rd = 1.0; FW, SIDE, GAP = 16.0, 0.55, 2.0
    TOP, CAP, KEY = 1.3, 1.2, 1.25                          # inches: title band, captions, key band
    base = {}
    for o in range(1, 7):                                   # geometry that does not depend on the scale
        vs = [v for v in range(5) if any(p["o"] == o and p["v"] == v for p in pp)]
        if vs:
            dots = {v: vogel(sum(p["o"] == o and p["v"] == v for p in pp), rd) for v in vs}
            sparse = sum(len(dots[v][0]) for v in vs) <= 6
            pos, enc = (None, None) if sparse else vpack({v: dots[v][1] for v in vs})
            base[o] = (vs, dots, pos, enc, sparse)
    U = 0.13
    for _ in range(4):                                      # fit the row into the page: labels depend on U
        ocs = []
        for o in range(1, 7):
            if o not in base:
                ocs.append(dict(o=o, R=3.5, vs=[])); continue
            vs, dots, pos, enc, sparse = base[o]
            if sparse:
                pos, enc = vrow({v: dots[v][1] for v in vs}, 1.6,
                                {v: tw(f"V{v} · {len(dots[v][0])}", FS5, U) for v in vs})
            labs = vlabels(pos, {v: dots[v][1] for v in vs}, {v: f"V{v} · {len(dots[v][0])}" for v in vs}, U, up=sparse)
            R = max(enc, max(np.hypot(*q) for v in vs for q in labs[v][4])) + 0.8
            ocs.append(dict(o=o, R=R, vs=vs, pos=pos, dots=dots, labs=labs))
        x = 0.0
        for c in ocs:
            half = max(c["R"], tw(O_T[c["o"] - 1], 15, U) / 2 + 0.6, tw("空白（仅声明）", FS5, U) / 2 + 0.6)
            c["x"] = x + half; x += 2 * half + GAP
        Wu = x - GAP; U = min(0.13, (FW - 2 * SIDE) / Wu)
    Rm = max(c["R"] for c in ocs); Hu = 2 * Rm; pw = Wu * U
    fh = TOP + Hu * U + CAP + KEY; extra = max(0.0, 8.8 - fh); TOP += extra * 0.5; KEY += extra * 0.5; fh += extra
    fig = plt.figure(figsize=(FW, fh))
    L = (FW - pw) / 2
    ax = fig.add_axes([L / FW, (KEY + CAP) / fh, pw / FW, Hu * U / fh])
    ax.set_xlim(0, Wu); ax.set_ylim(-Rm, Rm); ax.axis("off")
    ycap = (KEY + CAP - 0.1) / fh
    for c in ocs:
        o, R, X = c["o"], c["R"], c["x"]; n, s = st[o]; blank = n > 0 and s == 0
        if not c["vs"]:
            ax.add_patch(Circle((X, 0), R, fc="none", ec=FAINT, lw=1.1, ls=(0, (3, 3))))
        else:
            ax.add_patch(Circle((X, 0), R, fc="#faf8f4", ec=ACC if blank else "#cfc9bd", lw=1.6 if blank else 1.1,
                                ls=(0, (5, 3)) if blank else "-", zorder=1))
            for v in c["vs"]:
                (off, rv), (cx, cy) = c["dots"][v], c["pos"][v] + np.array([X, 0]); strong = v >= 3
                ax.add_patch(Circle((cx, cy), rv, fc="#f8e1d9" if strong else "#e9eef0",
                                    ec=ACC if strong else CLAIM, lw=1.3, zorder=2))
                ls = sorted(p["l"] for p in pp if p["o"] == o and p["v"] == v)
                for (dx, dy), l in zip(off, ls):
                    ax.add_patch(Circle((cx + dx, cy + dy), rd * 0.93, fc=L_COL[l], ec="white", lw=0.6, zorder=3))
                lx, ly, ha, va, _ = c["labs"][v]
                ax.text(lx + X, ly, f"V{v} · {len(ls)}", ha=ha, va=va, fontsize=FS5, zorder=5,
                        color=ACC if strong else MUTED, fontweight="bold" if strong else "normal")
        xf = (L + X * U) / FW
        fig.text(xf, ycap, O_T[o - 1], ha="center", va="top", fontsize=15, fontweight="bold", color=INK if n else FAINT)
        fig.text(xf, ycap - 0.34 / fh, f"强验证 {s} / {n}", ha="center", va="top", fontsize=FS5, color=INK if n else FAINT)
        t = "无论文" if n == 0 else "空白（仅声明）" if blank else ""
        t and fig.text(xf, ycap - 0.64 / fh, t, ha="center", va="top", fontsize=FS5, fontweight="bold",
                       color=FAINT if n == 0 else ACC)
    # key band, one row: autonomy colours | verification fills | V order
    yk = 0.5 / fh; yh = 0.88 / fh
    dot = lambda x, y, ms, fc, ec, lw=0: fig.add_artist(Line2D([x / FW], [y], marker="o", ms=ms, mfc=fc, mec=ec, mew=lw,
                                                               transform=fig.transFigure))
    fig.add_artist(plt.Line2D([SIDE / FW, 1 - SIDE / FW], [1.25 / fh] * 2, color="#e4dfd6", lw=0.8))
    xx = SIDE
    fig.text(xx / FW, yh, "论文点颜色 = 自主性", fontsize=FS5, color=MUTED, va="center")
    for k in range(4):
        dot(xx + 0.08, yk, 11, L_COL[k], "white", 0.6)
        fig.text((xx + 0.22) / FW, yk, L_NAME[k], color=INK, fontsize=FS5, va="center")
        xx += 0.5 + tw(L_NAME[k], FS5, 1.0)
    xx += 0.45
    fig.text(xx / FW, yh, "内圈 = 验证等级", fontsize=FS5, color=MUTED, va="center")
    for fc, ec, lab in (("#f8e1d9", ACC, "强验证（V3–V4）"), ("#e9eef0", CLAIM, "声明 / 弱验证（V0–V2）")):
        dot(xx + 0.1, yk, 15, fc, ec, 1.3)
        fig.text((xx + 0.28) / FW, yk, lab, color=ACC if ec == ACC else INK, fontsize=FS5, va="center")
        xx += 0.6 + tw(lab, FS5, 1.0)
    xx += 0.45
    fig.text(xx / FW, yh, "每个大圆内，验证等级从左到右递增", fontsize=FS5, color=MUTED, va="center")
    for v in range(5):
        dot(xx + 0.1 + 0.62 * v, yk, 15, "#f8e1d9" if v >= 3 else "#e9eef0", ACC if v >= 3 else CLAIM, 1.2)
        fig.text((xx + 0.24 + 0.62 * v) / FW, yk, f"V{v}", fontsize=FS5, va="center",
                 color=ACC if v >= 3 else MUTED, fontweight="bold" if v >= 3 else "normal")
    head(fig, f, "圆堆积：开放度 ⊃ 验证等级 ⊃ 论文",
         "大圆 = 开放度，内圈 = 验证等级（大圆内从左到右 V0→V4），小点 = 一篇论文　·　灵感：圆堆积（d3.pack / Bostock）", pp)
    save(fig, 5, "packing", f, sub="shortlist")


# ---------------------------------------------------------------- A6 treemap
def squarify(vals, x, y, w, h):
    """Squarified treemap (Bruls et al. 2000); vals sorted descending and summing to w*h; returns (x, y, w, h)."""
    def lay(vs, x, y, w, h):
        a = sum(vs); out = []
        if w >= h:
            ww = a / h
            for v in vs:
                out.append((x, y, ww, v / ww)); y += v / ww
        else:
            hh = a / w
            for v in vs:
                out.append((x, y, v / hh, hh)); x += v / hh
        return out
    def worst(vs, x, y, w, h):
        return max(max(r[2] / r[3], r[3] / r[2]) for r in lay(vs, x, y, w, h))
    if not vals:
        return []
    if len(vals) == 1:
        return lay(vals, x, y, w, h)
    i = 1
    while i < len(vals) and worst(vals[:i], x, y, w, h) >= worst(vals[:i + 1], x, y, w, h):
        i += 1
    cur, a = vals[:i], sum(vals[:i])
    rest = (x + a / h, y, w - a / h, h) if w >= h else (x, y + a / w, w, h - a / w)
    return lay(cur, x, y, w, h) + squarify(vals[i:], *rest)


def tfit(cands, w, fs):
    """The first label variant whose estimated width fits w (inches)."""
    for t in cands:
        if sum(1.0 if ord(ch) > 0x2E80 else 0.58 for ch in t) * fs / 72 < w - 0.08:
            return t
    return None


def treemap(items, x, y, w, h):
    items = sorted(items, key=lambda t: -t[1]); s = sum(n for _, n in items)
    return list(zip([k for k, _ in items], squarify([n * w * h / s for _, n in items], x, y, w, h)))


def a6(pp, f):
    fig = plt.figure(figsize=(16, 10.5)); W, H = 15.04, 8.2
    ax = fig.add_axes([0.03, 0.08, 0.94, H / 10.5]); st = stat(pp)
    for o, (x, y, w, h) in treemap([(o, st[o][0]) for o in range(1, 7) if st[o][0]], 0, 0, W, H):
        n, s = st[o]; blank = not s; x, y, w, h = x + 0.04, y + 0.04, w - 0.08, h - 0.08
        ax.add_patch(Rectangle((x, y), w, h, fc="#fbefeb" if blank else "#f1ede5", ec=ACC if blank else "none",
                               lw=1.5, ls=(0, (5, 3)) if blank else "-", zorder=1))
        HH = 0.36; t, c = otxt(o, n, s)
        lab = tfit([f"{O_T[o - 1]}　{t}", f"O{o} {t}", f"O{o}"], w, 12)
        ax.text(x + 0.08, y + h - HH / 2, lab, va="center", fontsize=12, fontweight="bold", color=c if blank else INK, zorder=5)
        for v, (vx, vy, vw, vh) in treemap([(v, sum(p["o"] == o and p["v"] == v for p in pp)) for v in range(5)
                                            if any(p["o"] == o and p["v"] == v for p in pp)],
                                           x + 0.06, y + 0.06, w - 0.12, h - HH - 0.06):
            strong = v >= 3; nv = sum(p["o"] == o and p["v"] == v for p in pp); vh2 = 0.27
            vx, vy, vw, vh = vx + 0.03, vy + 0.03, vw - 0.06, vh - 0.06
            ax.add_patch(Rectangle((vx, vy), vw, vh, fc="white", ec=ACC if strong else "#cfc9bd", lw=2.2 if strong else 0.8, zorder=2))
            vl = tfit([f"{V_T[v]}　{nv}", f"V{v} {nv}", f"V{v}"], vw, 10)
            vl and ax.text(vx + 0.06, vy + vh - vh2 / 2, vl, va="center", fontsize=10, color=ACC if strong else MUTED,
                           fontweight="bold" if strong else "normal", zorder=5)
            for l, (lx, ly, lw_, lh) in treemap([(l, sum(p["o"] == o and p["v"] == v and p["l"] == l for p in pp))
                                                  for l in range(4) if any(p["o"] == o and p["v"] == v and p["l"] == l for p in pp)],
                                                 vx + 0.05, vy + 0.05, vw - 0.1, vh - vh2 - 0.05):
                nl = sum(p["o"] == o and p["v"] == v and p["l"] == l for p in pp)
                ax.add_patch(Rectangle((lx + 0.02, ly + 0.02), lw_ - 0.04, lh - 0.04, fc=L_COL[l], alpha=1 if strong else 0.42,
                                       ec="none", zorder=3))
                ll = tfit([f"{L_NAME[l]}  {nl}", f"L{l} {nl}", f"{nl}"], lw_, 10) if lh > 0.22 else None
                ll and ax.text(lx + lw_ / 2, ly + lh / 2, ll, ha="center", va="center", fontsize=10, zorder=5,
                               color="white" if strong else INK, fontweight="bold" if strong else "normal")
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    miss = [O_T[o - 1] for o in range(1, 7) if not st[o][0]]
    if miss:
        fig.text(0.97, 0.035, "　".join(miss) + "：本学科无论文", ha="right", fontsize=11, color=FAINT)
    head(fig, f, "矩形树图：开放度 → 验证 → 自主性",
         "面积 ∝ 论文数；红框 = 强验证（V3–V4），框内实色；灰框 = 声明/弱验证，框内浅色；红虚线 = 空白　·　灵感：Shneiderman 树图 / Bruls 方形化算法", pp)
    lkey(fig, y=0.035); save(fig, 6, "treemap", f)


# ---------------------------------------------------------------- A7 sunburst
V_RING = ["#e3dfd7", "#cbc5b9", "#a8a194", "#e3917b", ACC]


def a7(pp, f):
    fig = plt.figure(figsize=(16, 12)); ax = fig.add_axes([0.0, 0.02, 0.7, 0.86]); kx = fig.add_axes([0.7, 0.25, 0.28, 0.5])
    N = len(pp); st = stat(pp); deg = lambda k: 90 - 360 * k / N
    ps = sorted(pp, key=lambda p: (p["o"], p["v"], p["l"]))
    def runs(key):
        out, i = [], 0
        for k, g in IT.groupby(ps, key=key):
            m = len(list(g)); out.append((k, i, i + m)); i += m
        return out
    mid = lambda a, b: np.radians((deg(a) + deg(b)) / 2)
    for o, a, b in runs(lambda p: p["o"]):
        ax.add_patch(Wedge((0, 0), 0.62, deg(b), deg(a), width=0.24, fc=ALT(0.12 + 0.15 * o), ec="white", lw=1.5))
        span = 360 * (b - a) / N; t = mid(a, b)
        if span >= 12:
            ax.text(0.5 * np.cos(t), 0.5 * np.sin(t), f"O{o}", ha="center", va="center", fontsize=13, fontweight="bold",
                    color="white" if o >= 4 else INK)
        n, s = st[o]; tt, c = otxt(o, n, s); r0 = 1.06
        ha = "left" if np.cos(t) > 0.15 else "right" if np.cos(t) < -0.15 else "center"
        if span < 15 and o == 5:
            t = t + np.radians(4)
        if span < 15 and o == 6:
            t = t - np.radians(2)
        ax.plot([1.0 * np.cos(mid(a, b)), r0 * np.cos(t)], [1.0 * np.sin(mid(a, b)), r0 * np.sin(t)], color=MUTED, lw=0.7)
        ax.text((r0 + 0.02) * np.cos(t), (r0 + 0.02) * np.sin(t), f"{O_T[o - 1]}  {tt}", ha=ha, va="center", fontsize=12,
                color=c if c == ACC else INK, fontweight="bold")
        if s:                                                # strong share = contiguous V3-V4 run at the wedge end
            ax.add_patch(Wedge((0, 0), 1.0, deg(b), deg(b - s), width=0.035, fc=ACC, ec="none"))
        else:
            th = np.radians(np.linspace(deg(a), deg(b), 60))
            ax.plot(0.985 * np.cos(th), 0.985 * np.sin(th), color=ACC, lw=2, ls=(0, (3, 2)))
    for (o, v), a, b in runs(lambda p: (p["o"], p["v"])):
        ax.add_patch(Wedge((0, 0), 0.8, deg(b), deg(a), width=0.16, fc=V_RING[v], ec="white", lw=1.2))
        if 360 * (b - a) / N >= 7:
            t = mid(a, b); ax.text(0.72 * np.cos(t), 0.72 * np.sin(t), f"V{v}", ha="center", va="center", fontsize=10,
                                   color="white" if v >= 3 else INK, fontweight="bold")
    for (o, v, l), a, b in runs(lambda p: (p["o"], p["v"], p["l"])):
        ax.add_patch(Wedge((0, 0), 0.95, deg(b), deg(a), width=0.13, fc=L_COL[l], alpha=1 if v >= 3 else 0.5,
                           ec="white", lw=0.9))
        if 360 * (b - a) / N >= 6:
            t = mid(a, b); ax.text(0.885 * np.cos(t), 0.885 * np.sin(t), str(b - a), ha="center", va="center", fontsize=9.5,
                                   color="white" if v >= 3 else INK)
    ns = sum(p["v"] >= 3 for p in pp)
    ax.text(0, 0.1, f"{N}", ha="center", va="center", fontsize=34, fontweight="bold", color=INK)
    ax.text(0, -0.08, f"篇论文\n强验证 {ns}", ha="center", va="center", fontsize=12, color=MUTED, linespacing=1.5)
    ax.set_xlim(-1.55, 1.55); ax.set_ylim(-1.25, 1.25); ax.set_aspect("equal"); ax.axis("off")
    kx.set_xlim(0, 10); kx.set_ylim(0, 10); kx.axis("off")
    kx.text(0, 9.7, "由内到外", fontsize=14, fontweight="bold", color=INK)
    kx.text(0, 8.9, "内环 = 开放度 O，中环 = 验证强度 V，外环 = 自主性 L", fontsize=11, color=INK)
    for v in range(5):
        kx.add_patch(Rectangle((0, 7.75 - 0.62 * v), 0.5, 0.42, fc=V_RING[v], ec="none"))
        kx.text(0.75, 7.96 - 0.62 * v, V_T[v], va="center", fontsize=11, color=ACC if v >= 3 else INK)
    for l in range(4):
        kx.add_patch(Rectangle((0, 4.3 - 0.62 * l), 0.5, 0.42, fc=L_COL[l], ec="none"))
        kx.text(0.75, 4.51 - 0.62 * l, L_NAME[l] + "（浅色 = 未强验证）" * (l == 0), va="center", fontsize=11, color=INK)
    kx.add_patch(Rectangle((0, 1.25), 0.5, 0.12, fc=ACC, ec="none"))
    kx.text(0.75, 1.31, "最外细弧 = 该开放度中强验证的份额", va="center", fontsize=11, color=INK)
    kx.plot([0, 0.5], [0.6, 0.6], color=ACC, lw=2, ls=(0, (3, 2)))
    kx.text(0.75, 0.6, "红色虚弧 = 有论文但无强验证（空白）", va="center", fontsize=11, color=ACC)
    miss = [O_T[o - 1] for o in range(1, 7) if not st[o][0]]
    if miss:
        kx.text(0, -0.2, "　".join(miss) + "：本学科无论文", fontsize=11, color=FAINT, va="center")
    head(fig, f, "旭日图：开放度 → 验证 → 自主性",
         "角度 ∝ 论文数，顺时针从 12 点起按 O1→O6、V0→V4、L0→L3 排列　·　灵感：John Stasko 旭日图 / Kerry Rodden 序列旭日图", pp)
    save(fig, 7, "sunburst", f)


# ---------------------------------------------------------------- A8 hex mosaic
def a8(pp, f):
    fig = plt.figure(figsize=(16, 12)); ax = fig.add_axes([0.03, 0.03, 0.66, 0.85]); kx = fig.add_axes([0.71, 0.3, 0.27, 0.45])
    R = 1.0; h3 = np.sqrt(3) * R; st = stat(pp)
    cnt = C.defaultdict(list)
    for p in pp:
        cnt[(p["o"], p["v"])].append(p["l"])
    top = max(len(v) for v in cnt.values())
    ctr = lambda o, v: (1.5 * R * (o - 1), h3 * v + (h3 / 2 if o % 2 == 0 else 0))
    for strong_pass in (False, True):
        for o in range(1, 7):
            for v in range(5):
                if (v >= 3) != strong_pass:
                    continue
                x, y = ctr(o, v); ls = cnt.get((o, v), []); s = v >= 3
                fc = ("#f6ddd4" if ls else "#fbefea") if s else ("#e9eef0" if ls else "#f7f7f5")
                ax.add_patch(RegularPolygon((x, y), 6, radius=R * 0.97, orientation=np.pi / 6, fc=fc,
                                            ec=ACC if s else "#dcd7cd", lw=1.8 if s else 0.9, zorder=2 if s else 1))
                if not ls:
                    continue
                n = len(ls); rr = R * (0.3 + 0.48 * np.sqrt(n / top)); a0 = 90
                for l in range(4):
                    k = ls.count(l)
                    if k:
                        ax.add_patch(Wedge((x, y), rr, a0 - 360 * k / n, a0, width=rr * 0.42, fc=L_COL[l], ec="white",
                                           lw=0.8, zorder=3)); a0 -= 360 * k / n
                ax.text(x, y, str(n), ha="center", va="center", fontsize=9 + 7 * np.sqrt(n / top), fontweight="bold",
                        color=INK, zorder=4)
    ybot, ytop = -h3 / 2 - 0.25, 4 * h3 + h3 + 0.25
    for o in range(1, 7):
        x = 1.5 * R * (o - 1); n, s = st[o]; t, c = otxt(o, n, s)
        ax.text(x, ybot, O_T[o - 1].replace(" ", "\n"), ha="center", va="top", fontsize=12, fontweight="bold",
                color=INK if n else FAINT, linespacing=1.3)
        ax.text(x, ytop, t.replace("  ", "\n"), ha="center", va="bottom", fontsize=12, color=c,
                fontweight="bold" if c != INK else "normal", linespacing=1.3)
    for v in range(5):
        ax.text(-R * 1.05, v * h3, V_T[v].replace(" ", "\n"), ha="right", va="center", fontsize=11,
                color=ACC if v >= 3 else MUTED, fontweight="bold" if v >= 3 else "normal", linespacing=1.2)
    ax.text(-R * 1.05, ytop, "强验证/全部", ha="right", va="bottom", fontsize=11, color=MUTED)
    ax.set_xlim(-3.0, 7.5 * R + 1.15); ax.set_ylim(ybot - 1.0, ytop + 1.0); ax.set_aspect("equal"); ax.axis("off")
    kx.set_xlim(0, 10); kx.set_ylim(0, 10); kx.axis("off")
    kx.text(0, 9.6, "如何读一块六边形", fontsize=14, fontweight="bold", color=INK)
    for i, r in enumerate(["列 = 开放度（偶数列错开半格），行 = 验证强度", "红边六边形 = 强验证区（V3–V4），连起来是海岸线",
                           "环内数字 = 论文数，环的大小 ∝ √论文数", "环的分段 = 自主性构成（12 点起顺时针 L0→L3）"]):
        kx.text(0, 8.7 - 0.8 * i, r, fontsize=11, color=INK)
    for l in range(4):
        kx.text(0, 5.0 - 0.75 * l, f"● {L_NAME[l]}", color=L_COL[l], fontsize=11, fontweight="bold")
    head(fig, f, "六边形马赛克：开放度 × 验证强度",
         "每格一个 (O, V) 组合，格内圆环 = 自主性构成；红边 = 强验证区　·　灵感：六边形分箱地图（hexbin）/ 方块拼贴马赛克", pp)
    save(fig, 8, "hexes", f)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--all"]; f = (args or ["03"])[0]; pp = load(f)
    every = [g for k, g in sorted(globals().items()) if k[0] == "a" and k[1:].isdigit()]
    for fn in (every if "--all" in sys.argv else [a5]):
        fn(pp, f)
