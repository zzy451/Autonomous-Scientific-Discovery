# ASD Structured Data Check Policy

日期：2026-07-05

`check_data_consistency.py` must classify findings by severity. A report that does not distinguish blocking errors from review notes is not sufficient for long-term maintenance.

## 1. Severity Levels

| Severity | Meaning | Build / commit behavior |
|---|---|---|
| `ERROR` | Structural or semantic violation that can corrupt identity, classification, code assignment, or file integrity | Must be fixed before build / commit |
| `WARNING` | Acceptable temporary limitation or low-confidence state that must remain visible | Does not block, but must enter review backlog |
| `INFO` | Descriptive state, useful for reporting but not a problem | Does not block |

## 2. ERROR Examples

- Duplicate or malformed `paper_id`.
- Master and progress cannot be joined for active records.
- Active paper is missing a note path or note file.
- Non-empty `pdf_path` points to a missing file.
- Supplementary PDF is marked as main full text.
- `scientific_object_modules` contains an invalid code or contains `01.04`.
- `primary_module_for_filing` is outside `scientific_object_modules` without an override reason.
- Duplicate active `discipline_local_code`.
- More than one `active_code` assignment for the same `paper_id`.
- `retired_code` is reused as active.
- `redirected_code` lacks a valid `redirected_to_code`.
- `retired_code` has non-null `redirected_to_code`.
- `pending_secondary` has a normal `MM-SS-NNN` code.
- `non_discipline_general_method` has a normal `MM-SS-NNN` code.
- `discipline_code_assignments.jsonl` references an unknown `paper_id`.
- Derived Data outputs cannot be regenerated from owner sources.
- Export overwrites `discipline_code_assignments.jsonl`.

## 3. WARNING Examples

- `secondary_class_confidence=low`.
- `primary_module_confidence=low`.
- `source_limited=yes`.
- Missing PDF but official page or abstract exists.
- `pending_secondary` needs human secondary-class review.
- Pure `01.04` method record needs later special shelving discussion.

## 4. INFO Examples

- `background_only` record.
- `non_discipline_general_method` assignment.
- Supplementary-only source state.
- Derived snapshot generated with `worktree_dirty=true`.

## 5. Report Output

The checker should write:

```text
Data/integrity_check_report.md
```

The report should include:

- summary counts by severity
- failing file / field
- `paper_id` or `assignment_id` when applicable
- machine-readable controlled error code when practical
- recommended owner file to fix
