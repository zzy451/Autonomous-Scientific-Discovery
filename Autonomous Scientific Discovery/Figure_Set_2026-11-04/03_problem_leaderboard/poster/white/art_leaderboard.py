"""Leaderboard of closed loops (meeting request: field problems, links and solution status).
Per field, the top entries ranked by evidence endpoint (E3 > E2 > E1 > E0), then research-loop reach
(L4 first), then earliest year. Each row: system, year, status badge, reach badge, resolvable link.
The full table (all 662 papers, with the papercard's verbatim problem statement) is derived/leaderboard.csv."""
import csv, re
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import style as S, cover as V

W, H, TOP = 210.0, 297.0, 4
STATUS = {"E3": "strong", "E2": "computed", "E1": "benchmark", "E0": "claim"}
LUM = {"E3": 1.0, "E2": 0.62, "E1": 0.38, "E0": 0.22}


def link(u):
    m = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9.]+)", u)
    if m:
        return "arXiv:" + m.group(1)
    m = re.search(r"(10\.\d{4,9}/\S+)", u)
    if m:
        d = m.group(1).rstrip(".")
        return "doi:" + (d if len(d) <= 30 else d[:29] + "…")
    u = re.sub(r"^https?://(www\.)?", "", u)
    return u if len(u) <= 34 else u[:33] + "…"


def short(t, n=34):
    t = t.strip()
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"


def main():
    rows = list(csv.DictReader(open(S.DER / "leaderboard.csv", encoding="utf-8")))
    cards = {c["paper_id"]: c for c in S.papercards()}
    key = lambda r: (-(int(r["evidence_tier"][1:]) if r["evidence_tier"] else -1),
                     -(int(r["loop_reach"][1:]) if r["loop_reach"] else -1), int(r["year"]), r["paper_id"])
    fig = plt.figure(figsize=(W / 25.4, H / 25.4), facecolor=V.BG)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    ax.text(12, H - 12, "FIELD PROBLEMS, LINKS AND SOLUTION STATUS", fontsize=6.4, color=V.DIM, fontweight="bold", va="top")
    ax.text(12, H - 17, "Leaderboard of closed loops", fontsize=17, color=V.TXT, fontweight="bold", va="top")
    ax.text(12, H - 26, "Ranked within each field by verification strength, then system autonomy, then the earliest year.",
            fontsize=6.0, color=V.DIM, va="top")
    colx = [12.0, 112.0]
    y = {0: H - 36.0, 1: H - 36.0}
    for i, f in enumerate(S.FIELDS):
        col = 0 if i < 6 else 1
        x0 = colx[col]
        ent = sorted([r for r in rows if f in r["field"].split(";") and r["evidence_tier"] and r["loop_reach"]], key=key)[:TOP]
        yy = y[col]
        ax.text(x0, yy, f"{f}", fontsize=7.0, color=V.DIM, fontweight="bold", va="top")
        ax.text(x0 + 7, yy, S.FNAME[f], fontsize=8.0, color=V.TXT, fontweight="bold", va="top")
        n_field = sum(1 for r in rows if f in r["field"].split(";"))
        ax.text(x0 + 86, yy, f"{n_field} papers", fontsize=5.4, color=V.DIM, ha="right", va="top")
        ax.plot([x0, x0 + 86], [yy - 4.6, yy - 4.6], color=V.TXT, lw=0.6, alpha=0.7)
        yy -= 7.6
        for rank, r in enumerate(ent, 1):
            c = cards[r["paper_id"]]
            ax.text(x0, yy, f"{rank}", fontsize=8.5, color=V.TXT, fontweight="bold", va="center")
            ax.scatter([x0 + 5.2], [yy], s=(1.5 * S.PT) ** 2, c=V.MECH[c["mechanism"]], lw=0)
            ax.text(x0 + 7.4, yy + 1.5, short(r["system"]), fontsize=6.4, color=V.TXT, va="center", fontweight="bold")
            ax.text(x0 + 7.4, yy - 1.9, f"{r['year']}  ·  {link(r['link'])}  ·  {r['paper_id']}", fontsize=4.8,
                    color=V.DIM, va="center")
            st = r["evidence_tier"]
            ax.add_patch(FancyBboxPatch((x0 + 66, yy - 1.6), 12.0, 3.4, boxstyle="round,pad=0,rounding_size=1.6",
                                        fc=S.mix(V.FAINT, V.NEUTRAL, LUM[st]), ec="none"))
            ax.text(x0 + 72, yy + 0.1, STATUS[st], fontsize=4.9, color=V.BG if LUM[st] > 0.5 else V.TXT,
                    ha="center", va="center", fontweight="bold")
            ax.add_patch(FancyBboxPatch((x0 + 79.5, yy - 1.6), 6.5, 3.4, boxstyle="round,pad=0,rounding_size=1.6",
                                        fc="none", ec=V.TXT, lw=0.5))
            ax.text(x0 + 82.75, yy + 0.1, r["loop_reach"], fontsize=4.9, color=V.TXT, ha="center", va="center",
                    fontweight="bold")
            yy -= 6.5
        y[col] = yy - 3.2
    # legend
    ly = 20.0
    ax.text(12, ly + 4.5, "STATUS  ·  VERIFICATION STRENGTH", fontsize=5.4, color=V.DIM, fontweight="bold")
    x = 12
    for st in ("E3", "E2", "E1", "E0"):
        ax.add_patch(FancyBboxPatch((x, ly - 1.7), 12, 3.4, boxstyle="round,pad=0,rounding_size=1.6",
                                    fc=S.mix(V.FAINT, V.NEUTRAL, LUM[st]), ec="none"))
        ax.text(x + 6, ly, STATUS[st], fontsize=4.9, color=V.BG if LUM[st] > 0.5 else V.TXT, ha="center",
                va="center", fontweight="bold")
        ax.text(x + 13.2, ly, {"E3": "V3–V4 experiment / proof / replication", "E2": "V2 computational", "E1": "V1 benchmark / internal",
                               "E0": "V0 claim only"}[st], fontsize=5.4, color=V.TXT, va="center")
        x += 44
    ly -= 9
    ax.text(12, ly + 4.5, "DOT  ·  DECISION MECHANISM      BADGE  ·  SYSTEM AUTONOMY L0–L3", fontsize=5.4,
            color=V.DIM, fontweight="bold")
    x = 12
    for m in ("llm", "optimization", "hybrid", "classical"):
        ax.scatter([x + 1], [ly], s=(1.6 * S.PT) ** 2, c=V.MECH[m], lw=0)
        ax.text(x + 3, ly, V.MECH_SHORT[m], fontsize=5.4, color=V.TXT, va="center")
        x += 30
    ax.text(W - 12, 8, "full table: derived/leaderboard.csv (662 rows, verbatim problem statements) · snapshot 1 Nov 2026",
            fontsize=5.0, color=V.DIM, ha="right")
    S.save(fig, "art_leaderboard")


if __name__ == "__main__":
    main()
