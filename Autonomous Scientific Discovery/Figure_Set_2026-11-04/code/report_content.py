"""Single source of text for the figure package: per-folder READMEs and the Tech Report.

Each entry maps one proposal claim to the figure that tests it. Numbers quoted here were
computed from derived/ (snapshot 2026-11-01, mechanism labels 2026-11-03)."""

FIGS = [
    dict(
        id="01", folder="01_frontier", title="The expanding frontier of closed research loops",
        files=["fig_frontier"], script="fig_frontier.py",
        claim="A frontier curve can be checked: with openness on the vertical axis and time on the horizontal, "
              "the boundary of problem classes holding at least one strongly verified solution can be drawn era by "
              "era (proposal §2(3)(i), Fig. 1). Blanks and rates follow from the same table (§2(3)(ii)-(iii)).",
        verdict="Demonstrated with proxies",
        caption="Columns are the 11 fields; altitude is research-loop reach L1-L4, a proxy for how open and how "
                "delegated the problem is. Land marks reach closed by at least one paper whose own validation "
                "includes a physical experiment, clinical data, field deployment or a formal proof (E3). Land is "
                "cumulative, with one shade per era from 2004-2019 (darkest) to 2026 (lightest). Water marks reach "
                "that has been attempted without any E3 endpoint. Each point is one paper-field assignment (n = 895 "
                "with both proxies coded): ink = E3, grey = computational or simulation (E2), open = benchmark, "
                "expert or case evaluation only (E0-E1). The labels along the top give each field's highest "
                "attempted reach that is not yet closed.",
        method="fig_frontier.py reads derived/papercards (via style.papercards) and derived/proxies.csv. For "
               "each field f and era e, frontier(f, e) = max L over papers in f published up to the end of e with "
               "E = 3. The land profile is a per-field step of height LH x frontier, smoothed by a Gaussian "
               "(sigma = 6 samples) for display only. Points are placed by a Halton sequence inside each "
               "field x reach cell and sorted so that E3 points are drawn first.",
        analysis="By the end of 2026, six fields are closed to L4: Formal, Chemistry, Materials, Life sciences, "
                 "Medicine and Engineering. The frontier advanced at very different rates. Chemistry (L3) and Life "
                 "sciences (L3) were already high in 2004-2019. Medicine went from no E3 paper to L4 in 2024. Formal "
                 "sciences climbed L2 to L4 between 2024 and 2026. Earth & environment and Aerospace, marine & "
                 "transport have stayed at L2 since 2004-2019: their closed loops are planning and optimisation "
                 "agents, such as AEGIS and the EO-1 sciencecraft. The unclosed summits are Physics (L4 attempted, "
                 "0 of 4 closed), Earth (0 of 2), Agriculture (0 of 1), Aerospace (0 of 1) and Social & knowledge "
                 "systems (0 of 7). These are the corpus-level analogue of the proposal's located blanks.",
        limits="E3 is self-reported by the paper; it is not the proposal's V3 (which also needs third-party "
               "replication to reach V4) and was not adjudicated by domain experts. L is derived from coded "
               "workflow roles, not from the problem statement, so it mixes openness with autonomy. Named open "
               "problems (Riemann, fusion control, ...) cannot be placed without the 84-case chronicle table.",
    ),
    dict(
        id="02", folder="02_evidence_thinning", title="Evidence thins as the record grows",
        files=["fig_thinning"], script="fig_thinning.py",
        claim="Evidence thins over time: case counts rise quickly while the evidence behind 'solved' weakens "
              "(proposal §2(2), second finding).",
        verdict="Supported; mostly composition-driven",
        caption="a, River of the 642 core papers with a coded validation endpoint, by era. Width is proportional "
                "to the number of papers, and layers run from the E3 core outwards to E2, E1 and E0. The E3 share and "
                "the number of weak papers (E0 + E1) are printed per era. Eras are ordinal and unequal in length. "
                "b, E3 share per era with Wilson 95% intervals, for all papers and within LLM-driven (D5) and "
                "optimisation (D3) papers. Strata with n < 3 are omitted.",
        method="fig_thinning.py; tiers from proxies.py (validation_type, max over values, ambiguous values "
               "assigned to the lower tier). River boundaries are PCHIP-interpolated between era centres.",
        analysis="The E3 share falls monotonically: 93% (28/30) in 2004-2019, 88% (38/43) in 2020-2023, 42% "
                 "(22/53) in 2024, 21% (32/150) in 2025 and 12% (44/366) in 2026. Weak-only papers rise from 1 to 1, "
                 "17, 68 and 121 per era, which mirrors the proposal's 0/1/4/13. Panel b shows where the decline "
                 "comes from. Within LLM-driven papers the E3 share is roughly flat from 2024 (13%, 11%, 10%). "
                 "Within optimisation papers it stays high until 2025 (85%) and drops to 57% (8/14) in 2026. Most "
                 "of the aggregate thinning is therefore a shift in which kind of system is being built, not a "
                 "within-kind decline.",
        limits="Self-reported endpoints; 2026 is incomplete (cut-off 22 Oct 2026); bibliographic year may be a "
               "preprint or a later journal version.",
    ),
    dict(
        id="03", folder="03_reach_vs_evidence", title="Delegated reach versus evidence",
        files=["fig_reach"], script="fig_reach.py",
        claim="Autonomy and verification run opposite: the more autonomous the system, the less often its result "
              "is independently verified (proposal §2(2), first finding). It also bears on the claim that openness, "
              "verification and autonomy are separate axes that are currently conflated (§2(1)).",
        verdict="Opposition not supported; separation supported",
        caption="a, Evidence-endpoint mix for each research-loop reach level (633 papers with both proxies), as "
                "% of papers at that level, with n. b, E3 share by reach within 2024-2026 only, for LLM-driven "
                "papers and all other mechanisms, with Wilson 95% CIs. Hollow markers have n < 10, and the "
                "number above each interval is n. The subtitle gives Spearman rho between reach and evidence tier "
                "with a 2,000-sample bootstrap CI.",
        method="fig_reach.py; proxies from proxies.py; scipy.stats.spearmanr; bootstrap with numpy "
               "default_rng(7).",
        analysis="Reach and evidence are essentially uncorrelated: rho = 0.03, 95% CI -0.05 to 0.12. The E3 "
                 "share is 4.5% at L1, 46.9% at L2, 14.5% at L3 and 20.0% at L4. That is not monotonic: systems "
                 "that design and run experiments (L2) reach physical endpoints most often. With era held fixed "
                 "(2024-2026), the contrast is between mechanisms, not reach levels. LLM-driven papers reach E3 in "
                 "10.6% of cases (50/470), against 53.3% (48/90) for all other mechanisms, at every reach level. "
                 "The proposal's opposition claim (0/12 strong at L3 vs 24/59 at L1, on Wei's autonomy scale) is "
                 "not reproduced by this proxy. The near-zero correlation does support §2(1): knowing how much of "
                 "the loop was delegated says almost nothing about how strongly the result was checked, so the two "
                 "need separate axes.",
        limits="Reach is not Wei's L0-L3 autonomy scale; the chronicle's 84 hand-coded cases may still show the "
               "opposition. This is reported as a negative result under the corpus proxy, not a refutation.",
    ),
    dict(
        id="04", folder="04_strata_overview", title="Strata of autonomous science (overview)",
        files=["main_figure"], script="make_figure.py",
        claim="Work described as 'scientific agents' has grown sharply since 2024 (§1). The two current "
              "instruments, announcement and benchmark, can rise without real progress (§1).",
        verdict="Supported (growth); indicative (instruments)",
        caption="a, Each dot is one paper-field assignment (935). Dots are hex-packed per field x era, and pile "
                "area is proportional to the count. Within each pile, dots are ordered by decision mechanism from "
                "the base upwards (D1/D2/D4, D3, D6, D5). Fill shows the venue: filled for journal or conference, "
                "open for preprint. b, Mechanism share per era. c, Venue share per era. d, Cross-field ties among "
                "198 multi-field papers. e, Field signatures: LLM-driven share against preprint share.",
        method="build_data.py then make_figure.py (self-contained matplotlib, mm coordinates).",
        analysis="Paper counts are 30, 43, 55, 153 and 381 across the five eras. LLM-driven systems rise from "
                 "12% (2020-2023) to 91% (2026) of papers. 81% of LLM-driven papers are preprints, against 22% of "
                 "all others, so the record is increasingly carried by the instrument the proposal flags as "
                 "unreliable: announcement before peer review.",
        limits="Venue is not peer-review or verification status. 2004-2019 spans 16 years and is plotted as one "
               "era.",
    ),
    dict(
        id="05", folder="05_cross_domain_atlas", title="Cross-domain atlas",
        files=["fig_atlas", "fig_atlas_dark"], script="fig_atlas.py",
        claim="Each paper's scientific-object classification is archived and may span several fields, under a "
              "three-level code: field, second level, third level (team discussion; taxonomy file).",
        verdict="Descriptive",
        caption="The rings, from inside out, are 173 third-level categories, 42 second-level categories and 11 "
                "fields, with arc length proportional to assignments. Inner-ring tone gives the share of a "
                "category's papers that are cross-field. Each of the 422 curves joins the two third-level "
                "categories of one paper in two fields. Curves are routed through the hierarchy, bundled (beta = "
                "0.82) and coloured by decision mechanism. A dark variant is provided for cover or poster use.",
        method="fig_atlas.py [--dark]; hierarchical edge bundling with clamped cubic B-splines (scipy BSpline).",
        analysis="Cross-field work concentrates in two bundles: Life sciences-Medicine and Chemistry-Materials. "
                 "Optimisation-driven curves run between Chemistry, Materials and Earth/Aerospace; the rest are "
                 "overwhelmingly LLM-driven. Eight papers span 5 or more fields, led by ASD-0940 OmniScientist "
                 "(k = 10).",
        limits="Two assignments lack second/third-level codes and sit in a placeholder leaf.",
    ),
    dict(
        id="06", folder="06_field_combinations_upset", title="Which fields does one paper span? (UpSet)",
        files=["fig_upset"], script="fig_upset.py",
        claim="The cross-domain situation of the same paper can be shown across the 11 fields (team discussion).",
        verdict="Descriptive",
        caption="Each column is one exact set of fields held by at least 2 of the 198 cross-field papers. The "
                "other 32 papers each have a unique combination and are pooled at right. Bars are stacked by "
                "decision mechanism. The left bars show each field's assignments, split into cross-field and "
                "single-field.",
        method="fig_upset.py.",
        analysis="Life x Medicine is the largest combination (48 papers, 98% LLM-driven), followed by "
                 "Chemistry x Materials (28, 68% LLM-driven). Earth x Aerospace (12) is the only leading "
                 "combination with no LLM-driven paper.",
        limits="Multi-field assignment depends on the classification rules (object-first) documented in the "
               "repository.",
    ),
    dict(
        id="07", folder="07_domain_pair_matrix", title="Domain-pair matrix",
        files=["fig_matrix"], script="fig_matrix.py",
        claim="Same as 06, at pair level; this figure also corrects the circulated infographic's node counts.",
        verdict="Descriptive",
        caption="Fields are ordered by average-linkage clustering on 1 - Jaccard. The upper triangle shows papers "
                "shared by each pair as circle area plus count. The lower triangle shows Jaccard overlap on a "
                "one-hue ramp. The diagonal gives papers per field, with an arc for the share in 2 or more fields.",
        method="fig_matrix.py; scipy.cluster.hierarchy.linkage(method='average').",
        analysis="Three clusters emerge: Earth-Aerospace (with Agriculture); Life-Medicine-Chemistry-Materials; "
                 "and Formal-Social-Physics-Engineering. The strongest pairs are 06-07 (64), 03-04 (46), 03-07 (24) "
                 "and 04-06 (18).",
        limits="Jaccard is sensitive to field size; counts are shown alongside for that reason.",
    ),
    dict(
        id="08", folder="08_papercard_ledger", title="Papercard ledger",
        files=["fig_ledger"], script="fig_ledger.py",
        claim="A record that can be re-checked: each level assignment carries at least one independent source; "
              "entries without one are flagged (proposal §2(3)(iv)). Also: is there a mechanism that keeps the "
              "content from being hallucinated? (team discussion).",
        verdict="Supported for classification provenance",
        caption="One column per cross-field paper. The upper block shows field memberships coloured by decision "
                "mechanism. The lower block shows the provenance trail from the same papercard: era, venue, note "
                "present in the repository, PDF archived, source level read for coding, mechanism confidence, and "
                "whether the mechanism label was checked on the PDF. Totals are at right.",
        method="fig_ledger.py; note and PDF existence checked against the file list of commit 60f8bad "
               "(source_data/repo_tree_60f8bad.txt).",
        analysis="All 662 core notes and all 635 claimed PDFs exist in the commit. For the 198 cross-field papers: "
                 "195 have archived PDFs; 190 were coded from full text, 7 from abstract or official pages and 1 "
                 "is source-limited; mechanism confidence is 165 high, 29 medium and 4 low; 29 mechanism labels were "
                 "checked against the PDF. This makes every classification mark traceable. It does not make the "
                 "papers' scientific claims verified.",
        limits="Provenance covers classification, not the correctness of each paper's results.",
    ),
]

NOT_TESTABLE = [
    ("Verified 63 / claimed 10 / contested 10 / refuted 1 status (§2(2))",
     "No status coding exists in the 662-paper corpus."),
    ("Third-party replication (V4) and the V3/V2 boundary (§3)",
     "Needs domain experts reading original evidence; E3 is self-reported."),
    ("The actual AI contribution vs human-supplied candidates (§3)", "Not coded corpus-wide."),
    ("Named O6 blanks (Riemann, P vs NP, fusion, origin of life, ...) (§2(3)(ii))",
     "Requires the 84-case chronicle table with problem statements."),
]
