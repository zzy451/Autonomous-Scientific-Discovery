# Batch 02 Partial-11 Multi-Module / Note / PDF Reaudit Report

Generated: `2026-06-21`  
Coverage: the next confirmed-core flat positions after `ASD-0083`, skipping `ASD-0086`, `ASD-0087`, `ASD-0088`, and `ASD-0092` because they are not active confirmed-core landing targets in the current flat pass, and closing `ASD-0084`, `ASD-0085`, `ASD-0089`, `ASD-0090`, `ASD-0091`, and `ASD-0093`.  
Mode: `Batch 02 partial-11`; this closeout used the upgraded plan-defined structure: `Evidence-Agent-A/B/C` for read-only first-hand evidence collection, `Classification-Reviewer` for independent adjudication, `Writeback-Agent-1/2/3` for disjoint note writeback, and `Main Controller` for final master-list editing, recounting, progress/report updates, and git closeout.

## 1. What Was Closed In This Partial Slice

- `ASD-0084` now has an archived local PDF and remains a stable `04` materials-science record, while this landing stays explicitly `source_limited`.
- `ASD-0085` now has an archived local PDF and lands as relaxed multi-module `04;06`, with `06` retained as the filing anchor and `04` added for protein-materials / mechanical-property object coverage.
- `ASD-0089` now has an archived local PDF and is no longer treated as a pure `01.04` general-method record; the current landing is concrete formal-computational `01`.
- `ASD-0090` now has an archived local PDF and stays a stable `02` record because the validated object is quantum-physics experimentation on a superconducting quantum processor.
- `ASD-0091` now has an archived local PDF and lands as `03;04`, keeping chemistry as the filing anchor while adding materials-related benchmark coverage conservatively.
- `ASD-0093` now has an archived local PDF and lands as `03;04;07`, with chemistry retained for filing and materials / drug-discovery coverage accepted conservatively under the relaxed object-coverage rule.

## 2. Record-Level Outcomes

| ID | Title | Authoritative modules or bucket | PDF / source status | Outcome |
|---|---|---|---|---|
| ASD-0084 | Automating alloy design and discovery with physics-aware multimodal multiagent ai | `04` | archived project PDF | keep stable single-module materials record; source-limited landing |
| ASD-0085 | Protagents: protein discovery via large language model multi-agent collaborations combining physics and machine learning | `04;06` | archived project PDF | land relaxed multi-module protein-science plus materials-coverage record |
| ASD-0089 | Researchcodeagent: An llm multi-agent system for automated codification of research methodologies | `01` | archived project PDF | remove stale pure `01.04` treatment and land concrete formal-computational record |
| ASD-0090 | Agents for self-driving laboratories applied to quantum computing | `02` | archived project PDF | keep stable quantum-physics / self-driving-lab record |
| ASD-0091 | Agentic mixture-of-workflows for multi-modal chemical search | `03;04` | archived project PDF | keep chemistry filing anchor and add cautious materials benchmark coverage |
| ASD-0093 | Augmenting large language models with chemistry tools | `03;04;07` | archived project PDF | land broadest multi-module expansion in the slice, conservatively and source-limited |

## 3. Boundary Notes

`ASD-0084`  
The current landing remains conservative. Everything stable in the checked source trail still points to alloy / material-property discovery, so there is no reason to drift toward a general workflow bucket or force extra modules.

`ASD-0085`  
This is the clearest `04 / 06` boundary paper in the slice. Protein-design and protein-structure tasks keep `06` as the filing anchor, while targeted mechanical-property and protein-materials-style objectives are sufficient for relaxed `04` add-on coverage.

`ASD-0089`  
This paper should no longer remain in the independent `01.04` bucket. Under the current rule, research-method codification and computational reproduction benchmark tasks count as concrete formal-computational object coverage in `01`.

`ASD-0090`  
Despite the strong self-driving-lab framing, the directly validated object is still quantum-physics experimentation on a superconducting quantum processor, so `02` stays stable.

`ASD-0091`  
Chemistry remains the filing anchor, but polymer / materials-related benchmark coverage is enough to support cautious `04` add-on recording under the relaxed rule.

`ASD-0093`  
This is the broadest and most source-limited module expansion in the slice. Chemistry remains primary, while materials-design and drug-discovery-facing task coverage are accepted as auxiliary object modules rather than equal-contribution claims.

## 4. Partial Statistics

- Closed records in this partial slice: `6`
- Archived local PDFs confirmed in this slice: `6`
- Notes updated: `6`
- Master rows updated: `6`
- Source-limited landings in this slice: `6`
- Final distribution inside this partial slice: `04 x1`, `04;06 x1`, `01 x1`, `02 x1`, `03;04 x1`, `03;04;07 x1`

## 5. Multi-Agent Audit Trace

- `Evidence-Agent-A/B/C` collected the first-hand evidence for this slice within the current 30-paper evidence round.
- `Classification-Reviewer` independently returned the landed outcomes:
  - `ASD-0084 -> 04`
  - `ASD-0085 -> 04;06`
  - `ASD-0089 -> 01`
  - `ASD-0090 -> 02`
  - `ASD-0091 -> 03;04`
  - `ASD-0093 -> 03;04;07`
- `Writeback-Agent-1/2/3` returned disjoint note edits for the six note files in this slice.
- No paper in this partial slice required `safety_skip` or `not accessed due to safety`.

## 6. Next Step

Continue the same already-reviewed 30-paper evidence round in flat row order, starting from `ASD-0094`.
