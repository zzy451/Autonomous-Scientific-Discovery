# Per-paper classification audit task

You are performing an independent classification audit of one confirmed-core paper in the Autonomous Scientific Discovery library. This is a read-only audit. Do not edit, create, or delete project files. Return exactly one JSON object conforming to the supplied JSON Schema.

## Evidence standard

1. Classify from the paper's concrete scientific objects and reported experiments, validations, benchmark tasks, case studies, or results. Do not classify from the venue, authors, Agent architecture, title keywords alone, or the paper's broad claims.
2. The complete extracted PDF text, when supplied, is the primary source. A project note is secondary context and may itself contain an earlier classification. Ignore every class code, class label, or classification recommendation in notes; derive the result independently from quoted object and result evidence. Never claim to have read a PDF when its text is not supplied.
3. For each supported module, give a distinct object/result evidence row with a short verbatim quote and a page/section/table/figure locator when available. A broad statement that the system is “for science” is not enough.
4. Include every supported scientific-object module among `01`-`11`, including secondary objects with their own reported experiment, validation, benchmark task, case study, or result. Do not add a module just because a tool, model, dataset, or application is mentioned.
5. Use `01.04` only as the separate general-method bucket when no concrete scientific-object evidence supports any `01`-`11` module. Do not put `01.04` in `modules`.
6. Assign the deepest active secondary and tertiary codes supported by the evidence and controlled codebook. A null code is required when the taxonomy has no applicable active term or evidence cannot distinguish codes; explain that in `taxonomy_gap_reason` or `human_review_reasons`. Never invent or promote a legacy `needs_review` term to an active code. Modules `06` and `07` require a tertiary code for a definitive assignment; when evidence is inadequate, keep the proposed module but mark low confidence and require human review.
7. Multi-disciplinary classification is evidence-based. The same paper can have multiple module rows, each backed by its own object and reported result. Keep secondary/tertiary values within the corresponding module.
8. Be conservative. A source-limited note or metadata-only review must be marked for human review. State exactly what source was available and what would resolve the uncertainty.

## Project boundary rules to apply

- Assign by the direct scientific object and its reported result, not by the Agent or computational method. Mentioned tools, datasets, and downstream applications alone do not create extra modules.
- `03` covers molecules, reactions, synthesis, catalysis, and chemical processes. `04` covers material composition, structure, phase, morphology, properties, and material characterization. If the evaluated object is a material rather than a reaction route, prefer `04`.
- `05` covers natural Earth, climate, water, and environmental processes; `10` covers aerospace, marine equipment/engineering, and transportation systems. Planetary astrophysics belongs to `02`; planetary environment/geology can belong to `05`.
- `06` covers biological mechanisms and organisms; `07` covers disease, diagnosis, treatment, clinical data, health systems, and translational drug/medical-device work. A biomedical dataset does not by itself establish `07`; a concrete disease or health task must be reported.
- `08` is for agricultural, food, forestry, animal, fishery, and production-oriented objects. `09` is for engineering systems, devices, instruments, processes, manufacturing, and infrastructure. `11.07` is only for science systems, scientific knowledge production, research communities, science policy/history/philosophy/methodology; it is not a general cross-disciplinary bucket.
- `01` is for formal, information, computational, mathematical, AI/system objects themselves. Using code, ML, or an LLM to study another discipline does not make the paper `01`.
- `01.04` is allowed only when no concrete `01`-`11` object has a reported experiment, validation, benchmark task, case study, or result.

## Supplied context

The input includes project scope and boundary rules, the active controlled taxonomy terms, paper identity, evidence-source status, and either extracted PDF text or note text. It intentionally omits the current classification assignments so your judgment is not anchored to them. The script will compare your returned result with current owner data afterward.

## Output interpretation

- `classification_bucket` is `01.04` only for the separate general-method bucket; otherwise it is null.
- `modules` contains one row per supported primary module. Use labels and active secondary/tertiary codes exactly as supplied.
- `object_evidence` describes the concrete object, action/result, verbatim short quote, source location, and evidence basis for that module.
- `source_limitations` must identify missing, incomplete, or indirectly summarized evidence.
- Set `needs_human_review` for material uncertainty, missing full text, conflicts, or source limitations. Do not treat a legacy note as independent verification.
