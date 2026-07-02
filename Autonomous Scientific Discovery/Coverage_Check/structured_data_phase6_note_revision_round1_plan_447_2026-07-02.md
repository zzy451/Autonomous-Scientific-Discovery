# ASD Phase 6 note revision round 1 plan

Date: 2026-07-02
Round label: `Phase6NoteRevisionR1`

This round is a bounded Phase 6 note-wording harmonization round launched from the refreshed note-revision queue after `Phase6QueueRefreshAfterR5`.

## 1. Scope

Approved landing subset:

- `ASD-0541`
- `ASD-0097`
- `ASD-0112`

This round is note-only. No master or progress writeback is planned unless note review exposes an unexpected authoritative mismatch.

## 2. Why this subset

These three papers are all refreshed note-queue records with stable authoritative classification already frozen, but their current note bodies still carry wording pressure from earlier boundary states:

- `ASD-0541`
  - authoritative state is independent `01.04`
  - note still reads too much like a near-`06` object paper in several sections
- `ASD-0097`
  - authoritative state is now `06` only
  - note still foregrounds the old `07` pressure strongly enough to feel half-landed
- `ASD-0112`
  - authoritative state is now `03` only
  - note still over-emphasizes the old `07` biomedical pressure in multiple body sections

## 3. Read-only audit stage

Read-only sub-agents used before writeback:

- `Herschel`
  - audited `ASD-0541` and `ASD-0097`
- `Boole`
  - audited `ASD-0112`

Both agents were instructed to:

- stay read-only
- compare notes against current master/progress anchors
- identify wording that could make old states look currently landed
- recommend whether the note is safe to land this round

Result:

- all three notes are safe to land this round
- this is a wording-harmonization round, not a reclassification round

## 4. Writeback topology

Landed note count is `3`, so this round uses:

- `Writeback-Agent-1`

Owned note files:

- `Notes/06_Life_Sciences/Zhang_2025_PromptBio_Bioinformatics.md`
- `Notes/06_Life_Sciences/Alber_2026_CellVoyager.md`
- `Notes/07_Medical_and_Health_Sciences/Che_2025_CSSTep.md`

No other agent may edit these files in this round.

## 5. Controller rule for this round

The writeback agent may:

- tighten wording
- refresh evidence-log wording
- clarify current authoritative anchor
- reduce stale boundary pressure

The writeback agent may not:

- change modules beyond the adjudicated row
- edit master/progress/report files
- expand or retract classification

## 6. Expected round outcome

After writeback, the notes should read as:

- `ASD-0541`: stable independent `01.04` platform-boundary record with `source_limited=yes`
- `ASD-0097`: stable `06` record with `07` retained only as future source-limited lead
- `ASD-0112`: stable `03` record with `07` retained only as future source-limited lead
