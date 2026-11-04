"""Fig. E - The expanding frontier (corpus proxy of the proposal's Fig. 1).

Altitude = research-loop reach L1-L4. Land = the highest reach in a field closed by at least
one paper with a physical, clinical, deployed or formal endpoint (E3), cumulative to the end
of each era (one shade per era). Water = reach attempted but not yet closed. Each point is one
paper-field assignment: filled ink = E3, grey = E2, open = E0-E1."""
import math, collections as C
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.ndimage import gaussian_filter1d
import style as S, proxies as X

W, H = 183.0, 118.0
X0, X1, Y0, LH = 30.0, 176.0, 22.0, 11.4          # plot box (mm); LH = height per openness level
ERAS = ["2004–2019", "2020–2023", "2024", "2025", "2026"]
LAND = ["#86705a", "#a08769", "#bba483", "#d6c4a4", "#ede3cf"]    # earliest (dark) -> latest (light)
WATER, WAVE = "#e4edf2", "#c9d9e3"


def halton(i, b):
    f, r = 1.0, 0.0
    while i > 0:
        f /= b; r += f * (i % b); i //= b
    return r


def main():
    cards = S.papercards()
    ov = X.load_ov()
    px = {pid: (min(v, 3), o) for pid, (o, v, L) in ov.items()}          # (strength tier, openness O1-O6)
    fw = (X1 - X0) / len(S.FIELDS)
    xc = {f: X0 + fw * (i + 0.5) for i, f in enumerate(S.FIELDS)}
    yL = lambda L: Y0 + (L - 0.5) * LH

    pts = [(f, c, *px[c["paper_id"]]) for c in cards for f in c["fields"]
           if px[c["paper_id"]][0] is not None and px[c["paper_id"]][1] is not None]
    # frontier height per field, cumulative by era
    front = {}
    for k, e in enumerate(ERAS):
        upto = set(ERAS[:k + 1])
        for f in S.FIELDS:
            ls = [L for g, c, E, L in pts if g == f and c["era"] in upto and E == 3]
            front[(f, e)] = max(ls) if ls else 0
    attempted = {f: max([L for g, c, E, L in pts if g == f] or [0]) for f in S.FIELDS}

    fig = plt.figure(figsize=(W / 25.4, H / 25.4), facecolor=S.SURF)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    top = Y0 + 6 * LH
    # water with wave lines
    ax.add_patch(Rectangle((X0, Y0), X1 - X0, 6 * LH + 3, fc=WATER, ec="none", zorder=0))
    xs = np.linspace(X0, X1, 900)
    for yy in np.arange(Y0 + 2, top + 2.5, 2.2):
        ax.plot(xs, yy + 0.22 * np.sin((xs - X0) * 1.9 + yy), color=WAVE, lw=0.3, zorder=0.5)
    # land, latest era first (widest), earliest on top
    for k in range(len(ERAS) - 1, -1, -1):
        e = ERAS[k]
        step = np.zeros_like(xs)
        for f in S.FIELDS:
            h = front[(f, e)]
            m = np.abs(xs - xc[f]) <= fw * 0.44
            step[m] = (h * LH) if h else 1.2
        prof = gaussian_filter1d(step, 6)
        prof = np.maximum(prof, 0.8)
        ax.fill_between(xs, Y0, Y0 + prof, color=LAND[k], lw=0, zorder=1 + (len(ERAS) - k) * 0.01)
        ax.plot(xs, Y0 + prof, color=S.mix(LAND[k], "#000000", 0.25), lw=0.35, zorder=1.05 + (len(ERAS) - k) * 0.01)
    # reach-level guides
    for L in range(1, 7):
        yb = Y0 + L * LH
        ax.plot([X0, X1], [yb, yb], color="#ffffff", lw=0.5, alpha=0.8, zorder=1.6)
        ax.text(X0 - 2, yL(L) + 2.2, f"O{L}", fontsize=6.5, fontweight="bold", color=S.INK, ha="right", va="center")
        ax.text(X0 - 2, yL(L) - 1.0, X.O_NAME[L].split(" (")[0], fontsize=4.6, color=S.INK2, ha="right",
                va="center", linespacing=1.1)
    ax.text(4, Y0 + 3 * LH, "Problem openness  →  from rule worlds to open science", fontsize=5.3,
            color=S.INK2, rotation=90, ha="center", va="center")
    # points
    cell = C.defaultdict(list)
    for f, c, E, L in pts:
        cell[(f, L)].append((E, c["paper_id"]))
    for (f, L), lst in cell.items():
        lst.sort(key=lambda t: (-t[0], t[1]))
        for i, (E, pid) in enumerate(lst):
            u, v = halton(i + 1, 2), halton(i + 1, 3)
            x = xc[f] + (u - 0.5) * fw * 0.80
            y = yL(L) + (v - 0.5) * LH * 0.78
            if E == 3:
                kw = dict(c=S.INK, edgecolors=S.SURF, linewidths=0.2)
            elif E == 2:
                kw = dict(c="#8f877a", edgecolors=S.SURF, linewidths=0.2)
            else:
                kw = dict(c=S.SURF, edgecolors="#6f685d", linewidths=0.35)
            ax.scatter([x], [y], s=(0.78 * S.PT) ** 2, zorder=4, **kw)
    # field labels + summit status (the "located blanks")
    for f in S.FIELDS:
        x = xc[f]
        ax.text(x, Y0 - 2.2, S.FNAME[f].replace(" & ", " &\n").replace(", ", ",\n"), fontsize=4.9, color=S.INK,
                ha="center", va="top", linespacing=1.1)
        ax.text(x, Y0 - 0.7, f, fontsize=4.4, color=S.INK3, ha="center", va="top", fontweight="bold")
        a, fr = attempted[f], front[(f, ERAS[-1])]
        if a > fr:
            n_top = sum(1 for g, c, E, L in pts if g == f and L == a)
            msg = f"O{a} attempted\n0 of {n_top} strong" if fr < a else ""
            ax.text(x, top + 4.4, msg, fontsize=4.5, color=S.INK, ha="center", va="bottom", fontstyle="italic",
                    linespacing=1.15)
        else:
            ax.text(x, top + 4.4, f"strong to O{fr}", fontsize=4.5, color=S.INK3, ha="center", va="bottom")
    ax.text(X0, top + 11.5, "UNCLOSED SUMMITS  ·  highest openness attempted in each field without strong verification (V3–V4)",
            fontsize=5, color=S.INK2, fontweight="bold")
    # header + legend
    ax.text(2, H - 4, "The expanding frontier of strongly verified AI-solved problems", fontsize=9,
            fontweight="bold", color=S.INK, va="top")
    ax.text(2, H - 9, "Land = openness reached by ≥1 paper with strong verification (V3–V4: experiment, proof or replication), "
            "one shade per era (cumulative). Water = attempted, not yet strongly verified.",
            fontsize=5.2, color=S.INK2, va="top")
    ly = 5.5
    ax.text(X0, ly + 3.4, "Land closed by end of", fontsize=4.8, color=S.INK2, va="center")
    lx = X0
    for k, e in enumerate(ERAS):
        ax.add_patch(Rectangle((lx, ly - 1), 4, 2.2, fc=LAND[k], ec="none"))
        ax.text(lx + 5, ly + 0.1, e, fontsize=4.8, color=S.INK, va="center")
        lx += 9 + len(e) * 0.95
    lx += 2
    for E, lab in [(3, "V3–V4 strong"), (2, "V2 computational"), (0, "V0–V1 claim / benchmark")]:
        kw = dict(c=S.INK, edgecolors=S.SURF) if E == 3 else dict(c="#8f877a", edgecolors=S.SURF) if E == 2 \
            else dict(c=S.SURF, edgecolors="#6f685d")
        ax.scatter([lx + 1], [ly + 0.1], s=(1.3 * S.PT) ** 2, linewidths=0.4, **kw)
        ax.text(lx + 2.6, ly + 0.1, lab, fontsize=4.8, color=S.INK, va="center")
        lx += 7 + len(lab) * 0.9
    S.save(fig, "fig_frontier")
    for f in S.FIELDS:
        print(f, [front[(f, e)] for e in ERAS], "attempted", attempted[f])


if __name__ == "__main__":
    main()
