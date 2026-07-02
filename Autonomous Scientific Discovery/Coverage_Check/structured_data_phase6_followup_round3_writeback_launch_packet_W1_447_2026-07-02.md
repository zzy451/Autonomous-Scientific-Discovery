# ASD Phase 6 follow-up round 3 writeback launch packet

Date: 2026-07-02
Round label: `Phase6FollowupR3`
Owned agent: `Writeback-Agent-1`

This packet freezes the only approved writeback subset for the current round. The owned note list is disjoint and complete for this round.

## Ownership

Owned note files:

- `Notes/01_Formal_Information_and_Computational_Sciences/Gandhi_2025_ResearchCodeAgent.md`
- `Notes/03_Chemical_Sciences/Callahan_2025_CRAG_MoW.md`
- `Notes/03_Chemical_Sciences/Bran_2024_ChemCrow.md`

Do not edit:

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- any round report under `Coverage_Check/`
- any note file outside the three owned files above

## Approved landing subset

The controller-approved landed subset for this round is exactly:

- `ASD-0089`
- `ASD-0091`
- `ASD-0093`

No other paper may be added to writeback in this round.

## Per-paper adjudication rows

### ASD-0089

- paper_id: `ASD-0089`
- title: `Researchcodeagent: An llm multi-agent system for automated codification of research methodologies`
- note_path: `Notes/01_Formal_Information_and_Computational_Sciences/Gandhi_2025_ResearchCodeAgent.md`
- supported_modules: `01`
- final_01_04_bucket: `none`
- primary_module_for_filing: `01`
- source_limited: `no`
- safety_access_status: `local_pdf`
- sections_to_refresh: `archive-sync header; Evidence Log; 2.1-2.3; 5.3; 8; 9.3`
- final_reason: `Concrete ML codification/evaluation tasks provide formal-computational object coverage, so it should not remain 01.04-only.`

### ASD-0091

- paper_id: `ASD-0091`
- title: `Agentic mixture-of-workflows for multi-modal chemical search`
- note_path: `Notes/03_Chemical_Sciences/Callahan_2025_CRAG_MoW.md`
- supported_modules: `03;04`
- final_01_04_bucket: `none`
- primary_module_for_filing: `03`
- source_limited: `no`
- safety_access_status: `local_pdf`
- sections_to_refresh: `archive-sync header; Evidence Log; 2.1-2.3; 8; 9.3`
- final_reason: `Small-molecule/reaction tasks plus polymer/material benchmarks support 03;04.`

### ASD-0093

- paper_id: `ASD-0093`
- title: `Augmenting large language models with chemistry tools`
- note_path: `Notes/03_Chemical_Sciences/Bran_2024_ChemCrow.md`
- supported_modules: `03;04;07`
- final_01_04_bucket: `none`
- primary_module_for_filing: `03`
- source_limited: `no`
- safety_access_status: `local_pdf`
- sections_to_refresh: `archive-sync header; Evidence Log; 2; 5; 6-7`
- final_reason: `Organic synthesis, materials-design, and drug-discovery tasks all have concrete object-level support.`

## Expected writeback style

- apply the adjudicated modules exactly
- preserve note location as filing convenience only
- remove legacy wording that still presents these papers as `01.04`-only, `03`-only, or source-limited when the adjudicated row now says otherwise
- keep the evidence wording tied to already checked local PDF / full-text status
- do not expand or retract modules beyond the adjudicated row

## Return contract

Return:

- owned note files
- changed note files
- whether each changed note was archive-sync only or also classification-wording updated
- any intentionally unchanged owned note
- any blocker that prevented completion
