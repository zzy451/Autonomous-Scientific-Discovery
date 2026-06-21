# Relaxed multi-module round-2 P1-P audit

> Date: 2026-06-21
> Scope: P1 concrete-module boundary follow-up focused on `ASD-0543`.
> Rule: only high-confidence changes supported by first-hand paper evidence, official project assets, or other authoritative first-hand sources are written back to the master list and Notes.

## 本轮结论

本轮关闭 1 条 `06 / 07` 高压边界记录：

| ID | Title short | Sources checked | Decision | Note action |
|---|---|---|---|---|
| `ASD-0543` | ML Copilot Agent | Crossref DOI metadata and deposited reference list `10.2139/ssrn.5343855`; official author Hugging Face datasets `Project-Lambda-TCGA-HNSCC` and `Case-Study-HNSCC-ML-Copilot-Agent`; official PyPI / repo / docs | accepted `scientific_object_modules=06;07`; set `primary_module_for_filing=07` in the relaxed overlay | revised `Notes/06_Life_Sciences/Patel_2025_ML_Copilot_Prognostic_Gene_Discovery.md` |

## Evidence summary

### `ASD-0543` Machine Learning Copilot Agent: An LLM-Guided Workflow for Prognostic Gene Discovery

- Agent evidence: the title explicitly states `Copilot Agent` and `LLM-Guided Workflow`, while the official package / repo / docs confirm a multi-step ML assistant with preprocessing, model training, evaluation, plotting, and code-execution workflow structure.
- `06` evidence: the paper is directly framed as `prognostic gene discovery`, and the official case-study assets include `survival_associated_genes.txt`, `selected_features.txt`, and gene-expression / molecular-feature files that keep gene-level discovery as a stable life-science object.
- `07` evidence: the official author datasets provide direct disease/prognosis objects rather than only generic bioinformatics data. `Project-Lambda-TCGA-HNSCC` exposes HNSCC patient records with `Overall Survival Status`, `Overall Survival (Months)`, `Disease-specific Survival status`, `Progression Free Status`, AJCC staging, and ICD-coded disease metadata. `Case-Study-HNSCC-ML-Copilot-Agent` exposes HNSCC survival tables and treatment-subtype candidate outputs such as `CDK_inhibitors_candidate`, `EGFR_mAb_candidate`, and `Immunotherapy_candidate`.
- Why the boundary is now closed: unlike the earlier source-limited pass, this round adds official author-owned case-study datasets whose filenames, cohort labels, and column structure directly expose patient-level prognosis and disease-endpoint objects. Even though the SSRN abstract/full text remains access-blocked, the accessible official datasets are now strong enough to support independent medical-object coverage under the relaxed object-first rule.
- Accepted action: close the `06 / 07` boundary as `06;07`, with `07` as the relaxed primary filing direction and `06` retained for prognostic-gene / survival-associated-gene discovery coverage.

## Count update

Post-P1-P relaxed overlay counts increase only in module `07`:

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 55 |
| `02` | 37 |
| `03` | 82 |
| `04` | 110 |
| `05` | 35 |
| `06` | 75 |
| `07` | 71 |
| `08` | 3 |
| `09` | 36 |
| `10` | 24 |
| `11` | 35 |

| Metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 561 |
| Independent `01.04` general-method bucket count | 20 |

## Remaining uncertainty

- The SSRN abstract and full text remain desirable for richer workflow reconstruction, page-level note citations, and final section synthesis.
- However, top-level module uncertainty is no longer strong enough to keep this record open in the round-2 queue, because the official author datasets already provide direct disease/prognosis object evidence in addition to gene-level discovery evidence.
