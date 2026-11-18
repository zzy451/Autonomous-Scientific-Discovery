"""Nightingale rose of the review queue (proposal §3: where domain scientists are needed).
Per field, four stacked queues (area proportional to papers): E3 endpoints whose V3/V2 status needs an
expert; L3-L4 papers whose actual AI contribution needs checking; papers at an unclosed summit (is the
blank real?); mechanism labels that are provisional or low confidence. Rings mark the proposal's
15-20 cases per field."""
import math, collections as C
import numpy as np
from matplotlib.patches import Wedge, Circle
import style as S, proxies as X, cover as V

GOLD = "#a87a1e" if V.LIGHT else "#ffd27a"
Q = [("V3 / V2 boundary", "strong (V3–V4) claim to confirm", GOLD),
     ("Actual AI contribution", "L3 autonomous-researcher systems", S.mix(GOLD, V.BG, 0.45)),
     ("Is the blank real?", "papers at the highest openness without strong verification", V.TXT),
     ("Contested label", "provisional or low-confidence mechanism", V.DIM)]


def main():
    cards = S.papercards()
    ov = X.load_ov()
    px = {k: (min(v, 3), o) for k, (o, v, L) in ov.items()}          # (strength tier, openness) for the frontier
    top_closed = {}
    for f in S.FIELDS:
        cl = [px[c["paper_id"]][1] for c in cards if f in c["fields"] and px[c["paper_id"]][0] == 3 and px[c["paper_id"]][1]]
        att = [px[c["paper_id"]][1] for c in cards if f in c["fields"] and px[c["paper_id"]][1]]
        top_closed[f] = (max(cl) if cl else 0, max(att) if att else 0)
    counts = {}
    for f in S.FIELDS:
        ps = [c for c in cards if f in c["fields"]]
        cl, at = top_closed[f]
        counts[f] = [sum(px[c["paper_id"]][0] == 3 for c in ps),
                     sum(ov[c["paper_id"]][2] >= 3 for c in ps),                 # L3 autonomous researchers
                     sum((px[c["paper_id"]][1] or 0) == at for c in ps) if at > cl else 0,
                     sum(c["provisional"] or c["confidence"] == "low" for c in ps)]
    fig, ax = V.canvas()
    cx, cy, R = V.CX, V.CY, V.RMAX
    k = R / math.sqrt(max(sum(v) for v in counts.values()))       # area-true: r = k * sqrt(cumulative)
    span = V.sectors({f: 1 for f in S.FIELDS}, gap=1.8)
    for n_ in (15, 20):
        ax.add_patch(Circle((cx, cy), k * math.sqrt(n_), fc="none", ec=V.TXT, lw=0.5, alpha=0.6, zorder=6))
    xr, yr = V.polar(cx, cy, 198, k * math.sqrt(20))
    ax.plot([xr, cx - R - 6], [yr, yr - 8], color=V.TXT, lw=0.35, alpha=0.7, zorder=7)
    ax.text(cx - R - 6.5, yr - 8, "rings: 15 and 20 cases\n= half a day per field", fontsize=5.0, color=V.TXT,
            ha="right", va="center", zorder=7, linespacing=1.25)
    for f, (a0, a1) in span.items():
        cum = 0
        for qi, (_, _, col) in enumerate(Q):
            r0 = k * math.sqrt(cum); cum += counts[f][qi]; r1 = k * math.sqrt(cum)
            if r1 > r0:
                ax.add_patch(Wedge((cx, cy), r1, a1, a0, width=r1 - r0, fc=col, ec=V.BG, lw=0.5,
                                   alpha=0.95 if qi < 2 else 0.8, zorder=3))
        V.curved(ax, S.FSHORT[f], cx, cy, (a0 + a1) / 2, max(k * math.sqrt(cum), 24) + 4.2, 6.0, V.TXT)
        V.curved(ax, str(sum(counts[f])), cx, cy, (a0 + a1) / 2, max(k * math.sqrt(cum), 24) + 1.4, 4.6, V.DIM,
                 weight="normal", track=0.05)
    V.title(ax, "Where domain scientists are needed  ·  §3", "The review rose")
    sw = lambda col: (lambda a, x, y: a.add_patch(Wedge((x, y - 1.5), 3.0, 60, 120, fc=col, ec="none")))
    V.legend(ax, mech=False, tiers=False, extra=("Petal layers  ·  papers needing each judgement (area ∝ papers)",
             [(sw(c), n) for n, _, c in Q]))
    V.footer(ax, "a paper can sit in several queues · snapshot 1 Nov 2026")
    V.save(fig, "art_rose")
    for f in S.FIELDS:
        print(f, counts[f])


if __name__ == "__main__":
    main()
