# ASD Project Layout and Writeback

Use this reference after the evidence decision is ready and before editing project records.

## GitHub Portable Checkout

The repository includes the text files required to classify and write back a paper: the master list, current notes, note templates, taxonomy/policy files, mapping ledgers, and the source/progress owner file. Archived PDFs are distributed through Git LFS; ensure the actual PDF objects have been fetched, rather than only LFS pointers. Retrieve first-hand evidence from official online pages, preprints, supplements, or project sites when an asset is absent.

Without the PDF asset library, do not regenerate asset-aware derived files or run the full pipeline. Make owner-file edits only, validate identifiers and Markdown, then hand off the pending local-asset refresh. With `Reference_PDF/` restored, use the full local archive workflow and run the pipeline.

## Directory Roles

| Location | Role | Editing rule |
|---|---|---|
| `Paper_Lists/agent_master_paper_list.md` | Canonical paper identity, inclusion decision, core classification overlay, legacy fields, and filing module | Main owner for paper and classification facts. |
| `Notes/XX_.../` | One structured note per core paper | Versioned in GitHub. File by `primary_module_for_filing`; this is a convenience, not the authoritative classification. |
| `Reference_PDF/XX_.../` | Archived primary PDFs | Git LFS assets; optional for portable evidence classification but required locally for the full asset-aware pipeline. |
| `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md` | Source/PDF/evidence owner facts | Versioned in GitHub; update only facts actually checked. |
| `Data/classification_code_index.json` | Taxonomy vocabulary, labels, definitions, and boundaries | Update only when the taxonomy vocabulary itself changes. |
| `Data/paper_module_taxonomy_assignments.jsonl` | Per-paper, per-module secondary/tertiary taxonomy mapping | Use for every supported module that has a resolved internal taxonomy position. |
| `Data/discipline_code_assignments.jsonl` | Stable filing/management code ledger | One active filing code at most per paper; not a substitute for multi-module facts. |
| `Data/papers.jsonl`, `Data/papers.sqlite`, registries, manifests, CSVs | Derived data | Regenerate through the pipeline; never patch directly. |

## Core Classification Fields

| Field | Valid intent |
|---|---|
| `scientific_object_modules` | One or more formal `01`-`11` modules supported by object-level evidence. Never include `01.04`. |
| `object_coverage_mode` | `single_module`, `multi_module`, or `general_method_without_concrete_object_experiments`. |
| `general_method_bucket` | `none` or `01.04_general_asd_methods_without_concrete_object_experiments`. |
| `primary_module_for_filing` | Exactly one supported module used for directory/ordering convenience; give an override reason if it falls outside supported modules. |
| `primary_module_confidence` | `high`, `medium`, or `low`. |
| `primary_module_assignment_rule` | `main_scientific_object`, `main_validation_object`, `direct_contribution_target`, `substantive_application_object`, or `manual_override`. |
| `module_assignment_evidence` | First-hand object evidence for every assigned module; do not write a bare code. |
| `multi_module_object_coverage_note` | Explain why each additional module has independent evidence. |
| `tertiary_taxonomy_code` | Deepest active controlled code for that module. Mandatory for every confirmed `06` and `07` assignment; for every module, unresolved tertiary positions must retain a specific evidence or taxonomy-gap reason. Existing trees must be checked in full before declaring a missing category. |

## Writeback Order

1. Confirm deduplication and preserve or allocate the permanent `ASD-xxxx` paper ID.
2. Update `agent_master_paper_list.md` with canonical metadata, status, structured classification fields, source trail, evidence summary, and filing choice.
3. Add or revise `paper_module_taxonomy_assignments.jsonl` for each supported module. Resolve the deepest active controlled code supported by evidence. `06` and `07` always require a tertiary code for confirmed core assignments; do not substitute a bare secondary code for an unresolved tertiary decision. For other modules, leave the tertiary field blank only for a documented taxonomy gap, never because classification work stopped early.
4. Update `discipline_code_assignments.jsonl` only if the single filing position is new or changes. Append new codes; never reorder existing codes. A pure `01.04` record uses `non_discipline_general_method`, not a normal `MM-SS-NNN` code.
5. Write/update the note for a confirmed core record. Add a note-revision queue item if classification changes but the note cannot be safely revised in the same task.
6. Update source/PDF progress facts only when those facts were actually checked or changed.
7. In a full local archive, regenerate derived data and inspect `Data/integrity_check_report.md`. In a GitHub portable checkout, record this as deferred rather than regenerating asset-aware data without PDFs.

## Evidence and Review States

- Prefer full text, official preprint, publisher/DOI page, supplement, official benchmark page, or official project page.
- If source access is insufficient, retain specific evidence, mark the record source-limited, and say what source would resolve the decision.
- Use `needs_review` for a real unresolved boundary or inclusion question; name the competing classes and the missing discriminator.
- Keep `background_only` when a review, roadmap, tool, benchmark, or infrastructure work is useful but does not itself meet the included Agent-system standard.

## Completion Checks

- Each confirmed core paper has a supported module or an explicit `01.04` bucket decision.
- Module codes, coverage mode, general bucket, and filing module are mutually consistent; every confirmed `06` or `07` mapping has a valid tertiary code under its secondary code.
- For other modules, every missing tertiary code is either outside the active controlled tree or has an explicit review/taxonomy-gap rationale.
- Multi-module papers have evidence for each assigned module.
- The note name is English and its folder matches `primary_module_for_filing`.
- The pipeline has no `ERROR` findings caused by the edit.


## 2026-10-29 all-domain ledger update

The module ledger now covers every confirmed paper/module pair across 01–11. It accepts validated tertiary codes in every domain, including chemistry and materials. Read Coverage_Check/tertiary_boundary_protocol_2026-10-29.md for task evidence, benchmark, platform and historical redirect boundaries. A blank legacy field, a missing module-level tertiary, and an administrative general-method bucket are different statistics. Never infer scientific completeness from a populated filing code.
