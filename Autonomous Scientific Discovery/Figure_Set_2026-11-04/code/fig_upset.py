"""Fig. B - Field combinations (UpSet). Each column is one exact set of fields shared by
>= 2 papers' assignments; bars stack papers by decision mechanism."""
import collections as C
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import style as S

W, H = 183.0, 112.0
TOPN = 30


def main():
    cards = [c for c in S.papercards() if len(c["fields"]) > 1]
    combos = C.defaultdict(list)
    for c in cards:
        combos[tuple(sorted(c["fields"]))].append(c)
    order = sorted(combos, key=lambda k: (-len(combos[k]), len(k), k))
    shown = [k for k in order if len(combos[k]) >= 2][:TOPN]
    rest = [c for k in order if k not in shown for c in combos[k]]

    fig = plt.figure(figsize=(W / 25.4, H / 25.4), facecolor=S.SURF)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    X0, CW = 58.0, 3.95                       # matrix left, column pitch
    ROW_Y0, RH = 8.0, 3.35                    # bottom row baseline, row pitch
    BAR0, BARH = ROW_Y0 + 11 * RH + 3.0, 46.0
    rows = {f: ROW_Y0 + (10 - i) * RH for i, f in enumerate(S.FIELDS)}   # 01 on top
    ymax = len(combos[shown[0]])

    ax.text(2, H - 4, "Which fields does one paper span?", fontsize=9, fontweight="bold", color=S.INK, va="top")
    ax.text(2, H - 9, f"Exact field combinations of the {len(cards)} cross-field papers; the {len(shown)} combinations "
            f"held by ≥2 papers are shown, {len(rest)} papers in singleton combinations are pooled at right",
            fontsize=5.4, color=S.INK2, va="top")

    # row stripes + labels + set-size bars (left)
    fa = C.Counter(f for c in S.papercards() for f in c["fields"])
    fx = C.Counter(f for c in cards for f in c["fields"])
    for i, f in enumerate(S.FIELDS):
        y = rows[f]
        if i % 2 == 0:
            ax.add_patch(Rectangle((X0 - 2, y - RH / 2), CW * (len(shown) + 2) + 2, RH, fc="#f5f2ec", ec="none", zorder=0))
        ax.text(X0 - 3.5, y, f"{f}  {S.FNAME[f]}", fontsize=5.3, color=S.INK, ha="right", va="center")
        L = 17.0 * fa[f] / max(fa.values())
        Lx = 17.0 * fx[f] / max(fa.values())
        ax.add_patch(Rectangle((5 + 17 - L, y - 1.0), L - Lx, 2.0, fc="#d6cfc3", ec="none"))
        ax.add_patch(Rectangle((5 + 17 - Lx, y - 1.0), Lx, 2.0, fc=S.INK, ec="none"))
        ax.text(5 + 17 - L - 0.6, y, str(fa[f]), fontsize=4.3, color=S.INK2, ha="right", va="center")
    yk = ROW_Y0 - 3.2
    ax.text(2, yk, "Field assignments:", fontsize=4.6, color=S.INK2, va="center")
    for xk, fc, lab in [(17.5, S.INK, "in cross-field papers"), (37.5, "#d6cfc3", "single-field")]:
        ax.add_patch(Rectangle((xk, yk - 0.75), 1.5, 1.5, fc=fc, ec="none"))
        ax.text(xk + 2.1, yk, lab, fontsize=4.6, color=S.INK2, va="center")

    # intersection columns
    cols = shown + ["rest"]
    for j, k in enumerate(cols):
        x = X0 + j * CW + (CW if k == "rest" else 0)
        ps = rest if k == "rest" else combos[k]
        # stacked mechanism bar
        y = BAR0
        cnt = C.Counter(p["mechanism"] for p in ps)
        scale = BARH / max(ymax, len(rest)) if k == "rest" else BARH / max(ymax, len(rest))
        for m in S.MECH_ORDER:
            h = cnt[m] * scale
            if h:
                ax.add_patch(Rectangle((x - CW * 0.36, y), CW * 0.72, max(h - 0.25, 0.15), fc=S.MECH[m], ec="none"))
                y += h
        ax.text(x, y + 0.8, str(len(ps)), fontsize=4.8, color=S.INK, ha="center", va="bottom")
        if k == "rest":
            ax.text(x, ROW_Y0 + 5 * RH, "other\ncombinations", fontsize=4.6, color=S.INK2, ha="center",
                    va="center", rotation=90, linespacing=1.1)
            continue
        on = [rows[f] for f in k]
        for f in S.FIELDS:
            ax.scatter([x], [rows[f]], s=(1.55 * S.PT) ** 2, c=S.INK if f in k else "#dcd6cc", edgecolors="none", zorder=3)
        ax.plot([x, x], [min(on), max(on)], color=S.INK, lw=1.0, zorder=2)
    # bar axis
    for v in range(0, ymax + 1, 10):
        yy = BAR0 + v * BARH / max(ymax, len(rest))
        ax.plot([X0 - 2.5, X0 - 1.8], [yy, yy], color=S.INK3, lw=0.4)
        ax.text(X0 - 3.2, yy, str(v), fontsize=4.8, color=S.INK2, ha="right", va="center")
    ax.plot([X0 - 1.8, X0 - 1.8], [BAR0, BAR0 + ymax * BARH / max(ymax, len(rest))], color=S.INK3, lw=0.4)
    ax.text(X0 - 9, BAR0 + BARH / 2, "Papers", fontsize=5.3, color=S.INK, rotation=90, va="center", ha="center")

    # annotations on the two leading combinations
    for j, k in enumerate(shown[:2]):
        x = X0 + j * CW
        top = BAR0 + len(combos[k]) * BARH / max(ymax, len(rest))
        share = sum(p["mechanism"] == "llm" for p in combos[k]) / len(combos[k])
        ax.text(x + 2.6, top - 2, f"{S.FSHORT[k[0]]} × {S.FSHORT[k[1]]}\n{100 * share:.0f}% LLM-driven",
                fontsize=4.8, color=S.INK, va="top", linespacing=1.2)

    # legend
    lx, ly = 2, BAR0 + BARH - 2
    ax.text(lx, ly, "Bar colour · decision mechanism", fontsize=5.3, fontweight="bold", color=S.INK)
    for m in S.MECH_ORDER:
        ly -= 3.3
        ax.add_patch(Rectangle((lx, ly - 0.4), 2.2, 2.0, fc=S.MECH[m], ec="none"))
        ax.text(lx + 3.2, ly + 0.6, S.MECH_LABEL[m], fontsize=4.8, color=S.INK, va="center")
    S.save(fig, "fig_upset")


if __name__ == "__main__":
    main()
