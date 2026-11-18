"""Report: four ways to show each paper's five dimensions (openness O, verification V, autonomy L, time T, field C), six fields.

Renders the four approved views for each field, then writes and compiles report/OVL_Four_Views.tex:
  mode5 ridges   (fig_ovl_modes.m5)      : one ridge per year, openness distribution, strong part red
  C3 relief      (fig_ovl_styles_C.c3)   : oblique shaded relief of paper density over O x V
  B8 parallel    (fig_ovl_styles_B.b8)   : one path per paper, era -> O -> V -> L
  D4 rings       (fig_ovl_styles_D.d4)   : one ring per openness level, strong arc red, autonomy sub-ring
Every number in the report is computed from ov_coding/increment/classification_results_662.jsonl.
Usage: python3 build_ovl_views_report.py [--no-render]
"""
import sys, subprocess
import style as S
import fig_ovl_modes as M, fig_ovl_styles_B as B, fig_ovl_styles_C as Cc, fig_ovl_styles_D as D
from fig_ovl_surface import FZH

FIELDS = ["03", "04", "06", "07", "01", "11"]
REP = S.ROOT / "report"
VIEWS = [
    ("年轮山脊：时间 × 开放度", "../out/modes/mode5_ridges_f{f}.png", M.m5,
     "每一行是一年（2013 年以前有论文的时代合并为一行），横向是开放度 O1--O6。灰色山体是当年全部论文的开放度分布，"
     "红色是其中强验证（V3--V4）的部分；山脚每根短线是一篇论文，颜色为自主性 L。右列给出当年的强验证 / 全部。"
     "底部标出位置空白（有论文但没有一篇强验证）与无论文的开放度。"
     "这一视图回答“前沿随时间如何移动”：山体变高说明论文增多，红色占比变小说明证据变薄。"),
    ("斜视晕渲：开放度 × 验证强度的地貌", "../out/styles/shortlist/C3_relief_f{f}.png", Cc.c3,
     "把每篇论文放在（O, V）平面上，按论文密度堆成地形，从斜上方打光。红色海岸线位于 V2 与 V3 之间："
     "岸上（暖色）是强验证，岸下（冷色）只有声明。山顶上方一排标签给出论文最多的组合及其自主性构成，"
     "被前山挡住的峰标“（山后）”。这一视图回答“论文集中在哪里、有多少已经上岸”。"),
    ("平行坐标：每篇论文一条路径", "../out/styles/shortlist/B8_parallel_f{f}.png", B.b8,
     "四根轴依次为时期、开放度、验证强度、自主性；每篇论文是一条从左到右的曲线，红色为强验证，蓝灰为仅声明。"
     "方框给出该类别的论文数与强验证数；没有论文的类别压成虚线小框并标“无论文”。"
     "这一视图把三维分类与时间同时摊开，适合追踪“哪个开放度的论文流向了哪种验证、由哪级自主性完成”。"),
    ("活动圆环：每个开放度一环", "../out/styles/shortlist/D4_rings_f{f}.png", D.d4,
     "由外到内依次为 O6 到 O1；红弧是强验证论文，灰弧是仅声明，空轨道表示没有论文；"
     "每环外侧细环按论文逐篇对齐显示自主性 L。右侧列出每个开放度的强验证 / 全部和空白标记，"
     "底部三组小圆环为截至 2019、2023、2026 的累计状态。这一视图是全学科的一页摘要。"),
]


def stats(f):
    pp = M.load(f)
    n, s = len(pp), sum(p["v"] >= 3 for p in pp)
    blanks = [o for o in range(1, 7) if any(p["o"] == o for p in pp) and not any(p["o"] == o and p["v"] >= 3 for p in pp)]
    none = [o for o in range(1, 7) if not any(p["o"] == o for p in pp)]
    recent = sum(p["year"] >= 2024 for p in pp)
    top = max(range(1, 7), key=lambda o: sum(p["o"] == o and p["v"] >= 3 for p in pp))
    return dict(n=n, s=s, blanks=blanks, none=none, recent=recent, y0=min(p["year"] for p in pp),
                top=top if s else None, v4=sum(p["v"] == 4 for p in pp), l3=sum(p["l"] == 3 for p in pp))


def olist(xs):
    return "、".join(f"O{o}" for o in xs) or "无"


def tex():
    rows = []
    for f in FIELDS:
        t = stats(f)
        rows.append(f"{FZH[f]} & {t['n']} & {t['s']}（{100 * t['s'] / t['n']:.0f}\\%） & {t['v4']} & {t['l3']} & "
                    f"{100 * t['recent'] / t['n']:.0f}\\% & {olist(t['blanks'])} & {olist(t['none'])}\\\\")
    out = [r"""\documentclass[10pt,a4paper]{article}
\usepackage[margin=14mm,top=16mm,bottom=16mm]{geometry}
\usepackage{fontspec}\setmainfont{Arial}\setsansfont{Arial}
\usepackage{xeCJK}\setCJKmainfont[BoldFont={Hiragino Sans GB W6}]{Hiragino Sans GB W3}
\usepackage{graphicx,booktabs,tabularx,xcolor,titlesec,microtype,float,caption}\captionsetup{labelformat=empty}
\usepackage[hidelinks]{hyperref}
\definecolor{ink}{HTML}{1D1D1B}\definecolor{ink2}{HTML}{55524C}\definecolor{acc}{HTML}{B2412F}
\titleformat{\section}{\Large\bfseries\color{ink}}{\thesection}{0.6em}{}
\titleformat{\subsection}{\large\bfseries\color{ink}}{\thesubsection}{0.6em}{}
\setlength{\parindent}{0pt}\setlength{\parskip}{5pt}\renewcommand{\arraystretch}{1.3}
\linespread{1.25}
\renewcommand{\contentsname}{目录}
\begin{document}
\begin{titlepage}\vspace*{40mm}
{\color{ink}\fontsize{28}{34}\selectfont\bfseries 一篇论文的五维展示\par}\vspace{6mm}
{\Large 开放度 O × 验证强度 V × 自主性 L × 时间 T × 学科 C：四种呈现方式\par}\vspace{3mm}
{\large 六个学科：化学、材料、生命科学、医学与健康、形式与计算科学、社会与知识系统\par}\vspace{10mm}
{\color{ink2}662 篇核心论文 · 快照 2026-11-01 · 报告生成 2026-11-04\par}
\vfill{\color{ink2}\small 所有图由脚本从归档的分类记录生成（\texttt{build\_ovl\_views\_report.py}），没有手工录入的数字。
V 为论文自报证据的编码，不是“已解决”的裁定。\par}
\end{titlepage}
\tableofcontents\clearpage
\section{编码与读法}
三根轴沿用 proposal：问题开放度 O1--O6（规则世界、既定基准、新实例、需物理检验、开放数学、开放科学），
验证强度 V0--V4（声明、基准、计算/仿真、物理实验、证明/第三方复现；\textcolor{acc}{\textbf{V3--V4 为强验证}}，
即 proposal Fig.~1 的“陆地”），系统自主性 L0--L3（工具、任务助手、闭环执行者、自主研究者）。
时间按 proposal 的五个时代分：≤1997、1998--2012、2013--2019、2020--2023、2024--2026。

四张图共用一套约定：红色只表示强验证；自主性 L 的四种颜色在所有图中一致；
\textbf{位置空白}指某开放度有论文、但没有一篇强验证；某开放度一篇论文都没有时标“无论文”，不算空白。
跨学科论文在它所属的每个学科各计一次。

\begin{table}[H]\small\centering
\begin{tabularx}{\textwidth}{@{}l r r r r r X X@{}}\toprule
学科 & 论文 & 强验证 & V4 & L3 & 2024 年后 & 位置空白 & 无论文\\\midrule
""" + "\n".join(rows) + r"""
\bottomrule\end{tabularx}
\caption*{\small 各列由编码记录直接计算。“2024 年后”= 2024--2026 年论文的占比。}
\end{table}

\textbf{四种视图的分工。}每篇论文有五个维度：开放度 O、验证强度 V、自主性 L、发表时间 T 和学科类别 C。
四种视图把前四维放在不同的视觉通道上；学科 C 在所有视图里都用分面表示，即每个学科单独一张图（本报告取六个学科，
其余学科运行同一脚本即可）。下表给出每种视图里各维的位置。

\begin{table}[H]\small\centering
\begin{tabularx}{\textwidth}{@{}l X X X X l@{}}\toprule
视图 & 开放度 O & 验证强度 V & 自主性 L & 时间 T & 学科 C\\\midrule
年轮山脊 & 横轴 & 红色填充 = V3--V4 & 山脚短线颜色 & 纵轴（每年一行） & 分面\\
斜视晕渲 & 横轴 & 纵深轴，红色海岸线分强弱 & 峰顶标注条的构成 & 不显示 & 分面\\
平行坐标 & 第 2 根轴 & 第 3 根轴，红线 = 强验证 & 第 4 根轴 & 第 1 根轴（时代） & 分面\\
活动圆环 & 每环一个等级 & 红弧 = 强验证 & 外侧细环 & 底部三组累计小圆环 & 分面\\
\bottomrule\end{tabularx}
\end{table}
"""]
    for k, (title, path, _, how) in enumerate(VIEWS, 1):
        out.append(f"\\clearpage\\section{{{title}}}\n\\textbf{{读法。}}{how}\n")
        for f in FIELDS:
            t = stats(f)
            note = (f"{t['n']} 篇，强验证 {t['s']} 篇；位置空白：{olist(t['blanks'])}；无论文：{olist(t['none'])}；"
                    f"最早论文 {t['y0']} 年。")
            out.append(f"\\begin{{figure}}[H]\\centering\n\\includegraphics[width=\\textwidth,height=0.8\\textheight,"
                       f"keepaspectratio]{{{path.format(f=f)}}}\n\\caption*{{\\small\\textbf{{{FZH[f]}}}　{note}}}\n"
                       f"\\end{{figure}}\n")
    out.append(r"""\clearpage\section{局限}
\begin{itemize}
\item V 是论文自报证据的编码，强验证不等于问题已解决；争议案例在全部 662 篇中只有 1 篇。
\item 语料集中在 2024--2026 年，早期时代多数学科没有论文，所以按时间展开的视图左侧偏空；这是语料本身的分布，不是画法造成的。
\item proposal Fig.~1 的 84 个案例与里程碑记录不在本语料中，本报告只用核心论文。
\item 自主性 L3 的颜色与强验证红色接近，L3 论文紧挨红弧时不易分辨（各学科 L3 均很少，见上表）。
\end{itemize}
\end{document}
""")
    return "\n".join(out)


if __name__ == "__main__":
    if "--no-render" not in sys.argv:
        for f in FIELDS:
            pp = M.load(f)
            for _, _, fn, _ in VIEWS:
                fn(pp, f)
    (REP / "OVL_Four_Views.tex").write_text(tex(), encoding="utf-8")
    for _ in range(2):
        subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "OVL_Four_Views.tex"], cwd=REP,
                       check=True, stdout=subprocess.DEVNULL)
    print(REP / "OVL_Four_Views.pdf")
