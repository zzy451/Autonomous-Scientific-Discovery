# Batch 25 Partial-1 Multi-Module / Note / PDF Reaudit Report

Generated: `2026-06-23`  
Coverage: the current 30-paper unresolved confirmed-core slice in flat master-list row order: `ASD-0682`, `ASD-0688`, `ASD-0695`, `ASD-0696`, `ASD-0697`, `ASD-0698`, `ASD-0700`, `ASD-0702`, `ASD-0705`, `ASD-0706`, `ASD-0707`, `ASD-0713`, `ASD-0716`, `ASD-0717`, `ASD-0719`, `ASD-0721`, `ASD-0724`, `ASD-0725`, `ASD-0727`, `ASD-0728`, `ASD-0729`, `ASD-0731`, `ASD-0734`, `ASD-0735`, `ASD-0736`, `ASD-0737`, `ASD-0738`, `ASD-0741`, `ASD-0743`, and `ASD-0744`.  
Mode: `Batch25Partial1`; this closeout follows the plan-defined split: read-only evidence agents, one independent classification reviewer, three disjoint writeback agents, and single-writer controller closeout for master / progress / report.

## 1. 本次落地范围

- 本次直接落地 `24` 篇：
  - `ASD-0682`
  - `ASD-0688`
  - `ASD-0695`
  - `ASD-0696`
  - `ASD-0697`
  - `ASD-0698`
  - `ASD-0705`
  - `ASD-0707`
  - `ASD-0713`
  - `ASD-0716`
  - `ASD-0717`
  - `ASD-0719`
  - `ASD-0721`
  - `ASD-0725`
  - `ASD-0727`
  - `ASD-0728`
  - `ASD-0729`
  - `ASD-0731`
  - `ASD-0734`
  - `ASD-0735`
  - `ASD-0736`
  - `ASD-0738`
  - `ASD-0741`
  - `ASD-0744`
- 本次继续保守挂起 `6` 篇：
  - `ASD-0700`
  - `ASD-0702`
  - `ASD-0706`
  - `ASD-0724`
  - `ASD-0737`
  - `ASD-0743`
- 本次没有新增 `safety_skip`。
- 本次显式撤销了旧的错误 safety 口径：
  - `ASD-0696`：从旧 `safety_skip` 改为安全可访问的一手来源，最终 closed with `source_limited=yes`
  - `ASD-0743`：从旧 `safety_skip` 改为安全可访问的一手摘要证据，但本轮仍 conservative
  - `ASD-0744`：从旧 `safety_skip` 改为安全可访问的一手 abstract / API 证据，最终 closed with `source_limited=yes`

## 2. 结果概览

- closed records in this partial slice: `24`
- conservative carry-forward records: `6`
- notes updated: `24`
- master rows updated by controller closeout: `30`
- progress rows updated: `30`
- newly archived local PDFs in this slice: `0`
- landed records with `source_limited=yes`: `5`
- landed records with `source_limited=no`: `19`
- the most important closeout corrections in this slice:
  - `ASD-0696`, `0697`, `0719`, `0721`: stabilize relaxed `05;10` multi-module treatment with `10` as `primary_module_for_filing`
  - `ASD-0698`, `0705`, `0717`: keep scientific knowledge production / reproducibility objects in `11`, not `01.04`
  - `ASD-0731`: make `03;06;07` multi-module object coverage explicit instead of leaving the record effectively `06`-only
  - `ASD-0736`, `0738`: retire stale independent `01.04` wording and keep both records in concrete computational-research module `01`
  - `ASD-0744`: remove stale `not accessed due to safety` wording and replace it with safe first-hand `source_limited` coverage in `06`

## 3. Record-Level Outcomes

| ID | Final modules or bucket | PDF / source status | Closeout note |
|---|---|---|---|
| ASD-0682 | `04` | arXiv PDF checked | solid-state simulation workflow remains a concrete materials object case, not `01.04` |
| ASD-0688 | `09` | arXiv PDF + ar5iv checked | concrete CFD workflow validation keeps the record in engineering |
| ASD-0695 | `08` | arXiv PDF checked | flavor / food-science object stays primary; chemistry remains a boundary note only |
| ASD-0696 | `05;10` | safe repository abstract / attached PDF checked; source-limited closeout | old safety skip retired; rover mission autonomy stays primary with Mars surface target coverage retained |
| ASD-0697 | `05;10` | accepted-manuscript PDF checked | Curiosity / ChemCam deployment supports mission-science autonomy plus planetary-surface science coverage |
| ASD-0698 | `11` | arXiv PDF checked | APRES is a scientific knowledge-production / manuscript-evaluation record, not `01.04` |
| ASD-0705 | `11` | arXiv PDF checked | reproducibility auditing of published science remains a clean `11` landing |
| ASD-0707 | `02` | arXiv abstract checked | fundamental-physics object coverage remains stable in `02` |
| ASD-0713 | `10` | JPL-hosted PDF checked | Europa biology / geology remain mission context only; do not expand to `05` or `06` |
| ASD-0716 | `07` | arXiv abstract checked | CAR-T therapeutic-development pipeline remains a stable health-science object |
| ASD-0717 | `11` | arXiv abstract checked | literature discovery / organization / knowledge-graph construction remain direct `11` coverage |
| ASD-0719 | `05;10` | official PDF / NTRS / JPL pages checked | EO-1 mission autonomy stays primary while Earth-event detection supports `05` |
| ASD-0721 | `05;10` | AAAI official PDF checked | onboard event detection and replanning justify `05;10` with `10` primary |
| ASD-0725 | `05` | arXiv abstract checked | atmospheric-environment mechanism validation remains a clean Earth / environment object |
| ASD-0727 | `05` | official abstract checked; source-limited closeout | framework wording does not override concrete geospatial reasoning task coverage |
| ASD-0728 | `06` | arXiv abstract checked | virtual-cell and single-cell multi-omics modeling remain direct life-science object coverage |
| ASD-0729 | `06` | arXiv abstract checked | protein discovery and directed evolution remain direct biological object coverage |
| ASD-0731 | `03;06;07` | first-hand abstract-level packet closed | chemistry, biological knowledge extraction, and pharmacological property tasks all remain explicit |
| ASD-0734 | `03` | first-hand abstract-level packet closed | reaction-space reactivity discovery remains a clean chemistry object |
| ASD-0735 | `04` | source-limited abstract / publisher-link packet closed | quantum-dot material-property optimization remains a materials object case |
| ASD-0736 | `01` | arXiv abstract checked | stale independent `01.04` wording removed; computational-research tasks anchor the record in `01` |
| ASD-0738 | `01` | arXiv abstract checked | AI model discovery and reproduction tasks keep the record in `01` |
| ASD-0741 | `06` | abstract / API packet closed as source-limited | spatial transcriptomics pancreas-maturation analysis remains a direct life-science object |
| ASD-0744 | `06` | abstract / API packet closed as source-limited | old safety skip retired; current first-hand evidence supports bioinformatics / multi-omics object coverage in `06` |

## 4. Conservative Carry-Forward

| ID | Current hold reason | Current status |
|---|---|---|
| ASD-0700 | current evidence remains too position-paper-like; inclusion/core strength still too weak to close | keep conservative |
| ASD-0702 | rover-science direction is stable, but current source depth is still too thin for closeout | keep conservative |
| ASD-0706 | publication-ecosystem object points to `11`, but abstract-only evidence is still too thin to close | keep conservative |
| ASD-0724 | title-level first-hand evidence points to `06`, but current source access remains too limited | keep conservative |
| ASD-0737 | module `01` direction is stable, but broader cross-domain hints are still too weak to close aggressively | keep conservative |
| ASD-0743 | old safety skip retired; `06;07` remains directionally supported, but current abstract-only evidence is still too limited for closeout | keep conservative |

## 5. Multi-Agent Audit Trace

- `Evidence-Agent-A/B/C` returned non-overlapping evidence packs for the 30-paper slice.
- `Classification-Reviewer` returned:
  - direct high-confidence landings: `16`
  - explicit conservative holds: `6`
  - no current safety-skip cases
- Main-controller freeze decision:
  - accepted the 6 conservative holds unchanged
  - additionally landed 8 medium-to-high-confidence rows after evidence review:
    - `ASD-0695`
    - `ASD-0696`
    - `ASD-0719`
    - `ASD-0727`
    - `ASD-0729`
    - `ASD-0735`
    - `ASD-0736`
    - `ASD-0744`
- `Writeback-Agent-1` owned and changed:
  - `ASD-0682`, `0688`, `0695`, `0696`, `0697`, `0698`, `0705`, `0707`
- `Writeback-Agent-2` owned and changed:
  - `ASD-0713`, `0716`, `0717`, `0719`, `0721`, `0725`, `0727`, `0728`
- `Writeback-Agent-3` owned and changed:
  - `ASD-0729`, `0731`, `0734`, `0735`, `0736`, `0738`, `0741`, `0744`
- all three writeback agents returned with:
  - no ownership overlap
  - no blockers
  - note wording updated to the frozen adjudications
- all round agents were closed immediately after completion.

## 6. 本轮后的累计进度

- confirmed core total remains `451`
- reviewed records: `373 -> 373`
- `closed=yes`: `318 -> 342`
- `closed=no`: `55 -> 31`
- not yet entered progress: `78 -> 78`
- remaining unresolved confirmed-core records by controller closeout definition: `109`
  - still open in progress: `31`
  - not yet entered progress: `78`

## 7. Next Step

The current 30-paper unresolved slice is now partially landed as:

- landed: `24`
- still conservative/open: `6`

The next controller action is to continue from the next unresolved confirmed-core record in current flat master-list row order, while keeping these six conservative holds explicit in the progress tracker.
