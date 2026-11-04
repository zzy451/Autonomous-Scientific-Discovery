"""Fig. A - Cross-domain atlas: hierarchical edge bundling over the three-level taxonomy.

Rings (inside out): third-level leaves, second-level, field. Arc length is proportional to
paper-field assignments. Each curve is one cross-field pair of a single paper, routed
leaf -> second -> field -> centre -> field -> second -> leaf and bundled (beta).
Usage: python3 fig_atlas.py [--dark]
"""
import sys, math, collections as C
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.patches import Wedge, Rectangle
from scipy.interpolate import BSpline
from matplotlib.textpath import TextToPath
from matplotlib.font_manager import FontProperties
import style as S

DARK = "--dark" in sys.argv
BG = "#0e1013" if DARK else S.SURF
T1 = "#ecebe6" if DARK else S.INK          # primary text
T2 = "#a9a59c" if DARK else S.INK2
MECH = S.MECH_DARK if DARK else S.MECH
W, H = 183.0, 150.0
CX, CY, R = 72.0, 74.0, 34.0
BETA = 0.82
GAP_F, GAP_S = 1.4, 0.35                    # degrees between fields / second-level


def spline(ctrl, n=70):
    ctrl = np.asarray(ctrl, float)
    p0, pn = ctrl[0], ctrl[-1]
    t = np.linspace(0, 1, len(ctrl))[:, None]
    ctrl = BETA * ctrl + (1 - BETA) * (p0 + t * (pn - p0))
    k = 3
    m = len(ctrl)
    knots = np.r_[np.zeros(k), np.linspace(0, 1, m - k + 1), np.ones(k)]
    return BSpline(knots, ctrl, k)(np.linspace(0, 1, n))


def polar(a, r):
    a = math.radians(a)
    return CX + r * math.cos(a), CY + r * math.sin(a)


_TTP = TextToPath()


def adv(txt, size, weight):
    """Advance width of a string in mm (matplotlib text layout, includes kerning)."""
    w, _, _ = _TTP.get_text_width_height_descent(txt, FontProperties(family="Arial", size=size, weight=weight),
                                                 ismath=False)
    return w / S.PT


def curved_text(ax, text, amid, r, size, color, weight="bold", track=0.12):
    """Characters along an arc centred on amid, using measured advances; flipped on the lower half."""
    lower = math.sin(math.radians(amid)) < -0.05
    total = adv(text, size, weight) + track * (len(text) - 1)
    sign = 1 if lower else -1                       # direction of reading along the arc
    a_start = amid - sign * math.degrees(total / r) / 2
    for i, ch in enumerate(text):
        x0 = adv(text[:i], size, weight) + track * i if i else 0.0
        cwid = adv(ch, size, weight)
        ac = a_start + sign * math.degrees((x0 + cwid / 2) / r)
        x, y = polar(ac, r)
        rot = ac + 90 if lower else ac - 90
        ax.text(x, y, ch, fontsize=size, color=color, ha="center", va="center", rotation=rot,
                rotation_mode="anchor", fontweight=weight, zorder=8)


def fits(text, size, span_deg, r):
    return adv(text, size, "bold") + 1.2 < math.radians(span_deg) * r


def short_title(t, n=27):
    t = t.split(":")[0].strip()
    if len(t) <= n:
        return t
    return t[:n].rsplit(" ", 1)[0] + "…"


def layout(cards):
    """Angular layout shared by the atlas and the wormhole: spans for third-level leaves,
    second-level and fields, plus one anchor angle per paper-field assignment."""
    asg =[(c["paper_id"], f, s or f + ".??", t or f + ".??.??") for c in cards for f, s, t in c["codes"]]
    n_t = C.Counter(t for _, _, _, t in asg)
    tree = C.defaultdict(lambda: C.defaultdict(list))
    for f, s, t in sorted({(f, s, t) for _, f, s, t in asg}):
        tree[f][s].append(t)
    n_secgaps = sum(len(tree[f]) - 1 for f in tree)
    deg_per = (360 - GAP_F * len(tree) - GAP_S * n_secgaps) / len(asg)
    span_t, span_s, span_f = {}, {}, {}
    a = 90.0                                 # start at 12 o'clock, run clockwise
    for f in S.FIELDS:
        fa = a
        for j, s in enumerate(sorted(tree[f])):
            sa = a
            for t in tree[f][s]:
                span_t[t] = (a, a - n_t[t] * deg_per)
                a -= n_t[t] * deg_per
            span_s[s] = (sa, a)
            if j < len(tree[f]) - 1:
                a -= GAP_S
        span_f[f] = (fa, a)
        a -= GAP_F
    # spread each leaf's assignments across its arc so curve ends fan out
    anchor = {}
    by_t = C.defaultdict(list)
    for pid, f, s, t in asg:
        by_t[t].append((pid, f))
    for t, lst in by_t.items():
        a0, a1 = span_t[t]
        for i, key in enumerate(sorted(lst)):
            anchor[key] = (a0 + (i + 0.5) / len(lst) * (a1 - a0), t)
    return asg, span_t, span_s, span_f, anchor, by_t


def main():
    cards = S.papercards()
    asg, span_t, span_s, span_f, anchor, by_t = layout(cards)
    mid = lambda sp: (sp[0] + sp[1]) / 2
    sec_of = {(pid, f): s for pid, f, s, _ in asg}

    fig = plt.figure(figsize=(W / 25.4, H / 25.4), facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    ax.set_facecolor(BG)

    # ---- curves ------------------------------------------------------------------
    segs = {m: [] for m in S.MECH_ORDER}
    for c in cards:
        fs = c["fields"]
        for i in range(len(fs)):
            for j in range(i + 1, len(fs)):
                u, v = (c["paper_id"], fs[i]), (c["paper_id"], fs[j])
                ctrl = [polar(anchor[u][0], R - 0.4), polar(mid(span_s[sec_of[u]]), R * 0.66),
                        polar(mid(span_f[fs[i]]), R * 0.34), (CX, CY),
                        polar(mid(span_f[fs[j]]), R * 0.34), polar(mid(span_s[sec_of[v]]), R * 0.66),
                        polar(anchor[v][0], R - 0.4)]
                segs[c["mechanism"]].append((spline(ctrl), len(fs)))
    for m in ["llm", "optimization", "hybrid", "classical"]:       # rarer mechanisms on top
        if not segs[m]:
            continue
        lines = [s for s, _ in segs[m]]
        lw = [0.32 if k <= 3 else 0.22 for _, k in segs[m]]
        ax.add_collection(LineCollection(lines, colors=MECH[m], linewidths=lw,
                                         alpha=(0.5 if DARK else 0.42) if m == "llm" else 0.8,
                                         capstyle="round", zorder=3))

    # ---- rings -------------------------------------------------------------------
    kmap = {c["paper_id"]: len(c["fields"]) for c in cards}
    xshare = {t: sum(kmap[p] > 1 for p, _ in lst) / len(lst) for t, lst in by_t.items()}
    lo, hi = ("#2a2d33", "#c9c4b8") if DARK else ("#ece7de", "#6b604f")
    for t, (a0, a1) in span_t.items():
        ax.add_patch(Wedge((CX, CY), R + 1.9, a1 + 0.08, a0 - 0.08, width=1.4,
                           fc=S.mix(lo, hi, xshare[t]), ec="none", zorder=4))
    sec_c = "#5d6068" if DARK else "#b3ab9d"
    for s, (a0, a1) in span_s.items():
        ax.add_patch(Wedge((CX, CY), R + 3.9, a1 + 0.1, a0 - 0.1, width=1.5, fc=sec_c, ec="none", zorder=4))
    fld_c = "#d8d5cd" if DARK else S.INK
    for f, (a0, a1) in span_f.items():
        ax.add_patch(Wedge((CX, CY), R + 8.6, a1, a0, width=4.1, fc=fld_c, ec="none", zorder=4))
        name = S.FSHORT[f] if fits(S.FSHORT[f], 5.2, a0 - a1, R + 6.45) else f
        curved_text(ax, name, mid((a0, a1)), R + 6.45, 5.2 if name != f else 4.6, BG)
    # second-level radial labels
    for s, (a0, a1) in span_s.items():
        if (a0 - a1) < 2.2 or s.endswith("??"):
            continue
        am = mid((a0, a1))
        x, y = polar(am, R + 10.0)
        flip = math.cos(math.radians(am)) < 0
        ax.text(x, y, S.SECNAME.get(s, s), fontsize=4.3, color=T2, rotation=am + (180 if flip else 0),
                rotation_mode="anchor", ha="right" if flip else "left", va="center", zorder=8)

    # ---- right column ------------------------------------------------------------
    x0 = 136
    ax.text(x0, H - 9, "Cross-domain atlas", fontsize=9, fontweight="bold", color=T1, va="top")
    ax.text(x0, H - 14, "Agent-for-science core corpus · snapshot 1 Nov 2026", fontsize=5.3, color=T2, va="top")
    n_multi = sum(len(c["fields"]) > 1 for c in cards)
    n_pairs = sum(len(c["fields"]) * (len(c["fields"]) - 1) // 2 for c in cards)
    stats = [(f"{n_pairs}", "cross-field pairs"), (f"{n_multi}", "papers in ≥2 fields"),
             (f"{len(asg)}", "paper–field assignments"), (f"{sum(not t.endswith('??') for t in span_t)}", "third-level categories")]
    y = H - 24
    for big, small in stats:
        ax.text(x0, y, big, fontsize=10, fontweight="bold", color=T1, va="baseline")
        ax.text(x0 + 13.5, y, small, fontsize=5.5, color=T2, va="baseline")
        y -= 6.2
    # breadth histogram
    y -= 2
    ax.text(x0, y, "Fields per paper (k)", fontsize=5.5, fontweight="bold", color=T1)
    kc = C.Counter(len(c["fields"]) for c in cards if len(c["fields"]) > 1)
    ks = list(range(2, 11))
    bar_w, maxh = 4.2, 12
    for i, k in enumerate(ks):
        h = maxh * math.sqrt(kc[k] / max(kc.values())) if kc[k] else 0
        bx = x0 + i * bar_w
        if h:
            ax.add_patch(Rectangle((bx, y - 3 - maxh), bar_w - 0.6, h, fc=T2, ec="none"))
            ax.text(bx + (bar_w - 0.6) / 2, y - 3 - maxh + h + 0.5, str(kc[k]), fontsize=4.4,
                    color=T1, ha="center", va="bottom")
        ax.text(bx + (bar_w - 0.6) / 2, y - 4.4 - maxh, str(k), fontsize=4.6, color=T2, ha="center", va="top")
    ax.text(x0 + len(ks) * bar_w + 0.5, y - 3 - maxh, "bar height ∝ √count", fontsize=4, color=T2,
            rotation=90, va="bottom")
    y -= maxh + 11
    ax.text(x0, y, "Broadest papers (k ≥ 5)", fontsize=5.5, fontweight="bold", color=T1)
    y -= 3.6
    for c in sorted(cards, key=lambda c: (-len(c["fields"]), c["paper_id"]))[:8]:
        nm = short_title(c["title"])
        ax.text(x0, y, f"{c['paper_id']}", fontsize=4.5, color=T2, va="baseline", family="Arial")
        ax.text(x0 + 11.5, y, f"{nm}", fontsize=4.7, color=T1, va="baseline")
        ax.text(W - 4, y, f"k={len(c['fields'])}", fontsize=4.5, color=T2, ha="right", va="baseline")
        y -= 3.3
    # legend
    y -= 3
    ax.text(x0, y, "Curve colour · decision mechanism of the paper", fontsize=5.3, fontweight="bold", color=T1)
    for m in S.MECH_ORDER:
        y -= 3.4
        ax.plot([x0, x0 + 4.5], [y + 0.6, y + 0.6], color=MECH[m], lw=1.1, solid_capstyle="round")
        ax.text(x0 + 6, y, S.MECH_LABEL[m], fontsize=4.8, color=T1, va="baseline")
    y -= 5.5
    for i in range(6):
        ax.add_patch(Rectangle((x0 + i * 3, y), 3, 1.6, fc=S.mix(lo, hi, i / 5), ec="none"))
    ax.text(x0 + 19.5, y + 0.8, "inner ring: share of a third-level\ncategory's papers that are cross-field",
            fontsize=4.4, color=T2, va="center", linespacing=1.25)
    ax.text(x0, y - 1.2, "0", fontsize=4.2, color=T2, va="top"); ax.text(x0 + 18, y - 1.2, "1", fontsize=4.2, color=T2, va="top", ha="right")
    S.save(fig, "fig_atlas_dark" if DARK else "fig_atlas")


if __name__ == "__main__":
    main()
