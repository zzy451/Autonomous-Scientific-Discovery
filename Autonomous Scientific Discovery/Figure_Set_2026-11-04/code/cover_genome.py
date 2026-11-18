"""Cover · The papercard genome. 662 papers as radial slots grouped by primary field. Inner 11 tracks =
field membership (lit in the paper's mechanism colour); outer tracks = evidence endpoint, PDF archived,
note in repository, mechanism-label confidence."""
import math, collections as C
from matplotlib.collections import PatchCollection
from matplotlib.patches import Wedge, Circle
import style as S, proxies as X, cover as V


def main():
    cards = S.papercards(); px = X.load()
    prim = lambda c: c["fields"][0] if c["fields"] else "GM"
    groups = S.FIELDS + ["GM"]
    cards.sort(key=lambda c: (groups.index(prim(c)), c["year"], c["paper_id"]))
    fig, ax = V.canvas()
    cx, cy = V.CX, V.CY
    gap, label_gap = 1.4, 16.0                 # wide gap at 12 o'clock holds the track labels
    per = (360 - label_gap - gap * (len(groups) - 1)) / len(cards)
    a, ang, gspan = 90.0 - label_gap / 2, {}, {}
    for g in groups:
        g0 = a
        for c in [c for c in cards if prim(c) == g]:
            ang[c["paper_id"]] = (a, a - per); a -= per
        gspan[g] = (g0, a); a -= gap
    r_in, tw = 16.0, 2.55                      # field tracks
    tracks = [("evidence", 47.6), ("pdf", 51.2), ("note", 54.0), ("confidence", 56.8)]
    patches, colors = [], []
    for c in cards:
        a0, a1 = ang[c["paper_id"]]
        for i, f in enumerate(S.FIELDS):
            on = f in c["fields"]
            patches.append(Wedge((cx, cy), r_in + (i + 1) * tw, a1 + 0.04, a0 - 0.04, width=tw * 0.82))
            colors.append(V.MECH[c["mechanism"]] if on else V.FAINT)
        E = px[c["paper_id"]][0]
        lum = {3: 1.0, 2: 0.62, 1: 0.36, 0: 0.2, None: 0.0}[E]
        vals = {"evidence": lum, "pdf": 1.0 if c["pdf_in_repo"] else 0.0, "note": 1.0 if c["note_in_repo"] else 0.0,
                "confidence": {"high": 1.0, "medium": 0.5, "low": 0.22}[c["confidence"]]}
        for name, r in tracks:
            patches.append(Wedge((cx, cy), r + 2.2, a1 + 0.04, a0 - 0.04, width=2.2))
            colors.append(S.mix(V.FAINT, V.NEUTRAL, vals[name]))
    ax.add_collection(PatchCollection(patches, facecolors=colors, edgecolors="none", zorder=3))
    for g, (g0, g1) in gspan.items():
        if (g0 - g1) < 3:
            continue                             # the 2 general-method papers get no label
        name = S.FSHORT.get(g, "General") if (g0 - g1) > 12 else g
        V.curved(ax, name, cx, cy, (g0 + g1) / 2, 63.5, 6.2, V.TXT)
    for name, r in tracks:
        x, y = V.polar(cx, cy, 90, r + 1.1)
        ax.text(x, y, {"evidence": "Evidence endpoint", "pdf": "PDF archived", "note": "Note in repository",
                             "confidence": "Label confidence"}[name], fontsize=4.6, color=V.DIM, ha="center",
                va="center", zorder=31)
    for i, f in enumerate(S.FIELDS):
        x, y = V.polar(cx, cy, 90, r_in + (i + 0.6) * tw)
        ax.text(x, y, f, fontsize=4.0, color=V.DIM, ha="center", va="center", zorder=31)
    ax.text(cx, cy + 2.0, "662", fontsize=13, color=V.TXT, ha="center", va="center", fontweight="bold")
    ax.text(cx, cy - 3.2, "papercards", fontsize=5.6, color=V.DIM, ha="center", va="center")
    V.title(ax, "A record that can be re-checked", "The papercard genome")
    sw = lambda t: (lambda a_, x, y: a_.add_patch(Wedge((x, y - 1.2), 2.6, 60, 120, width=1.6,
                                                         fc=S.mix(V.FAINT, V.NEUTRAL, t), ec="none")))
    V.legend(ax, tiers=False, extra=("Outer tracks  ·  provenance from the same papercard", [
        (sw(1.0), "present / physical-formal / high"), (sw(0.5), "intermediate"), (sw(0.0), "absent / lowest")]))
    V.footer(ax, "662/662 notes and 635/635 PDFs found in commit 60f8bad · snapshot 1 Nov 2026")
    V.save(fig, "cover_genome")


if __name__ == "__main__":
    main()
