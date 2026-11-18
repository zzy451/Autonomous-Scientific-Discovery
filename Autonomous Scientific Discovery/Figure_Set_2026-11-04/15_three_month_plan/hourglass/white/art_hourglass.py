"""The hourglass of the plan (proposal §5: AI screening -> expert review -> dictionary).
Top bulb: the 662 core papers already screened (lit by mechanism and evidence). Neck: the papers that
need an expert judgement (E3 endpoint or L3-L4 reach). Bottom bulb: the proposal's planned review
capacity, 11 fields x 20 cases, drawn as empty slots: none has been adjudicated yet."""
import math
import numpy as np
from matplotlib.patches import Polygon, Circle
import style as S, proxies as X, cover as V

GA = 137.50776


def main():
    cards = S.papercards(); px = X.load()
    fig, ax = V.canvas()
    cx, neck_y = V.CX, 104.0
    # glass outline
    t = np.linspace(-1, 1, 200)
    half = lambda yy: 3.0 + 52 * (np.abs(yy) ** 1.6)
    ys = neck_y + 66 * t
    right = cx + half(t); left = cx - half(t)
    ax.plot(right, ys, color=V.TXT, lw=0.7, alpha=0.7); ax.plot(left, ys, color=V.TXT, lw=0.7, alpha=0.7)
    for yy in (neck_y + 66, neck_y - 66):
        ax.plot([cx - 55, cx + 55], [yy, yy], color=V.TXT, lw=1.2, alpha=0.8)
    # top bulb: core papers, sorted so strong evidence settles at the bottom (nearest the neck)
    ps = sorted(cards, key=lambda c: (-(px[c["paper_id"]][0] if px[c["paper_id"]][0] is not None else -1), c["paper_id"]))
    pts = []
    yy = neck_y + 8
    while len(pts) < len(ps):
        w = half((yy - neck_y) / 66) - 2.2
        n_row = max(1, int(2 * w / 2.05))
        for j in range(n_row):
            pts.append((cx - w + (j + 0.5) * 2 * w / n_row, yy))
        yy += 1.85
    xs, ys2, cols, tiers = [], [], [], []
    for (x, y), c in zip(pts, ps):
        xs.append(x); ys2.append(y); cols.append(V.MECH[c["mechanism"]])
        tiers.append(px[c["paper_id"]][0] if px[c["paper_id"]][0] is not None else 0)
    V.marks(ax, xs, ys2, cols, tiers, scale=0.8)
    # neck: stream of papers needing judgement
    need = [c for c in cards if px[c["paper_id"]][0] == 3 or (px[c["paper_id"]][1] or 0) >= 3]
    rng = np.random.default_rng(3)
    for i, c in enumerate(need[:120]):
        y = neck_y + 6 - i * 0.42
        x = cx + rng.normal(0, 0.6 + 0.02 * i)
        if y < neck_y - 44:
            break
        V.marks(ax, [x], [y], [V.MECH[c["mechanism"]]], [px[c["paper_id"]][0] or 0], scale=0.55, z=6)
    # bottom bulb: planned slots, 11 fields x 20
    k = 0
    for row in range(12):
        yb = neck_y - 64 + row * 2.4
        w = half((yb - neck_y) / 66) - 3
        n_row = max(1, int(2 * w / 2.6))
        for j in range(n_row):
            if k >= 220:
                break
            ax.add_patch(Circle((cx - w + (j + 0.5) * 2 * w / n_row, yb), 0.75, fc="none", ec=V.TXT, lw=0.4, alpha=0.7))
            k += 1
    lab = dict(fontsize=6.0, color=V.TXT, fontweight="bold", va="center")
    ax.text(cx + 60, neck_y + 40, "1  AI screening", **lab)
    ax.text(cx + 60, neck_y + 36, f"{len(cards)} core papers coded on\nfield, mechanism, evidence, reach",
            fontsize=5.2, color=V.DIM, va="top", linespacing=1.3)
    ax.text(cx + 60, neck_y + 2, "2  Expert review", **lab)
    ax.text(cx + 60, neck_y - 2, f"{len(need)} papers need a judgement\n(strong V3–V4 claim or L3 autonomy)",
            fontsize=5.2, color=V.DIM, va="top", linespacing=1.3)
    ax.text(cx + 60, neck_y - 50, "3  Dictionary", **lab)
    ax.text(cx + 60, neck_y - 54, "planned: 11 fields × 15–20 cases\nempty slots = not yet adjudicated",
            fontsize=5.2, color=V.DIM, va="top", linespacing=1.3)
    V.title(ax, "The three-month plan  ·  §5", "An hourglass of judgement")
    slot = lambda a, x, y: a.add_patch(Circle((x, y), 1.1, fc="none", ec=V.TXT, lw=0.5))
    V.legend(ax, extra=("Bottom bulb  ·  planned capacity", [(slot, "one empty slot per planned expert case (220)")]))
    V.footer(ax, "top and neck from the 1 Nov 2026 snapshot · bottom bulb from the proposal's plan")
    V.save(fig, "art_hourglass")


if __name__ == "__main__":
    main()
