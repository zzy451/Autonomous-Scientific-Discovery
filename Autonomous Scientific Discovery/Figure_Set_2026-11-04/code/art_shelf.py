"""Sixty-five new rulers (proposal §1: benchmark score as an instrument). Every core paper whose contribution
type is a benchmark or evaluation suite, as a spine on a shelf, bookended by year. Spine colour = decision
mechanism; cap brightness = evidence endpoint; base = field codes."""
import json
from matplotlib.patches import Rectangle
import style as S, proxies as X, cover as V


def is_bench(p):
    return any(("benchmark" in X.fix(t).lower()) or ("评测" in X.fix(t)) or ("基准" in X.fix(t))
               for t in (p.get("scientific_contribution_type") or []))


def short(t, n=30):
    t = t.split(":")[0].strip()
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"


def main():
    cards = {c["paper_id"]: c for c in S.papercards()}; px = X.load()
    recs = [json.loads(l) for l in open(S.SRC / "papers.jsonl", encoding="utf-8")]
    bench = sorted([cards[p["paper_id"]] for p in recs if p["paper_id"] in cards and is_bench(p)],
                   key=lambda c: (c["year"], c["paper_id"]))
    fig, ax = V.canvas()
    sw, sh, per = 6.1, 31.0, 23
    shelves = [bench[i:i + per] for i in range(0, len(bench), per)]
    ytop = 172.0
    lum = {3: 1.0, 2: 0.62, 1: 0.38, 0: 0.22, None: 0.1}
    for si, shelf in enumerate(shelves):
        yb = ytop - (si + 1) * (sh + 10.5)
        x = 14.0
        prev = None
        for c in shelf:
            if c["year"] != prev:                       # bookend with the year
                if prev is not None:
                    x += 2.0
                ax.add_patch(Rectangle((x, yb), 1.2, sh * 0.62, fc=V.TXT, ec="none", alpha=0.8))
                ax.text(x + 0.6, yb + sh * 0.62 + 1.2, str(c["year"]), fontsize=5.4, color=V.TXT, ha="center",
                        va="bottom", fontweight="bold")
                x += 2.4; prev = c["year"]
            col = V.MECH[c["mechanism"]]
            ax.add_patch(Rectangle((x, yb), sw - 0.5, sh, fc=S.mix(col, V.BG, 0.35), ec="none"))
            E = px[c["paper_id"]][0]
            ax.add_patch(Rectangle((x, yb + sh - 3.0), sw - 0.5, 3.0, fc=S.mix(V.FAINT, V.NEUTRAL, lum[E]), ec="none"))
            ax.text(x + (sw - 0.5) / 2, yb + 4.2, short(c["title"]), fontsize=4.6, color="#ffffff", rotation=90,
                    ha="center", va="bottom", fontweight="bold")
            ax.text(x + (sw - 0.5) / 2, yb + 1.6, "·".join(c["fields"][:3]) + ("+" if len(c["fields"]) > 3 else ""),
                    fontsize=2.9, color="#ffffff", ha="center", va="center", alpha=0.9)
            x += sw
        ax.plot([10, 190], [yb - 0.5, yb - 0.5], color=V.TXT, lw=1.4, alpha=0.85)
    V.title(ax, "Benchmark score as an instrument  ·  §1", f"{len(bench)} new rulers")
    cap = lambda t: (lambda a, x, y: a.add_patch(Rectangle((x - 1.3, y - 1.0), 2.6, 2.0,
                                                           fc=S.mix(V.FAINT, V.NEUTRAL, t), ec="none")))
    V.legend(ax, tiers=False, extra=("Spine cap  ·  the benchmark paper's own evidence endpoint", [
        (cap(1.0), "strong (V3–V4)"), (cap(0.62), "computational (V2)"), (cap(0.3), "benchmark / claim (V0–V1)")]))
    V.footer(ax, "core papers whose contribution type is a benchmark or evaluation suite · base = field codes · snapshot 1 Nov 2026")
    V.save(fig, "art_shelf")
    from collections import Counter
    print(len(bench), Counter(c["year"] for c in bench))


if __name__ == "__main__":
    main()
