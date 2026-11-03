"""Proposal main figure in 3D: problem openness (O), verification strength (V), system autonomy (L),
from the coded increment (ov_coding/increment/classification_results_662.jsonl). Light background only.

  fig_axes3d_curtains : one translucent wall per autonomy level; on each, the share of that level's papers
                        verified at V or stronger (V0..V4). The V3 point is the strong-verification share.
  fig_axes3d_lattice  : every (O, V, L) cell as a bubble, area proportional to papers; strong (V3-V4) cells
                        in the accent colour.
Usage: python3 fig_axes3d.py
"""
import json, collections as C
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import style as S

INC = S.ROOT / "ov_coding" / "increment" / "classification_results_662.jsonl"
V_NAME = ["V0 声明", "V1 基准", "V2 计算/仿真", "V3 物理实验", "V4 证明/复现"]
O_NAME = ["O1 规则世界", "O2 既定基准", "O3 新实例", "O4 需物理检验", "O5 开放数学", "O6 开放科学"]
L_NAME = {1: "L1 任务助手", 2: "L2 闭环执行者", 3: "L3 自主研究者"}
L_COL = {1: "#5b8fa8", 2: "#d9a26b", 3: "#c4553f"}        # sequential teal -> sand -> coral, as the reference
INK, MUTED, ACC = "#1d1d1b", "#6b665c", "#b2412f"
plt.rcParams.update({"font.family": ["Arial Unicode MS", "Arial"], "font.size": 9})


def load():
    rows = [json.loads(l) for l in open(INC, encoding="utf-8")]
    return [r for r in rows if r["coded"]]


def curtains(rows):
    n_L = C.Counter(int(r["autonomy"][1]) for r in rows)
    fig = plt.figure(figsize=(9.2, 7.4), facecolor="white")
    ax = fig.add_subplot(projection="3d", computed_zorder=False)
    xs = np.arange(5)
    for L in (1, 2, 3):
        sub = [r for r in rows if int(r["autonomy"][1]) == L]
        n = len(sub)
        if not n:
            continue
        surv = [100 * sum(int(r["verification"][1]) >= v for r in sub) / n for v in xs]
        y = np.full(5, L)
        verts = [list(zip(xs, y, surv)) + [(4, L, 0), (0, L, 0)]]
        ax.add_collection3d(Poly3DCollection(verts, facecolor=L_COL[L], alpha=0.30, edgecolor=L_COL[L], lw=0.8))
        ax.plot(xs, y, surv, color=L_COL[L], lw=2.2, marker="o", ms=4.5, mec="white", mew=0.8, zorder=5)
        for x, z in zip(xs, surv):
            if x in (1, 2, 3):
                lab = f"{z:.0f}%" if x != 3 else f"★ {z:.0f}%"
                ax.text(x + 0.12, L, z + 5, lab, fontsize=8.5 if x == 3 else 7.5, color=ACC if x == 3 else INK,
                        ha="center", fontweight="bold" if x == 3 else "normal", zorder=6)
        ax.text(0, L, max(surv) + 9, f"{L_NAME[L]} · n = {n}", fontsize=8, color=L_COL[L], fontweight="bold", ha="left")
    # dashed guide joining the strong-verification points across walls
    sv = [(3, L, 100 * sum(int(r["verification"][1]) >= 3 for r in rows if int(r["autonomy"][1]) == L) / n_L[L])
          for L in (1, 2, 3) if n_L[L]]
    ax.plot([p[0] for p in sv], [p[1] for p in sv], [p[2] for p in sv], color=ACC, lw=1.0, ls="--", zorder=7)
    ax.set_xticks(xs, V_NAME, fontsize=8)
    ax.set_yticks([1, 2, 3], ["L1", "L2", "L3"], fontsize=8)
    ax.set_zlim(0, 115)
    ax.set_xlabel("验证强度 V", labelpad=14); ax.set_ylabel("系统自主性 L", labelpad=16)
    ax.set_zlabel("达到该验证强度及以上的论文占比（%）", labelpad=8)
    ax.view_init(elev=22, azim=-58)
    for a in (ax.xaxis, ax.yaxis, ax.zaxis):
        a.pane.set_facecolor((0.97, 0.965, 0.955, 1)); a.pane.set_edgecolor("#ddd8cf")
    ax.set_box_aspect((1.5, 1.0, 0.9))
    fig.text(0.06, 0.95, "自主性 × 验证强度", fontsize=15, fontweight="bold", color=INK)
    fig.text(0.06, 0.915, "★ = 物理实验、形式化证明或第三方复现（V3–V4，提案定义的强验证）", fontsize=9, color=MUTED)
    fig.text(0.06, 0.03, f"{len(rows)} 篇核心论文 · 编码依据 RUBRIC.md（以提案为准）· 快照 2026-11-01", fontsize=8, color=MUTED)
    S.save(fig, "fig_axes3d_curtains")
    return {L: round(z, 1) for _, L, z in sv}


def lattice(rows):
    cnt = C.Counter((int(r["verification"][1]), int(r["autonomy"][1]), int(r["openness"][1])) for r in rows)
    fig = plt.figure(figsize=(9.2, 7.6), facecolor="white")
    ax = fig.add_subplot(projection="3d")
    mx = max(cnt.values())
    for (v, L, o), n in cnt.items():
        strong = v >= 3
        ax.scatter([v], [L], [o], s=18 + 900 * n / mx, c=ACC if strong else "#8fa7b3", alpha=0.75 if strong else 0.45,
                   edgecolors="white", linewidths=0.6, depthshade=False)
        if n >= 12:
            ax.text(v, L, o + 0.28, str(n), fontsize=7, color=INK, ha="center")
    ax.set_xticks(range(5), V_NAME, fontsize=7.5)
    ax.set_yticks([1, 2, 3], [L_NAME[k] for k in (1, 2, 3)], fontsize=7.5)
    ax.set_zticks(range(1, 7), O_NAME, fontsize=7.5)
    ax.set_xlim(-0.4, 4.4); ax.set_ylim(0.6, 3.4); ax.set_zlim(0.6, 6.5)
    ax.set_xlabel("验证强度 V", labelpad=14); ax.set_ylabel("系统自主性 L", labelpad=14); ax.set_zlabel("问题开放度 O", labelpad=18)
    ax.view_init(elev=20, azim=-52)
    for a in (ax.xaxis, ax.yaxis, ax.zaxis):
        a.pane.set_facecolor((0.97, 0.965, 0.955, 1)); a.pane.set_edgecolor("#ddd8cf")
    fig.text(0.06, 0.95, "问题开放度 × 验证强度 × 系统自主性", fontsize=15, fontweight="bold", color=INK)
    fig.text(0.06, 0.915, "气泡面积 ∝ 论文数；红色 = 强验证（V3–V4）", fontsize=9, color=MUTED)
    fig.text(0.06, 0.03, f"{len(rows)} 篇核心论文 · 快照 2026-11-01", fontsize=8, color=MUTED)
    S.save(fig, "fig_axes3d_lattice")


if __name__ == "__main__":
    rows = load()
    print("strong share by L:", curtains(rows))
    lattice(rows)
