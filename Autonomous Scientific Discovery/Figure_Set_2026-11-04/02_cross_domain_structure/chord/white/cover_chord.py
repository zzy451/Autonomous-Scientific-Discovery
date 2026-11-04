"""Cover · Luminous chord of cross-domain ties. Arc = a field's cross-field pair-ends; each ribbon joins two
fields and is split by the decision mechanism of the papers they share (width proportional to papers)."""
import itertools, math, collections as C
from matplotlib.patches import PathPatch, Wedge
from matplotlib.path import Path as MPath
import style as S, cover as V

ORDER = ["llm", "optimization", "hybrid", "classical"]


def main():
    cards = S.papercards()
    pair = C.Counter()
    for c in cards:
        for a, b in itertools.combinations(sorted(c["fields"]), 2):
            pair[(a, b, c["mechanism"])] += 1
    ends = C.Counter()
    for (a, b, m), n in pair.items():
        ends[a] += n; ends[b] += n
    fig, ax = V.canvas()
    cx, cy, R = V.CX, V.CY, V.RMAX
    span = V.sectors({f: ends[f] for f in S.FIELDS}, gap=2.2)
    per = (span["01"][0] - span["01"][1]) / ends["01"]           # degrees per pair-end
    cursor = {f: span[f][0] for f in S.FIELDS}
    idx = {f: i for i, f in enumerate(S.FIELDS)}
    seg = {}
    for f in S.FIELDS:   # partners in clockwise order from f, then mechanism
        partners = sorted([g for g in S.FIELDS if g != f], key=lambda g: (idx[g] - idx[f]) % 11)
        for g in partners:
            a, b = sorted((f, g))
            for m in ORDER:
                n = pair[(a, b, m)]
                if n:
                    seg[(f, g, m)] = (cursor[f], cursor[f] - n * per)
                    cursor[f] -= n * per
    # ribbons: biggest first so thin ones stay on top
    rib = sorted({(a, b, m): n for (a, b, m), n in pair.items()}.items(), key=lambda t: -t[1])
    for (a, b, m), n in rib:
        a0, a1 = seg[(a, b, m)]; b0, b1 = seg[(b, a, m)]
        P = lambda ang: V.polar(cx, cy, ang, R - 0.6)
        verts = [P(a0)]; codes = [MPath.MOVETO]
        for t in (0.33, 0.66, 1.0):
            verts.append(P(a0 + (a1 - a0) * t)); codes.append(MPath.LINETO)
        verts += [(cx, cy), P(b0)]; codes += [MPath.CURVE3, MPath.CURVE3]
        for t in (0.33, 0.66, 1.0):
            verts.append(P(b0 + (b1 - b0) * t)); codes.append(MPath.LINETO)
        verts += [(cx, cy), P(a0)]; codes += [MPath.CURVE3, MPath.CURVE3]
        path = MPath(verts, codes)
        ax.add_patch(PathPatch(path, fc=V.MECH[m], ec="none", alpha=(0.30 if m == "llm" else 0.75) if n >= 3 else 0.5, zorder=3 if m == "llm" else 3.2))
        ax.add_patch(PathPatch(path, fc="none", ec=V.MECH[m], lw=0.3, alpha=0.9, zorder=3.1 if m == "llm" else 3.3))
    for f, (s0, s1) in span.items():
        ax.add_patch(Wedge((cx, cy), R + 3.2, s1, s0, width=2.6, fc=V.TXT, ec="none", zorder=4))
        lab = S.FSHORT[f] if (s0 - s1) > 13 else f
        V.curved(ax, lab, cx, cy, (s0 + s1) / 2, R + 7.4, 6.4, V.TXT)
        V.curved(ax, str(ends[f]), cx, cy, (s0 + s1) / 2, R + 1.9, 4.4, V.BG, weight="bold", track=0.05) \
            if (s0 - s1) > 6 else None
    # label the four widest ties at the centre-side end of the ribbon
    tot = C.Counter()
    for (a, b, m), n in pair.items():
        tot[(a, b)] += n
    for (a, b), n in tot.most_common(4):
        ang = [ (seg[(a, b, m)][0] + seg[(a, b, m)][1]) / 2 for m in ORDER if (a, b, m) in seg]
        x, y = V.polar(cx, cy, sum(ang) / len(ang), R * 0.72)
        ax.text(x, y, f"{S.FSHORT[a]}–{S.FSHORT[b]}  {n}", fontsize=5.6, color=V.TXT, ha="center", va="center",
                fontweight="bold", zorder=6, bbox=dict(boxstyle="round,pad=0.2", fc=V.BG, ec="none", alpha=0.7))
    V.title(ax, "Cross-domain structure", "One paper, many fields")
    arc = lambda a_, x, y: a_.add_patch(Wedge((x, y - 1.6), 2.6, 55, 125, width=1.0, fc=V.TXT, ec="none"))
    V.legend(ax, tiers=False, extra=("Ribbons  ·  papers shared by two fields", [
        (arc, "arc = a field's cross-field pair-ends (printed); ribbon width ∝ shared papers")]))
    V.footer(ax, "198 cross-field papers · 422 field pairs · snapshot 1 Nov 2026")
    V.save(fig, "cover_chord")


if __name__ == "__main__":
    main()
