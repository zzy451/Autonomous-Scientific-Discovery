# Relaxed multi-module round-2 P1-H audit

> Date: 2026-06-21
> Scope: P1 concrete-module boundary follow-up focused on `ASD-0064`.
> Rule: only high-confidence changes supported by first-hand paper evidence are written back to the master list and Notes.

## 本轮结论

本轮关闭 1 条 P1 边界项：

| ID | Title short | Sources checked | Decision | Note action |
|---|---|---|---|---|
| `ASD-0064` | PhenoGraph | OpenReview full PDF; Crossref DOI abstract `10.1101/2025.06.06.658341` | accepted `scientific_object_modules=06;07`; keep `primary_module_for_filing=06` | revised `Notes/06_Life_Sciences/Niyakan_2025_PhenoGraph.md` |

## Evidence summary

### `ASD-0064` PhenoGraph

- Agent evidence: the paper explicitly presents an LLM-based multi-agent system with `TCGA Agent`, `ML Agent`, and `Knowledge Graph Agent`, capable of phenotype-pipeline selection, data retrieval, code execution/correction, and KG-grounded reasoning.
- `06` evidence: the abstract and methods consistently anchor the work in phenotype-driven spatial-transcriptomics analysis, tumor-microenvironment discovery, and spatial molecular expression patterns.
- `07` evidence: the full text does more than mention clinical context in passing. It reports a breast invasive-carcinoma tumor-vs-normal case and a PDAC survival-phenotype case using `TCGA-BRCA` / `TCGA-PAAD` clinical metadata, patient prognosis, poor-survival-region localization, overlap with histologically labeled tumor regions, and prognostic spatial biomarkers.
- Accepted action: close the `06/07` boundary as `06;07`, while keeping `06` as `primary_module_for_filing` because the system's main workflow remains an omics / ST analysis agent rather than a diagnosis or treatment-decision system.

## Count update

Post-P1-H relaxed overlay counts add one `06` assignment and one `07` assignment relative to the post-P1-G state:

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 55 |
| `02` | 37 |
| `03` | 80 |
| `04` | 109 |
| `05` | 35 |
| `06` | 75 |
| `07` | 69 |
| `08` | 3 |
| `09` | 36 |
| `10` | 24 |
| `11` | 34 |

| Metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 555 |
| Independent `01.04` general-method bucket count | 20 |

## Remaining uncertainty

- Additional page-level evidence extraction could further enrich the note.
- That said, the currently accessible first-hand full text is already sufficient to support `07` as an additional module rather than leaving it as a tentative future possibility.
