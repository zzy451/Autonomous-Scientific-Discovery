# ASD Phase 6 follow-up round 8 closeout

Date: 2026-07-03
Round label: `Phase6FollowupR8`

This file will record the controller closeout for the fresh bounded six-paper follow-up round.

## 1. Round scope

Frozen focus set:

- `ASD-0572`
- `ASD-0735`
- `ASD-0727`
- `ASD-0859`
- `ASD-0860`
- `ASD-0861`

## 2. Agent return status

- `Evidence-Agent-A` (`Lorentz`): completed; usable evidence rows returned for `ASD-0572`, `ASD-0735`.
- `Evidence-Agent-B` (`Locke`): completed; usable evidence rows returned for `ASD-0727`, `ASD-0859`.
- `Evidence-Agent-C` (`Lagrange`): completed; usable evidence rows returned for `ASD-0860`, `ASD-0861`.
- `Classification-Reviewer` (`Pauli`): completed; usable adjudication file landed at `Coverage_Check/structured_data_phase6_followup_round8_classification_review_447_2026-07-03.tsv`.
- `PDF-Archive-Agent` (`Raman`): completed; successfully archived `ASD-0735` to `Reference_PDF/04_Materials_Science/Epps_2020_Artificial_Chemist_Quantum_Dot.pdf`.
- `Writeback-Agent-1` (`Hilbert`): completed; changed exactly 3 owned notes:
  - `Notes/04_Materials_Science/Wu_2025_Random_Heteropolymer_Blends.md`
  - `Notes/04_Materials_Science/Epps_2020_Artificial_Chemist_Quantum_Dot.md`
  - `Notes/05_Earth_and_Environmental_Sciences/Liang_2026_GeoAgentic_RAG.md`
- Controller post-writeback independent read-only review confirmed the note diffs are consistent with the reviewer/controller ceiling and that only `ASD-0735` should land in the authoritative pair this round.

## 3. Merged evidence summary

- `ASD-0572`: official publisher preview plus ChemRxiv lead materially strengthen the existing `04;06` reading, but no retrievable full text or local PDF was verified in this environment; keep `source_limited=yes`.
- `ASD-0735`: legal NSF PAR accepted-manuscript PDF provides first-hand full-text evidence for autonomous quantum-dot material optimization; the local archived copy is readable and supports removing `source_limited`.
- `ASD-0727`: DOI/article page plus HKU Scholars Hub record and visible repository-PDF lead strengthen the concrete geospatial / Earth-observation anchor for `05`, but the repository PDF was not actually retrieved in this environment; keep `source_limited=yes`.
- `ASD-0859`, `ASD-0860`, `ASD-0861`: official abstract/article-page evidence plus JPL / NASA materials further stabilize the `05` Earth-science reading, but exact article full text/PDF was still not verified; keep conservative hold.

## 4. Controller decision

- authoritative landing:
  - `ASD-0735`
- note-only refresh:
  - `ASD-0572`
  - `ASD-0727`
- conservative hold:
  - `ASD-0859`
  - `ASD-0860`
  - `ASD-0861`

Authoritative landing details for `ASD-0735`:

- `agent_master_paper_list.md` updated with local archived PDF path `Reference_PDF/04_Materials_Science/Epps_2020_Artificial_Chemist_Quantum_Dot.pdf`
- progress row updated from `abstract_only_checked` / `source_limited_review_packet` / `source_limited=yes` to:
  - `pdf_status=archived_pdf`
  - `pdf_path=Reference_PDF/04_Materials_Science/Epps_2020_Artificial_Chemist_Quantum_Dot.pdf`
  - `evidence_status=first_hand_full_text`
  - `source_limited=no`
  - `batch=Phase6FollowupR8`
- note wording for `ASD-0735` now explicitly states that the local readable file is an NSF PAR accepted-manuscript archive rather than a Wiley version-of-record PDF.

Explicit non-landings:

- `ASD-0572` and `ASD-0727` did not receive authoritative-pair changes in this round.
- `ASD-0859`, `ASD-0860`, and `ASD-0861` did not receive note writeback or authoritative changes in this round.

## 5. Baseline and git verification

- Controller reran the structured-data pipeline after the bounded authoritative landing:
  - `python "Autonomous Scientific Discovery/scripts/export_structured_data.py"`
  - `python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"`
  - `python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"`
  - `python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" summary`
- Verified baseline after `ASD-0735` landing:
  - active confirmed-core = `447`
  - active local PDF = `422`
  - active no-local-PDF = `25`
  - canonical `01.04` bucket = `9`
  - workflow mirror semantic drift = `0`
  - workflow mirror order drift = `0`
- `check_data_consistency.py` passes under the updated authoritative baseline, confirming the bounded landing did not introduce canonical / mirror drift.
