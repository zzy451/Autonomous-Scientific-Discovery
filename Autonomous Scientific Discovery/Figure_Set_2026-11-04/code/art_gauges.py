"""The instrument panel (proposal §1: announcement and benchmark score as instruments of progress, versus the
problems actually solved). Three dials, five needles each (one per era, brighter = later):
announcement = share of papers recorded as preprints; benchmark = share whose validation includes a
benchmark; closed = share with a physical, clinical, deployed or formal endpoint (E3)."""
import json, math
import numpy as np
from matplotlib.patches import Wedge, Circle, Polygon
import style as S, proxies as X, cover as V

ERAS = ["2004–2019", "2020–2023", "2024", "2025", "2026"]
GOLD = "#a87a1e" if V.LIGHT else "#ffd27a"


def bench_flag():
    out = {}
    for l in open(S.SRC / "papers.jsonl", encoding="utf-8"):
        p = json.loads(l)
        out[p["paper_id"]] = any(("benchmark" in X.fix(t).lower()) or ("基准" in X.fix(t))
                                 for t in (p.get("validation_type") or []))
    return out


def main():
    cards = S.papercards(); px = X.load(); bf = bench_flag()
    shares = {"Announcement": [], "Benchmark score": [], "Closed problems": []}
    for e in ERAS:
        ps = [c for c in cards if c["era"] == e]
        kn = [c for c in ps if c["venue_class"] != "unknown"]
        shares["Announcement"].append(sum(c["venue_class"] == "preprint" for c in kn) / len(kn))
        shares["Benchmark score"].append(sum(bf[c["paper_id"]] for c in ps) / len(ps))
        ev = [c for c in ps if px[c["paper_id"]][0] is not None]
        shares["Closed problems"].append(sum(px[c["paper_id"]][0] == 3 for c in ev) / len(ev))
    sub = {"Announcement": "share recorded as preprints", "Benchmark score": "share validated on a benchmark",
           "Closed problems": "share with a physical or formal endpoint"}
    fig, ax = V.canvas()
    R = 24.5
    for i, (name, vals) in enumerate(shares.items()):
        cx, cy = 36 + i * 64, 116
        ax.add_patch(Wedge((cx, cy), R + 2.2, 0, 180, width=0.5, fc=V.TXT, alpha=0.8, ec="none"))
        for t in range(0, 101, 5):                   # ticks
            a = math.radians(180 - 1.8 * t)
            r0 = R - (3.2 if t % 25 == 0 else 1.6)
            ax.plot([cx + r0 * math.cos(a), cx + R * math.cos(a)], [cy + r0 * math.sin(a), cy + R * math.sin(a)],
                    color=V.TXT, lw=0.6 if t % 25 == 0 else 0.3, alpha=0.8)
            if t % 25 == 0:
                ax.text(cx + (R - 6.5) * math.cos(a), cy + (R - 6.5) * math.sin(a), f"{t}", fontsize=4.8,
                        color=V.DIM, ha="center", va="center")
        for k, v in enumerate(vals):                 # needles, earliest dim -> latest bright
            a = math.radians(180 - 180 * v)
            col = S.mix(V.DIM, GOLD, k / 4)
            tip = (cx + (R - 1.0) * math.cos(a), cy + (R - 1.0) * math.sin(a))
            base_l = (cx + 0.9 * math.cos(a + math.pi / 2), cy + 0.9 * math.sin(a + math.pi / 2))
            base_r = (cx + 0.9 * math.cos(a - math.pi / 2), cy + 0.9 * math.sin(a - math.pi / 2))
            ax.add_patch(Polygon([base_l, tip, base_r], fc=col, ec="none", alpha=0.55 + 0.45 * k / 4, zorder=4 + k))
            if k in (0, 4):
                ax.text(cx + (R + 4.6) * math.cos(a), cy + (R + 4.6) * math.sin(a),
                        f"{100 * v:.0f}%", fontsize=6.2 if k == 4 else 5.2, color=col, ha="center", va="center",
                        fontweight="bold")
        ax.add_patch(Circle((cx, cy), 2.0, fc=V.TXT, ec="none", zorder=10))
        ax.text(cx, cy - 7, name, fontsize=8.5, color=V.TXT, ha="center", fontweight="bold")
        ax.text(cx, cy - 11.5, sub[name], fontsize=5.4, color=V.DIM, ha="center")
        ax.text(cx, cy - 15.5, ["instrument one", "instrument two", "the third instrument"][i], fontsize=5.0,
                color=GOLD, ha="center", fontstyle="italic")
        ax.text(cx, cy - 20.5, "  ·  ".join(f"{100 * v:.0f}" for v in vals) + " %", fontsize=5.2, color=V.TXT,
                ha="center")
        ax.text(cx, cy - 24.0, "2004–19 → 2026", fontsize=4.6, color=V.DIM, ha="center")
    # era key under the dials
    for k, e in enumerate(ERAS):
        x = 52 + k * 22
        ax.add_patch(Polygon([(x - 0.8, 70), (x + 4.5, 70.8), (x - 0.8, 71.6)], fc=S.mix(V.DIM, GOLD, k / 4), ec="none"))
        ax.text(x + 5.6, 70.8, e, fontsize=5.6, color=V.TXT, va="center")
    ax.text(52, 75.5, "NEEDLES  ·  ONE PER ERA, BRIGHTER = LATER", fontsize=5.4, color=V.DIM, fontweight="bold")
    V.title(ax, "Two instruments, and a third  ·  §1", "The instrument panel")
    V.footer(ax, "662 core papers (announcement: 657 with a known venue) · closed = V3–V4 · snapshot 1 Nov 2026")
    V.save(fig, "art_gauges")
    for k, v in shares.items():
        print(k, [round(100 * x) for x in v])


if __name__ == "__main__":
    main()
