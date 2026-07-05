# ASD Phase 6 note revision round 24 plan

Date: 2026-07-05
Round label: `Phase6NoteRevisionR24`
Execution mode: real multi-agent round

This round is the next truthful standard Phase 6 `30`-paper round after `Phase6NoteRevisionR23`.

## 1. Why this round exists

After `Phase6QueueRefreshAfterR23`, the refreshed `note_revision_queue` still contains a deep backlog of stable-authority notes whose wording can be tightened against the current authoritative pair.

Applying freshness override to the exact `Phase6NoteRevisionR22` and `Phase6NoteRevisionR23` 30-paper packets still leaves a truthful next `30`-paper note-harmonization packet.

Therefore, under the governing plan stack, the next standard round remains a note-harmonization round rather than switching packet type.

## 2. Frozen round shape

- standard round shape preserved: `3` sub-agents x `10` notes / papers each = `30` notes / papers total
- the packet is frozen from the refreshed note-revision queue after freshness override of the full `R22` and `R23` 30-paper sets
- this round is note-centered; no master / progress writeback is pre-authorized at launch time

## 3. Scope

Frozen 30-paper focus set in current note-revision queue order after `R22` and `R23` freshness override:

- `ASD-0857`
- `ASD-0869`
- `ASD-0870`
- `ASD-0871`
- `ASD-0003`
- `ASD-0112`
- `ASD-0117`
- `ASD-0603`
- `ASD-0740`
- `ASD-0818`
- `ASD-0819`
- `ASD-0821`
- `ASD-0116`
- `ASD-0385`
- `ASD-0466`
- `ASD-0520`
- `ASD-0522`
- `ASD-0539`
- `ASD-0547`
- `ASD-0569`
- `ASD-0739`
- `ASD-0811`
- `ASD-0651`
- `ASD-0722`
- `ASD-0727`
- `ASD-0803`
- `ASD-0859`
- `ASD-0860`
- `ASD-0861`
- `ASD-0141`

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

- `ASD-0857`
- `ASD-0869`
- `ASD-0870`
- `ASD-0871`
- `ASD-0003`
- `ASD-0112`
- `ASD-0117`
- `ASD-0603`
- `ASD-0740`
- `ASD-0818`

### Slice B

- `ASD-0819`
- `ASD-0821`
- `ASD-0116`
- `ASD-0385`
- `ASD-0466`
- `ASD-0520`
- `ASD-0522`
- `ASD-0539`
- `ASD-0547`
- `ASD-0569`

### Slice C

- `ASD-0739`
- `ASD-0811`
- `ASD-0651`
- `ASD-0722`
- `ASD-0727`
- `ASD-0803`
- `ASD-0859`
- `ASD-0860`
- `ASD-0861`
- `ASD-0141`

## 7. Controller discipline

- all launch-time sub-agents are read-only
- old notes are leads only, not authority
- merged audit evidence is controller-owned
- no note writeback starts until the controller freezes the note subset that is safe to land this round
- only the controller may edit master / progress / closeout / git
- closeout must explicitly close all launched agent handles
