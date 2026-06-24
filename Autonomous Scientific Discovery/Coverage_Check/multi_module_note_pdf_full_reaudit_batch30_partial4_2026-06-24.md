# Batch 30 Partial-4 Final Open Conservative Refresh Report

Generated: 2026-06-24
Coverage: the remaining 3-paper open confirmed-core queue in flat master-list row order: ASD-0466, ASD-0623, ASD-0838.
Mode: Batch30Partial4; this closeout follows the plan-defined multi-agent structure for the final open queue, with `Evidence-Agent-A/B/C`, one independent `Classification-Reviewer`, one disjoint `Writeback-Agent-1`, and single-writer controller closeout for progress / report only. No `PDF-Archive-Agent` was used because only one small legal PDF-supporting artifact required local archiving.

## 1. 本轮结果

- 本轮新增 `closed=yes`：`0`
- 本轮继续保守挂起：`3`
  - `ASD-0466`
  - `ASD-0623`
  - `ASD-0838`
- 本轮新增 `safety_skip`：`0`

## 2. 收口摘要

- note files updated: `3`
- master rows updated by controller closeout: `0`
- progress rows updated: `3`
- newly archived local supporting PDF assets: `1`
  - `ASD-0466`: official ACS supplementary PDF archived locally
- newly archived legal main-article PDFs: `0`
- key closeout points:
  - `ASD-0466`: no legal main-article PDF was available in this environment, but the official ACS supplementary PDF was legally accessible and is now archived locally; this upgrades the old abstract-only hold into a stronger first-hand conservative hold without forcing `closed=yes`.
  - `ASD-0623`: the `05` climate-science direction remains stable, but as of 2026-06-24 the official arXiv record is still withdrawn, `/pdf` remains unavailable, and the cited repo is broken; keep the record open conservatively.
  - `ASD-0838`: chemistry remains the primary filing, and this round adds explicit source-limited secondary `04` support from ORNL-reported materials-side results; however, official ChemRxiv full/PDF access remained Cloudflare-blocked in this environment, so the record stays open.

## 3. 逐篇结果

| ID | Final outcome | PDF / source status | Closeout note |
|---|---|---|---|
| ASD-0466 | `04` conservative hold | official ACS abstract + official supplementary PDF checked; supplementary PDF archived locally; main article gated | object direction is stably materials-side CNT growth selectivity, but accessible first-hand evidence still under-specifies stronger autonomous Agent decision-making |
| ASD-0623 | `05` conservative hold | withdrawn arXiv landing page checked; no legal local PDF from official routes; cited repo broken | climate-task object coverage still supports `05` rather than `01.04`, but the withdrawn / unstable record is still too source-limited for direct landing |
| ASD-0838 | `03;04` conservative hold with `03` primary | Crossref-linked ChemRxiv `v1` full/PDF URLs identified; official routes blocked by Cloudflare in this environment; no local PDF archived | chemistry remains primary, while ORNL-reported copolymer / materials-side results support secondary `04`; keep conservative until official full text is actually accessed |

## 4. 边界与未收口原因

### ASD-0466

`04` materials classification is no longer the main risk. The remaining blocker is Agent-strength / automation-vs-agent pressure: the accessible abstract plus official supplementary material confirm automated experimentation, in situ Raman monitoring, and model-guided wall-selectivity mapping, but they still do not cleanly document a stronger autonomous next-experiment-deciding Agent loop.

### ASD-0623

`05` remains more stable than `01.04` because the surviving first-hand abstract evidence is still explicitly climate-science-task and climate-benchmark oriented. The blocker is record instability, not classification direction: withdrawn arXiv state, unavailable official PDF/html/src, and broken cited repository.

### ASD-0838

The main classification direction is now clearer than before: `03` primary is stable, and current evidence also makes source-limited secondary `04` support visible. The blocker is still access depth and primary-paper strength rather than `03 / 09 / 01.04` confusion.

## 5. Multi-Agent Trace

- `Evidence-Agent-A` owned `ASD-0466` and returned a stronger first-hand packet from the official ACS abstract plus official supplementary PDF.
- `Evidence-Agent-B` owned `ASD-0623` and reconfirmed the withdrawn arXiv state, missing official PDF, and broken cited repo.
- `Evidence-Agent-C` owned `ASD-0838` and reconfirmed the official ChemRxiv `v1` routes plus ORNL-side first-hand supporting pages, while recording the Cloudflare access block as non-safety `source_limited`.
- `Classification-Reviewer` adjudicated all three as `yes_but_conservative_hold`, with `no` direct landings and `no` safety-skip additions.
- `Writeback-Agent-1` owned exactly the three note files, refreshed note wording, and returned with no blockers.
- All round agents were closed immediately after completion.

## 6. 本轮后的累计进度

- progress file scope remains the original 451-paper audit queue
- progress entered: `451`
- progress `closed=yes`: `448`
- progress `closed=no`: `3`
- still open in progress: `3`
  - `ASD-0466`
  - `ASD-0623`
  - `ASD-0838`
- master-list confirmed core count: `450`
- no new confirmed-core demotions this round
- no new master-list landed rows this round

## 7. 下一步

当前 `451` 篇 confirmed-core full reaudit 仍未完全收口，因为这 `3` 篇在 2026-06-24 的可合法一手来源条件下仍然只能维持 conservative hold。下一步应继续围绕这三篇的合法 full-text / official PDF 可达性推进；若后续环境能安全访问更强一手全文，再决定是否把它们从 `closed=no` 推到 `closed=yes`。
