# ASD Phase 6 note revision round 25 plan

Date: 2026-07-05
Round label: `Phase6NoteRevisionR25Approx`
Execution mode: controller-executed approximate multi-agent round

This round is the next truthful standard Phase 6 `30`-paper round after `Phase6NoteRevisionR24`.

## 1. Why this round exists

After `Phase6QueueRefreshAfterR24`, the refreshed `note_revision_queue` still contains a deep backlog of stable-authority notes whose wording can be tightened against the current authoritative pair.

Applying freshness override to the exact `Phase6NoteRevisionR22`, `Phase6NoteRevisionR23`, and `Phase6NoteRevisionR24` 30-paper packets still leaves a truthful next `30`-paper note-harmonization packet.

Therefore, under the governing plan stack, the next standard round remains a note-harmonization round rather than switching packet type.

## 2. Why approximate multi-agent mode is used

Real sub-agent tooling is not exposed in the current session's available tool surface, so this round uses the approximate multi-agent fallback allowed by the orchestration skill.

The controller will still preserve:

- `Evidence-Agent-A/B/C` contiguous slice ownership
- read-only evidence gathering before adjudication
- a separate controller-owned classification-review pass over merged evidence
- frozen writeback ownership before any note edits
- Main Controller single-write control over closeout, verification, and git

## 3. Frozen round shape

- standard round shape preserved: `3` role slices x `10` notes / papers each = `30` notes / papers total
- the packet is frozen from the refreshed note-revision queue after freshness override of the full `R22`, `R23`, and `R24` 30-paper sets
- this round is note-centered; no master / progress writeback is pre-authorized at launch time

## 4. Scope

Frozen 30-paper focus set in current note-revision queue order after `R22`, `R23`, and `R24` freshness override:

- `ASD-0152`
- `ASD-0276`
- `ASD-0599`
- `ASD-0617`
- `ASD-0660`
- `ASD-0724`
- `ASD-0731`
- `ASD-0741`
- `ASD-0742`
- `ASD-0743`
- `ASD-0744`
- `ASD-0745`
- `ASD-0770`
- `ASD-0030`
- `ASD-0113`
- `ASD-0254`
- `ASD-0531`
- `ASD-0537`
- `ASD-0543`
- `ASD-0545`
- `ASD-0548`
- `ASD-0554`
- `ASD-0679`
- `ASD-0715`
- `ASD-0817`
- `ASD-0820`
- `ASD-0822`
- `ASD-0826`
- `ASD-0866`
- `ASD-0782`

## 5. Round intent

This is a bounded note-harmonization round, not a pre-committed authoritative landing round.

The read-only audit stage should check whether each note:

- still states the current `01-11` / `01.04` classification truth clearly
- still overstates or understates old boundary pressure
- mismatches current `source_limited` / local-PDF / evidence-state wording
- needs only wording cleanup or also reveals a genuine authoritative mismatch

Default expectation:

- many rows should be safe for note-only tightening
- any row that exposes a real authoritative mismatch must be escalated back to controller review before writeback is frozen

## 6. Approximate role topology

- `Evidence-Agent-A` owns the first `10` papers
- `Evidence-Agent-B` owns the next `10` papers
- `Evidence-Agent-C` owns the final `10` papers
- a later `Classification-Reviewer` pass should operate on merged audit output only
- `Writeback-Agent-1/2/3` should be launched only after the controller freezes a landed note subset

## 7. Frozen slice ownership

### Slice A

- `ASD-0152`
- `ASD-0276`
- `ASD-0599`
- `ASD-0617`
- `ASD-0660`
- `ASD-0724`
- `ASD-0731`
- `ASD-0741`
- `ASD-0742`
- `ASD-0743`

### Slice B

- `ASD-0744`
- `ASD-0745`
- `ASD-0770`
- `ASD-0030`
- `ASD-0113`
- `ASD-0254`
- `ASD-0531`
- `ASD-0537`
- `ASD-0543`
- `ASD-0545`

### Slice C

- `ASD-0548`
- `ASD-0554`
- `ASD-0679`
- `ASD-0715`
- `ASD-0817`
- `ASD-0820`
- `ASD-0822`
- `ASD-0826`
- `ASD-0866`
- `ASD-0782`

## 8. Controller discipline

- all launch-time evidence roles are read-only
- old notes are leads only, not authority
- merged audit evidence is controller-owned
- no note writeback starts until the controller freezes the note subset that is safe to land this round
- only the controller may edit master / progress / closeout / git
- closeout must explicitly state that approximate roles were closed and that no real external agent handles were claimed
