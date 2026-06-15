# ASD Coverage Check: Needs-Review Resolution

Date: 2026-06-15

## 1. Scope

This report records the first rough-screen pass over records previously marked `needs_review` in `Paper_Lists/agent_master_paper_list.md`.

The pass is metadata/source-record based. It does not replace full-text reading. Its purpose is to remove obvious non-Agent entries, merge duplicates, and return plausible science-Agent records to the candidate pool.

## 2. Updated Status Counts

Total records: 110

| Inclusion status | Count |
|---|---:|
| `candidate` | 89 |
| `to_read` | 8 |
| `background_only` | 6 |
| `excluded` | 7 |
| `needs_review` | 0 |

| Main class | Count |
|---|---:|
| `01` | 22 |
| `02` | 3 |
| `03` | 26 |
| `04` | 16 |
| `06` | 17 |
| `07` | 14 |
| `09` | 3 |

No populated note paths are missing.

## 3. Records Returned to Candidate Pool

| ID | New status | Main class | Reason |
|---|---|---|---|
| `ASD-0053` | `candidate` | `01.04` | Autonomous hypothesis verification may be a general research-Agent workflow. |
| `ASD-0060` | `candidate` | `01.04` | Multi-agent collaboration for scientific discovery; plausible general scientific Agent system. |
| `ASD-0072` | `candidate` | `01.04` | Open co-scientist / data-driven discovery benchmark or workflow; plausible scientific Agent relevance. |
| `ASD-0083` | `candidate` | `01.04` | Multi-agent system explicitly for automating scientific discovery. |
| `ASD-0089` | `candidate` | `01.04` | Multi-agent codification of research methodologies; plausible research-workflow Agent. |
| `ASD-0090` | `candidate` | `02.03` | Self-driving laboratory applied to quantum computing; scientific object is quantum computing. |
| `ASD-0100` | `candidate` | `01.04` | Agent-driven algorithmic reproduction benchmark; canonical record after duplicate merge. |

## 4. Records Marked Background-Only

| ID | New status | Main class | Reason |
|---|---|---|---|
| `ASD-0088` | `background_only` | `07.04` | High-value Cell framework/perspective on biomedical AI agents; not counted as core system unless full text shows a concrete Agent system. |
| `ASD-0099` | `background_only` | `01.04` | Scientific coding benchmark; useful for evaluation context, but not itself an Agent system. |
| `ASD-0102` | `background_only` | `01.04` | General autonomous AI-agent review; useful for boundary/background. |

## 5. Records Excluded

| ID | Reason |
|---|---|
| `ASD-0042` | General LLM-agent planning method; no clear scientific research object or scientific workflow role. |
| `ASD-0050` | Duplicate record of `ASD-0100`; canonical record retained as `ASD-0100`. |
| `ASD-0073` | LLM assistance for causal experimental design; Agent loop and autonomous scientific workflow role are unclear from the source record. |
| `ASD-0098` | Literature-review toolkit; autonomous Agent loop and concrete scientific discovery role are unclear. |
| `ASD-0104` | General agentic-system evaluation and dataset paper; no clear scientific research object. |
| `ASD-0105` | General tool-learning paper; not specific to scientific discovery or a scientific research object. |
| `ASD-0106` | General LLM-agent tool-use instruction method; no clear scientific research object or scientific Agent workflow. |

## 6. Remaining Risks

- Some returned `01.04` candidates may become `excluded` after full-text reading if they lack a genuine Agent loop.
- Some `background_only` records may still be useful for definitions, benchmarks, or related-work framing.
- The new `02.03` quantum-computing self-driving-lab candidate needs careful classification against `01` because quantum computing can be treated as computational science or physical/quantum science depending on the paper's final object.

## 7. Next Actions

1. Full-read the 8 `to_read` core system papers.
2. Decide whether `ASD-0088` remains `background_only` after full-text inspection.
3. Create notes for the strongest `01.04` candidates only after verifying the Agent inclusion criteria.
4. Begin citation expansion from the core papers and from domain-specific surveys such as Ramos et al. 2025.
