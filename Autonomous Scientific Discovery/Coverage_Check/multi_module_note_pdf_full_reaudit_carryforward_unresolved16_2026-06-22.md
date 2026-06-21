# CarryForward Unresolved16 Multi-Module / Note / PDF Reaudit Report

Generated: `2026-06-22`  
Coverage: the earliest unresolved confirmed-core carry-forward slice in flat master-list row order after the previous completed rounds: `ASD-0052`, `ASD-0054`, `ASD-0097`, `ASD-0112`, `ASD-0139`, `ASD-0141`, `ASD-0145`, `ASD-0158`, `ASD-0357`, `ASD-0370`, `ASD-0379`, `ASD-0381`, `ASD-0385`, `ASD-0388`, `ASD-0389`, `ASD-0410`.  
Mode: carry-forward unresolved closeout using the plan-defined structure: `Evidence-Agent-A/B/C` for read-only first-hand evidence collection, `Classification-Reviewer` for independent adjudication, `PDF-Archive-Agent` for approved archive work, `Writeback-Agent-1/2/3` for disjoint note writeback, and `Main Controller` for final master/progress/report editing and recounting.

## 1. 本次落地范围

- 本次直接落地 `11` 篇：
  - `ASD-0139`
  - `ASD-0145`
  - `ASD-0158`
  - `ASD-0357`
  - `ASD-0370`
  - `ASD-0379`
  - `ASD-0381`
  - `ASD-0385`
  - `ASD-0388`
  - `ASD-0389`
  - `ASD-0410`
- 本次继续保守挂起 `5` 篇：
  - `ASD-0052`
  - `ASD-0054`
  - `ASD-0097`
  - `ASD-0112`
  - `ASD-0141`

## 2. 结果概览

- closed records in this carry-forward slice: `11`
- conservative carry-forward records remaining open: `5`
- newly archived local PDFs in this slice: `7`
- notes updated: `11`
- master rows updated: `11`
- source-limited but now formally closed: `ASD-0158`, `ASD-0357`, `ASD-0370`, `ASD-0381`
- explicit safety carry-forward kept visible: `ASD-0054`

## 3. Record-Level Outcomes

| ID | Final modules or bucket | PDF / source status | Closeout note |
|---|---|---|---|
| ASD-0139 | `02` | archived arXiv PDF | migrated out of stale independent `01.04`; current first-hand full text shows concrete physics benchmark / case coverage |
| ASD-0145 | `01.04` | archived OpenReview PDF | keeps the independent `01.04` bucket; automated review remains a feedback mechanism for a general research-agent workflow rather than `11.07` |
| ASD-0158 | `03` | source-limited; Science PDF `403` | stable chemistry anchor; source limitation no longer blocks closeout because class identity is firm |
| ASD-0357 | `07` | source-limited; bioRxiv PDF `403` | Crossref abstract plus official homepage metadata are sufficient to keep a stable disease-target-discovery filing |
| ASD-0370 | `06` | source-limited; Nature client challenge | stable protein-engineering / enzyme-thermostability record |
| ASD-0379 | `04` | archived open-access publisher PDF | stable materials-property SDL record |
| ASD-0381 | `03` | source-limited; publisher preview only | stable catalysis / ligand-optimization record |
| ASD-0385 | `03;04` | archived open-access publisher PDF | closed the outstanding hold and landed the already-suspected chemistry + materials multi-module fact |
| ASD-0388 | `04` | archived arXiv PDF | stable materials-characterization / discovery companion-agent record; residual risk is core-strength, not module identity |
| ASD-0389 | `04` | archived open-access publisher PDF | stable chiral inorganic perovskite nanocrystal discovery record |
| ASD-0410 | `04` | archived open-access publisher PDF | stable Ge-Sb-Te phase-change-material discovery record |

## 4. 关键边界说明

`ASD-0139`  
这条是本轮最重要的主类迁移。旧的 `01.04` 说法依赖摘要级直觉，把它看成“physics-themed general reasoning framework”。但本轮直接核对 arXiv 全文后，已经能看到 SciBench mechanics、statistical thermodynamics、classical dynamics 和 electrodynamics 的可识别 benchmark / case coverage，所以不能继续留在“无具体对象实验”的独立 `01.04` 桶里。

`ASD-0145`  
这条恰好相反。本轮虽然拿到了 OpenReview / arXiv 一手 PDF，但证据仍然显示它的验证对象主要是 automated research / review-loop workflow，而不是 scientific knowledge production itself，更不是具体自然科学对象实验。因此它仍应保留在独立 `01.04`，而不是向 `11.07` 或具体对象模块迁移。

`ASD-0385`  
这条是本轮最典型的 `03 / 04` relaxed multi-module 着陆样本。全文同时覆盖了 multi-step chemistry / synthetic-route optimization 和 semiconductor core-shell nanoparticle materials discovery。旧的单一 `04` filing 仍可保留为 `primary_module_for_filing`，但分类事实必须记为 `03;04`。

`ASD-0158 / ASD-0357 / ASD-0370 / ASD-0381`  
这 4 条都没有在本轮拿到本地 PDF，但当前 first-hand abstract / metadata / official homepage evidence 已足以让主类稳定，不再需要因为“缺全文”而无限期挂起。它们本轮以 `source_limited but classification-stable` 方式关闭。

`ASD-0054`  
这条仍然保持显式 safety carry-forward。本轮没有重新访问任何新的 unsafe route；进度和边界队列都继续可见地标记为 `not accessed due to safety`，没有用旧 note 或旧字段偷偷回填。

## 5. Conservative Carry-Forward

| ID | Current hold reason | Current status |
|---|---|---|
| ASD-0052 | SSRN official abstract supports stable `09`, but DOI route was partially safety-blocked and SSRN PDF remained `403` | keep conservative |
| ASD-0054 | explicit `not accessed due to safety`; no fresh safe first-hand recheck this turn | keep conservative |
| ASD-0097 | official Nature Methods preview increases `06;07` pressure, but this round still kept the proposed medical-side expansion conservative | keep conservative |
| ASD-0112 | official abstract / highlights increase `07;03` pressure, but the chemistry-side expansion remains conservative without stronger full-text support | keep conservative |
| ASD-0141 | DOI / Crossref abstract increases `06;07` pressure, but the medical-side expansion remains conservative without stronger full-text support | keep conservative |

## 6. PDF Archive Results

- `7/7` approved archive attempts succeeded.
- Archived this round:
  - `Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Xu_2025_Interpretable_Physics_Reasoning.pdf`
  - `Reference_PDF/01_04_General_Method_Bucket/Weng_2025_CycleResearcher.pdf`
  - `Reference_PDF/04_Materials_Science/MacLeod_2022_Pareto_Front_Materials.pdf`
  - `Reference_PDF/04_Materials_Science/Volk_2023_AlphaFlow_Nanoparticle_Growth.pdf`
  - `Reference_PDF/04_Materials_Science/Maffettone_2021_Crystallography_Companion_Agent.pdf`
  - `Reference_PDF/04_Materials_Science/Li_2020_MAOSIC_Chiral_Perovskite.pdf`
  - `Reference_PDF/04_Materials_Science/Kusne_2020_CAMEO_Materials_Discovery.pdf`

## 7. Multi-Agent Audit Trace

- `Evidence-Agent-A` covered:
  - `ASD-0052`, `ASD-0054`, `ASD-0097`, `ASD-0112`, `ASD-0139`
  - key pressure points: `ASD-0139 -> 02`; `ASD-0097 -> 06;07`; `ASD-0112 -> 07;03`
- `Evidence-Agent-B` covered:
  - `ASD-0141`, `ASD-0145`, `ASD-0158`, `ASD-0357`, `ASD-0370`
  - key pressure points: `ASD-0145` remains `01.04`; `ASD-0158` is stable `03`; `ASD-0357` remains stable `07`
- `Evidence-Agent-C` covered:
  - `ASD-0379`, `ASD-0381`, `ASD-0385`, `ASD-0388`, `ASD-0389`, `ASD-0410`
  - key pressure points: `ASD-0385 -> 03;04`; the rest of the materials SDL cluster can now close cleanly
- `Classification-Reviewer` returned:
  - 5 explicit conservative holds: `ASD-0052`, `ASD-0054`, `ASD-0097`, `ASD-0112`, `ASD-0141`
  - 11 landable records, of which `ASD-0139` and `ASD-0385` required the most important master-side classification updates
- `Writeback-Agent-1/2/3` returned disjoint note ownership with no file overlap
- `PDF-Archive-Agent` archived 7 PDFs and validated each with a `%PDF` header check

## 8. 本次后累计进度

- Total unresolved carry-forward rows before this round: `16`
- Closed in this round: `11`
- Remaining unresolved after this round: `5`
- Remaining unresolved IDs after this round:
  - `ASD-0052`
  - `ASD-0054`
  - `ASD-0097`
  - `ASD-0112`
  - `ASD-0141`
