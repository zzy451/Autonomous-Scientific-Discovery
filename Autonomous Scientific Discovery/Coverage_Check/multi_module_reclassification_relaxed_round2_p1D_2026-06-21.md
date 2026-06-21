# Relaxed multi-module round-2 P1-D audit

> Date: 2026-06-21
> Scope: P1 concrete-module boundary follow-up focused on `ASD-0035`.
> Rule: only high-confidence changes supported by first-hand paper evidence are written back to the master list and Notes.

## 本轮结论

本轮关闭 1 条 P1 边界项：

| ID | Title short | Sources checked | Decision | Note action |
|---|---|---|---|---|
| `ASD-0035` | SciAgents | arXiv abstract `2409.05556`; canonical DOI landing for `10.1002/adma.202413523` | accepted `scientific_object_modules=04`; keep `primary_module_for_filing=04`; do not add `06` | revised `Notes/04_Materials_Science/Ghafarollahi_2025_SciAgents.md` |

## Evidence summary

### `ASD-0035` SciAgents

- Agent evidence: the official arXiv abstract presents SciAgents as a multi-agent intelligent graph-reasoning framework that combines ontological knowledge graphs, LLMs, data-retrieval tools, and in-situ learning to autonomously generate and refine scientific hypotheses.
- `04` evidence: the same abstract explicitly states that the system is applied to biologically inspired materials and that it yields material discoveries, design principles, and unexpected material properties. This keeps the final object on the materials-discovery side.
- Why `06` is not accepted: the available first-hand evidence does contain biologically inspired / biological-system language, but it does not report independent life-science object experiments, biological mechanism studies, or separate protein / cell / tissue discovery tasks. The biological motifs function as inspiration or ingredients within biomaterial hypotheses rather than as standalone life-science research objects under the relaxed rule.
- Accepted action: close the `04` plus possible biology boundary as `04` only, and revise the note so it no longer stays in a vague “full-text pending, maybe biology” state.

## Count update

Post-P1-D partial overlay counts are unchanged because `ASD-0035` lands as a single-module `04` record:

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 55 |
| `02` | 37 |
| `03` | 79 |
| `04` | 108 |
| `05` | 35 |
| `06` | 74 |
| `07` | 68 |
| `08` | 3 |
| `09` | 36 |
| `10` | 24 |
| `11` | 34 |

| Metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 553 |
| Independent `01.04` general-method bucket count | 19 |

## Remaining uncertainty

- Full Wiley text would still be useful for richer note details and case-study extraction, but it is not required to reject `06` at the current evidence level because no first-hand source currently shows an independent life-science object experiment.
- No taxonomy-level instability was found in this slice; this is a clean example of “bio-inspired materials” not automatically implying a separate life-science module.
