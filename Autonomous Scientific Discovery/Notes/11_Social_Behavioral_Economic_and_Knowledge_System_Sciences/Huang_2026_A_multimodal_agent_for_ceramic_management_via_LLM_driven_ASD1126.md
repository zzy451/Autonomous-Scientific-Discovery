# A multimodal agent for ceramic management via LLM-driven knowledge and visual synergy

**论文信息**

- ID：ASD-1126
- 标题：A multimodal agent for ceramic management via LLM-driven knowledge and visual synergy
- 作者：Yuexin Huang; Bin Du; Jingyan Qin
- 年份：2026
- 来源 / venue：npj Heritage Science
- DOI / arXiv / URL：https://doi.org/10.1038/s40494-026-02868-y
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1126.txt
- PDF / 本地文件路径：Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Huang_2026_A_multimodal_agent_for_ceramic_management_via_LLM_driven_ASD1126.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 考古/文化遗产研究对象 | 系统从陶瓷专家描述提取属性关系，定位釉色转折、开片纹和窑印等器物细节。 | 全文第182行；核验TXT行号 182 | visual alignment with a knowledge graph mounting pipeline, and graph- | 高（一手正文；非独立复现） |
| 多步处理阶段 | 工作流分为离线多模态知识构建与在线查询引导推理。 | 全文第204行；核验TXT行号 204 | overall workﬂow of CeramicAgent is illustrated in Fig. 2. The framework | 高（一手正文；非独立复现） |
| 查询引导的模块协作 | 按查询证据需求组合文本、图像与图谱检索，不是固定单次分类器。 | 全文第253行；核验TXT行号 253 | Unlike a rigid sequential pipeline, CeramicAgent uses query guided | 高（一手正文；非独立复现） |
| 可追溯推理输出 | 推理路径由显式模块证据构成，可供学术核验。 | 全文第220行；核验TXT行号 220 | which is used to retrieve relevant anchor nodes from the knowledge graph. | 高（一手正文；非独立复现） |
| 使用边界 | 系统支持器物组织和 scholarly verification，专业解释仍由专家审核。 | 全文第1718行；核验TXT行号 1718 | qualiﬁed specialists. The case studies illustrate how CeramicAgent can be | 高（一手正文；非独立复现） |

## 0. 摘要翻译

CeramicAgent面向陶瓷遗产管理，融合文本、图像与结构化资料进行属性抽取和证据关联。系统结合模式约束的信息抽取、HQ-SAM高质量视觉分割及知识图谱引导推理，将器物图像局部与历史文本/元数据连接，在故宫陶瓷数据集上验证多模态管理能力。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。系统目标是从陶瓷遗产图像、专家描述与知识图谱中构建可核验的器物属性和历史证据答案。
  - 原文位置：全文第179行；核验TXT行号 179；引文：knowledge-level representations, this paper proposes CeramicAgent, a
- 多步行动过程：yes。离线阶段抽取文本三元组、分割器物图像并构建多模态知识图谱；在线阶段按查询检索、遍历证据路径并生成答案。
  - 原文位置：全文第204行；核验TXT行号 204；引文：overall workﬂow of CeramicAgent is illustrated in Fig. 2. The framework
- 至少一种Agent能力：yes。CeramicAgent根据查询需求协调schema抽取、HQ-SAM图像分割、图谱检索与多跳推理，产出带证据路径的回答。
  - 原文位置：全文第253行；核验TXT行号 253；引文：Unlike a rigid sequential pipeline, CeramicAgent uses query guided
- 明确科研流程角色：yes。该工具支持陶瓷遗产研究与馆藏知识组织，且案例说明其回答可供专业人员核验；属于研究辅助型Agent流程。
  - 原文位置：全文第1718行；核验TXT行号 1718；引文：qualiﬁed specialists. The case studies illustrate how CeramicAgent can be

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：11
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：11（仅归档，不覆盖其他模块）
- 模块内分类路径：11.06.03 考古科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

- 陶瓷器物的形制、釉面、窑印及历史知识关系；博物馆陶瓷遗产数据

### 2.3 容易混淆的边界

陶瓷器物知识抽取、细粒度形貌定位、知识图谱构建及证据路径问答直接支持考古与文化遗产研究，按对象归11.06.03考古科学。系统根据查询需要协调文本抽取、视觉分割和图谱推理，具有多步Agent能力；不能因为对象是文化遗产而将其排除。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签



### 3.2 科研流程角色



输入陶瓷图像、文字记录和结构化知识；抽取器按schema整理属性，HQ-SAM分割定位视觉区域，图谱推理将文本、图像和历史证据关联后生成器物分析结果。

### 3.3 自主能力

CeramicAgent根据查询需求协调schema抽取、HQ-SAM图像分割、图谱检索与多跳推理，产出带证据路径的回答。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

对象是文化遗产数字化与博物馆藏品管理，不是科学发现研究Agent；属领域应用，需依项目是否纳入数字人文/考古对象决定，当前保留needs_review。

### 4.2 系统流程与组件

输入陶瓷图像、文字记录和结构化知识；抽取器按schema整理属性，HQ-SAM分割定位视觉区域，图谱推理将文本、图像和历史证据关联后生成器物分析结果。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

输入陶瓷图像、文字记录和结构化知识；抽取器按schema整理属性，HQ-SAM分割定位视觉区域，图谱推理将文本、图像和历史证据关联后生成器物分析结果。 验证以文中所列任务、数据和对照为准。

### 5.2 基线、指标与结果

在故宫陶瓷数据集评估属性抽取及区域定位，并检查多模态证据关联效果。

### 5.3 科学贡献与证据强度

对象是文化遗产数字化与博物馆藏品管理，不是科学发现研究Agent；属领域应用，需依项目是否纳入数字人文/考古对象决定，当前保留needs_review。

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

CeramicAgent面向陶瓷遗产管理，融合文本、图像与结构化资料进行属性抽取和证据关联。系统结合模式约束的信息抽取、HQ-SAM高质量视觉分割及知识图谱引导推理，将器物图像局部与历史文本/元数据连接，在故宫陶瓷数据集上验证多模态管理能力。

### 9.2 速记版 pipeline

输入陶瓷图像、文字记录和结构化知识；抽取器按schema整理属性，HQ-SAM分割定位视觉区域，图谱推理将文本、图像和历史证据关联后生成器物分析结果。

### 9.3 标注字段汇总

```text
paper_id=ASD-1126
inclusion_status=to_read
scientific_object_modules=11
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=11
module_taxonomy_codes=11.06.03
source_level=first_hand_full_text
fulltext_followup_required=true
```

### 全文后续要求

当前纳入和分类证据已足够；第7节明确的结果/复现细节仍需继续回查。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 陶瓷属性识别在已知数据集上评估 | “ceramic management via LLM-driven knowledge” · L6 |
| 验证强度 | V1 基准/内部评测 | 故宫数据集评估无独立专家验证 | “visual alignment with a knowledge graph” · L21 |
| 系统自主性 | L1 任务助手 | 按查询组合检索模块但人给定问题 | — |

- 强验证（V3–V4）：否
- 置信度：medium；需全文复核：是；争议记录：无
- 复核状态：待专家复核：需全文复核
