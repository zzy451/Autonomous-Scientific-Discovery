# 边界文献池清理审计报告

> 日期：2026-06-16
> 对象：`Paper_Lists/agent_master_paper_list.md` 中原 `candidate` 与 `needs_review` 边界文献。
> 方法：按项目 Agent 纳入口径与 01-11 科学对象分类口径，结合 4 个只读子 Agent 的分领域复核结果，并对剩余 5 篇做公开摘要/页面复核后合并决策。

## 一、总体结果

| 指标 | 数量 |
|---|---:|
| 主表总记录 | 500 |
| 本轮触达记录 | 85 |
| 已确认并收录分类论文 | 136 |
| 当前 `candidate` | 0 |
| 当前 `to_read` | 136 |
| 当前 `background_only` | 333 |
| 当前 `excluded` | 31 |
| 当前 `needs_review` | 0 |

本轮之后，`candidate` 与 `needs_review` 已全部清零。边界池中的文献均已被归入 `to_read`、`background_only` 或 `excluded`。

## 二、已确认收录论文主类分布

| Main class | Count |
|---|---:|
| 01 | 18 |
| 02 | 9 |
| 03 | 29 |
| 04 | 37 |
| 05 | 0 |
| 06 | 19 |
| 07 | 16 |
| 08 | 0 |
| 09 | 8 |
| 10 | 0 |
| 11 | 0 |

## 三、本轮状态流向

### `to_read`：59 篇

| ID | Main class | Title |
|---|---|---|
| ASD-0112 | 07 / 07.04 | CSSTep: Step-by-step exploration of the chemical space of drug molecules via multi-agent and multi-stage reinforcement learning |
| ASD-0113 | 07 / 07.04 | PharmAgents: Building a virtual pharma with large language model agents |
| ASD-0114 | 06 / 06.03 | Sparks: Multi-agent artificial intelligence model discovers protein design principles |
| ASD-0115 | 07 / 07.04 | Towards an AI co-scientist |
| ASD-0116 | 04 / 04.04 | Electromagnetic metamaterial agent |
| ASD-0117 | 04 / 04.02 | OSDA agent: Leveraging large language models for de novo design of organic structure directing agents |
| ASD-0118 | 07 / 07.04 | Biomni: A general-purpose biomedical AI agent |
| ASD-0119 | 04 / 04.03 | ChatMOF: An autonomous AI system for predicting and generating metal-organic frameworks |
| ASD-0120 | 02 / 02.01 | AI agents for ground-based gamma astronomy |
| ASD-0121 | 02 / 02.01 | Multi-agent system for cosmological parameter analysis |
| ASD-0124 | 09 / 09.05 | A large language model-empowered agent for reliable and robust structural analysis |
| ASD-0125 | 09 / 09.03 | Physics-informed LLM-agent for automated modulation design in power electronics systems |
| ASD-0127 | 02 / 02.01 | The AI Cosmologist I: An agentic system for automated data analysis |
| ASD-0128 | 09 / 09.01 | MechAgents: Large language model multi-agent collaborations can solve mechanics problems, generate new data, and integrate knowledge |
| ASD-0129 | 09 / 09.01 | OpenFOAMGPT: a RAG-augmented LLM agent for OpenFOAM-based computational fluid dynamics |
| ASD-0132 | 01 / 01.04 | Many heads are better than one: Improved scientific idea generation by a LLM-based multi-agent system |
| ASD-0133 | 02 / 02.01 | Interpreting multi-band galaxy observations with large language model-based agents |
| ASD-0135 | 04 / 04.04 | A multi-agent framework integrating large language models and generative AI for accelerated metamaterial design |
| ASD-0136 | 02 / 02.01 | Starwhisper telescope: Agent-based observation assistant system to approach AI astrophysicist |
| ASD-0137 | 06 / 06.03 | Accelerating primer design for amplicon sequencing using large language model-powered agents |
| ASD-0138 | 06 / 06.03 | CellAgent: An LLM-driven multi-agent framework for automated single-cell data analysis |
| ASD-0139 | 02 / 02.02 | Advancing AI-scientist understanding: Making LLM think like a physicist with interpretable reasoning |
| ASD-0141 | 06 / 06.03 | TransAgent: Dynamizing transcriptional regulation analysis via multi-omics-aware AI agent |
| ASD-0145 | 01 / 01.04 | CycleResearcher: Improving automated research via automated review |
| ASD-0146 | 01 / 01.04 | AIGS: Generating science from AI-powered automated falsification |
| ASD-0147 | 01 / 01.04 | Nova: An iterative planning and search approach to enhance novelty and diversity of LLM-generated ideas |
| ASD-0149 | 03 / 03.03 | A flexible and affordable self-driving laboratory for automated reaction optimization |
| ASD-0150 | 03 / 03.03 | A dynamic knowledge graph approach to distributed self-driving laboratories |
| ASD-0151 | 04 / 04.04 | Self-driving lab discovers principles for steering spontaneous emission beyond conventional Fourier optics |
| ASD-0152 | 06 / 06.03 | An agentic AI framework for ingestion and standardization of single-cell RNA-seq data analysis |
| ASD-0154 | 04 / 04.04 | Real-time experiment-theory closed-loop interaction for autonomous materials science |
| ASD-0155 | 04 / 04.04 | A multi-agentic framework for real-time, autonomous freeform metasurface design |
| ASD-0156 | 04 / 04.01 | Bridging electron microscopy and materials analysis with an autonomous agentic platform |
| ASD-0158 | 03 / 03.03 | A robotic platform for flow synthesis of organic compounds informed by AI planning |
| ASD-0179 | 03 / 03.03 | Chemist-x: Large language model-empowered agent for reaction condition recommendation in chemical synthesis |
| ASD-0357 | 07 / 07.04 | Origene: A self-evolving virtual disease biologist automating therapeutic target discovery |
| ASD-0370 | 06 / 06.03 | Self-driving laboratories to autonomously navigate the protein fitness landscape |
| ASD-0376 | 04 / 04.04 | Self-Driving Laboratory for Polymer Electronics |
| ASD-0379 | 04 / 04.04 | A self-driving laboratory advances the Pareto front for material properties |
| ASD-0381 | 03 / 03.03 | Autonomous reaction Pareto-front mapping with a self-driving catalysis laboratory |
| ASD-0385 | 03 / 03.03 | AlphaFlow: autonomous discovery and optimization of multi-step chemistry using a self-driven fluidic lab guided by reinforcement learning |
| ASD-0388 | 04 / 04.04 | Crystallography companion agent for high-throughput materials discovery |
| ASD-0389 | 04 / 04.04 | Autonomous discovery of optically active chiral inorganic perovskite nanocrystals through an intelligent cloud lab |
| ASD-0390 | 04 / 04.04 | A self-driving laboratory designed to accelerate the discovery of adhesive materials |
| ASD-0410 | 04 / 04.04 | On-the-fly closed-loop materials discovery via Bayesian active learning |
| ASD-0415 | 03 / 03.03 | Autonomous polymer synthesis delivered by multi-objective closed-loop optimisation |
| ASD-0417 | 04 / 04.04 | Autonomous optimization of non-aqueous Li-ion battery electrolytes via robotic experimentation and machine learning coupling |
| ASD-0418 | 03 / 03.03 | Data-science driven autonomous process optimization |
| ASD-0421 | 04 / 04.04 | Closed-loop superconducting materials discovery |
| ASD-0422 | 03 / 03.03 | Autonomous closed-loop mechanistic investigation of molecular electrochemistry via automation |
| ASD-0425 | 04 / 04.03 | Efficient Closed-loop Maximization of Carbon Nanotube Growth Rate using Bayesian Optimization |
| ASD-0428 | 03 / 03.03 | Discovering New Chemistry with an Autonomous Robotic Platform Driven by a Reactivity-Seeking Neural Network |
| ASD-0429 | 09 / 09.02 | Toward autonomous additive manufacturing: Bayesian optimization on a 3D printer |
| ASD-0455 | 03 / 03.03 | A mobile robotic chemist |
| ASD-0463 | 03 / 03.03 | AI-driven robotic chemist for autonomous synthesis of organic molecules |
| ASD-0466 | 04 / 04.03 | Discovery of Wall-Selective Carbon Nanotube Growth Conditions <i>via</i> Automated Experimentation |
| ASD-0468 | 04 / 04.03 | Closed-loop optimization of nanoparticle synthesis enabled by robotics and machine learning |
| ASD-0487 | 04 / 04.04 | Autonomous Discovery of Battery Electrolytes with Robotic Experimentation and Machine Learning |
| ASD-0491 | 04 / 04.04 | Optimizing Perovskite Thin‐Film Parameter Spaces with Machine Learning‐Guided Robotic Platform for High‐Performance Perovskite Solar Cells |

### `background_only`：24 篇

| ID | Main class | Title |
|---|---|---|
| ASD-0111 | 01 / 01.04 | SciMaster: Towards general-purpose scientific AI agents, Part I. X-Master as foundation: Can we lead on Humanity's Last Exam? |
| ASD-0122 | 07 / 07.02 | Agent Hospital: A simulacrum of hospital with evolvable medical agents |
| ASD-0126 | 06 / 06.03 | BioAgents: Democratizing bioinformatics analysis with multi-agent systems |
| ASD-0130 | 01 / 01.04 | Large language models are zero-shot hypothesis proposers |
| ASD-0134 | 03 / 03.01 | ChemAgent: Self-updating library in large language models improves chemical reasoning |
| ASD-0140 | 11 / 11.02 | Large language models for automated open-domain scientific hypotheses discovery |
| ASD-0142 | 06 / 06.03 | CompBioAgent: An LLM-powered agent for single-cell RNA-seq data exploration |
| ASD-0143 | 01 / 01.04 | MAPS: A multi-agent framework based on Big Five personality and Socratic guidance for multimodal scientific problem solving |
| ASD-0148 | 01 / 01.04 | AIRUS: a simple workflow for AI-assisted exploration of scientific data |
| ASD-0153 | 07 / 07.02 | Development and validation of an autonomous artificial intelligence agent for clinical decision-making in oncology |
| ASD-0159 | 07 / 07.03 | Conversational health agents: A personalized llm-powered agent framework |
| ASD-0207 | 01 / 01.04 | Ds-agent: Automated data science by empowering large language models with case-based reasoning |
| ASD-0222 | 02 / 02.02 | Improving physics reasoning in large language models using mixture of refinement agents |
| ASD-0372 | 04 / 04.04 | Data-Centric Architecture for Self-Driving Laboratories with Autonomous Discovery of New Nanomaterials |
| ASD-0373 | 01 / 01.04 | ChemOS: An orchestration software to democratize autonomous discovery |
| ASD-0382 | 04 / 04.04 | Toward autonomous design and synthesis of novel inorganic materials |
| ASD-0383 | 01 / 01.04 | Universal self-driving laboratory for accelerated discovery of materials and molecules |
| ASD-0384 | 01 / 01.04 | Chimera: enabling hierarchy based multi-objective optimization for self-driving laboratories |
| ASD-0402 | 04 / 04.04 | Self-Driving Laboratories for Development of New Functional Materials and Optimizing Known Reactions |
| ASD-0414 | 04 / 04.04 | Accelerating materials discovery using artificial intelligence, high performance computing and robotics |
| ASD-0447 | 03 / 03.03 | An autonomous portable platform for universal chemical synthesis |
| ASD-0469 | 06 / 06.03 | Achieving Reproducibility and Closed-Loop Automation in Biological Experimentation with an IoT-Enabled Lab of the Future |
| ASD-0478 | 04 / 04.04 | NIMS-OS: an automation software to implement a closed loop between artificial intelligence and robotic experiments in materials science |
| ASD-0484 | 01 / 01.04 | Evolution-guided Bayesian optimization for constrained multi-objective optimization in self-driving labs |

### `excluded`：2 篇

| ID | Main class | Title |
|---|---|---|
| ASD-0367 | 06 / 06.03 | Advancing biomolecular understanding and design following human instructions |
| ASD-0470 | 06 / 06.02 | Hard real-time closed-loop electrophysiology with the Real-Time eXperiment Interface (RTXI) |

## 四、最终边界复核决策

| ID | 最终状态 | 判断依据 |
|---|---|---|
| ASD-0126 | background_only | BioAgents 是 multi-agent / RAG 生物信息学辅助系统，但公开摘要主要显示 conceptual genomics tasks，且代码执行和端到端科研分析闭环仍是后续方向。 |
| ASD-0140 | background_only | 面向 social science academic hypothesis discovery，具有多模块与反馈机制，但 Agent 行动闭环表述不足。 |
| ASD-0142 | background_only | CompBioAgent 面向 scRNA-seq 数据查询与探索，但公开摘要中规划、工具执行和反馈迭代证据不足。 |
| ASD-0147 | to_read | Nova 采用 iterative planning and search，通过规划检索外部知识迭代生成科研想法，符合 01.04 科研 idea generation 的多步 Agent-like 工作流。 |
| ASD-0466 | to_read | 公开摘要称该 automated rapid serial experimentation 是迈向 autonomous closed-loop learning system / Robot Scientist 的进展，符合材料自主实验闭环。 |

## 五、分类压力判断

本轮清理后，已确认收录论文仍然没有覆盖以下主类：

- `05`
- `08`
- `10`
- `11`

这说明当前核心 Agent 论文仍集中在 `01`、`02`、`03`、`04`、`06`、`07`、`09`。这不代表后续必须定向搜索，只表示在当前池子中这些主类的核心收录为 0。

## 六、下一步建议

1. 继续按照 source-first 路径扩展：先从 Shanghai AI Lab seed survey 及相关综述的引用链继续扩展，再从 Nature / Science 及其 family journals 的高影响论文继续向后、向前引用扩展。
2. 继续先粗筛、归类、记录 source trail，把确认收录论文数量推进到 500。
3. 达到 500 篇确认收录后，再统一做去重、分类压力审计和论文笔记批量生成。
