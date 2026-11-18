# Figure set — Agent for Science core corpus

There are five standalone figures, each in its own visual register, plus the earlier "Strata" overview. They all read the same papercard ledger (`derived/papercards.csv`), so every dot, bar, curve and number traces to an `ASD-xxxx` record with a note and, for 635/662 papers, an archived PDF.

| File | Style | Question it answers |
|---|---|---|
| `out/fig_atlas.pdf` | Hierarchical edge bundling, print | How does one paper connect sub-fields across the three-level taxonomy? |
| `out/fig_atlas_dark.pdf` | Same, dark cover-art variant | (as above; for cover, slides or poster) |
| `out/fig_upset.pdf` | UpSet (Nature Methods idiom) | Which exact field combinations do papers span? |
| `out/fig_matrix.pdf` | Clustered bubble/Jaccard matrix | How strongly does each pair of fields overlap? |
| `out/fig_ledger.pdf` | Barcode ledger | What evidence backs each cross-field mark? |
| `out/main_figure.pdf` | Stratigraphic dot piles | How did fields, mechanisms and venues shift over time? |

To rebuild, run these after `build_data.py`:

```bash
python3 style.py
```

```bash
python3 fig_atlas.py
```

```bash
python3 fig_atlas.py --dark
```

```bash
python3 fig_upset.py
```

```bash
python3 fig_matrix.py
```

```bash
python3 fig_ledger.py
```

### How the set guards against hallucinated content

1. **No hand-entered numbers.** Every count is computed from the three source files, pinned by MD5 (below).
2. **Papercard existence check.** `style.py` matches every `note_path`/`pdf_path` against the file list of commit `60f8bad` (`source_data/repo_tree_60f8bad.txt`). Result: 662/662 notes and 635/635 claimed PDFs present.
3. **Code reconciliation.** Each paper's field list equals the field set of its taxonomy assignments for 662/662 papers. Pairs total 422 and assignments 935, matching the repository's own figures.
4. **Provenance on the page.** `fig_ledger` prints, for each cross-field paper:
   - whether its note and PDF exist;
   - what level of source was read for coding;
   - the mechanism-label confidence;
   - whether that label was checked against the PDF.

**Errors found in the circulated "科学智能体跨域结构信息图" against this snapshot.** Its pair counts are correct: 06–07 = 64, 03–04 = 46, 03–07 = 24, 01–11 = 15, 422 pairs in total. Several node values are not:

| Field | Infographic | Snapshot |
|---|---|---|
| 04 Materials | 120 | 172 |
| 05 Earth & environment | 58 | 52 |
| 08 Agriculture & food | 70 | 9 |
| 09 Engineering & industry | 67 | 62 |
| 11 Social & knowledge systems | 69 | 68 |
| Multi-field share, 02 Physics | 13.4% | 40.2% |
| Multi-field share, 11 Social | 58.3% | 36.8% |
| Multi-field share, 01 Formal | 38.4% | 40.4% |
| Multi-field share, 07 Medicine | 62.1% | 66.1% |

That infographic should not be circulated as it stands.

### Captions

**Cross-domain atlas (`fig_atlas`, `fig_atlas_dark`).**
- **Rings:** from inside out, the 173 third-level categories, the 42 second-level categories and the 11 fields. Arc length is proportional to paper–field assignments (935).
- **Inner-ring tone:** the share of a third-level category's papers that are assigned to ≥2 fields.
- **Curves:** each of the 422 curves joins the two third-level categories of one paper in two different fields. It is routed through the second-level and field nodes and the centre, then bundled (β = 0.82). Colour gives that paper's decision mechanism.
- **Right column:** breadth distribution (k fields per paper) and the eight broadest papers by ID.
- The dense bundles are Life sciences ↔ Medicine and Chemistry ↔ Materials. Optimization-driven curves (orange) concentrate between Chemistry, Materials and Earth/Aerospace.

**Field combinations (`fig_upset`).**
- **Columns:** each column is one exact set of fields held by ≥2 of the 198 cross-field papers. The remaining 32 papers, each in a combination of its own, are pooled at right.
- **Bars:** stacked by decision mechanism.
- **Left bars:** each field's assignments, split into those in cross-field papers and single-field ones.
- **Key combinations:**
  - Life × Medicine is the largest combination (48 papers, 98% LLM-driven).
  - Chemistry × Materials follows (28 papers, 68% LLM-driven, the rest mostly optimization).
  - Earth × Aerospace (12) is the only leading combination with no LLM-driven papers.

**Domain-pair matrix (`fig_matrix`).**
- **Ordering:** fields are ordered by average-linkage clustering on 1 − Jaccard.
- **Upper triangle:** circle area is proportional to papers shared by the two fields, and the number is the count.
- **Lower triangle:** Jaccard overlap, |A∩B| / |A∪B|, on a one-hue ramp capped at 0.3.
- **Diagonal:** papers per field, with an arc for the share in ≥2 fields.
- **Clusters:** three emerge: Earth–Aerospace (with Agriculture), Life–Medicine–Chemistry–Materials, and Formal–Social–Physics–Engineering.

**Papercard ledger (`fig_ledger`).**
- **Columns:** one per cross-field paper, sorted by number of fields and then by field set.
- **Upper block:** field memberships, coloured by decision mechanism.
- **Lower block:** the provenance trail from the same papercard, with per-row totals at right:
  - era;
  - recorded venue;
  - note present in the repository (198/198);
  - PDF archived (195/198);
  - source level read for coding (190 full text, 7 abstract or official pages, 1 source-limited);
  - mechanism-label confidence (165 high, 29 medium, 4 low);
  - whether the mechanism label was checked on the PDF (29).

---

# Main figure — Strata of autonomous science

`out/main_figure.pdf` (vector, fonts embedded) · `out/main_figure.svg` · `out/main_figure.png` (600 dpi). 183 × 211 mm, Nature double-column width.

## Caption

**Fig. 1 | Strata of autonomous science: how 662 agent-for-science studies accumulated across eleven scientific fields, and how their decision mechanism and venue shifted.**
**a**, Each dot is one paper–field assignment (935 assignments from 660 papers; cross-field papers appear once per field). Within each field (rows) and era (columns), dots are hex-packed into a pile whose area is proportional to the number of assignments. Inside a pile they are ordered from the base upwards by decision mechanism: symbolic/planning/learned-policy (D1, D2, D4), then optimization/probabilistic (D3), then hybrid (D6), then LLM-driven (D5). Older paradigms therefore form the base of each pile and LLM-driven work its cap. Filled dots are records with a journal or conference venue, open rings are preprints and tinted dots have an unknown venue. Ringed dots mark milestone systems discussed in the text. Era columns have equal width but unequal duration (2004–2019 spans 16 years; 2026 runs to the search cutoff of 22 October 2026), so read across the columns as ordered eras, not as a linear time axis. *n*, assignments per field.
**b**, Decision-mechanism composition of all 662 papers per era (% of papers). Symbolic and planning agents (53%) and optimization (43%) dominate 2004–2019; closed-loop optimization dominates 2020–2023 (77%); LLM-driven systems rise to 60%, 76% and 91% of papers in 2024, 2025 and 2026.
**c**, Venue composition per era. Journals and conferences carry the early record (2004–2019: 60% and 40%; 2020–2023: 88% journal). Preprints account for 49%, 63% and 82% of papers from 2024 onwards.
**d**, Cross-field ties among the 198 papers assigned to two or more fields. Ribbon width is proportional to the number of shared papers, and node area to the field's assignments. The strongest ties are life sciences–medicine (64), chemistry–materials (46), chemistry–medicine (24) and materials–life sciences (18).
**e**, Field signatures: the share of a field's papers that are LLM-driven against the share recorded as preprints. Bubble area is proportional to the field's papers, and darker fill means a larger share published before 2024. Grey lines mark corpus-wide values (76% LLM-driven; 67% preprint among papers with a known venue). Of the LLM-driven papers, 81% are preprints, against 22% of all other papers. Chemistry and Earth & environment coincide (67%, 58%). Aerospace, marine & transport is the outlier: it is dominated by pre-2024 planning agents, 11% LLM-driven and 19% preprint.
Data: core snapshot of 1 November 2026 and decision-mechanism classification of 3 November 2026 (one primary label per paper; 522/126/14 high/medium/low confidence; 15 provisional). Mechanism labels describe the dominant decision mechanism as coded from notes and, for 83 papers, primary sources. Venue classes come from the recorded `source` string (rules below) and do not certify peer-review status. Bibliographic years can be preprint, conference or journal versions. Counts describe this corpus, not global publication volume.

## What it shows, compared with the earlier version

The earlier landscape plotted *time × venue × field*, with venue encoded as small marker shapes. This version:

1. **Adds the decision-mechanism axis (D1–D6)** as the primary color, so the transition from planning and optimization to LLM agents is visible inside every field.
2. **Makes counts honest and legible.** Pile area is proportional to n, every paper stays visible, and the stratigraphic ordering turns each pile into a stacked composition.
3. **Encodes venue as fill vs ring**, which reads at dot size where shapes do not, and summarizes it quantitatively in strip **c**.
4. **Adds two analytical panels.** Panel **d** shows where cross-field work concentrates. Panel **e** shows the coupling between LLM-driven methods and preprint dissemination (81% vs 22%), which is the corpus-level evidence trend behind the proposal's claim that "evidence thins over time".

### Relation to the proposal's frontier figure
The proposal's main figure needs **problem openness (O1–O6)** and **verification strength (V0–V4)**. Neither is coded for this 662-paper corpus: the repository states it "does not have corpus-wide coding of problem openness, scientific verification strength or solved status", and no such coding was found on H20. This figure therefore does **not** draw a solved-problem frontier. Venue class in **c**/**e** is a coarse proxy for dissemination, not verification. Once the 84 coded chronicle cases (O, V, autonomy) are available as a table, they can be overlaid on panel **a** as a sixth layer, for example a V≥3 halo on the matching dots.

## Encoding and color

| Channel | Meaning |
|---|---|
| Dot color | Decision mechanism: classical D1/D2/D4 `#a8326e`, optimization D3 `#d9622b`, hybrid D6 `#1a9b74`, LLM-driven D5 `#2f5fb3` |
| Fill vs ring | Journal or conference (filled) vs preprint (ring); tint = unknown venue |
| Pile area | Number of paper–field assignments in that field × era |
| Vertical order in pile | Mechanism strata (classical → optimization → hybrid → LLM), then venue, year, ID |
| Sand ridges | Smoothed envelope of the piles; lighter for upper rows (aerial perspective, decorative only) |

The four mechanism colors pass every check of the dataviz palette validator under all-pairs comparison: worst CVD ΔE 9.9, normal-vision ΔE 18.5, all ≥3:1 contrast. Venue uses an ink/grey/white ramp so it never competes with mechanism color.

## Venue-class rules (`build_data.py`)

Applied to the manifest `source` column in this order:
1. `Unknown` → unknown.
2. A conference, proceedings, workshop or named venue (ICLR, ICML, NeurIPS, AAAI, IJCAI, ACL/EMNLP, KDD, ICRA, i-SAIRAS, SpaceOps, PMLR, OpenReview poster, …) → conference. This includes records co-listed with arXiv.
3. arXiv, bioRxiv, medRxiv, ChemRxiv, Research Square, SSRN or "preprint" → preprint, including PMC mirrors of bioRxiv/medRxiv.
4. Everything else → journal, including two records co-listed with arXiv (JCIM, Science China).

Result: 183 journal, 36 conference, 438 preprint and 5 unknown.

## Reproduce

```bash
python3 build_data.py
```

```bash
python3 make_figure.py
```

`source_data/` holds the three inputs, taken from repository commit `60f8bad` (2026-11-03) via the H20 checkout:

| File | MD5 |
|---|---|
| `core_corpus_manifest.csv` | `56b8dceaec07fa163a9d6acbf43dce25` |
| `classification_results_662.csv` | `e57197d4992e13ae32b228b35dfba46c` |
| `paper_module_taxonomy_assignments.jsonl` | `8c0d1ffad1874cc2c244c8f5f3f9fcc8` |

`derived/` holds the tidy tables behind every number above (`papers.csv`, `assignments.csv`, `cooccur.csv`). The two general-method papers (ASD-0040, ASD-0059) have no field: they are counted in **b** and **c** but do not appear in **a**, **d** or **e**.

Requires Python 3 with matplotlib ≥3.10, numpy and scipy, plus the Arial and Arial Unicode MS fonts.
