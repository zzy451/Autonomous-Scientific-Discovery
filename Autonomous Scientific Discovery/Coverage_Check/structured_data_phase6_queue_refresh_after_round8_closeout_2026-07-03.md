# ASD Phase 6 queue refresh after R8 closeout

Date: 2026-07-03
Round label: `Phase6QueueRefreshAfterR8`

This refresh round does not create new authoritative facts. It propagates the already-landed `Phase6FollowupR8` result into the reusable Phase 6 queue layer so the next evidence packet does not relaunch stale frontier rows by mistake.

## 1. Why this refresh was needed

`Phase6FollowupR8` landed one bounded authoritative delta:

- `ASD-0735`
  - `pdf_status: abstract_only_checked -> archived_pdf`
  - `pdf_path: <empty> -> Reference_PDF/04_Materials_Science/Epps_2020_Artificial_Chemist_Quantum_Dot.pdf`
  - `evidence_status: source_limited_review_packet -> first_hand_full_text`
  - `source_limited: yes -> no`

Without a queue refresh, the reusable Phase 6 follow-up queue would still incorrectly present `ASD-0735` as a no-local-PDF high-pressure frontier row.

## 2. Controller actions

The controller ran:

1. `python "Autonomous Scientific Discovery/scripts/generate_phase6_preparation_queues.py"`
2. `git status --short`
3. reviewed the refreshed `structured_data_phase6_full_text_followup_queue_447_2026-07-02.tsv`
4. reviewed the refreshed `structured_data_phase6_note_revision_queue_447_2026-07-02.tsv`

No authoritative files were edited in this refresh step.

## 3. Verified refresh results

The refreshed queue layer now correctly reflects the post-R8 authoritative state:

- `ASD-0735` is removed from the no-local-PDF high-pressure frontier
- active local PDF coverage in the refreshed module coverage pool reflects the current `422 / 25` baseline
- the refreshed note queue still keeps `ASD-0572` and `ASD-0727` visible as source-limited note-refresh candidates, which matches the R8 note-only outcome

## 4. Controller interpretation

The refreshed queue is still recency-blind. It continues to rank several papers that were already re-evidenced on `2026-07-03`, including:

- `ASD-0005`
- `ASD-0158`
- `ASD-0097`
- `ASD-0112`
- `ASD-0569`
- `ASD-0572`
- `ASD-0727`
- `ASD-0859`
- `ASD-0860`
- `ASD-0861`

That means the next controller packet must still apply an explicit freshness override rather than naively taking the top six queue rows as launch truth.

## 5. Next fresh non-safety frontier

After excluding:

- same-day re-evidenced rows
- already-landed `ASD-0735`
- explicit safety-skip rows such as `ASD-0547` and `ASD-0544`

the next clean controller-facing candidate focus set is:

- `ASD-0536`
- `ASD-0617`
- `ASD-0631`
- `ASD-0724`
- `ASD-0855`
- `ASD-0858`

Why this set is the current best next packet:

1. all six still have `no local PDF`
2. five of the six still have `source_limited=yes`
3. all six have meaningful access/evidence follow-up value
4. the set opens a fresh cross-module frontier across `07`, `06`, `04`, `11`, and `10`, instead of looping back into same-day chemistry/Earth rows

## 6. Conclusion

`Phase6QueueRefreshAfterR8` closes the queue-layer drift introduced by the bounded `ASD-0735` landing and provides the correct fresh starting point for the next bounded follow-up round.
