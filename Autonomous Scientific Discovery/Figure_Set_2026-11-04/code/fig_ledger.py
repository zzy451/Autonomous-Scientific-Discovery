"""Fig. D - Papercard ledger. One column per cross-field paper: its field memberships
(coloured by decision mechanism) above the provenance trail that backs each mark."""
import collections as C
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import style as S

W, H = 183.0, 104.0
X0, X1 = 44.0, 144.0
GREY = ["#ece8e1", "#c9c2b6", "#8f877a", "#55504a", S.INK]


def evidence(s):
    if "full_text" in s or "preprint_pdf" in s:
        return 2
    if "source_limited" in s:
        return 0
    return 1


def main():
    cards = [c for c in S.papercards() if len(c["fields"]) > 1]
    cards.sort(key=lambda c: (-len(c["fields"]), tuple(c["fields"]), c["year"], c["paper_id"]))
    # small gap between k-groups
    xs, x, prev = [], X0, None
    pitch = (X1 - X0 - 1.2 * 6) / len(cards)
    for c in cards:
        k = len(c["fields"])
        if prev is not None and k != prev:
            x += 1.2
        xs.append(x); x += pitch; prev = k
    cw = pitch * 0.78

    fig = plt.figure(figsize=(W / 25.4, H / 25.4), facecolor=S.SURF)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    ax.text(2, H - 4, "Papercard ledger: every mark traces to an archived record", fontsize=9,
            fontweight="bold", color=S.INK, va="top")
    ax.text(2, H - 9, f"{len(cards)} cross-field papers (columns), sorted by number of fields then field set. "
            "Upper block: field memberships coloured by decision mechanism; lower block: provenance trail "
            "from the same papercard", fontsize=5.2, color=S.INK2, va="top")

    RH, CH = 3.1, 2.35
    top = 70.0
    frow = {f: top - i * RH for i, f in enumerate(S.FIELDS)}
    # k bars + IDs of the broadest papers
    for c, x in zip(cards, xs):
        k = len(c["fields"])
        ax.add_patch(Rectangle((x, top + 2.4), cw, 0.95 * k, fc=S.INK3, ec="none"))
    # callout for the broadest papers instead of rotated per-column labels
    broad = [(c, x) for c, x in zip(cards, xs) if len(c["fields"]) >= 5]
    bx0, bx1 = broad[0][1], broad[-1][1] + cw
    yb = top + 2.4 + 0.95 * 10 + 1.2
    ax.plot([bx0, bx0, bx1, bx1], [yb - 0.6, yb, yb, yb - 0.6], color=S.INK, lw=0.35)
    ax.plot([bx1, bx1 + 6], [yb, yb + 2.2], color=S.INK, lw=0.35)
    lines = [f"{c['paper_id']}  {c['title'].split(':')[0][:30]}  (k = {len(c['fields'])})"
             for c, _ in broad if len(c["fields"]) >= 6]
    lines.append("k = 5: " + ", ".join(c["paper_id"] for c, _ in broad if len(c["fields"]) == 5))
    for i, t in enumerate(lines):
        ax.text(bx1 + 7, yb + 2.2 - i * 2.6, t, fontsize=4.6, color=S.INK, va="center")
    ax.text(X0 - 2, top + 4, "fields per paper (k)", fontsize=4.7, color=S.INK2, ha="right", va="center")
    # field block
    for f in S.FIELDS:
        y = frow[f]
        ax.text(X0 - 2, y + CH / 2, f"{S.FNAME[f]}  {f}", fontsize=4.9, color=S.INK, ha="right", va="center")
        ax.add_patch(Rectangle((X0 - 0.6, y - 0.35), X1 - X0 + 1.2, CH + 0.7, fc="#f7f5f1", ec="none", zorder=0))
    for c, x in zip(cards, xs):
        for f in c["fields"]:
            ax.add_patch(Rectangle((x, frow[f]), cw, CH, fc=S.MECH[c["mechanism"]], ec="none"))
    # provenance block
    prov = [
        ("Era", lambda c: ["2004–2019", "2020–2023", "2024", "2025", "2026"].index(c["era"]),
         ["2004–19", "2020–23", "2024", "2025", "2026"]),
        ("Recorded venue", lambda c: {"unknown": 0, "preprint": 1, "conference": 3, "journal": 4}[c["venue_class"]],
         None),
        ("Note (papercard) in repo", lambda c: 4 if c["note_in_repo"] else 0, None),
        ("PDF archived in repo", lambda c: 4 if c["pdf_in_repo"] else 0, None),
        ("Source read for coding", lambda c: [0, 2, 4][evidence(c["evidence_status"])], None),
        ("Mechanism confidence", lambda c: {"low": 1, "medium": 2, "high": 4}[c["confidence"]], None),
        ("Mechanism checked on PDF", lambda c: 4 if c["mech_basis"] != "note" else 1, None),
    ]
    summary = {
        "Recorded venue": lambda cs: f"{sum(c['venue_class'] in ('journal', 'conference') for c in cs)} journal/conf. · "
                                     f"{sum(c['venue_class'] == 'preprint' for c in cs)} preprint",
        "Note (papercard) in repo": lambda cs: f"{sum(c['note_in_repo'] for c in cs)}/{len(cs)}",
        "PDF archived in repo": lambda cs: f"{sum(c['pdf_in_repo'] for c in cs)}/{len(cs)}",
        "Source read for coding": lambda cs: f"{sum(evidence(c['evidence_status']) == 2 for c in cs)} full text · "
                                             f"{sum(evidence(c['evidence_status']) == 1 for c in cs)} abstract/pages · "
                                             f"{sum(evidence(c['evidence_status']) == 0 for c in cs)} limited",
        "Mechanism confidence": lambda cs: " · ".join(f"{sum(c['confidence'] == v for c in cs)} {v}"
                                                      for v in ("high", "medium", "low")),
        "Mechanism checked on PDF": lambda cs: f"{sum(c['mech_basis'] != 'note' for c in cs)} on PDF · rest from note",
        "Era": lambda cs: " · ".join(f"{sum(c['era'] == e for c in cs)}" for e in
                                     ["2004–2019", "2020–2023", "2024", "2025", "2026"]) + " by era",
    }
    py0 = frow["11"] - 6.5
    for r, (name, fn, _) in enumerate(prov):
        y = py0 - r * RH
        ax.text(X0 - 2, y + CH / 2, name, fontsize=4.9, color=S.INK, ha="right", va="center")
        for c, x in zip(cards, xs):
            ax.add_patch(Rectangle((x, y), cw, CH, fc=GREY[fn(c)], ec="none"))
        ax.text(X1 + 1.5, y + CH / 2, summary[name](cards), fontsize=4.2, color=S.INK2, va="center")
    ax.text(X1 + 1.5, top + 4, "per row", fontsize=4.4, color=S.INK3, va="center", fontstyle="italic")
    ax.plot([X0 - 22, X1 + 12], [py0 + RH + 0.9, py0 + RH + 0.9], color=S.RULE, lw=0.4)

    # legends
    ly = 3.2
    lx = 2
    for m in S.MECH_ORDER:
        ax.add_patch(Rectangle((lx, ly - 0.8), 1.8, 1.8, fc=S.MECH[m], ec="none"))
        lab = S.MECH_LABEL[m]
        ax.text(lx + 2.5, ly + 0.1, lab, fontsize=4.6, color=S.INK, va="center")
        lx += 4.5 + len(lab) * 0.83
    lx += 4
    for i, lab in [(0, "absent / lowest"), (2, "intermediate"), (4, "present / highest")]:
        ax.add_patch(Rectangle((lx, ly - 0.8), 1.8, 1.8, fc=GREY[i], ec="none"))
        ax.text(lx + 2.5, ly + 0.1, lab, fontsize=4.6, color=S.INK, va="center")
        lx += 4.5 + len(lab) * 0.83
    S.save(fig, "fig_ledger")


if __name__ == "__main__":
    main()
