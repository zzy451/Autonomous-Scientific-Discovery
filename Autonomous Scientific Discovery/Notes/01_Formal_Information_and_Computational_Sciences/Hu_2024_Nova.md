# Hu et al. 2024 - Nova: An iterative planning and search approach to enhance novelty and diversity of LLM-generated ideas

**Paper Info**
- paper_id: `ASD-0147`
- Title: `Nova: An iterative planning and search approach to enhance novelty and diversity of LLM-generated ideas`
- Authors: `Hu et al.`
- Year: `2024`
- Venue: `arXiv`
- URL: `https://arxiv.org/abs/2410.14255`
- PDF: `https://arxiv.org/pdf/2410.14255.pdf`
- First-hand source checked: `arXiv PDF`
- PDF status: `arXiv PDF checked; local archive path = Reference_PDF/01_Formal_Information_and_Computational_Sciences/Hu_2024_Nova.pdf`
- Classification evidence source level: `first_hand_full_text`
- source_limited: `no`
- Current note status: `reaudit writeback refreshed on 2026-06-22`
- Note location statement: this file is stored under module `01` for filing convenience only; note path is not classification authority.

## Evidence Log

| Judgment item | Conclusion | First-hand basis | Reaudit landing |
|---|---|---|---|
| Agent inclusion | yes | The paper presents an iterative planning-and-search workflow that intentionally retrieves external knowledge and uses it to refine idea generation. | Keep as an included Agent paper. |
| Scientific object | `01` | The PDF validates the system on research-idea generation over a concrete computational paper corpus and reports evaluation on `170 seed papers`. | Supported module is `01`, not `01.04`. |
| Validation | direct corpus-based evaluation | The paper reports automated and human assessment, including novelty/diversity gains and Swiss Tournament ranking outcomes. | This is concrete computational research-object validation. |
| Boundary | not `01.04` | The method is general enough in appearance to look like a broad idea-agent, but the experiments are anchored in a concrete computational research setting. | Retire stale `01.04` wording. |

## 0. Abstract Overview

Nova is an LLM-based idea-generation system that tries to improve novelty and diversity through iterative planning and knowledge search. The core point for the reaudit is that the paper does not merely propose a generic ideation strategy; it validates that strategy on a concrete computational research-paper corpus and compares idea quality under explicit evaluation protocols. Under the current project rules, that moves the note from a conservative `01.04` position into module `01`.

## 1. Inclusion in This Review

### 1.1 Agent decision

- Included as an Agent paper: `yes`
- Scientific goal: automated generation of high-quality research ideas
- Multi-step action: yes
- Agent capability evidence: iterative planning, retrieval-guided search, refinement
- Workflow role tags: `hypothesis_generation`; `planning`; `literature_search_and_reading`
- Inclusion confidence: `high`

### 1.2 Exclusion-risk check

- Not a one-shot text-generation paper
- Not only a prompt-engineering variant with no workflow
- Not object-free under current policy because the evaluation corpus is concrete and computational

## 2. Scientific-Domain Classification

### 2.1 Final adjudicated fields

- supported_modules: `01`
- final_01_04_bucket: `none`
- primary_module_for_filing: `01`
- confidence: `high`

### 2.2 Classification rationale

The older note used `01.04` because the paper looked like a general scientific-idea generation method. The updated conclusion keeps the method description but changes the classification authority: the experiments are run on a concrete computational research corpus, and the paper measures idea quality within that domain context. That is enough object-level coverage for module `01`.

### 2.3 Boundary note

- Why not `01.04`: the paper is not object-free under the project's current rule.
- Why `01` fits: the work is validated as computational research ideation over a concrete paper set.
- Why note location remains secondary: the note stays in the `01` folder, but the classification claim is justified by object evidence rather than by filing path.

## 3. Agent System and Research Workflow Role

### 3.1 Agent type tags

- `LLM Agent`
- `Planning Agent`

### 3.2 Research workflow roles

- `hypothesis_generation`
- `planning`
- `literature_search_and_reading`

### 3.3 Autonomy profile

- planning: central
- retrieval / external knowledge use: central
- feedback iteration: central
- autonomous decision making: moderate
- multi-agent structure: not the main emphasis here

## 4. Method and Workflow

### 4.1 Method motivation

The paper starts from the observation that plain LLM idea generation often produces repetitive or shallow suggestions. Its answer is to add explicit planning and external-knowledge search so that the system can progressively enrich idea proposals and escape local novelty traps.

### 4.2 Workflow sketch

1. Start from seed research papers or a target research topic.
2. Plan what external knowledge should be retrieved.
3. Retrieve and integrate broader evidence.
4. Generate candidate research ideas.
5. Iterate the planning-and-search loop to improve novelty and diversity.
6. Rank or compare generated ideas through automated and human evaluation.

### 4.3 System emphasis

The important classification point is that this is not merely an abstract planning method. It is a planning-and-search Agent applied to a concrete computational research ideation setting.

## 5. Experiment and Validation

### 5.1 Validation form

- automated evaluation: yes
- human evaluation: yes
- comparative tournament-style evaluation: yes
- physical experiment: no

### 5.2 Task and evidence

The paper evaluates the system over `170 seed papers` and reports improvement in novelty, diversity, and counts of top-rated ideas. The PDF states that Nova produces `3.4x` more unique novel ideas than the baseline and at least `2.5x` more top-rated ideas in Swiss Tournament evaluation.

### 5.3 Contribution strength

- scientific contribution type: `hypothesis`
- evidence strength: first-hand full text with concrete corpus-based evaluation
- ASD relevance: sufficient for inclusion because the Agent plays an explicit multi-step role in scientific ideation

## 6. Limitations and Risks

- Validation is still computational and evaluation-centric rather than downstream laboratory or field impact.
- The paper is easy to over-generalize into `01.04` if one focuses only on the method narrative.
- The note should therefore preserve the explicit reason why a corpus-grounded computational ideation study still belongs in module `01`.

## 7. Review Value

- Useful for the review section on computational-science ideation agents.
- Useful as a boundary case between general research-agent methods and object-supported computational ideation work.
- Helpful when discussing planning-and-search as a mechanism for improving Agent novelty rather than just model scale.

## 8. Summary

### 8.1 One-sentence summary

An iterative planning-and-search Agent for computational research idea generation that is better classified in module `01` than in the general-method bucket because of its concrete corpus-grounded validation.

### 8.2 Reaudit summary

- Kept the updated classification conclusion: `01`
- Kept `final_01_04_bucket: none`
- Kept `source_limited: no`
- Restored a fuller structured note while preserving the corrected evidence and boundary wording

