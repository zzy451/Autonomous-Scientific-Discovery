# 500-Record Literature Pool Classification Pressure Report

Date: 2026-06-16

## Purpose

This report summarizes the expanded 500-record literature pool used to test whether the current `01-11` science-domain taxonomy can absorb a much larger Scientific Agent / Autonomous Scientific Discovery literature set.

Important: this is a broad collection pool. It is not a 500-paper confirmed core set. Records retain status labels (`candidate`, `to_read`, `background_only`, `excluded`) so later strict review can promote, downgrade, or remove items from core analysis.

## Overall Counts

- Total records: 500
- Status counts: {'to_read': 77, 'background_only': 296, 'excluded': 25, 'candidate': 102}
- Main-class counts: {'01': 175, '02': 25, '03': 100, '04': 67, '05': 6, '06': 70, '07': 26, '09': 15, '10': 3, '11': 4}

## Expansion Since `ASD-0111`

- Newly added expansion records: 390
- Expansion status counts: {'candidate': 102, 'background_only': 274, 'excluded': 14}
- Expansion class counts: {'01': 151, '02': 22, '03': 76, '04': 50, '05': 6, '06': 56, '07': 12, '09': 11, '10': 2, '11': 4}

## Candidate Distribution

- Candidate records by class: {'01': 20, '02': 6, '03': 29, '04': 22, '06': 12, '07': 8, '09': 5}
- Background-only records by class: {'01': 128, '02': 15, '03': 51, '04': 28, '05': 6, '06': 45, '07': 7, '09': 7, '10': 3, '11': 4}

## Light Cleanup Applied

- Duplicate records were kept as rows but marked `excluded` when a canonical record already exists.
- Review/perspective-style self-driving laboratory papers were downgraded to `background_only`.
- A small number of obvious metadata/classification slips were corrected, including protein fitness landscape (`06`) and generic computer-vision background (`01`).

## Classification Stress Points

1. `01.04` remains necessary for domain-free scientific Agents, benchmarks, automated research systems, and general scientific idea-generation systems.
2. `03` and `04` are heavily populated and remain the most important boundary pair: molecular design, OSDAs, reaction optimization, MOFs, metamaterials, and materials characterization often sit near this border.
3. `06` and `07` need strict object-first rules for biomedical systems: omics/cell/protein mechanism should stay in `06`, while disease, therapeutic, clinical, or drug-discovery objects move to `07`.
4. `05`, `08`, `10`, and `11` remain low-coverage or weakly verified. This does not yet prove taxonomy failure; it likely reflects the literature-search routes and current Agent adoption patterns.
5. Many high-impact self-driving laboratory papers are not LLM-Agent papers but do show classic autonomous/closed-loop Agent behavior, which supports keeping the review scope broader than LLM-based agents.

## Low-Coverage Classes

- Classes with fewer than 5 records: `08` (0), `10` (3), `11` (4)

## Recommended Next Pass

1. Run a strict review of all `candidate` records added in `ASD-0111` onward.
2. Keep high-value `background_only` records for citation expansion, but exclude them from core statistics.
3. Deliberately search for Agent papers in `05` Earth/environment, `08` agriculture/food, `10` aerospace/traffic, and `11` social/knowledge-system classes.
4. Only after strict review should promoted records receive full paper notes.
