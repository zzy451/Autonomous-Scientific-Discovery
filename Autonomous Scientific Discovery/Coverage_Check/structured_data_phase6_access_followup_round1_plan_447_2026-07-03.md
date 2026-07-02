# ASD Phase 6 access follow-up round 1 plan

Date: 2026-07-03
Round label: `Phase6AccessFollowupR1`

This round is a one-paper access/archive follow-up round launched directly from the controller override recorded in `Phase6FollowupR7`.

## 1. Scope

Frozen focus paper:

- `ASD-0569`

Current authoritative state before this round:

- `scientific_object_modules=04`
- `primary_module_for_filing=04`
- `pdf_status=source_limited_no_local_pdf`
- `evidence_status=source_limited_review_packet`
- `source_limited=yes`

## 2. Why this round exists

`Phase6FollowupR7` established a tension that is worth isolating into its own bounded round:

1. Crossref now exposes:
   - `license_URL = http://creativecommons.org/licenses/by/4.0/`
   - `link_URL = https://onlinelibrary.wiley.com/doi/pdf/10.1002/aisy.202200017`
   - `link_content_type = application/pdf`
2. But both shell and browser-style fetches in the current environment still hit Wiley / Cloudflare `403` behavior.

That means this paper has moved beyond a generic abstract-only frontier, but the controller still needs a cleaner answer to:

- does the current project rule permit dropping `source_limited=yes`?
- is there a legal archiveable PDF that is actually retrievable in this environment?
- if not, should the note still be refreshed to reflect the stronger OA metadata and official PDF lead?

## 3. Round questions

This round tries to answer three concrete questions:

1. Official access question:
   - Is the Wiley article or PDF actually reachable in the current environment?
2. Archive-readiness question:
   - Even if the file is not currently reachable, is the legal archive path now strong enough to record in note wording?
3. Landing-readiness question:
   - Does the stronger access metadata justify authoritative `source_limited=no`, or only a note-only refresh?

## 4. Multi-agent topology

This round uses:

- `Evidence-Agent-A`
  - official-access verifier
- `Evidence-Agent-B`
  - archive / license verifier
- `Classification-Reviewer`
  - landing-readiness reviewer after merged evidence

No note writeback or authoritative landing is launched at packet-freeze time.

## 5. Ownership discipline

This round starts as read-only only:

- no sub-agent may edit master, progress, notes, reports, or `Reference_PDF/`
- writeback is allowed only if the controller freezes a note-only or authoritative landing subset after review

## 6. Expected next step

After the two evidence packets return:

1. merge them into a controller-owned evidence file
2. run one read-only `Classification-Reviewer`
3. choose exactly one of:
   - conservative hold, no writeback
   - note-only refresh for `ASD-0569`
   - 1-paper authoritative landing
