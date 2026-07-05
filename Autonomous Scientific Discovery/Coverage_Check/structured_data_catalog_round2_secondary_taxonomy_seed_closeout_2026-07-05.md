# ASD structured data catalog round 2 closeout

Date: 2026-07-05
Scope: secondary taxonomy owner seeding after initial discipline-code preview export

## What landed

This round did not touch the long-term plan file. It advanced the post-preview implementation slice by making the secondary taxonomy vocabulary usable as an owner file instead of leaving every legacy secondary code outside the index.

Implemented changes:

1. `Data/classification_code_index.json`
   - seeded provisional `secondary_code_to_label`
   - seeded provisional `label_to_secondary_code`
   - seeded `secondary_terms` for the currently observed legacy secondary classes in the active confirmed-core preview
   - each secondary term is explicitly marked as:
     - `status=needs_review`
     - `review_status=unreviewed`
     - `source=legacy_secondary_class_seed_2026-07-05`
   - this keeps the file honest as a provisional vocabulary owner rather than pretending the secondary taxonomy is already normalized

2. `scripts/export_structured_data.py`
   - kept reading `classification_code_index.json` as owner input
   - updated preview flagging so rows now surface:
     - missing taxonomy term
     - non-active secondary term status
     - non-reviewed secondary review status
   - result: preview review visibility remains strong even after seeding the owner vocabulary

3. `scripts/check_data_consistency.py`
   - added owner-level consistency validation for `classification_code_index.json`
   - checks now cover:
     - required top-level keys
     - primary-term map consistency
     - secondary-term uniqueness
     - secondary code and parent primary-code consistency
     - inverse-map coverage between term arrays and code-label maps

## Current preview state

`Data/discipline_code_initial_assignment_preview.csv` regenerated successfully.

Current counts:

- `active_code`: 423
- `pending_secondary`: 15
- `non_discipline_general_method`: 9

Current dominant review flags:

- `secondary_term_status_needs_review`: 447
- `secondary_term_review_unreviewed`: 447
- `multi_module`: 104
- `source_limited`: 20
- `secondary_primary_mismatch`: 15

This is the intended intermediate state: the secondary terms are now present in the taxonomy owner, but they are still explicitly review-pending.

## Validation

Executed successfully from repo root:

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

Observed result:

- export passed
- check passed
- build passed
- no owner file was overwritten by daily export beyond derived outputs

## Remaining direct blocker before ledger freeze

The next hard gate is no longer “secondary terms missing from taxonomy owner”.

The remaining direct blocker for `discipline_code_assignments.jsonl` initial freeze is review/adjudication of:

- the 15 `pending_secondary` rows
- the seeded secondary vocabulary terms still marked `needs_review / unreviewed`
- any record whose filing choice or legacy secondary position still requires correction in owner files before ledger creation

## Next recommended slice

Next implementation should stay inside the existing plan and focus on one of:

1. review-oriented tooling / reporting for the 15 `pending_secondary` rows and seeded secondary terms
2. initial ledger creation tooling that consumes reviewed facts but does not bypass the review gate
3. derived discipline registry / SQLite support once the ledger owner exists
