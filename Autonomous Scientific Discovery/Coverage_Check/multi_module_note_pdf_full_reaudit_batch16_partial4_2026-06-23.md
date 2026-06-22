# Batch 16 Partial-4 Multi-Module / Note / PDF Reaudit Report

Generated: `2026-06-23`  
Coverage: the same 30 confirmed-core records in flat master-list row order already opened by `Batch 16 partial-1`: `ASD-0517`, `ASD-0518`, `ASD-0519`, `ASD-0520`, `ASD-0521`, `ASD-0522`, `ASD-0523`, `ASD-0524`, `ASD-0525`, `ASD-0526`, `ASD-0528`, `ASD-0529`, `ASD-0530`, `ASD-0531`, `ASD-0535`, `ASD-0536`, `ASD-0537`, `ASD-0538`, `ASD-0539`, `ASD-0540`, `ASD-0541`, `ASD-0542`, `ASD-0543`, `ASD-0544`, `ASD-0545`, `ASD-0547`, `ASD-0548`, `ASD-0549`, `ASD-0552`, and `ASD-0553`.  
Mode: `Batch 16 partial-4`; this closeout again followed the plan-defined structure: `Evidence-Agent-A/B/C` for read-only evidence collection, `Classification-Reviewer` for independent adjudication, `Writeback-Agent-1/2` for disjoint note writeback on the approved landed subset, and `Main Controller` for the only master/progress/report closeout.

## 1. 本次落地范围

- 本次在 `Batch 16 partial-3` 剩余的 `10` 篇 conservative/open records 中，再落地 `4` 篇：
  - `ASD-0519`
  - `ASD-0520`
  - `ASD-0535`
  - `ASD-0536`
- 本次继续保守挂起 `6` 篇：
  - `ASD-0531`
  - `ASD-0541`
  - `ASD-0544`
  - `ASD-0545`
  - `ASD-0547`
  - `ASD-0553`

## 2. 结果概览

- newly landed notes updated in this partial: `4`
- master rows updated in this partial: `4`
- no local PDFs were newly archived in this partial
- no shared-note-path record was written in this partial; all landed notes had disjoint ownership
- safety visibility was preserved explicitly rather than collapsed into ordinary source-thin wording:
  - `ASD-0541` remains a safety-visible `01.04` hold
  - `ASD-0545` remains a safety-supported `06;07` hold
  - `ASD-0547` and `ASD-0553` remain safety-skip conservative holds

## 3. 本次新增落地记录

| ID | Final modules or bucket | PDF / source status | Closeout note |
|---|---|---|---|
| ASD-0519 | `03;04` | open PMC full text checked, no local archive | this record is no longer just a tentative `03` electrochemistry platform hold; PMC full text adds concrete aqueous-zinc-battery electrolyte-additive evidence, so `04` is now landed alongside `03`, while the note still keeps explicit wording that Agent strength is softer than object evidence |
| ASD-0520 | `03;04` | open PMC full text checked, no local archive | direct PMC evidence now closes the old Crossref-only boundary hold; electrocatalysis supports independent `03` coverage while catalyst composition / performance keeps `04` as primary filing |
| ASD-0535 | `04` | official publisher open-access abstract/highlights plus arXiv abstract checked, no local archive | this paper stays firmly on inorganic-materials design and should not keep drifting toward `01.04` or an unresolved platform-style hold |
| ASD-0536 | `07` | official JPA abstract checked, no local archive | this record now closes as an explicit source-limited but object-stable medical/pharmacology paper: `07` stays supported from first-hand publisher sources even though full text was not retrieved in this run |

## 4. 关键边界说明

`ASD-0519`  
这是本 partial 中最值得单独记下的“对象证据强于 Agent 强度”案例。PMC 全文已经把论文从旧的 abstract-level conservative hold 推到了可落地状态，因为它不再只是抽象的高通量 electrochemistry platform，而是明确做了 aqueous zinc battery electrolyte additive screening。当前仍应保留“Agent inclusion borderline”的提示，但这已经不妨碍 `03;04` 在对象层面落地。

`ASD-0520`  
这条不是简单重复 `03;04` overlay，而是把原本只靠 Crossref/publisher abstract 支撑的边界真正收口成 `closed=yes`。PMC 全文使 `03` 不再只是 future follow-up，而是与 `04` 同时被一手证据支撑。

`ASD-0535`  
这条的关键不是扩大模块，而是停止把它当作 source-thin platform sample。官方期刊开放摘要页与 arXiv 摘要都已足够稳定地把它留在 inorganic materials design 对象路径中，因此本轮直接落地 `04`。

`ASD-0536`  
这条与 `ASD-0535` 不同。它不是 full-text-strength closeout，而是 source-limited closeout。官方 JPA 摘要已经足以稳定支持 TCM / herbal-medicine discovery object，因此本轮可以收口到 `07`，但必须继续显式保留 `source_limited=yes`，不能假装拿到了全文或本地 PDF。

## 5. Continue Conservative / Safety Queue 的 `6` 篇

| ID | Current hold reason | Current status |
|---|---|---|
| ASD-0531 | title anchors a therapeutic-discovery object, but stronger first-hand evidence for the old `06;07` reading was not resecured in-session | keep conservative |
| ASD-0541 | stronger accessible sources currently support independent `01.04`, but official preprint access remained safety-blocked (`403` / safe-open block) | keep conservative safety-visible hold |
| ASD-0544 | DOI/title still anchor a cancer biomarker object, but current first-hand access stops at the IEEE shell | keep conservative |
| ASD-0545 | abstract-level evidence still supports `06;07`, but DOI redirected to non-safe `http` bioRxiv in this environment | keep conservative safety-supported hold |
| ASD-0547 | only title-level official evidence was safely reachable from the SPIE landing path | keep conservative safety-skip hold |
| ASD-0553 | official platform evidence still reads as a bioinformatics automation substrate without object-level life/medical case results | keep conservative safety-skip hold |

## 6. Multi-Agent Audit Trace

- `Evidence-Agent-A/B/C`
  - completed disjoint evidence packets for the remaining `10` open records
- `Classification-Reviewer`
  - returned `4` high-confidence direct landings and `6` conservative holds
- `Writeback-Agent-1`
  - owned and changed:
    - `Lin_2025_High_Throughput_Electrochemistry_Discovery.md`
    - `Niu_2025_Bayesian_Catalyst_Discovery_Iridium.md`
- `Writeback-Agent-2`
  - owned and changed:
    - `Takahara_2025_MatAgent_Inorganic_Materials.md`
    - `Wang_2026_TCM_Agent_Herbal_Discovery.md`
- `Main Controller`
  - inspected all landed note diffs
  - confirmed disjoint note ownership
  - updated the master list
  - updated the progress tracker
  - wrote this partial report
  - closed all completed round agents immediately after completion packets returned

## 7. 本 partial 后的统计变化

- confirmed included-and-classified record count remains `451`
- current progress tracker reviewed-row count remains `373`
- current progress tracker `closed=yes`: `263 -> 267`
- current progress tracker `closed=no`: `110 -> 106`
- batch-16 cumulative landed count: `20 -> 24`
- batch-16 cumulative remaining conservative/open count: `10 -> 6`

## 8. Next Step

`Batch 16` 的 stronger-source follow-up 已推进到：

- landed `24`
- conservative/open `6`

下一步不应跳到 `ASD-0554+`，而应继续只处理 `Batch 16` 剩余的 `6` 篇 `closed=no` 队列，并继续保持 safety-visible closeout discipline：

- ordinary conservative holds:
  - `ASD-0531`
  - `ASD-0544`
- safety-visible / safety-supported holds:
  - `ASD-0541`
  - `ASD-0545`
- safety-skip holds:
  - `ASD-0547`
  - `ASD-0553`
