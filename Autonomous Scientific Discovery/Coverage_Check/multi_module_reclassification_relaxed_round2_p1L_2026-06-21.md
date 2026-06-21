# Relaxed multi-module round-2 P1-L audit

> Date: 2026-06-21
> Scope: P1 concrete-module boundary follow-up focused on `ASD-0539`, `ASD-0609`, and `ASD-0664`.
> Rule: only high-confidence changes supported by first-hand paper evidence are written back to the master list and Notes.

## 本轮结论

本轮关闭 3 条 P1 边界项，其中 2 条接受多模块扩展，1 条在复核后维持单模块：

| ID | Title short | Sources checked | Decision | Note action |
|---|---|---|---|---|
| `ASD-0539` | AI-Agent materials discovery | official JMI HTML page for DOI `10.20517/jmi.2025.69` | accepted `scientific_object_modules=03;04`; keep `primary_module_for_filing=04` | revised `Notes/04_Materials_Science/Wang_2026_AI_Agent_Materials_Discovery.md` |
| `ASD-0609` | Automated pH adjustment | ChemRxiv full-text PDF; ScienceDirect publisher page / abstract | kept `scientific_object_modules=03` only; keep `primary_module_for_filing=03` | revised `Notes/03_Chemical_Sciences/Pomberger_2022_Automated_pH_Adjustment.md` |
| `ASD-0664` | CatMaster computational catalysis | arXiv abstract; arXiv full-text HTML `2601.13508v1`; official CatMaster repository | accepted `scientific_object_modules=03;04`; keep `primary_module_for_filing=03` | revised `Notes/03_Chemical_Sciences/Unknown_2026_Autonomous_Computational_Catalysis.md` |

## Evidence summary

### `ASD-0539` Accelerating materials discovery via AI-Agent integration of large language models and simulation tools

- Agent evidence: the official JMI page describes an AI-Agent platform that interprets natural-language requests, dynamically assembles task-specific workflows from simulation tools, and executes the resulting materials-research calculations.
- `04` evidence: one representative case is a goal-driven electronic-structure calculation for periodic monolayer transition metal dichalcogenides, which is stable materials-side object coverage.
- `03` evidence: the same official page explicitly reports an inverse design of battery electrolyte additives based on user-defined targets for molecular weight and frontier orbital energies. Under the current relaxed rule, this is identifiable molecular / chemistry-side object evidence rather than a merely rhetorical downstream application.
- Accepted action: close the `04 / 03` boundary as `03;04`, while keeping `04` as `primary_module_for_filing` because the paper remains framed and filed as a materials-discovery system.

### `ASD-0609` Automated pH Adjustment Driven by Robotic Workflows and Active Machine Learning

- Agent evidence: the system runs a closed-loop robotic workflow that predicts the next acid/base addition, executes the step, measures the intermediate state, and iterates with active machine learning.
- `03` evidence: the validated objects remain buffered chemical systems, including acetate, citrate, KH2PO4, ammonium, and related multi-buffer compositions, together with their titration / pH-response behavior.
- Why `09` is not accepted: publisher-facing industrial / process-control language is present, but the reported experiments do not become an independent engineering-process, plant, reactor, or infrastructure study. The robot is an execution substrate for chemistry-side experiments rather than the primary engineering object.
- Accepted action: close the `03 / 09` boundary as `03` only, and revise the note so it no longer remains in a “needs another full-text review before top-level decision” state.

### `ASD-0664` Autonomous computational catalysis through an agentic research system

- Agent evidence: the arXiv full text shows CatMaster decomposing natural-language catalysis requests into multi-step milestone tasks with evidence packages, persistent project records, deferred resolution, remote/HPC execution, and iterative critique.
- `03` evidence: the paper's main axis remains computational heterogeneous catalysis, including O2 spin-state checking, CO adsorption site ranking on Fe surfaces, HER descriptor screening, surrogate-to-DFT validation, and CO@FeN4/graphene catalyst modeling.
- `04` evidence: the same full text also reports independent materials-side objects and results: BCC Fe surface energies, Pt-Ni-Cu alloy candidate/slab screening, Materials Project retrieval, BCC Fe equation-of-state fitting with bulk modulus extraction, and procedural FeN4/graphene single-atom-catalyst structural construction.
- Why `01.04` is not accepted: the paper is not a domain-general scientific-agent runtime validated only at workflow level. It repeatedly performs recognizable object-level materials and catalysis computations with concrete outputs.
- Accepted action: close the `03 / 04 / 01.04` boundary as `03;04`, while keeping `03` as `primary_module_for_filing` because the title, framing, and dominant workflow remain catalysis-first.

## Count update

Post-P1-L relaxed overlay counts add one `03` assignment from `ASD-0539` and one `04` assignment from `ASD-0664` relative to the post-P1-K state:

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
| `11` | 34 |

| Metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 559 |
| Independent `01.04` general-method bucket count | 20 |

## Remaining uncertainty

- `ASD-0539` would still benefit from a locally saved full text for richer note extraction, but the official JMI page is already explicit enough for the narrow `03 / 04` boundary.
- `ASD-0609` still has a source-depth gap on page-level extraction in the local note, but the present first-hand evidence is already sufficient to reject `09`.
- `ASD-0664` is no longer a live `01.04` question; the remaining follow-up value is mainly richer page-level extraction for future comparative synthesis with nearby catalysis/materials agent papers.
