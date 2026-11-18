"""Cover · The sunflower of the record (claim: evidence thins over time).
642 papers in golden-angle phyllotaxis, oldest at the centre; colour = mechanism, brightness = evidence."""
import math, collections as C
from matplotlib.patches import Circle
import style as S, proxies as X, cover as V

ERAS = ["2004–2019", "2020–2023", "2024", "2025", "2026"]
GA = 137.50776


def main():
    cards = S.papercards(); px = X.load()
    ps = sorted([c for c in cards if px[c["paper_id"]][0] is not None],
                key=lambda c: (ERAS.index(c["era"]), c["year"], c["paper_id"]))
    fig, ax = V.canvas()
    cx, cy, R = V.CX + 8, V.CY, V.RMAX
    k = R / math.sqrt(len(ps))
    xs, ys, cols, tiers = [], [], [], []
    for i, c in enumerate(ps):
        r = k * math.sqrt(i + 0.6)
        x, y = V.polar(cx, cy, 90 - i * GA, r)
        xs.append(x); ys.append(y); cols.append(V.MECH[c["mechanism"]]); tiers.append(px[c["paper_id"]][0])
    V.marks(ax, xs, ys, cols, tiers, scale=1.05)
    cum = 0
    for j, e in enumerate(ERAS):
        sub = [c for c in ps if c["era"] == e]
        cum += len(sub)
        r = k * math.sqrt(cum)
        ax.add_patch(Circle((cx, cy), r + k * 0.35, fc="none", ec=V.DIM, lw=0.35, alpha=0.55, zorder=2))
        share = 100 * sum(px[c["paper_id"]][0] == 3 for c in sub) / len(sub)
        # every era labelled the same way: leader from its ring to a column at left
        x0, y0 = V.polar(cx, cy, 196 - j * 3.2, r + k * 0.35)
        x1, y1 = cx - R - 10, cy + 22 - j * 9
        ax.plot([x0, x1 + 1.2], [y0, y1], color=V.DIM, lw=0.35, zorder=30)
        ax.scatter([x0], [y0], s=(0.8 * S.PT) ** 2, c=V.TXT, lw=0, zorder=31)
        ax.text(x1, y1 + 1.6, e, fontsize=6.0, color=V.TXT, ha="right", va="center", fontweight="bold", zorder=31)
        ax.text(x1, y1 - 1.6, f"{share:.0f}% strong (V3–V4)", fontsize=5.2, color=V.DIM, ha="right", va="center",
                zorder=31)
    V.title(ax, "Evidence thins over time", "The sunflower of the record")
    ring = lambda a, x, y: a.add_patch(Circle((x, y), 1.4, fc="none", ec=V.DIM, lw=0.6))
    V.legend(ax, extra=("Spiral  ·  one seed per paper, oldest at the centre",
                        [(ring, "rings close each era; % = share strongly verified (V3–V4)")]))
    V.footer(ax, "662 core papers · strong = V3–V4 · snapshot 1 Nov 2026")
    V.save(fig, "cover_sunflower")


if __name__ == "__main__":
    main()
