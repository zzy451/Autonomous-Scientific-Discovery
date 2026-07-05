# ASD Phase 6 follow-up round 21 writeback launch packet

Date: 2026-07-05
Round label: `Phase6FollowupR21`

This is a real multi-agent writeback-ownership packet. Writeback agents must edit only their owned note files and must not edit master, progress, report, queue, or git-tracking files.

## Frozen landing subset

Approved landing subset:

- `ASD-0737`
- `ASD-0738`
- `ASD-0549`
- `ASD-0567`
- `ASD-0613`
- `ASD-0748`
- `ASD-0750`
- `ASD-0734`
- `ASD-0535`
- `ASD-0747`
- `ASD-0749`
- `ASD-0753`
- `ASD-0754`
- `ASD-0625`
- `ASD-0626`

## Planned ownership

- `Writeback-Agent-1`: `ASD-0737`, `ASD-0738`, `ASD-0549`, `ASD-0567`, `ASD-0613`
- `Writeback-Agent-2`: `ASD-0748`, `ASD-0750`, `ASD-0734`, `ASD-0535`, `ASD-0747`
- `Writeback-Agent-3`: `ASD-0749`, `ASD-0753`, `ASD-0754`, `ASD-0625`, `ASD-0626`

## Required writeback shape

- add an explicit `Phase6FollowupR21 Frozen Adjudication` section to each owned note
- refresh note-level `PDF path` / first-hand-source wording to the canonical local archived PDF path
- replace stale abstract-only, no-local-PDF, or non-full-text wording with truthful local-PDF-backed first-hand wording
- preserve the final adjudicated modules exactly as frozen in the landing decision
- where applicable, retire stale residual `01.04`-style, abstract-only, or source-depth caveat wording that no longer matches the current evidence state
- preserve note location as filing convenience only; do not treat note directory as classification authority

## Scope reminders

- local archived PDF evidence is already sufficient for this round's landed notes; no further PDF hard-fighting is needed
- do not expand or retract modules beyond the frozen adjudication row
- do not touch any note outside the owned list
- do not edit `agent_master_paper_list.md`, progress trackers, closeout files, queue files, or git state
- return a completion packet listing owned files, changed files, untouched files, and any blockers
