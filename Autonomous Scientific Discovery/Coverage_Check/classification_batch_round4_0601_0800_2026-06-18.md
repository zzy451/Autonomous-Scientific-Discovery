# 第4轮全库分类复核报告：`ASD-0601`–`ASD-0800`

生成日期：`2026-06-18`  
审计模式：全库分类复核，第 4 轮，`200` 篇一批，`4 x 50` 只读 reviewer，由主控代理统一裁决并维护主列表  
审计范围：`Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md` 中 `ASD-0601`–`ASD-0800`  
说明：本文件为第 4 轮收口版，已按当前权威主列表重新对齐；只记录已经真实落地到主列表的改动，以及本轮只读 reviewer 交叉复核后仍需后续观察的边界样本。

## 1. 本轮开始前基线

- confirmed included + classified count：`478`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- 当前主要边界压力点：
  - `01.04 / 具体学科`
  - `01.04 / 11.07`
  - `03 / 04`
  - `05 / 10`
  - `06 / 07`
  - `08 / 06`
  - review / benchmark / framework / conceptual / deployment report 是否被过宽保留为 confirmed core
  - same-system lineage / infrastructure / AaaS / copilot 记录是否被过宽计入核心覆盖

## 2. 本轮已落地主列表改动

### 2.1 从 confirmed core 降为 `background_only`

| ID | 题名 | 原状态 / 原主类 | 新状态 / 新主类 | 处理结论 | 理由 |
|---|---|---|---|---|---|
| ASD-0619 | ChemOS 2.0: An orchestration architecture for chemical self-driving laboratories | `to_read / 03` | `background_only / 03` | 降级 | 核心贡献是 chemical SDL orchestration architecture，属于基础设施层，不宜继续作为稳定化学发现 Agent 核心记录计数。 |
| ASD-0620 | Enabling Modular Autonomous Feedback-Loops in Materials Science through Hierarchical Experimental Laboratory Automation and Orchestration | `to_read / 04` | `background_only / 04` | 降级 | 重点在 hierarchical automation / orchestration stack，而不是稳定的 primary materials-discovery system study。 |
| ASD-0657 | Vibe Researching as Wolf Coming: Can AI Agents with Skills Replace or Augment Social Scientists? | `to_read / 11` | `background_only / 11` | 降级 | 当前证据更像能力评估 / 讨论型 paper，而不是稳定的 primary social-science Agent-system study。 |
| ASD-0785 | Multi-Agent Geospatial Copilots for Remote Sensing Workflows | `to_read / 05` | `background_only / 05` | 降级 | 更像 remote-sensing workflow copilot / platform，而不是稳定 primary Earth-observation discovery-agent study。 |
| ASD-0795 | OpenAaaS: An Open Agent-as-a-Service Framework for Distributed Materials-Informatics Research | `to_read / 09` | `background_only / 09` | 降级 | 核心是 distributed AaaS / research infrastructure，而不是稳定的 primary materials-discovery system。 |

### 2.2 主类收口修正

| ID | 原主类 | 新主类 | 处理结论 | 理由 |
|---|---|---|---|---|
| ASD-0660 | `06 / 06.03` | `01 / 01.04` | 主类改判 | 虽有生物、化学、材料实验验证，但论文主对象是 multidisciplinary general scientific-research framework，应回到 `01.04`。 |
| ASD-0673 | `04 / 04.04` | `01 / 01.04` | 主类改判 | AtomisticSkills 是跨 materials / chemistry / drug-design 的通用 atomistic-research harness，不是单一稳定材料对象。 |
| ASD-0798 | `09 / 09.01` | `07 / 07.04` | 主类改判 | 按 object-first 规则，最终对象是 drug lead optimization 与 ADMET refinement，应回收到药物发现侧，而不是保留在工程基础设施侧。 |

### 2.3 重复 / 同源题名清理

| ID | 原状态 / 原主类 | 新状态 / 新主类 | 处理结论 | 理由 |
|---|---|---|---|---|
| ASD-0746 | `to_read / 10` | `excluded / 10` | duplicate cleanup | 与 `ASD-0712` 共用同一 2005 OASIS rover-science primary PDF，本轮按 title/source-shared duplicate 处理，保留 `ASD-0712` 为 canonical record。 |

### 2.4 二级类与元数据纠错

| ID | 处理类型 | 结果 | 理由 |
|---|---|---|---|
| ASD-0605 | 二级类修正 | `03.05 -> 03.04` | `03.05` 不是当前 taxonomy 有效二级码；对象仍是 chemical droplet formulation / behavior search，而不是材料对象。 |
| ASD-0613 | 二级类修正 | `02.03 -> 02.02` | `02.03` 不是当前 taxonomy 有效二级码；对象是 physical-science experimentation rather than astronomy。 |
| ASD-0724 | 二级类修正 | `06.04 -> 06.02` | `06.04` 不是当前 taxonomy 有效二级码；对象是 marine biodiversity rather than missing biotechnology subtype。 |
| ASD-0636 | 元数据纠错 | arXiv 改为 `2606.06025` | 修正 EGTR-Review 的错链，保留 `11.07` 与 core 状态。 |
| ASD-0637 | 元数据纠错 | arXiv 改为 `2511.03758` | 修正 citation-network simulation 社会科学研究条目的错链，保留 `11.07`。 |

## 3. 本轮重点复核但暂不改动

以下条目在四个只读 reviewer 的交叉复核中被再次点名，但本轮没有形成足够强的新证据，因此主列表暂不继续改动。

| ID | 题名 | 当前主类 | 暂不改动原因 | 是否建议后续复核 |
|---|---|---|---|---|
| ASD-0624 | Toward a domain-grounded AI collaborator with SciSciGPT | `11` | 主列表已是 primary research article 而非 Research Briefing，降级证据不足。 | 是 |
| ASD-0625 | ReviewAgents: Bridging the Gap Between Human and AI-Generated Paper Reviews | `11` | peer-review object 明确，但 benchmark / work-in-progress 味较重。 | 是 |
| ASD-0628 | ScholarPeer: A Context-Aware Multi-Agent Framework for Automated Peer Review | `11` | object 明确属于 `11.07`，但 assistant-like 色彩偏重。 | 是 |
| ASD-0629 | CiteME: Can Language Models Accurately Cite Scientific Claims? | `11` | title benchmark 味重，但 claim-attribution object 仍可支撑 `11.07`。 | 是 |
| ASD-0634 | Aleks: AI powered Multi Agent System for Autonomous Scientific Discovery via Data-Driven Approaches in Plant Science | `08` | 仍是本轮最关键的 `08 / 06` 压测样本之一；当前证据仍可支持 agricultural object framing。 | 是 |
| ASD-0669 | MARBLE: Multi-Agent Reasoning for Bioinformatics Learning and Evolution | `06` | 有 `06 / 01.04` 框架化压力，但未达直接改判阈值。 | 是 |
| ASD-0688 | OpenFOAMGPT 2.0: end-to-end, trustworthy automation for computational fluid dynamics | `09` | reviewer 提示可降为 background，但当前四代理没有形成足够一致的高置信主控改动。 | 是 |
| ASD-0695 | FoodPuzzle: Developing Large Language Model Agents as Flavor Scientists | `08` | `08` 必须严守；当前保留但仍需全文确认其是否超过 ideation / benchmark。 | 是 |
| ASD-0700 | Reimagining Peer Review Process Through Multi-Agent Mechanism | `11` | peer-review object 明确；当前不足以仅因 prototype / benchmark 味降级。 | 是 |
| ASD-0701 | Automating Computational Reproducibility in Social Science: Comparing Prompt-Based and Agent-Based Approaches | `11` | reproducibility object 明确；但 evaluation-forward 压力仍在。 | 是 |
| ASD-0705 | Automated reproducibility assessments in the social and behavioral sciences using large language models | `11` | 与 `0701` 类似，属于 `11.07` 评测型核心边界样本。 | 是 |
| ASD-0717 | Paper Circle: An Open-source Multi-agent Research Discovery and Analysis Framework | `11` | object 已偏向 knowledge production，但 core 强度弱于更稳定样本。 | 是 |
| ASD-0719 | Mission Operations of Earth Observing-1 with Onboard Autonomy | `10` | 有 same-system lineage inflation 压力，但当前摘要级证据仍支持 distinct mission-operations paper。 | 是 |
| ASD-0721 | Integrated AI in Space: The Autonomous Sciencecraft on Earth Observing One | `10` | 同属 class-10 同源谱系膨胀风险，但现阶段不宜无更细文献对照即直接降级。 | 是 |
| ASD-0726 | AutoClimDS: Climate Data Science Agentic AI -- A Knowledge Graph is All You Need | `05` | 可能偏 workflow assistant，但当前证据仍不足以直接降为背景。 | 是 |
| ASD-0727 | GeoAgentic-RAG: A Multi-Agent framework for autonomous geospatial reasoning and visual insight generation with LLM | `05` | 可能偏 workflow / reasoning platform，但 concrete geospatial object 仍在。 | 是 |
| ASD-0730 | Traxia: A Framework for Verifiable, Agent-Native Scientific Publishing | `11` | scientific publishing object 明确，但更像 formal architecture / prototype paper。 | 是 |
| ASD-0736 | AI-Researcher: Autonomous Scientific Innovation | `01` | general scientific-agent system 成立，但 benchmark / venue 属性较重。 | 是 |
| ASD-0738 | EvoMaster: Evolutionary Multi-Agent System for Autonomous Scientific Discovery | `01` | general scientific-discovery framework 成立，但 case-study strength 偏弱。 | 是 |
| ASD-0768 | When Reviews Disagree: Fine-Grained Contradiction Analysis in Scientific Peer Reviews | `11` | `11.07` object 明确，但 Agent 强度仍有 review-analysis / NLP-task 压力。 | 是 |
| ASD-0773 | Skill-Augmented AI Agents for Medical Research Analysis | `07` | 当前是 disease-facing medical research analysis 样本，但 human-evaluation 色彩偏重。 | 是 |
| ASD-0774 | Causal-Enhanced AI Agents for Medical Research Screening | `07` | 当前是 medical evidence-screening Agent，但 discovery 强度偏弱。 | 是 |
| ASD-0790 | Hierarchical Multi-agent Large Language Model Reasoning for Autonomous Heterogeneous Catalyst Discovery | `04` | 这是本轮最典型的 `03 / 04` 边界样本之一；当前仍保留为 deliberate boundary-test record。 | 是 |
| ASD-0800 | Risk-Aware LLM Agents for Geospatial Data Retrieval: Design and Preliminary Adversarial Evaluation | `05` | 可能偏 retrieval / safety evaluation，但 object 仍在 geospatial scientific inquiry 侧。 | 是 |

## 4. 边界问题清单

### 4.1 `01.04 / 具体学科`

`ASD-0660` 与 `ASD-0673` 的落地改判，进一步说明“带多领域实验”并不自动离开 `01.04`。  
只要论文主对象仍是通用 scientific-agent framework、跨域 harness、general research runtime / workflow substrate，就不应仅因它在生物、化学、材料上有 case study 而硬压进具体学科。

### 4.2 `01.04 / 11.07`

`0700 / 0701 / 0705 / 0717 / 0730 / 0768` 说明这条边界是本轮最大压力点之一。  
当前规则仍稳定：
- 通用科研能力平台、general scientific workflow、general scientific agent system 归 `01.04`
- peer review、reproducibility auditing、scientific publishing、literature synthesis、knowledge production object 归 `11.07`

问题不在一级类设计，而在 `11.07` 内部是否把“评测 / 架构 / prototype”记得过宽。

### 4.3 `03 / 04`

本轮没有出现需要直接重写一级边界的高置信误判。  
但 `ASD-0790`、`ASD-0792` 继续提醒我们：MOF、heterogeneous catalyst、COF、battery electrolyte、材料表征与 chemistry workflow 之间仍是高压边界。当前仍应保持原规则：
- 若直接被搜索和优化的是分子、反应、合成路线、催化条件、动力学路径，优先归 `03`
- 若直接被搜索和优化的是材料组成、结构、相、表面配置、材料性能或器件相关材料对象，优先归 `04`

### 4.4 `05 / 10`

本轮已将 `ASD-0785` 从 confirmed core 降为 `background_only`，说明 geospatial / remote-sensing workflow copilot 不应轻易计入核心。  
mission-science 主类判断继续沿用现有硬规则：
- 若研究对象是 Earth observation、气候、水文、冰冻圈、火山等自然过程，优先 `05`
- 若核心是 rover / spacecraft / mission science autonomy，则归 `10`

`0719 / 0721` 继续提示 class-10 内部还要防止 same-system lineage inflation。

### 4.5 `06 / 07`

本轮没有直接改类，但 `0773 / 0774 / 0798` 这些样本说明：只要对象明确转向 disease、clinical reasoning、drug lead optimization、medical evidence synthesis，就应更稳定地归 `07`。  
相反，gene/protein/cell/perturbation biology、bioinformatics over biological datasets 等仍以 `06` 为主。

### 4.6 `08 / 06`

`08` 仍然极度稀缺，本轮 confirmed count 仍只有 `3`。  
本轮复核没有找到足够证据去“放宽标准补数”；相反，`0634 / 0695` 更说明 `08` 必须严守“农业生产对象优先”口径：
- 若对象主要是 crop、breeding、agricultural production、food / flavor science、farming system，才可稳定归 `08`
- 若只是 plant biology / genomics / life mechanism，则应回到 `06`

### 4.7 infrastructure / benchmark / lineage cleanup

本轮真正落地的最大清理仍来自 infrastructure / orchestration / copilot / AaaS 记录：
- `0619`
- `0620`
- `0785`
- `0795`

`0657` 说明 capability / evaluation-heavy 的 `11` 类论文也需要更谨慎。  
class `10` 则还要继续防止 EO-1 / rover / mission lineage 因系统同源而造成 coverage inflation。

## 5. 本轮后统计

- confirmed included + classified count：`478`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- confirmed class 分布：
  - `01: 48`
  - `02: 31`
  - `03: 73`
  - `04: 99`
  - `05: 25`
  - `06: 58`
  - `07: 52`
  - `08: 3`
  - `09: 34`
  - `10: 23`
  - `11: 32`
- 当前主要边界压力点：
  - `01.04 / 具体学科`
  - `01.04 / 11.07`
  - `03 / 04`
  - `05 / 10`
  - `06 / 07`
  - `08 / 06`
  - infrastructure / copilot / benchmark / evaluation-heavy records 是否被过宽保留为 confirmed core
  - class-10 same-system lineage cleanup

## 6. 结论

- 第 4 轮确实发现并落地了一批高置信问题，但主要不是一级类错设，而是 confirmed core 口径过宽，把 infrastructure、copilot、AaaS、evaluation-heavy 记录算得过满。
- 本轮同时新增了少量高置信 object-first 收口结果：`0673` 回到 `01.04`，`0798` 回到 `07.04`，`0746` 作为同源 title/source-shared duplicate 清理出 confirmed core。
- 当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。

## 7. 下一轮建议

- 下一轮范围：`ASD-0801`–项目末尾
- 优先继续清理：
  - `Science Earth` 及同类 “general platform + concrete domain experiments” 样本
  - `01.04 / 11.07` 边界中的 benchmark / prototype / publishing / reproducibility records
  - `05 / 10` 中 Earth observation vs mission-science autonomy
  - `08 / 06` 稀缺样本
  - class-10 同系 mission-science lineage 膨胀
