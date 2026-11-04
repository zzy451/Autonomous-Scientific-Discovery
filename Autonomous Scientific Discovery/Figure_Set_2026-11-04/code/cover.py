"""Shared canvas, glow marks, title and the ONE legend system used by every cover image.

Encoding is identical across the series:
  colour     = decision mechanism (validated palette, dark or light step)
  brightness = evidence endpoint E3 > E2 > E1 > E0 (size + opacity + glow)
Each script may add at most one figure-specific legend row (e.g. rings = era)."""
import sys, math
import numpy as np
import matplotlib.pyplot as plt
import style as S

LIGHT = True                       # one version only: white background
W = H = 200.0
BG = "#fbfaf7" if LIGHT else "#07090d"
TXT = "#1d1d1b" if LIGHT else "#ebe8e1"
DIM = "#77736b" if LIGHT else "#8e8a82"
FAINT = "#d9d4ca" if LIGHT else "#262a31"
MECH = S.MECH if LIGHT else S.MECH_DARK
NEUTRAL = "#3a3833" if LIGHT else "#f3efe6"
MECH_SHORT = {"llm": "LLM-driven", "optimization": "Optimization", "hybrid": "Hybrid",
              "classical": "Symbolic / planning"}
# evidence tier -> (core diameter mm, opacity, glow strength)
TIER = {3: (1.30, 1.00, 1.0), 2: (0.95, 0.80, 0.35), 1: (0.72, 0.55, 0.0), 0: (0.58, 0.38, 0.0)}
TIER_SHORT = {3: "Strong (V3–V4)", 2: "Computational (V2)", 1: "Benchmark (V1)", 0: "Claim (V0)"}


def canvas():
    fig = plt.figure(figsize=(W / 25.4, H / 25.4), facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    ax.set_facecolor(BG)
    return fig, ax


def marks(ax, xs, ys, colors, tiers, scale=1.0, z=5):
    """Glow points: per tier, a wide faint halo, a mid halo, then the core."""
    xs, ys, tiers = np.asarray(xs), np.asarray(ys), np.asarray(tiers)
    colors = np.asarray(colors, dtype=object)
    for t in (0, 1, 2, 3):
        m = tiers == t
        if not m.any():
            continue
        d, a, g = TIER[t]
        d *= scale
        if g and not LIGHT:
            ax.scatter(xs[m], ys[m], s=(d * 4.2 * S.PT) ** 2, c=list(colors[m]), alpha=0.05 * g, lw=0, zorder=z)
            ax.scatter(xs[m], ys[m], s=(d * 2.2 * S.PT) ** 2, c=list(colors[m]), alpha=0.16 * g, lw=0, zorder=z + 0.1)
        ax.scatter(xs[m], ys[m], s=(d * S.PT) ** 2, c=list(colors[m]), alpha=a, lw=0, zorder=z + 0.2 + t * 0.01)
        if t == 3:   # bright centre for the strongest endpoint
            ax.scatter(xs[m], ys[m], s=(d * 0.42 * S.PT) ** 2, c=BG if LIGHT else "#ffffff", alpha=0.75 if not LIGHT else 0.0,
                       lw=0, zorder=z + 0.3)


def title(ax, kicker, text):
    ax.text(10, H - 10, kicker.upper(), fontsize=6.2, color=DIM, fontweight="bold", va="top")
    ax.text(10, H - 14.5, text, fontsize=15, color=TXT, fontweight="bold", va="top")


def footer(ax, note="662 core papers · snapshot 1 Nov 2026"):
    ax.text(W - 10, 8, note, fontsize=5.6, color=DIM, ha="right", va="bottom")


def legend(ax, extra=None, mech=True, tiers=True):
    """Bottom-left block; identical position, order and type in every image."""
    x0, y = 10.0, 26.0
    if extra:
        y += 6.0
    if mech:
        ax.text(x0, y, "COLOUR  ·  DECISION MECHANISM", fontsize=5.4, color=DIM, fontweight="bold", va="center")
        x = x0
        for m in ("llm", "optimization", "hybrid", "classical"):
            ax.scatter([x + 1.2], [y - 4.2], s=(1.8 * S.PT) ** 2, c=MECH[m], lw=0)
            ax.text(x + 3.2, y - 4.2, MECH_SHORT[m], fontsize=6.0, color=TXT, va="center")
            x += 5.5 + len(MECH_SHORT[m]) * 1.12
        y -= 10.0
    if tiers:
        ax.text(x0, y, "BRIGHTNESS  ·  EVIDENCE ENDPOINT", fontsize=5.4, color=DIM, fontweight="bold", va="center")
        x = x0
        for t in (3, 2, 1, 0):
            marks(ax, [x + 1.2], [y - 4.2], [NEUTRAL], [t], scale=1.25, z=20)
            ax.text(x + 3.2, y - 4.2, TIER_SHORT[t], fontsize=6.0, color=TXT, va="center")
            x += 5.5 + len(TIER_SHORT[t]) * 1.12
        y -= 10.0
    if extra:
        head, items = extra
        ax.text(x0, y, head.upper(), fontsize=5.4, color=DIM, fontweight="bold", va="center")
        x = x0
        for draw, lab in items:
            draw(ax, x + 1.2, y - 4.2)
            ax.text(x + 3.6, y - 4.2, lab, fontsize=6.0, color=TXT, va="center")
            x += 6.0 + len(lab) * 1.12


def polar(cx, cy, a_deg, r):
    a = math.radians(a_deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def halton(i, b):
    f, r = 1.0, 0.0
    while i > 0:
        f /= b; r += f * (i % b); i //= b
    return r


def save(fig, name):
    S.save(fig, name)


def curved(ax, text, cx, cy, amid, r, size, color, weight="bold", track=0.25):
    """Text along an arc centred on angle amid (deg); flipped on the lower half."""
    from matplotlib.textpath import TextToPath
    from matplotlib.font_manager import FontProperties
    ttp, fp = TextToPath(), FontProperties(family="Arial", size=size, weight=weight)
    adv = lambda s: ttp.get_text_width_height_descent(s, fp, ismath=False)[0] / S.PT
    lower = math.sin(math.radians(amid)) < -0.05
    total = adv(text) + track * (len(text) - 1)
    sign = 1 if lower else -1
    a0 = amid - sign * math.degrees(total / r) / 2
    for i, ch in enumerate(text):
        x0 = (adv(text[:i]) + track * i) if i else 0.0
        ac = a0 + sign * math.degrees((x0 + adv(ch) / 2) / r)
        x, y = polar(cx, cy, ac, r)
        ax.text(x, y, ch, fontsize=size, color=color, ha="center", va="center", fontweight=weight,
                rotation=ac + 90 if lower else ac - 90, rotation_mode="anchor", zorder=30)


def sectors(weights, gap=1.6, start=90.0):
    """Clockwise angular spans proportional to weights: {key: (a_start, a_end)}."""
    tot = sum(weights.values())
    per = (360 - gap * len(weights)) / tot
    out, a = {}, start
    for k, w in weights.items():
        out[k] = (a, a - w * per)
        a -= w * per + gap
    return out

CX, CY, RMAX = 104.0, 108.0, 59.0    # shared circle geometry: clear of title (top) and legend (bottom)
