# Relaxed multi-module round-2 P1-K audit

> Date: 2026-06-21
> Scope: P1 concrete-module boundary follow-up focused on `ASD-0520`.
> Rule: only high-confidence changes supported by first-hand paper evidence are written back to the master list and Notes.

## 本轮结论

本轮关闭 1 条 P1 边界项：

| ID | Title short | Sources checked | Decision | Note action |
|---|---|---|---|---|
| `ASD-0520` | low-Ir OER catalyst discovery | Crossref DOI abstract `10.1126/sciadv.adw0894` | accepted `scientific_object_modules=03;04`; keep `primary_module_for_filing=04` | revised `Notes/04_Materials_Science/Niu_2025_Bayesian_Catalyst_Discovery_Iridium.md` |

## Evidence summary

### `ASD-0520` Bayesian learning-assisted catalyst discovery for efficient iridium utilization in electrochemical water splitting

- Agent evidence: the publisher-registered abstract describes a multi-step discovery workflow that integrates DFT calculations with Bayesian learning, uses theoretically optimized surface compositions and oxygen vacancies to guide candidate selection, and then synthesizes and validates the resulting catalyst.
- `04` evidence: the directly optimized objects include bimetallic oxides, surface Ir-doped TiO2, oxygen-vacancy configurations, atomically dispersed Ir on TiO2, and catalyst-material performance against commercial IrO2. This is stable `04` materials-side object coverage.
- `03` evidence: the paper is not only about static material composition. Its explicit scientific target is oxygen evolution reaction electrocatalysis, and the validated outputs are catalytic overpotential reduction plus Ir mass-specific activity gains for electrochemical water splitting. Under the current relaxed rule, this is enough chemistry-side electrochemical catalysis coverage to add `03`.
- Accepted action: close the `03/04` boundary as `03;04`, while keeping `04` as `primary_module_for_filing` because the optimized object family remains low-Ir catalyst materials rather than a chemistry-only reaction-planning paper.

## Count update

Post-P1-K relaxed overlay counts add one `03` assignment relative to the post-P1-J state:

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 55 |
| `02` | 37 |
| `03` | 81 |
| `04` | 109 |
| `05` | 35 |
| `06` | 75 |
| `07` | 70 |
| `08` | 3 |
| `09` | 36 |
| `10` | 24 |
| `11` | 34 |

| Metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 557 |
| Independent `01.04` general-method bucket count | 20 |

## Remaining uncertainty

- The record still has a separate confirmed-core-strength question because currently accessible first-hand evidence is abstract-level rather than full-text-level.
- But for the narrow `03/04` multi-module boundary, the publisher-registered abstract is already explicit enough to land `03;04` with `04` as the filing module.
