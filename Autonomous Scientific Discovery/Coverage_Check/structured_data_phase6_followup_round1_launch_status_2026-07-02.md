# ASD Phase 6 follow-up round 1 launch status

Date: 2026-07-02
Round label: `Phase6FollowupR1`

This file records the actual launch status of the first live follow-up evidence round based on the previously generated packet assets.

## Intended topology

Planned evidence collection topology:

- `Evidence-Agent-A`
- `Evidence-Agent-B`
- `Evidence-Agent-C`

Owned slice files:

- `Coverage_Check/structured_data_phase6_followup_round1_slice_A_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_followup_round1_slice_B_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_followup_round1_slice_C_447_2026-07-02.tsv`

## Actual launch status

### Launched successfully in the first wave

- `Evidence-Agent-A`
  - packet: slice A
  - live status at launch: started

- `Evidence-Agent-B`
  - packet: slice B
  - live status at launch: started

### Delayed at first attempt

- `Evidence-Agent-C`
  - packet: slice C
  - launch result: failed at first attempt because the current agent thread limit was reached

Important at that checkpoint:

- This round has **not** been falsely treated as three-agent live execution.
- `Evidence-Agent-C` remains pending until a concurrency slot is free or the round is explicitly downgraded.

## Main-controller handling rule at the launch checkpoint

Until `Evidence-Agent-C` is either:

1. successfully launched, or
2. explicitly replaced by a documented downgraded execution shape,

the round should be treated as `partially launched`, not `fully launched`.

## Controller actions actually taken after the checkpoint

The controller then did the following:

1. waited for a concurrency slot to free
2. launched `Evidence-Agent-C` with the existing slice C packet
3. recovered the exact completion packet for `Evidence-Agent-A`
4. received completion packets from `Evidence-Agent-B` and `Evidence-Agent-C`
5. merged all three evidence returns into the controller-owned round evidence template

## Final round-launch outcome

The round ultimately completed in the intended three-slice evidence shape:

- `Evidence-Agent-A`: completed and closed
- `Evidence-Agent-B`: completed and closed
- `Evidence-Agent-C`: delayed at first launch attempt, later launched successfully, completed, and closed

No silent downgrade was applied.
