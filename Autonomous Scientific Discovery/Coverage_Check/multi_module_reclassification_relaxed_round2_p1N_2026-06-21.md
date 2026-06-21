# Relaxed multi-module round-2 P1-N audit

> Date: 2026-06-21
> Scope: P1 concrete-module boundary follow-up focused on `ASD-0543` and `ASD-0547`.
> Rule: only high-confidence changes supported by first-hand paper evidence are written back to the master list and Notes.

## 本轮结论

本轮复核 2 条 P1 边界记录，其中 1 条在 source-limited 的一手证据下可以收口为单模块维持项，1 条仍保留在 full-text follow-up 队列中：

| ID | Title short | Sources checked | Decision | Note action |
|---|---|---|---|---|
| `ASD-0543` | ML Copilot Agent | DOI redirect to SSRN landing `10.2139/ssrn.5343855`; Crossref DOI metadata / deposited reference list; official docs / PyPI / GitHub | no landed master-list rewrite; current first-hand evidence is source-limited, but it raises strong `06 / 07` pressure | revised note with source-limited round-2 boundary update |
| `ASD-0547` | Pixelated metasurface design | Crossref DOI record `10.1117/12.3091089`; DOI resolver / official SPIE landing URL | accepted `scientific_object_modules=04`; keep `primary_module_for_filing=04`; do not add `09` | revised `Notes/04_Materials_Science/Lee_2026_Closed_Loop_Pixelated_Metasurface_Design.md` |

## Evidence summary

### `ASD-0543` Machine Learning Copilot Agent: An LLM-Guided Workflow for Prognostic Gene Discovery

- Agent evidence: the paper title itself explicitly frames a `Copilot Agent` and an `LLM-Guided Workflow`, while the same-name official project sources describe a multi-step ML workflow assistant with code/tool execution.
- `06` pressure: the title directly names `gene discovery`, which is recognizable life-science object coverage.
- `07` pressure: the title also directly names `prognostic`, and the DOI-deposited Crossref reference list is strongly oncology / clinical-prognosis oriented, including head and neck squamous cell carcinoma prognostic signatures, lung-adenocarcinoma prognosis, proteogenomics in breast cancer, and healthcare / biomedical ML references.
- Why no landed rewrite is written back this round: the SSRN abstract and full text remained inaccessible in the current audit environment, so the evidence is still too source-limited for a confident landed `06;07` master-list rewrite. Under the current merge discipline, this should stay in the queue rather than be forced.
- Accepted action: keep the master-list row stable for now, but revise the note so it no longer reads like a comfortable `06`-only case.

### `ASD-0547` Closed-loop experimental AI for pixelated metasurface design

- Agent evidence: the title explicitly presents a `closed-loop experimental AI` system, and the DOI resolves to an official SPIE proceedings record in `Photonic and Phononic Properties of Engineered Nanostructures XVI`, which keeps the paper inside the project's Agent workflow boundary rather than reducing it to a generic offline model.
- `04` evidence: the stable named object is `pixelated metasurface design`, i.e. a photonic / nanostructure / metasurface material-design object.
- Why `09` is not accepted: the accessible first-hand sources do show engineering-like workflow language, but they do not expose enough abstract/body detail to show that the paper becomes an independent engineering-system, manufacturing-process, or control-system study. Under the object-first rule, that is not enough to add `09`.
- Accepted action: close the `04 / 09` boundary as `04` only, and revise the note so it no longer remains a generic weak-evidence follow-up placeholder.

## Count update

Post-P1-N relaxed overlay counts are unchanged relative to the post-P1-M state because `ASD-0547` lands as a single-module `04` record and `ASD-0543` remains open:

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 55 |
| `02` | 37 |
| `03` | 82 |
| `04` | 110 |
| `05` | 35 |
| `06` | 75 |
| `07` | 70 |
| `08` | 3 |
| `09` | 36 |
| `10` | 24 |
| `11` | 35 |

| Metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 560 |
| Independent `01.04` general-method bucket count | 20 |

## Remaining uncertainty

- `ASD-0543` remains a live `06 / 07` queue item. The title and biomedical reference context create real multi-module pressure, but a landed rewrite should wait for an accessible SSRN abstract or full text.
- `ASD-0547` is no longer a live `04 / 09` boundary question at the current evidence level, although full SPIE abstract/PDF access would still help future note enrichment and page-level comparative synthesis.
