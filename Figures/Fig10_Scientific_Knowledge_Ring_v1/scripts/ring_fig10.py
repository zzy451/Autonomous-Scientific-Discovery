"""Fig. 10 ring: field composition (outer skyline) and cross-field links (inner chords), Nature double column.

Encodings
  sector        one per top-level field, all equal width (arc length carries no data)
  outer bars    one bar per third-level theme with records; length = records (shared linear scale);
                largest theme in the middle of the sector, then alternating outward (a rank 'mountain')
  chords        records assigned to both fields (any co-membership); width = records; < 5 records in grey
  inset         the five largest exact three-field combinations
Inputs are read from the Fig10 v37 package in this repository (or the folder given as the second argument):
  inputs/fields.csv, inputs/themes.csv, data/field_memberships.csv, data/tertiary_memberships.csv, data/tertiary_vocabulary.csv
Usage: python ring_fig10.py out_prefix [v37_folder]        -> out_prefix.pdf / .svg / .png
"""
import csv, sys, json, math, random, itertools, collections, textwrap
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Wedge, Rectangle
from matplotlib.collections import LineCollection
import matplotlib.patheffects as pe

for f in ("/usr/share/fonts/arial/Arial.ttf", "/usr/share/fonts/arial/Arial Bold.ttf"):   # optional explicit Arial files
    if Path(f).exists():
        font_manager.fontManager.addfont(f)
plt.rcParams.update({"font.family": "Arial", "font.size": 6, "pdf.fonttype": 42, "svg.fonttype": "none"})
INK, MUTE = "#1A1A1A", "#5F6B77"

out = sys.argv[1]
SRC = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parents[2] / "Fig10_Scientific_Knowledge_Archipelago_v37"
rows = lambda p: list(csv.DictReader(open(SRC / p, encoding="utf-8-sig")))
FLD = {r["field_code"]: r for r in rows("inputs/fields.csv")}
codes = sorted(FLD)
mem = collections.defaultdict(set)
for r in rows("data/field_memberships.csv"):
    mem[r["paper_id"]].add(r["field_code"])
nrec = {c: sum(c in s for s in mem.values()) for c in codes}
tmem = collections.defaultdict(set)
for r in rows("data/tertiary_memberships.csv"):
    tmem[r["paper_id"]].add(r["tertiary_code"])
tcount = collections.Counter(t for ts in tmem.values() for t in ts)
voc = {r["tertiary_code"]: r for r in rows("data/tertiary_vocabulary.csv")}
themes_en = {r["tertiary_code"]: r["name_en"] for r in rows("inputs/themes.csv")}
pair = collections.Counter(p for s in mem.values() for p in itertools.combinations(sorted(s), 2))
tri = collections.Counter(tuple(sorted(s)) for s in mem.values() if len(s) == 3)
SHORT = {"01": "Formal", "02": "Physics", "03": "Chemistry", "04": "Materials", "05": "Earth", "06": "Life",
         "07": "Medicine", "08": "Agriculture", "09": "Engineering", "10": "Aerospace", "11": "Society"}

# field order: consensus ring, then local search that shortens heavily weighted chords
start = ["01", "02", "10", "09", "04", "03", "06", "07", "08", "05", "11"]
def cost(order):
    pos = {c: i for i, c in enumerate(order)}; n = len(order)
    return sum(w * min(abs(pos[a] - pos[b]), n - abs(pos[a] - pos[b])) for (a, b), w in pair.items())
order, bc = start[:], cost(start)
rng = random.Random(7)
for _ in range(4000):
    i, j = sorted(rng.sample(range(1, 11), 2))
    cand = order[:i] + order[i:j + 1][::-1] + order[j + 1:]
    c = cost(cand)
    if c < bc: order, bc = cand, c
N = len(order); SEC = 360 / N; GAP = 3.2
ang = {c: i * SEC for i, c in enumerate(order)}

# geometry in inches; figure 183 mm x 160 mm
W, H = 7.205, 6.60
R_CH, R_B0, R_B1, R_SKY = 1.56, 1.59, 1.67, 1.72
K = 0.62 / max(tcount.values())
R_LAB = R_SKY + 0.62 + 0.08
def xy(th, r):
    t = math.radians(th); return r * math.sin(t), r * math.cos(t)
mang = lambda th: 90 - th
def hexrgb(h):
    h = h.lstrip("#"); return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)]) / 255
def shade(rgb, f):
    return rgb * (1 + f) if f < 0 else rgb + (1 - rgb) * f

fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(-W / 2, W / 2); ax.set_ylim(-H / 2, H / 2); ax.set_aspect("equal"); ax.axis("off")

# ── outer skyline and field band
for c in order:
    col = hexrgb(FLD[c]["color"])
    a0, a1 = ang[c] - SEC / 2 + GAP / 2, ang[c] + SEC / 2 - GAP / 2
    ax.add_patch(Wedge((0, 0), R_B1, mang(a1), mang(a0), width=R_B1 - R_B0, fc=shade(col, -0.15), ec="none"))
    th = sorted([t for t in tcount if voc.get(t, {}).get("field_code") == c], key=lambda t: (-tcount[t], t))
    dq = collections.deque()
    for k, t in enumerate(th):
        (dq.append if k % 2 else dq.appendleft)(t)
    seq = list(dq); w = (a1 - a0) / len(seq)
    for k, t in enumerate(seq):
        b0, b1 = a0 + k * w + w * 0.08, a0 + (k + 1) * w - w * 0.08
        L = K * tcount[t]
        fcol = shade(col, -0.32) if t in th[:2] else shade(col, -0.05) if t in th[:4] else shade(col, 0.35)
        ax.add_patch(Wedge((0, 0), R_SKY + L, mang(b1), mang(b0), width=L, fc=fcol, ec="none"))
    # label block
    x, y = xy(ang[c], R_LAB)
    ha = "left" if x > 0.25 else "right" if x < -0.25 else "center"
    va = "bottom" if y > 0.6 else "top" if y < -0.6 else "center"
    tl = json.loads(FLD[c]["title_lines"]); title = " ".join(tl) if len(" ".join(tl)) <= 22 else "\n".join(tl)
    def wrapc(name, n, width=25):
        ls = textwrap.wrap(name, width); ls[-1] += f"  {n}"; return "\n".join(ls)
    lab = [f"n = {nrec[c]}"] + [wrapc(themes_en.get(t, t), tcount[t]) for t in th[:2]]
    LH = 0.104; nt = title.count("\n") + 1; hb = (nt + sum(s.count("\n") + 1 for s in lab)) * LH
    yt = y + hb if va == "bottom" else y if va == "top" else y + hb / 2
    ax.text(x, yt, title, ha=ha, va="top", fontweight="bold", fontsize=6.5, color=INK, linespacing=1.2)
    ax.text(x, yt - nt * LH, "\n".join(lab), ha=ha, va="top", color=INK, linespacing=1.25)

# ── chords: endpoints spread inside each sector; gradient between the two field colours
ends = collections.defaultdict(list)
for (a, b), w in pair.items():
    ends[a].append((b, w)); ends[b].append((a, w))
slot = {}
for c in order:
    lst = sorted(ends[c], key=lambda bw: ((ang[bw[0]] - ang[c]) % 360))
    span = SEC - GAP - 6; m = len(lst)
    for k, (o, w) in enumerate(lst):
        slot[(c, o)] = ang[c] + span / 2 - (k + 0.5) * span / m
def bez(p0, p1, n=60):
    c0, c1 = p0 * 0.22, p1 * 0.22; t = np.linspace(0, 1, n)[:, None]
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * c0 + 3 * (1 - t) * t ** 2 * c1 + t ** 3 * p1
lw_of = lambda w: 0.35 + 3.3 * w / max(pair.values())
labels_at = []
TOP = {k for k, _ in sorted(pair.items(), key=lambda kv: -kv[1])[:7]}
for (a, b), w in sorted(pair.items(), key=lambda kv: kv[1]):
    p0, p1 = np.array(xy(slot[(a, b)], R_CH)), np.array(xy(slot[(b, a)], R_CH))
    pts = bez(p0, p1)
    if w < 5:
        ax.plot(pts[:, 0], pts[:, 1], color="#BCC3CA", lw=0.3, alpha=0.8, zorder=2, solid_capstyle="butt")
        continue
    ca, cb = shade(hexrgb(FLD[a]["color"]), -0.30), shade(hexrgb(FLD[b]["color"]), -0.30)
    segs = np.stack([pts[:-1], pts[1:]], axis=1); tt = np.linspace(0, 1, len(segs))[:, None]
    lc = LineCollection(segs, colors=np.hstack([(1 - tt) * ca + tt * cb, np.full((len(segs), 1), 0.88)]),
                        linewidths=lw_of(w), capstyle="round", zorder=3)
    ax.add_collection(lc)
    if (a, b) in TOP:
        for t in (0.5, 0.36, 0.64, 0.26, 0.74):
            pt = bez(p0, p1, 101)[int(t * 100)]
            if all(np.hypot(*(pt - q)) > 0.22 for q in labels_at): break
        labels_at.append(pt)
        ax.text(*pt, str(w), fontweight="bold", fontsize=6.5, ha="center", va="center", zorder=7, color=INK,
                path_effects=[pe.withStroke(linewidth=2.2, foreground="white")])

# ── legend (top-left): bar scale, chord widths
lx, ly = -W / 2 + 0.12, H / 2 - 0.14
ax.text(lx, ly, "Records per theme", fontweight="bold", va="top")
for k, v in enumerate((25, 50, 100)):
    bx = lx + 0.05 + k * 0.32
    base = ly - 0.20 - K * 100
    ax.add_patch(Rectangle((bx, base), 0.05, K * v, fc="#8A99A8", ec="none"))
    ax.text(bx + 0.09, base, str(v), va="bottom", color=INK)
ly2 = -H / 2 + 0.72
ax.text(lx, ly2, "Records shared by two fields", fontweight="bold", va="top")
for k, v in enumerate((5, 25, 100)):
    yy = ly2 - 0.21 - k * 0.13
    ax.plot([lx + 0.02, lx + 0.34], [yy, yy], color="#6F7E8C", lw=lw_of(v), solid_capstyle="butt")
    ax.text(lx + 0.42, yy, str(v), va="center", color=INK)
yy = ly2 - 0.21 - 3 * 0.13
ax.plot([lx + 0.02, lx + 0.34], [yy, yy], color="#BCC3CA", lw=0.3)
ax.text(lx + 0.42, yy, "< 5", va="center", color=INK)

# ── exact three-field combinations (top-right)
x0, ty = W / 2 - 1.80, -H / 2 + 0.88
ax.text(x0, ty, "Records in exactly three fields", fontweight="bold", va="top")
for k, (combo, n) in enumerate(tri.most_common(4)):
    yy = ty - 0.22 - k * 0.13
    for j, c in enumerate(combo):
        ax.add_patch(plt.Circle((x0 + 0.04 + j * 0.085, yy), 0.032, fc=shade(hexrgb(FLD[c]["color"]), -0.25), ec="none"))
    ax.text(x0 + 0.40, yy, str(n), ha="right", va="center", fontweight="bold", color=INK)
    ax.text(x0 + 0.47, yy, " · ".join(SHORT[c] for c in combo), va="center", color=INK)
ax.text(x0, ty - 0.22 - 4 * 0.13, f"4 of {len(tri)} combinations shown", va="center", color=MUTE)

for ext in ("pdf", "svg"):
    fig.savefig(f"{out}.{ext}")
fig.savefig(f"{out}.png", dpi=600)
print("order", [SHORT[c] for c in order], "cost", bc, "top pairs", sorted(pair.items(), key=lambda kv: -kv[1])[:7])
