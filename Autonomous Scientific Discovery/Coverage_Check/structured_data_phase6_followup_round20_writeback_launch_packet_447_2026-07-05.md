# ASD Phase 6 follow-up round 20 writeback launch packet

Date: 2026-07-05
Round label: `Phase6FollowupR20`

This is a real multi-agent writeback-ownership packet. Writeback agents must edit only their owned note files and must not edit master, progress, report, queue, or git-tracking files.

## Frozen landing subset

Approved landing subset:

- `ASD-0743`
- `ASD-0744`
- `ASD-0745`
- `ASD-0770`
- `ASD-0531`
- `ASD-0543`
- `ASD-0545`
- `ASD-0554`
- `ASD-0556`
- `ASD-0052`
- `ASD-0775`
- `ASD-0652`
- `ASD-0655`
- `ASD-0701`
- `ASD-0766`

## Planned ownership

- `Writeback-Agent-1`: `ASD-0743`, `ASD-0744`, `ASD-0745`, `ASD-0770`, `ASD-0531`
- `Writeback-Agent-2`: `ASD-0543`, `ASD-0545`, `ASD-0554`, `ASD-0556`, `ASD-0052`
- `Writeback-Agent-3`: `ASD-0775`, `ASD-0652`, `ASD-0655`, `ASD-0701`, `ASD-0766`

## Required writeback shape

- add an explicit `Phase6FollowupR20` frozen-adjudication section to each owned note
- refresh note-level `PDF path` / first-hand-source wording to the canonical local archived PDF path
- replace stale `source_limited=yes` language with truthful first-hand local-PDF wording
- preserve the final adjudicated modules exactly as frozen in the landing decision
- where applicable, retire stale independent `01.04` or single-module wording that survives only from older note states
- preserve note location as filing convenience only; do not treat note directory as classification authority

## Scope reminders

- local archived PDF evidence is already sufficient for this round's landed notes; no further PDF hard-fighting is needed
- do not expand or retract modules beyond the frozen adjudication row
- do not touch any note outside the owned list
- return a completion packet listing owned files, changed files, untouched files, and any blockers
