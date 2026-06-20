# 第3轮全库分类复核报告：`ASD-0401`–`ASD-0600`

生成日期：`2026-06-18`  
审计模式：全库分类复核，第 3 轮，`200` 篇一批，`4 x 50` 只读 reviewer，由主控代理统一裁决并维护主列表  
审计范围：`Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md` 中 `ASD-0401`–`ASD-0600`  
说明：本文件为第 3 轮收口版，已按当前权威主列表重新对齐；仅记录已经真实落地到主列表的改动，以及本轮只读 reviewer 交叉复核后仍需后续关注的边界样本。

## 1. 本轮开始前基线

- confirmed included + classified count：`479`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- 当前主要边界压力点：
  - `01.04 / 具体学科`
  - `03 / 04`
  - `06 / 07`
  - `11.07 / 01.04`
  - `05 / 10`
  - SDL infrastructure / facility assistant / orchestration interface 是否被过宽保留为 confirmed core

## 2. 本轮已落地主列表改动

### 2.1 从 confirmed core 降为 `background_only`

| ID | 题名 | 原状态 / 原主类 | 新状态 / 新主类 | 处理结论 | 理由 |
|---|---|---|---|---|---|
| ASD-0559 | Evaluating open LLMs for agentic analysis orchestration in a typical biomedical lab | `to_read / 06` | `background_only / 06` | 降级 | 当前证据更像 biomedical-lab analysis orchestration evaluation，重点是评测与编排能力，而不是稳定的主系统型 ASD 核心论文。 |
| ASD-0560 | Evaluating agentic AI for biological discovery in autonomous and copilot settings | `to_read / 06` | `background_only / 06` | 降级 | 当前证据偏向 autonomous / copilot setting 对比评测，尚不足以稳定保留为 confirmed core。 |
| ASD-0578 | VISION: a modular AI assistant for natural human-instrument interaction at scientific user facilities | `to_read / 01` | `background_only / 01` | 降级 | 更接近 scientific user facility 场景下的 instrument assistant / facility infrastructure，而不是主科研发现系统。 |
| ASD-0585 | IvoryOS: an interoperable web interface for orchestrating Python-based self-driving laboratories | `to_read / 01` | `background_only / 01` | 降级 | 主体是 SDL orchestration interface / infrastructure，应保留为背景而非 confirmed core。 |
| ASD-0594 | LabPilot: an agentic copilot for scientific instrument control | `to_read / 01` | `background_only / 01` | 降级 | 当前证据更像 instrument-control copilot / facility assistant，而不是稳定的 scientific-discovery Agent 核心样本。 |

### 2.2 已落地的二级类收口修正

| ID | 原二级类 | 新二级类 | 处理结论 | 理由 |
|---|---|---|---|---|
| ASD-0430 | `07.04` | `07.02` | 修正 | therapeutic biosensor review 更接近临床/治疗系统背景，不是药物发现论文。 |
| ASD-0433 | `02.01` | `02.02` | 修正 | synchrotron / neutron facilities 的对象是 physics instrumentation，而非 astronomy。 |
| ASD-0456 | `01.04` | `01.02` | 修正 | general autonomous-agent survey，不是 ASD-specific research-agent paper。 |
| ASD-0467 | `01.04` | `01.01` | 修正 | metaheuristic / optimization tutorial 更适合作为形式与优化方法背景。 |
| ASD-0494 | `01.04` | `01.02` | 修正 | generic deep-learning review，不应继续挂在 `01.04`。 |
| ASD-0497 | `01.04` | `01.02` | 修正 | never-ending language learning architecture 属于通用 AI / 计算背景。 |
| ASD-0498 | `01.04` | `01.02` | 修正 | AutoML book 属于通用计算方法背景，而不是 scientific-Agent 文献。 |
| ASD-0518 | `06.01` | `06.03` | 修正 | autonomous enzyme engineering 更接近 biotechnology / protein engineering。 |
| ASD-0521 | `06.01` | `06.03` | 修正 | gene-editing automation 更接近 biotechnology，而不是一般生物学。 |

## 3. 本轮重点复核但暂不改动

以下条目在四个只读 reviewer 的交叉复核中被再次点名，但本轮没有形成足够强的新证据，因此主列表暂不继续改动。

| ID | 题名 | 当前主类 | 暂不改动原因 | 是否建议后续复核 |
|---|---|---|---|---|
| ASD-0411 | Autonomy in materials research: a case study in carbon nanotube growth | `04` | 有“可能被保守留在 background”的压力，但仅凭当前元数据不足以上调。 | 是 |
| ASD-0414 | Accelerating materials discovery using artificial intelligence, high performance computing and robotics | `04` | 可能偏 broad perspective / review，但当前记录仍保留 concrete materials-discovery workflow 解释。 | 是 |
| ASD-0418 | Data-science driven autonomous process optimization | `03` | 可能偏 optimization / methodology，但目前仍可按 chemistry process optimization 保持。 | 是 |
| ASD-0429 | Toward autonomous additive manufacturing: Bayesian optimization on a 3D printer | `09` | 当前仍更像 engineering system object；但 reviewer 提醒其 core-strength 证据偏弱。 | 是 |
| ASD-0431 | Machine learning for automated experimentation in scanning transmission electron microscopy | `04` | 有被低估为 background_only 的可能，但现阶段 Agent 证据仍弱。 | 是 |
| ASD-0459 | Toward “On-Demand” Materials Synthesis and Scientific Discovery through Intelligent Robots | `04` | 可能是 under-kept background；但现有证据不足以上调为 confirmed core。 | 是 |
| ASD-0469 | Achieving Reproducibility and Closed-Loop Automation in Biological Experimentation with an IoT-Enabled Lab of the Future | `06` | 存在 infrastructure / reproducibility 压力，但仍可解释为 biological experimentation lineage anchor。 | 是 |
| ASD-0478 | NIMS-OS: an automation software to implement a closed loop between artificial intelligence and robotic experiments in materials science | `04` | orchestration/software-layer 压力明显，但当前主列表仍按 concrete materials closed loop 保持。 | 是 |
| ASD-0484 | Evolution-guided Bayesian optimization for constrained multi-objective optimization in self-driving labs | `04` | 可能偏 optimization method；但当前尚不足以从 materials core 中移出。 | 是 |
| ASD-0486 | ChatGPT Research Group for Optimizing the Crystallinity of MOFs and COFs | `04` | 有被保守留在 background 的可能，但 Agent 闭环证据仍不足。 | 是 |
| ASD-0511 | Operating advanced scientific instruments with AI agents that learn on the job | `04` | 存在 `04 / 01.04` 压力；当前仍按 materials/instrumentation object 暂留。 | 是 |
| ASD-0522 | Evaluating large language model agents for automation of atomic force microscopy | `04` | 存在 instrument-evaluation / `01.04` 压力，但仍可按 materials characterization 保持。 | 是 |
| ASD-0525 | TeLLAgent: a dual-agent framework for reliable scientific discovery with tool-enhanced LLMs | `03` | reviewer 提醒若 full text 中 chemistry object 不够实，应回看 `03 / 01.04`。当前先保持 `03`。 | 是 |
| ASD-0528 | AutoSciLab: A Self-Driving Laboratory for Interpretable Scientific Discovery | `01` | 这是较典型但仍偏 broad 的 `01.04` 样本；本轮没有足够证据将其移出 confirmed core。 | 是 |
| ASD-0541 | PromptBio: A Multi-Agent AI Platform for Bioinformatics Data Analysis | `06` | 有平台化 / 分析型压力，但当前仍可按 bioinformatics scientific object 保持。 | 是 |
| ASD-0543 | Machine Learning Copilot Agent: An LLM-Guided Workflow for Prognostic Gene Discovery | `06` | 存在 `06 / 07` 压力；当前证据仍更偏 gene-discovery 而非 patient / therapy。 | 是 |
| ASD-0553 | ToolsGenie 2.0: A Scalable and Extensible Multi-Agent System for Bioinformatics Automation | `06` | 有 `06 / 01.04` 平台化压力，但当前仍可按 bioinformatics object 暂留。 | 是 |
| ASD-0554 | BioAgent: An Auditable Multi-Agent Framework for Reproducible Translational Bioinformatics | `06` | 有 `06 / 01.04` 平台化压力，但当前仍未达到直接下调阈值。 | 是 |
| ASD-0561 | Toward Full Autonomous Laboratory Instrumentation Control with Large Language Models | `09` | 主类本身未见明显错误，但 confirmed core 强度仍有待后续回看。 | 是 |
| ASD-0572 | Autonomous discovery of functional random heteropolymer blends for protein stabilization using a robotic platform and Bayesian optimization | `06` | `06 / 04` 边界压力较强；当前仍按 protein-stabilization life-science object 保持。 | 是 |
| ASD-0581 | A chemical autonomous robotic platform for end-to-end synthesis of nanoparticles | `03` | `03 / 04` 边界尚未彻底消解；当前先按 synthesis object 保持 `03`。 | 是 |

## 4. 边界问题清单

### 4.1 `01.04 / 具体学科`

本轮最明确的收口不是把更多具体学科论文移出 `01.04`，而是把 facility assistant、instrument copilot、SDL orchestration interface 这类“科研基础设施层”论文从 confirmed core 中清出去。  
这说明当前 `01.04` 的主要风险，不是顶层定义失效，而是平台层 / 界面层 / 协同层样本容易被过宽保留。

### 4.2 `03 / 04`

nanoparticle、MOF/COF、electrocatalyst、polymer blend 等仍是高压边界。  
当前执行口径仍应保持稳定：直接被搜索和优化的是分子、反应、合成路线、催化条件时优先归 `03`；直接被搜索和优化的是材料组成、结构、相、性能、表征对象时优先归 `04`。本轮没有足够强的新证据支持重写这一边界。

### 4.3 `06 / 07`

本轮主要压力不只是 biology vs medicine，而是“bioinformatics / biological-discovery platform 是否被过宽保留为 confirmed core”。  
`ASD-0559`、`ASD-0560` 的降级进一步说明：只要论文主体更像 evaluation、orchestration、copilot-setting，对象即使在生命科学侧，也不应自动保留为核心样本。

### 4.4 `11.07 / 01.04`

本轮没有新增必须立刻改动的 `11.07` 个案，但这条边界依然稳定有效。  
通用科研能力平台仍归 `01.04`；凡研究对象已转向 scientific knowledge production itself、peer review、科研共同体或 science-of-science，则应优先归 `11.07`。后续仍需持续盯防 review / benchmark / science-of-science 条目误留在 `01.04`。

### 4.5 `05 / 10`

本轮没有出现足以触发新增改动的 `05 / 10` 样本，但现有口径继续成立：  
若研究对象是地球环境、气候、水文、冰冻圈、火山等自然过程，优先归 `05`；若核心是 mission science operation、rover、spacecraft science autonomy、海工装备或交通系统，则归 `10`。

## 5. 本轮交叉复核结论

- 本轮四个只读 reviewer 的交叉复核，没有再产生新的高置信主列表改动。
- 当前主列表已经包含第 3 轮最重要的高置信收口结果，尤其是：
  - review / tutorial / generic AI background 的二级类收紧
  - facility assistant / orchestration interface / instrument copilot 从 confirmed core 中退出
- 其余被 reviewer 再次点名的样本，当前主要属于“边界压力仍在，但证据不足以继续强改”的后续观察池。

## 6. 本轮后统计

- confirmed included + classified count：`479`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- confirmed class 分布：
  - `01: 47`
  - `02: 31`
  - `03: 73`
  - `04: 100`
  - `05: 25`
  - `06: 58`
  - `07: 51`
  - `08: 3`
  - `09: 35`
  - `10: 24`
  - `11: 32`
- 当前主要边界压力点：
  - `01.04 / 具体学科`
  - `03 / 04`
  - `06 / 07`
  - `11.07 / 01.04`
  - `05 / 10`
  - 平台层 / 设施层 / 评测型论文是否被过宽保留为 confirmed core

## 7. 结论

- 第 3 轮已经完成对 `ASD-0401`–`ASD-0600` 的一轮有效收口，真正落地的高置信改动主要集中在 confirmed core 过宽保留的 infrastructure / assistant / evaluation 类论文。
- 当前剩余问题主要不是一级类失稳，而是平台层与对象层的解释边界，以及 `03 / 04`、`06 / 07` 这类高压对象边界的持续压测。
- 当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。

## 8. 下一轮建议

- 下一轮范围：`ASD-0601`–`ASD-0800`
- 继续采用 `200` 篇一轮、`4 x 50` reviewer 的只读并行复核模式
- 主控代理优先抓以下问题：
  - `01.04` 中可能被误保留为核心的 review / benchmark / orchestration / instrumentation 记录
  - `03 / 04` 高压边界样本
  - `06 / 07` 与 bioinformatics-platform / translational framing 交叉样本
  - duplicate / lineage / preprint cleanup
