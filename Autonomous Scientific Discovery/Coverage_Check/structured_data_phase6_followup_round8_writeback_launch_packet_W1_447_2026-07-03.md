# ASD Phase 6 follow-up round 8 writeback launch packet W1

Date: 2026-07-03
Round label: `Phase6FollowupR8`
Writeback role: `Writeback-Agent-1`

## 1. Owned note files

This writeback ownership list is frozen and disjoint:

- `Notes/04_Materials_Science/Wu_2025_Random_Heteropolymer_Blends.md`
- `Notes/04_Materials_Science/Epps_2020_Artificial_Chemist_Quantum_Dot.md`
- `Notes/05_Earth_and_Environmental_Sciences/Liang_2026_GeoAgentic_RAG.md`

## 2. Approved landing subset

### `ASD-0572`

- landing scope: note-only refresh
- final adjudication:
  - `supported_modules=04;06`
  - `final_01_04_bucket=none`
  - `primary_module_for_filing=04`
  - `source_limited=yes`
- refresh target:
  - strengthen evidence wording from abstract-only packet to official publisher preview + ChemRxiv lead
  - keep the `06` add-on
  - do not claim local PDF retrieval or resolved full-text access

### `ASD-0735`

- landing scope: authoritative-plus-note
- final adjudication:
  - `supported_modules=04`
  - `final_01_04_bucket=none`
  - `primary_module_for_filing=04`
  - `source_limited=no`
- confirmed archive result:
  - `Reference_PDF/04_Materials_Science/Epps_2020_Artificial_Chemist_Quantum_Dot.pdf`
  - archive source: `https://par.nsf.gov/servlets/purl/10165734`
  - archive status: success
  - readability: confirmed readable PDF
- refresh target:
  - update PDF path / first-hand source wording
  - replace old source-limited wording with accepted-manuscript full-text wording
  - keep stable `04` materials framing

### `ASD-0727`

- landing scope: note-only refresh
- final adjudication:
  - `supported_modules=05`
  - `final_01_04_bucket=none`
  - `primary_module_for_filing=05`
  - `source_limited=yes`
- refresh target:
  - correct stale note-front wording that currently says `source_limited=no`
  - add HKU Scholars Hub record and visible repository-PDF lead as stronger evidence
  - keep explicit `05`, not `01.04`
  - do not claim the repository PDF was actually retrieved in this environment

## 3. Hard constraints

- Edit only the three owned note files above.
- Do not edit `agent_master_paper_list.md`.
- Do not edit progress files.
- Do not edit round reports.
- Do not edit files outside the owned list.
- Do not add or remove modules beyond the adjudicated rows.
- Keep note location as filing convenience, not classification authority.

## 4. Expected return packet

Return:

- owned files
- changed files
- whether each note change was archive-sync only or also classification-wording updated
- intentionally unchanged files, if any
- blockers, if any
