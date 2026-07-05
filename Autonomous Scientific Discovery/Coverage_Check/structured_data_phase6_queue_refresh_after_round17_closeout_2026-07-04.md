# ASD Phase 6 queue refresh after R17 closeout

Date: 2026-07-04
Round label: `Phase6QueueRefreshAfterR17`

This refresh step propagates the already-landed `Phase6FollowupR17Approx` result into the reusable Phase 6 queue layer. It does not create new authoritative facts.

## 1. Landed deltas

`Phase6FollowupR17Approx` landed six bounded authoritative deltas:

- `ASD-0568`
- `ASD-0581`
- `ASD-0582`
- `ASD-0591`
- `ASD-0668`
- `ASD-0672`

For all six rows:

- `evidence_status: <non-full-text local-PDF state> -> first_hand_full_text`
- `source_limited: yes -> no`

## 2. Controller actions

The controller ran:

1. `python "Autonomous Scientific Discovery/scripts/generate_phase6_preparation_queues.py"`
2. `python "Autonomous Scientific Discovery/scripts/generate_phase6_round1_packets.py"`
3. reviewed the refreshed full-text follow-up and note-revision queues

No authoritative files were edited in this refresh step beyond the already-landed R17 changes.

## 3. Verified refresh results

- none of `ASD-0568`, `ASD-0581`, `ASD-0582`, `ASD-0591`, `ASD-0668`, or `ASD-0672` remain in the full-text follow-up queue
- none of these six rows remain in the note-revision queue
- the refreshed preparation layer still reflects the stable `447 / 422 / 25 / canonical 01.04 = 9 / drift 0` baseline

Current machine-generated queue counts after refresh:

- note revision queue candidates: `144`
- full-text follow-up queue candidates: `99`
- representative paper pool rows: `54`
- module coverage pool rows: `11`
- boundary case pool rows: `9`

## 4. Conclusion

`Phase6QueueRefreshAfterR17` closes the queue-layer drift introduced by the six-paper `Phase6FollowupR17Approx` landing and provides the correct post-R17 starting point for the next bounded follow-up round.
