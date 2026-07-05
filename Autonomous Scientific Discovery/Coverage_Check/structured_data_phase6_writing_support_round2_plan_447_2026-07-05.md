# ASD Phase 6 writing support round 2 plan

Date: 2026-07-05
Round label: `Phase6WritingSupportR2Approx`
Execution mode: controller-executed approximate multi-agent round

This round is the next truthful standard Phase 6 `30`-paper round after `Phase6NoteRevisionR25Approx`.

## 1. Why this round exists

After `Phase6QueueRefreshAfterR25`:

- the refreshed `note_revision_queue` no longer contains a truthful fresh `30`-paper packet after freshness override of `R22-R25`
- the refreshed `full_text_followup_queue` no longer contains a truthful fresh `30`-paper packet after freshness override of `R19-R25`
- the refreshed `representative_paper_pool` remains the only truthful `30`-capable Phase 6 pool

Therefore, under the governing plan stack, the next standard `3 x 10 = 30` round switches task family from authoritative maintenance to writing-support validation.

## 2. Why approximate multi-agent mode is used

Real sub-agent tooling is not exposed in the current session's available tool surface, so this round uses the approximate multi-agent fallback.

The controller will still preserve:

- contiguous `A/B/C` slice ownership
- read-only note/PDF readiness checking before review
- a separate controller-owned section-review pass over merged slice output
- Main Controller single-write control over closeout, verification, and git

## 3. Frozen round shape

- standard round shape preserved: `3` role slices x `10` notes / papers each = `30` notes / papers total
- the packet is frozen from the refreshed `representative_paper_pool`
- this is a read-only writing-support validation round; no authoritative writeback is pre-authorized at launch time

## 4. Scope

Frozen 30-paper representative packet in current pool order:

- `ASD-0013`
- `ASD-0018`
- `ASD-0019`
- `ASD-0032`
- `ASD-0048`
- `ASD-0058`
- `ASD-0090`
- `ASD-0687`
- `ASD-0062`
- `ASD-0151`
- `ASD-0010`
- `ASD-0012`
- `ASD-0022`
- `ASD-0036`
- `ASD-0037`
- `ASD-0001`
- `ASD-0009`
- `ASD-0016`
- `ASD-0031`
- `ASD-0046`
- `ASD-0653`
- `ASD-0662`
- `ASD-0691`
- `ASD-0693`
- `ASD-0696`
- `ASD-0014`
- `ASD-0020`
- `ASD-0033`
- `ASD-0051`
- `ASD-0055`

## 5. Round intent

This round does not revisit authoritative classification truth.

The read-only validation stage should check whether each selected representative note is:

- still section-ready under the current authoritative pair
- backed by local note and PDF coverage as expected
- carrying stale `to_read` / source-state drift that should be flagged before direct quotation
- best used as an `anchor`, `exemplar`, or `boundary` support paper in later drafting packets

## 6. Approximate role topology

- `Evidence-Agent-A` owns the first `10` representative rows
- `Evidence-Agent-B` owns the next `10` representative rows
- `Evidence-Agent-C` owns the final `10` representative rows
- the controller performs a separate section-review synthesis pass over merged slice output
- no note writeback or master/progress writeback is authorized in this round

## 7. Frozen slice ownership

### Slice A

- `ASD-0013`
- `ASD-0018`
- `ASD-0019`
- `ASD-0032`
- `ASD-0048`
- `ASD-0058`
- `ASD-0090`
- `ASD-0687`
- `ASD-0062`
- `ASD-0151`

### Slice B

- `ASD-0010`
- `ASD-0012`
- `ASD-0022`
- `ASD-0036`
- `ASD-0037`
- `ASD-0001`
- `ASD-0009`
- `ASD-0016`
- `ASD-0031`
- `ASD-0046`

### Slice C

- `ASD-0653`
- `ASD-0662`
- `ASD-0691`
- `ASD-0693`
- `ASD-0696`
- `ASD-0014`
- `ASD-0020`
- `ASD-0033`
- `ASD-0051`
- `ASD-0055`

## 8. Controller discipline

- all launch-time evidence roles are read-only
- current notes and current pool scores are leads for writing support, not authority to change classification
- merged slice evidence is controller-owned
- closeout must explicitly state that approximate roles were closed and that no real external agent handles were claimed
