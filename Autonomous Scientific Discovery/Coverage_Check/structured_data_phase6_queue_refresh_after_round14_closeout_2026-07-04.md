# ASD Phase 6 queue refresh after R14 closeout

Date: 2026-07-04
Round label: `Phase6QueueRefreshAfterR14`

This refresh step does not create new authoritative facts. It propagates the already-landed `Phase6FollowupR14Approx` result into the reusable Phase 6 queue layer so the next evidence packet does not relaunch stale local-PDF source-limited rows by mistake.

## 1. Why this refresh was needed

`Phase6FollowupR14Approx` landed six bounded authoritative deltas:

- `ASD-0014`
- `ASD-0055`
- `ASD-0085`
- `ASD-0357`
- `ASD-0564`
- `ASD-0670`

For all six rows:

- `evidence_status: <non-full-text local-PDF state> -> first_hand_full_text`
- `source_limited: yes -> no`

Without a queue refresh, the reusable Phase 6 follow-up queue would still incorrectly present these six rows as active local-PDF source-limited pressure.

## 2. Controller actions

The controller ran:

1. `python "Autonomous Scientific Discovery/scripts/generate_phase6_preparation_queues.py"`
2. `python "Autonomous Scientific Discovery/scripts/generate_phase6_round1_packets.py"`
3. reviewed the refreshed `structured_data_phase6_full_text_followup_queue_447_2026-07-02.tsv`
4. reviewed the refreshed `structured_data_phase6_note_revision_queue_447_2026-07-02.tsv`
5. reviewed the refreshed `structured_data_phase6_followup_round1_plan_447_2026-07-02.md`

No authoritative files were edited in this refresh step beyond the already-landed R14 changes.

## 3. Verified refresh results

The refreshed queue layer now correctly reflects the post-R14 authoritative state:

- none of `ASD-0014`, `ASD-0055`, `ASD-0085`, `ASD-0357`, `ASD-0564`, or `ASD-0670` remain in the full-text follow-up queue
- the note-revision queue still surfaces `ASD-0085` and `ASD-0564` because they remain multi-module note-wording cases; this matches queue semantics and does not signal authoritative drift
- the refreshed preparation layer still reflects the stable `447 / 422 / 25 / canonical 01.04 = 9 / drift 0` baseline

Current machine-generated queue counts after refresh:

- note revision queue candidates: `161`
- full-text follow-up queue candidates: `117`
- representative paper pool rows: `54`
- module coverage pool rows: `11`
- boundary case pool rows: `9`

## 4. Controller interpretation

The refreshed queue is still recency-blind. It continues to rank several rows that were already re-evidenced in `R11Approx`, `R13Approx`, or newly cleared in `R14Approx`, so the next controller packet must still apply an explicit freshness override rather than naively taking the top rows as launch truth.

## 5. Next fresh frontier under the current user rule

The current user rule for this phase is:

- if a row is still hard-blocked for PDF retrieval, do not waste repeated rounds on the same blocked route
- HTML / abstract / official-page evidence is enough to keep a true paper indexed and conservatively classified

Under that rule, the next controller packet should prefer:

- fresh no-local-PDF rows that still have realistic HTML / publisher / repository improvement potential
- or the next not-yet-reread local-PDF source-limited pocket

rather than repeatedly refighting the already-probed hard-blocked routes from `R13Approx`.

## 6. Conclusion

`Phase6QueueRefreshAfterR14` closes the queue-layer drift introduced by the six-paper `Phase6FollowupR14Approx` landing and provides the correct post-R14 starting point for the next bounded follow-up round.
