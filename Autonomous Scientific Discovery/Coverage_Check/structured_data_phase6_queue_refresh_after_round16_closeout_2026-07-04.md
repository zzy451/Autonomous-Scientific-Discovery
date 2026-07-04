# ASD Phase 6 queue refresh after R16 closeout

Date: 2026-07-04
Round label: `Phase6QueueRefreshAfterR16`

This refresh step propagates the already-landed `Phase6FollowupR16Approx` result into the reusable Phase 6 queue layer. It does not create new authoritative facts.

## 1. Why this refresh was needed

`Phase6FollowupR16Approx` landed six bounded authoritative deltas:

- `ASD-0587`
- `ASD-0665`
- `ASD-0832`
- `ASD-0838`
- `ASD-0491`
- `ASD-0558`

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

No authoritative files were edited in this refresh step beyond the already-landed R16 changes.

## 3. Verified refresh results

The refreshed queue layer now correctly reflects the post-R16 authoritative state:

- none of `ASD-0587`, `ASD-0665`, `ASD-0832`, `ASD-0838`, `ASD-0491`, or `ASD-0558` remain in the full-text follow-up queue
- none of these six rows remain in the note-revision queue
- the refreshed preparation layer still reflects the stable `447 / 422 / 25 / canonical 01.04 = 9 / drift 0` baseline

Current machine-generated queue counts after refresh:

- note revision queue candidates: `150`
- full-text follow-up queue candidates: `105`
- representative paper pool rows: `54`
- module coverage pool rows: `11`
- boundary case pool rows: `9`

## 4. Controller interpretation

The refreshed queue remains a pressure signal, not launch truth. The next controller packet should still apply freshness override and avoid repeatedly launching already-probed hard no-local-PDF rows.

## 5. Conclusion

`Phase6QueueRefreshAfterR16` closes the queue-layer drift introduced by the six-paper `Phase6FollowupR16Approx` landing and provides the correct post-R16 starting point for the next bounded follow-up round.
