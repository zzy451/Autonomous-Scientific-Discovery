# ASD Phase 6 queue refresh after R18 closeout

Date: 2026-07-05
Round label: `Phase6QueueRefreshAfterR18`

This refresh step propagates the already-landed `Phase6FollowupR18Approx` result into the reusable Phase 6 queue layer. It does not create new authoritative facts.

## 1. Landed deltas

`Phase6FollowupR18Approx` landed six bounded authoritative deltas:

- `ASD-0765`
- `ASD-0772`
- `ASD-0049`
- `ASD-0137`
- `ASD-0141`
- `ASD-0370`

For all six rows:

- `evidence_status: <non-full-text local-PDF state> -> first_hand_full_text`
- `source_limited: yes -> no`

## 2. Controller actions

The controller ran:

1. `python "Autonomous Scientific Discovery/scripts/generate_phase6_preparation_queues.py"`
2. `python "Autonomous Scientific Discovery/scripts/generate_phase6_round1_packets.py"`
3. reviewed the refreshed full-text follow-up and note-revision queues

No authoritative files were edited in this refresh step beyond the already-landed R18 changes.

## 3. Verified refresh results

- none of `ASD-0765`, `ASD-0772`, `ASD-0049`, `ASD-0137`, `ASD-0141`, or `ASD-0370` remain in the full-text follow-up queue
- `ASD-0765`, `ASD-0772`, `ASD-0049`, and `ASD-0370` no longer remain in the note-revision queue
- `ASD-0137` and `ASD-0141` still appear there only because the queue generator keeps multi-module rows under the generic `multi_module_note_wording_check` flag
- the refreshed preparation layer still reflects the stable `447 / 422 / 25 / canonical 01.04 = 9 / drift 0` baseline

## 4. Conclusion

`Phase6QueueRefreshAfterR18` closes the queue-layer drift introduced by the six-paper `Phase6FollowupR18Approx` landing and provides the correct post-R18 starting point for the next bounded follow-up round.
