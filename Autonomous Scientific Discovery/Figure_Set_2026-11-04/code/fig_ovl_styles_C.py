"""Design study, group C (cartography / terrain metaphors): one field's openness x verification x autonomy x era data.

  C1 vridges   : ridgelines per verification level V0-V4, openness distribution, strong ridges red, autonomy rug
  C2 islands   : island map, x = year, y = openness, paper density = land, bathymetric sea, eras as national borders
  C3 relief    : oblique shaded relief (rayshader-like) of O x V density with cast soft shadows and a cut base
  C4 swiss     : Swiss-minimal contour map, contour lines + spot heights, peaks labelled like summits
  C5 tanaka    : Tanaka illuminated contours of O x V density, light from the north-west
  C6 polar     : polar topography, angle = openness, radius = verification, Imhof-coloured relief, rim histogram
  C7 hex       : extruded hexagonal elevation map over O x V, autonomy as dots on the hex tops
  C8 pleasures : "Unknown Pleasures" ridge map, dense lines over openness, x = year, red where strongly verified
Strong verification = V3-V4; a blank (空白) = an openness level with papers but no strong case.
Data: fig_ovl_frontier_mountain.load (ov_coding/increment/classification_results_662.jsonl).
Approved styles (C1-C5, C7, C8) are written to out/styles/shortlist/C{n}_{name}_f{field}.png; C6 (rejected) is kept
for reference and written to out/styles/ only when asked for explicitly.
Usage: python3 fig_ovl_styles_C.py [field] [n ...]   (default: field 03, the approved styles; e.g. `03 6` renders C6)
"""
import sys, collections as C
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import Wedge, Polygon, Rectangle, Circle
from matplotlib.collections import LineCollection, PolyCollection
from matplotlib.colors import LightSource, LinearSegmentedColormap, to_rgb
from scipy.ndimage import distance_transform_edt, map_coordinates
from scipy.interpolate import RegularGridInterpolator
import style as S
from fig_ovl_frontier_mountain import load, ERAS, ERA_TICK
from fig_ovl_surface import INK, MUTED, ACC, L_COL, L_NAME, FZH, ALT
from fig_ovl_modes import O_T, V_T, head

OUT = S.ROOT / "out" / "styles"
plt.rcParams.update({"font.family": ["Arial Unicode MS", "Arial"], "font.size": 12})
SHORT = OUT / "shortlist"
APPROVED = (1, 2, 3, 4, 5, 7, 8)
HALO = [pe.withStroke(linewidth=3.2, foreground="white")]
SEA = "#4f7f99"


def save(fig, k, name, f):
    d = SHORT if k in APPROVED else OUT
    d.mkdir(parents=True, exist_ok=True)
    fig.savefig(d / f"C{k}_{name}_f{f}.png", dpi=160, facecolor="white"); plt.close(fig)


def lkey(fig, x=0.04, y=0.035):
    """The house L0-L3 colour key (fig_ovl_modes.lkey), set at 12 pt."""
    for k in range(4):
        fig.text(x + 0.12 * k, y, f"■ {L_NAME[k]}", color=L_COL[k], fontsize=12, fontweight="bold")


def ostat(pp):
    """[(papers, strong)] per openness level O1-O6."""
    return [(sum(p["o"] == o for p in pp), sum(p["o"] == o and p["v"] >= 3 for p in pp)) for o in range(1, 7)]


BLANK = "空白（仅声明）"


def tag(n, st):
    """无论文 = no paper at this openness level; 空白（仅声明）= papers, but none strongly verified (V3-V4)."""
    return "无论文" if not n else BLANK if not st else ""


def nice_iv(zmax, n=20):
    """Equal contour interval: the smallest of 1, 2, 5, 10 giving at most ~n contours."""
    return next(iv for iv in (1, 2, 5, 10, 20) if zmax / iv <= n)


def tcol(t):
    return ACC if t == BLANK else "#a39d90" if t else INK


def kde(pp, X, Y, kx="o", ky="v", sx=0.36, sy=0.36, sel=None):
    """Unnormalised Gaussian density (peak 1 per paper) over the papers' (kx, ky), summed per occupied cell."""
    z = np.zeros(np.shape(X))
    for (a, b), n in C.Counter((p[kx], p[ky]) for p in pp if sel is None or sel(p)).items():
        z += n * np.exp(-(X - a) ** 2 / (2 * sx ** 2) - (Y - b) ** 2 / (2 * sy ** 2))
    return z


def spiral(n, r=0.4):
    """Phyllotaxis offsets: n points spread evenly over a disc of radius r (deterministic, no random jitter)."""
    k = np.arange(n); rad = r * np.sqrt((k + 0.5) / max(n, 1)); a = k * 2.39996
    return rad * np.cos(a), rad * np.sin(a)


def cells(pp, kx="o", ky="v"):
    g = C.defaultdict(list)
    for p in pp:
        g[(p[kx], p[ky])].append(p)
    for v in g.values():
        v.sort(key=lambda p: (p["l"], -p["v"], p["year"]))
    return g


def pie(ax, x, y, ls, r, z=6, ec="white"):
    cnt = C.Counter(ls); a0 = 90.0
    for l in range(4):
        if cnt[l]:
            a1 = a0 + 360 * cnt[l] / len(ls)
            ax.add_patch(Wedge((x, y), r, a0, a1, fc=L_COL[l], ec=ec, lw=0.6, zorder=z)); a0 = a1


def spaced(s):
    return " ".join(s)


def hill(Z, az=315, alt=40, ve=1.0, dx=1.0, dy=1.0):
    """Hillshade for an array whose row 0 is the SOUTH edge (origin='lower'); light azimuth from north, clockwise."""
    return LightSource(azdeg=az, altdeg=alt).hillshade(Z[::-1], vert_exag=ve, dx=dx, dy=dy)[::-1]


def oside(fig, pp, rect, title="各开放度：强验证 / 全部"):
    """Right-hand legend panel: one bar per openness level, grey = all papers, red = strongly verified."""
    ax = fig.add_axes(rect); st_ = ostat(pp); top = max(n for n, _ in st_)
    for k, (n, st) in enumerate(st_):
        y = 6 - k; t = tag(n, st)
        ax.barh(y, n / top, height=0.34, color="#d9d4ca", lw=0)
        ax.barh(y, st / top, height=0.34, color=ACC, lw=0)
        ax.text(0, y + 0.3, O_T[k] + (f"　{t}" if t else ""), fontsize=12, color=tcol(t) if t else INK, va="bottom",
                fontweight="bold" if t == BLANK else "normal")
        ax.text(max(n / top, 0) + 0.03, y, f"{st}/{n}", va="center", fontsize=12, color=tcol(t) if t else INK)
    ax.text(0, 7.05, title, fontsize=12, fontweight="bold", color=INK)
    ax.set_xlim(0, 1.6); ax.set_ylim(0.5, 7.4); ax.axis("off")
    return ax


# ---------------------------------------------------------------- C1 ridgelines per verification level
def c1(pp, f):
    fig, ax = plt.subplots(figsize=(16, 10)); fig.subplots_adjust(0.1, 0.1, 0.97, 0.86)
    og = np.linspace(0.35, 6.65, 600); GAP, H, SIG = 1.5, 1.1, 0.17          # GAP > H + rug: no peak reaches the next rug
    k1 = lambda os: sum(np.exp(-(og - o) ** 2 / (2 * SIG ** 2)) for o in os) if os else og * 0
    top = max(k1([p["o"] for p in pp if p["v"] == v]).max() for v in range(5))
    os_ = ostat(pp)
    for o, (n, st) in enumerate(os_, 1):                                   # the blank columns, behind the ridges
        if tag(n, st) == BLANK:
            ax.axvspan(o - 0.42, o + 0.42, color="#f7e4de", zorder=0, lw=0)
    yc = 2 * GAP + H + 0.12
    ax.axhline(yc, color=ACC, lw=1.4, ls=(0, (7, 4)), zorder=1)
    ax.text(-0.48, yc - 0.06, "强验证海岸线 ↑", color=ACC, ha="left", va="top", fontsize=12.5, fontweight="bold", zorder=1)
    for v in range(4, -1, -1):
        b = v * GAP; ps = [p for p in pp if p["v"] == v]; z = 20 - 3 * v
        a = k1([p["o"] for p in ps]) / top * H; strong = v >= 3
        ax.fill_between(og, b, b + a, color="white", zorder=z, lw=0)
        ax.fill_between(og, b, b + a, color=ACC if strong else "#cfd8dc", alpha=0.92 if strong else 1, zorder=z, lw=0)
        ax.plot(og, b + a, color="#5e1b10" if strong else INK, lw=1.6, zorder=z + 1, solid_capstyle="round")
        ax.plot([0.35, 6.65], [b, b], color=INK, lw=0.6, zorder=z + 1)
        for o in range(1, 7):                                             # autonomy rug under the baseline
            ls = sorted(p["l"] for p in ps if p["o"] == o)
            xs = o + (np.arange(len(ls)) - (len(ls) - 1) / 2) * min(0.022, 0.7 / max(len(ls), 1))
            for x, l in zip(xs, ls):
                ax.plot([x, x], [b - 0.24, b - 0.05], color=L_COL[l], lw=1.6, zorder=z + 2, solid_capstyle="butt")
            if ls:
                h = np.interp(o, og, a); side = h > 0.45
                ax.text(o + (0.27 if side else 0.05), b + (0.5 * h if side else h + 0.04), str(len(ls)), ha="left",
                        va="center" if side else "bottom", fontsize=12.5, fontweight="bold",
                        color="#7a2418" if strong else INK, zorder=40, path_effects=HALO)
        lab = f"{V_T[v]}\n{len(ps)} 篇" + ("　尚无" if not ps else "")
        ax.text(0.22, b + 0.06, lab, ha="right", va="bottom", fontsize=13, linespacing=1.35,
                color=ACC if strong else INK, fontweight="bold" if strong else "normal")
    for o, (n, st) in enumerate(os_, 1):
        t = tag(n, st)
        ax.text(o, -0.55, f"强 {st} / {n}" + (f"\n{t}" if t else ""), ha="center", va="top", fontsize=12.5,
                color=tcol(t), fontweight="bold" if t else "normal", linespacing=1.4)
    a4 = k1([p["o"] for p in pp if p["v"] == 4]) / top * H
    ax.set_xlim(-0.5, 6.7); ax.set_ylim(-1.3, 4 * GAP + max(a4.max(), 0.15) + 0.3)
    ax.set_xticks(range(1, 7), O_T, fontsize=13); ax.xaxis.tick_top(); ax.tick_params(length=0, pad=8)
    ax.set_yticks([]); ax.spines[:].set_visible(False)
    head(fig, f, "验证层山脊：每个验证等级一条开放度山脊线",
         "红脊 = 强验证；脊下竖线 = 每篇论文的自主性；粉色列 = 空白（仅声明）；底行 = 强验证/全部；灵感：ridge_map 脊线地图", pp)
    lkey(fig); save(fig, 1, "vridges", f)


# ---------------------------------------------------------------- C2 island map with bathymetry
YW = lambda y: 2.0 if y >= 2024 else 1.0                                 # C2 time axis: 2024-2026 drawn twice as wide
YC = {2013: 0.0}
for _y in range(2014, 2027):
    YC[_y] = YC[_y - 1] + (YW(_y - 1) + YW(_y)) / 2


def sea_run(row):
    """Centre index of the longest run of True in a 1-D mask (where to write a label in open sea)."""
    best, cur, st = (0, 0), 0, 0
    for i, m in enumerate(np.r_[row, False]):
        if m:
            st = i if cur == 0 else st; cur += 1
        else:
            if cur > best[0] - best[1]:
                best = (st + cur, st)
            cur = 0
    return (best[0] + best[1]) // 2, best[0] - best[1]


def c2(pp, f):
    fig, ax = plt.subplots(figsize=(16, 10)); fig.subplots_adjust(0.12, 0.1, 0.94, 0.86)
    x0, x1, y0, y1 = -0.6, YC[2026] + 1.1, 0.35, 6.75
    gx, gy = np.linspace(x0, x1, 900), np.linspace(y0, y1, 420)
    X, Y = np.meshgrid(gx, gy)
    def dens(sel=None):
        z = np.zeros_like(X)
        for (yr, o), n in C.Counter((p["year"], p["o"]) for p in pp if sel is None or sel(p)).items():
            z += n * np.exp(-(X - YC[yr]) ** 2 / (2 * (0.5 * YW(yr)) ** 2) - (Y - o) ** 2 / (2 * 0.25 ** 2))
        return z
    z = dens(); zs = dens(lambda p: p["v"] >= 3)
    TH = 0.4; land = z >= TH
    inx, iny = 0.82 * 16 / (x1 - x0), 0.76 * 10 / (y1 - y0)          # sea depth in page inches: even isobaths
    d = distance_transform_edt(~land, sampling=(np.diff(gy)[0] * iny, np.diff(gx)[0] * inx))
    sea_c = ["#eaf3f6", "#dcebf1", "#cee2ea", "#c0d8e3", "#b2cfdc"]
    rgb = np.array([to_rgb(sea_c[min(int(k), 4)]) for k in np.clip(d / 0.22, 0, 4).ravel()]).reshape(*d.shape, 3)
    hyp = LinearSegmentedColormap.from_list("hyp", ["#d6e4ba", "#bccf95", "#d3c48a", "#c09a63", "#9c6f4a", "#7a5236"])
    e = np.log1p(z) / np.log1p(max(z.max(), 1))
    hs = hill(np.log1p(z) * 0.5, dx=np.diff(gx)[0] * inx, dy=np.diff(gy)[0] * iny)[..., None]
    lr = np.clip(hyp(e)[..., :3] * (0.72 + 0.4 * hs), 0, 1)
    rgb[land] = lr[land]
    ax.imshow(rgb, extent=(x0, x1, y0, y1), origin="lower", aspect="auto", interpolation="bilinear", zorder=0)
    for k, w in enumerate([0.035, 0.075, 0.12, 0.17]):                     # old-map water-lining around every coast
        ax.contour(X, Y, d, levels=[w], colors=SEA, linewidths=0.7, alpha=0.55 - 0.11 * k, zorder=1)
    ax.contour(X, Y, d, levels=[0.44, 0.66], colors="white", linewidths=0.8, linestyles=":", zorder=1)
    ax.contour(X, Y, z, levels=[TH], colors="#3b4a3f", linewidths=1.1, zorder=3)
    ax.contour(X, Y, z, levels=[2, 5, 12, 25, 50], colors="#5e4a33", linewidths=0.5, alpha=0.55, zorder=3)
    if zs.max() >= TH:                                                     # strong territory: a border ribbon, land left visible
        ax.contourf(X, Y, zs, levels=[TH, 1e9], colors=[ACC], alpha=0.08, zorder=4)
        ax.contour(X, Y, zs, levels=[TH], colors=[ACC], linewidths=7, alpha=0.22, zorder=4)
        ax.contour(X, Y, zs, levels=[TH], colors=[ACC], linewidths=1.8, zorder=5)
    xb = [YC[2019] + 0.5, YC[2023] + 0.5]
    for x in xb:                                                           # eras as national borders
        ax.plot([x, x], [y0, y1], color="white", lw=4.5, zorder=6, solid_capstyle="butt")
        ax.plot([x, x], [y0, y1], color="#6b4a6b", lw=1.6, ls=(0, (9, 3, 2, 3)), zorder=7)
    for t, xc in zip([ERA_TICK[2], ERA_TICK[3], ERA_TICK[4] + "（横向 ×2）"], [(x0 + xb[0]) / 2, sum(xb) / 2, (xb[1] + x1) / 2]):
        ax.text(xc, 6.55, spaced(t) if "×" not in t else t, ha="center", va="center", fontsize=14, color="#6b4a6b",
                fontweight="bold", zorder=9, path_effects=HALO)
    for (yr, o), ps in cells(pp, "year", "o").items():                    # one settlement per paper
        dx, dy = spiral(len(ps), 0.1 + 0.06 * np.sqrt(len(ps)))
        for p, a, b in zip(ps, dx, dy):
            ax.plot(YC[yr] + a * YW(yr) * 0.95, o + b * 0.5, "^" if p["v"] >= 3 else "o", ms=6.6 if p["v"] >= 3 else 5.2,
                    color=L_COL[p["l"]], mec="white", mew=0.6, zorder=8)
    st_ = ostat(pp); nblank = sum(tag(n, st) == BLANK for n, st in st_)
    for o, (n, st) in enumerate(st_, 1):
        t = tag(n, st); row = ~land[np.argmin(np.abs(gy - o))] & (gx > x0 + 1.2) & (gx < xb[0] - 0.25)
        i, run = sea_run(row)
        if t and run > 150 and (t == "无论文" or nblank <= 2):
            txt = spaced(f"O{o} · 无 人 海 域") if t == "无论文" else f"O{o} {BLANK}\n有岛屿，无强验证领地"
            ax.text(gx[i], o, txt, ha="center", va="center", fontsize=15 if t == "无论文" else 14,
                    style="italic" if t == "无论文" else "normal", color=SEA if t == "无论文" else ACC,
                    fontweight="normal" if t == "无论文" else "bold", zorder=9, path_effects=HALO, linespacing=1.4)
        ax.text(x1 + 0.15, o, f"{st}/{n}", ha="left", va="center", fontsize=12.5, color=tcol(t), fontweight="bold")
    if not sum(st for _, st in st_):
        ax.text((x0 + xb[0]) / 2, 5.0, "本学科尚无强验证领地\n各开放度均为空白（仅声明）", ha="center", va="center", fontsize=15,
                color=ACC, fontweight="bold", zorder=9, path_effects=HALO, linespacing=1.5)
    ax.text(x1 + 0.15, 6.55, "强/全部", ha="left", va="center", fontsize=12, color=MUTED)
    sy = 0.45                                                              # two scale bars: the axis changes scale in 2024
    for xa, w, lab in [(0.0, 1.0, "1 年（≤2023）"), (2.3, 2.0, "1 年（2024–2026）")]:
        ax.add_patch(Rectangle((xa, sy), w, 0.07, fc=INK, ec=INK, lw=0.8, zorder=9))
        ax.text(xa + w / 2, sy + 0.14, lab, ha="center", fontsize=12, color=INK, zorder=9, path_effects=HALO)
    ax.annotate("", (0.4, 5.7), (0.4, 4.85), arrowprops=dict(arrowstyle="-|>,head_width=0.5,head_length=1",
                                                            color=INK, lw=1.5), zorder=9)
    ax.text(0.4, 5.78, "N\n更开放", ha="center", va="bottom", fontsize=12, color=INK, fontweight="bold", linespacing=1.1)
    ax.set_xlim(x0, x1); ax.set_ylim(y0, y1)
    ax.set_xticks([YC[y] for y in range(2013, 2027)], [str(y) for y in range(2013, 2027)], fontsize=12)
    ax.set_yticks(range(1, 7), O_T, fontsize=13)
    ax.tick_params(length=4, color=INK, direction="in", top=True, right=True, pad=7)
    for sp in ax.spines.values():
        sp.set_linewidth(1.6); sp.set_color(INK)
    ax.add_patch(Rectangle((0.005, 0.008), 0.99, 0.984, transform=ax.transAxes, fill=False, ec=INK, lw=0.5, zorder=10))
    head(fig, f, "群岛图：开放度 × 年份的论文陆地",
         "陆地 = 论文密度；红色边带 = 强验证领地；▲ 强验证 ● 仅声明；点画线国界 = 时代；灵感：Imhof 等深线与水纹线", pp)
    lkey(fig); save(fig, 2, "islands", f)


# ---------------------------------------------------------------- C3 oblique shaded relief (rayshader-like)
def ray_shadow(Z, dx, dy, azs=(245, 255, 265), alts=(22, 28, 34), steps=120):
    """Soft cast shadow (0 lit .. 1 dark): march toward the sun from every cell over several sun positions,
    the way rayshader's ray_shade does; row 0 is the south edge."""
    ny, nx = Z.shape; ii, jj = np.mgrid[0:ny, 0:nx].astype(float); out = np.zeros_like(Z)
    ds = min(dx, dy)
    for az in azs:
        for al in alts:
            ux, uy = np.sin(np.radians(az)), np.cos(np.radians(az)); tn = np.tan(np.radians(al)); sh = np.zeros_like(Z, bool)
            for k in range(1, steps):
                t = k * ds; r, c = ii + uy * t / dy, jj + ux * t / dx
                zs = map_coordinates(Z, [r, c], order=1, mode="nearest")
                sh |= zs > Z + t * tn + 1e-3
            out += sh
    return out / (len(azs) * len(alts))


def c3(pp, f):
    from mpl_toolkits.mplot3d import proj3d
    from matplotlib.lines import Line2D
    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_axes([-0.1, -0.1, 1.2, 1.2], projection="3d", computed_zorder=False)
    o0, o1, v0, v1 = 0.3, 6.7, -0.7, 4.7
    go, gv = np.linspace(o0, o1, 200), np.linspace(v0, v1, 170); O, V = np.meshgrid(go, gv)
    z = kde(pp, O, V, sx=0.34, sy=0.34); ZH = 1.9; Z = z / z.max() * ZH
    dx, dy = go[1] - go[0], gv[1] - gv[0]
    sage = LinearSegmentedColormap.from_list("sg", ["#a9bca3", "#c6d2a8", "#e2dfb6", "#f3ead0", "#fbf6ea"])
    terra = LinearSegmentedColormap.from_list("tr", ["#ddb09f", "#e6bba7", "#eec3ae", "#f6dccc", "#fdf1e9"])
    t = np.clip(Z / ZH, 0, 1) ** 0.6; strong = np.clip((V - 2.5) / 0.12 + 0.5, 0, 1)[..., None]
    base = sage(t)[..., :3] * (1 - strong) + terra(t)[..., :3] * strong     # claims side sage, strong side terracotta
    hs = hill(Z, az=255, alt=38, ve=1.3, dx=dx, dy=dy)[..., None]
    sh = ray_shadow(Z, dx, dy)[..., None]
    shade_c = np.array(to_rgb("#5d5a7a"))                                   # Imhof: blue-violet shadows, warm light
    rgb = np.clip((base * (0.62 + 0.48 * hs)) * (1 - 0.45 * sh) + shade_c * 0.25 * sh, 0, 1)
    ax.plot_surface(O, V, Z, facecolors=rgb, rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False, zorder=2)
    zb = -0.32                                                              # rayshader-style cut base (soil walls)
    for xs, ys, zt, col in [(go, np.full_like(go, v0), Z[0], "#6e5d4b"), (np.full_like(gv, o1), gv, Z[:, -1], "#4f4236")]:
        ax.plot_surface(np.vstack([xs, xs]), np.vstack([ys, ys]), np.vstack([zt, np.full_like(zt, zb)]), color=col,
                        shade=False, linewidth=0, zorder=1)
    ax.plot(go, np.full_like(go, v0), zb, color="#3a3027", lw=0.8, zorder=3)
    fz = RegularGridInterpolator((gv, go), Z)
    ax.plot(go, np.full_like(go, 2.5), fz(np.c_[np.full_like(go, 2.5), go]) + 0.012, color=ACC, lw=2.6, zorder=5)
    ax.text(o1 + 0.1, 2.5, zb + 0.05, "强验证海岸线", color=ACC, fontsize=13, fontweight="bold", zorder=50)
    st_ = ostat(pp); none = not sum(st for _, st in st_)
    if none:
        fig.text(0.87, 0.6, f"本学科尚无\n强验证论文\n各开放度均为\n{BLANK}", ha="center", va="center", fontsize=15,
                 fontweight="bold", color=ACC, linespacing=1.5)
    for k, (n, st) in enumerate(st_):
        tg = "" if none and n else tag(n, st)
        ax.text(k + 1, v0 - 0.35, zb, O_T[k] + (f"\n{tg}" if tg else ""), ha="center", va="top", fontsize=12.5,
                color=tcol(tg), fontweight="bold" if tg == BLANK else "normal", zorder=50, linespacing=1.3)
    for k in range(5):
        ax.text(o1 + 0.25, k, zb, V_T[k], ha="left", va="center", fontsize=12.5, zorder=50,
                color=ACC if k >= 3 else INK, fontweight="bold" if k >= 3 else "normal")
    ax.set_xlim(o0, o1); ax.set_ylim(v0, v1); ax.set_zlim(zb, ZH * 1.05)
    ax.set_box_aspect((o1 - o0, v1 - v0, 2.1), zoom=1.0); ax.view_init(elev=34, azim=-62); ax.set_axis_off()
    # callouts: summits are found in screen space, labels sit in a row above the relief on leader lines
    fig.canvas.draw(); M = ax.get_proj(); inv = fig.transFigure.inverted()
    def scr(x, y, zz):
        px, py, pz = proj3d.proj_transform(np.atleast_1d(x), np.atleast_1d(y), np.atleast_1d(zz), M)
        return inv.transform(ax.transData.transform(np.c_[px, py])), pz
    sxy, sd = scr(O[::2, ::2].ravel(), V[::2, ::2].ravel(), Z[::2, ::2].ravel())
    _, dn = scr(o1, v0, 0); _, df = scr(o0, v1, 0); sgn = 1 if df[0] > dn[0] else -1   # sgn * depth grows away from us
    g = cells(pp); top = sorted(g.items(), key=lambda t: -len(t[1]))[:6]
    pts = []
    for (o, v), ps in top:
        h = fz([[v, o]])[0]; (q,), (dq,) = scr(o, v, h)
        near = np.hypot(*(sxy - q).T) < 0.012
        hidden = bool(np.any(sgn * sd[near] < sgn * dq - 0.02))
        pts.append([q, o, v, ps, hidden])
    pts.sort(key=lambda t: t[0][0]); W, Y0 = 0.118, 0.8
    xs = [min(max(p[0][0], 0.08), 0.9) for p in pts]
    for _ in range(50):                                                    # push labels apart, keep them in the frame
        for i in range(1, len(xs)):
            if xs[i] - xs[i - 1] < W:
                m = (xs[i] + xs[i - 1]) / 2; xs[i - 1], xs[i] = m - W / 2, m + W / 2
        xs = [min(max(x, 0.08), 0.92) for x in xs]
    for x, (q, o, v, ps, hidden) in zip(xs, pts):
        col = ACC if v >= 3 else INK
        fig.add_artist(Line2D([x, x, q[0]], [Y0 - 0.012, Y0 - 0.03, q[1] + 0.008], color=col, lw=0.9,
                              ls=(0, (3, 2)) if hidden else "-", transform=fig.transFigure, zorder=60))
        fig.add_artist(Circle((q[0], q[1]), 0.0035, transform=fig.transFigure, fc="white" if hidden else col, ec=col,
                              lw=1.2, zorder=61))
        fig.text(x, Y0 + 0.035, f"O{o}·V{v}", ha="center", va="bottom", fontsize=13.5, fontweight="bold", color=col)
        fig.text(x, Y0 + 0.012, f"{len(ps)} 篇" + ("（山后）" if hidden else ""), ha="center", va="bottom", fontsize=12,
                 color=MUTED)
        cnt = C.Counter(p["l"] for p in ps); xa = x - 0.04
        for l in range(4):                                                 # autonomy mix of the cell
            if cnt[l]:
                w = 0.08 * cnt[l] / len(ps)
                fig.add_artist(Rectangle((xa, Y0 - 0.008), w, 0.009, transform=fig.transFigure, fc=L_COL[l], ec="white",
                                         lw=0.5, zorder=62)); xa += w
    head(fig, f, "斜视晕渲：开放度 × 验证强度的论文地貌",
         "海拔 = 论文密度；西南光照 + 投影软阴影；赭红坡 = 强验证区；标注条 = 该格自主性构成；灵感：rayshader / Imhof 晕渲", pp)
    lkey(fig); save(fig, 3, "relief", f)


# ---------------------------------------------------------------- C4 Swiss-minimal contour map
def c4(pp, f):
    fig, ax = plt.subplots(figsize=(16, 10)); fig.subplots_adjust(0.09, 0.09, 0.76, 0.88)
    o0, o1, v0, v1 = 0.3, 6.7, -0.75, 4.75
    X, Y = np.meshgrid(np.linspace(o0, o1, 640), np.linspace(v0, v1, 550))
    z = kde(pp, X, Y, sx=0.34, sy=0.34); BR = "#9a6a43"
    ax.contour(X, Y, z, levels=[0.5], colors=BR, linewidths=0.6, linestyles=[(0, (1.5, 2))], zorder=2)   # auxiliary
    iv = nice_iv(z.max(), 24); lv = np.arange(iv, z.max(), iv)
    ax.contour(X, Y, z, levels=[l for l in lv if l % (5 * iv)], colors=BR, linewidths=0.55, zorder=2)
    idx = [l for l in lv if not l % (5 * iv)]
    if idx:                                                                 # index contours, every fifth line
        ci = ax.contour(X, Y, z, levels=idx, colors=BR, linewidths=1.35, zorder=2)
        ax.clabel(ci, fmt="%d", fontsize=12, colors=BR, inline_spacing=6)
    ax.plot([o0, o1], [2.5, 2.5], color=ACC, lw=1.2, ls=(0, (10, 3, 2, 3)), zorder=3)
    ax.text(o1 - 0.05, 2.56, spaced("强验证海岸线"), color=ACC, ha="right", va="bottom", fontsize=12.5, zorder=9, path_effects=HALO)
    ax.text(0.95, 4.3, spaced("强 验 证 高 地"), color="#8a4a3a", fontsize=17, ha="center", style="italic", zorder=9)
    ax.text(5.0, -0.42, spaced("仅 声 明 低 地"), color="#5f6e78", fontsize=17, ha="center", style="italic", zorder=9)
    g = cells(pp); cnt = {k: len(v) for k, v in g.items()}
    for (o, v), ps in g.items():
        n = len(ps); peak = all(cnt.get(nb, 0) < n for nb in [(o + 1, v), (o - 1, v), (o, v + 1), (o, v - 1)])
        pie(ax, o, v, [p["l"] for p in ps], 0.05 + 0.017 * np.sqrt(n), z=8)
        if peak and n >= 10:
            r = 0.05 + 0.017 * np.sqrt(n); up = not (v < 2.5 < v + r + 0.6)   # a label that would cross the coast goes below
            ax.plot(o, v + r + 0.1, marker="^", ms=8, color=INK, zorder=9)
            ax.text(o, v + r + 0.23 if up else v - r - 0.1, f"O{o}·V{v} 峰  {n} 篇", ha="center", va="bottom" if up else "top",
                    fontsize=14.5,
                    fontweight="bold", color=ACC if v >= 3 else INK, zorder=10,
                    bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="none"))
        else:
            ax.text(o + 0.1 + 0.017 * np.sqrt(n), v - 0.06, f"{n}", ha="left", va="top", fontsize=12.5, style="italic",
                    color=ACC if v >= 3 else INK, zorder=10, path_effects=HALO)
    st_ = ostat(pp); none = not sum(st for _, st in st_)
    if none:                                                               # no strong case at all: one banner, not six boxes
        ax.add_patch(Rectangle((0.45, 2.8), 6.1, 1.2, fill=False, ec=ACC, lw=1.1, ls=(0, (3, 2)), zorder=4))
        ax.text(3.5, 3.4, f"本学科尚无强验证论文\n各开放度均为{BLANK}", ha="center", va="center", color=ACC, fontsize=15,
                fontweight="bold", linespacing=1.5, zorder=9, path_effects=HALO)
    for o, (n, st) in enumerate(st_, 1):
        t = tag(n, st)
        if t == BLANK and not none:
            ax.add_patch(Rectangle((o - 0.4, 2.62), 0.8, 2.0, fill=False, ec=ACC, lw=1.1, ls=(0, (3, 2)), zorder=4))
            ax.text(o, 3.62, f"O{o} 空白\n（仅声明）\n{n} 篇\n无一强验证", ha="center", va="center", color=ACC, fontsize=12.5,
                    fontweight="bold", linespacing=1.4, zorder=9)
        elif t == "无论文":
            ax.text(o - 0.4, 1.0, spaced("无 论 文"), ha="center", va="center", color="#a39d90", fontsize=12, rotation=90, zorder=9)
    ax.set_xlim(o0, o1); ax.set_ylim(v0, v1); ax.set_aspect("equal")
    ax.set_xticks(range(1, 7), O_T, fontsize=13); ax.set_yticks(range(5), V_T, fontsize=13)
    for t in ax.get_yticklabels()[3:]:
        t.set_color(ACC)
    ax.tick_params(length=5, direction="in", top=True, right=True, color=INK, pad=7)
    for s in ax.spines.values():
        s.set_linewidth(1.4)
    ax.add_patch(Rectangle((0.006, 0.008), 0.988, 0.984, transform=ax.transAxes, fill=False, ec=INK, lw=0.5, zorder=10))
    oside(fig, pp, [0.8, 0.3, 0.17, 0.5])
    fig.text(0.8, 0.24, f"等高距 {iv}（单篇峰值 = 1）\n粗线 = 计曲线，每 {5 * iv} 一条\n点线 = 0.5 辅助等高线", fontsize=12,
             color=MUTED, va="top", linespacing=1.6)
    head(fig, f, "瑞士极简等高线：开放度 × 验证强度",
         "只留等高线与高程点；▲ 峰 = 局部最高格；饼 = 该格自主性构成；灵感：瑞士国家地形图（swisstopo / Imhof）", pp)
    lkey(fig); save(fig, 4, "swiss", f)


# ---------------------------------------------------------------- C5 Tanaka illuminated contours
def c5(pp, f):
    fig, ax = plt.subplots(figsize=(16, 10)); fig.subplots_adjust(0.09, 0.09, 0.76, 0.88)
    o0, o1, v0, v1 = 0.3, 6.7, -0.75, 4.75
    go, gv = np.linspace(o0, o1, 760), np.linspace(v0, v1, 650); X, Y = np.meshgrid(go, gv)
    z = kde(pp, X, Y, sx=0.36, sy=0.36)
    iv = nice_iv(z.max(), 24); lv = np.r_[0.5, np.arange(iv, z.max(), iv)]     # equal interval + one 0.5 shoreline
    band = np.digitize(z, lv)                                             # 0 = below the lowest contour
    cool = LinearSegmentedColormap.from_list("c", ["#7d8b97", "#97a4ad", "#b4bec3", "#d2d7d6", "#ecece6"])
    warm = LinearSegmentedColormap.from_list("w", ["#8c7f80", "#a8918b", "#c4a597", "#dcbfae", "#f2e2d4"])
    t = band / len(lv); wmix = np.clip((Y - 2.5) / 0.12 + 0.5, 0, 1)[..., None]
    rgb = cool(t)[..., :3] * (1 - wmix) + warm(t)[..., :3] * wmix
    ax.imshow(rgb, extent=(o0, o1, v0, v1), origin="lower", interpolation="nearest", zorder=0)
    gy, gx = np.gradient(z, gv, go)
    gi = RegularGridInterpolator((gv, go), np.stack([gx, gy], -1), bounds_error=False, fill_value=0)
    cs = ax.contour(X, Y, z, levels=lv, alpha=0)
    lt = np.array([-1.0, 1.0]) / np.sqrt(2)                               # direction toward the light: north-west
    segs, cols, wids = [], [], []
    for lev in cs.allsegs:
        for sg in lev:
            if len(sg) < 2:
                continue
            mid = (sg[1:] + sg[:-1]) / 2; g = gi(mid[:, ::-1]); nrm = -g / (np.linalg.norm(g, axis=1, keepdims=True) + 1e-12)
            d = nrm @ lt
            for a, b, dd in zip(sg[:-1], sg[1:], d):
                segs.append([a, b]); wids.append(0.35 + 2.4 * abs(dd))
                cols.append((1, 1, 1, 0.95) if dd > 0 else (0.11, 0.13, 0.16, 0.9))
    cs.remove()
    ax.add_collection(LineCollection(segs, colors=cols, linewidths=wids, capstyle="round", zorder=2))
    ax.plot([o0, o1], [2.5, 2.5], color=ACC, lw=1.8, ls=(0, (7, 3)), zorder=3)
    ax.text(o1 - 0.06, 2.57, "强验证海岸线", color=ACC, ha="right", va="bottom", fontsize=12.5, fontweight="bold", zorder=9,
            path_effects=HALO)
    g = cells(pp)
    for (o, v), ps in g.items():
        n = len(ps); big = n >= 10
        ax.text(o, v, str(n), ha="center", va="center", fontsize=15 if big else 12.5, fontweight="bold",
                color="#5e1b10" if v >= 3 else INK, zorder=6, path_effects=[pe.withStroke(linewidth=3, foreground="#f6f2ea")])
        lc = C.Counter(p["l"] for p in ps); xs = o - 0.05 * (len(lc) - 1) + 0.1 * np.arange(len(lc))
        for x, (l, _) in zip(xs, sorted(lc.items())):                       # which autonomy levels live here
            ax.plot(x, v - (0.23 if big else 0.18), "s", ms=5, color=L_COL[l], mec="white", mew=0.5, zorder=6)
    st_ = ostat(pp)
    if not sum(st for _, st in st_):
        ax.text(3.5, 4.35, f"本学科尚无强验证论文：各开放度均为{BLANK}", ha="center", va="center", fontsize=14,
                fontweight="bold", color=ACC, zorder=9, path_effects=HALO)
    else:
        for o, (n, st) in enumerate(st_, 1):
            tg = tag(n, st)
            if tg:
                ax.text(o, 4.35, f"O{o}\n{tg}", ha="center", va="center", fontsize=13, fontweight="bold", zorder=9,
                        linespacing=1.3, color=ACC if tg == BLANK else "#efece6",
                        path_effects=HALO if tg == BLANK else [pe.withStroke(linewidth=3, foreground="#6e6667")])
    ax.set_xlim(o0, o1); ax.set_ylim(v0, v1); ax.set_aspect("equal")
    ax.set_xticks(range(1, 7), O_T, fontsize=13); ax.set_yticks(range(5), V_T, fontsize=13)
    for t_ in ax.get_yticklabels()[3:]:
        t_.set_color(ACC)
    ax.tick_params(length=0, pad=8); ax.spines[:].set_visible(False)
    oside(fig, pp, [0.8, 0.3, 0.17, 0.5])
    fig.text(0.8, 0.24, f"等高距 {iv}（单篇峰值 = 1）\n最外一圈 = 0.5，勾出有论文之处\n方块 = 该格出现的自主性等级",
             fontsize=12, color=MUTED, va="top", linespacing=1.6)
    head(fig, f, "田中光照等高线：开放度 × 验证强度",
         "西北光源：迎光坡等高线亮白、背光坡黑，线宽随朝向变化；暖色带 = 强验证；等距等高线；灵感：田中吉郎 Tanaka 1950", pp)
    lkey(fig); save(fig, 5, "tanaka", f)


# ---------------------------------------------------------------- C6 polar topography
TH0, SPAN = np.radians(240), np.radians(300)                           # O1 at lower left, clockwise over the top
th = lambda o: TH0 - (np.asarray(o, float) - 0.4) / 6.2 * SPAN
rr = lambda v: 1.5 + (np.asarray(v, float) + 0.7) * 0.92                # V0 near the hub, V4 at the rim


def c6(pp, f):
    fig = plt.figure(figsize=(16, 10)); ax = fig.add_axes([0.02, 0.06, 0.7, 0.83])
    R = 9.4; gx = np.linspace(-R, R, 900); X, Y = np.meshgrid(gx, gx)
    r = np.hypot(X, Y); d = (TH0 - np.arctan2(Y, X)) % (2 * np.pi)
    O = 0.4 + d / SPAN * 6.2; V = (r - 1.5) / 0.92 - 0.7
    ok = (d <= SPAN) & (V >= -0.7) & (V <= 4.7)
    z = kde(pp, O, V, sx=0.34, sy=0.34) * ok
    imhof = LinearSegmentedColormap.from_list("im", ["#c9d8d6", "#cfdcc4", "#dfe0b8", "#efe3bf", "#f8efd9", "#fffbf2"])
    base = imhof(np.clip(np.sqrt(z / z.max()), 0, 1))[..., :3]
    hs = hill(np.sqrt(z) * 0.9, az=315, alt=40, dx=gx[1] - gx[0], dy=gx[1] - gx[0])[..., None]
    rgb = base * (0.7 + 0.38 * hs) + np.array(to_rgb("#6b6896")) * 0.18 * (1 - hs)       # Imhof: violet shade
    rgb = np.where(ok[..., None], np.clip(rgb, 0, 1), 1.0)
    ax.imshow(rgb, extent=(-R, R, -R, R), origin="lower", interpolation="bilinear", zorder=0)
    zc = np.where(ok, z, np.nan)
    ax.contour(X, Y, zc, levels=[0.5, 2, 5, 10, 15, 20, 25, 30], colors="#7a5f45", linewidths=0.6, alpha=0.75, zorder=2)
    ta = np.linspace(th(0.4), th(6.6), 400)
    for v in range(5):                                                     # graticule: one ring per V level
        ax.plot(rr(v) * np.cos(ta), rr(v) * np.sin(ta), color="white", lw=0.7, alpha=0.8, zorder=1)
    for o in np.arange(0.5, 7, 1):
        ax.plot([rr(-0.7) * np.cos(th(o)), rr(4.7) * np.cos(th(o))], [rr(-0.7) * np.sin(th(o)), rr(4.7) * np.sin(th(o))],
                color="white", lw=0.7, alpha=0.8, zorder=1)
    ax.plot(rr(2.5) * np.cos(ta), rr(2.5) * np.sin(ta), color=ACC, lw=1.8, ls=(0, (7, 3)), zorder=4)
    for e in (-0.7, 4.7):
        ax.plot(rr(e) * np.cos(ta), rr(e) * np.sin(ta), color=INK, lw=1.0, zorder=4)
    for a in (th(0.4), th(6.6)):
        ax.plot([rr(-0.7) * np.cos(a), rr(4.7) * np.cos(a)], [rr(-0.7) * np.sin(a), rr(4.7) * np.sin(a)], color=INK, lw=1.0, zorder=4)
    g = cells(pp)
    for (o, v), ps in g.items():                                          # one dot per paper, spread inside its cell
        dx, dy = spiral(len(ps), 0.1 + 0.05 * np.sqrt(len(ps)))
        for p, a, b in zip(ps, dx, dy):
            t, q = th(o + a * 0.9), rr(v + b * 0.9)
            ax.plot(q * np.cos(t), q * np.sin(t), "^" if v >= 3 else "o", ms=5.2 if v >= 3 else 4.2, color=L_COL[p["l"]],
                    mec="white", mew=0.5, zorder=6)
    st_ = ostat(pp); top = max(n for n, _ in st_); r0 = rr(4.7) + 0.15; W = 1.35
    for o, (n, st) in enumerate(st_, 1):                                   # rim histogram: papers per openness level
        a0, a1 = np.degrees(th(o + 0.36)), np.degrees(th(o - 0.36))
        if n:
            ax.add_patch(Wedge((0, 0), r0 + W * n / top, a0, a1, width=W * n / top, fc="#d9d4ca", ec="none", zorder=3))
        if st:
            ax.add_patch(Wedge((0, 0), r0 + W * st / top, a0, a1, width=W * st / top, fc=ACC, ec="none", zorder=3))
        t = th(o); tg = tag(n, st); rl = r0 + W * n / top + 0.35
        ha = "left" if np.cos(t) > 0.2 else "right" if np.cos(t) < -0.2 else "center"
        ax.text(rl * np.cos(t), rl * np.sin(t), f"{O_T[o - 1]}\n强 {st} / {n}" + (f"　{tg}" if tg else ""), ha=ha,
                va="bottom" if np.sin(t) > 0.3 else "top" if np.sin(t) < -0.3 else "center", fontsize=12, linespacing=1.4,
                color=tcol(tg), fontweight="bold" if tg else "normal", zorder=9)
    for v in range(5):                                                     # ring labels in the open wedge at the bottom
        ax.text(0, -rr(v), V_T[v], ha="center", va="center", fontsize=11.5, zorder=9,
                color=ACC if v >= 3 else INK, fontweight="bold" if v >= 3 else "normal")
    ax.text(0, -rr(2.5), "— 强验证海岸线 —", ha="center", va="center", fontsize=10.5, color=ACC, zorder=9)
    ax.text(0, 0.15, FZH[f], ha="center", va="center", fontsize=17, fontweight="bold", color=INK)
    ax.text(0, -0.55, f"{len(pp)} 篇", ha="center", va="center", fontsize=12, color=MUTED)
    ax.set_xlim(-9.3, 9.3); ax.set_ylim(-6.0, 8.6); ax.set_aspect("equal"); ax.axis("off")
    fig.text(0.74, 0.62, "读图", fontsize=14, fontweight="bold", color=INK)
    fig.text(0.74, 0.6, "角度 = 开放度 O1→O6（顺时针）\n半径 = 验证强度，越外越强\n红色虚圈外 = 强验证（V3–V4）\n"
             "地貌 = 论文密度，西北光照晕渲\n外圈柱 = 每个开放度的论文数，红 = 强验证\n▲ 强验证论文　● 仅声明；颜色 = 自主性",
             fontsize=12, color=MUTED, va="top", linespacing=1.9)
    head(fig, f, "极坐标地貌：开放度为方位，验证为半径",
         "一圈一个验证等级、一扇一个开放度；外圈越红越扎实；灵感：方位投影岛图 + Imhof 紫影晕渲", pp)
    lkey(fig); save(fig, 6, "polar", f)


# ---------------------------------------------------------------- C7 extruded hexagonal elevation map
def c7(pp, f):
    fig, ax = plt.subplots(figsize=(16, 10)); fig.subplots_adjust(0.06, 0.07, 0.78, 0.89)
    s, KY, KZ, VB = 0.115, 0.95, 1.25, 4.62                                # hex radius, ground tilt, extrusion, back edge
    w, hstep = np.sqrt(3) * s, 1.5 * s
    rows = np.arange(-0.62, 4.65, hstep)
    gyv = lambda v: (VB - np.asarray(v, float)) * KY                       # V4 in front, V0 at the back: strong rows unhidden
    hexs = []
    for i, v in enumerate(rows):
        for o in np.arange(0.38 + (w / 2 if i % 2 else 0), 6.65, w):
            hexs.append((o, v, i))
    HO, HV = np.array([h[0] for h in hexs]), np.array([h[1] for h in hexs])
    Z = kde(pp, HO, HV, sx=0.34, sy=0.34); zmax = max(Z.max(), 1)
    H = np.clip(Z / zmax, 0, 1) ** 0.7 * KZ * (Z > 0.3)
    red = LinearSegmentedColormap.from_list("r", ["#f3dfd6", "#d9826b", "#b2412f", "#6e1f14"])
    sla = LinearSegmentedColormap.from_list("s", ["#e9ecec", "#a9b8c0", "#5f7887", "#2f4656"])
    ang = np.radians(np.arange(30, 360, 60))                                # pointy-top: 30, 90, ..., 330
    hit = C.defaultdict(list)                                              # papers dropped onto their nearest hex
    for (o, v), ps in cells(pp).items():
        dx, dy = spiral(len(ps), 0.08 + 0.055 * np.sqrt(len(ps)))
        for p, a, b in zip(ps, dx, dy):
            hit[int(np.argmin((HO - o - a) ** 2 + (HV - v - b) ** 2))].append(p["l"])
    zr = lambda v: 10 + (v + 1) * 10
    for v in range(5):                                                     # row guides on the ground, out to the labels
        ax.plot([-0.05, 6.75], [gyv(v)] * 2, color="#cfc9bd", lw=0.8, ls=(0, (2, 3)), zorder=zr(v - 0.2))
    for i, v in enumerate(rows):
        polys, cols = [], []
        for k in np.where(np.isclose(HV, v))[0]:
            o, h = HO[k], H[k]; vx = o + s * 0.97 * np.cos(ang); vy = gyv(v) - s * 0.97 * np.sin(ang) * KY
            t = h / KZ; cm = red if v >= 2.5 else sla
            top = np.array(cm(0.08 + 0.92 * t)[:3]) if h > 0 else np.array(to_rgb("#f4f1ea" if v < 2.5 else "#f8ece6"))
            if h > 0:
                for a, b, sh in [(1, 2, 0.78), (0, 1, 0.6)]:              # the two faces whose base is nearest the viewer
                    polys.append([(vx[a], vy[a] + h), (vx[b], vy[b] + h), (vx[b], vy[b]), (vx[a], vy[a])])
                    cols.append(tuple(top * sh))
            polys.append(list(zip(vx, vy + h))); cols.append(tuple(top))
        ax.add_collection(PolyCollection(polys, facecolors=cols, edgecolors=(1, 1, 1, 0.55), linewidths=0.35, zorder=zr(v)))
        for k in np.where(np.isclose(HV, v))[0]:
            ls = sorted(hit.get(k, []))
            if ls:
                cx, cy = HO[k], gyv(v) + H[k]; m = len(ls)
                offs = [(0, 0)] if m == 1 else [(0.042 * np.cos(2 * np.pi * j / m), 0.03 * np.sin(2 * np.pi * j / m)) for j in range(m)]
                for l, (a, b) in zip(ls, offs):
                    ax.plot(cx + a, cy + b, "o", ms=3.8, color=L_COL[l], mec="white", mew=0.4, zorder=zr(v) + 1)
    for xa, xb in [(-0.05, 0.3), (6.68, 6.85)]:
        ax.plot([xa, xb], [gyv(2.5)] * 2, color=ACC, lw=1.8, zorder=400)
    ax.text(6.9, gyv(2.5), "强验证海岸线\n↓ 前排 = 强验证", color=ACC, fontsize=12.5, fontweight="bold", va="center", zorder=200,
            linespacing=1.4)
    placed = []
    for (o, v), ps in sorted(cells(pp).items(), key=lambda t: -len(t[1]))[:6]:   # name the six largest cells
        hm = H[(np.abs(HO - o) < 0.3) & (np.abs(HV - v) < 0.3)].max(); y = y0 = gyv(v) + hm + 0.08
        while any(abs(o - a) < 1.1 and abs(y - b) < 0.26 for a, b in placed):
            y += 0.27
        placed.append((o, y))
        if y > y0:                                                         # pushed up: a leader back to its own column
            ax.plot([o, o], [y - 0.02, y0 + 0.04], color=INK, lw=0.9, zorder=599)
        ax.text(o, y, f"O{o}·V{v}  {len(ps)}", ha="center", va="bottom", fontsize=12.5, fontweight="bold",
                color="#6e1f14" if v >= 3 else INK, zorder=600, path_effects=HALO)
    st_ = ostat(pp)
    if not sum(st for _, st in st_):
        ax.text(3.5, gyv(3.6), f"本学科尚无强验证论文：各开放度均为{BLANK}", ha="center", va="center", fontsize=14,
                fontweight="bold", color=ACC, zorder=700, path_effects=HALO)
    else:
        for o, (n, st) in enumerate(st_, 1):
            tg = tag(n, st)
            if tg:
                ax.text(o, gyv(3.75), f"O{o}\n{tg}", ha="center", va="center", fontsize=12.5, fontweight="bold", zorder=700,
                        color=tcol(tg), path_effects=HALO, linespacing=1.3)
    for v in range(5):
        ax.text(-0.1, gyv(v), V_T[v], ha="right", va="center", fontsize=12.5,
                color=ACC if v >= 3 else INK, fontweight="bold" if v >= 3 else "normal")
    for o in range(1, 7):
        ax.text(o, gyv(4.85), O_T[o - 1], ha="center", va="top", fontsize=12.5, color=INK)
    ax.set_xlim(-1.15, 7.9); ax.set_ylim(gyv(5.0), max(gyv(HV) + H) + 0.4); ax.set_aspect("equal"); ax.axis("off")
    oside(fig, pp, [0.8, 0.32, 0.17, 0.48])
    fig.text(0.8, 0.26, "六边形高度 ∝ 论文密度的 0.7 次方\n红柱 = 强验证区（V3–V4），置于前排\n柱顶圆点 = 每篇论文，颜色 = 自主性",
             fontsize=12, color=MUTED, va="top", linespacing=1.7)
    head(fig, f, "六边形高程图：开放度 × 验证强度",
         "每个六边形按所在点的论文密度拔高；虚线 = 各验证等级所在行；灵感：六边形网格高程图（hex elevation map）", pp)
    lkey(fig); save(fig, 7, "hex", f)


# ---------------------------------------------------------------- C8 "Unknown Pleasures" ridge map
def c8(pp, f):
    fig, ax = plt.subplots(figsize=(16, 10)); fig.subplots_adjust(0.17, 0.1, 0.8, 0.88)
    x0, x1 = 2012.4, 2026.8; gx = np.linspace(x0, x1, 700)
    lines = np.round(np.arange(0.5, 6.51, 0.1), 2); HM = 1.4
    zf = lambda o, sel=None: kde(pp, gx, np.full_like(gx, o), "year", "o", 0.42, 0.2, sel=sel)
    zmax = max(zf(o).max() for o in range(1, 7))
    ink, red = np.array(to_rgb(INK)), np.array(to_rgb(ACC))
    for era_x in (2019.5, 2023.5):
        ax.plot([era_x, era_x], [0.1, 7.1], color="#d8d2c6", lw=1, ls=(0, (2, 3)), zorder=0)
    for i, o in enumerate(lines[::-1]):
        z = zf(o); h = np.sqrt(z / zmax) * HM
        y = o + h; main = abs(o - round(o)) < 1e-6; zo = 2 * i + 1
        ax.fill_between(gx, o - 0.02, y, color="white", lw=0, zorder=zo)
        if main:                                                           # data: an openness level, black -> red by strong share
            zs = zf(o, sel=lambda p: p["v"] >= 3); frac = np.where(z > 0.05, zs / (z + 1e-9), 0)
            fm = (frac[1:] + frac[:-1]) / 2; cols = ink[None] * (1 - fm[:, None]) + red[None] * fm[:, None]
            seg = np.stack([np.c_[gx[:-1], y[:-1]], np.c_[gx[1:], y[1:]]], 1)
            ax.add_collection(LineCollection(seg, colors=cols, linewidths=2.3, capstyle="round", zorder=zo + 1))
        else:                                                              # interpolation between levels: not data, kept grey
            ax.plot(gx, y, color="#b3ada2", lw=0.6, zorder=zo + 1)
    for (yr, o), ps in cells(pp, "year", "o").items():                    # every paper, in its autonomy colour
        per = max(12, -(-len(ps) // 3)); dxp = min(0.068, 0.86 / per)      # at most three rows under each line
        for j, p in enumerate(ps):
            ax.plot(yr + (j % per - (per - 1) / 2) * dxp, o - 0.1 - (j // per) * 0.075, "o", ms=3.6 if dxp > 0.06 else 2.8, color=L_COL[p["l"]],
                    mec="white", mew=0.4, zorder=500)
    for o, (n, st) in enumerate(ostat(pp), 1):
        tg = tag(n, st)
        ax.text(x1 + 0.25, o, f"{O_T[o - 1]}", ha="left", va="center", fontsize=13, fontweight="bold", color=tcol(tg))
        ax.text(x1 + 0.25, o - 0.3, f"强 {st} / {n}" + (f"　{tg}" if tg else ""), ha="left", va="center", fontsize=12,
                color=tcol(tg) if tg else MUTED)
        ax.plot([x1 + 0.02, x1 + 0.18], [o, o], color=INK, lw=1.2)
    for t, xc in zip(ERA_TICK[2:], [2016.0, 2021.5, 2025.15]):
        ax.text(xc, -0.12, t, ha="center", va="top", fontsize=13, color=MUTED, fontweight="bold")
    for y in range(2013, 2027):
        ax.text(y, 0.2, str(y)[2:] if y != 2013 else "2013", ha="center", va="top", fontsize=12, color=INK)
    ax.set_xlim(x0, x1); ax.set_ylim(-0.5, 6.5 + HM * 0.55); ax.axis("off")
    fig.text(0.03, 0.66, "读图", fontsize=14, fontweight="bold", color=INK)
    fig.text(0.03, 0.635, "粗线 = 数据（O1–O6）\n细灰线 = 级间插值，非数据\n峰高 ∝ √论文数\n粗线由黑转红 =\n该处论文多为强验证\n"
             "线下圆点 = 每篇论文，\n颜色 = 自主性\n≤2012 本学科无论文", fontsize=12, color=MUTED, va="top", linespacing=1.85)
    head(fig, f, "未知的愉悦：开放度山脉的时间剖面",
         "横轴 = 年份，粗线 = 各开放度的论文数；红色 = 强验证占多数；灵感：Joy Division《Unknown Pleasures》/ ridge_map", pp)
    lkey(fig); save(fig, 8, "pleasures", f)


if __name__ == "__main__":
    f = (sys.argv[1:] or ["03"])[0]; pp = load(f)
    only = sys.argv[2:]
    for k, fn in enumerate([c1, c2, c3, c4, c5, c6, c7, c8], 1):
        if (str(k) in only) if only else (k in APPROVED):
            fn(pp, f)
