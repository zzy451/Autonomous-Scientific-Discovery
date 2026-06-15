# To-Read Paper Note Batch

Date: 2026-06-15

## Scope

This report records the first large-scale note-writing batch for the Scientific Agent review. The batch targeted all `to_read` records that did not yet have a note path after resolving the `needs_review` records.

- Core `to_read` records after needs-review resolution: 62
- Existing `to_read` notes before this batch: 8
- New notes created in this batch: 54
- Total populated note paths after this batch: 64, including 62 `to_read` notes and 2 background notes

## Workflow

Six worker agents were assigned disjoint ID ranges. Workers wrote note files only and did not modify `Paper_Lists/agent_master_paper_list.md` or policy files. The main workflow integrated note paths, checked coverage, and applied one object-priority classification correction.

## Batch Outputs

### Batch A: `ASD-0001` to `ASD-0013`

Created notes for `ASD-0001`, `ASD-0002`, `ASD-0004`, `ASD-0006`, `ASD-0008`, `ASD-0009`, `ASD-0010`, `ASD-0012`, `ASD-0013`.

Evidence levels:

- full-text: `ASD-0001`, `ASD-0002`, `ASD-0004`, `ASD-0008`, `ASD-0009`, `ASD-0010`, `ASD-0012`, `ASD-0013`
- abstract+metadata: `ASD-0006`

Key follow-up points:

- `ASD-0004`: master-list title says NovelSeek, but note/PDF indicate InternAgent; metadata needs correction.
- `ASD-0006`: PDF access limited; verify inclusion strength and whether domain should remain `06`, move to `07`, or move to `01.04`.

### Batch B: `ASD-0014` to `ASD-0031`

Created notes for `ASD-0014`, `ASD-0017`, `ASD-0018`, `ASD-0019`, `ASD-0020`, `ASD-0022`, `ASD-0024`, `ASD-0026`, `ASD-0031`.

Evidence levels:

- full-text: `ASD-0017`, `ASD-0018`, `ASD-0019`, `ASD-0020`, `ASD-0022`, `ASD-0024`, `ASD-0026`, `ASD-0031`
- abstract+metadata: `ASD-0014`

Key follow-up points:

- `ASD-0014`: needs PDF-level verification and more precise benchmark/result evidence.
- `ASD-0022`: may be described as chemistry/materials crossover in synthesis tables, while main class remains `03`.

### Batch C: `ASD-0032` to `ASD-0051`

Created notes for `ASD-0032`, `ASD-0033`, `ASD-0034`, `ASD-0036`, `ASD-0040`, `ASD-0041`, `ASD-0046`, `ASD-0048`, `ASD-0051`.

Evidence levels:

- full-text: `ASD-0032`, `ASD-0033`, `ASD-0036`, `ASD-0040`, `ASD-0041`, `ASD-0046`, `ASD-0048`, `ASD-0051`
- abstract+metadata: `ASD-0034`

Key follow-up points:

- `ASD-0033`: `06` vs `07` can be revisited if later biomedical translation emphasis dominates.
- `ASD-0034`: PMLR PDF access failed; needs full-text verification of components, metrics, ablations, and true closed loop.

### Batch D: `ASD-0054` to `ASD-0065`

Created notes for `ASD-0054`, `ASD-0055`, `ASD-0057`, `ASD-0058`, `ASD-0060`, `ASD-0062`, `ASD-0063`, `ASD-0064`, `ASD-0065`.

Evidence levels:

- full-text: `ASD-0057`, `ASD-0058`, `ASD-0060`, `ASD-0062`, `ASD-0063`, `ASD-0064`, `ASD-0065`
- abstract+metadata: `ASD-0054`, `ASD-0055`

Key follow-up points:

- `ASD-0054`, `ASD-0055`: bioRxiv/PDF access limited; supplement with full-text page evidence later.
- `ASD-0060`, `ASD-0062`: note files use 2026 because current arXiv/PDF versions appear to be 2026; master-list metadata still needs a separate version check.
- `ASD-0062`: `09` vs `01.04` remains a boundary between engineering/scientific workflow infrastructure and general research-Agent infrastructure.

### Batch E: `ASD-0068` to `ASD-0080`

Created notes for `ASD-0068`, `ASD-0069`, `ASD-0070`, `ASD-0071`, `ASD-0075`, `ASD-0076`, `ASD-0077`, `ASD-0079`, `ASD-0080`.

Evidence levels:

- full-text: all nine records

Key follow-up points:

- `ASD-0070`: verify the distribution of 124 hypotheses and whether main class should remain `03`.
- `ASD-0071`: `06` vs `07` can be revisited if disease translation dominates.
- `ASD-0077`: biomedical benchmark agent; avoid describing it as experimentally validated discovery.
- `ASD-0079`: note indicates DTI prediction rather than drug repurposing; master-list title/remark should be corrected in a metadata-cleanup pass.

### Batch F: `ASD-0081` to `ASD-0100`

Created notes for `ASD-0081`, `ASD-0083`, `ASD-0085`, `ASD-0089`, `ASD-0090`, `ASD-0091`, `ASD-0096`, `ASD-0097`, `ASD-0100`.

Evidence levels:

- full-text: `ASD-0081`, `ASD-0083`, `ASD-0085`, `ASD-0089`, `ASD-0090`, `ASD-0091`, `ASD-0096`, `ASD-0100`
- abstract+metadata: `ASD-0097`

Key follow-up points:

- `ASD-0083`: object-priority correction applied. Main class moved from `01.04` to `07.04` because full-text note indicates dry AMD drug repurposing / therapeutic discovery.
- `ASD-0097`: Nature Methods 2026 page confirms metadata, but full text access was blocked; note remains abstract+metadata.
- `ASD-0085`: arXiv PDF was damaged; note used PMC full text and DOI metadata.

## Integration Actions

- Updated all 62 `to_read` records with populated note paths.
- Updated note coverage count in `agent_master_paper_list.md` to 64 populated paths.
- Applied object-priority correction for `ASD-0083 Robin`: `01.04` -> `07.04`.

## Remaining Follow-Up Queue

1. Full-text supplementation needed for abstract/metadata-level notes: `ASD-0006`, `ASD-0014`, `ASD-0034`, `ASD-0054`, `ASD-0055`, `ASD-0097`.
2. Metadata cleanup candidates: `ASD-0004`, `ASD-0060`, `ASD-0062`, `ASD-0079`, `ASD-0097`.
3. Boundary classification review candidates: `ASD-0006`, `ASD-0033`, `ASD-0062`, `ASD-0064`, `ASD-0071`, `ASD-0077`.
4. Avoid overclaiming discovery strength for benchmark-only or simulation-only systems in the final review tables.
