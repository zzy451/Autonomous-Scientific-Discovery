"""Regenerate every figure, write the content -> form -> version folder tree with a README in every
folder, typeset the Figure Tech Report (XeLaTeX, table of contents first) and zip the package.
Usage: python3 build_package.py [--no-render]"""
import shlex, shutil, subprocess, sys, zipfile, datetime
from pathlib import Path
from package_spec import TREE, NOT_TESTABLE

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
PKG = DIST / "Agent4Science_FigureSet"
REPORT = "Figure_Tech_Report.pdf"
CODE = sorted(p.name for p in ROOT.glob("*.py"))
OV_KEEP = ["RUBRIC.md", "README.md"]
VISUAL_REFS = [
    ("Hierarchical edge bundling, chord, genome rings", "Circos-style circular data art (M. Krzywinski, Nature journal covers)"),
    ("Cross-domain atlas, wormhole", "Barabasi Lab co-citation network for Nature's 150th anniversary (2019)"),
    ("Pulsar ridgelines", "H. Craft's PSR B1919+21 plot (Arecibo), used on Unknown Pleasures (1979)"),
    ("Periodic table with gaps", "Mendeleev's 1869 table and its predicted eka-elements"),
    ("Review rose", "F. Nightingale's coxcomb diagrams (1858)"),
    ("Ledger mosaic", "Tsevis's mosaic covers for Science"),
]
VIDEO = ROOT / "video"            # proposal explainer video and its HyperFrames source, copied as-is
VIDEO_DIR = "16_proposal_explainer_video"
FOUR_DIR = "17_five_dimension_views"    # one paper, five dimensions (O, V, L, T, field C): four views x six fields + report
FOUR_PDF = ROOT / "report" / "OVL_Four_Views.pdf"
FOUR_FIELDS = ["03", "04", "06", "07", "01", "11"]
FOUR_VIEWS = [  # folder, source pattern, script, how the four dimensions are placed
    ("ridges", "out/modes/mode5_ridges_f{f}.png", "fig_ovl_modes.py",
     "T = one row per year, O = horizontal axis, V = red fill for V3–V4, L = colour of the tick under each paper"),
    ("relief", "out/styles/shortlist/C3_relief_f{f}.png", "fig_ovl_styles_C.py",
     "O × V = oblique shaded relief of paper density, red coastline between V2 and V3, L = composition bars on the summit labels; no T"),
    ("parallel", "out/styles/shortlist/B8_parallel_f{f}.png", "fig_ovl_styles_B.py",
     "T → O → V → L as four parallel axes, one path per paper, red = strong verification"),
    ("rings", "out/styles/shortlist/D4_rings_f{f}.png", "fig_ovl_styles_D.py",
     "O = one ring per level, V = red arc for strong, L = thin outer sub-ring, T = cumulative mini rings at 2019, 2023, 2026"),
]
SNAP = "662 core papers · snapshot 2026-11-01 · decision mechanisms 2026-11-03 · repository commit 60f8bad"


def leaves(form):
    """Yield (relative path parts, version) for a form, through optional sub-forms."""
    for sf in form.get("subforms", []):
        for ver in sf["versions"]:
            yield [sf["folder"], ver["folder"]], ver
    for ver in form.get("versions", []):
        yield [ver["folder"]], ver


def run_all():
    for s in ["build_data.py", "style.py", "proxies.py", "notes_extract.py", "make_leaderboard_html.py"]:
        subprocess.run([sys.executable, s], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
    seen = set()
    for c in TREE:
        for f in c["forms"]:
            for _, ver in leaves(f):
                if ver["cmd"] not in seen:
                    seen.add(ver["cmd"])
                    args = shlex.split(ver["cmd"])[1:]
                    subprocess.run([sys.executable, *args], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)


# ------------------------------------------------------------------ READMEs
def readme_root():
    lines = [f"# Agent-for-Science figure set\n\n{SNAP}.\n",
             "Figures for *From Computable Tasks to Open Science: A Chronicle of AI Problem Solving*, built from the "
             "classified literature corpus. Folders are organised as **content → presentation form → version**, "
             f"and every folder has a README. `{REPORT}` collects every figure with its caption, generation method "
             "and analysis; its table of contents mirrors this tree.\n",
             "| Content | Forms | Verdict on the proposal claim |", "|---|---|---|"]
    for c in TREE:
        lines.append(f"| `{c['folder']}/` {c['title']} | " + ", ".join(f"`{f['folder']}`" for f in c["forms"])
                     + f" | {c['verdict']} |")
    if VIDEO.exists():
        lines.append(f"| `{VIDEO_DIR}/` Proposal explainer video | 1080p and 480p MP4, HyperFrames source | "
                     "Walkthrough of the proposal, 14 scenes, Mandarin narration |")
    if FOUR_PDF.exists():
        lines.append(f"| `{FOUR_DIR}/` One paper, five dimensions (O, V, L, T, field C) | "
                     + ", ".join(f"`{v[0]}`" for v in FOUR_VIEWS) + " | Four views × six fields, with `OVL_Four_Views.pdf` |")
    lines += ["\n## Tree\n", "```"]
    for c in TREE:
        lines.append(f"{c['folder']}/")
        for f in c["forms"]:
            lines.append(f"  {f['folder']}/")
            for parts, _ in leaves(f):
                lines.append("    " + "/".join(parts) + "/")
    if VIDEO.exists():
        lines += [f"{VIDEO_DIR}/", "  source/"]
    if FOUR_PDF.exists():
        lines += [f"{FOUR_DIR}/"] + [f"  {v[0]}/" for v in FOUR_VIEWS]
    lines += ["```\n", "## Rebuild\n",
              "`code/` holds the runnable copy: MD5-pinned source data, derived tables, all scripts and this builder. "
              "Requirements: Python 3 with matplotlib ≥3.10, numpy and scipy; XeLaTeX for the report.\n",
              "```bash\ncd code && python3 build_package.py\n```\n",
              "## Visual references\n",
              *[f"- **{a}**: after {r}" for a, r in VISUAL_REFS], "",
              "## The three axes\n",
              "All 662 core papers are coded on the proposal's three axes: problem openness O1–O6, verification "
              "strength V0–V4 (V3–V4 = strong) and system autonomy L0–L3. The rubric is `code/ov_coding/RUBRIC.md`; "
              "labels and evidence quotes are in `code/ov_coding/increment/`. V is the paper's self-reported "
              "evidence, not an adjudicated 'solved'.\n"]
    return "\n".join(lines)


def readme_content(c):
    out = [f"# {c['title']}\n", f"**Classification:** content `{c['folder']}`\n",
           f"## Proposal claim\n{c['claim']}\n", f"**Verdict:** {c['verdict']}\n",
           f"## Analysis\n{c['analysis']}\n", f"## Limits\n{c['limits']}\n", "## Presentation forms\n"]
    for f in c["forms"]:
        n = sum(1 for _ in leaves(f))
        out.append(f"- `{f['folder']}/`: {f['title']} ({n} version{'s' if n > 1 else ''})")
    return "\n".join(out) + "\n"


def readme_form(c, f):
    out = [f"# {f['title']}\n", f"**Classification:** content `{c['folder']}` › form `{f['folder']}`\n",
           f"## Caption\n{f['caption']}\n", f"## How it is generated\n{f['method']} "
           f"Scripts: {', '.join('`' + s + '`' for s in f['scripts'])} (run from `code/`).\n"]
    if f.get("analysis"):
        out.append(f"## Analysis\n{f['analysis']}\n")
    out.append("## Versions\n")
    for parts, ver in leaves(f):
        out.append(f"- `{'/'.join(parts)}/`: {ver['note']}")
    return "\n".join(out) + "\n"


def readme_subform(c, f, sf):
    out = [f"# {f['title']} · {sf['folder']} view\n",
           f"**Classification:** content `{c['folder']}` › form `{f['folder']}` › view `{sf['folder']}`\n",
           f"## How to read this view\n{sf.get('about', '')}\n", f"## Caption\n{f['caption']}\n", "## Versions\n"]
    out += [f"- `{ver['folder']}/`: {ver['note']}" for ver in sf["versions"]]
    return "\n".join(out) + "\n"


def readme_leaf(c, f, parts, ver):
    files = "\n".join(f"- `{n}.pdf` (vector) and `{n}.png` (600 dpi)" for n in ver["files"])
    return (f"# {f['title']} · {' / '.join(parts)}\n\n"
            f"**Classification:** content `{c['folder']}` › form `{f['folder']}` › version `{'/'.join(parts)}`\n\n"
            f"{ver['note']}\n\n## Files\n{files}\n- a copy of the generating script\n"
            + "".join(f"- `{Path(e).name}`\n" for e in ver.get("extra", [])) + "\n"
            f"## Caption\n{f['caption']}\n\n## Regenerate\n```bash\ncd code && {ver['cmd']}\n```\n")


# ------------------------------------------------------------------ report
def esc(s):
    rep = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
           "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\^{}"}
    return "".join(rep.get(ch, ch) for ch in s)


PREAMBLE = r"""\documentclass[10pt,a4paper]{article}
\usepackage[margin=14mm,top=16mm,bottom=16mm]{geometry}
\usepackage{fontspec}\setmainfont{Arial}\setsansfont{Arial}
\usepackage{graphicx,booktabs,tabularx,xcolor,titlesec,enumitem,microtype,float,tocloft}
\usepackage[hidelinks]{hyperref}
\definecolor{ink}{HTML}{1D1D1B}\definecolor{ink2}{HTML}{55524C}
\titleformat{\section}{\Large\bfseries\color{ink}}{\thesection}{0.6em}{}
\titleformat{\subsection}{\large\bfseries\color{ink}}{\thesubsection}{0.6em}{}
\titleformat{\subsubsection}{\normalsize\bfseries\color{ink2}}{\thesubsubsection}{0.6em}{}
\setcounter{tocdepth}{3}\setcounter{secnumdepth}{3}
\setlength{\parindent}{0pt}\setlength{\parskip}{4pt}\renewcommand{\arraystretch}{1.25}
\newcommand{\lab}[1]{\textcolor{ink2}{\footnotesize\bfseries\MakeUppercase{#1}}\par}
\begin{document}
"""


def fig_block(name):
    return (f"\\begin{{figure}}[H]\\centering\\includegraphics[width=\\textwidth,height=0.62\\textheight,"
            f"keepaspectratio]{{../out/{name}.pdf}}\\end{{figure}}\n")


def report_tex():
    t = [PREAMBLE, r"""\begin{titlepage}\vspace*{40mm}
{\color{ink}\fontsize{30}{34}\selectfont\bfseries Figure Tech Report\par}\vspace{6mm}
{\Large From Computable Tasks to Open Science:\\ figures for the chronicle of AI problem solving\par}\vspace{10mm}
{\color{ink2}""" + esc(SNAP) + r"""\\ report built """ + datetime.date.today().isoformat() + r"""\par}
\vfill{\color{ink2}\small Organisation: content $\rightarrow$ presentation form $\rightarrow$ version, identical to the
folder tree of the accompanying archive. Every figure is generated by script from the archived classification
records; no number is entered by hand.\par}
\end{titlepage}
\tableofcontents\clearpage
"""]
    t.append(r"\section*{Summary}\addcontentsline{toc}{section}{Summary}" + "\n")
    t.append(r"\begin{tabularx}{\textwidth}{@{}p{46mm}X p{38mm}@{}}\toprule\textbf{Content} & \textbf{Proposal claim} "
             r"& \textbf{Verdict}\\\midrule" + "\n")
    for c in TREE:
        t.append(f"{esc(c['title'])} & {esc(c['claim'].split(' (')[0])} & \\textbf{{{esc(c['verdict'])}}}\\\\\n")
    t.append(r"\bottomrule\end{tabularx}" + "\n\n")
    t.append(r"""\section*{Data and methods}\addcontentsline{toc}{section}{Data and methods}
\textbf{Sources.} All inputs come from repository commit \texttt{60f8bad} (2026-11-03): the core manifest (662 papers),
the D1--D6 decision-mechanism classification, the taxonomy assignments (935 field assignments with second- and
third-level codes), and \texttt{Data/papers.jsonl}, which supplies validation types and workflow roles. Each input is
pinned by MD5 in \texttt{code/README.md}. A few records with UTF-8-read-as-GBK mojibake were repaired before coding.

\textbf{Papercard verification.} Every note and PDF path was matched against the commit's file list: 662/662 notes
and 635/635 claimed PDFs are present. Each paper's field list equals the field set of its taxonomy codes (662/662).
Pairs (422) and assignments (935) match the repository's own counts.

\textbf{The three axes} (\texttt{ov\_coding/RUBRIC.md}, following the proposal). Every core paper is coded on problem
openness O1--O6 (rule world, fixed benchmark, new instance, needs physical test, open mathematics, open science),
verification strength V0--V4 (claim, benchmark, computational, physical experiment, formal proof or third-party
replication; V3--V4 = strong) and system autonomy L0--L3 (tool, task assistant, closed-loop executor, autonomous
researcher). Claude Sonnet 5.5 coded each paper from its papercard; every O and V label quotes the note verbatim with
its line number, and a script checks every quote (662/662 pass). A 30-paper pilot was double-coded with Haiku 5.5
(verification weighted $\kappa$ = 0.93). The labels were written into the papercards in the repository's pull request.

\textbf{Statistics and design.} Proportions carry Wilson 95\% intervals; rank association uses Spearman $\rho$ with a
2{,}000-sample bootstrap. Mechanism colours (\#2f5fb3, \#d9622b, \#1a9b74, \#a8326e, plus a stepped dark set) pass an
all-pairs colour-vision-deficiency check. Brightness always encodes the evidence endpoint.
""")
    t.append(r"\section*{Visual references}\addcontentsline{toc}{section}{Visual references}" + "\n")
    t.append(r"\begin{tabularx}{\textwidth}{@{}p{62mm}X@{}}\toprule\textbf{Form} & \textbf{After}\\\midrule" + "\n")
    t += [f"{esc(a)} & {esc(r)}\\\\\n" for a, r in VISUAL_REFS]
    t.append(r"\bottomrule\end{tabularx}" + "\n")
    for c in TREE:
        t.append(f"\\clearpage\\section{{{esc(c['title'])}}}\n")
        t.append(f"\\lab{{Proposal claim}}{esc(c['claim'])}\n\n\\lab{{Verdict}}\\textbf{{{esc(c['verdict'])}}}\n\n"
                 f"\\lab{{Analysis}}{esc(c['analysis'])}\n\n\\lab{{Limits}}{esc(c['limits'])}\n\n")
        for f in c["forms"]:
            t.append(f"\\clearpage\\subsection{{{esc(f['title'])}}}\n")
            t.append(f"\\lab{{Folder}}\\texttt{{{esc(c['folder'] + '/' + f['folder'] + '/')}}}\n\n"
                     f"\\lab{{Caption}}{esc(f['caption'])}\n\n\\lab{{How it is generated}}{esc(f['method'])}\n\n")
            if f.get("analysis"):
                t.append(f"\\lab{{Analysis}}{esc(f['analysis'])}\n\n")
            about = {sf["folder"]: sf.get("about", "") for sf in f.get("subforms", [])}
            for parts, ver in leaves(f):
                if len(parts) == 2 and about.get(parts[0]):
                    t.append(f"\\lab{{View: {esc(parts[0])}}}{esc(about.pop(parts[0]))}\n\n")
                t.append(f"\\subsubsection{{{esc(' / '.join(parts))}}}\n{esc(ver['note'])}\n")
                for n in ver["files"]:
                    t.append(fig_block(n))
                t.append(f"{{\\footnotesize\\color{{ink2}}\\texttt{{{esc(ver['cmd'])}}}}}\n")
    t.append(r"\clearpage\section*{What this corpus cannot test}\addcontentsline{toc}{section}{What this corpus cannot test}" + "\n")
    t.append(r"\begin{tabularx}{\textwidth}{@{}p{75mm}X@{}}\toprule\textbf{Proposal element} & \textbf{Why not}\\\midrule" + "\n")
    t += [f"{esc(a)} & {esc(b)}\\\\\n" for a, b in NOT_TESTABLE]
    t.append(r"\bottomrule\end{tabularx}" + "\n\\end{document}\n")
    return "".join(t)


def build_report():
    rep = ROOT / "report"; rep.mkdir(exist_ok=True)
    (rep / "Figure_Tech_Report.tex").write_text(report_tex(), encoding="utf-8")
    for _ in range(2):                                   # second pass fills the table of contents
        subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "Figure_Tech_Report.tex"],
                       cwd=rep, check=True, stdout=subprocess.DEVNULL)
    return rep / REPORT


# ------------------------------------------------------------------ package
def package(report_pdf):
    if PKG.exists():
        shutil.rmtree(PKG)
    code = PKG / "code"; code.mkdir(parents=True)
    for p in CODE:
        shutil.copy2(ROOT / p, code / p)
    for d in ("source_data", "derived"):
        shutil.copytree(ROOT / d, code / d, ignore=shutil.ignore_patterns("notes", "notes.tar.gz"))
    shutil.copytree(ROOT / "ov_coding" / "increment", code / "ov_coding" / "increment")
    shutil.copy2(ROOT / "ov_coding" / "RUBRIC.md", code / "ov_coding" / "RUBRIC.md")
    shutil.copy2(ROOT / "README.md", code / "README.md")
    (PKG / "README.md").write_text(readme_root(), encoding="utf-8")
    shutil.copy2(report_pdf, PKG / REPORT)
    for c in TREE:
        cd = PKG / c["folder"]; cd.mkdir()
        (cd / "README.md").write_text(readme_content(c), encoding="utf-8")
        for f in c["forms"]:
            fd = cd / f["folder"]; fd.mkdir()
            (fd / "README.md").write_text(readme_form(c, f), encoding="utf-8")
            for sf in f.get("subforms", []):
                (fd / sf["folder"]).mkdir()
                (fd / sf["folder"] / "README.md").write_text(readme_subform(c, f, sf), encoding="utf-8")
            for parts, ver in leaves(f):
                ld = fd.joinpath(*parts); ld.mkdir(parents=True, exist_ok=True)
                for n in ver["files"]:
                    for ext in ("pdf", "png"):
                        shutil.copy2(ROOT / "out" / f"{n}.{ext}", ld / f"{n}.{ext}")
                for s in f["scripts"]:
                    shutil.copy2(ROOT / s, ld / s)
                for e in ver.get("extra", []):
                    shutil.copy2(ROOT / e, ld / Path(e).name)
                (ld / "README.md").write_text(readme_leaf(c, f, parts, ver), encoding="utf-8")
    if VIDEO.exists():
        shutil.copytree(VIDEO, PKG / VIDEO_DIR, ignore=shutil.ignore_patterns(".DS_Store"))
    if FOUR_PDF.exists():
        four_views(PKG / FOUR_DIR)
    zpath = DIST / "Agent4Science_FigureSet.zip"
    if zpath.exists():
        zpath.unlink()
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(PKG.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(DIST))
    return zpath


def four_views(d):
    """Copy the five-dimension views (built by build_ovl_views_report.py) with a README per folder."""
    from fig_ovl_surface import FZH
    d.mkdir()
    shutil.copy2(FOUR_PDF, d / FOUR_PDF.name)
    top = ["# One paper, five dimensions: openness O × verification V × autonomy L × time T × field C\n",
           "Each core paper carries five coordinates. The four views place O, V, L and T on different visual channels; "
           f"field C is faceting: every view is drawn once per field, here six fields ({', '.join(FZH[f] for f in FOUR_FIELDS)}). `{FOUR_PDF.name}` collects all 24 "
           "figures with how to read each view. Strong verification = V3–V4 (red); a *blank* is an openness level "
           "with papers but no strong case, and a level with no papers is marked 无论文 instead.\n",
           "| View | Where O, V, L and T go (C = one figure per field) | Script |", "|---|---|---|"]
    for folder, pat, script, how in FOUR_VIEWS:
        top.append(f"| `{folder}/` | {how} | `{script}` |")
        vd = d / folder; vd.mkdir()
        for f in FOUR_FIELDS:
            shutil.copy2(ROOT / pat.format(f=f), vd / Path(pat.format(f=f)).name)
        shutil.copy2(ROOT / script, vd / script)
        (vd / "README.md").write_text(f"# {folder}\n\n{how}.\n\nOne PNG per field: "
                                      + ", ".join(f"`{Path(pat.format(f=f)).name}` ({FZH[f]})" for f in FOUR_FIELDS)
                                      + f".\n\nRebuild all four views and the report: `python3 build_ovl_views_report.py`"
                                      f" (script for this view: `{script}`).\n", encoding="utf-8")
    top.append("\nRebuild: `cd code && python3 build_ovl_views_report.py`.\n")
    (d / "README.md").write_text("\n".join(top), encoding="utf-8")


if __name__ == "__main__":
    if "--no-render" not in sys.argv:
        run_all()
    pdf = build_report()
    print("report:", pdf)
    print("zip:", package(pdf))
