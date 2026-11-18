"""Fig. C - Domain-pair matrix. Upper triangle: circle area = papers shared by two fields.
Lower triangle: Jaccard overlap. Diagonal: papers per field with cross-field share arc.
Order: average-linkage clustering on 1 - Jaccard."""
import itertools, math, collections as C
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Wedge
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform
import style as S

W, H = 120.0, 140.0
RAMP = ["#f4efe6", "#e3d3bd", "#c9ad8a", "#a3825d", "#715538", "#45321f"]   # one-hue sand -> umber


def ramp(t):
    t = min(max(t, 0), 1) * (len(RAMP) - 1)
    i = min(int(t), len(RAMP) - 2)
    return S.mix(RAMP[i], RAMP[i + 1], t - i)


def main():
    cards = S.papercards()
    members = C.defaultdict(set)
    for c in cards:
        for f in c["fields"]:
            members[f].add(c["paper_id"])
    F = S.FIELDS
    n = len(F)
    shared = np.zeros((n, n), int)
    jac = np.zeros((n, n))
    for i, j in itertools.product(range(n), range(n)):
        a, b = members[F[i]], members[F[j]]
        shared[i, j] = len(a & b)
        jac[i, j] = len(a & b) / len(a | b)
    Z = linkage(squareform(1 - jac, checks=False), "average")
    order = dendrogram(Z, no_plot=True)["leaves"]
    Fo = [F[i] for i in order]

    fig = plt.figure(figsize=(W / 25.4, H / 25.4), facecolor=S.SURF)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    X0, Y0, CS = 36.0, 110.0, 7.4            # matrix top-left corner, cell size
    cxy = lambda i, j: (X0 + (j + 0.5) * CS, Y0 - (i + 0.5) * CS)

    ax.text(2, H - 4, "Domain-pair matrix", fontsize=9, fontweight="bold", color=S.INK, va="top")
    ax.text(2, H - 9, "Papers shared by every pair of fields, ordered by overlap similarity", fontsize=5.4,
            color=S.INK2, va="top")

    # dendrogram above columns
    dn = dendrogram(Z, no_plot=True)
    dmax = max(max(d) for d in dn["dcoord"])
    for xs, ys in zip(dn["icoord"], dn["dcoord"]):
        px = [X0 + (x - 5) / 10 * CS + CS / 2 for x in xs]
        py = [Y0 + 2.0 + y / dmax * 10.5 for y in ys]
        ax.plot(px, py, color=S.INK3, lw=0.45, solid_capstyle="butt")
    smax = max(shared[i, j] for i in range(n) for j in range(n) if i != j)
    for a, fi in enumerate(Fo):
        for b, fj in enumerate(Fo):
            i, j = F.index(fi), F.index(fj)
            x, y = cxy(a, b)
            if a == b:
                tot = len(members[fi])
                multi = sum(1 for p in members[fi] if len(next(c for c in cards if c["paper_id"] == p)["fields"]) > 1)
                ax.add_patch(Rectangle((x - CS / 2, y - CS / 2), CS, CS, fc=S.INK, ec=S.SURF, lw=0.6))
                ax.add_patch(Wedge((x, y), CS * 0.42, 90 - 360 * multi / tot, 90, width=0.55, fc="#e3d3bd", ec="none"))
                ax.text(x, y, str(tot), fontsize=5.6, color=S.SURF, ha="center", va="center", fontweight="bold")
            elif b > a:
                v = shared[i, j]
                ax.add_patch(Rectangle((x - CS / 2, y - CS / 2), CS, CS, fc="#faf8f4", ec=S.SURF, lw=0.6))
                if v:
                    r = 0.47 * CS * math.sqrt(v / smax)
                    ax.add_patch(Circle((x, y), max(r, 0.35), fc=S.INK2 if v < 12 else S.INK, ec="none"))
                    if r > 1.25:
                        ax.text(x, y, str(v), fontsize=4.8 if v < 40 else 5.2, color=S.SURF, ha="center",
                                va="center", fontweight="bold")
                    else:
                        ax.text(x + CS * 0.36, y + CS * 0.28, str(v), fontsize=3.9, color=S.INK3, ha="right", va="top")
            else:
                ax.add_patch(Rectangle((x - CS / 2, y - CS / 2), CS, CS, fc=ramp(jac[i, j] / 0.3),
                                       ec=S.SURF, lw=0.6))
    for a, f in enumerate(Fo):
        x, y = cxy(a, a)
        ax.text(X0 - 1.5, y, f"{S.FNAME[f]}  {f}", fontsize=5.2, color=S.INK, ha="right", va="center")
        ax.text(cxy(0, a)[0], Y0 - n * CS - 1.5, f"{f}", fontsize=5.2, color=S.INK, ha="center", va="top",
                fontweight="bold")
    # keys
    ky = Y0 - n * CS - 9
    ax.text(X0, ky, "Upper · papers shared (circle area)", fontsize=5.2, fontweight="bold", color=S.INK)
    for k, v in enumerate([2, 12, 46]):
        r = 0.47 * CS * math.sqrt(v / smax)
        ax.add_patch(Circle((X0 + 3 + k * 8.5, ky - 5.2), r, fc=S.INK if v >= 12 else S.INK2, ec="none"))
        ax.text(X0 + 3 + k * 8.5 + r + 0.8, ky - 5.2, str(v), fontsize=4.8, color=S.INK2, va="center")
    kx = X0 + 44
    ax.text(kx, ky, "Lower · Jaccard overlap", fontsize=5.2, fontweight="bold", color=S.INK)
    for k in range(30):
        ax.add_patch(Rectangle((kx + k * 1.0, ky - 6.2), 1.0, 2.2, fc=ramp(k / 29), ec="none"))
    for v in (0, 0.1, 0.2, 0.3):
        ax.text(kx + v / 0.3 * 30, ky - 7, f"{v:.1f}" + ("+" if v == 0.3 else ""), fontsize=4.4, color=S.INK2,
                ha="center", va="top")
    ax.text(X0, ky - 12.5, "Diagonal · papers in field; light arc = share in ≥2 fields", fontsize=4.8, color=S.INK2)
    S.save(fig, "fig_matrix")


if __name__ == "__main__":
    main()
