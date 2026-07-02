# ASD Phase 6 follow-up round 8 plan

Date: 2026-07-03
Round label: `Phase6FollowupR8`

This round is a fresh bounded evidence round launched after `Phase6FollowupR7` and `Phase6AccessFollowupR1`.

## 1. Scope

Frozen focus set:

- `ASD-0572`
- `ASD-0735`
- `ASD-0727`
- `ASD-0859`
- `ASD-0860`
- `ASD-0861`

These six are frozen from the current `structured_data_phase6_full_text_followup_queue_447_2026-07-02.tsv` as the freshest non-safety high-pressure frontier that has not already been re-evidenced on `2026-07-03`.

## 2. Why this round exists

After `Phase6FollowupR7` and `Phase6AccessFollowupR1`, the highest-score queue rows still contain multiple recently rechecked papers:

- `ASD-0005`
- `ASD-0158`
- `ASD-0097`
- `ASD-0112`
- `ASD-0603`
- `ASD-0569`

The current queue is recency-blind, so a naive score-only selection would incorrectly relaunch same-day work.

This round therefore intentionally skips those same-day-rechecked papers and instead advances a fresh non-safety frontier:

- one multi-module materials/life source-limited case: `ASD-0572`
- one materials SDL case: `ASD-0735`
- one geospatial / Earth-observation reasoning case: `ASD-0727`
- three correlated EO-1 Earth-science application papers: `ASD-0859`, `ASD-0860`, `ASD-0861`

## 3. Round questions

This round tries to answer four concrete questions:

1. Can any of these six move from abstract / metadata / review-packet evidence to stronger first-hand article, HTML, or supplementary evidence?
2. Can any local-PDF or legal full-text status improve without overstating access?
3. Do the currently landed module anchors remain stable under refreshed first-hand evidence?
4. Does any paper become strong enough for note-only refresh or authoritative landing in a later follow-up round?

## 4. Multi-agent topology

This round uses:

- `Evidence-Agent-A`
  - owned papers: `ASD-0572`, `ASD-0735`
- `Evidence-Agent-B`
  - owned papers: `ASD-0727`, `ASD-0859`
- `Evidence-Agent-C`
  - owned papers: `ASD-0860`, `ASD-0861`
- `Classification-Reviewer`
  - read-only adjudication after merged evidence

No writeback agent and no `PDF-Archive-Agent` are launched at packet-freeze time.

## 5. Ownership discipline

This round starts as read-only evidence collection only:

- no sub-agent may edit master, progress, notes, reports, or `Reference_PDF/`
- old notes are leads only, not authority
- writeback is allowed only if the controller freezes a landing subset after evidence review

## 6. Current authoritative starting states

Frozen current states before this round:

- `ASD-0572`
  - `scientific_object_modules=04;06`
  - `primary_module_for_filing=04`
  - `pdf_status=abstract_only_checked`
  - `evidence_status=first_hand_abstract_review_packet`
  - `source_limited=yes`

- `ASD-0735`
  - `scientific_object_modules=04`
  - `primary_module_for_filing=04`
  - `pdf_status=abstract_only_checked`
  - `evidence_status=source_limited_review_packet`
  - `source_limited=yes`

- `ASD-0727`
  - `scientific_object_modules=05`
  - `primary_module_for_filing=05`
  - `pdf_status=source_limited_no_local_pdf`
  - `evidence_status=source_limited_review_packet`
  - `source_limited=yes`

- `ASD-0859`
  - `scientific_object_modules=05`
  - `primary_module_for_filing=05`
  - `pdf_status=source_limited_no_local_pdf`
  - `evidence_status=first_hand_abstract_and_official_pages`
  - `source_limited=yes`

- `ASD-0860`
  - `scientific_object_modules=05`
  - `primary_module_for_filing=05`
  - `pdf_status=source_limited_no_local_pdf`
  - `evidence_status=first_hand_abstract_and_official_pages`
  - `source_limited=yes`

- `ASD-0861`
  - `scientific_object_modules=05`
  - `primary_module_for_filing=05`
  - `pdf_status=source_limited_no_local_pdf`
  - `evidence_status=first_hand_abstract_and_official_pages`
  - `source_limited=yes`

## 7. Expected next step

After the three evidence packets return:

1. merge them into a controller-owned evidence file
2. run one read-only `Classification-Reviewer`
3. choose exactly one of:
   - conservative hold, no writeback
   - note-only refresh for a bounded subset
   - bounded authoritative landing for a subset
