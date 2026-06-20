# 第 5 轮全库分类复核报告：`ASD-0801`–`ASD-0871`

> Historical note 2026-06-20：本报告形成于当前“放松领域实验覆盖”口径完全固化之前。报告中关于 `cross-domain demo`、`主对象`、`核心贡献`、`暂保持 01.04` 的判断只作为历史背景；本轮 451 篇多模块复核必须以 `multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md` 为准，逐项检查具体科学对象实验、验证、benchmark task、case study 或结果报告。只要对象层证据可识别，即可记录对应 `01–11` 模块，不要求该模块构成论文核心贡献。

生成日期：`2026-06-18`  
审计模式：全库分类复核，第 5 轮，尾段收口，`4` 个只读 reviewer 并行复核，主控代理统一裁决  
审计范围：`Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md` 中 `ASD-0801`–`ASD-0871`

说明：本文件为 Round 5 的 canonical 收口版。此前 Round 5 过程中已有部分收口直接写入主列表，但旧版报告的基线与当前权威主列表不一致，因此本次按当前主列表真值重新对齐。以下只记录已经真实落地主列表的 Round 5 收口结果，以及本轮 4 个只读 reviewer 复核后仍需关注但暂不改动的边界样本。

## 1. 本轮开始前基线

- confirmed included + classified count：`478`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- 当前主要边界压力点：
  - `01.04 / 具体学科对象`
  - `01.04 / 11.07`
  - `03 / 04`
  - `05 / 10`
  - `08 / 06`

## 2. Round 5 已落地主列表的收口项

说明：本轮最终 read-only reviewer 收口没有再新增主列表改动。下表仅回溯记录 Round 5 中已经真实写入 `agent_master_paper_list.md` 的处理结果。

| ID | 题名 | 当前主列表状态 | 处理结论 | 理由 |
|---|---|---|---|---|
| ASD-0834 | AiSciVision: A Framework for Specializing Large Multimodal Models in Scientific Image Classification | `background_only / 01.04` | 从 confirmed core 收口为 background | 当前更像跨领域 scientific image workflow / interpretability framework，而不是稳定的 primary scientific-discovery Agent paper。 |
| ASD-0835 | SciDataCopilot: An Agentic Data Preparation Framework for AGI-driven Scientific Discovery | `background_only / 01.04` | 从 confirmed core 收口为 background | 论文主对象是 scientific-data ingestion / preparation / integration infrastructure，不宜继续占用 confirmed core。 |
| ASD-0836 | Reframing Discovery Trade-Off in Plant Genomics Through Autonomous Agents | `background_only / 08.01` | 清出 `needs_review`，不进入 confirmed core | 当前证据只支持其作为 plant-genomics review / benchmark / agenda 型边界样本保留；既不应继续挂在 `needs_review`，也不足以进入 confirmed core。 |
| ASD-0837 | VESTA: Visual Exploration with Statistical Tool Agents | `background_only / 01.04` | 从 confirmed core 收口为 background | 当前更像 statistical-tool scientific-modeling workflow 与 benchmark substrate，真实 astronomy task 只是验证场景。 |
| ASD-0846 | SCP: Accelerating Discovery with a Global Web of Autonomous Scientific Agents | `background_only / 01.04` | 从 confirmed core 收口为 background | 主对象是 protocol-level orchestration / lifecycle-management infrastructure，而不是稳定的 primary discovery-agent study。 |
| ASD-0847 | Claw AI Lab: An Autonomous Multi-Agent Research Team | `background_only / 01.04` | 从 confirmed core 收口为 background | 当前更像 AI-lab infrastructure、interactive control plane 与 research-team orchestration，而不是具体学科科学对象论文。 |
| ASD-0848 | PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing | `to_read / 11.07` | 收口到 `11.07` | 直接对象是 scientific manuscript production / publication workflow，属于 scientific knowledge production itself。 |
| ASD-0849 | OmniScientist: Toward a Co-evolving Ecosystem of Human and AI Scientists | `to_read / 11.07` | 从 `01.04` 收口到 `11.07` | 论文中心已转向 human-AI scientist ecosystem、peer review、contribution attribution、scientific knowledge networks 与 open scientific evaluation infrastructure。 |

## 3. 本轮重点复核但暂不改动

| ID | 题名 | 当前主列表状态 | 暂不改动原因 | 是否建议后续全文复核 |
|---|---|---|---|---|
| ASD-0802 | Exploring Robust Multi-Agent Workflows for Environmental Data Management | `background_only / 05.03` | reviewer 对其 `05 / 11.07` 归属有中等分歧；当前仍可解释为 environment-facing data-management boundary sample，但证据不足以直接改到 `11.07`。 | 是 |
| ASD-0811 | Closed-Loop Molecular Design with Calibrated Deference | `to_read / 04.04` | reviewer 提示其标题与直接搜索对象更像 molecule-side sample，但当前主列表备注仍强调 battery-material / energy-materials object，`03 / 04` 边界证据尚不足以强改。 | 是 |
| ASD-0844 | Science Earth: Towards A Planet-Scale Operating System for AI-Native Scientific Discovery | `to_read / 01.04` | 虽然有 physics / biology case study，但当前证据更支持其为 scientific-agent runtime / OS / coordination substrate；跨域 demo 本身不足以把它移出 `01.04`。 | 是 |
| ASD-0845 | SciDER: Scientific Data-centric End-to-end Researcher | `to_read / 01.04` | 当前仍缺少稳定、单一、可重复指向的 concrete scientific object 证据；更像通用 data-centric end-to-end scientific researcher。 | 是 |
| ASD-0855 | Automating Scientific Evaluation: A Multi-Agent Framework for Transparent and Trustworthy Peer Review | `to_read / 11.07` | `11.07` 方向稳定，但 empirically 仍偏 framework / evaluation-heavy sample，后续可在写 note 时再核一次强度。 | 是 |

## 4. 边界问题清单

### 4.1 `01.04 / 具体学科对象`

本轮尾段最重要的判断不是再把更多论文硬移出 `01.04`，而是继续稳住“通用 scientific-agent runtime / workflow substrate 不因跨学科 demo 自动脱离 `01.04`”这条规则。  
`ASD-0844` `Science Earth` 与 `ASD-0845` `SciDER` 当前都更像 general scientific-agent substrate，而不是已经稳定落在某个具体 scientific object 上的 domain paper。

### 4.2 `01.04 / 11.07`

这一边界在尾段总体更清楚了：

- `ASD-0848` `PaperOrchestra`、`ASD-0849` `OmniScientist`、`ASD-0855` 都支持：scientific manuscript production、peer review、scientific evaluation、scientific knowledge production itself 应优先归 `11.07`
- `ASD-0844`、`ASD-0845`、`ASD-0846`、`ASD-0847` 则继续支持：general scientific runtime、protocol、research-team substrate、workflow infrastructure 仍应留在 `01.04`

因此，当前压力主要在边界解释，不在一级主类设计本身。

### 4.3 `03 / 04`

`ASD-0811` 是本轮最典型的 `03 / 04` 边界样本。reviewer 有一方认为题名与直接搜索对象更像 molecule design，应回到 `03`；但当前主列表已有 battery-material / energy-materials explanation，且没有足够强的新证据支持立即改写主类。  
这说明 `03 / 04` 当前仍是高压边界，但现行 object-first 规则仍能工作。

### 4.4 `05 / 10`

尾段样本继续稳定支持既有硬规则：

- `ASD-0851` 这类 geospatial / Earth-science model discovery 留在 `05`
- `ASD-0852`–`ASD-0854`、`ASD-0858` 这类 rover / mission-science autonomy 留在 `10`
- `ASD-0859`–`ASD-0861` 这类 mission-borne Earth natural-process monitoring 留在 `05`

因此，本轮没有形成支持重写 `05 / 10` 一级边界的新证据。

### 4.5 `08 / 06`

`ASD-0836` 的收口再次说明：`08` 稀缺不等于可以放宽。  
当前最稳妥的做法仍是：

- 若只是 plant genomics / plant-science review、benchmark、agenda paper，则保留为边界背景样本
- 只有当论文真正面向 crop production / breeding / agricultural research object 且满足 Agent 核心纳入标准时，才进入 `08` confirmed core

本轮没有找到新的证据去放宽 `08`。

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
  - `01.04 / 具体学科对象`
  - `01.04 / 11.07`
  - `03 / 04`
  - `05 / 10`
  - `08 / 06`
  - infrastructure / protocol / workflow-heavy records 是否被误计入 confirmed core

## 6. 结论

Round 5 的主结论不是一级类失稳，而是尾段样本进一步证实：当前真正需要持续收口的，是 `01.04` 中 infrastructure / protocol / workflow-heavy records 的解释边界，以及少数 `03 / 04`、`05 / 10`、`08 / 06` 压力样本的谨慎裁决。  

当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。
