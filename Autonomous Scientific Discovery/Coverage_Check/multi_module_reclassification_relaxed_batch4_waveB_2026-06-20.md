# Batch 4 / Wave B relaxed multi-module reclassification audit

> Date: 2026-06-20  
> Scope: Batch 4 / Wave B, `ASD-0805`-`ASD-0871` returned by four read-only reviewers.  
> Policy: relaxed scientific-object experiment-coverage rule; original / first-hand source evidence preferred over legacy Notes.

## 1. 本轮最新状态

- confirmed included + classified count: `451`
- needs_review count: `0`
- independent `01.04` bucket count after accepted relaxed migrations: `32`
- expanded module assignment count: `512`
- 本轮主要边界压力点：`03/07` lead optimization, `01.04` equation-discovery benchmarks, `01.04` general agents with concrete case studies, and `05/10` rover / mission-science boundary.

## 2. 本轮已合并改动

| ID | 题名 | 原状态 / 原模块或 `01.04` bucket | 新状态 / 新模块或 `01.04` bucket | primary_module_for_filing | 理由 |
|---|---|---|---|---|---|
| `ASD-0811` | Closed-Loop Molecular Design with Calibrated Deference | `04 / 04.04` | `03;04`, `general_method_bucket=none` | `04` | AORFB negolyte molecular design and synthesis support `03`; battery / electrochemical material performance supports `04`. |
| `ASD-0820` | Reinforcement Learning with LLM-Guided Action Spaces for Synthesizable Lead Optimization | `03 / 03.04` | `03;07`, `general_method_bucket=none` | `07` | Reaction templates and synthetic trajectories support `03`; synthesizable lead optimization, docking/TDC tasks, and drug-discovery objectives support `07`. |
| `ASD-0844` | Science Earth | `01 / 01.04` | `01;06`, `general_method_bucket=none` | `01` | Kuramoto / Ott-Antonsen complex-systems case supports `01`; pan-cancer single-cell atlas and Treg validation support `06`. |
| `ASD-0866` | Accelerating Scientific Discovery with Autonomous Goal-evolving Agents | `01 / 01.04` | `03;04;06;07`, `general_method_bucket=none` | `07` | Reported antibiotics, E. coli hits, functional DNA, inorganic materials, chemical processes and PD-L1 nanobody / therapeutic endpoints provide concrete multi-domain object coverage. |
| `ASD-0868` | Think like a Scientist | `01 / 01.04` | `02`, `general_method_bucket=none` | `02` | Physical equation benchmarks and physics-guided symbolic-equation discovery constitute concrete physics object coverage. |
| `ASD-0870` | SR-Scientist | `01 / 01.04` | `02;03;04;06`, `general_method_bucket=none` | `02` | SR benchmark / dataset evidence covers physics, chemistry, materials and biology equation-discovery tasks. |
| `ASD-0871` | The Denario project | `01 / 01.04` | `02;03;04;06;07`, `general_method_bucket=none` | `02` | arXiv HTML reports concrete end-to-end research examples spanning astrophysics/cosmology, chemistry, materials, life science and health. |

## 3. Note updates completed

已同步修订 7 篇 note，均在标题下方加入 `2026-06-20 relaxed multi-module revision` 区块：

| ID | Note path |
|---|---|
| `ASD-0811` | `Notes/04_Materials_Science/Unknown_2026_CLIO.md` |
| `ASD-0820` | `Notes/03_Chemical_Sciences/Li_2026_MolReAct_Lead_Optimization.md` |
| `ASD-0844` | `Notes/01_Formal_Information_and_Computational_Sciences/Unknown_2026_Science_Earth.md` |
| `ASD-0866` | `Notes/01_Formal_Information_and_Computational_Sciences/Unknown_2025_SAGA.md` |
| `ASD-0868` | `Notes/01_Formal_Information_and_Computational_Sciences/Yang_2026_KeplerAgent_Equation_Discovery.md` |
| `ASD-0870` | `Notes/01_Formal_Information_and_Computational_Sciences/Xia_2025_SR_Scientist.md` |
| `ASD-0871` | `Notes/01_Formal_Information_and_Computational_Sciences/Unknown_2025_Denario.md` |

## 4. 本轮未改动但重点复核的记录

| ID | 当前 scientific_object_modules / `01.04` bucket | 保持原因 | 后续是否还需复核 |
|---|---|---|---|
| `ASD-0810` | keep `03` | Drug-like / sEH signal exists, but reviewer confidence is medium and asks for full-text harmonization. | yes |
| `ASD-0817` | keep `07` | Structure-based drug design is stable; chemistry secondary remains policy-sensitive. | yes |
| `ASD-0818` | keep `03` | Mixed molecular optimization includes drug-target framing, but current evidence remains chemistry-first. | yes |
| `ASD-0838` | keep `03` | Flow chemistry object is stable; possible `04` needs full text. | yes |
| `ASD-0845` | keep `01.04` | Abstract does not list stable concrete benchmark objects. | yes |
| `ASD-0850` | keep `01` | Cooperative-driving scenario may trigger `10`, but full-text task depth is needed. | yes |
| `ASD-0856` | keep `01.04` for now | Abstract suggests biology/economics/finance/behavioral-science datasets, but exact dataset-to-module mapping requires full text. | yes |
| `ASD-0869` | keep `01.04` for now | LSR-Synth / benchmark evidence suggests `02;03;04;06`, but exact task inventory still needs full-text confirmation. | yes |

## 5. 本轮边界问题

- `01.04` bucket 明显继续收缩：只要 general scientific-agent paper 报告了 concrete object case studies 或 domain benchmark tasks，就不能继续只按 independent `01.04` 处理。
- Equation-discovery papers 的边界更复杂：如果 benchmark 明确落在 physics / chemistry / materials / biology tasks，应记录相应对象模块；若仅是抽象 symbolic-regression capability benchmark，则可暂留 `01.04` 或 `01.03` 队列。
- `03/07` lead optimization 不能一刀切：target-facing / therapeutic / docking / TDC drug-discovery evidence 明确时可加 `07`；普通 molecular optimization 或 cheminformatics benchmark 不自动加 `07`。
- `05/10` 本轮总体稳定：rover / spacecraft mission-science autonomy 仍按 `10`，Earth-observation natural-process monitoring仍按 `05`。

## 6. Updated partial overlay counts

Post Batch 4 / Wave B audited relaxed overlay:

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 47 |
| `02` | 33 |
| `03` | 73 |
| `04` | 103 |
| `05` | 34 |
| `06` | 66 |
| `07` | 64 |
| `08` | 3 |
| `09` | 35 |
| `10` | 23 |
| `11` | 31 |

| Relaxed-counting metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 512 |
| Independent `01.04` general-method bucket count, after accepted relaxed migrations | 32 |

## 7. 下一轮建议

- 将 `ASD-0856`、`ASD-0869` 放入 full-text boundary queue，重点核对具体 benchmark / dataset task inventory。
- 后续 schema migration 时，应把 `scientific_object_modules`, `primary_module_for_filing`, `general_method_bucket`, `object_coverage_mode` 从 remarks 中迁入结构化字段。
- Batch 4 已完成 A/B 两个 wave；下一步宜汇总 Batch 4 或进入本轮剩余高风险队列整理。
