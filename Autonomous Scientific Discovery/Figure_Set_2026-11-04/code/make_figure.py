"""Main figure: 'Strata of autonomous science' (183 mm, Nature double column).

Reads derived/*.csv (see build_data.py); writes out/main_figure.{pdf,svg,png}.
All geometry is in millimetres on a single full-figure axes, except panel e.
"""
import csv, math, collections as C
from pathlib import Path
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, PathPatch, Rectangle
from matplotlib.path import Path as MPath
import matplotlib.patheffects as pe
from scipy.ndimage import gaussian_filter1d

ROOT = Path(__file__).parent
DER, OUT = ROOT / "derived", ROOT / "out"

mpl.rcParams.update({
    "font.family": ["Arial", "Arial Unicode MS"], "font.size": 6, "pdf.fonttype": 42, "svg.fonttype": "none",
    "axes.linewidth": 0.4, "xtick.major.width": 0.4, "ytick.major.width": 0.4,
    "xtick.major.size": 2, "ytick.major.size": 2, "xtick.labelsize": 5.5, "ytick.labelsize": 5.5,
})

# ---- tokens ---------------------------------------------------------------
INK, INK2, INK3, RULE = "#1d1d1b", "#55524c", "#8a857c", "#d9d4cb"
SURF = "#ffffff"
# validated: validate_palette.js --pairs all, light -> ALL CHECKS PASS
MECH = {"classical": "#a8326e", "optimization": "#d9622b", "hybrid": "#1a9b74", "llm": "#2f5fb3"}
MECH_ORDER = ["classical", "optimization", "hybrid", "llm"]
MECH_LABEL = {"classical": "Symbolic, planning or learned policy (D1, D2, D4)",
              "optimization": "Optimization / probabilistic (D3)",
              "hybrid": "Hybrid (D6)", "llm": "LLM-driven (D5)"}
VENUE_ORDER = ["journal", "conference", "preprint", "unknown"]
VENUE_FILL = {"journal": INK, "conference": "#8f8a80", "preprint": SURF, "unknown": "#e7e3dc"}
ERAS = ["2004–2019", "2020–2023", "2024", "2025", "2026"]
ERA_SUB = {"2004–2019": "16 years", "2020–2023": "4 years", "2024": "", "2025": "", "2026": "to 22 Oct"}
FIELDS = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]
FNAME = {"01": "Formal & computational", "02": "Physics & astronomy", "03": "Chemistry",
         "04": "Materials", "05": "Earth & environment", "06": "Life sciences",
         "07": "Medicine & health", "08": "Agriculture & food", "09": "Engineering & industry",
         "10": "Aerospace, marine & transport", "11": "Social & knowledge systems"}

# (paper_id, field row, label, label x [mm], label height above row baseline [mm], ha)
MILESTONES = [
    ("ASD-0501", "06", "Robot Scientist", 44, 4.6, "right"),
    ("ASD-0645", "10", "EO-1 Autonomous Sciencecraft", 43, 4.8, "right"),
    ("ASD-0697", "05", "AEGIS on Curiosity", 51, 4.6, "left"),
    ("ASD-0605", "03", "Chemorobotic droplets", 44, 4.8, "right"),
    ("ASD-0466", "04", "ARES nanotube growth", 44, 4.4, "right"),
    ("ASD-0455", "03", "Mobile robotic chemist", 69, 6.0, "right"),
    ("ASD-0094", "03", "Coscientist", 78.5, 5.2, "left"),
    ("ASD-0016", "04", "A-Lab", 79, 5.4, "left"),
    ("ASD-0504", "09", "BEAR", 77.5, 4.4, "left"),
    ("ASD-0512", "01", "FunSearch", 97, 4.8, "right"),
    ("ASD-0090", "02", "k-agents", 97, 4.6, "right"),
    ("ASD-0069", "11", "The AI Scientist", 97, 4.6, "right"),
    ("ASD-0063", "01", "AlphaEvolve", 123, 5.0, "right"),
    ("ASD-0115", "06", "AI co-scientist", 121.5, 6.0, "right"),
    ("ASD-0054", "07", "Virtual Lab", 121.5, 6.0, "right"),
    ("ASD-0549", "02", "DeepInflation", 146.5, 6.6, "right"),
    ("ASD-0097", "06", "CellVoyager", 146.5, 7.0, "right"),
    ("ASD-0704", "11", "PaperRepro", 146.5, 6.6, "right"),
]

W, H = 183.0, 211.0
X0, X1 = 33.0, 168.0                     # plot band of panel a
ROW_TOP, ROW_DY = 186.0, 9.15            # baseline of row 01 and row spacing
P = 0.98                                 # hex pitch (mm)
DOT = 0.80                               # dot diameter (mm)
PT = 72 / 25.4                           # points per mm


def read(name):
    return list(csv.DictReader(open(DER / name, encoding="utf-8")))


def era_x(e):
    w = (X1 - X0) / len(ERAS)
    return X0 + w * (ERAS.index(e) + 0.5)


def pile(n):
    """Hex-packed pile: base length b = ceil(1.6*sqrt(n)), each row one shorter."""
    if n == 0:
        return []
    b = max(1, math.ceil(1.6 * math.sqrt(n)))
    pts, k = [], 0
    while len(pts) < n:
        L = max(1, b - k)
        take = min(L, n - len(pts))
        for j in range(take):
            pts.append(((j - (take - 1) / 2) * P, k * P * 0.866))
        k += 1
    return pts


def mm_scatter(ax, xs, ys, face, edge, lw=0.32, d=DOT, z=3):
    ax.scatter(xs, ys, s=(d * PT) ** 2, c=face, edgecolors=edge, linewidths=lw, zorder=z)


def main():
    papers = read("papers.csv")
    asg = read("assignments.csv")
    co = read("cooccur.csv")
    P_BY = {p["paper_id"]: p for p in papers}

    fig = plt.figure(figsize=(W / 25.4, H / 25.4))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    fig.patch.set_facecolor(SURF)

    panel_a(ax, papers, asg, P_BY)
    strips(ax, papers)
    panel_d(ax, asg, co)
    panel_e(fig, papers, asg)

    OUT.mkdir(exist_ok=True)
    for ext, kw in [("pdf", {}), ("svg", {}), ("png", {"dpi": 600})]:
        fig.savefig(OUT / f"main_figure.{ext}", facecolor=SURF, **kw)
    print("wrote", OUT)


# ---- panel a: strata ----------------------------------------------------------
def panel_a(ax, papers, asg, P_BY):
    rank = {m: i for i, m in enumerate(MECH_ORDER)}
    vrank = {"journal": 0, "conference": 1, "unknown": 2, "preprint": 3}
    cells = C.defaultdict(list)
    for r in asg:
        cells[(r["field"], r["era"])].append(r)
    fcount = C.Counter(r["field"] for r in asg)

    ax.text(2, H - 4, "a", fontsize=8, fontweight="bold", va="top")
    ax.text(6, H - 4, "Strata of autonomous science: every dot is one paper–field assignment",
            fontsize=7, fontweight="bold", va="top", color=INK)
    ax.text(6, H - 7.6, "Pile area ∝ number of assignments; within each pile older decision paradigms "
            "settle at the base and later ones cap the peak", fontsize=5.5, va="top", color=INK2)

    # era headers
    era_n = C.Counter(p["era"] for p in papers)
    hy = H - 13.5
    for e in ERAS:
        x = era_x(e)
        ax.text(x, hy, e, ha="center", va="bottom", fontsize=6.5, fontweight="bold", color=INK)
        sub = f"{era_n[e]} papers" + (f" · {ERA_SUB[e]}" if ERA_SUB[e] else "")
        ax.text(x, hy - 0.6, sub, ha="center", va="top", fontsize=5, color=INK2)
    w = (X1 - X0) / len(ERAS)
    for i in range(1, len(ERAS)):
        xb = X0 + w * i
        ax.plot([xb, xb], [ROW_TOP - 10 * ROW_DY - 1.5, hy + 3], color=RULE, lw=0.3, zorder=0)

    pos = {}
    xs_grid = np.linspace(X0, X1, 1400)
    for i, f in enumerate(FIELDS):
        base = ROW_TOP - i * ROW_DY
        # ridge silhouette: envelope of the piles, softened
        env = np.full_like(xs_grid, 0.35)
        for e in ERAS:
            n = len(cells[(f, e)])
            if not n:
                continue
            b = math.ceil(1.6 * math.sqrt(n)) * P
            hgt = len({round(y, 3) for _, y in pile(n)}) * P * 0.866 + 0.9
            half = b / 2 + 1.0
            prof = hgt * np.clip(1 - (np.abs(xs_grid - era_x(e)) - (half - hgt / math.tan(math.radians(60)))) /
                                 (hgt / math.tan(math.radians(60))), 0, 1)
            prof = np.minimum(prof, hgt)
            env = np.maximum(env, prof)
        env = gaussian_filter1d(env, 6)
        t = i / (len(FIELDS) - 1)
        fill = mix("#f3efe8", "#e6ddcf", t)
        line = mix("#d3c8b6", "#b9a98f", t)
        ax.fill_between(xs_grid, base - 0.45, base - 0.45 + env, color=fill, lw=0, zorder=1)
        ax.plot(xs_grid, base - 0.45 + env, color=line, lw=0.35, zorder=1.5)
        ax.plot([X0, X1], [base - 0.45, base - 0.45], color=line, lw=0.35, zorder=1.5)

        # row labels
        ax.text(3, base + 1.2, f, fontsize=5, color=INK3, va="center", fontweight="bold")
        ax.text(7, base + 1.2, FNAME[f], fontsize=5.8, color=INK, va="center")
        ax.text(X1 + 2.5, base + 1.2, f"{fcount[f]}", fontsize=5.5, color=INK, va="center")

        for e in ERAS:
            rows = sorted(cells[(f, e)], key=lambda r: (rank[r["mechanism"]], vrank[r["venue_class"]],
                                                       r["year"], r["paper_id"]))
            for (dx, dy), r in zip(pile(len(rows)), rows):
                x, y = era_x(e) + dx, base + DOT / 2 + dy
                pos[(r["paper_id"], f)] = (x, y)
                col = MECH[r["mechanism"]]
                v = r["venue_class"]
                if v == "preprint":
                    mm_scatter(ax, [x], [y], SURF, col, lw=0.45, d=DOT * 0.92)
                elif v == "unknown":
                    mm_scatter(ax, [x], [y], mix(col, "#ffffff", 0.55), col, lw=0.3)
                else:
                    mm_scatter(ax, [x], [y], col, SURF, lw=0.2)

    ax.text(X1 + 2.5, ROW_TOP + 5.2, "n", fontsize=5.5, color=INK2, fontstyle="italic")

    # milestones: ring the dot, leader to the inner lower corner of a two-line label
    halo = [pe.withStroke(linewidth=1.3, foreground=SURF)]
    for pid, f, label, lx, lh, ha in MILESTONES:
        x, y = pos[(pid, f)]
        base = ROW_TOP - FIELDS.index(f) * ROW_DY
        ly = base + lh
        ax.add_patch(Circle((x, y), DOT * 0.95, fill=False, ec=INK, lw=0.5, zorder=6))
        ex = lx + (0.4 if ha == "right" else -0.4)
        ax.plot([x, ex], [y + DOT * 0.95, ly - 1.75], color=INK, lw=0.3, zorder=5,
                solid_capstyle="round", path_effects=halo)
        ax.text(lx, ly, label, fontsize=5, color=INK, ha=ha, va="bottom", zorder=7,
                fontweight="bold", path_effects=halo)
        ax.text(lx, ly - 0.1, P_BY[pid]["year"], fontsize=4.6, color=INK2, ha=ha, va="top",
                zorder=7, path_effects=halo)
    legend_a(ax)


def legend_a(ax):
    y = 74.6  # just under strip c, above bottom panels
    x = 33
    ax.text(x - 31, y, "Decision mechanism", fontsize=5.5, fontweight="bold", va="center", color=INK)
    for m in MECH_ORDER:
        mm_scatter(ax, [x], [y], MECH[m], SURF, lw=0.2, d=1.3)
        ax.text(x + 1.3, y, MECH_LABEL[m], fontsize=5.3, va="center", color=INK)
        x += 6 + len(MECH_LABEL[m]) * 0.93
    y -= 3.6; x = 33
    ax.text(x - 31, y, "Recorded venue", fontsize=5.5, fontweight="bold", va="center", color=INK)
    for v, lab in [("journal", "Journal or conference (filled)"), ("preprint", "Preprint (open ring)"),
                   ("unknown", "Unknown (tint)")]:
        face = {"journal": INK3, "preprint": SURF, "unknown": "#d8d4cc"}[v]
        mm_scatter(ax, [x], [y], face, INK3 if v != "journal" else SURF, lw=0.45, d=1.3)
        ax.text(x + 1.3, y, lab, fontsize=5.3, va="center", color=INK)
        x += 6 + len(lab) * 0.93
    ax.add_patch(Circle((x + 0.2, y), 0.75, fill=False, ec=INK, lw=0.5))
    ax.text(x + 1.6, y, "Milestone (ringed)", fontsize=5.3, va="center", color=INK)
    y -= 3.6; x = 33
    ax.text(x - 31, y, "Venue share (c)", fontsize=5.5, fontweight="bold", va="center", color=INK)
    for v, lab in [("journal", "Journal"), ("conference", "Conference"), ("preprint", "Preprint"),
                   ("unknown", "Unknown")]:
        ax.add_patch(Rectangle((x - 0.9, y - 0.9), 1.8, 1.8, fc=VENUE_FILL[v],
                               ec=INK3 if v == "preprint" else "none", lw=0.3))
        ax.text(x + 1.4, y, lab, fontsize=5.3, va="center", color=INK)
        x += 6 + len(lab) * 0.93


# ---- strips b, c: composition by era, aligned with panel a ---------------------
def strips(ax, papers):
    w = (X1 - X0) / len(ERAS)
    bw = w * 0.80
    yb = ROW_TOP - 10 * ROW_DY - 7.6
    yc = yb - 7.2
    for y, letter, title, key, order, color in [
        (yb, "b", "Mechanism share", "mechanism", MECH_ORDER, lambda k: MECH[k]),
        (yc, "c", "Venue share", "venue_class", VENUE_ORDER, lambda k: VENUE_FILL[k]),
    ]:
        ax.text(2, y + 1.6, letter, fontsize=8, fontweight="bold", va="center")
        ax.text(7, y + 1.6, title, fontsize=5.8, va="center", color=INK, fontweight="bold")
        ax.text(7, y - 0.9, "% of papers per era", fontsize=4.8, va="center", color=INK2)
        for e in ERAS:
            sub = [p for p in papers if p["era"] == e]
            cnt = C.Counter(p[key] for p in sub)
            x = era_x(e) - bw / 2
            for k in order:
                frac = cnt[k] / len(sub)
                if frac == 0:
                    continue
                seg = bw * frac
                ec = INK3 if k == "preprint" else "none"
                ax.add_patch(Rectangle((x + 0.15, y), max(seg - 0.3, 0.12), 3.0, fc=color(k),
                                       ec=ec, lw=0.3, zorder=3))
                if k in ("llm", "optimization", "classical", "preprint", "journal") and frac >= 0.17:
                    tc = INK if k == "preprint" else SURF
                    ax.text(x + seg / 2, y + 1.5, f"{100 * frac:.0f}", fontsize=4.8, color=tc,
                            ha="center", va="center", zorder=4, fontweight="bold")
                x += seg


# ---- panel d: cross-field ties ----------------------------------------------------
def panel_d(ax, asg, co):
    cx, cy, R = 44.0, 32.5, 18.5
    ax.text(2, 61.5, "d", fontsize=8, fontweight="bold", va="center")
    ax.text(6, 61.5, "Cross-field ties", fontsize=6.5, fontweight="bold", va="center", color=INK)
    ax.text(6, 58.6, "198 papers sit in ≥2 fields; ribbon width ∝ shared papers",
            fontsize=5, va="center", color=INK2)
    fcount = C.Counter(r["field"] for r in asg)
    ang = {f: math.pi / 2 - 2 * math.pi * i / len(FIELDS) for i, f in enumerate(FIELDS)}
    pt = {f: (cx + R * math.cos(a), cy + R * math.sin(a)) for f, a in ang.items()}
    edges = sorted(((int(r["n"]), r["a"], r["b"]) for r in co), reverse=True)
    nmax = edges[0][0]
    def ctrl(a, b):
        (x1, y1), (x2, y2) = pt[a], pt[b]
        return (x1, y1), (cx + 0.12 * ((x1 + x2) / 2 - cx), cy + 0.12 * ((y1 + y2) / 2 - cy)), (x2, y2)
    for n, a, b in sorted(edges):
        p0, c1, p2 = ctrl(a, b)
        path = MPath([p0, c1, p2], [MPath.MOVETO, MPath.CURVE3, MPath.CURVE3])
        strong = n >= 12
        ax.add_patch(PathPatch(path, fc="none", ec=INK if strong else INK3,
                               lw=0.2 + 3.0 * n / nmax, alpha=0.62 if strong else 0.2,
                               capstyle="round", zorder=2))
    for f in FIELDS:
        x, y = pt[f]
        r = 0.55 + 2.3 * math.sqrt(fcount[f] / max(fcount.values()))
        ax.add_patch(Circle((x, y), r, fc=INK, ec=SURF, lw=0.6, zorder=4))
        a = ang[f]
        lx, ly = cx + (R + r + 1.6) * math.cos(a), cy + (R + r + 1.6) * math.sin(a)
        ha = "left" if math.cos(a) > 0.2 else "right" if math.cos(a) < -0.2 else "center"
        va = "bottom" if math.sin(a) > 0.5 else "top" if math.sin(a) < -0.5 else "center"
        ax.text(lx, ly, f"{f} {FNAME[f].split(' &')[0].split(',')[0]}", fontsize=5, ha=ha, va=va,
                color=INK, zorder=5)
    # label the strongest ties at the ribbon midpoint
    for n, a, b in edges[:4]:
        p0, c1, p2 = ctrl(a, b)
        mx, my = [0.25 * p0[k] + 0.5 * c1[k] + 0.25 * p2[k] for k in (0, 1)]
        ax.text(mx, my, str(n), fontsize=5, ha="center", va="center", color=INK,
                fontweight="bold", zorder=6, bbox=dict(boxstyle="round,pad=0.15", fc=SURF, ec="none"))
    ax.text(cx, cy - R - 9.5, "Node area ∝ field assignments; dark ribbons ≥ 12 shared papers",
            fontsize=4.8, color=INK2, ha="center")


# ---- panel e: field signatures -----------------------------------------------
def panel_e(fig, papers, asg):
    ax_l = fig.add_axes([108 / W, 9 / H, 70 / W, 47 / H])
    fig.text(94 / W, 61.5 / H, "e", fontsize=8, fontweight="bold", va="center")
    fig.text(98 / W, 61.5 / H, "Field signatures", fontsize=6.5, fontweight="bold", va="center", color=INK)
    fig.text(98 / W, 58.6 / H, "Share of a field's papers that are LLM-driven vs. recorded as preprints",
             fontsize=5, va="center", color=INK2)
    byf = C.defaultdict(set)
    for r in asg:
        byf[r["field"]].add(r["paper_id"])
    P_BY = {p["paper_id"]: p for p in papers}
    allp = [p for p in papers if p["venue_class"] != "unknown"]
    gx = 100 * sum(p["mechanism"] == "llm" for p in papers) / len(papers)
    gy = 100 * sum(p["venue_class"] == "preprint" for p in allp) / len(allp)
    ax_l.axvline(gx, color=RULE, lw=0.5, zorder=0); ax_l.axhline(gy, color=RULE, lw=0.5, zorder=0)
    ax_l.text(gx + 1, 3, f"corpus {gx:.0f}%", fontsize=4.8, color=INK3)
    ax_l.text(2, gy + 1.5, f"corpus {gy:.0f}%", fontsize=4.8, color=INK3)
    # label anchor (x, y) in data units and alignment; Chemistry and Earth coincide at (67, 58)
    LAB = {"01": (84, 98, "right"), "02": (83, 91.5, "right"), "03": (62.5, 63, "right"),
           "04": (63.5, 44, "left"), "05": (72, 53.5, "left"), "06": (78, 70, "right"),
           "07": (99.5, 69.5, "right"), "08": (73.5, 82, "right"), "09": (88, 62.5, "center"),
           "10": (15, 19, "left"), "11": (99.5, 88.5, "right")}
    pts = []
    for f in FIELDS:
        ps = [P_BY[i] for i in byf[f]]
        x = 100 * sum(p["mechanism"] == "llm" for p in ps) / len(ps)
        kn = [p for p in ps if p["venue_class"] != "unknown"]
        y = 100 * sum(p["venue_class"] == "preprint" for p in kn) / len(kn)
        early = sum(p["era"] in ("2004–2019", "2020–2023") for p in ps) / len(ps)
        pts.append((len(ps), f, x, y, early))
    for n, f, x, y, early in sorted(pts, reverse=True):
        s = (0.9 + 4.2 * math.sqrt(n / 172)) * PT
        ax_l.scatter([x], [y], s=s ** 2, c=mix("#f1ece4", "#5b4a36", min(1, early * 1.5)),
                     edgecolors=INK, linewidths=0.45, zorder=3)
        lx, ly, ha = LAB[f]
        ax_l.annotate(FNAME[f].split(" &")[0].split(",")[0], (x, y), (lx, ly), fontsize=5, color=INK,
                      ha=ha, va="center", zorder=4,
                      arrowprops=dict(arrowstyle="-", lw=0.3, color=INK3, shrinkA=0.5, shrinkB=2.2))
    llm_pp = [p["venue_class"] == "preprint" for p in allp if p["mechanism"] == "llm"]
    oth_pp = [p["venue_class"] == "preprint" for p in allp if p["mechanism"] != "llm"]
    ax_l.text(3, 47, f"Of LLM-driven papers,\n{100 * sum(llm_pp) / len(llm_pp):.0f}% are preprints;"
              f"\nof all others, {100 * sum(oth_pp) / len(oth_pp):.0f}%", fontsize=5.3,
              color=INK, va="top", linespacing=1.3, fontweight="bold")
    ax_l.set_xlim(0, 100); ax_l.set_ylim(0, 100)
    ax_l.set_xlabel("LLM-driven (D5), % of field's papers", fontsize=5.5, labelpad=1.5)
    ax_l.set_ylabel("Preprint, % of field's papers", fontsize=5.5, labelpad=1.5)
    for s in ("top", "right"):
        ax_l.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax_l.spines[s].set_color(INK3)
    ax_l.tick_params(colors=INK2)
    ax_l.set_facecolor("none")
    # size / tint key
    ax_l.text(99, 18, "Bubble area ∝ papers in field\nDarker = larger share before 2024",
              fontsize=4.8, color=INK2, ha="right", va="top", linespacing=1.3)


def mix(a, b, t):
    ca, cb = np.array(mpl.colors.to_rgb(a)), np.array(mpl.colors.to_rgb(b))
    return mpl.colors.to_hex((1 - t) * ca + t * cb)


if __name__ == "__main__":
    main()
