# Yang et al. 2024 - Large language models for automated open-domain scientific hypotheses discovery

**Paper Info**
- paper_id: `ASD-0140`
- Title: `Large language models for automated open-domain scientific hypotheses discovery`
- Authors: `Yang et al.`
- Year: `2024`
- Venue: `Findings of ACL 2024`
- URL: `https://aclanthology.org/2024.findings-acl.804/`
- First-hand source checked: `ACL PDF`
- PDF status: `publisher PDF checked; local archive path = Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Yang_2024_Open_Domain_Hypotheses_Discovery.pdf`
- Classification evidence source level: `first_hand_full_text`
- source_limited: `no`
- Current note status: `reaudit writeback refreshed on 2026-06-22`
- Note location statement: this file is stored under module `11` for filing convenience only; note path is not classification authority.

## Evidence Log

| Judgment item | Conclusion | First-hand basis | Reaudit landing |
|---|---|---|---|
| Agent inclusion | yes | The ACL paper presents a multi-module workflow that retrieves observations from raw web corpora, proposes hypotheses, and uses feedback mechanisms to improve generation quality. | Keep as an included Agent paper. |
| Scientific object | `11` | The abstract explicitly frames the task as `social science academic hypotheses discovery` rather than a generic research-agent benchmark. | Supported module is `11`. |
| Validation | direct task validation | The paper reports both GPT-4-based and expert-based evaluation for validity, novelty, and usefulness of generated hypotheses. | This is object-level validation, not a pure methods-only showcase. |
| Boundary | not `11.07`; not `01.04` | The system is not primarily studying science-of-science objects such as peer review, citation structure, or knowledge-production systems themselves. | Remove stale `11.07` wording. |

## 0. Abstract Overview

This paper studies automated hypothesis generation in an open-domain social-science setting. Instead of using tightly curated observation sentences or commonsense-only targets, it builds a setting in which the system must work from raw web-scale observations and generate hypotheses that are intended to be scientifically useful, potentially novel, and socially grounded. The paper therefore reads as a social-science hypothesis-discovery study implemented with an LLM-centered Agent workflow, rather than as a generic research-agent framework detached from a concrete scientific object.

## 1. Inclusion in This Review

### 1.1 Agent decision

- Included as an Agent paper: `yes`
- Scientific goal: explicit social-science hypothesis discovery
- Multi-step action: yes
- Agent capability evidence: retrieval, iterative generation, feedback-driven refinement, evaluation
- Workflow role tags: `hypothesis_generation`; `literature_search_and_reading`; `evidence_assessment_and_validation`
- Inclusion confidence: `high`

### 1.2 Exclusion-risk check

- Not merely a one-shot LLM generation paper
- Not only a benchmark wrapper with no workflow
- Not only a general `AI for Science` narrative
- Not a pure science-of-science paper despite surface overlap with knowledge-generation language

## 2. Scientific-Domain Classification

### 2.1 Final adjudicated fields

- supported_modules: `11`
- final_01_04_bucket: `none`
- primary_module_for_filing: `11`
- confidence: `high`

### 2.2 Classification rationale

The decisive object is social-science hypothesis generation. The paper introduces a dataset and workflow for discovering social-science academic hypotheses from raw evidence sources, so the note should stay in module `11`. The older `11.07` wording overstated the extent to which the paper studies scientific knowledge production itself. It is closer to social-science research support than to science-of-science analytics.

### 2.3 Boundary note

- Why not `11.07`: the target is not citation networks, scientific institutions, peer review, or research-policy systems as objects of study.
- Why not `01.04`: the paper is not object-free; it validates on a concrete social-science hypothesis-discovery task.
- Why note location still matters less than classification: the note remains filed in the `11` folder, but the note path is only a filing convenience.

## 3. Agent System and Research Workflow Role

### 3.1 Agent type tags

- `LLM Agent`
- `Tool-using Agent`

### 3.2 Research workflow roles

- `hypothesis_generation`
- `literature_search_and_reading`
- `evidence_assessment_and_validation`

### 3.3 Autonomy profile

- planning: present in workflow organization
- tool use / retrieval: present
- feedback iteration: present
- autonomous decision making: partial to moderate
- multi-agent collaboration: not the main emphasis, but modular staged workflow is explicit

## 4. Method and Workflow

### 4.1 Method motivation

The paper argues that previous hypothesis-discovery settings were too constrained: observations were preselected and the target hypotheses were often too close to commonsense knowledge. The proposed system instead uses raw evidence and aims at more realistic social-science hypothesis generation.

### 4.2 Workflow sketch

1. Gather observations from open-domain raw web corpora.
2. Organize or filter candidate evidence relevant to the target topic.
3. Generate social-science hypotheses from the evidence.
4. Apply feedback mechanisms to improve validity, novelty, and usefulness.
5. Rank or evaluate generated hypotheses for downstream researcher use.

### 4.3 System emphasis

The key contribution is not a robotic experimental loop but an evidence-to-hypothesis workflow for a social-science object. The system is closer to an Agent-based social-science reasoning and discovery assistant than to a general-purpose ASD framework.

## 5. Experiment and Validation

### 5.1 Validation form

- automated evaluation: yes
- expert evaluation: yes
- benchmark-style tasking: yes
- real physical experiment: no

### 5.2 Task and evidence

The paper validates whether the system can generate social-science hypotheses that are valid, useful, and novel relative to prior baselines. The reported evidence is tied to hypothesis quality in the social-science discovery setting rather than to a domain-agnostic research-agent capability score.

### 5.3 Contribution strength

- scientific contribution type: `hypothesis`; `system_platform`
- evidence strength: first-hand full text with direct task validation
- ASD relevance: strong enough for inclusion because the Agent is assigned a concrete scientific role in hypothesis generation

## 6. Limitations and Risks

- The evidence is stronger for hypothesis-generation quality than for downstream real-world scientific impact.
- The paper remains computationally evaluated rather than validated through long-cycle social-science research adoption.
- Some wording in the paper can sound like knowledge-production or meta-science language, so the `11` vs `11.07` boundary needs to stay explicit in the note.

## 7. Review Value

- Useful as a module-`11` example where the target object is social science rather than natural science.
- Helpful for distinguishing social-science hypothesis discovery from `11.07` science-of-science work.
- Useful in the review when discussing Agent support for literature-grounded hypothesis generation without a wet-lab loop.

## 8. Summary

### 8.1 One-sentence summary

An LLM-centered Agent workflow for generating and evaluating social-science hypotheses from open-domain evidence, best classified under module `11` rather than `11.07`.

### 8.2 Reaudit summary

- Kept the updated classification conclusion: `11`
- Kept `final_01_04_bucket: none`
- Kept `source_limited: no`
- Preserved the note as a fuller structured project note instead of a short-form writeback summary

