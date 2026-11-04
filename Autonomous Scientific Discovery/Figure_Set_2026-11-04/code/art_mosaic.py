"""Two ledgers (proposal §2(2) status and §3 'survey completed'). Left: every one of the 1,133 records
in the project ledger as a tile, grouped by record status; core papers are lit in their mechanism colour
with brightness by evidence endpoint. Right: the 84 chronicle cases with the status counts reported in the
proposal (verified 63, claimed 10, contested 10, refuted 1) - quoted, not recomputed."""
import json, math, collections as C
from matplotlib.patches import Rectangle
import style as S, proxies as X, cover as V

GOLD = "#a87a1e" if V.LIGHT else "#ffd27a"
STAT = [("active_confirmed_core", "Core papers"), ("background_only", "Background"), ("candidate", "Pending review"),
        ("duplicate", "Duplicate"), ("excluded", "Excluded")]


def main():
    cards = {c["paper_id"]: c for c in S.papercards()}; px = X.load()
    recs = [json.loads(l) for l in open(S.SRC / "papers.jsonl", encoding="utf-8")]
    order = {k: i for i, (k, _) in enumerate(STAT)}
    ERA = ["2004–2019", "2020–2023", "2024", "2025", "2026"]
    recs.sort(key=lambda r: (order.get(r.get("record_status"), 9),
                             ERA.index(cards[r["paper_id"]]["era"]) if r["paper_id"] in cards else 0,
                             r["paper_id"]))
    fig, ax = V.canvas()
    ncol, t, g = 34, 3.05, 0.42
    x0, y0 = 10.0, 172.0
    alpha_t = {3: 1.0, 2: 0.78, 1: 0.55, 0: 0.4, None: 0.3}
    starts = {}
    for i, r in enumerate(recs):
        row, col = divmod(i, ncol)
        x, y = x0 + col * (t + g), y0 - row * (t + g)
        st = r.get("record_status")
        starts.setdefault(st, (x, y))
        if r["paper_id"] in cards:
            c = cards[r["paper_id"]]; E = px[c["paper_id"]][0]
            ax.add_patch(Rectangle((x, y - t), t, t, fc=V.MECH[c["mechanism"]], ec="none", alpha=alpha_t[E]))
            if E == 3:
                ax.add_patch(Rectangle((x + t * 0.32, y - t * 0.68), t * 0.36, t * 0.36, fc="#ffffff" if not V.LIGHT else V.BG,
                                       ec="none", alpha=0.85))
        elif st == "background_only":
            ax.add_patch(Rectangle((x, y - t), t, t, fc=V.DIM, ec="none", alpha=0.35))
        elif st == "candidate":
            ax.add_patch(Rectangle((x + 0.25, y - t + 0.25), t - 0.5, t - 0.5, fc="none", ec=V.TXT, lw=0.5))
        else:
            ax.add_patch(Rectangle((x, y - t), t, t, fc="none", ec=V.DIM, lw=0.35, alpha=0.6))
            ax.plot([x + 0.5, x + t - 0.5], [y - t + 0.5, y - 0.5], color=V.DIM, lw=0.35, alpha=0.6)
    cnt = C.Counter(r.get("record_status") for r in recs)
    xr = x0 + ncol * (t + g) + 1.5
    for k, lab in STAT:
        if k in starts:
            ax.text(xr, starts[k][1] - t / 2, f"{lab}  {cnt[k]}", fontsize=5.6, color=V.TXT, va="center",
                    fontweight="bold" if k == "active_confirmed_core" else "normal")
    # the proposal's 84 chronicle cases, as reported
    ox, oy, tt = 160.0, 150.0, 3.4
    ax.text(ox, oy + 12, "THE CHRONICLE'S 84 CASES", fontsize=5.4, color=V.DIM, fontweight="bold")
    ax.text(ox, oy + 8.5, "as reported in the proposal, §2", fontsize=5.0, color=V.DIM)
    seq = [("Verified", 63, GOLD, True), ("Claimed", 10, V.TXT, False), ("Contested", 10, V.DIM, True),
           ("Refuted", 1, "#c2453b" if not V.LIGHT else "#a63228", True)]
    i = 0
    for lab, n, col, fill in seq:
        for _ in range(n):
            row, cc = divmod(i, 7)
            x, y = ox + cc * (tt + 0.6), oy - row * (tt + 0.6)
            ax.add_patch(Rectangle((x, y - tt), tt, tt, fc=col if fill else "none", ec=col, lw=0.6, alpha=0.95))
            i += 1
    yl = oy - 13 * (tt + 0.6) - 4
    for lab, n, col, fill in seq:
        ax.add_patch(Rectangle((ox, yl - 1.4), 2.6, 2.6, fc=col if fill else "none", ec=col, lw=0.6))
        ax.text(ox + 4, yl, f"{lab}  {n}", fontsize=5.6, color=V.TXT, va="center"); yl -= 4.4
    V.title(ax, "Survey completed  ·  §2(2), §3", "Two ledgers")
    sq = lambda kind: (lambda a, x, y: a.add_patch(Rectangle((x - 1.3, y - 1.3), 2.6, 2.6,
                       fc=V.DIM if kind == "bg" else "none", ec=V.TXT if kind == "cand" else V.DIM,
                       alpha=0.5 if kind == "bg" else 1, lw=0.5)))
    V.legend(ax, extra=("Other tiles  ·  ledger records outside the core", [
        (sq("bg"), "background"), (sq("cand"), "pending review"), (sq("x"), "duplicate / excluded")]))
    V.footer(ax, "1,133 ledger records · white centre = strongly verified (V3–V4) · snapshot 1 Nov 2026")
    V.save(fig, "art_mosaic")


if __name__ == "__main__":
    main()
