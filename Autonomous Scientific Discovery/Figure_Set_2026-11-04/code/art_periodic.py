"""Periodic table of the frontier (proposal §2(3)(ii): located blanks).
Columns = fields, rows = problem openness O1 (bottom) to O6 (top). A tile is filled when at least one
paper in that cell has strong verification (V3-V4); its tone gives the era of the first such paper.
A tile attempted without any strongly verified paper is a Mendeleev-style gap ('?'). Number = papers in the cell."""
import collections as C
from matplotlib.patches import FancyBboxPatch
import style as S, proxies as X, cover as V

ERAS = ["2004–2019", "2020–2023", "2024", "2025", "2026"]
SYM = {"01": "Fo", "02": "Ph", "03": "Ch", "04": "Ma", "05": "Ea", "06": "Li", "07": "Me", "08": "Ag",
       "09": "En", "10": "Ae", "11": "So"}
RAMP = (["#5a3b0c", "#865f22", "#a98547", "#c4ab78", "#ddd0b4"] if V.LIGHT
        else ["#ffe3a3", "#e0b866", "#b08f4f", "#7a6640", "#4f4636"])          # earliest = strongest


def main():
    cards = S.papercards(); px = {k: (min(v, 3), o) for k, (o, v, L) in X.load_ov().items()}   # (strength tier, openness O1-O6)
    pts = [(f, c, *px[c["paper_id"]]) for c in cards for f in c["fields"] if None not in px[c["paper_id"]]]
    fig, ax = V.canvas()
    tw, th, g = 14.4, 16.0, 1.1
    x0 = 24.0
    y0 = 44.0
    for i, f in enumerate(S.FIELDS):
        x = x0 + i * (tw + g)
        ax.text(x + tw / 2, y0 - 3.5, S.FSHORT[f], fontsize=5.6, color=V.TXT, ha="center", va="top", rotation=0)
        for L in range(1, 7):
            y = y0 + (L - 1) * (th + g)
            cell = [(c, E) for g_, c, E, LL in pts if g_ == f and LL == L]
            e3 = [c for c, E in cell if E == 3]
            if not cell:
                ax.add_patch(FancyBboxPatch((x, y), tw, th, boxstyle="round,pad=0,rounding_size=1.2",
                                            fc="none", ec=V.FAINT, lw=0.4))
                continue
            if e3:
                first = min(ERAS.index(c["era"]) for c in e3)
                fc, tc, ec = RAMP[first], (V.BG if first <= 2 else V.TXT), "none"
            else:
                fc, tc, ec = "none", V.TXT, V.TXT
            ax.add_patch(FancyBboxPatch((x, y), tw, th, boxstyle="round,pad=0,rounding_size=1.2", fc=fc, ec=ec,
                                        lw=0.7))
            ax.text(x + 1.4, y + th - 1.6, str(len(cell)), fontsize=5.2, color=tc, va="top", fontweight="bold")
            ax.text(x + tw - 1.3, y + th - 1.6, f"O{L}", fontsize=4.6, color=tc, va="top", ha="right")
            ax.text(x + tw / 2, y + th / 2 + 0.8, SYM[f] if e3 else "?", fontsize=15 if e3 else 17, color=tc,
                    ha="center", va="center", fontweight="bold")
            sub = ERAS[min(ERAS.index(c["era"]) for c in e3)] if e3 else "gap"
            ax.text(x + tw / 2, y + 3.6, sub, fontsize=4.3, color=tc, ha="center", va="center")
            ax.text(x + tw / 2, y + 1.5, f"{len(e3)} closed" if e3 else "0 closed", fontsize=3.9, color=tc,
                    ha="center", va="center", alpha=0.85)
    for L in range(1, 7):
        y = y0 + (L - 1) * (th + g) + th / 2
        ax.text(x0 - 2.5, y + 1.5, f"O{L}", fontsize=7, color=V.TXT, ha="right", va="center", fontweight="bold")
        ax.text(x0 - 2.5, y - 2.0, ["rule world", "benchmark", "new instance", "physical test", "open maths", "open science"][L - 1], fontsize=4.6,
                color=V.DIM, ha="right", va="center")
    V.title(ax, "Located blanks  ·  §2(3)(ii)", "A periodic table of the frontier")
    sw = lambda k: (lambda a, x, y: a.add_patch(FancyBboxPatch((x - 1.2, y - 1.6), 2.4, 3.2,
                                                               boxstyle="round,pad=0,rounding_size=0.4",
                                                               fc=RAMP[k], ec="none")))
    gap = lambda a, x, y: a.add_patch(FancyBboxPatch((x - 1.2, y - 1.6), 2.4, 3.2,
                                                     boxstyle="round,pad=0,rounding_size=0.4", fc="none",
                                                     ec=V.TXT, lw=0.6))
    V.legend(ax, mech=False, tiers=False, extra=("Tile  ·  era of the first strongly verified (V3–V4) paper in the cell",
             [(sw(0), "2004–19"), (sw(1), "2020–23"), (sw(2), "2024"), (sw(3), "2025"), (sw(4), "2026"),
              (gap, "? attempted, never closed")]))
    V.footer(ax, "number = papers in cell · 935 paper–field points · snapshot 1 Nov 2026")
    V.save(fig, "art_periodic")


if __name__ == "__main__":
    main()
