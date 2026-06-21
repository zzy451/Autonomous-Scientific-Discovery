# Batch 03 Partial-1 Multi-Module / Note / PDF Reaudit Report

Generated: `2026-06-22`  
Coverage: the next 30 confirmed-core records in flat master-list row order after the `ASD-0139` carry-forward point: `ASD-0140`, `ASD-0141`, `ASD-0145`, `ASD-0146`, `ASD-0147`, `ASD-0149`, `ASD-0150`, `ASD-0151`, `ASD-0152`, `ASD-0154`, `ASD-0155`, `ASD-0156`, `ASD-0158`, `ASD-0179`, `ASD-0186`, `ASD-0189`, `ASD-0254`, `ASD-0276`, `ASD-0280`, `ASD-0290`, `ASD-0333`, `ASD-0357`, `ASD-0370`, `ASD-0379`, `ASD-0381`, `ASD-0385`, `ASD-0388`, `ASD-0389`, `ASD-0390`, and `ASD-0410`.  
Mode: `Batch 03 partial-1`; this closeout used the upgraded plan-defined structure: `Evidence-Agent-A/B/C` for read-only first-hand evidence collection, `Classification-Reviewer` for independent adjudication, `Writeback-Agent-1/2/3` for disjoint note writeback, `PDF-Archive-Agent` for archive confirmation, and `Main Controller` for final master-list editing, recounting, progress/report updates, and git closeout.

## 1. 本次落地范围

- 本次直接落地 `19` 篇：
  - `ASD-0140`
  - `ASD-0146`
  - `ASD-0147`
  - `ASD-0149`
  - `ASD-0150`
  - `ASD-0151`
  - `ASD-0152`
  - `ASD-0154`
  - `ASD-0155`
  - `ASD-0156`
  - `ASD-0179`
  - `ASD-0186`
  - `ASD-0189`
  - `ASD-0254`
  - `ASD-0276`
  - `ASD-0280`
  - `ASD-0290`
  - `ASD-0333`
  - `ASD-0390`
- 本次保守挂起 `11` 篇：
  - `ASD-0141`
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
- 本次没有新增 `safety_skip`。

## 2. 结果概览

- closed records in this partial slice: `19`
- conservative carry-forward records: `11`
- archived local PDFs confirmed in this slice: `19`
- notes updated: `19`
- master rows updated: `19`
- newly landed relaxed multi-module expansions:
  - `ASD-0151`: `04 -> 02;04`
  - `ASD-0152`: `06 -> 06;07`
- independent `01.04` bucket exits landed in this slice:
  - `ASD-0146`: `01.04 -> 01`
  - `ASD-0147`: `01.04 -> 01`
- note/master sync landings where relaxed overlay already existed but note / PDF / source trail were still stale:
  - `ASD-0254`: keep `06;07`
  - `ASD-0276`: keep `06;07`

## 3. Record-Level Outcomes

| ID | Final modules or bucket | PDF / source status | Closeout note |
|---|---|---|---|
| ASD-0140 | `11` | archived ACL publisher PDF | retire stale `11.07` wording; this is social-science hypothesis discovery, not science-of-science |
| ASD-0146 | `01` | archived arXiv PDF | concrete computational research tasks displace stale independent `01.04` treatment |
| ASD-0147 | `01` | archived arXiv PDF | LLM-research ideation benchmarks are concrete formal/computational objects, not a pure `01.04` shell |
| ASD-0149 | `03` | archived publisher PDF | stable chemistry reaction-optimization record |
| ASD-0150 | `03` | archived publisher PDF | stable chemistry SDL / reaction-optimization record |
| ASD-0151 | `02;04` | archived publisher PDF | materials filing anchor retained; spontaneous-emission steering and governing-equation discovery add `02` |
| ASD-0152 | `06;07` | archived publisher PDF | single-cell biology remains primary; patient-centered cancer use cases add `07` |
| ASD-0154 | `04` | archived arXiv PDF fallback | Science.org access was blocked here, but first-hand arXiv full text was sufficient |
| ASD-0155 | `04` | archived PMC official PDF | stable metasurface design record |
| ASD-0156 | `04` | archived PMC official PDF | stable materials-analysis / microscopy record |
| ASD-0179 | `03` | archived arXiv PDF | stable chemistry reaction-condition recommendation record |
| ASD-0186 | `11` | archived arXiv PDF | stable scientific peer-review / knowledge-production record in class `11` |
| ASD-0189 | `06` | archived arXiv PDF | keep `06` only; immune/tumor context did not justify independent `07` |
| ASD-0254 | `06;07` | archived arXiv PDF | removed stale note-level `01.04` wording; keep existing relaxed overlay `06;07` |
| ASD-0276 | `06;07` | archived arXiv PDF | keep existing relaxed overlay `06;07`; note and PDF trail now aligned |
| ASD-0280 | `03` | archived publisher PDF | stable chemistry synthesis-development record |
| ASD-0290 | `03` | archived arXiv PDF | keep `03` only; no fresh `04` expansion accepted |
| ASD-0333 | `03` | archived arXiv PDF | stable chemistry-hypothesis rediscovery record |
| ASD-0390 | `04` | archived publisher PDF | stable adhesive-material SDL record |

## 4. 关键边界说明

`ASD-0140`  
这条本轮最重要的变化不是 `11 -> 11` 本身，而是把旧的 `11.07` 口径明确清掉。ACL 一手 PDF 支撑的是 social-science hypothesis discovery，不是 peer review、citation network、科研共同体或 science-of-science 对象本身。

`ASD-0146` 与 `ASD-0147`  
这两条都从旧的独立 `01.04` 叙事回落到正式 `01`。原因不是系统不再通用，而是它们已经对 data engineering、alignment、language modeling、LLM-paper ideation 等 formal / computational research objects 做了明确验证，不能再按“无具体对象实验”的 general-method 样本处理。

`ASD-0151`  
当前最稳的是 `04` filing anchor，但不能再压成单模块。闭环系统既优化 semiconductor metasurface materials，又报告 spontaneous-emission steering 与 governing-equation discovery，因此接受 `02;04`。

`ASD-0152`  
这条本轮从单一 `06` 扩成 `06;07`。单细胞数据摄取与标准化分析当然仍是生命科学对象，但论文同时使用患者样本、多癌种场景和 patient-centered cancer cases，足以记入医学与健康科学。

`ASD-0254`  
这条的 relaxed overlay `06;07` 其实在 master 里已经存在，但 note 仍残留旧的 `01.04` 叙事。本 partial 的作用是把 note、PDF、source trail 和 master overlay 真正对齐。

## 5. Conservative Carry-Forward

| ID | Current hold reason | Current status |
|---|---|---|
| ASD-0141 | access-limited evidence increases `06;07` pressure, but the full-text chain is still thin for a direct master landing | keep conservative |
| ASD-0145 | OpenReview evidence increases `01;11` pressure, but the `01 / 11 / old 01.04` boundary is still better kept conservative for now | keep conservative |
| ASD-0158 | chemistry classification is stable, but direct Science full text / PDF access remained limited in this environment | keep conservative |
| ASD-0357 | accessible homepage supports stable `07`, but no strong independent `06` expansion is accepted without bioRxiv full text | keep conservative |
| ASD-0370 | stable `06` evidence is strong from abstract-level first-hand metadata, but publisher full text remained access-limited | keep conservative |
| ASD-0379 | stable `04` evidence is strong from abstract-level first-hand metadata, but publisher full text remained access-limited | keep conservative |
| ASD-0381 | stable `03` evidence is strong from publisher snippet / metadata, but publisher full text remained access-limited | keep conservative |
| ASD-0385 | current record already pressures `03;04`, but source-limited publisher access kept this round conservative rather than landing a fresh rewrite | keep conservative |
| ASD-0388 | class `04` is stable, but confirmed-core strength remains weaker because the paper is a companion-style characterization agent | keep conservative |
| ASD-0389 | stable `04` evidence is strong from abstract-level metadata, but publisher full text remained access-limited | keep conservative |
| ASD-0410 | stable `04` evidence is strong from abstract-level metadata, but publisher full text remained access-limited | keep conservative |

## 6. Multi-Agent Audit Trace

- `Evidence-Agent-A` covered the first 10-paper contiguous slice:
  - key new pressure points returned: `ASD-0146 -> 01`, `ASD-0147 -> 01`, `ASD-0151 -> 02;04`, `ASD-0152 -> 06;07`
- `Evidence-Agent-B` covered the middle 10-paper contiguous slice:
  - key new pressure points returned: `ASD-0254 -> 06;07`; `ASD-0189` stays `06`; `ASD-0290` stays `03`
- `Evidence-Agent-C` covered the final 10-paper contiguous slice:
  - key new pressure points returned: `ASD-0385 -> 03;04` pressure remains real, but is still source-limited this round
- `Classification-Reviewer` returned:
  - 19 high-confidence direct landings
  - 11 conservative holds
  - no safety-skip additions
- `Writeback-Agent-1/2/3` completed disjoint note writeback for the 19 approved landings.
- `PDF-Archive-Agent` archived all 19 approved PDFs successfully and reported no failures.
- `Main Controller` then:
  - reviewed note writeback quality
  - rejected an over-compressed note rewrite once and required a corrected second pass before accepting it
  - updated `agent_master_paper_list.md`
  - updated the progress tracker
  - refreshed the open boundary queue
  - wrote this partial report

## 7. 本 partial 后的统计变化

- confirmed included-and-classified record count remains `451`
- expanded module assignment count updated from `546` to `550`
- independent `01.04` bucket count decreased from `14` to `12`
- expanded module table changes:
  - `01: 23 -> 25`
  - `02: 37 -> 38`
  - `07: 73 -> 74`

## 8. Next Step

The current 30-paper evidence round is now partially landed as:

- landed: `19`
- still conservative/open: `11`

The next main-controller action after this partial is to keep the open hold set explicit in progress / boundary tracking and then continue the flat master-list row order from the next unresolved confirmed-core record once the current carry-forward status is accepted.
