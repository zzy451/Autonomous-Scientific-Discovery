# Relaxed multi-module reclassification round 2 / P0-D

> Date: 2026-06-20  
> Scope: P0 `01.04` / general-agent boundary follow-up for `ASD-0671`, `ASD-0676`, and `ASD-0845`.  
> Rule: local Notes were used only as leads; accepted decisions below rely on first-hand PDF evidence.

## 1. 本轮结论

本轮完成 3 条 P0 记录复核。

| ID | Decision | Accepted modules / bucket | First-hand sources checked | Note action |
|---|---|---|---|---|
| `ASD-0671` | closed | `01;02;06`, `general_method_bucket=none` | arXiv PDF `2605.20025` | note revised |
| `ASD-0676` | closed | `01;06;07`, `general_method_bucket=none` | arXiv PDF `2605.31468` | note revised |
| `ASD-0845` | closed | `01;02;11`, `general_method_bucket=none` | arXiv PDF `2603.01421` | note revised |

## 2. 逐条证据

### `ASD-0671` AutoResearchClaw

- Accepted relaxed modules: `01;02;06`.
- Source: arXiv PDF `2605.20025`.
- Evidence:
  - ARC-Bench reports 25 ML research topics, including tabular ML, optimization, dimensionality reduction, NLP, AutoML, GP kernels, causal discovery, and learning-to-rank, supporting `01`.
  - The scientific-domain extension reports 10 HEP-ph tasks, with MadGraph / FeynRules / MadAnalysis tooling and cross-section reproduction, supporting `02`.
  - The same extension reports 7 systems-biology tasks with COBRApy and BiGG genome-scale models, including E. coli succinate knockout screens, M. tuberculosis essentiality, and drug-target prioritization, supporting `06`.
- Boundary decision: statistics tasks remain within `01`. The domain-support matrix alone was not counted as evidence for chemistry, economics, mathematics, neuroscience, or other modules.

### `ASD-0676` AutoSci

- Accepted relaxed modules: `01;06;07`.
- Source: arXiv PDF `2605.31468`.
- Evidence:
  - GPU kernel optimization case executes profiling-guided code optimization over TritonBench / PyTorch workloads, supporting formal / computational-systems coverage (`01`).
  - Biomedical drug-discovery case executes PTM-aware degrader target nomination, DeepTernary / PROTAC-STAN reproduction, and a 22-complex PROTAC test set, supporting `07`.
  - The same biomedical case evaluates 15 POIs / 189 interface sites with phospho, alanine, and Kme3 perturbations, PTM-aware scoring, and Boltz-2 cross-checks, supporting protein / PTM / structural-biology coverage (`06`).
- Boundary decision: no separate `03` assignment was accepted because the paper does not report chemical synthesis, reaction, catalyst, or standalone small-molecule design results beyond the drug-discovery / PROTAC evaluation context.

### `ASD-0845` SciDER

- Accepted relaxed modules: `01;02;11`.
- Source: arXiv PDF `2603.01421`.
- Evidence:
  - AI-Idea-Bench, MLE-Bench, AIRS-Bench, and ML research-execution evaluations support formal / computational science coverage (`01`).
  - AstroVisBench is evaluated as an astronomy / astrophysics visualization and specialized tool-use benchmark, supporting `02`.
  - The end-to-end case study generates a calibrated few-shot knowledge-tracing paper on ASSISTments 2009-2010, with reported educational-learning metrics and discussion, supporting `11`.
- Boundary decision: broad skill lists and unspecific DiscoveryBench / SciCode subdomain labels were not counted as high-confidence evidence for `03`, `04`, `05`, or `06`.

## 3. Count update

Post-P0-D relaxed overlay:

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 55 |
| `02` | 36 |
| `03` | 77 |
| `04` | 106 |
| `05` | 35 |
| `06` | 71 |
| `07` | 67 |
| `08` | 3 |
| `09` | 36 |
| `10` | 24 |
| `11` | 33 |

| Metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 543 |
| Independent `01.04` general-method bucket count | 21 |

## 4. Remaining uncertainty

All three records in this P0-D slice are closed. The taxonomy itself did not show instability in this slice; the main correction was stale `01.04` treatment caused by earlier abstract-level or single-module notes. The next unresolved P0 items remain `ASD-0006`, `ASD-0553`, `ASD-0856`, and `ASD-0869`, plus any later queue items not yet full-text reviewed.
