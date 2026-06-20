# Relaxed multi-module reclassification round 2 / P0-C

> Date: 2026-06-20  
> Scope: P0 `01.04` / general-agent boundary follow-up for `ASD-0553`, `ASD-0660`, and `ASD-0662`.  
> Rule: local Notes were used only as leads; accepted decisions below rely on first-hand PDF / DOI / arXiv evidence.

## 1. 本轮结论

本轮完成 3 条 P0 记录复核：

| ID | Decision | Accepted modules / bucket | First-hand sources checked | Note action |
|---|---|---|---|---|
| `ASD-0553` | source-limited, still open | keep provisional independent `01.04`; no accepted migration yet | DOI / bioRxiv DOI path and metadata mirrors; full text/PDF blocked | note revised with source-limited warning |
| `ASD-0660` | closed | `03;04;06;07`, `general_method_bucket=none` | arXiv PDF `2602.01550` | note revised |
| `ASD-0662` | closed | `03;05;06;11`, `general_method_bucket=none` | arXiv PDF `2603.28986` | note revised |

## 2. 逐条证据

### `ASD-0553` ToolsGenie 2.0

- Current action: do not migrate yet.
- Evidence checked: DOI / bioRxiv landing path and metadata mirrors. The bioRxiv full text/PDF was not accessible during this run.
- Reason: abstract-level evidence points to bioinformatics automation, an in-house dataset, BixBench, and research / clinical contexts. This makes `06` and possibly `07` plausible, but the round-2 queue explicitly requires full-text task inventory before accepting a high-confidence migration.
- Result: remains open in the P0 queue as `source_limited`.

### `ASD-0660` S1-NexusAgent

- Accepted relaxed modules: `03;04;06;07`.
- Source: arXiv PDF.
- Evidence:
  - Biomni-Eval / Biomni-Eval1 and GWAS variant prioritization support life-science / genetics coverage (`06`).
  - Rare-disease diagnosis examples and drug-development / virtual-screening pressure support biomedical / health coverage (`07`).
  - ChemBench molecular-property / cheminformatics tasks support chemistry coverage (`03`).
  - MatSciBench materials-science categories and electrochemical-cell examples support materials coverage (`04`).
- Result: independent `01.04` only treatment is no longer supported.

### `ASD-0662` Mimosa Framework

- Accepted relaxed modules: `03;05;06;11`.
- Source: arXiv PDF.
- Evidence:
  - The paper evaluates all 102 ScienceAgentBench tasks.
  - The benchmark is described as data-driven discovery tasks from 44 peer-reviewed publications across bioinformatics, computational chemistry, geographic information science, and psychology / cognitive neuroscience.
  - These map to `06`, `03`, `05`, and `11` respectively under the relaxed benchmark-object rule.
- Result: independent `01.04` only treatment is no longer supported, although legacy filing remains unchanged until schema migration.

## 3. Count update

Post-P0-C relaxed overlay:

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 52 |
| `02` | 34 |
| `03` | 77 |
| `04` | 106 |
| `05` | 35 |
| `06` | 69 |
| `07` | 66 |
| `08` | 3 |
| `09` | 36 |
| `10` | 24 |
| `11` | 32 |

| Metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 534 |
| Independent `01.04` general-method bucket count | 24 |

## 4. Remaining uncertainty

`ASD-0553` remains the only unresolved item in this P0-C slice. It should be revisited when the full paper or an authoritative task inventory is accessible. The taxonomy itself did not show instability in this slice; the main issue was stale `01.04` treatment caused by platform-first legacy notes.
