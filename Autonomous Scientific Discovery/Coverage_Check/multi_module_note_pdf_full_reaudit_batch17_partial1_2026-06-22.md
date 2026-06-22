# Batch 17 Partial-1 Multi-Module / Note / PDF Reaudit Report

Generated: `2026-06-22`  
Coverage: the next 30 confirmed-core records in flat master-list row order after `ASD-0553`: `ASD-0554`, `ASD-0556`, `ASD-0557`, `ASD-0558`, `ASD-0564`, `ASD-0565`, `ASD-0567`, `ASD-0568`, `ASD-0569`, `ASD-0570`, `ASD-0571`, `ASD-0572`, `ASD-0573`, `ASD-0574`, `ASD-0575`, `ASD-0576`, `ASD-0577`, `ASD-0579`, `ASD-0581`, `ASD-0582`, `ASD-0586`, `ASD-0587`, `ASD-0589`, `ASD-0590`, `ASD-0591`, `ASD-0592`, `ASD-0617`, `ASD-0618`, `ASD-0596`, and `ASD-0597`.  
Mode: `Batch 17 partial-1`; this round followed the plan-defined structure with in-session `Evidence-Agent-A/B`, reuse of the already completed third evidence slice, one independent `Classification-Reviewer`, two disjoint `Writeback-Agent`s, and `Main Controller` single-writer closeout.

## 1. 本次收口结果

- 本次直接落地 `8` 篇：
  - `ASD-0557`
  - `ASD-0571`
  - `ASD-0573`
  - `ASD-0574`
  - `ASD-0577`
  - `ASD-0586`
  - `ASD-0592`
  - `ASD-0618`
- 本次已审但保守挂起 `22` 篇：
  - `ASD-0554`
  - `ASD-0556`
  - `ASD-0558`
  - `ASD-0564`
  - `ASD-0565`
  - `ASD-0567`
  - `ASD-0568`
  - `ASD-0569`
  - `ASD-0570`
  - `ASD-0572`
  - `ASD-0575`
  - `ASD-0576`
  - `ASD-0579`
  - `ASD-0581`
  - `ASD-0582`
  - `ASD-0587`
  - `ASD-0589`
  - `ASD-0590`
  - `ASD-0591`
  - `ASD-0617`
  - `ASD-0596`
  - `ASD-0597`
- 本次没有新增 `safety_skip`；所有未落地记录要么是 `source_limited`，要么是本 partial 为了保持 landed subset 与已完成 writeback ownership 一致而主动延后到后续 partial 的强样本。

## 2. 结果概览

- landed notes updated: `8`
- landed master rows updated: `8`
- progress rows added this round: `30`
- `closed=yes` added: `8`
- `closed=no` added: `22`
- 本次 landed subset 没有 shared note-path ownership 冲突

## 3. Landed Record-Level Outcomes

| ID | Final modules or bucket | PDF / source status | Closeout note |
|---|---|---|---|
| ASD-0557 | `03` | publisher full text + PDF route checked | RSC 一手全文将桥连偶氮苯异构化机理、IR/Raman 光谱和机器人实验验证写实后，稳定落在 `03`，不进入 `01.04` |
| ASD-0571 | `04` | author PDF checked; no local archive | CRYSTAL 的 author PDF 已足够支撑材料晶体结构映射与相图生成对象，`04` 明确优于 `01.04` |
| ASD-0573 | `04` | publisher full text + PDF route checked | 直接优化对象是 lead-free perovskite nanocrystals 与 PLQY，材料对象证据强，`04` 落地稳定 |
| ASD-0574 | `06` | publisher full text + PDF route checked; local preprint archive exists | GeneAgent 明确围绕 gene-set / GO / pathway knowledge 展开，生命科学对象证据充分，`01.04` 排除清楚 |
| ASD-0577 | `04` | publisher full text + PDF route checked | 多机器人闭环最终优化的是 perovskite nanocrystal 材料性能而非通用平台，维持 `04` |
| ASD-0586 | `03` | publisher full text + PDF route checked | hybrid organic-enzymatic synthesis planning 的一手全文将对象牢牢锚定在具体化学合成路径上，`03` 可直接落地 |
| ASD-0592 | `04` | publisher PDF checked; no local archive | CASH 闭环直接优化 `Nb-doped TiO2 thin films` 的材料性质，材料对象稳定，`04` 落地 |
| ASD-0618 | `06` | publisher full text + PDF route checked | PLM + biofoundry 的真实对象是蛋白变体与蛋白功能优化，平台感不改变其 `06` 归属 |

## 4. Conservative Carry-Forward Logic

本轮 `22` 篇未落地不代表它们被否定，而是分成两类保守处理：

- `source_limited` / access-limited holds：
  - `ASD-0554`
  - `ASD-0556`
  - `ASD-0558`
  - `ASD-0564`
  - `ASD-0565`
  - `ASD-0567`
  - `ASD-0569`
  - `ASD-0570`
  - `ASD-0572`
  - `ASD-0575`
  - `ASD-0576`
  - `ASD-0587`
  - `ASD-0617`
  - `ASD-0596`
- first-hand reviewed but intentionally deferred to a later `Batch17` partial so this partial only lands records whose note writeback ownership was fully frozen and returned：
  - `ASD-0568`
  - `ASD-0579`
  - `ASD-0581`
  - `ASD-0582`
  - `ASD-0589`
  - `ASD-0590`
  - `ASD-0591`
  - `ASD-0597`

第二组并不是对象归类不稳；它们已经有较强的一手证据，但本 partial 没把它们纳入 writeback-frozen landed subset，因此统一先登记进 progress、保留在 `closed=no`，避免主控在没有对应 note writeback packet 的情况下越过 plan 直接落 master closeout。

## 5. Multi-Agent Audit Trace

- `Evidence-Agent-A/B`
  - 在当前会话内创建并完成了前 20 篇只读取证 packet。
- third evidence slice
  - 复用了本轮开始前已经完成的 `evidence_C`，没有重复起第三个同类 agent。
- `Classification-Reviewer`
  - 只基于 merged evidence pack 返回了 30 篇的 adjudication、landing-now list、conservative list 与 no-safety-skip conclusion。
- `Writeback-Agent-1`
  - 正常完成并回包，改写了 4 个 disjoint notes。
- initial `Writeback-Agent-2`
  - 连续未回 packet 且未落地改动，被主控关闭。
- replacement `Writeback-Agent-2`
  - 接管同一组 disjoint notes，完成 4 个 note 的 evidence-log / classification sync 并回包。
- `Main Controller`
  - 审查了 8 个 landed note diff
  - 审查 evidence packets 与 reviewer adjudication
  - 更新 `agent_master_paper_list.md`
  - 更新 `multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
  - 写入本 partial report

## 6. 本次后统计变化

- confirmed included-and-classified record count remains `451`
- expanded module assignment count remains `556`
- independent `01.04` bucket count remains `11`
- progress tracker reviewed-row count: `193 -> 223`
- progress tracker `closed=yes`: `164 -> 172`
- progress tracker `closed=no`: `29 -> 51`
- progress-unregistered remainder after this partial: `228`
- safety-open queue remains unchanged; no new safety case was added beyond the previously carried `ASD-0054`

## 7. Next Step

因为本批 30 篇已经全部写入 progress：

- 下一个 flat master-order 未登记起点应移到 `ASD-0597` 之后的下一条 confirmed-core 记录。
- 同时，本轮 `closed=no` 的 `22` 篇已经显式进入后续 follow-up queue，不应再被当作“未处理”记录。
- 如果继续沿 row order 推进，应从 `ASD-0597` 之后的下一批 confirmed-core 记录起新 round；如果优先收口本轮 carry-forward queue，则应明确以 `Batch17` deferred set 作为单独 follow-up partial 处理。  
