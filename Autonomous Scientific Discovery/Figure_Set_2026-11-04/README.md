# Agent-for-Science figure set

662 core papers · snapshot 2026-11-01 · decision mechanisms 2026-11-03 · repository commit 60f8bad.

Figures for *From Computable Tasks to Open Science: A Chronicle of AI Problem Solving*, built from the classified literature corpus. Folders are organised as **content → presentation form → version**, and every folder has a README. `Figure_Tech_Report.pdf` collects every figure with its caption, generation method and analysis; its table of contents mirrors this tree.

| Content | Forms | Verdict on the proposal claim |
|---|---|---|
| `01_three_axes/` The three axes: openness × verification × autonomy | `curtains_3d`, `mountain_surface_3d`, `mountain_surface_3d_by_field` | Axes separate cleanly; the opposition holds only from L2 to L3 |
| `02_cross_domain_structure/` Cross-domain structure | `atlas_ring`, `wormhole_45`, `chord`, `upset`, `pair_matrix` | Descriptive |
| `03_problem_leaderboard/` Problem leaderboard | `poster`, `interactive_html` | Hard material, every row linked |
| `04_growth/` Growth of scientific agents | `tree_rings`, `strata_overview` | Supported |
| `05_two_instruments/` Two instruments, and a third | `ternary_drift`, `instrument_panel`, `benchmark_shelf` | Supported as a corpus trend |
| `06_separate_axes/` Every result gets a coordinate | `glass_plates` | Supported |
| `07_autonomy_vs_verification/` Autonomy and verification | `constellation`, `bars_and_ci` | Partly supported: true from L2 to L3, not across all levels |
| `08_evidence_over_time/` Evidence thins over time | `sunflower`, `river_and_ci` | Supported |
| `09_chronicle_status/` Survey completed: two ledgers | `mosaic` | Shown as reported (84 cases) and as archived (1,133 records) |
| `10_frontier/` A checkable frontier | `landscape`, `bloom` | Demonstrated on the coded axes |
| `11_located_blanks/` Located blanks | `periodic_table` | Demonstrated on the coded axes |
| `12_frontier_rate/` A rate that can be computed | `pulsar_ridgelines` | Demonstrated on the coded axes |
| `13_provenance/` A record that can be re-checked | `ledger_barcode`, `genome_ring` | Supported |
| `14_where_experts_are_needed/` Where domain scientists are needed | `nightingale_rose` | Queue sized from the corpus |
| `15_three_month_plan/` The three-month plan | `hourglass` | Stage 1 done; stages 2–3 planned |
| `16_proposal_explainer_video/` Proposal explainer video | 1080p and 480p MP4, HyperFrames source | Walkthrough of the proposal, 14 scenes, Mandarin narration |

## Tree

```
01_three_axes/
  curtains_3d/
    white/
  mountain_surface_3d/
    white/
  mountain_surface_3d_by_field/
    white/
02_cross_domain_structure/
  atlas_ring/
    white/
  wormhole_45/
    white/
  chord/
    white/
  upset/
    white/
  pair_matrix/
    white/
03_problem_leaderboard/
  poster/
    white/
  interactive_html/
    white/
04_growth/
  tree_rings/
    white/
  strata_overview/
    white/
05_two_instruments/
  ternary_drift/
    white/
  instrument_panel/
    white/
  benchmark_shelf/
    white/
06_separate_axes/
  glass_plates/
    white/
07_autonomy_vs_verification/
  constellation/
    white/
  bars_and_ci/
    white/
08_evidence_over_time/
  sunflower/
    white/
  river_and_ci/
    white/
09_chronicle_status/
  mosaic/
    white/
10_frontier/
  landscape/
    white/
  bloom/
    white/
11_located_blanks/
  periodic_table/
    white/
12_frontier_rate/
  pulsar_ridgelines/
    white/
13_provenance/
  ledger_barcode/
    white/
  genome_ring/
    white/
14_where_experts_are_needed/
  nightingale_rose/
    white/
15_three_month_plan/
  hourglass/
    white/
16_proposal_explainer_video/
  source/
```

## Rebuild

`code/` holds the runnable copy: MD5-pinned source data, derived tables, all scripts and this builder. Requirements: Python 3 with matplotlib ≥3.10, numpy and scipy; XeLaTeX for the report.

```bash
cd code && python3 build_package.py
```

## Visual references

- **Hierarchical edge bundling, chord, genome rings**: after Circos-style circular data art (M. Krzywinski, Nature journal covers)
- **Cross-domain atlas, wormhole**: after Barabasi Lab co-citation network for Nature's 150th anniversary (2019)
- **Pulsar ridgelines**: after H. Craft's PSR B1919+21 plot (Arecibo), used on Unknown Pleasures (1979)
- **Periodic table with gaps**: after Mendeleev's 1869 table and its predicted eka-elements
- **Review rose**: after F. Nightingale's coxcomb diagrams (1858)
- **Ledger mosaic**: after Tsevis's mosaic covers for Science

## The three axes

All 662 core papers are coded on the proposal's three axes: problem openness O1–O6, verification strength V0–V4 (V3–V4 = strong) and system autonomy L0–L3. The rubric is `code/ov_coding/RUBRIC.md`; labels and evidence quotes are in `code/ov_coding/increment/`. V is the paper's self-reported evidence, not an adjudicated 'solved'.
