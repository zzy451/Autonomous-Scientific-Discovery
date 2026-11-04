"""Cover · Frontier bloom (proposal Fig. 1 claim: a checkable frontier, era by era).
Petals = per field, the highest problem openness reached by >= 1 strongly verified (V3-V4) paper; one translucent gold layer
per era (cumulative, so earlier ground glows brighter). Thin outline = highest openness attempted."""
import math, collections as C
import numpy as np
from matplotlib.patches import Circle, Polygon
import style as S, proxies as X, cover as V

ERAS = ["2004–2019", "2020–2023", "2024", "2025", "2026"]
GOLD = "#e9b860"


def main():
    cards = S.papercards(); px = {k: (min(v, 3), o) for k, (o, v, L) in X.load_ov().items()}   # (strength tier, openness O1-O6)
    pts = [(f, c, *px[c["paper_id"]]) for c in cards for f in c["fields"] if None not in px[c["paper_id"]]]
    fig, ax = V.canvas()
    cx, cy, R, R0 = V.CX, V.CY, V.RMAX, 9.0
    B = (R - R0) / 6
    span = V.sectors({f: 1 for f in S.FIELDS}, gap=2.0)
    mid = {f: (a0 + a1) / 2 for f, (a0, a1) in span.items()}
    half = (span["01"][0] - span["01"][1]) / 2 + 1.0

    def petal_curve(h):          # h: {field: level 0-4}
        th = np.linspace(90, -270, 1440)
        r = np.full_like(th, R0 * 0.75)
        for f in S.FIELDS:
            d = (th - mid[f] + 180) % 360 - 180
            w = np.clip(1 - np.abs(d) / (half * 0.92), 0, 1) ** 0.6
            r = np.maximum(r, R0 * 0.75 + (R0 * 0.25 + h[f] * B) * w)
        return [V.polar(cx, cy, t, rr) for t, rr in zip(th, r)]

    # reach bands + labels
    for L in range(1, 7):
        ax.add_patch(Circle((cx, cy), R0 + L * B, fc="none", ec=V.DIM, lw=0.3, alpha=0.45, zorder=2))
        x, y = V.polar(cx, cy, 90, R0 + (L - 0.5) * B)
        ax.text(x, y, f"O{L}", fontsize=6.2, color=V.TXT, ha="center", va="center", fontweight="bold", zorder=31)
    for k, e in enumerate(ERAS):
        upto = set(ERAS[:k + 1])
        h = {f: max([L for g, c, E, L in pts if g == f and c["era"] in upto and E == 3] or [0]) for f in S.FIELDS}
        poly = petal_curve(h)
        ax.add_patch(Polygon(poly, closed=True, fc=GOLD, ec="none", alpha=0.17 if not V.LIGHT else 0.22, zorder=1))
        ax.add_patch(Polygon(poly, closed=True, fc="none", ec=GOLD, lw=0.45, alpha=0.55, zorder=1.5))
    att = {f: max([L for g, c, E, L in pts if g == f] or [0]) for f in S.FIELDS}
    ax.add_patch(Polygon(petal_curve(att), closed=True, fc="none", ec=V.TXT, lw=0.5, alpha=0.5, zorder=1.6))
    # dots
    cell = C.defaultdict(list)
    for f, c, E, L in pts:
        cell[(f, L)].append((c, E))
    xs, ys, cols, tiers = [], [], [], []
    for (f, L), lst in cell.items():
        a0, a1 = span[f]
        for i, (c, E) in enumerate(sorted(lst, key=lambda t: t[0]["paper_id"])):
            u, v = V.halton(i + 1, 2), V.halton(i + 1, 3)
            r0, r1 = R0 + (L - 1) * B, R0 + L * B
            rr = math.sqrt(r0 ** 2 + (0.1 + 0.8 * v) * (r1 ** 2 - r0 ** 2))
            x, y = V.polar(cx, cy, a0 + (0.08 + 0.84 * u) * (a1 - a0), rr)
            xs.append(x); ys.append(y); cols.append(V.MECH[c["mechanism"]]); tiers.append(E)
    V.marks(ax, xs, ys, cols, tiers, scale=0.85)
    for f in S.FIELDS:
        V.curved(ax, S.FSHORT[f], cx, cy, mid[f], R + 6.5, 6.4, V.TXT)
        if att[f] > max([L for g, c, E, L in pts if g == f and E == 3] or [0]):
            V.curved(ax, "unclosed summit", cx, cy, mid[f], R + 2.6, 4.6, V.DIM, weight="normal", track=0.1)
    V.title(ax, "A checkable frontier", "The frontier bloom")
    pet = lambda a, x, y: a.add_patch(Polygon([(x - 1.4, y - 1.1), (x, y + 1.4), (x + 1.4, y - 1.1)], fc=GOLD,
                                               alpha=0.55, ec="none"))
    out = lambda a, x, y: a.add_patch(Polygon([(x - 1.4, y - 1.1), (x, y + 1.4), (x + 1.4, y - 1.1)], fc="none",
                                               ec=V.TXT, lw=0.6, alpha=0.7))
    V.legend(ax, extra=("Petals  ·  openness O1–O6 reached with strong verification (V3–V4)", [
        (pet, "one layer per era, " + ("deeper" if V.LIGHT else "brighter") + " = closed earlier"), (out, "highest openness attempted")]))
    V.footer(ax, "935 paper–field points · strong = V3–V4 · snapshot 1 Nov 2026")
    V.save(fig, "cover_bloom")


if __name__ == "__main__":
    main()
