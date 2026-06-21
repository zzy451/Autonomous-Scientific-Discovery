# Relaxed multi-module reclassification round 2 / P0-F

> Date: 2026-06-21
> Scope: P0 `01.04` / general-agent boundary follow-up for `ASD-0553`.
> Rule: local Notes were used only as leads; accepted decisions below rely on first-hand DOI-registered abstract evidence and official project pages.

## 1. 本轮结论

本轮关闭 1 条 P0 记录复核：

| ID | Decision | Accepted modules / bucket | First-hand sources checked | Note action |
|---|---|---|---|---|
| `ASD-0553` | closed | keep independent `01.04`; no accepted concrete-object modules | Crossref DOI abstract `10.64898/2026.01.06.697527`; official PromptBio platform landing page | note revised |

## 2. 逐条证据

### `ASD-0553` ToolsGenie 2.0

- Accepted action: keep the record in the independent `01.04` bucket; do not add `06` or `07`.
- First-hand evidence: the official DOI abstract presents ToolsGenie 2.0 as a multi-agent AI framework for bioinformatics automation via natural-language queries and file inputs, with ReAct-style architecture, dual-layer extensibility, dynamic Docker image selection, and benchmark accuracy on an in-house dataset plus BixBench.
- Why no concrete-domain migration landed: although the abstract mentions research and clinical contexts, the accessible first-hand evidence does not identify concrete gene, protein, cell, tissue, disease, or patient-object case studies with separate reported scientific results. The validated contribution remains platform extensibility, automation, reproducibility, and benchmark performance rather than a recognizable biology or biomedical object discovery study.
- Result: the earlier source-limited uncertainty is reduced enough to stabilize the relaxed-round decision at independent `01.04`.

## 3. Count update

Post-P0-F relaxed overlay counts are unchanged because `ASD-0553` remains in the independent `01.04` bucket:

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 55 |
| `02` | 37 |
| `03` | 79 |
| `04` | 108 |
| `05` | 35 |
| `06` | 74 |
| `07` | 68 |
| `08` | 3 |
| `09` | 36 |
| `10` | 24 |
| `11` | 34 |

| Metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 553 |
| Independent `01.04` general-method bucket count | 19 |

## 4. Remaining uncertainty

- Full preprint access would still be useful for extracting task-level examples and benchmarking details.
- However, under the current relaxed rule, the official abstract already provides enough first-hand evidence to keep this paper in the independent `01.04` bucket and reject premature `06` / `07` migration.
