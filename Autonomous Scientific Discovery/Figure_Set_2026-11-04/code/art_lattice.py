"""Glass plates of separated axes (proposal §2(1)). One isometric plate per era; on each plate a grid of
research-loop reach (L0-L4) x evidence endpoint (E0-E3). Each dot is a paper placed at its coordinate,
coloured by decision mechanism. Separating the axes gives every result a comparable coordinate."""
import math, collections as C
import numpy as np
from matplotlib.patches import Polygon
import style as S, proxies as X, cover as V

ERAS = ["2004–2019", "2020–2023", "2024", "2025", "2026"]
CS, GAP = 8.2, 24.5
C30, S30 = math.cos(math.radians(30)), math.sin(math.radians(30))


def iso(x, y, z, ox, oy):
    return ox + (x - y) * C30 * CS, oy + (x + y) * S30 * CS + z


def main():
    cards = S.papercards()
    px = {k: (v, L) for k, (o, v, L) in X.load_ov().items()}      # (verification V0-V4, autonomy L0-L3)
    fig, ax = V.canvas()
    ox, oy = 98.0, 42.0
    for k, e in enumerate(ERAS):
        z = k * GAP
        corners = [iso(0, 0, z, ox, oy), iso(4, 0, z, ox, oy), iso(4, 5, z, ox, oy), iso(0, 5, z, ox, oy)]
        ax.add_patch(Polygon(corners, closed=True, fc=V.TXT, ec=V.TXT, alpha=0.06, lw=0.0, zorder=1 + k))
        ax.add_patch(Polygon(corners, closed=True, fc="none", ec=V.DIM, lw=0.5, alpha=0.8, zorder=1.01 + k))
        for i in range(1, 4):
            a, b = iso(i, 0, z, ox, oy), iso(i, 5, z, ox, oy)
            ax.plot([a[0], b[0]], [a[1], b[1]], color=V.DIM, lw=0.25, alpha=0.5, zorder=1.02 + k)
        for j in range(1, 5):
            a, b = iso(0, j, z, ox, oy), iso(4, j, z, ox, oy)
            ax.plot([a[0], b[0]], [a[1], b[1]], color=V.DIM, lw=0.25, alpha=0.5, zorder=1.02 + k)
        lx, ly = iso(0, 5, z, ox, oy)
        ax.text(lx - 2, ly, e, fontsize=6.4, color=V.TXT, ha="right", va="center", fontweight="bold", zorder=20)
        cell = C.defaultdict(list)
        for c in cards:
            E, L = px[c["paper_id"]]
            if c["era"] == e and E is not None:
                cell[(L or 0, E)].append(c)
        n = sum(len(v) for v in cell.values())
        ax.text(lx - 2, ly - 3.4, f"{n} papers", fontsize=5.0, color=V.DIM, ha="right", va="center", zorder=20)
        xs, ys, cols, tiers = [], [], [], []
        for (L, E), lst in cell.items():
            for i, c in enumerate(sorted(lst, key=lambda c: c["paper_id"])):
                u, v = V.halton(i + 1, 2), V.halton(i + 1, 3)
                x, y = iso(L + 0.1 + 0.8 * u, E + 0.1 + 0.8 * v, z, ox, oy)
                xs.append(x); ys.append(y); cols.append(V.MECH[c["mechanism"]]); tiers.append(E)
        V.marks(ax, xs, ys, cols, [min(t, 3) for t in tiers], scale=0.62, z=2 + k)
        if k == 0:                                   # axis labels on the bottom plate
            for L in range(4):
                a = iso(L + 0.5, -0.35, z, ox, oy)
                ax.text(a[0], a[1] - 1.0, f"L{L}", fontsize=5.6, color=V.TXT, ha="center", va="top", fontweight="bold")
            for E in range(5):
                a = iso(4.35, E + 0.5, z, ox, oy)
                ax.text(a[0] + 0.8, a[1] - 0.6, f"V{E}", fontsize=5.6, color=V.TXT, ha="left", va="top", fontweight="bold")
            a = iso(2.5, -1.4, z, ox, oy)
            ax.text(a[0] - 3, a[1] - 2.5, "autonomy  L0 → L3", fontsize=5.0, color=V.DIM, ha="center", va="top", rotation=-30)
            a = iso(5.4, 2.5, z, ox, oy)
            ax.text(a[0] + 2, a[1] - 3.0, "verification  V0 → V4", fontsize=5.0, color=V.DIM, ha="center", va="top", rotation=30)
    V.title(ax, "Separating the axes  ·  §2(1)", "Every result gets a coordinate")
    plate = lambda a, x, y: a.add_patch(Polygon([(x - 1.8, y), (x, y + 1.1), (x + 1.8, y), (x, y - 1.1)],
                                                fc=V.TXT, alpha=0.25, ec=V.DIM, lw=0.4))
    V.legend(ax, extra=("Plates  ·  one per era, stacked in time", [(plate, "grid = autonomy × verification")]))
    V.footer(ax, "662 core papers · autonomy L0–L3 × verification V0–V4 · snapshot 1 Nov 2026")
    V.save(fig, "art_lattice")


if __name__ == "__main__":
    main()
