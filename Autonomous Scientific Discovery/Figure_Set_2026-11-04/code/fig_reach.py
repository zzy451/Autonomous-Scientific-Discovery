"""Fig. G - Does delegating more of the research loop mean weaker evidence?
(proposal §2 finding 1, tested with corpus proxies).

a, Evidence-endpoint mix for each research-loop reach level L1-L4 (100% bars, n, E3 share).
b, E3 share by reach within 2024-2026 only, split into LLM-driven (D5) and all other
   mechanisms (Wilson 95% CI) - holds era fixed to separate reach from mechanism.
Spearman rho(L, E) with a 2,000-sample bootstrap CI is printed in the panel.
"""
import collections as C
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.stats import spearmanr
import style as S, proxies as X

W, H = 183.0, 86.0


def main():
    cards = S.papercards()
    px = X.load()
    rows = [(px[c["paper_id"]][1], px[c["paper_id"]][0], c["mechanism"], c["era"]) for c in cards
            if px[c["paper_id"]][0] is not None and px[c["paper_id"]][1] is not None]
    Ls = np.array([r[0] for r in rows]); Es = np.array([r[1] for r in rows])
    rho = spearmanr(Ls, Es).statistic
    rng = np.random.default_rng(7)
    boot = []
    for _ in range(2000):
        i = rng.integers(0, len(rows), len(rows))
        boot.append(spearmanr(Ls[i], Es[i]).statistic)
    lo, hi = np.percentile(boot, [2.5, 97.5])

    fig = plt.figure(figsize=(W / 25.4, H / 25.4), facecolor=S.SURF)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    ax.text(2, H - 4, "Strong verification peaks at L2 and falls at L3; task assistants (L1) are rarely verified",
            fontsize=9, fontweight="bold", color=S.INK, va="top")
    ax.text(2, H - 9, f"{len(rows)} papers coded on the proposal axes. Spearman ρ(autonomy, verification) = {rho:.2f} "
            f"(95% bootstrap CI {lo:.2f} to {hi:.2f}); the sharper contrast is between mechanisms.",
            fontsize=5.3, color=S.INK2, va="top")

    # ---- a: 100% bars ---------------------------------------------------------------
    ax.text(2, H - 15, "a", fontsize=8, fontweight="bold", color=S.INK, va="top")
    BX0, BW, BH = 40.0, 62.0, 6.2
    cnt = C.Counter((L, E) for L, E, _, _ in rows)
    for k, L in enumerate([3, 2, 1]):
        y = 62 - k * 11.0
        n = sum(cnt[(L, E)] for E in range(4))
        ax.text(BX0 - 2, y + BH / 2 + 1.3, f"L{L}", fontsize=6.5, fontweight="bold", color=S.INK, ha="right", va="center")
        ax.text(BX0 - 2, y + BH / 2 - 1.6, X.L_NAME[L], fontsize=4.6, color=S.INK2, ha="right", va="center")
        x = BX0
        for E in (3, 2, 1, 0):
            w = BW * cnt[(L, E)] / n
            ax.add_patch(Rectangle((x + 0.15, y), max(w - 0.3, 0.1), BH, fc=S.TIER_FILL[E],
                                   ec=S.INK3 if E == 0 else "none", lw=0.3))
            if w > 5.5:
                ax.text(x + w / 2, y + BH / 2, f"{100 * cnt[(L, E)] / n:.0f}", fontsize=4.8, ha="center",
                        va="center", color=S.SURF if E >= 2 else S.INK, fontweight="bold")
            x += w
        ax.text(BX0 + BW + 1.5, y + BH / 2, f"n = {n}", fontsize=4.8, color=S.INK2, va="center")
    ly = 14.5
    lx = BX0
    for E in (3, 2, 1, 0):
        ax.add_patch(Rectangle((lx, ly - 1), 2.2, 2.0, fc=S.TIER_FILL[E], ec=S.INK3 if E == 0 else "none", lw=0.3))
        ax.text(lx + 2.9, ly, ["V0", "V1", "V2", "V3–V4"][E], fontsize=4.8, color=S.INK, va="center")
        lx += 9
    ax.text(BX0, 9.5, "% of papers at each autonomy level; V3–V4 = experiment, proof or replication (strong)",
            fontsize=4.6, color=S.INK2)

    # ---- b: E3 share within 2024-2026 by mechanism ---------------------------------------
    ax.text(116, H - 15, "b", fontsize=8, fontweight="bold", color=S.INK, va="top")
    axb = fig.add_axes([128 / W, 17 / H, 50 / W, 50 / H])
    late = [r for r in rows if r[3] in ("2024", "2025", "2026")]
    for gi, (lab, pred, col) in enumerate([("LLM-driven (D5)", lambda m: m == "llm", S.MECH["llm"]),
                                           ("Other mechanisms", lambda m: m != "llm", S.INK)]):
        for L in (1, 2, 3):
            sub = [E for LL, E, m, _ in late if LL == L and pred(m)]
            if len(sub) < 3:
                continue
            p, l, h = S.wilson(sum(E == 3 for E in sub), len(sub))
            x = L + (gi - 0.5) * 0.22
            small = len(sub) < 10                          # hollow = too few papers to read much into
            axb.vlines([x], [100 * l], [100 * h], color=col, lw=0.7, alpha=0.6)
            axb.scatter([x], [100 * p], s=(1.5 * S.PT) ** 2, c=S.SURF if small else col, edgecolors=col,
                        linewidths=0.7, zorder=3)
            axb.text(x, 100 * h + 2.5, f"{len(sub)}", fontsize=4.0, color=col, ha="center")
        axb.scatter([3.6], [92 - gi * 7], s=(1.5 * S.PT) ** 2, c=col, edgecolors=col, linewidths=0.7)
        axb.text(3.8, 92 - gi * 7, lab, fontsize=4.8, color=col, va="center")
    axb.scatter([3.6], [78], s=(1.5 * S.PT) ** 2, c=S.SURF, edgecolors=S.INK3, linewidths=0.7)
    axb.text(3.8, 78, "hollow: n < 10", fontsize=4.6, color=S.INK2, va="center")
    axb.set_xticks([1, 2, 3], ["L1", "L2", "L3"])
    axb.set_xlim(0.6, 5.4); axb.set_ylim(-4, 100)
    axb.set_ylabel("Strongly verified, V3–V4 (%)", fontsize=5.3)
    axb.set_title("2024–2026 only · Wilson 95% CI · n above bars", fontsize=5.0, color=S.INK2, loc="left")
    for s in ("top", "right"):
        axb.spines[s].set_visible(False)
    axb.tick_params(labelsize=4.9, colors=S.INK2)
    S.save(fig, "fig_reach")
    print(f"rho={rho:.3f} CI=({lo:.3f},{hi:.3f})")


if __name__ == "__main__":
    main()
