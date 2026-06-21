# Liu et al. 2024 - AIGS: Generating Science from AI-Powered Automated Falsification

**Paper Info**
- paper_id: `ASD-0146`
- Title: `AIGS: Generating Science from AI-Powered Automated Falsification`
- Authors: `Liu et al.`
- Year: `2024`
- Venue: `arXiv`
- URL: `https://arxiv.org/abs/2411.11910`
- PDF: `https://arxiv.org/pdf/2411.11910.pdf`
- Project page: `https://agent-force.github.io/AIGS/`
- First-hand sources checked: `arXiv abstract`; `arXiv PDF`; `official project page`
- PDF status: `arXiv PDF checked; local archive path = Reference_PDF/01_Formal_Information_and_Computational_Sciences/Liu_2024_AIGS.pdf`
- Classification evidence source level: `first_hand_full_text`
- source_limited: `no`
- Current note status: `reaudit writeback refreshed on 2026-06-22`
- Note location statement: this file is stored under module `01` for filing convenience only; note path is not classification authority.

## Evidence Log

| Judgment item | Conclusion | First-hand basis | Reaudit landing |
|---|---|---|---|
| Agent inclusion | yes | The abstract describes `Baby-AIGS` as a full-process multi-agent research system with role-specific agents and explicit falsification. | Keep as an included Agent paper. |
| Scientific object | `01` | The PDF reports experiments on computational research tasks including data engineering, self-instruct alignment, and language modeling. | Supported module is `01`, not `01.04`. |
| Validation | benchmark + human review | The paper compares against strong baselines and discusses falsification logs and generated discoveries. | This is concrete task-level validation. |
| Boundary | not `01.04` | The system is framework-heavy, but it is not object-free because it validates on explicit computational research objects. | Retire stale `01.04` wording. |

## 0. Abstract Overview

The paper studies `AI-Generated Science` and argues that falsification is central to both scientific reasoning and the design of an autonomous research system. It proposes `Baby-AIGS`, a multi-agent workflow with roles for proposal, execution, review, and falsification. Although the framing is broad and method-oriented, the empirical studies are grounded in concrete computational research tasks rather than being purely domain-agnostic demonstrations. Under the current relaxed multi-module rule, that makes the note better anchored in module `01` than in the general-method bucket.

## 1. Inclusion in This Review

### 1.1 Agent decision

- Included as an Agent paper: `yes`
- Scientific goal: full-process autonomous research / discovery
- Multi-step action: yes
- Agent capability evidence: planning, tool use, execution, review, falsification, feedback iteration
- Workflow role tags: `scientific_question_formulation`; `hypothesis_generation`; `experimental_design`; `tool_use_and_code_execution`; `experiment_execution`; `data_analysis`; `result_interpretation`; `evidence_assessment_and_validation`; `end_to_end_research_automation`
- Inclusion confidence: `high`

### 1.2 Exclusion-risk check

- Not a single-model prediction paper
- Not a one-shot LLM ideation paper
- Not merely a benchmark shell around a frozen model
- Not object-free under current project rules because the validation tasks are explicit computational research objects

## 2. Scientific-Domain Classification

### 2.1 Final adjudicated fields

- supported_modules: `01`
- final_01_04_bucket: `none`
- primary_module_for_filing: `01`
- confidence: `high`

### 2.2 Classification rationale

The current writeback decision keeps the framework conclusion but updates the object classification. The old note treated AIGS as a general method and placed it in `01.04`. Under the current rule, that is too conservative because the paper directly validates on computational research tasks in data engineering, alignment, and language modeling. Those tasks are concrete computational objects and therefore support module `01`.

### 2.3 Boundary note

- Why not `01.04`: the paper is not object-free; it contains direct task-level coverage in formal/information/computational science.
- Why still not multi-module: the concrete experimental coverage stays within computational research tasks rather than extending into another scientific-object module.
- Why note location remains secondary: the note is filed under `01`, but the filing path is not the authority; the object evidence is.

## 3. Agent System and Research Workflow Role

### 3.1 Agent type tags

- `LLM Agent`
- `Planning Agent`
- `Tool-using Agent`
- `Multi-Agent System`
- `Hybrid Agent`

### 3.2 Research workflow roles

- `scientific_question_formulation`
- `hypothesis_generation`
- `experimental_design`
- `tool_use_and_code_execution`
- `experiment_execution`
- `data_analysis`
- `result_interpretation`
- `evidence_assessment_and_validation`
- `end_to_end_research_automation`

### 3.3 Autonomy profile

- task decomposition: present
- planning: present
- tool use: present
- state / memory handling: present in workflow state and logs
- feedback iteration: present
- autonomous decision making: present
- multi-agent collaboration: present
- environment interaction: present

## 4. Method and Workflow

### 4.1 Method motivation

The paper tries to move from AI assistance toward fuller AI-generated science. Its key conceptual move is to argue that scientific progress is not just about proposing ideas; it also requires explicit falsification, which prior systems often omitted or outsourced to narrow verification engines.

### 4.2 Workflow sketch

1. Generate research ideas and candidate methods.
2. Translate them into executable workflows or experiments.
3. Run experiments or code-based evaluation.
4. Review and summarize intermediate results.
5. Apply explicit falsification or ablation-like checks.
6. Produce refined research conclusions or discoveries.

### 4.3 System emphasis

The important point for this reaudit is that the paper is not only a philosophical argument about AIGS. It uses a concrete multi-agent workflow and validates it on explicit computational research tasks, which is the basis for the module-`01` landing.

## 5. Experiment and Validation

### 5.1 Validation form

- benchmark evaluation: yes
- human evaluation: yes
- simulation / code execution environment: yes
- wet-lab or robotics: no

### 5.2 Task and evidence

The PDF describes experiments on computational tasks including data engineering, self-instruct alignment, and language modeling. These are the decisive object-level anchors for the present classification decision. The paper also reports comparison against systems such as `The AI Scientist` and discusses the strengths and weaknesses of the falsification-centered workflow.

### 5.3 Contribution strength

- scientific contribution type: `hypothesis`; `system_platform`
- evidence strength: first-hand full text with benchmark and human review
- ASD relevance: high, because the paper assigns agents explicit roles across the research workflow

## 6. Limitations and Risks

- The system remains an early prototype relative to experienced human researchers.
- The task set is computational and relatively narrow compared with broader cross-domain scientific discovery.
- The framework language can invite over-classification into `01.04`, so the note should preserve the explicit rationale for staying in `01`.

## 7. Review Value

- Useful as a computational-science example of full-process multi-agent research design.
- Useful for discussing falsification as an explicit Agent role.
- Important as a boundary case showing when a framework-heavy paper still belongs in a concrete scientific-object module rather than `01.04`.

## 8. Summary

### 8.1 One-sentence summary

A falsification-centered multi-agent autonomous research system whose concrete validations land it in module `01` rather than the general-method bucket.

### 8.2 Reaudit summary

- Kept the updated classification conclusion: `01`
- Kept `final_01_04_bucket: none`
- Kept `source_limited: no`
- Restored a fuller structured note while preserving the corrected evidence and boundary wording

