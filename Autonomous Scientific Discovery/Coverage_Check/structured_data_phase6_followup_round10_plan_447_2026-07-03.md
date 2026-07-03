# ASD Phase 6 follow-up round 10 plan

Date: 2026-07-03
Round label: `Phase6FollowupR10Approx`

This round is the first post-R9 bounded follow-up packet executed with an approximate multi-agent flow. Real sub-agent tools were not available in this environment, so the controller kept the standard role split but simulated the role-isolated passes with parallel tool execution and frozen ownership.

## 1. Scope

Frozen focus set:

- `ASD-0508`
- `ASD-0565`
- `ASD-0006`
- `ASD-0090`
- `ASD-0687`
- `ASD-0506`

## 2. Why this round exists

After `Phase6FollowupR9` and the downstream note-only harmonization round 3:

- the next fresh non-safety rows in the follow-up queue were no longer the R6-R9 same-day rechecked records
- four rows in the next frontier already had local archived PDFs but still carried stale source-limited or abstract-led evidence labels
- two rows remained no-local-PDF follow-up candidates and were still worth a fresh evidence check

This round therefore mixes:

- two no-local-PDF chemistry/materials follow-up rows
- four local-archived-PDF rows whose current authoritative evidence labels looked plausibly stale

## 3. Round questions

This round answers five concrete questions:

1. Which of these six rows still have real follow-up pressure after excluding all R6-R9 handled rows?
2. For the four local-archived-PDF rows, does direct local full-text reread justify clearing old `source_limited=yes` ceilings?
3. Do the current module anchors remain stable under direct full-text reread?
4. Does any no-local-PDF row merit a bounded authoritative delta in this round?
5. If landings occur, what disjoint note ownership should be frozen for writeback?

## 4. Role topology

Approximate role split used in this round:

- `Evidence-Agent-A` ownership: `ASD-0508`, `ASD-0565`
- `Evidence-Agent-B` ownership: `ASD-0006`, `ASD-0090`
- `Evidence-Agent-C` ownership: `ASD-0687`, `ASD-0506`
- `Classification-Reviewer`: merged-evidence adjudication only
- `Writeback-Agent-1` ownership candidate: `ASD-0006`, `ASD-0090`
- `Writeback-Agent-2` ownership candidate: `ASD-0687`, `ASD-0506`

No `Writeback-Agent-3` and no `PDF-Archive-Agent` were needed at packet-freeze time.

## 5. Controller discipline

- all evidence passes were read-only
- the merged evidence file was controller-owned
- the adjudication file was controller-owned
- write ownership was frozen by note file before any patching
- only the controller would touch `agent_master_paper_list.md`, progress, closeout, and git

## 6. Starting authoritative states

- `ASD-0508`: `03`; `pdf_status=publisher_full_text_checked`; `evidence_status=first_hand_full_text`; `source_limited=no`
- `ASD-0565`: `04`; `pdf_status=abstract_only_checked`; `evidence_status=first_hand_abstract_review_packet`; `source_limited=no`
- `ASD-0006`: independent `01.04`; `pdf_status=archived_pdf`; `evidence_status=first_hand_abstract_and_official_pages`; `source_limited=yes`
- `ASD-0090`: `02`; `pdf_status=archived_pdf`; `evidence_status=first_hand_pdf_checked_source_limited`; `source_limited=yes`
- `ASD-0687`: `02`; `pdf_status=archived_pdf`; `evidence_status=first_hand_abstract_review_packet`; `source_limited=yes`
- `ASD-0506`: `03`; `pdf_status=archived_pdf`; `evidence_status=first_hand_preview_only`; `source_limited=yes`

## 7. Intended outcomes

Possible controller outcomes were frozen as:

- conservative hold for rows with no new landing-strength delta
- authoritative landing plus note refresh for rows where local archived full text directly clears stale access ceilings
- no PDF archive write in this round unless a new legal archive artifact was actually created
