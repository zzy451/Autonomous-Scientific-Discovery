# Reference_PDF

## What This Directory Is For

`Reference_PDF/` stores the main-paper PDFs that have already been archived locally for this project.

In the current public GitHub version, this directory functions as the PDF library for the papers that have already been included in the review corpus and for which a local PDF is available. The folder structure remains organized by scientific domain so that readers can browse the corpus directly, spot-check sources, and return to the original papers during review writing.

## How This Structured Literature Management System Works

The current public GitHub release keeps a minimal, publication-facing subset of the project. It has three core parts:

1. `Reference_PDF/`
   The local PDF archive for papers whose main-paper PDFs are already available.
2. `Data/`
   The structured data layer, including paper records, PDF inventories, missing-PDF inventories, classification indices, and stable discipline-code mappings.
3. `scripts/`
   The scripts used to read, validate, build, and query the structured data products.

In one sentence:

> `Reference_PDF` stores the papers themselves, `Data` stores the structured records, and `scripts` provides the processing and query layer.

## How To Use This Repository When a PDF Exists or Does Not Exist

### 1. Papers With a Local PDF

If a paper already has a local PDF, look for it directly under `Reference_PDF/`, using the scientific-domain subdirectories.

The most useful companion files are:

- `Data/pdf_manifest.json`
  Lists which papers already have local PDFs, together with their `paper_id`, title, PDF path, classification information, and evidence status.
- `Data/papers.jsonl`
  Provides the full structured record for each public paper in the GitHub subset.

### 2. Papers Without a Local PDF

If a paper does not have a local main-paper PDF, do not look for it in `Reference_PDF/`. Instead, check:

- `Data/missing_pdf_manifest.json`

This file records the papers that currently do not have a locally archived main-paper PDF but still have a usable evidence route through DOI landing pages, publisher HTML, official article pages, abstracts, supplementary files, project pages, or related public source paths.

## Most Important Files

- `Data/papers.jsonl`
  The main structured record set for the current public paper subset.
- `Data/papers.sqlite`
  The queryable SQLite database for the current public paper subset.
- `Data/classification_code_index.json`
  The classification vocabulary and code mapping.
- `Data/discipline_code_assignments.jsonl`
  The stable discipline-code ledger.
- `Data/discipline_local_code_registry.jsonl`
  The current snapshot that maps papers to stable discipline-local codes.
- `Data/pdf_manifest.json`
  The inventory of papers with locally archived PDFs.
- `Data/missing_pdf_manifest.json`
  The inventory of papers without a local main-paper PDF but with retained evidence routes.

## Common Query Workflow

To inspect the current public subset at a high level, start with:

```powershell
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" summary
```

If you want to inspect the structured records directly, use:

- `Data/papers.jsonl`
- `Data/papers.sqlite`

If you want to see which public papers already have a local PDF, use:

- `Data/pdf_manifest.json`

If you want to see which public papers do not yet have a local PDF but are still tracked through alternative evidence, use:

- `Data/missing_pdf_manifest.json`

## Scope of the Current Public GitHub Release

The current GitHub release is a minimal public-facing subset for literature archiving and structured-data presentation. It is not the full internal production environment.

In practice, this means:

- GitHub keeps `Reference_PDF + Data + scripts`
- the public structured record set has been reduced to the `447` included confirmed-core papers
- additional internal process files, working logs, and broader local maintenance layers are not fully exposed in this public subset

## If the Corpus Continues To Be Maintained

The maintenance logic is straightforward:

1. First determine whether a paper already has a local PDF.
2. If a PDF exists, archive it under `Reference_PDF/` and register it in the structured data layer.
3. If no PDF exists, retain at least a DOI, HTML page, official page, abstract, or equivalent evidence route, and register that state through the structured missing-PDF layer.
4. After that, use `Data/` and `scripts/` for querying, filtering, and counting, rather than relying only on manual folder browsing.
