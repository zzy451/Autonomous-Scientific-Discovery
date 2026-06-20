# Relaxed multi-module round-2 P1-A audit

> Date: 2026-06-20
> Scope: first P1 concrete-module boundary pass after P0-E.
> Rule: high-confidence module additions require first-hand paper evidence; legacy Notes are only leads.

## 本轮结论

本轮复核 3 条 P1 queue 边界记录，其中 2 条有可解析全文并接受 high-confidence relaxed multi-module 更新，1 条因全文访问失败保留在 follow-up。

| ID | Title short | Sources checked | Decision | Note action |
|---|---|---|---|---|
| `ASD-0003` | ChemAgent / CheMatAgent | arXiv PDF `2506.07551` | accepted `scientific_object_modules=03;04`; keep `primary_module_for_filing=03`; `general_method_bucket=none` | revised `Notes/03_Chemical_Sciences/Wu_2025_ChemAgent.md` |
| `ASD-0008` | Tippy DMTA | arXiv PDF `2507.09023` | accepted `scientific_object_modules=07;03`; keep `primary_module_for_filing=07`; `general_method_bucket=none` | revised `Notes/07_Medical_and_Health_Sciences/Fehlis_2025_Tippy_DMTA.md` |
| `ASD-0014` | SpatialAgent | bioRxiv DOI / official-public PDF attempt; PDF blocked or damaged | no accepted change; remains `06` pending full-text review for possible `07` | no note rewrite this round |

## Evidence summary

### `ASD-0003` ChemAgent / CheMatAgent

- Agent evidence: LLM-based tool-learning agent with tool retrieval, policy / execution split, HE-MCTS search, and critic models.
- `03` evidence: ChemToolBench chemistry QA / discovery tasks and chemistry tool use remain the primary object evidence.
- `04` evidence: full text reports a Materials Science split, includes materials tooling such as `pymatgen`, and evaluates single- and multiple-calling tasks on Materials Science benchmark splits.
- Accepted action: add relaxed `04` module while preserving legacy filing under `03`.

### `ASD-0008` Tippy DMTA

- Agent evidence: multi-agent system with Supervisor, Molecule, Lab, Analysis, Report, and Safety Guardrail agents coordinating DMTA workflows.
- `07` evidence: paper is explicitly framed around drug discovery and DMTA optimization.
- `03` evidence: full text and appendix report molecule generation, synthesis workflow scheduling, HPLC analysis, retention-time use, purity / yield reporting, and a COVID drug molecule demonstration derived from Ensitrelvir.
- Accepted action: add relaxed `03` module while preserving legacy filing under `07`.

### `ASD-0014` SpatialAgent

- Current issue: the local Note already suggests spatial biology object evidence, but the note itself records that it used abstract / metadata / official repository rather than full text.
- This run: direct bioRxiv PDF access returned 403; the alternate publicly linked PDF download produced a damaged file that `pdftotext` could not parse.
- Decision: no high-confidence `07` addition from notes or damaged PDF. Keep as full-text-required boundary item.

## Count update

Post-P1-A partial overlay counts:

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 55 |
| `02` | 37 |
| `03` | 79 |
| `04` | 108 |
| `05` | 35 |
| `06` | 73 |
| `07` | 68 |
| `08` | 3 |
| `09` | 36 |
| `10` | 24 |
| `11` | 34 |

| Metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 552 |
| Independent `01.04` general-method bucket count | 19 |

## Remaining uncertainty

- `ASD-0014` remains open until a parseable full text or official full-text source confirms whether disease / clinical-translation evidence supports `07` beyond `06` spatial biology.
- No taxonomy-level instability was found in this small slice; both landed changes follow the relaxed object-experiment / benchmark-task rule.
