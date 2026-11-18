"""Eight presentation modes for one field's openness x verification x autonomy x era data (design exploration).

  mode1 landscape : proposal Fig. 1 for one field, time on x: land cells, papers as points, frontiers
  mode2 exploded  : teardown view, one plate per verification level V0-V4, each plate = openness x autonomy
  mode3 lego      : one brick per paper on an openness x verification baseplate, stacked by autonomy
  mode4 fission   : the same brick block split apart by autonomy L0-L3
  mode5 ridges    : one ridge per year, openness distribution, strong part filled
  mode6 alluvial  : every paper flowing openness -> verification -> autonomy
  mode7 waffle    : openness x verification matrix, one square per paper, coloured by autonomy
  mode8 topo      : topographic map of paper density over openness x verification
Data: ov_coding/increment/classification_results_662.jsonl. Usage: python3 fig_ovl_modes.py [field] (default 03)
"""
import sys, collections as C
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle
from matplotlib.lines import Line2D
from matplotlib.colors import LightSource, LinearSegmentedColormap, to_rgb
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import style as S
from fig_ovl_surface import INK, MUTED, ACC, L_COL, L_NAME, FZH, ALT
from fig_ovl_frontier_mountain import load, ERAS, ERA_TICK

O_T = ["O1 规则世界", "O2 既定基准", "O3 新实例", "O4 需物理检验", "O5 开放数学", "O6 开放科学"]
V_T = ["V0 声明", "V1 基准", "V2 计算/仿真", "V3 物理实验", "V4 证明/复现"]
LAND = ["#efe6cf", "#e2d3a9", "#cdb982", "#ae9a5e", "#86733f"]
OUT = S.ROOT / "out" / "modes"
plt.rcParams.update({"font.family": ["Arial Unicode MS", "Arial"], "font.size": 11})


def head(fig, field, title, sub, pp):
    ns = sum(p["v"] >= 3 for p in pp)
    fig.text(0.04, 0.95, f"{FZH[field]}：{title}", fontsize=22, fontweight="bold", color=INK)
    fig.text(0.04, 0.915, f"{sub}　·　{len(pp)} 篇，强验证（V3–V4）{ns} 篇", fontsize=12, color=MUTED)


def lkey(fig, x=0.04, y=0.035):
    for k in range(4):
        fig.text(x + 0.12 * k, y, f"■ {L_NAME[k]}", color=L_COL[k], fontsize=11, fontweight="bold")


def save(fig, k, name, field):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"mode{k}_{name}_f{field}.png", dpi=160, facecolor="white"); plt.close(fig)


def m1(pp, f):
    fig, ax = plt.subplots(figsize=(17, 10)); fig.subplots_adjust(0.12, 0.1, 0.86, 0.84)
    X = lambda y: -2.2 if y <= 1997 else -1.1 if y <= 2012 else y - 2013
    era = lambda y: next(k for k, (a, b) in enumerate(ERAS) if a <= y <= b)
    have = set()
    for y in range(2013, 2027):
        new = {p["o"] for p in pp if p["year"] == y and p["v"] >= 3}
        for o in have | new:
            ax.add_patch(FancyBboxPatch((X(y) - 0.47, o - 0.45), 0.94, 0.9, boxstyle="round,pad=0,rounding_size=0.12",
                                        fc=LAND[era(y)] if o in new - have else "#f1ebdd", ec="none", zorder=1))
        have |= new
    for xs in (-1.65, -0.55, 6.5, 10.5):
        ax.axvline(xs, color="#d8d2c6", lw=1, zorder=0)
    for t, x0, x1 in zip(ERA_TICK, [-2.75, -1.65, -0.55, 6.5, 10.5], [-1.65, -0.55, 6.5, 10.5, 13.6]):
        ax.text((x0 + x1) / 2, 6.75, t, ha="center", fontsize=12, color=INK, fontweight="bold")
    for x in (-2.2, -1.1):
        ax.text(x, 3.5, "本学科\n无论文", ha="center", va="center", color="#b5ae9f", fontsize=10)
    g = C.defaultdict(list)
    for p in pp:
        g[(p["year"], p["o"])].append(p)
    for (y, o), ps in g.items():
        ps.sort(key=lambda p: (-p["v"], p["l"])); n = len(ps); c = int(np.ceil(np.sqrt(n * 1.3))); r = int(np.ceil(n / c))
        for i, p in enumerate(ps):
            x = X(y) + (i % c - (c - 1) / 2) * 0.8 / max(c, 1); z = o + ((r - 1) / 2 - i // c) * 0.78 / max(r, 1)
            ms = 9 if n < 10 else 6
            if p["contested"]:
                ax.plot(x, z, "x", color=ACC, ms=ms, mew=2, zorder=5)
            elif p["v"] >= 3:
                ax.plot(x, z, "o", color=L_COL[p["l"]], ms=ms, mec="white", mew=0.6, zorder=4)
            else:
                ax.plot(x, z, "o", mfc="white", mec=L_COL[p["l"]], ms=ms, mew=1.1, zorder=3)
    yrs = sorted({p["year"] for p in pp})
    sf = [max([p["o"] for p in pp if p["year"] <= y and p["v"] >= 3] or [np.nan]) for y in yrs]
    ax.step([X(y) for y in yrs], sf, where="mid", color=ACC, lw=2.5, zorder=6)
    blanks = [o for o in range(1, 7) if o not in have]
    for o in blanks:
        ax.text(13.75, o, f"← 空白 O{o}", color=ACC, va="center", fontsize=12, fontweight="bold")
    ax.set_xlim(-2.75, 13.6); ax.set_ylim(0.4, 7.1)
    ax.set_xticks(range(14), [str(y) for y in range(2013, 2027)]); ax.set_yticks(range(1, 7), O_T)
    ax.spines[:].set_visible(False); ax.tick_params(length=0)
    head(fig, f, "开放度前沿（proposal Fig. 1 单学科展开）", "色块 = 已有强验证的开放度（深色 = 当年首次登陆）· 实心点 = 强验证 · 空心 = 仅声明 · 红线 = 强验证前沿", pp)
    lkey(fig); save(fig, 1, "landscape", f)


def m2(pp, f):
    fig = plt.figure(figsize=(16, 15)); ax = fig.add_axes([0.13, 0.0, 0.87, 0.9], projection="3d", computed_zorder=False)
    GAP = 2.2; top = max(C.Counter((p["o"], p["l"], p["v"]) for p in pp).values())
    for v in range(5):
        z = v * GAP; cnt = C.Counter((p["o"], p["l"]) for p in pp if p["v"] == v); strong = v >= 3
        slab = [[(-0.15, -0.15, z - 0.12), (6.15, -0.15, z - 0.12), (6.15, -0.15, z), (-0.15, -0.15, z)],
                [(6.15, -0.15, z - 0.12), (6.15, 4.15, z - 0.12), (6.15, 4.15, z), (6.15, -0.15, z)]]
        ax.add_collection3d(Poly3DCollection(slab, fc="#b9452f" if strong else "#8a9aa3", ec="none", alpha=0.9, zorder=v * 10))
        ax.add_collection3d(Poly3DCollection([[(-0.15, -0.15, z), (6.15, -0.15, z), (6.15, 4.15, z), (-0.15, 4.15, z)]],
                                             fc="#f6efe2" if strong else "#eef2f4", ec="#c8c2b6", zorder=v * 10 + 1))
        for o in range(1, 7):
            for l in range(4):
                n = cnt.get((o, l), 0)
                q = [(o - 0.95, l + 0.05, z), (o - 0.05, l + 0.05, z), (o - 0.05, l + 0.95, z), (o - 0.95, l + 0.95, z)]
                ax.add_collection3d(Poly3DCollection([q], fc=ALT(0.2 + 0.8 * n / top) if n else "white",
                                                     ec="#ddd8cf", lw=0.4, zorder=v * 10 + 2))
                if n:
                    ax.text(o - 0.5, l + 0.5, z + 0.02, str(n), ha="center", va="center", fontsize=10, zorder=v * 10 + 3,
                            color="white" if n / top > 0.4 else INK, fontweight="bold")
        nv = sum(cnt.values())
        ax.text(-0.4, -0.4, z, f"{V_T[v]}　{nv} 篇" + ("　强验证 = 陆地" if strong else ""), ha="right", fontsize=13,
                color=ACC if strong else INK, fontweight="bold", zorder=200)
    for x, y in [(-0.15, -0.15), (6.15, -0.15), (6.15, 4.15), (-0.15, 4.15)]:
        ax.plot([x, x], [y, y], [0, 4 * GAP], color="#9b958a", lw=0.8, ls=(0, (3, 3)), zorder=1)
    ax.set_xlim(0, 6); ax.set_ylim(0, 4); ax.set_zlim(0, 4 * GAP)
    for k in range(6):
        ax.text(k + 0.5, 4.4, -0.1, O_T[k].replace(" ", "\n"), ha="center", fontsize=9.5, color=INK)
    for l in range(4):
        ax.text(6.4, l + 0.5, -0.1, L_NAME[l], fontsize=10, color=L_COL[l], fontweight="bold")
    ax.set_axis_off(); ax.set_box_aspect((6, 4, 4 * GAP * 1.05), zoom=1.05); ax.view_init(elev=16, azim=-60)
    head(fig, f, "拆机图：按验证强度分层", "每层一块板 = 开放度 × 自主性，数字 = 论文数；红色板 = 强验证（V3–V4）", pp)
    save(fig, 2, "exploded", f)


def bricks(ax, pp, x0=0.0, only=None, top=None):
    cell = C.defaultdict(list)
    for p in pp:
        if only is None or p["l"] == only:
            cell[(p["o"], p["v"])].append(p["l"])
    for (o, v), ls in sorted(cell.items(), key=lambda t: (-t[0][1], t[0][0])):
        for i, l in enumerate(sorted(ls)):
            ax.bar3d(x0 + o - 0.42, v - 0.42, i, 0.84, 0.84, 0.94, color=L_COL[l], edgecolor="white", linewidth=0.5,
                     shade=True, lightsource=LightSource(azdeg=225, altdeg=65))
        ax.text(x0 + o, v, len(ls) + 0.8, str(len(ls)), ha="center", fontsize=9, color=INK, fontweight="bold")
    for o in range(1, 7):
        for v in range(5):
            ax.add_collection3d(Poly3DCollection([[(x0 + o - 0.48, v - 0.48, 0), (x0 + o + 0.48, v - 0.48, 0),
                                                   (x0 + o + 0.48, v + 0.48, 0), (x0 + o - 0.48, v + 0.48, 0)]],
                                                 fc="#f3dcd4" if v >= 3 else "#e8e4dc", ec="white", lw=0.8))


def m3(pp, f):
    fig = plt.figure(figsize=(16, 12)); ax = fig.add_axes([0, 0.04, 1, 0.86], projection="3d")
    bricks(ax, pp)
    ax.set_xticks(range(1, 7), O_T, fontsize=9); ax.set_yticks(range(5), V_T, fontsize=9)
    ax.set_zlabel("论文数（一块砖 = 一篇）"); ax.set_box_aspect((6, 5, 4)); ax.view_init(elev=28, azim=-50)
    head(fig, f, "乐高拼装：一块砖一篇论文", "底板 = 开放度 × 验证强度（粉色区 = 强验证 V3–V4），砖的颜色 = 自主性", pp)
    lkey(fig); save(fig, 3, "lego", f)


def m4(pp, f):
    fig = plt.figure(figsize=(24, 9))
    zt = max(C.Counter((p["o"], p["v"], p["l"]) for p in pp).values())
    for l in range(4):
        ax = fig.add_axes([0.005 + 0.245 * l, 0.02, 0.26, 0.8], projection="3d")
        bricks(ax, pp, only=l)
        nl = sum(p["l"] == l for p in pp); st = sum(p["l"] == l and p["v"] >= 3 for p in pp)
        ax.set_title(f"{L_NAME[l]}　{nl} 篇 · 强验证 {st}", fontsize=14, color=L_COL[l], fontweight="bold", y=0.92)
        ax.set_xticks(range(1, 7), [f"O{k}" for k in range(1, 7)], fontsize=8); ax.set_yticks(range(5), [f"V{k}" for k in range(5)], fontsize=8)
        ax.set_zlim(0, zt + 2); ax.tick_params(axis="z", labelsize=7)
        ax.set_box_aspect((6, 5, 4)); ax.view_init(elev=28, azim=-50)
    head(fig, f, "裂变：按自主性拆开的四块积木", "每块底板 = 开放度 O1–O6（左→右）× 验证强度 V0–V4（前→后），粉色 = 强验证；一块砖 = 一篇", pp)
    save(fig, 4, "fission", f)


def m5(pp, f):
    # rows: one per pre-2013 era that has papers (aggregated), then one per year from the field's first year >= 2013
    era = lambda y: next(k for k, (a, b) in enumerate(ERAS) if a <= y <= b)
    rows = [(ERA_TICK[e], (lambda p, e=e: p["era"] == e), e) for e in (0, 1) if any(p["era"] == e for p in pp)]
    y0 = min([p["year"] for p in pp if p["year"] >= 2013] or [2026])
    rows += [(str(y), (lambda p, y=y: p["year"] == y), era(y)) for y in range(y0, 2027)]
    R = len(rows)
    H = max(11, 5 + 0.92 * R)
    fig, ax = plt.subplots(figsize=(14, H)); fig.subplots_adjust(0.17, 1.5 / H, 0.86, 1 - 2.1 / H)
    og = np.linspace(0.45, 6.55, 600)
    k = lambda os: sum(np.exp(-(og - o) ** 2 / (2 * 0.2 ** 2)) for o in os) if os else og * 0
    sc = 0.16; rng = np.random.default_rng(5)
    for o in range(1, 7):
        ax.axvline(o, color="#ece8e1", lw=0.8, zorder=0)
    for i, (lab, sel, e) in enumerate(rows[::-1]):
        b = R - 1 - i; zo = 4 * i
        ps = [p for p in pp if sel(p)]; n = len(ps); st = sum(p["v"] >= 3 for p in ps)
        a = k([p["o"] for p in ps]) * sc; s = k([p["o"] for p in ps if p["v"] >= 3]) * sc
        ax.fill_between(og, b, b + a, color="white", lw=0, zorder=zo + 1)
        ax.fill_between(og, b, b + a, color="#e9e4da", alpha=0.9, lw=0, zorder=zo + 1)
        ax.fill_between(og, b, b + s, color=ACC, alpha=0.9, lw=0, zorder=zo + 2)
        ax.plot(og, b + a, color=INK if n else "#d8d2c6", lw=1.6 if n else 0.8, zorder=zo + 3)
        for p in ps:   # rug: one tick per paper, coloured by autonomy
            x = p["o"] + rng.uniform(-0.22, 0.22)
            ax.plot([x, x], [b - 0.02, b - 0.2], color=L_COL[p["l"]], lw=1.3, zorder=zo + 3, solid_capstyle="butt")
        ax.text(0.32, b + 0.05, lab, ha="right", fontsize=12.5, color=INK if n else "#c9c3b8",
                fontweight="bold" if n else "normal")
        if n:
            ax.text(6.68, b + 0.05, f"{st}/{n}", fontsize=12, color=ACC if st else INK, fontweight="bold")
    for e in range(5):                             # era brackets over the rows that belong to each era
        ix = [i for i, r in enumerate(rows) if r[2] == e]
        if not ix:
            continue
        a0, b0 = min(ix), max(ix)
        ax.plot([-0.55, -0.55], [a0 - 0.2, b0 + 0.5], color=MUTED, lw=2.2, solid_capstyle="round")
        ax.text(-0.68, (a0 + b0) / 2 + 0.15, ERA_TICK[e] if b0 > a0 else "", rotation=90, ha="right", va="center",
                color=MUTED, fontsize=12.5)
    empty = [ERA_TICK[e] for e in range(5) if not any(p["era"] == e for p in pp)]
    if empty:
        ax.text(-0.55, -1.7, f"{' · '.join(empty)}：本学科无论文", color="#b5ae9f", fontsize=11, ha="left")
    ax.text(6.68, R - 1 + 0.6, "强验证/全部", fontsize=11, color=MUTED)
    for o in range(1, 7):        # blanks: papers at this openness but none strongly verified; no papers at all is not a blank
        n = sum(p["o"] == o for p in pp); st = sum(p["o"] == o and p["v"] >= 3 for p in pp)
        if not n:
            ax.text(o, -0.75, "无论文", color="#b5ae9f", ha="center", fontsize=12)
        elif not st:
            ax.plot([o - 0.4, o + 0.4], [-0.5, -0.5], color=ACC, lw=2.5, solid_capstyle="butt")
            ax.text(o, -0.85, f"空白\n{n} 篇仅声明", color=ACC, ha="center", va="top", fontsize=11.5,
                    fontweight="bold")
    top = max(R - 1 + k([p["o"] for p in pp if p["year"] == 2026]).max() * sc, R) + 0.3
    ax.set_xlim(-1.0, 7.3); ax.set_ylim(-1.9, top)
    ax.set_xticks(range(1, 7), [t.replace(" ", "\n") for t in O_T], fontsize=12.5); ax.xaxis.tick_top()
    ax.set_yticks([]); ax.spines[:].set_visible(False); ax.tick_params(length=0, pad=8)
    head(fig, f, "年轮山脊：每年一条开放度分布",
         "灰色山体 = 当年全部论文，红色 = 其中强验证（V3–V4）；山脚短线 = 每篇论文，颜色 = 自主性；右列 = 强验证/全部", pp)
    lkey(fig); save(fig, 5, "ridges", f)


def m6(pp, f):
    fig, ax = plt.subplots(figsize=(17, 11)); fig.subplots_adjust(0.03, 0.06, 0.97, 0.86)
    cols = [("o", range(1, 7), O_T), ("v", range(5), V_T), ("l", range(4), L_NAME)]
    xs, W, GAPF, N = [0, 1, 2], 0.05, 0.025, len(pp)
    pos = {}
    for ci, (key, ks, names) in enumerate(cols):
        y = 0
        for kk in ks:
            n = sum(p[key] == kk for p in pp)
            pos[(ci, kk)] = [y, y + n / N]
            c = (L_COL[kk] if key == "l" else ACC if key == "v" and kk >= 3 else "#56707f") if n else "#ccc"
            ax.add_patch(Rectangle((xs[ci] - W / 2, y), W, max(n / N, 0.002), fc=c, ec="none", zorder=3))
            ax.text(xs[ci] + (-W if ci == 0 else W), y + n / N / 2, f"{names[kk - (key == 'o')]}  {n}", ha="right" if ci == 0 else "left",
                    va="center", fontsize=11, color=INK if n else "#b5ae9f", zorder=4)
            y += n / N + GAPF
    for ci, (ka, kb) in enumerate([("o", "v"), ("v", "l")]):
        out = {k: v[0] for k, v in pos.items()}; inn = dict(out)
        pairs = C.Counter((p[ka], p[kb]) for p in pp)
        for (a, b), n in sorted(pairs.items()):
            h = n / N; y0 = out[(ci, a)]; y1 = inn[(ci + 1, b)]; out[(ci, a)] += h; inn[(ci + 1, b)] += h
            t = np.linspace(0, 1, 50); s = 3 * t ** 2 - 2 * t ** 3; x = xs[ci] + W / 2 + t * (1 - W)
            top = y0 + (y1 - y0) * s
            col = (ACC if b >= 3 else "#8fa6b3") if ka == "o" else L_COL[b]
            ax.add_patch(Polygon(np.r_[np.c_[x, top], np.c_[x[::-1], (top + h)[::-1]]], fc=col, alpha=0.45, ec="none", zorder=1))
        for k in [k for k in pos if k[0] == ci + 1]:
            pass
    for ci, t in enumerate(["问题开放度 O", "验证强度 V", "系统自主性 L"]):
        ax.text(xs[ci], -0.05, t, ha="center", fontsize=14, fontweight="bold", color=INK)
    ax.set_xlim(-0.5, 2.5); ax.set_ylim(1.2, -0.1); ax.axis("off")
    head(fig, f, "冲积图：每篇论文从开放度流向验证与自主性", "红色流 = 进入强验证（V3–V4）；右半按自主性着色；带宽 ∝ 论文数", pp)
    save(fig, 6, "alluvial", f)


def m7(pp, f):
    fig, ax = plt.subplots(figsize=(16, 12)); fig.subplots_adjust(0.14, 0.08, 0.9, 0.86)
    cell = C.defaultdict(list)
    for p in pp:
        cell[(p["o"], p["v"])].append(p)
    nc = 8; nr = int(np.ceil(max(len(v) for v in cell.values()) / nc)); s = 0.9 / max(nc, nr)
    ax.add_patch(Rectangle((2.5, 0.5), 2, 6, fc="#f6ece4", ec="none", zorder=0))
    ax.axvline(2.5, color=ACC, lw=2); ax.text(2.55, 6.62, "水线 → 强验证（V3–V4）= 陆地", color=ACC, fontsize=12, fontweight="bold")
    for (o, v), ps in cell.items():
        ps.sort(key=lambda p: (p["l"], p["year"]))
        for i, p in enumerate(ps):
            x = v - 0.45 + (i % nc) * s; y = o + 0.4 - (i // nc + 1) * s
            ax.add_patch(Rectangle((x, y), s * 0.86, s * 0.86, fc=L_COL[p["l"]], ec="none",
                                   alpha=1 if p["year"] >= 2024 else 0.55, zorder=2))
        ax.text(v + 0.45, o - 0.44, str(len(ps)), ha="right", va="bottom", fontsize=10, color=MUTED)
    for o in range(1, 7):
        n = sum(p["o"] == o for p in pp); st = sum(p["o"] == o and p["v"] >= 3 for p in pp)
        ax.text(4.6, o, f"{st}/{n}" + ("  空白" if n and not st else ""), va="center", fontsize=12,
                color=ACC if n and not st else INK, fontweight="bold")
    ax.set_xlim(-0.5, 5.3); ax.set_ylim(0.5, 6.8); ax.set_xticks(range(5), V_T); ax.set_yticks(range(1, 7), O_T)
    ax.set_xticks(np.arange(-0.5, 5, 1), minor=True); ax.set_yticks(np.arange(0.5, 7, 1), minor=True)
    ax.grid(which="minor", color="#e4dfd6"); ax.tick_params(length=0, which="both"); ax.spines[:].set_visible(False)
    head(fig, f, "方块矩阵：一格一篇", "行 = 开放度，列 = 验证强度；方块颜色 = 自主性（浅色 = 2024 年前）；右侧 = 强验证 / 全部", pp)
    lkey(fig); save(fig, 7, "waffle", f)


def m8(pp, f):
    fig, ax = plt.subplots(figsize=(17, 12)); fig.subplots_adjust(0.13, 0.13, 0.86, 0.8)
    X0, X1, Y0, Y1 = 0.3, 6.7, -0.7, 4.7
    xo, yv = np.meshgrid(np.linspace(X0, X1, 640), np.linspace(Y0, Y1, 540))
    z = sum(np.exp(-((xo - p["o"]) ** 2 + (yv - p["v"]) ** 2) / (2 * 0.36 ** 2)) for p in pp)
    terr = LinearSegmentedColormap.from_list("t", ["#f4f1e8", "#e3e8cf", "#c4d29c", "#9fb377", "#c9a76a", "#a07a4f",
                                                   "#7b5a3c"])
    ls = LightSource(azdeg=315, altdeg=40)
    rgb = ls.shade(z, cmap=terr, vert_exag=0.06, blend_mode="soft", vmin=0, vmax=z.max())[:, :, :3]
    water = (yv < 2.5)[:, :, None]                 # below the coastline: claims only, washed in water blue
    rgb = np.where(water, rgb * 0.55 + np.array(to_rgb("#9cc3d5")) * 0.45, rgb)
    ax.imshow(rgb, extent=(X0, X1, Y0, Y1), origin="lower", aspect="auto", zorder=0)
    cs = ax.contour(xo, yv, z, levels=[1, 3, 6, 10, 15, 20, 25, 30], colors="#4f3f2c", linewidths=0.6, alpha=0.6, zorder=1)
    ax.clabel(cs, fontsize=8.5, fmt="%g", inline_spacing=2)
    for k in range(1, 7):
        ax.axvline(k, color="white", lw=0.5, alpha=0.6, ls=(0, (1, 3)), zorder=1)
    for k in range(5):
        ax.axhline(k, color="white", lw=0.5, alpha=0.6, ls=(0, (1, 3)), zorder=1)
    ax.axhline(2.5, color=ACC, lw=2, zorder=3)
    ax.text(X1 - 0.05, 2.58, "强验证海岸线  ↑ 陆地 = V3–V4", color=ACC, ha="right", fontsize=13, fontweight="bold", zorder=5)
    ax.text(X1 - 0.05, 2.32, "↓ 水面之下 = 仅声明 V0–V2", color="#2f6f8f", ha="right", va="top", fontsize=13, fontweight="bold", zorder=5)
    rng = np.random.default_rng(3)
    for p in pp:
        x, y = p["o"] + rng.uniform(-0.24, 0.24), p["v"] + rng.uniform(-0.24, 0.24)
        if p["contested"]:
            ax.plot(x, y, "x", color=ACC, ms=8, mew=2, zorder=6)
        else:
            ax.plot(x, y, "^" if p["v"] >= 3 else "o", color=L_COL[p["l"]], ms=6.5 if p["v"] >= 3 else 5.5,
                    mec="white", mew=0.6, alpha=0.95 if p["year"] >= 2024 else 1, zorder=6)
    cnt = C.Counter((p["o"], p["v"]) for p in pp)
    for (o, v), n in cnt.most_common(3):          # summits
        ax.plot(o, v + 0.36, marker="^", color=INK, ms=11, mec="white", mew=1.2, zorder=7)
        ax.text(o + 0.12, v + 0.36, f"O{o}·V{v} 峰  {n} 篇", fontsize=12, color=INK, fontweight="bold", va="center",
                zorder=7, bbox=dict(fc="white", ec="none", alpha=0.7, pad=1.5))
    for o in range(1, 7):                          # header strip: strong / all per openness level
        n = sum(p["o"] == o for p in pp); s = sum(p["o"] == o and p["v"] >= 3 for p in pp)
        lab = f"{s}/{n}" + ("\n空白" if n and not s else "") if n else "无论文"
        ax.text(o, Y1 + 0.12, lab, ha="center", va="bottom", fontsize=13, fontweight="bold",
                color=ACC if n and not s else INK if n else "#b5ae9f")
    ax.text(X0, Y1 + 0.12, "强验证/全部", ha="right", va="bottom", fontsize=11, color=MUTED)
    # compass
    cx, cy = X0 + 0.32, Y1 - 0.75
    ax.annotate("", xy=(cx, cy + 0.3), xytext=(cx, cy - 0.15), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4))
    ax.text(cx, cy + 0.36, "更强验证", ha="center", fontsize=10, color=INK)
    ax.set_xlim(X0, X1); ax.set_ylim(Y0, Y1)
    ax.set_xticks(range(1, 7), [t.replace(" ", "\n") for t in O_T], fontsize=12.5)
    ax.set_yticks(range(5), V_T, fontsize=12.5); ax.tick_params(length=0, pad=8)
    for sp in ax.spines.values():
        sp.set_linewidth(2.2); sp.set_color(INK)
    head(fig, f, "地形图：开放度 × 验证强度",
         "地势 = 论文密度（等高线数字 = 密度），▲ 峰 = 论文最多的组合；三角 = 强验证论文，圆点 = 仅声明，颜色 = 自主性", pp)
    lkey(fig); save(fig, 8, "topo", f)


if __name__ == "__main__":
    f = (sys.argv[1:] or ["03"])[0]; pp = load(f)
    for m in (m1, m2, m3, m4, m5, m6, m7, m8):
        m(pp, f)
