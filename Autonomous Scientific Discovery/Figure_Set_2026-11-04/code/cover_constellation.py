"""Cover · Where verification lives (claim: autonomy and verification).
Sectors = decision mechanism (angle proportional to papers); rings = research-loop reach L1-L4;
star = one paper, brightness = evidence endpoint."""
import math, collections as C
from matplotlib.patches import Circle, Wedge
import style as S, proxies as X, cover as V


def main():
    cards = S.papercards(); px = X.load()
    ps = [(c, *px[c["paper_id"]]) for c in cards if None not in px[c["paper_id"]]]
    fig, ax = V.canvas()
    cx, cy, R, R0 = V.CX, V.CY, V.RMAX, 8.0
    order = ["llm", "optimization", "hybrid", "classical"]
    n = C.Counter(c["mechanism"] for c, _, _ in ps)
    # small sectors widened to a floor so their stars stay legible; true counts are printed
    wts = {m: max(n[m], 60) for m in order}
    span = V.sectors(wts, gap=3.0, start=90 + 0.5 * wts["llm"] * (360 - 12) / sum(wts.values()))
    B = (R - R0) / 3
    for L in range(1, 4):
        ax.add_patch(Circle((cx, cy), R0 + L * B, fc="none", ec=V.DIM, lw=0.3, alpha=0.4, zorder=2))
    xs, ys, cols, tiers = [], [], [], []
    for m in order:
        a0, a1 = span[m]
        ax.add_patch(Wedge((cx, cy), R + 4.6, a1, a0, width=1.6, fc=V.MECH[m], ec="none", zorder=3))
        sub = [(c, E, L) for c, E, L in ps if c["mechanism"] == m]
        e3 = 100 * sum(E == 3 for _, E, _ in sub) / len(sub)
        V.curved(ax, V.MECH_SHORT[m], cx, cy, (a0 + a1) / 2, R + 10.5, 7.0, V.TXT)
        V.curved(ax, f"{len(sub)} papers · {e3:.0f}% strong (V3–V4)", cx, cy, (a0 + a1) / 2, R + 7.4, 5.0,
                 V.DIM, weight="normal", track=0.08)
        for L in range(1, 4):
            cell = sorted([(c, E) for c, E, LL in sub if LL == L], key=lambda t: t[0]["paper_id"])
            for i, (c, E) in enumerate(cell):
                u, v = V.halton(i + 1, 2), V.halton(i + 1, 3)
                r0, r1 = R0 + (L - 1) * B, R0 + L * B
                rr = math.sqrt(r0 ** 2 + (0.08 + 0.84 * v) * (r1 ** 2 - r0 ** 2))
                x, y = V.polar(cx, cy, a0 + (0.04 + 0.92 * u) * (a1 - a0), rr)
                xs.append(x); ys.append(y); cols.append(V.MECH[m]); tiers.append(E)
    V.marks(ax, xs, ys, cols, tiers, scale=1.0)
    gapmid = span["classical"][1] - 1.5
    for L in range(1, 4):
        x, y = V.polar(cx, cy, gapmid, R0 + (L - 0.5) * B)
        ax.text(x, y, f"L{L}", fontsize=6.0, color=V.TXT, fontweight="bold", ha="center", va="center", zorder=31,
                bbox=dict(boxstyle="round,pad=0.15", fc=V.BG, ec="none", alpha=0.8))
    V.title(ax, "Autonomy and verification", "Where the strongest evidence lives")
    ring = lambda a, x, y: a.add_patch(Circle((x, y), 1.4, fc="none", ec=V.DIM, lw=0.6))
    V.legend(ax, extra=("Rings  ·  system autonomy", [(ring, "L1 task assistant (centre) → L3 autonomous researcher (rim)")]))
    V.footer(ax, "662 core papers · small sectors widened, counts printed · snapshot 1 Nov 2026")
    V.save(fig, "cover_constellation")


if __name__ == "__main__":
    main()
