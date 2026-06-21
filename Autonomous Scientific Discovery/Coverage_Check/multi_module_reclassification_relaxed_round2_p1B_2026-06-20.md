# Relaxed multi-module round-2 P1-B audit

> Date: 2026-06-20
> Scope: P1 concrete-module boundary follow-up focused on `ASD-0054`.
> Rule: only high-confidence changes supported by first-hand paper evidence are written back to the master list and Notes.

## 本轮结论

本轮落地 1 条高置信 P1 边界更新：

| ID | Title short | Sources checked | Decision | Note action |
|---|---|---|---|---|
| `ASD-0054` | Virtual Lab nanobodies | Nature full-text PDF for DOI `10.1038/s41586-025-09442-9` | accepted `scientific_object_modules=07;06`; keep `primary_module_for_filing=07`; `general_method_bucket=none` | revised `Notes/07_Medical_and_Health_Sciences/Swanson_2025_Virtual_Lab_Nanobodies.md` |

## Evidence summary

### `ASD-0054` The Virtual Lab

- Agent evidence: AI-human multi-agent research collaboration with PI agent, Scientific Critic, multiple scientist agents, tool implementation, workflow design, candidate generation, and experimental validation.
- `07` evidence: the end objective is therapeutic nanobody / binder discovery against recent SARS-CoV-2 variants, which remains a biomedical / drug-discovery object.
- `06` evidence: the full text directly studies nanobody, spike-RBD, and protein-complex objects; the workflow mutates four starting nanobodies, designs 92 mutant nanobodies, and validates expression, solubility, and ELISA binding in wet-lab assays. These are concrete life-science object results under the relaxed rule.
- Accepted action: add `06` while preserving legacy filing and `primary_module_for_filing` under `07`.

## Count update

Post-P1-B partial overlay counts:

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

- `ASD-0033` and `ASD-0035` were not landed in this round because first-hand full-text access was still blocked by publisher / preprint delivery constraints in this run.
- No taxonomy-level instability was found in this slice; `ASD-0054` is a straightforward `07/06` multi-module case once the full text is checked.
