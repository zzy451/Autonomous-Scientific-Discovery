# ASD Phase 6 follow-up round 11 closeout

Date: 2026-07-04
Round label: `Phase6FollowupR11Approx`

This file records the controller closeout for the first post-R10 fresh bounded evidence round.

## 1. Round scope

Frozen focus set:

- `ASD-0005`
- `ASD-0158`
- `ASD-0097`
- `ASD-0112`
- `ASD-0603`
- `ASD-0569`

## 2. Execution mode

Real sub-agent tools were still unavailable.

The controller therefore preserved the standard role split through approximate parallel-tool execution:

- `Evidence-Agent-A` approximate ownership: `ASD-0005`, `ASD-0158`
- `Evidence-Agent-B` approximate ownership: `ASD-0097`, `ASD-0112`
- `Evidence-Agent-C` approximate ownership: `ASD-0603`, `ASD-0569`
- `Classification-Reviewer` approximate pass: controller-owned adjudication from merged evidence only

No writeback ownership and no PDF-archive ownership were launched because the round never froze a landed subset.

## 3. Merged evidence summary

- `ASD-0005`: Crossref still exposes ACS publisher PDF links, but ACS page and PDF access remain challenge-blocked in this environment; stable `03;04`.
- `ASD-0158`: Crossref abstract and Science PDF registration keep the stable `03` anchor, but the Science page and PDF remain blocked here.
- `ASD-0097`: Nature HTML/PDF registration and preprint lineage are clearer than before, but no readable full text or local PDF was actually retrieved; stable `06`.
- `ASD-0112`: Elsevier XML/plain-text endpoints remain visible and the `03` chemistry anchor stays stable, but this round did not retrieve readable full text or a local PDF.
- `ASD-0603`: Crossref abstract and Science PDF registration keep the stable `03` chemistry anchor, but the Science page/PDF remain blocked here.
- `ASD-0569`: Wiley PDF/XML registration and CC-BY license remain unusually strong metadata support, but direct readable Wiley retrieval still failed in this environment; stable `04`.

## 4. Controller decision

This round closes as an evidence-only conservative-hold round.

Final result:

- no authoritative landing
- no note writeback
- no PDF archive write

Per-paper outcome:

- `ASD-0005`: keep conservative hold
- `ASD-0158`: keep conservative hold
- `ASD-0097`: keep conservative hold
- `ASD-0112`: keep conservative hold
- `ASD-0603`: keep conservative hold
- `ASD-0569`: keep conservative hold

## 5. Baseline and verification

Because no authoritative files changed in this round:

- baseline remains `447 / 422 / 25 / canonical 01.04 = 9 / drift 0`
- no `export -> check -> build` rerun was required for the round itself

Controller still verified:

- the evidence merge file exists
- the classification review file exists
- the landing-decision file exists
- the worktree stayed scoped to round11 packet/closeout files only before commit

## 6. Conclusion

`Phase6FollowupR11Approx` advances the next post-R10 frontier without overstating access.

The practical outcome is:

- stronger evidence trails for six still-source-limited rows
- no false claim that registered PDF / XML endpoints equal readable full text
- no forced authoritative change where the environment still stopped short of first-hand retrieval

This round should be read as a valid bounded Phase 6 evidence pass, not as inactivity.
