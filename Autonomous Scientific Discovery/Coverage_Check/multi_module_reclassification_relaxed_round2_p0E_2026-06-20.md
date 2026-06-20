# Relaxed multi-module reclassification round 2 / P0-E

> Date: 2026-06-20  
> Scope: P0 `01.04` / general-agent boundary follow-up for `ASD-0856` and `ASD-0869`.  
> Rule: local Notes were used only as leads; accepted decisions below rely on first-hand PDF evidence.

## 1. 本轮结论

本轮完成 2 条 P0 记录复核。

| ID | Decision | Accepted modules / bucket | First-hand sources checked | Note action |
|---|---|---|---|---|
| `ASD-0856` | closed | `06;07;11`, `general_method_bucket=none` | arXiv PDF `2507.00310` | note revised |
| `ASD-0869` | closed | `02;03;04;06`, `general_method_bucket=none` | arXiv PDF `2605.17790` | note revised |

## 2. 逐条证据

### `ASD-0856` AutoDiscovery

- Accepted relaxed modules: `06;07;11`.
- Source: arXiv PDF `2507.00310`.
- Evidence:
  - The paper evaluates AutoDiscovery over 21 real-world data-driven-discovery datasets spanning biology, economics, finance, and behavioral science.
  - DiscoveryBench freshwater-fish and BLADE biological / fish datasets support life-science coverage (`06`).
  - SEA-AD is a human-brain cellular atlas across the Alzheimer's disease spectrum and includes donor cognitive status plus neuropathological assessments, supporting both life science (`06`) and biomedical / health coverage (`07`).
  - Economics, finance, and behavioral-science datasets, including NLS, mortgage, affairs, caschools, reading, teaching-ratings, soccer, and related expert hypothesis evaluation, support `11`.
- Boundary decision: hurricane and requirement-engineering datasets were not counted as high-confidence `05` or `01` module evidence. The Bayesian-surprise / MCTS machinery was treated as Agent infrastructure rather than independent formal-science object coverage.

### `ASD-0869` STRIDE

- Accepted relaxed modules: `02;03;04;06`.
- Source: arXiv PDF `2605.17790`.
- Evidence:
  - Appendix D states that benchmark tasks cover physics, biology, chemistry, and materials science.
  - LLM-SR tasks include nonlinear oscillator systems (`02`), E. coli growth (`06`), and temperature-dependent stress-strain material behavior (`04`).
  - LSR-Synth suites include CRK chemistry (`03`), BPG biology (`06`), PO physics (`02`), and MatSci material equations (`04`), with reported ID/OOD performance and case analysis.
- Boundary decision: no separate `01` module was added solely because the system is an equation-discovery framework; module assignment is driven by concrete benchmark scientific objects.

## 3. Count update

Post-P0-E relaxed overlay:

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 55 |
| `02` | 37 |
| `03` | 78 |
| `04` | 107 |
| `05` | 35 |
| `06` | 73 |
| `07` | 68 |
| `08` | 3 |
| `09` | 36 |
| `10` | 24 |
| `11` | 34 |

| Metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 550 |
| Independent `01.04` general-method bucket count | 19 |

## 4. Remaining uncertainty

Both records in this P0-E slice are closed. The taxonomy itself remains stable; the correction again reflects stale `01.04` treatment from earlier framework-first notes. The unresolved P0 cases after this slice are source-limited or not yet re-opened in this round, especially `ASD-0006` and `ASD-0553`.
