# ASD Phase 6 access follow-up round 1 closeout

Date: 2026-07-03
Round label: `Phase6AccessFollowupR1`

This file records the controller closeout for the one-paper access/archive follow-up round for `ASD-0569`.

## 1. Round scope

Frozen focus paper:

- `ASD-0569`

## 2. Agent return status

All launched sub-agents returned usable packets.

- `Evidence-Agent-A`
  - role: official-access verifier
  - return quality: usable
  - conclusion: DOI resolution still works, but all checked official Wiley article and PDF endpoints remained blocked by non-safety `403` / Cloudflare challenge in the local environment

- `Evidence-Agent-B`
  - role: archive / license verifier
  - return quality: usable
  - conclusion: Crossref strongly verifies OA / archive metadata, including official Wiley deposited PDF lead, `CC BY 4.0` license metadata for both AM and VOR, and `archive=Portico`; however no locally retrievable PDF was actually obtained

- `Classification-Reviewer`
  - return quality: usable
  - conclusion: stable `04`, keep `source_limited=yes`, and treat the strongest admissible landing as note-only metadata refresh rather than authoritative de-limiting

- `Writeback-Agent-1`
  - owned note: `Notes/04_Materials_Science/Bateni_2022_Autonomous_Nanocrystal_Doping.md`
  - return quality: usable
  - write scope completed: access-metadata refresh only; no classification drift introduced

No sub-agent edited the authoritative pair in this round.

## 3. Merged evidence summary

Controller-owned merged evidence file:

- `Coverage_Check/structured_data_phase6_access_followup_round1_evidence_merge_template_447_2026-07-03.tsv`

High-level merged result for `ASD-0569`:

- stable `scientific_object_modules=04`
- stronger official metadata now confirmed:
  - Crossref official deposited Wiley PDF lead: `https://onlinelibrary.wiley.com/doi/pdf/10.1002/aisy.202200017`
  - Crossref `link.content-type=application/pdf`
  - Crossref `content-version=vor`
  - Crossref `license.URL=http://creativecommons.org/licenses/by/4.0/` for both AM and VOR
  - Crossref license start date `2022-03-13`
  - Crossref `delay-in-days=0`
  - Crossref `archive=Portico`
- actual local first-hand access remained blocked:
  - DOI resolver still redirected to Wiley
  - Wiley article endpoints still returned `403 Forbidden`
  - Wiley PDF endpoints still returned `403 Forbidden`
  - returned pages were Cloudflare challenge HTML rather than readable article/PDF content
- therefore this round strengthened archiveability metadata, but did not resolve local full-text / PDF retrievability
- access blocking remained non-safety and should stay visible as `source_limited=yes`

## 4. Controller decision

Controller-used adjudication files:

- `Coverage_Check/structured_data_phase6_access_followup_round1_classification_review_447_2026-07-03.tsv`
- `Coverage_Check/structured_data_phase6_access_followup_round1_landing_decision_447_2026-07-03.tsv`

Final controller decision:

- no authoritative pair change
- no master update
- no progress update
- no PDF archive write
- one-note writeback landed

Landed note-only refresh:

- `Notes/04_Materials_Science/Bateni_2022_Autonomous_Nanocrystal_Doping.md`

Controller rationale:

1. `ASD-0569` remains a stable materials-science record with `supported_modules=04`.
2. Stronger Crossref / Wiley OA metadata is real and useful, so the note should no longer describe the paper as only a generic publisher-abstract lead.
3. However, actual Wiley article and PDF retrieval still failed in the local environment on `2026-07-03`.
4. Under the project rule, non-safety access blocking must remain visible rather than being silently collapsed into `source_limited=no`.
5. Therefore the correct landing is a note-only metadata refresh while keeping the authoritative pair unchanged and conservative.

## 5. Baseline and git verification

Because the authoritative pair did not change in this round:

- baseline remains `447 / 421 / 26 / canonical 01.04 = 9 / drift 0`
- no `export -> check -> build` rerun was required for authoritative recount

This round still requires:

- git commit after closeout
- clean worktree after commit
- all round agents closed
