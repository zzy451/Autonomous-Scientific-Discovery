# ASD Phase 6 follow-up round 8 launch status

Date: 2026-07-03
Round label: `Phase6FollowupR8`

This file records the launch status of the fresh bounded six-paper follow-up round.

## 1. Intended topology

Planned read-only roles:

- `Evidence-Agent-A`
- `Evidence-Agent-B`
- `Evidence-Agent-C`
- `Classification-Reviewer`

Owned slice files:

- `Coverage_Check/structured_data_phase6_followup_round8_slice_A_447_2026-07-03.tsv`
- `Coverage_Check/structured_data_phase6_followup_round8_slice_B_447_2026-07-03.tsv`
- `Coverage_Check/structured_data_phase6_followup_round8_slice_C_447_2026-07-03.tsv`

This round is launch-scoped as:

- read-only evidence collection only
- no note writeback at launch
- no authoritative landing at launch
- no PDF archive write at launch

## 2. Actual launch status

Evidence agents were launched by the controller on `2026-07-03`.

- `Evidence-Agent-A`
  - owned papers: `ASD-0572`, `ASD-0735`
  - agent id: `019f2449-96cc-7022-a58b-f000a3ee9483`
  - nickname: `Lorentz`
  - launch status: `completed`

- `Evidence-Agent-B`
  - owned papers: `ASD-0727`, `ASD-0859`
  - agent id: `019f2449-e911-7ea1-ba96-7284a7cd5919`
  - nickname: `Locke`
  - launch status: `completed`

- `Evidence-Agent-C`
  - owned papers: `ASD-0860`, `ASD-0861`
  - agent id: `019f244a-382b-7730-9f4f-d07f78c5dc2d`
  - nickname: `Lagrange`
  - launch status: `completed`

Controller merge file now exists:

- `Coverage_Check/structured_data_phase6_followup_round8_evidence_merge_template_447_2026-07-03.tsv`

`Classification-Reviewer`, `PDF-Archive-Agent`, and writeback follow-up:

- `Classification-Reviewer`
  - agent id: `019f2455-3c8a-7323-9cd4-c0de6463f9a7`
  - nickname: `Pauli`
  - launch status: `completed`
  - return status: `usable`
  - controller-owned output: `Coverage_Check/structured_data_phase6_followup_round8_classification_review_447_2026-07-03.tsv`

- `PDF-Archive-Agent`
  - agent id: `019f2459-fddb-7853-aa4e-7c6cd0a8b9e3`
  - nickname: `Raman`
  - approved paper: `ASD-0735`
  - launch status: `completed`
  - archive result: success to `Reference_PDF/04_Materials_Science/Epps_2020_Artificial_Chemist_Quantum_Dot.pdf`

- `Writeback-Agent-1`
  - agent id: `019f245d-ddc5-7dd1-b348-5b7bb0b0141a`
  - nickname: `Hilbert`
  - launch status: `completed`
  - return status: `usable`
  - approved owned notes:
    - `Notes/04_Materials_Science/Wu_2025_Random_Heteropolymer_Blends.md`
    - `Notes/04_Materials_Science/Epps_2020_Artificial_Chemist_Quantum_Dot.md`
    - `Notes/05_Earth_and_Environmental_Sciences/Liang_2026_GeoAgentic_RAG.md`
  - changed notes returned:
    - `Notes/04_Materials_Science/Wu_2025_Random_Heteropolymer_Blends.md`
    - `Notes/04_Materials_Science/Epps_2020_Artificial_Chemist_Quantum_Dot.md`
    - `Notes/05_Earth_and_Environmental_Sciences/Liang_2026_GeoAgentic_RAG.md`

## 3. Controller handling rule

Until the controller has:

1. received all three evidence packets, and
2. merged them into a controller-owned evidence pack,

this round should be treated as `frozen and ready to launch`, not `closed`.
