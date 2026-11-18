"""Cross-domain wormhole: the atlas ring repeated per era along a 3D time axis.

Each era (2004-2019 ... 2026) is one atlas ring with the same angular layout as fig_atlas, tilted 10 deg
and radius proportional to sqrt(paper-field assignments in that era). Inside a ring: that era's
cross-field pairs as bundled curves (colour = decision mechanism) and one dot per assignment on a
research-loop reach track (L0 innermost, uncoded; L4 at the rim). Between rings, each field's arc is
extruded into a translucent curtain of strands (one strand per third-level boundary).

Usage: python3 fig_wormhole.py [--view=tunnel|flare|mouth] [--light]
"""
import sys, math, collections as C
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection, PolyCollection
import style as S, proxies as X
from fig_atlas import layout, spline

VIEW = next((a.split("=")[1] for a in sys.argv if a.startswith("--view=")), "diag45")
LIGHT = True                                        # one version only: white background
BY_REACH = "--color=reach" in sys.argv          # variant: colour = research-loop reach instead of mechanism
CAM = {  # azimuth (deg from time axis), elevation, ring spacing, canvas, origin, scale
    "tunnel": dict(az=34, el=14, dx=62, W=240, H=150, u0=44, v0=70, sc=1.0, D=900),
    "diag45": dict(az=45, el=18, dx=88, W=240, H=155, u0=48, v0=74, sc=1.0, D=800),
    "flare": dict(az=52, el=28, dx=84, W=240, H=160, u0=52, v0=78, sc=0.95, D=700),
    "mouth": dict(az=86, el=7, dx=48, W=200, H=200, u0=86, v0=104, sc=0.92, D=230),
}[VIEW]
BG = "#fbfaf7" if LIGHT else "#07090d"
TXT = "#1d1d1b" if LIGHT else "#ece9e2"
DIM = "#77736b" if LIGHT else "#8e8a82"
STRAND = "#6b665c" if LIGHT else "#c9d3e2"
MECH = S.MECH if LIGHT else S.MECH_DARK
ERAS = ["2004–2019", "2020–2023", "2024", "2025", "2026"]
# one-hue ordinal ramp for reach L0-L4 (dim -> bright gold on dark; light -> deep umber on light)
REACH = (["#d9cfb8", "#c4ab78", "#a98547", "#865f22", "#5a3b0c"] if LIGHT
         else ["#4a4234", "#7a6640", "#b08f4f", "#e0b866", "#ffe3a3"])
TILT = math.radians(10)
RMIN, RMAX = 9.0, 46.0


def project(P):
    az, el = math.radians(CAM["az"]), math.radians(CAM["el"])
    x, y, z = P[..., 0], P[..., 1], P[..., 2]
    x1, y1 = x * math.cos(az) + y * math.sin(az), -x * math.sin(az) + y * math.cos(az)
    y2, z2 = y1 * math.cos(el) - z * math.sin(el), y1 * math.sin(el) + z * math.cos(el)
    s = CAM["D"] / (CAM["D"] + y2)
    return CAM["u0"] + CAM["sc"] * s * x1, CAM["v0"] + CAM["sc"] * s * z2, y2


def ring_pts(k, r, ang_deg):
    """3D points on ring k at radius r (mm) and angles (deg); ring plane tilted by TILT about Z."""
    a = np.radians(np.atleast_1d(ang_deg))
    cx = CENTRES[k]
    yv = np.array([-math.sin(TILT), math.cos(TILT), 0.0])
    zv = np.array([0.0, 0.0, 1.0])
    return np.array([cx, 0.0, 0.0]) + r[..., None] * (np.cos(a)[:, None] * yv + np.sin(a)[:, None] * zv) \
        if np.ndim(r) else np.array([cx, 0, 0]) + r * (np.cos(a)[:, None] * yv + np.sin(a)[:, None] * zv)


def main():
    global CENTRES
    cards = S.papercards(); px = X.load()
    asg, span_t, span_s, span_f, anchor, by_t = layout(cards)
    era_of = {c["paper_id"]: c for c in cards}
    n_era = C.Counter(era_of[p]["era"] for p, _, _, _ in asg)
    radius = {e: RMIN + (RMAX - RMIN) * math.sqrt(n_era[e] / max(n_era.values())) for e in ERAS}
    CENTRES = [-CAM["dx"] * (len(ERAS) - 1) + CAM["dx"] * k for k in range(len(ERAS))]   # 2026 nearest
    sec_of = {(p, f): s for p, f, s, _ in asg}
    mid = lambda sp: (sp[0] + sp[1]) / 2

    W, H = CAM["W"], CAM["H"]
    # auto-fit: project every ring (plus label margin) with unit transform, then fit the box
    CAM.update(u0=0.0, v0=0.0, sc=1.0)
    raw = np.vstack([np.c_[project(ring_pts(k, radius[e] * 1.10 + 9, np.linspace(0, 360, 90)))[:2]]
                     for k, e in enumerate(ERAS)])
    bx0, bx1, by0, by1 = 10.0, W - 10.0, 30.0, H - 22.0
    sc = min((bx1 - bx0) / np.ptp(raw[:, 0]), (by1 - by0) / np.ptp(raw[:, 1]))
    CAM.update(sc=sc, u0=bx0 - sc * raw[:, 0].min() + ((bx1 - bx0) - sc * np.ptp(raw[:, 0])) / 2,
               v0=by0 - sc * raw[:, 1].min() + ((by1 - by0) - sc * np.ptp(raw[:, 1])) / 2)
    fig = plt.figure(figsize=(W / 25.4, H / 25.4), facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

    def proj_ring(k, r, angs):
        u, v, d = project(ring_pts(k, r, angs))
        return np.c_[u, v], d

    # ---- curtains between consecutive rings (field arcs extruded), drawn first --------------------
    for k in range(len(ERAS) - 1):
        r0, r1 = radius[ERAS[k]] * 1.07, radius[ERAS[k + 1]] * 1.07
        polys, strands = [], []
        for f, (a0, a1) in span_f.items():
            angs = np.linspace(a0, a1, 24)
            p0, _ = proj_ring(k, r0, angs); p1, _ = proj_ring(k + 1, r1, angs)
            polys.append(np.r_[p0, p1[::-1]])
            for t, (t0, t1) in span_t.items():
                if t.startswith(f):
                    q0, _ = proj_ring(k, r0, [t0]); q1, _ = proj_ring(k + 1, r1, [t0])
                    strands.append([q0[0], q1[0]])
        ax.add_collection(PolyCollection(polys, facecolors=STRAND, edgecolors="none",
                                         alpha=0.05 if LIGHT else 0.045, zorder=1 + k * 0.01))
        ax.add_collection(LineCollection(strands, colors=STRAND, linewidths=0.18,
                                         alpha=0.30 if LIGHT else 0.28, zorder=1.05 + k * 0.01))

    # ---- rings, far (old) to near (new) -------------------------------------------------------------
    for k, e in enumerate(ERAS):
        R = radius[e]
        cue = 0.55 + 0.45 * k / (len(ERAS) - 1)              # depth cue: far rings dimmer
        z0 = 2 + k
        # field band
        polys = []
        for f, (a0, a1) in span_f.items():
            angs = np.linspace(a0, a1, 40)
            po, _ = proj_ring(k, R * 1.10, angs); pi, _ = proj_ring(k, R * 1.04, angs)
            polys.append(np.r_[po, pi[::-1]])
        ax.add_collection(PolyCollection(polys, facecolors=TXT, edgecolors="none", alpha=0.9 * cue, zorder=z0))
        # reach tracks L0..L4 (faint guides)
        trk = lambda L: R * (0.80 + 0.06 * L)          # autonomy tracks L0 (inner) .. L3 (rim)
        for L in range(4):
            pts, _ = proj_ring(k, trk(L), np.linspace(0, 360, 240))
            ax.plot(pts[:, 0], pts[:, 1], color=DIM, lw=0.2, alpha=0.35 * cue, zorder=z0 + 0.05)
        # this era's papers: dots on tracks + bundled curves for cross-field pairs
        papers = [c for c in cards if c["era"] == e]
        segs = C.defaultdict(list)
        dots = C.defaultdict(list)
        key = (lambda c: px[c["paper_id"]][1] or 0) if BY_REACH else (lambda c: c["mechanism"])
        for c in papers:
            L = px[c["paper_id"]][1] or 0
            for f in c["fields"]:
                a, _ = anchor[(c["paper_id"], f)]
                p, _ = proj_ring(k, trk(L), [a]); dots[key(c)].append(p[0])
            fs = c["fields"]
            for i in range(len(fs)):
                for j in range(i + 1, len(fs)):
                    u, v = (c["paper_id"], fs[i]), (c["paper_id"], fs[j])
                    Lu = trk(px[c["paper_id"]][1] or 0)
                    ctrl2 = [(anchor[u][0], Lu), (mid(span_s[sec_of[u]]), R * 0.6), (mid(span_f[fs[i]]), R * 0.3),
                             (None, 0), (mid(span_f[fs[j]]), R * 0.3), (mid(span_s[sec_of[v]]), R * 0.6),
                             (anchor[v][0], Lu)]
                    xy = [(r * math.cos(math.radians(a)), r * math.sin(math.radians(a))) if a is not None else (0, 0)
                          for a, r in ctrl2]
                    cur = spline(xy, n=48)
                    rr = np.hypot(cur[:, 0], cur[:, 1]); aa = np.degrees(np.arctan2(cur[:, 1], cur[:, 0]))
                    P3 = np.array([CENTRES[k], 0, 0]) + rr[:, None] * (
                        np.cos(np.radians(aa))[:, None] * np.array([-math.sin(TILT), math.cos(TILT), 0])
                        + np.sin(np.radians(aa))[:, None] * np.array([0, 0, 1.0]))
                    uu, vv, _ = project(P3)
                    segs[key(c)].append(np.c_[uu, vv])
        keys = [0, 1, 2, 3, 4] if BY_REACH else ["llm", "optimization", "hybrid", "classical"]
        col = (lambda q: REACH[q]) if BY_REACH else (lambda q: MECH[q])
        for q in keys:
            if segs[q]:
                a_ = (0.35 + 0.13 * q) if BY_REACH else (0.45 if q == "llm" else 0.85)
                ax.add_collection(LineCollection(segs[q], colors=col(q), linewidths=0.28, alpha=a_ * cue,
                                                 zorder=z0 + 0.1 + (0.01 * q if BY_REACH else 0)))
        for q in keys:
            if dots[q]:
                d = np.array(dots[q])
                ax.scatter(d[:, 0], d[:, 1], s=(0.55 * S.PT) ** 2, c=col(q), lw=0, alpha=0.95 * cue, zorder=z0 + 0.2)
        if k == len(ERAS) - 1:   # name the reach tracks once, on the nearest ring
            for L in range(4):
                p, _ = proj_ring(k, trk(L), [-38 if VIEW == "mouth" else -84])
                ax.text(p[0, 0], p[0, 1], f"L{L}", fontsize=4.6, color=TXT, ha="center", va="center", zorder=22,
                        fontweight="bold", bbox=dict(boxstyle="round,pad=0.1", fc=BG, ec="none", alpha=0.75))
        # era label above the ring
        if VIEW == "mouth":      # nested rings: leader from the ring's left rim to a label column
            lp, _ = proj_ring(k, R * 1.10, [196 - 4 * k])
            ha, va = "right", "center"; lx, ly = 30.0, H - 46 - k * 11
            ax.plot([lx + 1.0, lp[0, 0]], [ly, lp[0, 1]], color=DIM, lw=0.35, alpha=cue, zorder=19)
            ax.scatter([lp[0, 0]], [lp[0, 1]], s=(0.9 * S.PT) ** 2, c=TXT, lw=0, zorder=19)
        else:                    # tunnel / flare: label under the ring, clear of the field names
            lp, _ = proj_ring(k, R * 1.10 + (11 if k == len(ERAS) - 1 else 4.5), [270])
            ha, va = "center", "top"; lx, ly = lp[0, 0], lp[0, 1]
        ax.text(lx, ly, e, fontsize=7.5 if k == len(ERAS) - 1 else 6.5, color=TXT, ha=ha,
                va=va, fontweight="bold", alpha=cue, zorder=20,
                bbox=dict(boxstyle="round,pad=0.15", fc=BG, ec="none", alpha=0.6))
        ax.text(lx, ly - (3.2 if va == "top" else 2.6), f"{len(papers)} papers", fontsize=5.0, color=DIM, ha=ha,
                va="top", alpha=cue, zorder=20)
    # field names around the nearest ring
    kN, RN = len(ERAS) - 1, radius[ERAS[-1]]
    for f, (a0, a1) in span_f.items():
        p, _ = proj_ring(kN, RN * 1.10 + 4.2, [mid((a0, a1))])
        ha = "left" if p[0, 0] > project(np.array([[CENTRES[kN], 0, 0]]))[0][0] + 2 else "right"
        ax.text(p[0, 0], p[0, 1], S.FSHORT[f], fontsize=5.6, color=TXT, ha=ha, va="center", zorder=21)

    # ---- title + legend (same blocks in every view) ----------------------------------------------------
    ax.text(8, H - 8, "CROSS-DOMAIN STRUCTURE THROUGH TIME", fontsize=6, color=DIM, fontweight="bold", va="top")
    ax.text(8, H - 12.5, "The cross-domain wormhole", fontsize=14, color=TXT, fontweight="bold", va="top")
    x0, y = 8, 22
    if BY_REACH:
        ax.text(x0, y, "CURVE  ·  SYSTEM AUTONOMY", fontsize=5.2, color=DIM, fontweight="bold")
        items = [(REACH[L + 1], f"L{L} " + ["tool", "task assistant", "closed-loop", "autonomous"][L])
                 for L in range(4)]
    else:
        ax.text(x0, y, "CURVE  ·  DECISION MECHANISM", fontsize=5.2, color=DIM, fontweight="bold")
        items = [(MECH[m], lab) for m, lab in [("llm", "LLM-driven"), ("optimization", "Optimization"),
                                                ("hybrid", "Hybrid"), ("classical", "Symbolic / planning")]]
    xx = x0
    for cc, lab in items:
        ax.plot([xx, xx + 4], [y - 3.6, y - 3.6], color=cc, lw=1.2, solid_capstyle="round")
        ax.text(xx + 5.2, y - 3.6, lab, fontsize=5.6, color=TXT, va="center")
        xx += 9 + len(lab) * 1.05
    y -= 9.5
    ax.text(x0, y, "RINGS  ·  ONE PER ERA, RADIUS ∝ √ PAPER–FIELD ASSIGNMENTS", fontsize=5.2, color=DIM, fontweight="bold")
    ax.text(x0, y - 3.6, "dots sit on autonomy tracks: L0 tool (innermost) → L1 task assistant → L2 closed-loop executor → "
            "L3 autonomous researcher (rim)   ·   curtains carry each field from era to era",
            fontsize=5.4, color=TXT, va="center")
    ax.text(W - 8, 6, "662 core papers · 422 cross-field pairs · snapshot 1 Nov 2026", fontsize=5.2, color=DIM,
            ha="right")
    name = f"fig_wormhole_{VIEW}" + ("_reach" if BY_REACH else "")
    S.save(fig, name)
    print(name)


if __name__ == "__main__":
    main()
