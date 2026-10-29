# MacroRisk-agent: a retrieval-augmented multi-agent framework with deterministic validation gates for auditable stress testing

**论文信息**

- ID：ASD-1120
- 标题：MacroRisk-agent: a retrieval-augmented multi-agent framework with deterministic validation gates for auditable stress testing
- 作者：Yan Liu; Junyi Shangguan; Qianyi Wang; Shangfei Xu
- 年份：2026
- 来源 / venue：Scientific Reports
- DOI / arXiv / URL：https://doi.org/10.1038/s41598-026-73453-3
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1120.txt
- PDF / 本地文件路径：Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Liu_2026_MacroRisk_agent_a_retrieval_augmented_multi_agent_framework_with_ASD1120.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究对象与任务 | MacroRisk-Agent将检索增强多代理架构用于宏观金融压力测试，针对结构化输出幻觉、语义推理与数值模拟衔接及流程审计等问题，设置确定性验证门。代理检索情景依据、协调压力情景构造和数值计算，并以机器可检查规则验证结果，支持复现和监管追踪。 | 全文TXT第243行；核验TXT行号 243 | tecture where (i) scenario generation is grounded via retrieval and validation gates, (ii) simulation and analytics | 高（一手正文；非独立复现） |
| 系统输入及处理流程 | 检索代理获取宏观风险材料，分析代理生成压力情景和参数，计算代理调用确定性模拟，验证代理检查结构、约束及数值一致性；失败结果触发修订并保留审计记录。 | 全文TXT第974行；核验TXT行号 974 | with a fixed seed. Baseline factor and dependence parameters are estimated using data through December 2019. | 高（一手正文；非独立复现） |
| 实验或验证设置 | 检索代理获取宏观风险材料，分析代理生成压力情景和参数，计算代理调用确定性模拟，验证代理检查结构、约束及数值一致性；失败结果触发修订并保留审计记录。 | 全文TXT第1448行；核验TXT行号 1448 | reported mean±std (or proportion) and the scenario count n; bootstrap intervals are clustered by scenario family. | 高（一手正文；非独立复现） |
| 作者报告的贡献 | 验证重点是输出结构有效性、确定性数值结果一致性、可追溯性及压力测试案例表现。 | 全文TXT第1916行；核验TXT行号 1916 | Table 13 RQ3: Counterfactual Intervention Effectiveness (Suite C; 50 scenarios). Pre/post metrics for different intervention bundles. inline-eq-IEq339% shows improvement. | 高（一手正文；非独立复现） |
| 适用范围与边界 | 研究对象为宏观金融风险情景和压力测试，属经济金融研究应用；多代理流程清楚，但是否作为自主科研Agent而非决策支持需主控边界裁定。 | 全文TXT第2438行；核验TXT行号 2438 | Discrimination quality. The 0.93 AUC-ROC measures ranking and discrimination, not probabilistic calibra­ | 高（一手正文；非独立复现） |

## 0. 摘要翻译

MacroRisk-Agent将检索增强多代理架构用于宏观金融压力测试，针对结构化输出幻觉、语义推理与数值模拟衔接及流程审计等问题，设置确定性验证门。代理检索情景依据、协调压力情景构造和数值计算，并以机器可检查规则验证结果，支持复现和监管追踪。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。MacroRisk-Agent将检索增强多代理架构用于宏观金融压力测试，针对结构化输出幻觉、语义推理与数值模拟衔接及流程审计等问题，设置确定性验证门。代理检索情景依据、协调压力情景构造和数值计算，并以机器可检查规则验证结果，支持复现和监管追踪。
  - 原文位置：全文TXT第243行；核验TXT行号 243；引文：tecture where (i) scenario generation is grounded via retrieval and validation gates, (ii) simulation and analytics
- 多步行动过程：yes。检索代理获取宏观风险材料，分析代理生成压力情景和参数，计算代理调用确定性模拟，验证代理检查结构、约束及数值一致性；失败结果触发修订并保留审计记录。
  - 原文位置：全文TXT第974行；核验TXT行号 974；引文：with a fixed seed. Baseline factor and dependence parameters are estimated using data through December 2019.
- 至少一种Agent能力：yes。检索代理获取宏观风险材料，分析代理生成压力情景和参数，计算代理调用确定性模拟，验证代理检查结构、约束及数值一致性；失败结果触发修订并保留审计记录。
  - 原文位置：全文TXT第1448行；核验TXT行号 1448；引文：reported mean±std (or proportion) and the scenario count n; bootstrap intervals are clustered by scenario family.
- 明确科研流程角色：yes。研究对象为宏观金融风险情景和压力测试，属经济金融研究应用；多代理流程清楚，但是否作为自主科研Agent而非决策支持需主控边界裁定。
  - 原文位置：全文TXT第1916行；核验TXT行号 1916；引文：Table 13 RQ3: Counterfactual Intervention Effectiveness (Suite C; 50 scenarios). Pre/post metrics for different intervention bundles. inline-eq-IEq339% shows improvement.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：11
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：11（仅归档，不覆盖其他模块）
- 模块内分类路径：11.01 经济学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

研究对象为宏观金融风险情景和压力测试，属经济金融研究应用；多代理流程清楚，但是否作为自主科研Agent而非决策支持需主控边界裁定。

### 2.3 容易混淆的边界

研究对象为宏观金融风险情景和压力测试，属经济金融研究应用；多代理流程清楚，但是否作为自主科研Agent而非决策支持需主控边界裁定。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签



### 3.2 科研流程角色



检索代理获取宏观风险材料，分析代理生成压力情景和参数，计算代理调用确定性模拟，验证代理检查结构、约束及数值一致性；失败结果触发修订并保留审计记录。

### 3.3 自主能力

检索代理获取宏观风险材料，分析代理生成压力情景和参数，计算代理调用确定性模拟，验证代理检查结构、约束及数值一致性；失败结果触发修订并保留审计记录。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

研究对象为宏观金融风险情景和压力测试，属经济金融研究应用；多代理流程清楚，但是否作为自主科研Agent而非决策支持需主控边界裁定。

### 4.2 系统流程与组件

检索代理获取宏观风险材料，分析代理生成压力情景和参数，计算代理调用确定性模拟，验证代理检查结构、约束及数值一致性；失败结果触发修订并保留审计记录。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

检索代理获取宏观风险材料，分析代理生成压力情景和参数，计算代理调用确定性模拟，验证代理检查结构、约束及数值一致性；失败结果触发修订并保留审计记录。 验证以文中所列任务、数据和对照为准。

### 5.2 基线、指标与结果

验证重点是输出结构有效性、确定性数值结果一致性、可追溯性及压力测试案例表现。

### 5.3 科学贡献与证据强度

研究对象为宏观金融风险情景和压力测试，属经济金融研究应用；多代理流程清楚，但是否作为自主科研Agent而非决策支持需主控边界裁定。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与一般LLM代理、科学工作流自动化及该领域既有基准/模型相关；本文的具体差异见上述任务设计和验证设置。

## 7. 局限性与风险

本文结果受其数据、模拟环境、评测指标和实验预算限制；不得将基准或仿真表现直接外推为真实部署成效。

## 8. 对综述写作的价值

可用于综述讨论该类Agent的研究对象、工作流角色和验证边界。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

MacroRisk-Agent将检索增强多代理架构用于宏观金融压力测试，针对结构化输出幻觉、语义推理与数值模拟衔接及流程审计等问题，设置确定性验证门。代理检索情景依据、协调压力情景构造和数值计算，并以机器可检查规则验证结果，支持复现和监管追踪。

### 9.2 速记版 pipeline

检索代理获取宏观风险材料，分析代理生成压力情景和参数，计算代理调用确定性模拟，验证代理检查结构、约束及数值一致性；失败结果触发修订并保留审计记录。

### 9.3 标注字段汇总

```text
paper_id=ASD-1120
inclusion_status=to_read
scientific_object_modules=11
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=11
module_taxonomy_codes=11.01
source_level=first_hand_full_text
fulltext_followup_required=true
```

### 全文后续要求

当前纳入和分类证据已足够；第7节明确的结果/复现细节仍需继续回查。


## 2026-10-29 三级分类复核

- 归档分类：`11.01.04` 金融学；二级：`11.01`。
- 原文位置：PDF p.1。
- 判定：金融压力、追加保证金与抛售流动性反馈模拟，归金融学。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
