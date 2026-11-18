# ScienceFlow: A long-horizon agent for ML research, scientific discovery and beyond

**论文信息**

- ID：ASD-0953
- 标题：ScienceFlow: A long-horizon agent for ML research, scientific discovery and beyond
- 作者：Zhao, Mingming; Dong, Jiqian; Xu, Kangping; Hasan, Zadid; Fan, Chengrui; Jiang, Shan; Mao, Shuai; Ling, Yating; Zou, Linyi; Zhou, Tailin; Chan, Yun Hin; Zhang, Wenkai; Zhou, Zhanhong; Huang, Guowei; Li, Hongliang; Cun, Wenjing; Chen, Zhitang; Yuan, Mingxuan; Geng, Yanhui
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.14354
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0953.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Mingming_2026_ScienceFlow_A_long_horizon_agent_for_ML_research_scientific_ASD0953.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入判断依据：目标是研究而非通用产品应用。 | 纳入判断依据：目标是研究而非通用产品应用。 | TXT line 827；核验TXT行号 827 | A task is defined as 𝒯=(𝒢,U𝒢,V𝒢,B,W0)\mathcal{T}=(\mathcal{G},U_{\mathcal{G}},V_{\mathcal{G}},B,W_{0}), where 𝒢\mathcal{G} specifies the research goal and success criteria, U𝒢​(⋅)U_{\mathcal{G}}(\cdot) denotes the final task utility, V𝒢​(⋅)V_{\mathcal{G}}(\cdot) is the validation signal observable during research, BB specifies the available resource budget, and W0W_{0} is the initial executable workspace. | 高（一手正文；非独立复现） |
| 科学对象或研究任务由正文明确指出。 | 科学对象或研究任务由正文明确指出。 | TXT line 866；核验TXT行号 866 | This stage gate is triggered automatically by a task‑specific result signal. In addition, Executable-State Transition through Re-Anchoring (ESTRA) governs transitions between research segments by selecting the next anchor state and an extend-or-redirect direction. | 高（一手正文；非独立复现） |
| 方法包含任务路由、执行和结果处理。 | 方法包含任务路由、执行和结果处理。 | TXT line 1036；核验TXT行号 1036 | If αn,j≠∅\alpha_{n,j}\neq\varnothing, ScienceFlow executes the action, producing an observation on,jo_{n,j} and an updated workspace: | 高（一手正文；非独立复现） |
| 作者设置了对照或独立验证。 | 作者设置了对照或独立验证。 | TXT line 1070；核验TXT行号 1070 | Independently of the local interaction policy, ScienceFlow monitors the updated workspace for a task-specific result signal specified by the task adapter. Upon detection, the stage gate collects the result, invokes the evaluator to obtain validation evidence, and requests a compact progress summary from the worker. It then snapshots the workspace as Wv=Snapshot⁡(Wn,j+1)W_{v}=\operatorname{Snapshot}(W_{n,j+1}), records the associated memory mvm_{v}, validation evidence eve_{v}, and resource records ℓv\ell_{v}, and inserts the resulting state sv=(Wv,mv,ev,ℓv)s_{v}=(W_{v},m_{v},e_{v},\ell_{v}) into the archive 𝒜n\mathcal{A}_{n}. Temporary stage-gate exchanges are excluded from the segment-local history hn,j+1h_{n,j+1}, and the worker resumes forward research within the same segment. | 高（一手正文；非独立复现） |
| 正文报告可核对的结果或系统贡献。 | 正文报告可核对的结果或系统贡献。 | TXT line 1499；核验TXT行号 1499 | We evaluate ScienceFlow across three classes of executable research tasks: machine learning engineering, mathematical optimization, and scientific modeling, covering substantially different forms of long-horizon research. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出ScienceFlow长时程研究Agent，以可执行工作区状态为研究进展的基础，支持状态归档、路径回退或转向、资源控制。作者在ML工程、数学优化和科学建模三类任务上评估，涵盖多种超长任务执行与信息处理。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。论文设定了可检验的科研目标或学术问题。
  - 原文位置：TXT line 830；核验TXT行号 830；引文：Each executable state sv∈𝒜Ts_{v}\in\mathcal{A}_{T} represents a concrete checkpoint of the evolving research process, including the executable workspace and its associated artifacts, memory, validation evidence, and resource records.
- 多步行动过程：yes。正文实例显示Agent进行了多步任务路径。
  - 原文位置：TXT line 1036；核验TXT行号 1036；引文：If αn,j≠∅\alpha_{n,j}\neq\varnothing, ScienceFlow executes the action, producing an observation on,jo_{n,j} and an updated workspace:
- 至少一种Agent能力：yes。系统使用工具、计划、反馈或多Agent中明确能力。
  - 原文位置：TXT line 864；核验TXT行号 864；引文：ScienceFlow extends conventional tool‑using inference loops to long‑horizon executable research by organizing the process around recoverable executable states. Each state binds an executable workspace with compact memory, validation evidence, and resource records. These states persist across research iterations, providing a common foundation for resuming execution, adapting trajectories, and coordinating physical resources as new evidence accumulates.
- 明确科研流程角色：yes。系统在科研流程中承担研究者、执行者或审查者角色。
  - 原文位置：TXT line 1499；核验TXT行号 1499；引文：We evaluate ScienceFlow across three classes of executable research tasks: machine learning engineering, mathematical optimization, and scientific modeling, covering substantially different forms of long-horizon research.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02 计算机科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

科学模拟和数学优化任务是可验证对象，且系统也引入通用科研Agent系统设计；按对象规则一可同时纳01相关对象。

### 2.3 容易混淆的边界

科学模拟和数学优化任务是可验证对象，且系统也引入通用科研Agent系统设计；按对象规则一可同时纳01相关对象。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM research agent

### 3.2 科研流程角色

研究协调；实验执行

系统中的Agent角色为 ScienceFlow: A long-horizon agent for ML research, scientific discovery and beyond; 输入是分解后的研究目标和成功标准；worker在可执行workspace内推理并调用工具，产生代码、输出与中间状态。任务信号触发stage gate验证并保存checkpoint；ESTRA根据存档证据选择当前状态或历史状态作为锚点，继续或重定向；控制器评估资源状态再决定执行。

### 3.3 自主能力

系统使用工具、计划、反馈或多Agent中明确能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

学术贡献为长期研究轨迹的保存、重定向、资源调度方法；系统贡献是ScienceFlow框架及工作区、状态存档和证据门控的集成。

### 4.2 系统流程与组件

输入是分解后的研究目标和成功标准；worker在可执行workspace内推理并调用工具，产生代码、输出与中间状态。任务信号触发stage gate验证并保存checkpoint；ESTRA根据存档证据选择当前状态或历史状态作为锚点，继续或重定向；控制器评估资源状态再决定执行。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

评估包含75个MLE-bench、数学优化任务及科学建模任务，使用与基线相同的工具和隔离执行环境，不向Agent暴露held-out评估信息，以多次运行比较现有Agent。

### 5.2 基线、指标与结果

作者在近地小行星优化轨迹报告改善了结果：W01从1746.8935天降到420.2742天，约75.9%，后续到393.229天，比W00最终结果好24.32%。作者亦报告MLEbench完整实验表。

### 5.3 科学贡献与证据强度

学术贡献为长期研究轨迹的保存、重定向、资源调度方法；系统贡献是ScienceFlow框架及工作区、状态存档和证据门控的集成。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

正文在相关工作中将本系统放入自动研究Agent及其评测背景；与相邻自动化研究工作相比，本文主要增加了对应方法或监督机制。

## 7. 局限性与风险

作者限制或讨论中明示的证据见原文结论；阅读者推断是评测任务较窄或规模有限，不宜外推至广泛自主科学发现。

## 8. 对综述写作的价值

学术贡献为长期研究轨迹的保存、重定向、资源调度方法；系统贡献是ScienceFlow框架及工作区、状态存档和证据门控的集成。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文提出ScienceFlow长时程研究Agent，以可执行工作区状态为研究进展的基础，支持状态归档、路径回退或转向、资源控制。作者在ML工程、数学优化和科学建模三类任务上评估，涵盖多种超长任务执行与信息处理。

### 9.2 速记版 pipeline

输入是分解后的研究目标和成功标准；worker在可执行workspace内推理并调用工具，产生代码、输出与中间状态。任务信号触发stage gate验证并保存checkpoint；ESTRA根据存档证据选择当前状态或历史状态作为锚点，继续或重定向；控制器评估资源状态再决定执行。

### 9.3 标注字段汇总

```text
paper_id=ASD-0953
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 在MLEbench等既有基准评测 | “75个MLE-bench” · L101 |
| 验证强度 | V1 基准/内部评测 | 基准得分评价 | “作者在近地小行星优化轨迹报告改善了结果” · L105 |
| 系统自主性 | L2 闭环执行者 | 系统自主规划并迭代研究段 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
