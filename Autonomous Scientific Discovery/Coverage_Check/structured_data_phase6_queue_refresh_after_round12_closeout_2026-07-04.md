# ASD Phase 6 queue refresh after R12 closeout

Date: 2026-07-04
Round label: `Phase6QueueRefreshAfterR12`

This refresh step does not create new authoritative facts. It propagates the already-landed `Phase6FollowupR12Approx` result into the reusable Phase 6 queue layer so the next evidence packet does not relaunch stale local-PDF source-limited rows by mistake.

## 1. Why this refresh was needed

`Phase6FollowupR12Approx` landed six bounded authoritative deltas:

- `ASD-0507`
- `ASD-0684`
- `ASD-0084`
- `ASD-0666`
- `ASD-0667`
- `ASD-0653`

For all six rows:

- `evidence_status: <non-full-text local-PDF state> -> first_hand_full_text`
- `source_limited: yes -> no`

Without a queue refresh, the reusable Phase 6 follow-up queue would still incorrectly present these six rows as active local-PDF follow-up pressure.

## 2. Controller actions

The controller ran:

1. `python "Autonomous Scientific Discovery/scripts/generate_phase6_preparation_queues.py"`
2. `python "Autonomous Scientific Discovery/scripts/generate_phase6_round1_packets.py"`
3. reviewed the refreshed `structured_data_phase6_full_text_followup_queue_447_2026-07-02.tsv`
4. reviewed the refreshed `structured_data_phase6_note_revision_queue_447_2026-07-02.tsv`
5. reviewed the refreshed `structured_data_phase6_followup_round1_plan_447_2026-07-02.md`

No authoritative files were edited in this refresh step beyond the already-landed R12 changes.

## 3. Verified refresh results

The refreshed queue layer now correctly reflects the post-R12 authoritative state:

- none of `ASD-0507`, `ASD-0684`, `ASD-0084`, `ASD-0666`, `ASD-0667`, or `ASD-0653` remain in the full-text follow-up queue
- those same six rows are also absent from the note-revision queue
- the refreshed module-coverage / preparation layer still reflects the stable `447 / 422 / 25 / canonical 01.04 = 9 / drift 0` baseline

Current machine-generated queue counts after refresh:

- note revision queue candidates: `165`
- full-text follow-up queue candidates: `123`
- representative paper pool rows: `54`
- module coverage pool rows: `11`
- boundary case pool rows: `9`

The regenerated round1 packet summary now reports:

- top-30 queue contains `21` rows with `no_local_pdf` pressure
- top-30 queue contains `27` rows with `source_limited=yes`
- top-30 queue contains `29` rows with non-full-text evidence pressure

## 4. Controller interpretation

The refreshed queue is still recency-blind. It continues to rank several rows that were already re-evidenced in `R11Approx`, including:

- `ASD-0005`
- `ASD-0158`
- `ASD-0097`
- `ASD-0112`
- `ASD-0603`
- `ASD-0569`

That means the next controller packet must still apply an explicit freshness override rather than naively taking the top six queue rows as launch truth.

## 5. Next fresh non-safety frontier

After excluding:

- the already re-evidenced `R11Approx` six-paper set
- the already landed `R12Approx` six-paper set
- explicit safety-skip rows such as `ASD-0547`

the next clean controller-facing candidate focus set exposed by the refreshed queue is:

- `ASD-0572`
- `ASD-0727`
- `ASD-0859`
- `ASD-0860`
- `ASD-0861`
- `ASD-0617`

This is a queue-derived candidate set, not a frozen launch packet.

## 6. Conclusion

`Phase6QueueRefreshAfterR12` closes the queue-layer drift introduced by the six-paper `Phase6FollowupR12Approx` landing and provides the correct post-R12 starting point for the next bounded follow-up round.
