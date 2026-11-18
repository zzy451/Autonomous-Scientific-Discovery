# CosmoAgent: AI Agent for Theoretical Cosmology

**论文信息**

- ID：ASD-1058
- 标题：CosmoAgent: AI Agent for Theoretical Cosmology
- 作者：Stephon Alexander; Loukas Gouskos; Savvas M. Koushiappas; Cooper Niu; Wenrong Sun
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.16536
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1058.txt
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Alexander_2026_CosmoAgent_AI_Agent_for_Theoretical_Cosmology_ASD1058.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 宇宙学目标 | 系统搜索暗能量与修正引力理论。 | Abstract；核验TXT行号 311 | We present CosmoAgent, an agentic AI framework using large language models (LLMs) to search for dark-energy and modified-gravity models. | 高（一手正文；非独立复现） |
| 理论生成 | 协变语法限定并组织修正引力拉格朗日量空间。 | Abstract；核验TXT行号 311 | We define a covariant grammar that allows LLM agents to explore the space of modified-gravity Lagrangians. | 高（一手正文；非独立复现） |
| 观测数据 | 管线使用DES五年Ia型超新星和DESI DR2 BAO。 | Abstract；核验TXT行号 311 | including the DES 5-year type Ia supernova sample and the DESI Data Release 2 BAO measurements. | 高（一手正文；非独立复现） |
| 模型比较 | 88个前沿LLM参与基准搜索，理论按AIC平衡复杂度与似然。 | Abstract；核验TXT行号 311 | We benchmarked 88 frontier LLMs from ChatGPT, Claude, Gemini, Kimi, DeepSeek, and Qwen | 高（一手正文；非独立复现） |
| 结论边界 | 报告的AIC小幅改善不足以确认观测偏好。 | Abstract；核验TXT行号 311 | The modest AIC improvements do not establish an observational preference for these models over flat Λ\LambdaCDM. | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | 搜索暗能量、修正引力模型并拟合超新星和BAO宇宙学观测；建议细化为宇宙学，并在修正引力理论对象上标注相对论。 | TXT line 311；核验TXT行号 311 | dark-energy and modified-gravity models. We define a covariant grammar that allows LLM agents to explore the space of modified-gravity Lagrangians. An in-house computational pipeline derives the equations of motion, solves the background dynamics, and evaluate | 高（一手正文；非独立复现） |

## 0. 摘要翻译

CosmoAgent使用LLM搜索暗能量和修正引力模型。协变语法生成受限拉格朗日量候选，计算管线推导运动方程、求解宇宙背景并用晚期宇宙观测数据计算似然，按AIC排序；作者比较88种模型并给出代表性理论结构。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是搜索晚期宇宙加速的暗能量和修正引力模型。
  - 原文位置：Abstract；核验TXT行号 311；引文：We present CosmoAgent, an agentic AI framework using large language models (LLMs) to search for dark-energy and modified-gravity models.
- 多步行动过程：yes。Agent生成候选理论后经方程推导、动力学求解、数据似然和模型比较。
  - 原文位置：Abstract / Methods；核验TXT行号 311；引文：We define a covariant grammar that allows LLM agents to explore the space of modified-gravity Lagrangians.
- 至少一种Agent能力：yes。LLM依据语法探索理论空间并基于AIC更新搜索建议。
  - 原文位置：Section V.3；核验TXT行号 161；引文：AIC-guided proposal updates
- 明确科研流程角色：yes。Agent承担理论宇宙学模型构造、数据比较和搜索分析。
  - 原文位置：Abstract；核验TXT行号 311；引文：We present CosmoAgent, an agentic AI framework using large language models (LLMs) to search for dark-energy and modified-gravity models.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：02
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：02（仅归档，不覆盖其他模块）
- 模块内分类路径：02.01.05 宇宙学；02.02.07 相对论
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

搜索暗能量、修正引力模型并拟合超新星和BAO宇宙学观测；建议细化为宇宙学，并在修正引力理论对象上标注相对论。

### 2.3 容易混淆的边界

搜索暗能量、修正引力模型并拟合超新星和BAO宇宙学观测；建议细化为宇宙学，并在修正引力理论对象上标注相对论。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Planning Agent；Tool-using Agent

### 3.2 科研流程角色

hypothesis_generation；simulation_modeling；tool_use_and_code_execution；data_analysis；result_interpretation；evidence_assessment_and_validation

Agent生成并修订理论候选；程序化理论管线完成方程推导、背景演化、宇宙学可观测量及似然评估；另以多LLM对比搜索，并有随机搜索/参数基线和消融对照。

### 3.3 自主能力

LLM依据语法探索理论空间并基于AIC更新搜索建议。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

宇宙学侧探索了晚期膨胀观测可容许的理论结构；系统侧给出语法约束、物理过滤与似然反馈耦合的理论搜索Agent。

### 4.2 系统流程与组件

定义理论语法与参数范围；Agent提出协变作用量结构和参数；代码推导运动方程并施加背景物理筛选；计算Ia超新星和BAO似然及AIC；基于得分调整候选；将代表模型与平直ΛCDM和搜索基线比较。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

使用DES五年Ia型超新星、DESI DR2 BAO数据；与平直ΛCDM比较；包含随机搜索基线和Agent轨迹/记忆消融，检查理论搜索的可辨识性及接受筛选。

### 5.2 基线、指标与结果

作者报告88种LLM均能找到名义AIC低于平直ΛCDM的理论，最好ΔAIC为−3.328；七种模型重获二次quintessence。作者明确说明小幅改善不足以建立观测偏好。

### 5.3 科学贡献与证据强度

宇宙学侧探索了晚期膨胀观测可容许的理论结构；系统侧给出语法约束、物理过滤与似然反馈耦合的理论搜索Agent。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

不同于纯参数拟合，CosmoAgent可提出作用量结构并通过物理方程管线筛选；与人类理论扫描相比，它对88种LLM作统一框架评估。

## 7. 局限性与风险

AIC名义改善有限且依赖当前数据与模型语法；不能宣称观测证据支持替代ΛCDM。理论筛选结果仍需更多数据和物理一致性审查。

## 8. 对综述写作的价值

可用于综述Agent怎样把物理假设生成连接到宇宙学方程求解和真实观测数据比较。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

CosmoAgent以语法约束和观测反馈搜索宇宙学模型，但报告的AIC优势尚非观测偏好证据。

### 9.2 速记版 pipeline

定义理论语法与参数范围；Agent提出协变作用量结构和参数；代码推导运动方程并施加背景物理筛选；计算Ia超新星和BAO似然及AIC；基于得分调整候选；将代表模型与平直ΛCDM和搜索基线比较。

### 9.3 标注字段汇总

```text
paper_id=ASD-1058
inclusion_status=to_read
scientific_object_modules=02
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=02
module_taxonomy_codes=02.01.05;02.02.07
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 搜索修正引力理论并用晚期宇宙观测数据计算似然，答案可由数值求解和统计检验核对 | “DES 5-year type Ia supernova sample and the DESI Data Release 2 BAO” · L23 |
| 验证强度 | V2 计算/仿真/回顾性 | 计算理论背景动力学并与观测数据拟合，无新的物理实验 | “solves the background dynamics, and evaluate” · L26 |
| 系统自主性 | L2 闭环执行者 | Agent在协变语法约束内自主生成理论候选并迭代筛选 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
