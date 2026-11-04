"""Cover · Tree rings of autonomous science (claim: rapid growth since 2024).
Rings = eras (area proportional to paper-field assignments); sectors = fields; dot = one assignment."""
import math, collections as C
import numpy as np
from matplotlib.patches import Circle, Wedge
import style as S, proxies as X, cover as V

ERAS = ["2004–2019", "2020–2023", "2024", "2025", "2026"]


def main():
    cards = S.papercards(); px = X.load()
    asg = [(f, c) for c in cards for f in c["fields"]]
    fig, ax = V.canvas()
    cx, cy, R, R0 = V.CX, V.CY, V.RMAX, 7.0
    n_era = C.Counter(c["era"] for _, c in asg)
    cum, radii = 0, {}
    for e in ERAS:
        # annulus area proportional to the era's assignments, around a small open core
        rad = lambda k: math.sqrt(R0 ** 2 + (R ** 2 - R0 ** 2) * k / len(asg))
        r0 = rad(cum); cum += n_era[e]
        radii[e] = (r0, rad(cum))
    span = V.sectors({f: sum(1 for g, _ in asg if g == f) for f in S.FIELDS})
    # faint sector wedges + ring boundaries
    for f, (a0, a1) in span.items():
        ax.add_patch(Wedge((cx, cy), R + 1.2, a1, a0, width=R + 1.2, fc=V.FAINT, ec="none", alpha=0.35, zorder=1))
        ax.add_patch(Wedge((cx, cy), R + 5.2, a1, a0, width=2.0, fc=V.TXT, ec="none", alpha=0.85, zorder=2))
        V.curved(ax, S.FSHORT[f] if (a0 - a1) > 14 else f, cx, cy, (a0 + a1) / 2, R + 9.0, 6.4, V.TXT)
    for e in ERAS:
        ax.add_patch(Circle((cx, cy), radii[e][1], fc="none", ec=V.DIM, lw=0.35, alpha=0.6, zorder=3))
    # dots: uniform-in-area Halton placement inside each era x field annular cell
    cells = C.defaultdict(list)
    for f, c in asg:
        cells[(c["era"], f)].append(c)
    xs, ys, cols, tiers = [], [], [], []
    for (e, f), lst in cells.items():
        r0, r1 = radii[e]; a0, a1 = span[f]
        for i, c in enumerate(sorted(lst, key=lambda c: c["paper_id"])):
            u, v = V.halton(i + 1, 2), V.halton(i + 1, 3)
            rr = math.sqrt(r0 ** 2 + (0.08 + 0.84 * v) * (r1 ** 2 - r0 ** 2))
            aa = a0 + (0.06 + 0.88 * u) * (a1 - a0)
            x, y = V.polar(cx, cy, aa, rr)
            xs.append(x); ys.append(y); cols.append(V.MECH[c["mechanism"]])
            tiers.append(px[c["paper_id"]][0] if px[c["paper_id"]][0] is not None else 0)
    V.marks(ax, xs, ys, cols, tiers, scale=0.92)
    # era labels on the vertical axis gap
    for e in ERAS:
        r0, r1 = radii[e]
        x, y = cx + 0.8, cy + (r0 + r1) / 2
        ax.text(x, y, e, fontsize=5.6, color=V.TXT, ha="left", va="center", fontweight="bold", zorder=31,
                bbox=dict(boxstyle="round,pad=0.18", fc=V.BG, ec="none", alpha=0.75))
    V.title(ax, "Growth since 2024", "Tree rings of autonomous science")
    ring = lambda a, x, y: a.add_patch(Circle((x, y), 1.4, fc="none", ec=V.DIM, lw=0.6))
    V.legend(ax, extra=("Rings  ·  era, area ∝ papers", [(ring, "2004–2019 at the core, 2026 outermost")]))
    V.footer(ax, "935 paper–field assignments · 662 core papers · snapshot 1 Nov 2026")
    V.save(fig, "cover_rings")


if __name__ == "__main__":
    main()
