"""Ternary drift (proposal §1: two instruments are unreliable; a third instrument is needed).
Each field's evidence mix per era as a point in the simplex (benchmark/expert, computed, physically or
formally closed), joined in time order; the bold path is the whole corpus. Cells with n < 4 are skipped."""
import math, collections as C
import numpy as np
from matplotlib.patches import Polygon, FancyArrowPatch
import style as S, proxies as X, cover as V

ERAS = ["2004–2019", "2020–2023", "2024", "2025", "2026"]
GOLD = "#a87a1e" if V.LIGHT else "#ffd27a"


def main():
    cards = S.papercards(); px = X.load()
    fig, ax = V.canvas()
    cx, cy, R = V.CX, V.CY - 10, 72.0
    A = np.array([cx, cy + R])                          # top: E3 closed
    B = np.array([cx - R * math.sin(math.radians(60)), cy - R / 2])   # left: benchmark / expert
    Cc = np.array([cx + R * math.sin(math.radians(60)), cy - R / 2])  # right: computed
    to_xy = lambda w3, w01, w2: w3 * A + w01 * B + w2 * Cc
    ax.add_patch(Polygon([A, B, Cc], closed=True, fc=V.FAINT, ec=V.DIM, lw=0.5, alpha=0.5, zorder=1))
    for t in (0.25, 0.5, 0.75):                         # grid
        for P, Q, Rr in ((A, B, Cc), (B, Cc, A), (Cc, A, B)):
            p1, p2 = P + t * (Q - P), P + t * (Rr - P)
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=V.DIM, lw=0.25, alpha=0.45, zorder=1.1)
    ax.text(*(A + [0, 4]), "Strongly verified", fontsize=6.5, color=V.TXT, ha="center", fontweight="bold")
    ax.text(*(A + [0, 1.2]), "V3–V4  ·  the third instrument", fontsize=5.0, color=V.DIM, ha="center")
    ax.text(*(B + [-2, -5]), "Claimed or benchmarked\nV0–V1 · instruments one and two", fontsize=5.6, color=V.TXT,
            ha="center", va="top", fontweight="bold", linespacing=1.3)
    ax.text(*(Cc + [2, -5]), "Computed or simulated\nV2", fontsize=5.6, color=V.TXT, ha="center", va="top",
            fontweight="bold", linespacing=1.3)

    def path(sel):
        out = []
        for e in ERAS:
            es = [px[c["paper_id"]][0] for c in cards if c["era"] == e and sel(c) and px[c["paper_id"]][0] is not None]
            if len(es) < 4:
                continue
            n = len(es)
            out.append((e, n, to_xy(sum(E == 3 for E in es) / n, sum(E <= 1 for E in es) / n,
                                    sum(E == 2 for E in es) / n)))
        return out
    labels = []
    for f in S.FIELDS:
        p = path(lambda c: f in c["fields"])
        if len(p) < 2:
            continue
        xy = np.array([q for _, _, q in p])
        ax.plot(xy[:, 0], xy[:, 1], color=V.TXT, lw=0.55, alpha=0.55, zorder=3, solid_capstyle="round")
        for k, (e, n, q) in enumerate(p):
            t = ERAS.index(e) / 4
            ax.scatter([q[0]], [q[1]], s=((0.6 + 1.6 * math.sqrt(n / 300)) * S.PT) ** 2,
                       c=S.mix(GOLD, V.DIM, t), edgecolors=V.BG, linewidths=0.3, zorder=4)
        labels.append([xy[-1, 0] + 1.6, xy[-1, 1] - 0.4, S.FSHORT[f], xy[-1]])
    # simple vertical repel so end labels do not overlap; a leader joins a moved label to its point
    labels.sort(key=lambda t: t[1])
    for i in range(1, len(labels)):
        for j in range(i):
            if abs(labels[i][0] - labels[j][0]) < 11 and labels[i][1] - labels[j][1] < 2.6:
                labels[i][1] = labels[j][1] + 2.6
    for x, y, t, anc in labels:
        if abs(y - anc[1]) > 1.0:
            ax.plot([anc[0], x - 0.3], [anc[1], y], color=V.DIM, lw=0.3, zorder=5)
        ax.text(x, y, t, fontsize=4.8, color=V.TXT, va="center", zorder=5, alpha=0.9)
    p = path(lambda c: True)
    xy = np.array([q for _, _, q in p])
    for k in range(len(xy) - 1):
        ax.add_patch(FancyArrowPatch(xy[k], xy[k + 1], arrowstyle="-|>,head_length=2.2,head_width=1.2",
                                     color=GOLD, lw=1.6, zorder=6, shrinkA=1.5, shrinkB=1.5))
    for e, n, q in p:
        ax.text(q[0] - 2.2, q[1] + 1.6, e, fontsize=5.4, color=GOLD, ha="right", fontweight="bold", zorder=7)
    V.title(ax, "Two instruments, and a third  ·  §1", "The drift away from closed evidence")
    dot = lambda t: (lambda a, x, y: a.scatter([x], [y], s=(1.6 * S.PT) ** 2, c=S.mix(GOLD, V.DIM, t), lw=0))
    arr = lambda a, x, y: a.add_patch(FancyArrowPatch((x - 1.8, y), (x + 1.8, y), arrowstyle="-|>,head_length=1.6,head_width=0.9",
                                                      color=GOLD, lw=1.2))
    V.legend(ax, mech=False, tiers=False, extra=("Point  ·  a field's evidence mix in one era (area ∝ papers)", [
        (dot(0), "2004–19"), (dot(0.5), "2024"), (dot(1), "2026"), (arr, "whole corpus, era to era")]))
    V.footer(ax, "662 core papers · cells with n < 4 omitted · snapshot 1 Nov 2026")
    V.save(fig, "art_ternary")


if __name__ == "__main__":
    main()
