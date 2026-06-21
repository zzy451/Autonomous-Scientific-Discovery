# Relaxed multi-module round-2 P1-M audit

> Date: 2026-06-21
> Scope: P1 concrete-module boundary follow-up focused on `ASD-0651`.
> Rule: only high-confidence changes supported by first-hand paper evidence are written back to the master list and Notes.

## 本轮结论

本轮关闭 1 条 P1 边界项：

| ID | Title short | Sources checked | Decision | Note action |
|---|---|---|---|---|
| `ASD-0651` | Heatwave Discovery Agent | arXiv abstract; arXiv full-text HTML `2509.25112v1` | accepted `scientific_object_modules=05;11`; keep `primary_module_for_filing=05`; do not add `06` | revised `Notes/05_Earth_and_Environmental_Sciences/Wang_2025_Heatwave_Discovery_Agent.md` |

## Evidence summary

### `ASD-0651` AI Driven Discovery of Bio Ecological Mediation in Cascading Heatwave Risks

- Agent evidence: the full text presents HeDA as an intelligent multi-agent system for autonomous scientific discovery through literature-scale knowledge-graph construction, multi-layer risk propagation analysis, question answering, and chain validation.
- `05` evidence: the stable primary object remains compound heatwaves and cascading climate-risk mechanisms. The paper explicitly frames heatwaves as the starting natural hazard, collects a heatwave-risk literature corpus, and validates discovered pathways against major historical heatwave events such as the 2003 European heatwave, the 2006 California heatwave, and the 2021 Pacific Northwest heatwave.
- `11` evidence: the discovered and validated chains are not restricted to environmental consequences. The results explicitly report small-business disruption, local economic instability, hospital equipment failure and critical-care interruption, rural-to-urban migration pressure, housing-market strain, educational achievement gaps, long-term productivity impacts, and intergenerational inequality. These are independent social/economic-system objects under the current relaxed rule.
- Why `06` is not accepted: the paper uses “bio-ecological mediation” language and cites public-health/ecological literature, but the currently accessible first-hand evidence does not show an independent life-science object study comparable in specificity to the paper’s heatwave and social/economic risk-chain outputs. The paper’s own layer formalization groups health under the social layer rather than establishing a separate life-science experimental track.
- Accepted action: close the `05 / 06 / 11` boundary as `05;11`, while keeping `05` as `primary_module_for_filing` because the paper remains anchored in heatwave/climate-risk discovery rather than social-science methodology as its primary research object.

## Count update

Post-P1-M relaxed overlay counts add one `11` assignment relative to the post-P1-L state:

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 55 |
| `02` | 37 |
| `03` | 82 |
| `04` | 110 |
| `05` | 35 |
| `06` | 75 |
| `07` | 70 |
| `08` | 3 |
| `09` | 36 |
| `10` | 24 |
| `11` | 35 |

| Metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 560 |
| Independent `01.04` general-method bucket count | 20 |

## Remaining uncertainty

- A future full-text revisit could still ask whether a distinct `06` layer ever becomes strong enough through ecological/health-object evidence, but the currently accessible first-hand evidence is not sufficient for that extra module.
- The paper remains a useful pressure-test example for `05 / 11` cross-module assignment, especially because it is climate-risk primary while still producing explicit social/economic-system chains.
