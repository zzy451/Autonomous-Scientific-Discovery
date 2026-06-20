# `01.04` 中 SDL / data-science 残余样本收口报告

生成日期：`2026-06-18`  
审计目标：继续压缩 `01.04` 中仍被计入 confirmed core 的 benchmark / orchestration / general data-science automation 样本，避免把通用研究基础设施继续算作稳定 ASD 核心系统。

## 1. 本轮开始前基线

- confirmed included + classified count：`479`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- 当时主要边界压力点：
  - `01.04 / 具体学科`
  - `01.04 / 11.07`
  - `05 / 10`
  - `08 / 06`
  - `01.04` 内部的 SDL infrastructure / orchestration / benchmark / general data-science automation 是否仍被过宽计入 confirmed core

## 2. 本轮已落地主列表改动

| ID | 题名 | 原状态 / 原主类 | 新状态 / 新主类 | 处理结论 | 理由 |
|---|---|---|---|---|---|
| ASD-0207 | Ds-agent: Automated data science by empowering large language models with case-based reasoning | `to_read / 01` | `background_only / 01` | 降级为背景 | arXiv 摘要核心是 automated data-science task completion、experiment-plan quality、Kaggle expert knowledge reuse、development/deployment-stage code generation，更像通用 data-science automation，而不是对象清晰的 ASD 核心 scientific-discovery workflow。 |
| ASD-0373 | ChemOS: An orchestration software to democratize autonomous discovery | `to_read / 01` | `background_only / 01` | 降级为背景 | 题名和摘要层证据都把它定义为 orchestration software，用于集成 instruments、optimizers 与 workflow execution；这更符合 self-driving-lab 基础设施背景，而不是稳定的 confirmed core discovery-Agent paper。 |

## 3. 本轮重点复核但暂不改动

| ID | 题名 | 当前主类 | 暂不改动原因 | 是否建议后续复核 |
|---|---|---|---|---|
| ASD-0089 | ResearchCodeAgent: An LLM Multi-Agent System for Automated Codification of Research Methodologies | `01` | 本地 full note 支持它不仅是 benchmark，而是明确的多 Agent 科研方法 codification system；当前证据仍足以保留 confirmed core。 | 是 |
| ASD-0100 | SciReplicate-Bench: Benchmarking LLMs in Agent-driven Algorithmic Reproduction from Research Papers | `01` | 虽然 benchmark 属性很强，但它同时提出 `Sci-Reproducer` dual-agent framework，且本地 full note 已明确其作为科研复现 Agent benchmark 的代表性；暂不直接降级。 | 是 |
| ASD-0384 | Chimera: enabling hierarchy based multi-objective optimization for self-driving laboratories | `01` | 仍是高风险 SDL decision-loop / optimization infrastructure 样本，但当前缺少足够强的摘要或全文证据支持本轮直接降级。 | 是 |
| ASD-0528 | AutoSciLab: A Self-Driving Laboratory for Interpretable Scientific Discovery | `01` | 题名显示 general self-driving laboratory，存在继续降级空间，但当前证据仍不足以高置信收口。 | 是 |
| ASD-0593 | AutoDSL: Automated self-driving laboratory with large language model agents | `01` | 同样属于 general SDL orchestration 样本，仍值得后续重点复核。 | 是 |

## 4. 边界问题清单

### 4.1 `01.04` 当前最大残余压力不再是“明显跨学科 case study”

这轮进一步说明，`01.04` 当前更大的噪声来源不是带多个 science case 的 general agent paper，而是：

- data-science automation
- orchestration software
- workflow integration layer
- self-driving-lab operating interface
- benchmark-heavy scientific coding / reproduction stack

这些样本即使满足 Agent 最低纳入标准，也不应自动继续占用 confirmed core。

### 4.2 `general automation` 与 `scientific-discovery core` 需要继续分开

`DS-Agent` 的例子说明，只要研究对象主要是通用 data-science task automation、Kaggle knowledge reuse、model-selection / code-generation pipeline，就不能因为它“自动化了研究过程”而直接视为 ASD 核心 scientific-discovery paper。

### 4.3 `SDL orchestration layer` 应继续从严

`ChemOS` 的收口与前面 `ChemOS 2.0`、`IvoryOS`、`LabPilot` 等判断方向一致：  
如果论文核心是 orchestration architecture、web interface、facility integration、execution middleware 或 control surface，那么它更适合作为 `01.04` 背景设施，而不是 confirmed core。

## 5. 本轮后统计

- confirmed included + classified count：`477`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- confirmed class 分布：
  - `01: 48`
  - `02: 31`
  - `03: 71`
  - `04: 100`
  - `05: 25`
  - `06: 56`
  - `07: 51`
  - `08: 3`
  - `09: 36`
  - `10: 24`
  - `11: 32`
- 当前主要边界压力点：
  - `01.04 / 具体学科`
  - `01.04 / 11.07`
  - `05 / 10`
  - `08 / 06`
  - `01.04` 内 remaining SDL / benchmark / scientific-coding core 样本是否仍有少量过宽保留

## 6. 结论

这轮继续证明，confirmed core 的主要收口方向仍然是把 `01.04` 中的通用 infrastructure、benchmark、orchestration、data-workflow 类论文从核心统计里剥离出去，而不是重写一级分类框架本身。  
当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。
