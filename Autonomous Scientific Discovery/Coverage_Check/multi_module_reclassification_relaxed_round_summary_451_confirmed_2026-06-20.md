# 451 confirmed relaxed multi-module reclassification round summary

> Date: 2026-06-20  
> Scope: 451 confirmed core records in `Paper_Lists/agent_master_paper_list.md`.  
> Source files: Batch 1-4 / Wave A-B relaxed reclassification reports under `Coverage_Check/`.  
> Policy: classify by concrete scientific-object experiment / validation / benchmark task / case-study / reported-result coverage. Legacy Notes and legacy filing columns are evidence leads, not final authority.

## 1. Current Round Status

This relaxed round has completed all four planned batches and eight planned waves:

| Batch | Waves completed | Confirmed-record span |
|---|---:|---|
| Batch 1 | A / B | `ASD-0001`-`ASD-0154` |
| Batch 2 | A / B | `ASD-0155`-`ASD-0600` |
| Batch 3 | A / B | `ASD-0601`-`ASD-0739` |
| Batch 4 | A / B | `ASD-0740`-`ASD-0871` |

Current canonical master-list status remains:

| Metric | Count |
|---|---:|
| `candidate` | 0 |
| `to_read` | 451 |
| `background_only` | 370 |
| `excluded` | 50 |
| `needs_review` | 0 |
| legacy confirmed included-and-classified count | 451 |

This round did not expand the corpus. It only audited the 451 confirmed records under the relaxed multi-module object-coverage rule.

## 2. Current Relaxed Overlay Counts

The current audited overlay through Batch 4 / Wave B is:

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 47 |
| `02` | 33 |
| `03` | 73 |
| `04` | 103 |
| `05` | 34 |
| `06` | 66 |
| `07` | 64 |
| `08` | 3 |
| `09` | 35 |
| `10` | 23 |
| `11` | 31 |

| Relaxed-counting metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 512 |
| Independent `01.04` general-method bucket count after accepted migrations | 32 |

Interpretation: the record-level confirmed count remains 451, but the expanded module-assignment count is now 512 because high-confidence multi-module object coverage is recorded without forcing single-module simplification.

## 3. Landed High-Confidence Changes

The master list currently contains 46 `RelaxedMultiModule2026-06-20` landed markers:

`ASD-0254`, `ASD-0385`, `ASD-0447`, `ASD-0510`, `ASD-0522`, `ASD-0523`, `ASD-0525`, `ASD-0531`, `ASD-0537`, `ASD-0540`, `ASD-0545`, `ASD-0548`, `ASD-0554`, `ASD-0564`, `ASD-0663`, `ASD-0669`, `ASD-0673`, `ASD-0693`, `ASD-0696`, `ASD-0697`, `ASD-0702`, `ASD-0703`, `ASD-0709`, `ASD-0710`, `ASD-0711`, `ASD-0719`, `ASD-0721`, `ASD-0722`, `ASD-0731`, `ASD-0736`, `ASD-0737`, `ASD-0739`, `ASD-0740`, `ASD-0742`, `ASD-0745`, `ASD-0782`, `ASD-0787`, `ASD-0790`, `ASD-0792`, `ASD-0811`, `ASD-0820`, `ASD-0844`, `ASD-0866`, `ASD-0868`, `ASD-0870`, `ASD-0871`.

These records should be treated as accepted relaxed-overlay decisions, while their legacy `Main class` / `Secondary class` fields remain unchanged until schema migration.

## 4. Main Cleanup Themes

The strongest landed theme is the shrinking of pure independent `01.04`: platform-like or general scientific-agent papers left `01.04` when first-hand evidence showed concrete scientific-object case studies, benchmark tasks, or reported results.

The second theme is stable cross-boundary expansion rather than primary-class replacement. Typical examples include `03;04` chemistry/materials catalyst or emitter records, `06;07` life-science/medical records, `05;10` mission-science records, and `01;11` formal-computational research plus scientific knowledge-production records.

The third theme is that benchmark evidence can support object modules only when the benchmark tasks are recognizably domain-object tasks. Pure abstract capability benchmarks still remain in independent `01.04` or in follow-up until first-hand task inventory is checked.

## 5. Taxonomy Stability Judgment

The `01-11` top-level taxonomy remains usable. The relaxed audit did not reveal a need to add a new top-level module.

The remaining instability is operational rather than structural:

- the master list still lacks row-level structured fields for `scientific_object_modules`, `general_method_bucket`, `object_coverage_mode`, and `primary_module_for_filing`;
- some `01.04` records need full-text task inventory before migration;
- benchmark-object evidence needs careful source checking so abstract symbolic-regression or general research-agent capability tests are not over-expanded;
- `03/04`, `06/07`, `05/10`, and `11.07/01.04` remain the main boundary zones.

## 6. Required Next Step

Use `multi_module_reclassification_relaxed_round2_fulltext_boundary_queue_2026-06-20.md` as the next control file. The next pass should prioritize full-text / first-hand evidence for unresolved medium-confidence records, then update master-list remarks and corresponding Notes only for high-confidence resolved cases.

Do not continue broad expansion until this queue is reduced enough that the relaxed overlay is stable for schema migration.
