# ASD Phase 6 follow-up round 9 plan

Date: 2026-07-03
Round label: `Phase6FollowupR9`

This round is a fresh bounded evidence round launched after `Phase6FollowupR8` and `Phase6QueueRefreshAfterR8`.

## 1. Scope

Frozen focus set:

- `ASD-0536`
- `ASD-0617`
- `ASD-0631`
- `ASD-0724`
- `ASD-0855`
- `ASD-0858`

## 2. Why this round exists

After `Phase6FollowupR8`, the refreshed full-text follow-up queue correctly drops `ASD-0735` from the high-pressure no-local-PDF frontier.

However, the queue remains recency-blind and still ranks multiple same-day re-evidenced rows near the top, including:

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

This round therefore intentionally skips those same-day-rechecked rows and advances the next fresh non-safety frontier:

- one herbal / network-pharmacology discovery case: `ASD-0536`
- one programmable protein-evolution laboratory case: `ASD-0617`
- one polymer-electrolyte autonomous-discovery case with preprint-PDF lead: `ASD-0631`
- one coral-reef biodiversity hotspot AUV case: `ASD-0724`
- one scientific-peer-review automation case: `ASD-0855`
- one Mars rover mission-operations autonomous-science case: `ASD-0858`

## 3. Round questions

This round tries to answer four concrete questions:

1. Can any of these six move from abstract / metadata / review-packet evidence to stronger first-hand article, HTML, repository, or supplementary evidence?
2. Can any local-PDF or legal full-text status improve without overstating access?
3. Do the currently landed module anchors remain stable under refreshed first-hand evidence?
4. Does any paper become strong enough for note-only refresh, PDF archiving, or a bounded authoritative landing in a later follow-up round?

## 4. Multi-agent topology

This round uses:

- `Evidence-Agent-A`
  - owned papers: `ASD-0536`, `ASD-0617`
- `Evidence-Agent-B`
  - owned papers: `ASD-0631`, `ASD-0724`
- `Evidence-Agent-C`
  - owned papers: `ASD-0855`, `ASD-0858`
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

- `ASD-0536`
  - `scientific_object_modules=07`
  - `primary_module_for_filing=07`
  - `pdf_status=source_limited_no_local_pdf`
  - `evidence_status=first_hand_abstract_review_packet`
  - `source_limited=yes`

- `ASD-0617`
  - `scientific_object_modules=06`
  - `primary_module_for_filing=06`
  - `pdf_status=source_limited_no_local_pdf`
  - `evidence_status=source_limited_review_packet`
  - `source_limited=yes`

- `ASD-0631`
  - `scientific_object_modules=04`
  - `primary_module_for_filing=04`
  - `pdf_status=preprint_pdf_checked_no_local_archive`
  - `evidence_status=first_hand_preprint_pdf_review_packet`
  - `source_limited=no`

- `ASD-0724`
  - `scientific_object_modules=06`
  - `primary_module_for_filing=06`
  - `pdf_status=source_limited_no_local_pdf`
  - `evidence_status=first_hand_abstract_and_doi_metadata`
  - `source_limited=yes`

- `ASD-0855`
  - `scientific_object_modules=11`
  - `primary_module_for_filing=11`
  - `pdf_status=source_limited_no_local_pdf`
  - `evidence_status=first_hand_abstract_and_official_pages`
  - `source_limited=yes`

- `ASD-0858`
  - `scientific_object_modules=10`
  - `primary_module_for_filing=10`
  - `pdf_status=source_limited_no_local_pdf`
  - `evidence_status=official_record_checked_no_download`
  - `source_limited=yes`

## 7. Expected next step

After the three evidence packets return:

1. merge them into a controller-owned evidence file
2. run one read-only `Classification-Reviewer`
3. choose exactly one of:
   - conservative hold, no writeback
   - note-only refresh for a bounded subset
   - bounded authoritative landing for a subset
