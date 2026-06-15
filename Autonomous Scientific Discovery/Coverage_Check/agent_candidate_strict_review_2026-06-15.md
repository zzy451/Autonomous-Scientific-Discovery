# Scientific Agent Candidate Strict Review

Date: 2026-06-15

## 1. Scope

This report records the second-pass strict review of records marked `candidate` in `Paper_Lists/agent_master_paper_list.md`.

Review question:

> Is this paper a scientific Agent paper under the project inclusion criteria?

Minimum inclusion criteria:

1. Clear scientific research goal.
2. Multi-step action process.
3. At least one Agent capability: planning, tool use, feedback iteration, autonomous decision-making, or multi-agent collaboration.
4. A clear role in the scientific research workflow.

This review uses the project rule that inclusion is based on **Agent** criteria, not on whether a paper calls itself Autonomous Scientific Discovery. `ASD` remains a topic/system attribute and project name, not the screening gate.

## 2. Inputs

- Master list: `Paper_Lists/agent_master_paper_list.md`
- Candidate snapshot for review: `Paper_Lists/candidate_review_batch_all.json`
- Candidate count before review: 89
- Review method: four read-only sub-agent batches, followed by main-agent integration under the project policy files.

## 3. Review Batches

| Batch | ID range | Reviewer | Result |
|---|---|---|---|
| Batch A | `ASD-0001` to `ASD-0029` | Kepler | completed |
| Batch B | `ASD-0030` to `ASD-0059` | Lorentz | completed |
| Batch C | `ASD-0060` to `ASD-0089` | Ramanujan | completed |
| Batch D | `ASD-0090` to `ASD-0110` | Parfit | completed |

The sub-agents performed metadata/abstract-level screening only and did not modify files. Final list updates were integrated conservatively in the master list.

## 4. Decision Summary

Before strict review:

| Status | Count |
|---|---:|
| candidate | 89 |
| to_read | 8 |
| background_only | 6 |
| excluded | 7 |
| needs_review | 0 |

After strict review:

| Status | Count |
|---|---:|
| candidate | 15 |
| to_read | 61 |
| background_only | 20 |
| excluded | 11 |
| needs_review | 3 |

Main interpretation:

- `to_read`: high-value or plausible scientific Agent paper that should receive full-text reading and a formal note.
- `candidate`: still plausible but lower-confidence from metadata; keep for later targeted review.
- `background_only`: useful survey, benchmark, dataset, toolkit, or boundary paper, but not counted as a core system paper.
- `excluded`: duplicate, non-Agent AI-for-Science/model paper, or general Agent method without scientific workflow role.
- `needs_review`: boundary cases requiring full-text judgment before inclusion or exclusion.

## 5. Per-Paper Decisions

### Upgraded to `to_read`

`ASD-0001`, `ASD-0002`, `ASD-0004`, `ASD-0006`, `ASD-0008`, `ASD-0009`, `ASD-0010`, `ASD-0012`, `ASD-0013`, `ASD-0014`, `ASD-0017`, `ASD-0018`, `ASD-0019`, `ASD-0020`, `ASD-0022`, `ASD-0024`, `ASD-0026`, `ASD-0031`, `ASD-0032`, `ASD-0033`, `ASD-0034`, `ASD-0036`, `ASD-0040`, `ASD-0041`, `ASD-0046`, `ASD-0048`, `ASD-0051`, `ASD-0054`, `ASD-0055`, `ASD-0058`, `ASD-0060`, `ASD-0062`, `ASD-0063`, `ASD-0064`, `ASD-0065`, `ASD-0068`, `ASD-0069`, `ASD-0070`, `ASD-0071`, `ASD-0075`, `ASD-0076`, `ASD-0077`, `ASD-0079`, `ASD-0080`, `ASD-0081`, `ASD-0083`, `ASD-0085`, `ASD-0089`, `ASD-0090`, `ASD-0091`, `ASD-0096`, `ASD-0097`, `ASD-0100`.

Rationale: these records show clear signs of multi-step scientific Agent workflows, such as planning, tool use, feedback iteration, multi-agent collaboration, robot/experiment interaction, code execution, or end-to-end research automation.

### Kept as `candidate`

`ASD-0003`, `ASD-0007`, `ASD-0025`, `ASD-0028`, `ASD-0029`, `ASD-0030`, `ASD-0038`, `ASD-0044`, `ASD-0045`, `ASD-0047`, `ASD-0049`, `ASD-0053`, `ASD-0059`, `ASD-0061`, `ASD-0095`.

Rationale: these records remain plausible Agent papers, but metadata suggests weaker discovery closure, stronger QA/tool/benchmark character, or unresolved title/task ambiguity.

### Downgraded to `background_only`

`ASD-0011`, `ASD-0015`, `ASD-0023`, `ASD-0027`, `ASD-0043`, `ASD-0052`, `ASD-0067`, `ASD-0072`, `ASD-0074`, `ASD-0078`, `ASD-0082`, `ASD-0086`, `ASD-0107`, `ASD-0109`.

Rationale: these are mainly surveys, benchmarks, datasets, general research-support tools, duplicate/preprint background records, or systems where the scientific discovery Agent loop is not strong enough for core statistics.

### Moved to `excluded`

`ASD-0039`, `ASD-0092`, `ASD-0108`, `ASD-0110`.

Rationale: `ASD-0039` and `ASD-0110` appear to be non-Agent model/tool papers under the current criteria; `ASD-0092` and `ASD-0108` are duplicate records where canonical records are retained elsewhere.

### Moved to `needs_review`

`ASD-0057`, `ASD-0066`, `ASD-0087`.

Rationale:

- `ASD-0057`: may be chemical/process engineering automation, but Agent loop and scientific discovery role are unclear.
- `ASD-0066`: spacecraft autonomy is clear, but the scientific observation/discovery workflow role is unclear.
- `ASD-0087`: therapeutic tool-use reasoning is strong, but it may be clinical/therapeutic QA rather than scientific discovery research.

## 6. Classification Corrections Applied

- `ASD-0033`: moved from `07` to `06` pending full text, because the apparent object is single-cell/omics discovery rather than clinical medicine.
- `ASD-0036`: secondary class changed from `03.04` to `03.03`, because the object is automated chemical experimentation/synthesis.
- `ASD-0040`: moved from `06` to `01.04`, because the object is a general research idea-generation Agent.
- `ASD-0057`: moved to `09` pending review, because the apparent object is chemical/process engineering diagrams or process systems.
- `ASD-0058`: moved from `06` to `02`, because the object is astrobiology/space-science hypothesis generation.
- `ASD-0074`: moved from `06` to `01.04` as literature research/RAG Agent background.
- `ASD-0080`: moved from `03` to `04`, because MOFs are treated as materials objects in this taxonomy.
- `ASD-0086`: linked conceptually to canonical `ASD-0084` and marked as duplicate/preprint background.

## 7. Follow-Up Actions

1. Write full paper notes for the 61 `to_read` records, prioritizing Nature/Science-family, wet-lab/robotic closed-loop, and high-impact general research-Agent systems.
2. Resolve the three `needs_review` records before core statistics.
3. Do a targeted pass on the remaining 15 `candidate` records to decide whether they become `to_read`, `background_only`, or `excluded`.
4. Update metadata for records flagged in remarks, especially suspected title/version issues: `ASD-0004`, `ASD-0029`, `ASD-0079`, and `ASD-0097`.
5. Use `background_only` records for taxonomy, benchmark, evaluation, and citation-expansion context, but do not count them as core scientific Agent systems.
