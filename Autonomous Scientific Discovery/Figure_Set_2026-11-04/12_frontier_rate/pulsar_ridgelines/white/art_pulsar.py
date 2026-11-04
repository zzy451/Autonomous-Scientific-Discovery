"""Pulsar ridgelines (proposal §2(3)(iii): a rate that can be computed). After Harold Craft's PSR B1919+21
plot. One ridge per field: papers per year (Gaussian-smoothed, common scale). Gold ticks mark the year the
field's frontier stepped up, i.e. the first strongly verified (V3-V4) paper at a new highest openness."""
import math, collections as C
import numpy as np
import style as S, proxies as X, cover as V

GOLD = "#a87a1e" if V.LIGHT else "#ffd27a"


def main():
    cards = S.papercards(); px = {k: (min(v, 3), o) for k, (o, v, L) in X.load_ov().items()}   # (strength tier, openness O1-O6)
    yrs = np.linspace(2003.5, 2026.9, 700)
    fig, ax = V.canvas()
    X0, X1, Ytop, dy, amp = 44.0, 186.0, 150.0, 9.2, 21.0
    xmap = lambda y: X0 + (y - 2003.5) / (2026.9 - 2003.5) * (X1 - X0)
    dens = {}
    for f in S.FIELDS:
        ys = np.array([c["year"] + 0.5 for c in cards if f in c["fields"]], float)
        d = np.exp(-0.5 * ((yrs[:, None] - ys[None, :]) / 0.55) ** 2).sum(1) / (0.55 * math.sqrt(2 * math.pi))
        dens[f] = d
    top = max(d.max() for d in dens.values())
    for i, f in enumerate(S.FIELDS):                   # back (top row) to front, each ridge occludes the next
        base = Ytop - i * dy
        h = amp * dens[f] / top
        xs = xmap(yrs)
        ax.fill_between(xs, base, base + h, color=V.BG, lw=0, zorder=2 + i * 0.1)
        ax.plot(xs, base + h, color=V.TXT, lw=0.75, zorder=2.05 + i * 0.1, solid_capstyle="round")
        ax.text(X0 - 2.5, base + 1.2, S.FNAME[f], fontsize=5.4, color=V.TXT, ha="right", va="center", zorder=9)
        # frontier steps
        best = 0
        for y in range(2004, 2027):
            ls = [px[c["paper_id"]][1] for c in cards if f in c["fields"] and c["year"] <= y
                  and px[c["paper_id"]][0] == 3 and px[c["paper_id"]][1]]
            m = max(ls) if ls else 0
            if m > best:
                best = m
                xx = xmap(y + 0.5); hh = amp * np.interp(y + 0.5, yrs, dens[f]) / top
                ax.plot([xx, xx], [base, base + hh + 1.6], color=GOLD, lw=0.8, zorder=3 + i * 0.1)
                ax.text(xx, base + hh + 2.0, f"O{m}", fontsize=4.8, color=GOLD, ha="center", va="bottom",
                        fontweight="bold", zorder=3.05 + i * 0.1)
    for y in (2004, 2010, 2015, 2020, 2024, 2026):
        ax.text(xmap(y + 0.5), Ytop - 10 * dy - 6, str(y), fontsize=5.6, color=V.DIM, ha="center")
    V.title(ax, "A rate that can be computed  ·  §2(3)(iii)", "Pulsars of the frontier")
    tick = lambda a, x, y: (a.plot([x, x], [y - 1.6, y + 1.6], color=GOLD, lw=0.9),
                            a.text(x + 0.6, y + 1.2, "O4", fontsize=4.4, color=GOLD, fontweight="bold"))
    ridge = lambda a, x, y: a.plot(np.linspace(x - 1.5, x + 1.5, 20),
                                   y - 1 + 2.2 * np.exp(-((np.linspace(-1.5, 1.5, 20)) ** 2) * 2), color=V.TXT, lw=0.7)
    V.legend(ax, mech=False, tiers=False, extra=("Ridge  ·  papers per year in the field, common scale", [
        (ridge, "smoothed count"), (tick, "frontier steps up: first strongly verified (V3–V4) paper at a new highest openness")]))
    V.footer(ax, "935 paper–field assignments · snapshot 1 Nov 2026")
    V.save(fig, "art_pulsar")


if __name__ == "__main__":
    main()
