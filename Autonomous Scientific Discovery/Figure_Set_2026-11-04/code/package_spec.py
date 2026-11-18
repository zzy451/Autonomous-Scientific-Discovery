"""Tree layout of the figure package: content -> presentation form -> version (white background only).

Every number in this file comes from the coded O / V / L axes (ov_coding/increment, RUBRIC.md, proposal
scales; snapshot 2026-11-01) and the corpus tables in derived/. The Tech Report walks the same tree."""

LEG = ("Colour = decision mechanism (LLM-driven, optimisation, hybrid, symbolic/planning). Brightness = "
       "verification strength: V3–V4 strong (physical experiment, formal proof or third-party replication), "
       "then V2, V1, V0.")


def v(files, cmd, note="White background.", extra=None, folder="white"):
    d = dict(folder=folder, files=files, cmd=cmd, note=note)
    if extra:
        d["extra"] = extra
    return d


def form(folder, title, caption, method, scripts, files, cmd, analysis=None, extra=None):
    f = dict(folder=folder, title=title, caption=caption, method=method, scripts=scripts,
             versions=[v(files, cmd, extra=extra)])
    if analysis:
        f["analysis"] = analysis
    return f


NOT_TESTABLE = [
    ("Verified / claimed / contested / refuted status of the 84 chronicle cases (§2(2))",
     "The 84-case table is not in the repository; the corpus codes one contested record only."),
    ("Whether a V3 or V4 label survives expert reading (§3)",
     "Labels are coded from papercards; 109 papers are flagged for full-text review and 126 sit in the "
     "expert review queue."),
    ("The actual AI contribution versus human-supplied candidates (§3)", "Not coded corpus-wide."),
    ("Named O6 blanks (Riemann, P vs NP, fusion, origin of life, ...) (§2(3)(ii))",
     "Requires the chronicle's problem statements; the corpus marks field-level gaps instead."),
]

TREE = [
    dict(folder="01_three_axes", title="The three axes: openness × verification × autonomy",
         claim="Problem openness (O1–O6), verification strength (V0–V4) and system autonomy (L0–L3) are separate "
               "axes. Once separated, autonomy and verification run opposite (proposal §2(1)–(2)).",
         verdict="Axes separate cleanly; the opposition holds only from L2 to L3",
         analysis="Strong verification (V3–V4) by autonomy is 1% at L1 (2/179), 31% at L2 (144/471) and 25% at L3 "
                  "(3/12; 95% CI 9–53%). It falls from L2 to L3, as the proposal says, but task assistants (L1) are "
                  "the least verified, so over the whole corpus autonomy and verification are positively related "
                  "(Spearman ρ = 0.37). On the mountain, 662 papers occupy 33 of the 120 (O, V, L) cells. The largest is "
                  "O3·V2·L2 (178), and the strong cells are O4·V3·L2 (81) and O3·V3·L2 (54); O2 benchmark problems "
                  "almost never reach strong verification (1/185). By field, the strong share runs from 0% (social and "
                  "knowledge systems) and 6% (formal and computational) to 36% (chemistry), 40% (materials) and 44% "
                  "(aerospace, marine and transport).",
         limits="L3 has only 12 papers. V is self-reported in the papers; L0–L3 is operationalised in RUBRIC.md and "
                "awaits confirmation against Wei et al.",
         forms=[
             form("curtains_3d", "Autonomy curtains (3D)",
                  "One translucent wall per autonomy level (L1–L3; L0 has no papers). On each wall, the curve gives the "
                  "share of that level's papers verified at V or stronger, from V0 to V4. The ★ point is the share "
                  "with strong verification (V3–V4); a dashed line joins the ★ points across walls.",
                  "fig_axes3d.py (matplotlib mplot3d), from ov_coding/increment/classification_results_662.jsonl.",
                  ["fig_axes3d.py"], ["fig_axes3d_curtains"], "python3 fig_axes3d.py"),
             form("mountain_surface_3d", "One mountain through the 3D scatter: openness × verification × autonomy",
                  "Every (V, L, O) combination is a point in the three-axis space: verification V0–V4 (front), autonomy "
                  "L0–L3 (right) and problem openness O1–O6 (up). Point area is proportional to papers and colour gives "
                  "the autonomy level. The mountain is the Gaussian-smooth surface through all the points, a paper-"
                  "weighted Gaussian-kernel regression of openness over (V, L) (σ = 0.55 class steps along V and 0.22 "
                  "along L, so each autonomy level keeps its own mean). The colour bar gives altitude. Height is mean "
                  "openness, not a count, so wherever there are no papers (every empty (V, L) column, all of L0 and the "
                  "plain beyond V0–V4) it sits at 0. The line view draws the L0–L3 lines on the surface and labels each (V, L) "
                  "column with its paper count, hollow dots marking 0. Because a mean surface hides the spread, the "
                  "quantile view adds each level's 25–75% openness band and median. The floor right of the dashed "
                  "line is strong verification (V3–V4).",
                  "fig_ovl_surface.py (matplotlib mplot3d; Nadaraya–Watson surface); every count is in "
                  "derived/ovl_cube_counts.csv.",
                  ["fig_ovl_surface.py"], ["fig_ovl_surface", "fig_ovl_surface_cut", "fig_ovl_surface_quantiles", "fig_ovl_surface_fields"],
                  "python3 fig_ovl_surface.py --all", extra=["derived/ovl_cube_counts.csv"]),
             form("mountain_surface_3d_by_field", "The mountain for each field (3D)",
                  "The same surface and scatter for each field 01–11, one figure per field. A cross-field paper counts "
                  "in every field it belongs to (935 paper–field assignments).",
                  "fig_ovl_surface.py.", ["fig_ovl_surface.py"], [f"fig_ovl_surface_f{i:02d}" for i in range(1, 12)],
                  "python3 fig_ovl_surface.py --all", extra=["derived/ovl_cube_counts.csv"]),
         ]),
    dict(folder="02_cross_domain_structure", title="Cross-domain structure",
         claim="Each paper's scientific-object classification is archived and may span several fields, under a "
               "three-level code (taxonomy; team discussion).",
         verdict="Descriptive",
         analysis="198 of 662 papers sit in two or more fields, giving 422 field pairs. The strongest ties are Life "
                  "sciences–Medicine (64), Chemistry–Materials (46), Chemistry–Medicine (24) and Materials–Life (18). "
                  "Cross-field pairs grow 11, 5, 16, 98 and 292 across the eras; their LLM-driven share goes 0%, 20%, "
                  "75%, 74% and 93%.",
         limits="Two assignments lack second- or third-level codes.",
         forms=[
             form("atlas_ring", "Hierarchical edge-bundling ring (reference figure)",
                  "Rings, from inside out: 173 third-level categories, 42 second-level categories, 11 fields; arc "
                  "length is proportional to assignments. Each of the 422 curves joins the two categories of one paper "
                  "in two fields; curves are bundled and coloured by decision mechanism.",
                  "fig_atlas.py; hierarchical edge bundling with clamped cubic B-splines.",
                  ["fig_atlas.py"], ["fig_atlas"], "python3 fig_atlas.py"),
             form("wormhole_45", "3D wormhole at 45° (the atlas along a time axis)",
                  "The atlas ring is repeated per era (2004–2019 … 2026) along a 3D time axis, viewed at 45°. Each ring "
                  "has a radius proportional to the square root of that era's assignments and holds that era's "
                  "cross-field curves. Each dot sits on an autonomy track (L0 innermost, L3 at the rim). Translucent "
                  "curtains carry each field's arc from era to era.",
                  "fig_wormhole.py --view=diag45; perspective projection with auto-fit.",
                  ["fig_wormhole.py"], ["fig_wormhole_diag45"], "python3 fig_wormhole.py --view=diag45"),
             form("chord", "Chord diagram of field ties",
                  "Each field arc is proportional to its cross-field pair-ends. Ribbons join two fields and are split "
                  "by the decision mechanism of the papers they share.",
                  "cover_chord.py.", ["cover_chord.py"], ["cover_chord"], "python3 cover_chord.py"),
             form("upset", "UpSet plot of exact field combinations",
                  "Each column is one exact set of fields held by at least two cross-field papers; bars are stacked by "
                  "decision mechanism. Life × Medicine is the largest combination (48 papers).",
                  "fig_upset.py.", ["fig_upset.py"], ["fig_upset"], "python3 fig_upset.py"),
             form("pair_matrix", "Clustered domain-pair matrix",
                  "Upper triangle: papers shared by each pair (circle area). Lower triangle: Jaccard overlap. Diagonal: "
                  "papers per field. Order: average-linkage clustering on 1 − Jaccard.",
                  "fig_matrix.py.", ["fig_matrix.py"], ["fig_matrix"], "python3 fig_matrix.py"),
         ]),
    dict(folder="03_problem_leaderboard", title="Problem leaderboard",
         claim="Field problems with links and solution status, as hard material (survey meeting, 2026-11-03).",
         verdict="Hard material, every row linked",
         analysis="Within each field, papers are ranked by verification strength (V3–V4 first), then autonomy (L3 "
                  "first), then the earliest year. The Robot Scientist (2004, V3, L3) leads overall. 417 of 662 "
                  "papercards state the problem explicitly, quoted verbatim in LEADERBOARD.md.",
         limits="Status is the paper's self-reported verification strength, not an adjudicated 'solved'.",
         forms=[
             form("poster", "Leaderboard of strongly verified work (A4 poster)",
                  "Top four entries per field, each with system, year, link, a status badge (strong / computed / "
                  "benchmark / claim) and an autonomy badge.",
                  "notes_extract.py then art_leaderboard.py.", ["notes_extract.py", "art_leaderboard.py"],
                  ["art_leaderboard"], "python3 art_leaderboard.py",
                  extra=["derived/LEADERBOARD.md", "derived/leaderboard.csv"]),
             form("interactive_html", "Interactive leaderboard (standalone HTML, works offline)",
                  "One HTML file with all 662 papers embedded. It has headline figures, a status-by-field chart (click "
                  "to filter), filters and search, and a sortable table with per-field rank, status, autonomy, "
                  "mechanism, the verbatim problem statement and a live link.",
                  "make_leaderboard_html.py.", ["make_leaderboard_html.py"], [], "python3 make_leaderboard_html.py",
                  extra=["out/agent_science_leaderboard.html", "artifact/agent_science_leaderboard.csv"]),
         ]),
    dict(folder="04_growth", title="Growth of scientific agents",
         claim="Work described as scientific agents has grown sharply since 2024 (§1).", verdict="Supported",
         analysis="Papers per era are 30, 43, 55, 153 and 381. LLM-driven systems rise to 91% of 2026 papers; "
                  "81% of LLM-driven papers are preprints, against 22% of all others.",
         limits="2026 is incomplete (cut-off 22 Oct 2026).",
         forms=[
             form("tree_rings", "Tree rings (eras × fields)",
                  "Rings are eras, from 2004–2019 at the core to 2026 outermost; each annulus has area proportional to "
                  "its assignments. Sectors are fields; each dot is one assignment. " + LEG,
                  "cover_rings.py.", ["cover_rings.py"], ["cover_rings"], "python3 cover_rings.py"),
             form("strata_overview", "Strata overview (dot piles with composition strips)",
                  "Each dot is one paper–field assignment, hex-packed per field × era, with mechanism and venue strips "
                  "below.",
                  "build_data.py then make_figure.py.", ["make_figure.py"], ["main_figure"], "python3 make_figure.py"),
         ]),
    dict(folder="05_two_instruments", title="Two instruments, and a third",
         claim="Announcement and benchmark score are unreliable instruments; the problems actually solved, on what "
               "evidence, are the third (§1).", verdict="Supported as a corpus trend",
         analysis="Across the five eras, the preprint share goes 0%, 10%, 50%, 64% and 82%, and the share validated on "
                  "a benchmark goes 3%, 5%, 40%, 65% and 73%. Meanwhile strong verification goes 67%, 93%, 36%, 23% "
                  "and 9%. There are 65 benchmark or evaluation papers, 56 of them from 2026.",
         limits="Venue is not peer-review status; V is self-reported.",
         forms=[
             form("ternary_drift", "Ternary drift of each field's evidence mix",
                  "Each point is one field's mix in one era within the simplex of V0–V1, V2 and V3–V4, joined in time "
                  "order. The gold arrows trace the whole corpus.",
                  "art_ternary.py.", ["art_ternary.py"], ["art_ternary"], "python3 art_ternary.py"),
             form("instrument_panel", "The instrument panel",
                  "Three dials with one needle per era: preprint share, benchmark share and strong-verification share.",
                  "art_gauges.py.", ["art_gauges.py"], ["art_gauges"], "python3 art_gauges.py"),
             form("benchmark_shelf", "Sixty-five new rulers",
                  "Every benchmark or evaluation paper as a named spine, bookended by year. The cap gives the paper's own "
                  "verification strength.",
                  "art_shelf.py.", ["art_shelf.py"], ["art_shelf"], "python3 art_shelf.py"),
         ]),
    dict(folder="06_separate_axes", title="Every result gets a coordinate",
         claim="Separated, a result has a coordinate comparable with another (§2(1)).",
         verdict="Supported",
         analysis="In 2004–2019, 63% of papers sit at (L2, V3) and in 2020–2023, 91% do: closed-loop systems with physical "
                  "experiments. By 2026 the largest cells are (L2, V2) at 43% and (L2, V1) at 18%.",
         limits="L0 is empty in this corpus.",
         forms=[form("glass_plates", "Isometric glass plates (era × autonomy × verification)",
                     "One plate per era, stacked in time; on each, a grid of autonomy L0–L3 against verification V0–V4. "
                     "Each dot is a paper at its coordinate. " + LEG,
                     "art_lattice.py.", ["art_lattice.py"], ["art_lattice"], "python3 art_lattice.py")]),
    dict(folder="07_autonomy_vs_verification", title="Autonomy and verification",
         claim="Autonomy and verification run opposite: the more autonomous the system, the less often its result is "
               "strongly verified (§2(2)).",
         verdict="Partly supported: true from L2 to L3, not across all levels",
         analysis="Strong verification is 1% at L1, 31% at L2 and 25% at L3 (Spearman ρ = 0.37 over all papers). The "
                  "sharper contrast is mechanism. Over 2024–2026, LLM-driven papers reach V3–V4 in 7.9% of cases "
                  "(39/495), against 53.2% (50/94) for all other mechanisms; over the whole corpus, optimisation "
                  "reaches 83%, symbolic/planning 55%, hybrid 21% and LLM-driven 8%.",
         limits="L3 = 12 papers; mechanism and era are confounded.",
         forms=[
             form("constellation", "Constellation (mechanism sectors × autonomy rings)",
                  "Sectors are decision mechanisms (small ones widened, true counts printed). Rings are autonomy L1–L3, "
                  "and each star is a paper. " + LEG,
                  "cover_constellation.py.", ["cover_constellation.py"], ["cover_constellation"],
                  "python3 cover_constellation.py"),
             form("bars_and_ci", "Verification mix by autonomy, with stratified intervals",
                  "a, Verification mix at each autonomy level, with n. b, Strong-verification share by autonomy within "
                  "2024–2026, for LLM-driven and other mechanisms, with Wilson 95% CIs (hollow = n < 10).",
                  "fig_reach.py; scipy spearmanr with a 2,000-sample bootstrap.", ["fig_reach.py"], ["fig_reach"],
                  "python3 fig_reach.py"),
         ]),
    dict(folder="08_evidence_over_time", title="Evidence thins over time",
         claim="Case counts rise quickly while the evidence behind 'solved' weakens (§2(2)).", verdict="Supported",
         analysis="Strong verification falls from 67% (2004–2019) and 93% (2020–2023) to 36%, 23% and 9% in 2024–2026, "
                  "while weak papers (V0–V1) rise 0, 1, 18, 48 and 130. This mirrors the proposal's 0/1/4/13 and 5/7 → "
                  "12/41.",
         limits="2026 is incomplete.",
         forms=[
             form("sunflower", "Sunflower of the record (phyllotaxis)",
                  "All 662 papers in golden-angle phyllotaxis, oldest at the centre; the labels give each era's "
                  "strong-verification share. " + LEG,
                  "cover_sunflower.py.", ["cover_sunflower.py"], ["cover_sunflower"], "python3 cover_sunflower.py"),
             form("river_and_ci", "Evidence river with stratified intervals",
                  "a, River of papers per era by verification tier. b, Strong-verification share per era (Wilson 95% "
                  "CI), for all papers and within LLM-driven and optimisation papers.",
                  "fig_thinning.py.", ["fig_thinning.py"], ["fig_thinning"], "python3 fig_thinning.py"),
         ]),
    dict(folder="09_chronicle_status", title="Survey completed: two ledgers",
         claim="Status across the 84 coded cases; contested and refuted cases are kept (§2(2)).",
         verdict="Shown as reported (84 cases) and as archived (1,133 records)",
         analysis="The ledger holds 1,133 records: 662 core, 382 background, 29 pending, 31 duplicates and 29 excluded. "
                  "The chronicle's status counts (63/10/10/1) are quoted from the proposal.",
         limits="The right-hand mosaic reproduces the proposal's reported numbers.",
         forms=[form("mosaic", "Mosaic of every ledger record",
                     "Every ledger record as a tile, grouped by status; core papers lit by mechanism, with a white centre "
                     "for strong verification. Right: the proposal's 84 cases by reported status.",
                     "art_mosaic.py.", ["art_mosaic.py"], ["art_mosaic"], "python3 art_mosaic.py")]),
    dict(folder="10_frontier", title="A checkable frontier",
         claim="With openness on the vertical axis and time on the horizontal, the boundary of problem classes with at "
               "least one strongly verified solution can be drawn era by era (§2(3)(i), Fig. 1).",
         verdict="Demonstrated on the coded axes",
         analysis="By 2026, Physics, Chemistry, Materials and Life sciences hold strongly verified work at O6. "
                  "Formal sciences, Agriculture and Engineering reach O5, Medicine O4, and Earth and Aerospace only O3. "
                  "Social & knowledge systems has no strongly verified paper at any openness.",
         limits="A blank means no V3–V4 paper in this corpus.",
         forms=[
             form("landscape", "Frontier landscape (land and water)",
                  "Columns are fields and altitude is openness O1–O6. Land marks openness reached by at least one "
                  "strongly verified paper, cumulative with one shade per era; water marks openness attempted but not yet "
                  "strongly verified. Points: ink = V3–V4, grey = V2, open = V0–V1.",
                  "fig_frontier.py.", ["fig_frontier.py"], ["fig_frontier"], "python3 fig_frontier.py"),
             form("bloom", "Frontier bloom (polar petals)",
                  "Each field is a petal with radius O1 (centre) to O6 (rim). Each era adds one translucent layer marking "
                  "openness reached with strong verification; the outline marks the highest openness attempted. " + LEG,
                  "cover_bloom.py.", ["cover_bloom.py"], ["cover_bloom"], "python3 cover_bloom.py"),
         ]),
    dict(folder="11_located_blanks", title="Located blanks",
         claim="Unsolved problems per field are where no strongly verified case yet exists at high openness (§2(3)(ii)).",
         verdict="Demonstrated on the coded axes",
         analysis="23 field × openness cells are attempted without any strongly verified paper. O2 benchmark cells are "
                  "gaps almost everywhere, and O6 is a gap in Formal, Earth, Medicine and Social systems.",
         limits="A gap means no V3–V4 paper in this corpus, not that none exists.",
         forms=[form("periodic_table", "A periodic table of the frontier",
                     "Columns are fields and rows are openness O1–O6. A tile is filled when a paper in the cell is "
                     "strongly verified, its tone giving the era of the first one; '?' tiles were attempted but never "
                     "strongly verified.",
                     "art_periodic.py.", ["art_periodic.py"], ["art_periodic"], "python3 art_periodic.py")]),
    dict(folder="12_frontier_rate", title="A rate that can be computed",
         claim="How far the frontier advanced per era, which fields moved fastest and which have not moved (§2(3)(iii)).",
         verdict="Demonstrated on the coded axes",
         analysis="The frontier steps (first strongly verified paper at a new highest openness) are as follows. Life "
                  "sciences reached O6 in 2004. Chemistry went O3 in 2014 and O6 in 2018; Materials O4 in 2020 and O6 in "
                  "2022; Physics O6 in 2022. Engineering went O4 in 2020 and O5 in 2025; Formal O3 in 2024 and O5 in "
                  "2025; Medicine O4 in 2025. Earth (O3 since 2005) and Aerospace (O3 since 2004) have not moved in "
                  "twenty years.",
         limits="Bibliographic year may be a later version of the work.",
         forms=[form("pulsar_ridgelines", "Pulsar ridgelines (after PSR B1919+21)",
                     "One ridge per field shows papers per year on a common scale; gold ticks mark each step of that "
                     "field's strongly verified frontier in openness.",
                     "art_pulsar.py.", ["art_pulsar.py"], ["art_pulsar"], "python3 art_pulsar.py")]),
    dict(folder="13_provenance", title="A record that can be re-checked",
         claim="Each assignment carries an independent source; entries without one are flagged (§2(3)(iv)).",
         verdict="Supported",
         analysis="All 662 papercards and 635 claimed PDFs exist in the repository. Every O and V label quotes the "
                  "papercard verbatim with its line number, checked by script (662/662).",
         limits="Provenance covers classification, not the correctness of each result.",
         forms=[
             form("ledger_barcode", "Papercard ledger (barcode)",
                  "One column per cross-field paper: field memberships, then the provenance trail.",
                  "fig_ledger.py.", ["fig_ledger.py"], ["fig_ledger"], "python3 fig_ledger.py"),
             form("genome_ring", "Papercard genome (circular tracks)",
                  "All 662 papers as radial slots: 11 field tracks lit by mechanism, then evidence, PDF, note and "
                  "confidence tracks.",
                  "cover_genome.py.", ["cover_genome.py"], ["cover_genome"], "python3 cover_genome.py"),
         ]),
    dict(folder="14_where_experts_are_needed", title="Where domain scientists are needed",
         claim="Four judgements need a domain expert: the V3/V2 boundary, the actual AI contribution, whether an O6 blank "
               "is real, and contested cases (§3).",
         verdict="Queue sized from the corpus",
         analysis="149 papers claim strong verification (V3–V4) that an expert must confirm, 12 are L3 systems whose "
                  "actual AI contribution needs checking, and 126 sit in the coding review queue. Materials (77) and "
                  "Chemistry (48) carry by far the largest queues, then Life sciences (28): each exceeds the proposal's "
                  "15–20 cases per field.",
         limits="Queues overlap.",
         forms=[form("nightingale_rose", "Nightingale rose of the review queue",
                     "One petal per field with four stacked layers (area proportional to papers); rings mark the "
                     "proposal's 15 and 20 cases per field.",
                     "art_rose.py.", ["art_rose.py"], ["art_rose"], "python3 art_rose.py")]),
    dict(folder="15_three_month_plan", title="The three-month plan",
         claim="AI screening, then expert review, then a dictionary of problems (§5).",
         verdict="Stage 1 done; stages 2–3 planned",
         analysis="All 662 core papers are coded on the three axes. 158 need an expert judgement (strong verification "
                  "or L3 autonomy), against a planned capacity of 11 × 15–20 = 165–220 cases.",
         limits="The bottom bulb shows planned capacity.",
         forms=[form("hourglass", "An hourglass of judgement",
                     "Top: the 662 coded papers. Neck: those needing an expert judgement. Bottom: the planned 220 "
                     "expert slots, empty. " + LEG,
                     "art_hourglass.py.", ["art_hourglass.py"], ["art_hourglass"], "python3 art_hourglass.py")]),
]
