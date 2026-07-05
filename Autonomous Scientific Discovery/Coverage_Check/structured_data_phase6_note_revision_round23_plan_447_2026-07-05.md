# ASD Phase 6 note revision round 23 plan

Date: 2026-07-05
Round label: `Phase6NoteRevisionR23`
Execution mode: real multi-agent round

This round is the next truthful standard Phase 6 `30`-paper round after `Phase6NoteRevisionR22`.

## 1. Why this round exists

After `Phase6QueueRefreshAfterR22`, the refreshed `note_revision_queue` still contains a deep backlog of stable-authority notes whose wording can be tightened against the current authoritative pair.

Applying freshness override to the exact `Phase6NoteRevisionR22` 30-paper packet still leaves a truthful next `30`-paper note-harmonization packet.

Therefore, under the governing plan stack, the next standard round remains a note-harmonization round rather than switching packet type.

## 2. Frozen round shape

- standard round shape preserved: `3` sub-agents x `10` notes / papers each = `30` notes / papers total
- the packet is frozen from the refreshed note-revision queue after freshness override of the full `R22` 30-paper set
- this round is note-centered; no master / progress writeback is pre-authorized at launch time

## 3. Scope

Frozen 30-paper focus set in current note-revision queue order after `R22` freshness override:

- `ASD-0659`
- `ASD-0673`
- `ASD-0790`
- `ASD-0792`
- `ASD-0650`
- `ASD-0064`
- `ASD-0085`
- `ASD-0097`
- `ASD-0137`
- `ASD-0663`
- `ASD-0669`
- `ASD-0714`
- `ASD-0008`
- `ASD-0024`
- `ASD-0054`
- `ASD-0115`
- `ASD-0118`
- `ASD-0540`
- `ASD-0564`
- `ASD-0510`
- `ASD-0511`
- `ASD-0691`
- `ASD-0693`
- `ASD-0696`
- `ASD-0697`
- `ASD-0703`
- `ASD-0710`
- `ASD-0844`
- `ASD-0845`
- `ASD-0850`

## 4. Round intent

This is a bounded note-harmonization round, not a pre-committed authoritative landing round.

The read-only audit stage should check whether each note:

- still states the current `01-11` / `01.04` classification truth clearly
- still overstates or understates old boundary pressure
- mismatches current `source_limited` / local-PDF / evidence-state wording
- needs only wording cleanup or also reveals a genuine authoritative mismatch

Default expectation:

- many rows should be safe for note-only tightening
- any row that exposes a real authoritative mismatch must be escalated back to controller review before writeback is frozen

## 5. Real multi-agent topology

- `Evidence-Agent-A` owns the first `10` papers
- `Evidence-Agent-B` owns the next `10` papers
- `Evidence-Agent-C` owns the final `10` papers
- a later `Classification-Reviewer` pass should operate on merged audit output only
- `Writeback-Agent-1/2/3` should be launched only after the controller freezes a landed note subset

## 6. Frozen slice ownership

### Slice A

- `ASD-0659`
- `ASD-0673`
- `ASD-0790`
- `ASD-0792`
- `ASD-0650`
- `ASD-0064`
- `ASD-0085`
- `ASD-0097`
- `ASD-0137`
- `ASD-0663`

### Slice B

- `ASD-0669`
- `ASD-0714`
- `ASD-0008`
- `ASD-0024`
- `ASD-0054`
- `ASD-0115`
- `ASD-0118`
- `ASD-0540`
- `ASD-0564`
- `ASD-0510`

### Slice C

- `ASD-0511`
- `ASD-0691`
- `ASD-0693`
- `ASD-0696`
- `ASD-0697`
- `ASD-0703`
- `ASD-0710`
- `ASD-0844`
- `ASD-0845`
- `ASD-0850`

## 7. Controller discipline

- all launch-time sub-agents are read-only
- old notes are leads only, not authority
- merged audit evidence is controller-owned
- no note writeback starts until the controller freezes the note subset that is safe to land this round
- only the controller may edit master / progress / closeout / git
- closeout must explicitly close all launched agent handles
