# ASD Phase 6 follow-up round 13 closeout

Date: 2026-07-04
Round label: `Phase6FollowupR13Approx`

This file records the controller closeout for the first post-R12 fresh bounded evidence round.

## 1. Round scope

Frozen focus set:

- `ASD-0572`
- `ASD-0617`
- `ASD-0727`
- `ASD-0859`
- `ASD-0860`
- `ASD-0861`

## 2. Execution mode

Real sub-agent tools were still unavailable.

The controller therefore preserved the standard role split through approximate parallel-tool execution:

- `Evidence-Agent-A` approximate ownership: `ASD-0572`, `ASD-0617`
- `Evidence-Agent-B` approximate ownership: `ASD-0727`, `ASD-0859`
- `Evidence-Agent-C` approximate ownership: `ASD-0860`, `ASD-0861`
- `Classification-Reviewer` approximate pass: controller-owned adjudication from merged evidence only

No writeback ownership and no PDF-archive ownership were launched because the round never froze a landed subset.

## 3. Merged evidence summary

- `ASD-0572`: DOI routing still resolves into Elsevier, but ScienceDirect, cell.com PDF, and ChemRxiv routes all remained challenge-blocked in this environment; stable `04;06`.
- `ASD-0617`: Nature DOI and article-preview HTML are readable, and the page visibly exposes PDF / supplementary / source-data markers, but the page remains preview-only rather than a clearly retrievable full-text or local-PDF landing; stable `06`.
- `ASD-0727`: Elsevier DOI and previous abstract trail remain intact, but direct ScienceDirect and HKU repository routes were challenge-blocked in this environment; stable `05`.
- `ASD-0859`: the prior official article-page packet remains the best first-hand source; this rerun added no readable full text and the current ScienceDirect route is still blocked here; stable `05`.
- `ASD-0860`: DOI routing remains visible but ScienceDirect full article access is still blocked here; stable `05`.
- `ASD-0861`: DOI routing remains visible but ScienceDirect full article access is still blocked here; stable `05`.

## 4. Controller decision

This round closes as an evidence-only conservative-hold round.

Final result:

- no authoritative landing
- no note writeback
- no PDF archive write

Per-paper outcome:

- `ASD-0572`: keep conservative hold
- `ASD-0617`: keep conservative hold
- `ASD-0727`: keep conservative hold
- `ASD-0859`: keep conservative hold
- `ASD-0860`: keep conservative hold
- `ASD-0861`: keep conservative hold

## 5. Baseline and verification

Because no authoritative files changed in this round:

- baseline remains `447 / 422 / 25 / canonical 01.04 = 9 / drift 0`
- no `export -> check -> build` rerun was required for the round itself

Controller still verified:

- the evidence merge file exists
- the classification review file exists
- the landing-decision file exists
- the worktree stayed scoped to round13 packet/closeout/statused-plan files only before commit

## 6. Closing discipline

Approximate round closure for `Phase6FollowupR13Approx`:

- `Evidence-Agent-A` closed
- `Evidence-Agent-B` closed
- `Evidence-Agent-C` closed
- `Classification-Reviewer` closed
- approximate multi-agent round closed

## 7. Conclusion

`Phase6FollowupR13Approx` advances the next post-R12 frontier without overstating access.

The practical outcome is:

- stronger first-hand access diagnostics for six still-source-limited rows
- one materially stronger Nature preview / supplementary-cue record for `ASD-0617`, but still not enough to claim first-hand full text
- no false claim that visible PDF buttons, DOI redirects, repository leads, or publisher routing equal readable full text

This round should be read as a valid bounded Phase 6 evidence pass, not as inactivity.
