"""Proposal Fig. 1's frontier for one field, raised into a mountain of evidence.

Fig. 1 marks, per field, the openness levels O1-O6 that have at least one strongly verified case (V >= 3), era by
era. Here one field gets its own mountain on Fig. 1's two axes: x = the proposal's eras (to 1997 ... 2024-2026),
y = openness O1-O6, altitude = papers accumulated by the end of the era. The solid mountain counts strongly
verified papers (V3-V4): its footprint is exactly Fig. 1's land, and an openness level it never reaches is a
located blank. The glass mountain over it counts every claim (V0-V4): the gap is what is claimed but not strongly
verified. The two panels on the right open the latest cross-section along the other two axes: verification
V0-V4 (one profile per threshold) and autonomy L0-L3.
(A first draft put verification on the base with altitude = highest openness reached; in this corpus that
height is set by one to four O6 papers per field and the surface becomes a plateau, so it was dropped.)
Data: ov_coding/increment/classification_results_662.jsonl (year, O, V, L, contested). White background only.
Usage: python3 fig_ovl_frontier_mountain.py [field_code ...]   (default 03)
"""
import sys, json, collections as C
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource, Normalize, to_rgb
from matplotlib.cm import ScalarMappable
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from scipy.interpolate import RegularGridInterpolator
import style as S
from fig_ovl_surface import INC, INK, MUTED, ACC, L_COL, L_NAME, FZH, ALT

ERAS = [(0, 1997), (1998, 2012), (2013, 2019), (2020, 2023), (2024, 2026)]   # proposal Fig. 1
ERA_TICK = ["≤1997", "1998–2012", "2013–2019", "2020–2023", "2024–2026"]
O_TICK = ["O1 规则世界", "O2 既定基准", "O3 新实例", "O4 需物理检验", "O5 开放数学", "O6 开放科学"]
V_COL = ["#1d1d1b", "#6b665c", "#a39d90", ACC, "#7a2418"]                      # V>=0 ... V>=4 profiles
RES = 30
plt.rcParams.update({"font.family": ["Arial Unicode MS", "Arial"], "font.size": 10})


def load(field):
    rows = [json.loads(l) for l in open(INC, encoding="utf-8")]
    out = []
    for r in rows:
        if r["coded"] and field in r["scientific_object_modules"].split(";"):
            y = int(r["year"])
            e = next(k for k, (a, b) in enumerate(ERAS) if a <= y <= b)
            out.append(dict(o=int(r["openness"][1]), v=int(r["verification"][1]), l=int(r["autonomy"][1]),
                            year=y, era=e, contested=bool(r["contested"])))
    return out


def grid(pp, vmin):
    """N[e, o-1]: papers with verification >= vmin published by the end of era e at openness o."""
    N = np.zeros((5, 6))
    for p in pp:
        if p["v"] >= vmin:
            N[p["era"]:, p["o"] - 1] += 1
    return N


def smooth(N):
    f = RegularGridInterpolator((np.arange(5.0), np.arange(1.0, 7.0)), N, method="pchip")
    gx = np.linspace(-0.4, 4.4, 48 * 5 // 2 * 2 + 1); go = np.linspace(0.6, 6.4, 6 * RES + 1)
    XX, OO = np.meshgrid(gx, go, indexing="ij")
    zz = np.clip(f(np.stack([np.clip(XX, 0, 4), np.clip(OO, 1, 6)], -1)), 0, None)
    # the footprint: no mountain beyond half a class from an occupied openness level (keeps blanks flat)
    occ = (N[np.clip(np.rint(np.clip(XX, 0, 4)).astype(int), 0, 4), np.clip(np.rint(OO).astype(int) - 1, 0, 5)] > 0)
    edge = np.clip(1.6 - 2.4 * np.minimum(np.abs(XX - np.clip(XX, 0, 4)), np.abs(OO - np.clip(OO, 1, 6))), 0, 1)
    return XX, OO, zz * occ * edge


def draw(field):
    pp = load(field)
    Na, Ns = grid(pp, 0), grid(pp, 3)
    top = Na.max()
    fig = plt.figure(figsize=(19, 11.5), facecolor="white")
    ax = fig.add_axes([0.0, 0.1, 0.66, 0.8], projection="3d", computed_zorder=False)

    # ---- glass mountain: every claim
    XX, OO, za = smooth(np.sqrt(Na))     # altitude on a square-root scale: 2024-2026 holds most papers
    ax.plot_wireframe(XX, OO, za, rstride=8, cstride=10, color="#5d7f95", linewidth=0.45, alpha=0.55, zorder=1)
    ax.plot_surface(XX, OO, za, color="#cfe0ea", alpha=0.18, linewidth=0, shade=False, zorder=1)
    # ---- solid mountain: strongly verified (V3-V4) = Fig. 1's land
    XX, OO, zs = smooth(np.sqrt(Ns))
    ls = LightSource(azdeg=300, altdeg=40)
    rgb = ls.shade_rgb(ALT(0.12 + 0.88 * np.clip(zs / np.sqrt(max(Ns.max(), 1)), 0, 1))[:, :, :3], zs * 2.2,
                       blend_mode="soft", fraction=0.9)
    land = zs > 0.05
    fc = np.dstack([rgb, np.where(land, 0.97, 0.0)])
    ax.plot_surface(XX, OO, zs, facecolors=fc, rstride=1, cstride=1, linewidth=0, antialiased=True, shade=False,
                    zorder=2)
    # ---- Fig. 1 on the floor: land per era (shade = era), blanks in red
    LAND = ["#efe6cf", "#e2d3a9", "#cdb982", "#ae9a5e", "#86733f"]
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    for e in range(5):
        for o in range(1, 7):
            first = Ns[e, o - 1] > 0 and (e == 0 or Ns[e - 1, o - 1] == 0)
            if Ns[e, o - 1] > 0:
                ax.add_collection3d(Poly3DCollection([[(e - 0.46, o - 0.44, 0), (e + 0.46, o - 0.44, 0),
                                                       (e + 0.46, o + 0.44, 0), (e - 0.46, o + 0.44, 0)]],
                                                     facecolor=LAND[e] if first else LAND[e] + "80", alpha=0.75,
                                                     edgecolor="none", zorder=0.5))
    blanks = [o for o in range(1, 7) if Ns[-1, o - 1] == 0]
    for o in blanks:
        ax.plot([-0.45, 4.45], [o, o], [0, 0], color=ACC, lw=1.2, ls=(0, (2, 2)), zorder=3)
        ax.text(-0.55, o, 0, f"空白 O{o}" + ("（仅有声明）" if Na[-1, o - 1] else ""), fontsize=10, color=ACC,
                fontweight="bold", va="center", ha="right", zorder=30)
    # ---- numbers at each era node: strong / all
    for e in range(5):
        for o in range(1, 7):
            a, s = int(Na[e, o - 1]), int(Ns[e, o - 1])
            if a and (e == 4 or Na[e, o - 1] != (Na[e + 1, o - 1] if e < 4 else -1)):
                ax.text(e, o, np.sqrt(a) + 0.35, f"{s}/{a}" if s else f"–/{a}", fontsize=9.5 if e == 4 else 8.5,
                        ha="center", color=ACC if s else "#4a6a7f", fontweight="bold", zorder=40)
                if s:
                    ax.scatter([e], [o], [np.sqrt(s)], s=22, c=ACC, edgecolors="white", linewidths=0.8, depthshade=False,
                               zorder=35)
    # ---- axes
    ax.set_xlim(-0.5, 4.5); ax.set_ylim(0.5, 6.5); ax.set_zlim(0, np.sqrt(top) * 1.08)
    ax.set_xticks(range(5), ERA_TICK, fontsize=10.5)
    ax.set_yticks(range(1, 7), O_TICK, fontsize=10)
    zt = [k for k in (1, 2, 5, 10, 20, 40, 60, 100, 150) if k <= top * 1.1]
    ax.set_zticks(np.sqrt(zt), [str(k) for k in zt], fontsize=9.5)
    ax.set_xlabel("时期（proposal Fig. 1 的五个时代）", labelpad=20, fontsize=11.5)
    ax.set_ylabel("问题开放度 O", labelpad=26, fontsize=11.5)
    ax.set_zlabel("累计论文数（海拔，平方根刻度）", labelpad=12, fontsize=11.5)
    for a in (ax.xaxis, ax.yaxis, ax.zaxis):
        a.pane.set_facecolor((0.993, 0.99, 0.984, 1)); a.pane.set_edgecolor("#e4dfd6")
        a._axinfo["grid"].update(color="#ece8e1", linewidth=0.5)
    ax.set_box_aspect((2.1, 2.0, 1.35), zoom=1.0)
    ax.view_init(elev=28, azim=-58)

    # ---- right: the latest cross-section along V and along L
    o = np.arange(1, 7)
    a1 = fig.add_axes([0.725, 0.55, 0.25, 0.29])
    for v in range(5):
        n = grid(pp, v)[-1]
        a1.plot(o, n, color=V_COL[v], lw=3 if v in (0, 3) else 1.4, marker="o", ms=5 if v in (0, 3) else 3.5,
                label=f"V ≥ {v}" + ("（全部声明）" if v == 0 else "（强验证 = 陆地）" if v == 3 else ""), zorder=3)
    a1.fill_between(o, grid(pp, 3)[-1], grid(pp, 0)[-1], color="#cfe0ea", alpha=0.6, lw=0, zorder=1)
    a1.fill_between(o, 0, grid(pp, 3)[-1], color=ALT(0.55), alpha=0.35, lw=0, zorder=1)
    a1.set_xticks(o, [f"O{k}" for k in o]); a1.set_ylabel("论文数")
    a1.set_title("截至 2026 的截面：各验证门槛下的论文数", fontsize=11, color=INK, loc="left", fontweight="bold")
    a1.legend(frameon=False, fontsize=8.5, loc="upper right")
    a2 = fig.add_axes([0.725, 0.14, 0.25, 0.29])
    w = 0.38
    for side, (vlo, vhi, alpha, hatch) in enumerate([(3, 4, 1.0, None), (0, 2, 0.35, None)]):
        bot = np.zeros(6)
        for L in range(4):
            n = np.array([sum(p["o"] == k and p["l"] == L and vlo <= p["v"] <= vhi for p in pp) for k in o])
            a2.bar(o + (side - 0.5) * w, n, w * 0.92, bottom=bot, color=L_COL[L], alpha=alpha,
                   edgecolor="white", linewidth=0.6)
            bot += n
    a2.set_xticks(o, [f"O{k}" for k in o]); a2.set_ylabel("论文数")
    a2.set_title("同一截面按系统自主性 L 拆开：左柱强验证，右柱仅声明", fontsize=11, color=INK, loc="left",
                 fontweight="bold")
    a2.legend(handles=[Patch(color=L_COL[k], label=L_NAME[k]) for k in range(4)], frameon=False, fontsize=8.5,
              loc="upper right")
    for a in (a1, a2):
        a.spines[["top", "right"]].set_visible(False); a.grid(axis="y", color="#ece8e1", lw=0.6)
        a.tick_params(labelsize=9.5)

    # ---- text
    ns = sum(p["v"] >= 3 for p in pp)
    fig.text(0.03, 0.955, f"{FZH[field]}：可检验前沿的证据山", fontsize=21, fontweight="bold", color=INK)
    fig.text(0.03, 0.925, f"{len(pp)} 篇，强验证（V3–V4）{ns} 篇（{100 * ns / len(pp):.0f}%）　·　"
             f"截至 2026 的陆地：{'、'.join(f'O{k}' for k in o if Ns[-1, k - 1]) or '无'}　·　"
             f"位置空白：{'、'.join(f'O{k}' for k in blanks) or '无'}", fontsize=11.5, color=MUTED)
    hand = [Patch(color=ALT(0.6), label="实心山 = 强验证（V3–V4）论文累计数；山脚轮廓即 Fig. 1 的陆地"),
            Patch(facecolor="#cfe0ea", edgecolor="#5d7f95", label="玻璃山 = 全部声明（V0–V4）累计数；高出实心山的部分 = 水面之上"),
            Patch(color=LAND[2], label="地面色块 = Fig. 1 陆地，颜色由浅到深为首次登陆的时代"),
            Line2D([], [], color=ACC, lw=1.2, ls=(0, (2, 2)), label="红色虚线 = 位置空白（该开放度尚无强验证）")]
    fig.legend(handles=hand, loc="upper left", bbox_to_anchor=(0.03, 0.905), frameon=False, fontsize=9.8)
    fig.text(0.03, 0.022,
             "节点数字 = 强验证篇数 / 全部声明篇数（截至该时期末累计；只在数值变化处标注）；节点之间用单调插值连成山面，没有论文的开放度不起山。"
             "≤1997 与 1998–2012 两期本语料无该学科论文。\n"
             "数据：662 篇核心论文的 O/V/L 编码（V 为论文自报证据，非裁定）；跨学科论文在每个所属学科各计一次 · 快照 2026-11-01",
             fontsize=9, color=MUTED, linespacing=1.7)
    S.save(fig, f"fig_ovl_frontier_mountain_f{field}"); plt.close(fig)
    print(field, len(pp), "strong", Ns[-1], "all", Na[-1], "blanks", blanks)


if __name__ == "__main__":
    for fc in (sys.argv[1:] or ["03"]):
        draw(fc)
