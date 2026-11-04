"""Fig. F - Evidence thins as volume rises (proposal §2 finding 2).

a, River of papers per era, stratified by evidence endpoint (E3 core, outer = weaker).
b, Share of papers with an E3 endpoint per era (Wilson 95% CI), for all papers and within
   LLM-driven (D5) and optimisation (D3) papers - separates composition from within-mechanism change.
"""
import collections as C
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.interpolate import PchipInterpolator
import style as S, proxies as X

W, H = 183.0, 92.0
ERAS = ["2004–2019", "2020–2023", "2024", "2025", "2026"]


def main():
    cards = S.papercards()
    px = X.load()
    rows = [(c["era"], px[c["paper_id"]][0], c["mechanism"]) for c in cards if px[c["paper_id"]][0] is not None]
    cnt = C.Counter((e, E) for e, E, _ in rows)
    n_era = C.Counter(e for e, _, _ in rows)

    fig = plt.figure(figsize=(W / 25.4, H / 25.4), facecolor=S.SURF)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    ax.text(2, H - 4, "Evidence thins as the record grows", fontsize=9, fontweight="bold", color=S.INK, va="top")
    ax.text(2, H - 9, f"{len(rows)} core papers with a coded validation endpoint; eras are ordinal (unequal length)",
            fontsize=5.3, color=S.INK2, va="top")

    # ---- a: river --------------------------------------------------------------
    ax.text(2, H - 15, "a", fontsize=8, fontweight="bold", color=S.INK, va="top")
    X0, X1, YC, K = 12.0, 104.0, 44.0, 0.095          # K mm per paper
    xe = np.linspace(X0 + 6, X1 - 6, len(ERAS))
    xs = np.linspace(xe[0] - 6, xe[-1] + 6, 600)
    order = [3, 2, 1, 0]                               # centre outwards
    # half-width per tier boundary, centred on YC: E3 straddles the axis, weaker tiers on alternating sides
    cum = {}
    for e in ERAS:
        lo = hi = 0.0
        h3 = cnt[(e, 3)] * K
        lo, hi = -h3 / 2, h3 / 2
        cum[(e, 3)] = (lo, hi)
        for E in (2, 1, 0):
            h = cnt[(e, E)] * K
            cum[(e, E)] = (lo - h / 2, hi + h / 2)          # each weaker tier wraps both sides equally
            lo, hi = lo - h / 2, hi + h / 2
    for E in reversed(order):                          # paint outer tiers first
        lo = PchipInterpolator(xe, [cum[(e, E)][0] for e in ERAS])(np.clip(xs, xe[0], xe[-1]))
        hi = PchipInterpolator(xe, [cum[(e, E)][1] for e in ERAS])(np.clip(xs, xe[0], xe[-1]))
        taper = np.clip(1 - np.maximum(xe[0] - xs, xs - xe[-1]) / 6, 0, 1) ** 0.6
        ax.fill_between(xs, YC + lo * taper, YC + hi * taper, color=S.TIER_FILL[E], lw=0, zorder=2)
        ax.plot(xs, YC + hi * taper, color=S.SURF, lw=0.4, zorder=2.1)
        ax.plot(xs, YC + lo * taper, color=S.SURF, lw=0.4, zorder=2.1)
    for x, e in zip(xe, ERAS):
        n = n_era[e]
        top = YC + cum[(e, 0)][1]
        ax.plot([x, x], [YC + cum[(e, 0)][0] - 1, top + 1], color=S.INK3, lw=0.25, zorder=1)
        ax.text(x, 13.0, e, fontsize=5.6, fontweight="bold", color=S.INK, ha="center")
        ax.text(x, 9.6, f"n = {n}", fontsize=4.9, color=S.INK2, ha="center")
        ax.text(x, max(top + 1.6, YC + 3.2), f"{100 * cnt[(e, 3)] / n:.0f}% strong",
                fontsize=5.0, color=S.INK, ha="center", va="bottom", fontweight="bold")
        weak = cnt[(e, 0)] + cnt[(e, 1)]
        ax.text(x, YC + cum[(e, 0)][0] - 1.8, f"{weak} weak", fontsize=4.5, color=S.INK2, ha="center", va="top")
    # legend for tiers
    ly = 72.0
    for E in order:
        ax.add_patch(Rectangle((12, ly - 1), 2.4, 2.2, fc=S.TIER_FILL[E], ec=S.INK3 if E == 0 else "none", lw=0.3))
        ax.text(15.6, ly + 0.1, S.TIER_NAME[E], fontsize=4.8, color=S.INK, va="center")
        ly -= 3.2
    ax.text(60, 72.0, "River width ∝ papers in era.\n“weak” = E0 + E1 (benchmark,\nexpert or case only).",
            fontsize=4.7, color=S.INK2, va="top", linespacing=1.25)

    # ---- b: E3 share with CI, stratified -----------------------------------------
    ax.text(110, H - 15, "b", fontsize=8, fontweight="bold", color=S.INK, va="top")
    axb = fig.add_axes([122 / W, 16 / H, 56 / W, 52 / H])
    groups = [("All papers", None, S.INK), ("LLM-driven (D5)", "llm", S.MECH["llm"]),
              ("Optimization (D3)", "optimization", S.MECH["optimization"])]
    xi = np.arange(len(ERAS))
    for gi, (lab, mech, col) in enumerate(groups):
        ps, los, his, ns = [], [], [], []
        for e in ERAS:
            sub = [E for ee, E, m in rows if ee == e and (mech is None or m == mech)]
            p, lo, hi = S.wilson(sum(E == 3 for E in sub), len(sub))
            ps.append(p); los.append(lo); his.append(hi); ns.append(len(sub))
        off = (gi - 1) * 0.12
        ok = [i for i, n in enumerate(ns) if n >= 3]
        axb.vlines(xi[ok] + off, np.array(los)[ok] * 100, np.array(his)[ok] * 100, color=col, lw=0.7, alpha=0.55)
        axb.plot(xi[ok] + off, np.array(ps)[ok] * 100, color=col, lw=1.0 if mech else 1.4, marker="o",
                 ms=2.6, mec=S.SURF, mew=0.4)
        last = ok[-1]
        dy = {None: 4.5, "llm": -4.0, "optimization": 0.0}[mech]
        axb.text(xi[last] + 0.25, ps[last] * 100 + dy, lab, fontsize=4.8, color=col, va="center")
    axb.set_xticks(xi, ["2004–\n2019", "2020–\n2023", "2024", "2025", "2026"])
    axb.set_ylim(0, 104); axb.set_xlim(-0.4, len(ERAS) + 0.9)
    axb.set_ylabel("Strongly verified, V3–V4 (%)", fontsize=5.3)
    for s in ("top", "right"):
        axb.spines[s].set_visible(False)
    axb.tick_params(labelsize=4.9, colors=S.INK2)
    axb.set_title("V3–V4 share, Wilson 95% CI; strata with n < 3 omitted", fontsize=5.0, color=S.INK2, loc="left")
    S.save(fig, "fig_thinning")


if __name__ == "__main__":
    main()
