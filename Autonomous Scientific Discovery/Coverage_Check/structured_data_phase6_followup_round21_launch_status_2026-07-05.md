# ASD Phase 6 follow-up round 21 launch status

Date: 2026-07-05
Round label: `Phase6FollowupR21`
Execution mode: real multi-agent round

## 1. Frozen scope

This round uses the standard real multi-agent shape:

- `3` evidence agents
- `10` papers per evidence agent
- `30` papers total

Frozen packet artifacts:

- `Coverage_Check/structured_data_phase6_followup_round21_plan_447_2026-07-05.md`
- `Coverage_Check/structured_data_phase6_followup_round21_all30_preview_447_2026-07-05.tsv`
- `Coverage_Check/structured_data_phase6_followup_round21_slice_A_447_2026-07-05.tsv`
- `Coverage_Check/structured_data_phase6_followup_round21_slice_B_447_2026-07-05.tsv`
- `Coverage_Check/structured_data_phase6_followup_round21_slice_C_447_2026-07-05.tsv`
- `Coverage_Check/structured_data_phase6_followup_round21_evidence_merge_template_447_2026-07-05.tsv`

## 2. Agent launches

Launched real evidence agents:

- `Evidence-Agent-A`: `019f30ba-8851-7b52-b4f2-92682d4f3aa3`
- `Evidence-Agent-B`: `019f30ba-fba1-7070-915e-38d96d06b708`
- `Evidence-Agent-C`: `019f30bb-6f09-7382-bb0c-1bffbbdc975d`

Pending launch later in the round:

- `Classification-Reviewer`
- `Writeback-Agent-*` only if the controller freezes a landed subset large enough to justify note writeback

## 3. Launch discipline

- evidence agents are read-only
- old notes and old reports are leads only, not authority
- when a realistically obtainable PDF is unavailable, truthful HTML / abstract / official-page evidence is acceptable
- no authoritative files may be edited by evidence agents

## 4. Next controller step

The controller will merge the returned evidence rows, launch the independent `Classification-Reviewer`, then decide whether this round produces:

- authoritative landing plus note writeback
- evidence-only conservative hold
- or a mixed result
