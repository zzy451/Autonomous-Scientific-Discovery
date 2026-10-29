---
name: asd-single-paper-classification-workflow
description: Classify one paper for the Autonomous Scientific Discovery / Agent for Science review, including evidence-based inclusion, fine-grained scientific-object classification, note filing, and owner-data writeback. Use when adding or reclassifying an individual paper; not for broad searches or full-library audits.
metadata:
  short-description: Classify one ASD paper end to end
---

# ASD Single-Paper Classification Workflow

Use this skill when a person needs to add, review, or correct a single paper in the `Autonomous Scientific Discovery` project. The desired result is a traceable inclusion decision and scientific-object classification, not merely a plausible label.

## Project Discovery

Locate the project root named `Autonomous Scientific Discovery`. Do not assume the current working directory is the project root. Before changing a paper record, read:

- `review_scope_and_classification_policy.md`
- `domain_classification_rules.md`
- `science_domain_taxonomy.md`
- `Data/classification_code_index.json`
- `Data/field_ownership_matrix.md`
- `Paper_Lists/agent_master_paper_list.md`
- `paper_note_templates_and_prompts/ASD_annotation_schema.md`
- `paper_note_templates_and_prompts/ASD_single_paper_note_template.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`

For a paper that will enter or change the core library, also read the per-module mapping ledger and the discipline-code policy listed in [project-layout-and-writeback.md](references/project-layout-and-writeback.md).

## Operating Modes

### GitHub portable mode

A standard clone contains all text-based classification owners, the master list, current notes, note templates, taxonomy mappings, and source/progress facts. Use online first-hand sources when a local PDF is unavailable. Complete the classification decision, update the owner files, and commit the changed text records.

Archived PDFs are distributed through Git LFS. Check that actual PDF objects have been fetched rather than only pointer files. Do not run the full local-asset pipeline in a clone without the asset library because it asserts PDF and note-asset availability. Instead, validate changed owner records, preserve unverified PDF fields, and report the pending asset-aware refresh.

### Full local archive mode

When `Reference_PDF/` is available, use the same owner files and then run the canonical pipeline. This is the only mode in which `Data/papers.jsonl`, `Data/papers.sqlite`, manifests, and other asset-aware derived outputs should be refreshed.

## Non-Negotiable Rules

1. Include only Agent-for-Science papers. A core paper must have all of: a clear scientific goal, multi-step action, at least one Agent capability, and an explicit research-workflow role.
2. Closed-loop or full autonomous discovery is not a core inclusion requirement. Record it as evidence of autonomy rather than using it as an inclusion gate.
3. Classify by the concrete scientific object and evidence, never by venue, author affiliation, model type, or Agent architecture.
4. Use first-hand sources for a classification decision: full text/PDF first, then official preprint or publisher page, followed by official project, benchmark, or supplement. Existing notes and legacy classes are leads only.
5. Record every supported `01`-`11` module when the paper reports object-specific experiments, validations, benchmark tasks, case studies, or results. A module need not be the paper's main contribution.
6. Use the independent `01.04` bucket only when no concrete scientific-object evidence supports any `01`-`11` module. `01.04` never appears inside `scientific_object_modules`.
7. When evidence is weak, inaccessible, or conflicts materially, preserve the uncertainty as `needs_review` or `source_limited`; do not force a definitive classification.
8. Classify every supported module to the deepest active taxonomy level supported by first-hand object evidence. `06` and `07` have complete fixed tertiary trees and therefore require a tertiary code for every confirmed core assignment. A `06` or `07` record may not stop at its secondary class: unresolved evidence must remain `needs_review` or `source_limited` with the competing tertiary codes and missing discriminator stated.
9. The project target is three-level classification for every module. As of 2026-10-29, all eleven formal modules have existing tertiary definitions synchronized to the controlled index and are supported in the module ledger. Inspect the full tree before claiming a taxonomy gap. If evidence cannot resolve a position, preserve a specific pending reason and competing codes; never invent a code from a title or keyword. Distinguish primary filing completion from every additional module's internal classification.

## Classification Procedure

### 1. Establish identity and evidence

- Search the master list and `Data/papers.jsonl` by title, DOI, arXiv identifier, and normalized author/year before creating a record. Merge a version into the existing `ASD-xxxx` record instead of creating a duplicate.
- Gather canonical title, authors, year, venue, DOI/URL, and the best available first-hand sources.
- Extract short, attributable evidence for four Agent gates, the research object(s), the workflow, and the validation/result(s). Keep locations such as page, section, figure, table, official abstract, or URL.

### 2. Decide the record status

Apply the four Agent gates together:

| Decision | Use when |
|---|---|
| `to_read` / `included` | All four gates are supported and classification evidence is sufficient for a core record. |
| `candidate` | A likely in-scope paper needs evidence before inclusion. |
| `needs_review` | Evidence, boundary, identity, or source access is genuinely unresolved. State what would resolve it. |
| `background_only` | Useful review, roadmap, benchmark, infrastructure, or context paper that does not function as an included Agent-system study. |
| `excluded` | Clearly fails one or more Agent gates, is out of scope, or is a duplicate. Preserve the reason. |

Do not exclude a paper merely because it is a benchmark, a simulation study, or lacks a robot/wet-lab loop. Do exclude an ordinary prediction model, one-shot assistant, or automation system that lacks Agent behavior and a research-workflow role.

### 3. Assign scientific-object modules

For each candidate module, write an evidence row before assigning it:

| Module | Concrete object | Experiment, validation, task, case, or result | Source location | Confidence |
|---|---|---|---|---|

Apply these rules in order:

1. If one or more rows support concrete objects, assign all corresponding `01`-`11` modules and set `single_module` or `multi_module`.
2. If no row supports a concrete object but the work is an in-scope general research Agent, use `general_method_without_concrete_object_experiments` and `01.04_general_asd_methods_without_concrete_object_experiments`.
3. Select `primary_module_for_filing` only to decide the note/PDF directory. It does not erase other supported modules.
4. Resolve a secondary code for every supported module, then resolve the deepest active code. `06` and `07` must receive one of the controlled tertiary codes in `science_domain_taxonomy.md` and `Data/classification_code_index.json`; evidence that cannot distinguish adjacent tertiary codes is a review state, not permission to leave the tertiary field blank. For other modules, use an active tertiary code only when its formal tree and object evidence support it, and otherwise explicitly record the taxonomy gap. Do not invent a finer code from the title alone.
5. Resolve adjacent boundaries from `domain_classification_rules.md`, especially `03/04`, `05/10`, `06/07`, `01.04/concrete modules`, and `01.04/11.07`.

### 4. Produce the classification record

Before any writeback, provide a concise decision record with:

- canonical identity and source trail
- status and four Agent-gate evidence
- supported module(s), coverage mode, and `01.04` decision
- per-module object-evidence rows
- primary filing module, secondary code, and tertiary code or explicit taxonomy-gap/review state for every supported module
- boundary reasoning, confidence, source limitations, and next action

If the decision is a core record, draft or update the structured note using the project template. A complete note contains an Evidence Log and explicitly explains inclusion, scientific-object modules, workflow role, methods, validation, limitations, and review value.

## Writeback and File Management

Follow the ownership and ordering rules in [project-layout-and-writeback.md](references/project-layout-and-writeback.md). In particular:

- Edit owner facts before generated data.
- Update the master record and module-specific taxonomy mappings for a confirmed classification. For `06` and `07`, each supported-module mapping must contain a controlled tertiary code; do not write a blank tertiary field as a final classification.
- Add or update a stable discipline-local code only when the filing position is clear; never re-rank or reuse existing codes.
- Put a core note under the directory for `primary_module_for_filing`, using `FirstAuthor_Year_ShortTitle.md`. Note location is not classification evidence.
- In GitHub portable mode, use official online sources and preserve existing PDF fields unless a source/PDF fact was actually verified. Do not infer PDF status from a blank or nonblank path.
- Do not hand-edit derived exports such as `Data/papers.jsonl`, `Data/papers.sqlite`, manifests, registries, or CSV snapshots.

In full local archive mode, run the canonical project pipeline after owner edits:

```powershell
python 'Autonomous Scientific Discovery/scripts/run_structured_data_pipeline.py'
```

Resolve `ERROR` findings before considering the paper classification complete. In GitHub portable mode, run `git diff --check`, verify the master/progress/module-mapping identifiers manually, and preserve the asset-aware pipeline check as a handoff item. Preserve `WARNING` findings in the record or review queue.

## Handoff Standard

Report the changed paper ID, status, modules/bucket, filing module, secondary/tertiary classification for every module, evidence sources checked, files changed, operating mode, pipeline result or deferred asset check, and any unresolved question. For classification-sensitive changes, state why nearby classes were not selected.

Use the project's controlled English status values and codes, while writing explanatory prose in Chinese unless the task requires otherwise.
