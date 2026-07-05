# ASD Phase 6 note revision round 22 plan

Date: 2026-07-05
Round label: `Phase6NoteRevisionR22`
Execution mode: real multi-agent round

This round is the next truthful standard Phase 6 `30`-paper round after `Phase6FollowupR21`.

## 1. Why this round exists

After `Phase6QueueRefreshAfterR21`, the current `full_text_followup_queue` no longer contains a truthful fresh `30`-paper packet once all `R19-R21` rows are freshness-overridden.

The refreshed `note_revision_queue` still contains a deep backlog of stable-authority notes whose current wording can be tightened against the current authoritative pair.

Therefore, under the governing plan stack, the next standard round switches to note-harmonization rather than forcing a thin or padded follow-up round.

## 2. Frozen round shape

- standard round shape preserved: `3` sub-agents x `10` notes / papers each = `30` notes / papers total
- the packet is frozen from the refreshed note-revision queue after skipping already landed note-only rounds and already landed `R20-R21` writeback notes
- this round is note-centered; no master / progress writeback is pre-authorized at launch time

## 3. Scope

Frozen 30-paper focus set in current note-revision queue order:

- `ASD-0541`
- `ASD-0572`
- `ASD-0553`
- `ASD-0005`
- `ASD-0006`
- `ASD-0040`
- `ASD-0004`
- `ASD-0053`
- `ASD-0059`
- `ASD-0062`
- `ASD-0069`
- `ASD-0111`
- `ASD-0145`
- `ASD-0523`
- `ASD-0530`
- `ASD-0662`
- `ASD-0671`
- `ASD-0676`
- `ASD-0056`
- `ASD-0091`
- `ASD-0093`
- `ASD-0158`
- `ASD-0519`
- `ASD-0664`
- `ASD-0787`
- `ASD-0060`
- `ASD-0096`
- `ASD-0151`
- `ASD-0516`
- `ASD-0525`

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

- `ASD-0541`
- `ASD-0572`
- `ASD-0553`
- `ASD-0005`
- `ASD-0006`
- `ASD-0040`
- `ASD-0004`
- `ASD-0053`
- `ASD-0059`
- `ASD-0062`

### Slice B

- `ASD-0069`
- `ASD-0111`
- `ASD-0145`
- `ASD-0523`
- `ASD-0530`
- `ASD-0662`
- `ASD-0671`
- `ASD-0676`
- `ASD-0056`
- `ASD-0091`

### Slice C

- `ASD-0093`
- `ASD-0158`
- `ASD-0519`
- `ASD-0664`
- `ASD-0787`
- `ASD-0060`
- `ASD-0096`
- `ASD-0151`
- `ASD-0516`
- `ASD-0525`

## 7. Controller discipline

- all launch-time sub-agents are read-only
- old notes are leads only, not authority
- merged audit evidence is controller-owned
- no note writeback starts until the controller freezes the note subset that is safe to land this round
- only the controller may edit master / progress / closeout / git
- closeout must explicitly close all launched agent handles
