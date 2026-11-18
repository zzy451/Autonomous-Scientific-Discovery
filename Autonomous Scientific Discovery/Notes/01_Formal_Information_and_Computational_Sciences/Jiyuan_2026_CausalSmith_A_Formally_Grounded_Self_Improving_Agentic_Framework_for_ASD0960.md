# CausalSmith: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference

**论文信息**

- ID：ASD-0960
- 标题：CausalSmith: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference
- 作者：Tan, Jiyuan; Syrgkanis, Vasilis
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2607.22511
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0960.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Jiyuan_2026_CausalSmith_A_Formally_Grounded_Self_Improving_Agentic_Framework_for_ASD0960.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入判断：论文直接研究科研Agent或其评测。 | 论文提出CausalSmith，面向因果推断理论研究，以Lean 4机器核验证明，并通过声明审计核对形式化定理与自然语言主张。基础库Causalean包含8,179条机器检查定义和定理。 | TXT line 336；核验TXT行号 336 | Automating theoretical research requires generating candidate results and evaluating them reliably. Models keep getting better at the first, while the second remains hard. A common approach asks one large language model (LLM) to review what another produced, yet such reviewers are empirically unreliable: they may accept fabricated papers and catch the fabrication at close to chance rates [21]. We present CausalSmith, a framework for automated theoretical research in causal inference built on the Lean proof assistant, where a proof is checked by a program rather than read by a referee. | 高（一手正文；非独立复现） |
| 对象证据：正文界定科学问题及研究对象。 | 论文形式化因果推断中的干预效应、识别及统计估计问题，科学对象属于数学统计，依01.01.09统计学归类。文本明确将平均处理效应等因果估计量及识别问题作为形式化对象。 | TXT lines 806–811；核验TXT行号 807 | one per treatment level, and write causal estimands—the average treatment effect, the effect on the treated, difference-in-differences, the local average treatment effect—as functionals of their joint distribution. An estimand is identified when it is a function of the observational distribution alone and partially identified when the data determine only a set containing it, as with Manski or Balke–Pearl bounds. | 高（一手正文；非独立复现） |
| 方法证据：全文描述Agent操作或评测流程。 | 作者建设因果推断Lean基础库，再运行自动科研流水线，组合选题、结论生成、形式化、证明、机器核验和声明审计；评估依据自主运行日志并审查正确性、新颖性及证明完成度。 | TXT line 404；核验TXT行号 336 | Moreover, the pipeline pairs Lean verification with a statement audit that compares each formal theorem against the informal claim behind it. | 高（一手正文；非独立复现） |
| 验证证据：实验报告任务、数据与验证设计。 | 14次运行被接收，且均属gap-filling类。Lean机器检查证明有效性，声明审计补足“证明了什么”的核对。 | TXT line 2068；核验TXT行号 2068 | The run record holds 144144 runs, distributed across three outcomes (Table 5). A run is accepted only when it is sound, novel at its requested publishable tier, and proved to completion in Lean 4; fourteen runs meet this bar. | 高（一手正文；非独立复现） |
| 结果贡献：正文报告可核查结果和贡献。 | 研究对象为因果推断理论，但主要贡献是形式化自动研究框架，归入01一般方法。 | TXT line 2533；核验TXT行号 2533 | Our current evaluation has the following limitations. First, research quality is rated by the pipeline itself, and these LLM ratings do not have independent human validation. Second, the statement-match audit is itself an LLM task; frontier models handled it well in our observations, but we do not estimate how often they err. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出CausalSmith，面向因果推断理论研究，以Lean 4机器核验证明，并通过声明审计核对形式化定理与自然语言主张。基础库Causalean包含8,179条机器检查定义和定理。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。正文提出科学研究或科学评测目标。
  - 原文位置：TXT line 336；核验TXT行号 336；引文：Automating theoretical research requires generating candidate results and evaluating them reliably. Models keep getting better at the first, while the second remains hard. A common approach asks one large language model (LLM) to review what another produced, yet such reviewers are empirically unreliable: they may accept fabricated papers and catch the fabrication at close to chance rates [21]. We present CausalSmith, a framework for automated theoretical research in causal inference built on the Lean proof assistant, where a proof is checked by a program rather than read by a referee.
- 多步行动过程：yes。正文描述多阶段行动及反馈流程。
  - 原文位置：TXT line 336；核验TXT行号 336；引文：Around it we build a self-improving agentic pipeline that selects research topics, proposes results, formalizes statements, constructs proofs, and presents the resulting artifacts for human inspection.
- 至少一种Agent能力：yes。正文显示Agent使用工具、状态或证据进行决策。
  - 原文位置：TXT line 404；核验TXT行号 336；引文：Moreover, the pipeline pairs Lean verification with a statement audit that compares each formal theorem against the informal claim behind it.
- 明确科研流程角色：yes。系统承担科研执行、理论发现或科研评价角色。
  - 原文位置：TXT line 2068；核验TXT行号 2068；引文：The run record holds 144144 runs, distributed across three outcomes (Table 5). A run is accepted only when it is sound, novel at its requested publishable tier, and proved to completion in Lean 4; fourteen runs meet this bar.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.01.09 统计学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

研究对象不是泛化Agent能力，而是因果推断和统计估计量的形式化证明；形式化工具为Lean，领域对象是统计理论，故归入01.01.09。

### 2.3 容易混淆的边界

研究对象不是泛化Agent能力，而是因果推断和统计估计量的形式化证明；形式化工具为Lean，领域对象是统计理论，故归入01.01.09。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

语言模型Agent；工具增强Agent

### 3.2 科研流程角色

科学规划；理论推导；结果验证

CausalSmith从选题和文献检索开始，提出候选结果，将声明形式化为Lean定理并构造证明；Lean检查证明，声明审计核对定理与原主张，最后整理产物供人检查。运行图保存依赖及失败反馈。

### 3.3 自主能力

正文显示Agent使用工具、状态或证据进行决策。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

本文以Lean验证取代单纯LLM审稿，并将证明正确性和自然语言声明忠实度分开处理。

### 4.2 系统流程与组件

作者建设因果推断Lean基础库，再运行自动科研流水线，组合选题、结论生成、形式化、证明、机器核验和声明审计；评估依据自主运行日志并审查正确性、新颖性及证明完成度。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

评估汇总144次运行；被接收结果须正确、达到指定新颖性等级且Lean证明完成。作者还深入分析ATE minimax结果及知识库反馈案例。

### 5.2 基线、指标与结果

14次运行被接收，且均属gap-filling类。Lean机器检查证明有效性，声明审计补足“证明了什么”的核对。

### 5.3 科学贡献与证据强度

本文以Lean验证取代单纯LLM审稿，并将证明正确性和自然语言声明忠实度分开处理。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

作者指出研究质量由系统内LLM评价，缺少独立人工验证；声明审计本身也是LLM任务，错误率未估计。

## 7. 局限性与风险

研究对象为因果推断理论，但主要贡献是形式化自动研究框架，归入01一般方法。

## 8. 对综述写作的价值

CausalSmith以Lean库和自我改进Agent流水线自动提出并证明因果推断定理，再审计声明忠实度；144次运行中14次达到作者定义的接收标准。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

CausalSmith以Lean库和自我改进Agent流水线自动提出并证明因果推断定理，再审计声明忠实度；144次运行中14次达到作者定义的接收标准。

### 9.2 速记版 pipeline

作者建设因果推断Lean基础库，再运行自动科研流水线，组合选题、结论生成、形式化、证明、机器核验和声明审计；评估依据自主运行日志并审查正确性、新颖性及证明完成度。

### 9.3 标注字段汇总

```text
paper_id=ASD-0960
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.01.09
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O5 开放数学 | 自主生成因果推断理论新结果并以Lean形式化验证 | “面向因果推断理论研究，以Lean 4机器核验证明” · L29 |
| 验证强度 | V4 证明/复现 | Lean机器检查每个定理证明，提供形式化验证 | “14次运行被接收，且均属gap-filling类。Lean机器检查证明有效性” · L105 |
| 系统自主性 | L2 闭环执行者 | 系统在人给定因果推断领域内自主选题、证明和迭代 | — |

- 强验证（V3–V4）：是
- 置信度：medium；需全文复核：否；争议记录：无
- 复核状态：无需复核
