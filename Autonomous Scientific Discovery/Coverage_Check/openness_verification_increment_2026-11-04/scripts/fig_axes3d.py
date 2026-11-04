"""Proposal main figure in 3D: problem openness (O), verification strength (V), system autonomy (L),
from the coded increment (ov_coding/increment/classification_results_662.jsonl). Light background only.

  fig_axes3d_curtains : one translucent wall per autonomy level; on each, the share of that level's papers
                        verified at V or stronger (V0..V4). The V3 point is the strong-verification share.
  fig_axes3d_cube     : x = openness O1-O6, y = verification V0-V4, z = autonomy L0-L3; every (O, V, L) cell
                        as a bubble with its paper count; colour = V level, warm for strong (V3-V4).
  fig_axes3d_cube_fNN : the same cube for each field 01-11 (a cross-field paper counts in every field it has).
  fig_axes3d_cube_fields : all papers plus the 11 fields as small multiples on one shared bubble scale.
  derived/ovl_cube_counts.csv : every (O, V, L) count, for all papers and for each field (zeros included).
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


FZH = {"01": "形式与计算科学", "02": "物理与天文", "03": "化学", "04": "材料", "05": "地球与环境", "06": "生命科学",
       "07": "医学与健康", "08": "农业与食品", "09": "工程与工业", "10": "航空航天、海洋与交通", "11": "社会与知识系统"}
O_TICK = ["O1\n规则世界", "O2\n既定基准", "O3\n新实例", "O4\n需物理检验", "O5\n开放数学", "O6\n开放科学"]
V_TICK = ["V0 声明", "V1 基准", "V2 计算/仿真", "V3 物理实验", "V4 证明/复现"]
L_TICK = ["L0 工具", "L1 任务助手", "L2 闭环执行者", "L3 自主研究者"]
V_COL = ["#c3ced5", "#93afc0", "#4f7f9a", "#d0644a", "#8c2a1c"]   # V0-V2 cool, V3-V4 (strong) warm


def ovl(r):
    return int(r["openness"][1]), int(r["verification"][1]), int(r["autonomy"][1])


def cube_axes(ax, rows, mx, small=False):
    """Draw every (O, V, L) cell of rows as a bubble on ax: x = openness O1-O6, y = verification V0-V4,
    z = autonomy L0-L3; area proportional to papers (largest cell = mx), count printed on each bubble."""
    cnt = C.Counter(ovl(r) for r in rows)
    fs = 5.2 if small else 7.5
    z0 = -0.45
    for (o, v, L), n in sorted(cnt.items(), key=lambda t: -t[1]):
        strong = v >= 3
        col = V_COL[v]
        ax.plot([o, o], [v, v], [z0, L], color=col, lw=0.4, alpha=0.35, zorder=1)
        ax.scatter([o], [v], [z0], s=6 if small else 10, c=col, alpha=0.35, edgecolors="none", depthshade=False)
        ax.scatter([o], [v], [L], s=(6 if small else 14) + (380 if small else 1500) * n / mx, c=col,
                   alpha=0.8 if strong else 0.55, edgecolors="white", linewidths=0.6, depthshade=False, zorder=3)
        if n >= 0.1 * mx:
            ax.text(o, v, L, str(n), fontsize=fs, color="white", ha="center", va="center", fontweight="bold", zorder=5)
        else:
            ax.text(o + 0.16, v, L, str(n), fontsize=fs * 0.9, color=INK, ha="left", va="center", zorder=5)
    nO = C.Counter(ovl(r)[0] for r in rows); nV = C.Counter(ovl(r)[1] for r in rows)
    nL = C.Counter(ovl(r)[2] for r in rows)
    tk = 5.0 if small else 7.2
    if small:
        ax.set_xticks(range(1, 7), [f"O{k}" for k in range(1, 7)], fontsize=tk)
        ax.set_yticks(range(5), [f"V{k}" for k in range(5)], fontsize=tk)
        ax.set_zticks(range(4), [f"L{k}" for k in range(4)], fontsize=tk)
    else:
        ax.set_xticks(range(1, 7), [f"{t}\n({nO[k + 1]})" for k, t in enumerate(O_TICK)], fontsize=tk)
        ax.set_yticks(range(5), [f"{t} ({nV[k]})" for k, t in enumerate(V_TICK)], fontsize=tk)
        ax.set_zticks(range(4), [f"{t} ({nL[k]})" for k, t in enumerate(L_TICK)], fontsize=tk)
    ax.set_xlim(0.5, 6.5); ax.set_ylim(-0.5, 4.5); ax.set_zlim(z0, 3.4)
    ax.tick_params(pad=0 if small else 2)
    for a in (ax.xaxis, ax.yaxis, ax.zaxis):
        a.pane.set_facecolor((0.97, 0.965, 0.955, 1)); a.pane.set_edgecolor("#ddd8cf")
        a._axinfo["grid"].update(color="#e2ddd3", linewidth=0.5)
    ax.set_box_aspect((1.35, 1.15, 1.0))
    ax.view_init(elev=20, azim=-60)


def cube(rows, name, title, sub):
    fig = plt.figure(figsize=(9.6, 8.2), facecolor="white")
    ax = fig.add_axes([0.02, 0.06, 0.96, 0.82], projection="3d", computed_zorder=False)
    mx = max(C.Counter(ovl(r) for r in rows).values())
    cube_axes(ax, rows, mx)
    ax.set_xlabel("问题开放度 O", labelpad=22); ax.set_ylabel("验证强度 V", labelpad=26)
    ax.set_zlabel("系统自主性 L", labelpad=26)
    n_strong = sum(ovl(r)[1] >= 3 for r in rows)
    fig.text(0.06, 0.955, title, fontsize=15, fontweight="bold", color=INK)
    fig.text(0.06, 0.925, sub + f"　·　{len(rows)} 篇，强验证（V3–V4）{n_strong} 篇（{100 * n_strong / len(rows):.0f}%）",
             fontsize=9, color=MUTED)
    fig.text(0.06, 0.03, "每个气泡 = 一个 (O, V, L) 组合，数字为论文数，面积 ∝ 论文数；颜色 = 验证强度，暖色为强验证（V3–V4）；"
             "刻度括号内为该级合计；竖线指向底面的 O × V 位置 · 快照 2026-11-01", fontsize=7.5, color=MUTED)
    v_legend(fig, (0.985, 0.90), "upper right", 8)
    S.save(fig, name)
    plt.close(fig)


def v_legend(fig, loc, anchor, fs, ncol=1):
    from matplotlib.lines import Line2D
    hs = [Line2D([], [], ls="none", marker="o", ms=7, mfc=c, mec="white", label=t) for c, t in zip(V_COL, V_TICK)]
    fig.legend(handles=hs, loc=anchor, bbox_to_anchor=loc, frameon=False, fontsize=fs, title="验证强度（颜色）",
               title_fontsize=fs, ncol=ncol, handletextpad=0.3, columnspacing=1.0)


def cube_fields(rows, fields):
    """Small multiples: all papers plus one panel per field, bubble area on one shared scale across fields."""
    fig = plt.figure(figsize=(13.2, 10.6), facecolor="white")
    sets = [("全部", rows)] + [(FZH[f], [r for r in rows if f in fields[r["paper_id"]]]) for f in S.FIELDS]
    mx_f = max(max(C.Counter(ovl(r) for r in sub).values()) for _, sub in sets[1:])
    for i, (lab, sub) in enumerate(sets):
        ax = fig.add_subplot(3, 4, i + 1, projection="3d", computed_zorder=False)
        cube_axes(ax, sub, max(C.Counter(ovl(r) for r in sub).values()) if i == 0 else mx_f, small=True)
        ns = sum(ovl(r)[1] >= 3 for r in sub)
        ax.set_title(f"{lab}　n = {len(sub)}　强验证 {100 * ns / len(sub):.0f}%", fontsize=8.5,
                     color=INK, fontweight="bold", pad=-14)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.05, wspace=0.02, hspace=0.08)
    fig.text(0.03, 0.955, "问题开放度 O × 验证强度 V × 系统自主性 L：按学科", fontsize=15, fontweight="bold", color=INK)
    fig.text(0.03, 0.928, "x = O1–O6，y = V0–V4，z = L0–L3；数字为论文数；颜色 = 验证强度，暖色为强验证（V3–V4）。"
             "学科面板气泡面积共用同一比例，可直接比较；跨学科论文在每个所属学科各计一次。", fontsize=9, color=MUTED)
    fig.text(0.03, 0.02, f"{len(rows)} 篇核心论文，{sum(len(s) for _, s in sets[1:])} 个论文—学科归属 · 快照 2026-11-01",
             fontsize=8, color=MUTED)
    v_legend(fig, (0.99, 0.005), "lower right", 7.5, ncol=5)
    S.save(fig, "fig_axes3d_cube_fields")
    plt.close(fig)


def cubes(rows):
    fields = {c["paper_id"]: set(c["fields"]) for c in S.papercards()}
    cube(rows, "fig_axes3d_cube", "问题开放度 × 验证强度 × 系统自主性", "全部核心论文")
    for f in S.FIELDS:
        sub = [r for r in rows if f in fields[r["paper_id"]]]
        cube(sub, f"fig_axes3d_cube_f{f}", f"{FZH[f]}：开放度 × 验证强度 × 自主性", f"学科 {f} {FZH[f]}")
    cube_fields(rows, fields)
    import csv
    with open(S.DER / "ovl_cube_counts.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["scope", "field_code", "field_name", "openness", "verification", "autonomy", "papers"])
        scopes = [("all", "", "全部", rows)] + [("field", f, FZH[f], [r for r in rows if f in fields[r["paper_id"]]])
                                                for f in S.FIELDS]
        for sc, code, nm, sub in scopes:
            cnt = C.Counter(ovl(r) for r in sub)
            for o in range(1, 7):
                for v in range(5):
                    for L in range(4):
                        w.writerow([sc, code, nm, f"O{o}", f"V{v}", f"L{L}", cnt.get((o, v, L), 0)])


if __name__ == "__main__":
    rows = load()
    print("strong share by L:", curtains(rows))
    cubes(rows)
