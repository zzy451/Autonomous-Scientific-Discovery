# Omics data discovery agents: Agent-supported retrieval, reanalysis, and synthesis of published omics data

**论文信息**

- ID：ASD-0895
- 标题：Omics data discovery agents: Agent-supported retrieval, reanalysis, and synthesis of published omics data
- 作者：Alexandre Hutton; Jesse G. Meyer
- 年份：2026
- 来源 / venue：PLoS computational biology
- DOI / arXiv / URL：https://doi.org/10.1371/journal.pcbi.1014822
- 一手阅读来源：https://doi.org/10.1371/journal.pcbi.1014822
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：Omics data discovery agents: Agent-supported retrieval, reanalysis, and synthesis of published omics data
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/C_sources/ASD-0895.pdf
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Hutton_2026_Omics_data_discovery_agents.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| Agent具备检索、提取和执行工具链 | agents可fetch studies、extract metadata、identify/download data、execute containerized pipelines、synthesize results。 | 正文Abstract，第2页 | high |
| 系统面向多类组学数据源 | 介绍PRIDE、MassIVE、GEO、SRA及文章/补充材料/仓库的分散元数据。 | 正文Introduction与Methods，第3-5页 | high |
| 实际执行五项重分析 | 5项DDA/DIA proteomics和bulk RNA-seq端到端重分析全部完成。 | 正文Abstract，第2页；Methods，第7-12页 | high |
| 报告数值验证结果 | 样本相关0.85–0.997；fold-change Spearman 0.88–0.91；共同显著特征无方向逆转。 | 正文Abstract，第2页；Results，第12-14页 | high |
| 跨研究验证疾病对象并明确人工指导 | random-effects meta-analysis恢复liver fibrosis一致蛋白调控；五项流程存在文档化的人类指导。 | 正文Abstract，第2页；Discussion，第16-17页 | high |

## 0. 摘要翻译

ODDA使用可调用工具的语言模型 Agent 阅读文献、定位并下载组学数据、运行容器化定量管线、跨研究汇总结果。全文报告5个蛋白质组和RNA-seq重分析均完成，Agent流程需要记录的人类指导；重现作者数据的样本相关系数为0.85–0.997，差异表达fold-change Spearman相关为0.88–0.91，并对肝纤维化蛋白调控进行随机效应meta分析。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
已读19页正式全文。多步工具使用、数据检索、容器执行和结果综合证据充分；摘要和方法均明确流程需要人类指导，故系统自主程度应克制表述。

### 1.2 排除风险检查

06包括蛋白质组、bulk RNA-seq和相关分子数据；07的肝纤维化meta分析是明确疾病对象结果，因此保留07.02.11。数据复用平台的技术属性不能将对象分类降为通用01.04。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不替代多模块事实）
- 模块内分类路径：06.03.02; 07.02.11
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

五项端到端重分析覆盖DDA/DIA蛋白质组与bulk RNA-seq；每项有记录的人类指导。样本丰度相关0.85–0.997、差异表达fold-change Spearman 0.88–0.91；共同显著特征无方向反转；肝纤维化随机效应meta分析恢复一致蛋白调控。文献级数据引用目录是描述性输出，并非准确性验证基准。

### 2.3 容易混淆的边界

06包括蛋白质组、bulk RNA-seq和相关分子数据；07的肝纤维化meta分析是明确疾病对象结果，因此保留07.02.11。数据复用平台的技术属性不能将对象分类降为通用01.04。

## 3. Agent 系统与科研流程角色

已读19页正式全文。多步工具使用、数据检索、容器执行和结果综合证据充分；摘要和方法均明确流程需要人类指导，故系统自主程度应克制表述。

科研流程与自主能力以本文实际行动和工具调用为依据：

ODDA通过MCP server暴露容器化工具；Agent从全文/补充材料/代码中提取样本和参数，识别PRIDE、MassIVE、GEO、SRA等数据，下载数据并运行DIA/蛋白质组或bulk RNA-seq流程，再整合研究结果。全文强调人类指导与逐研究流程适配。

## 4. 方法设计

### 4.1 方法动机与设计

以Agent使分散于论文、补充材料和数据仓库的组学研究可检索、可重分析并可跨研究综合，提供可审计的复用框架。

### 4.2 系统流程与组件

ODDA通过MCP server暴露容器化工具；Agent从全文/补充材料/代码中提取样本和参数，识别PRIDE、MassIVE、GEO、SRA等数据，下载数据并运行DIA/蛋白质组或bulk RNA-seq流程，再整合研究结果。全文强调人类指导与逐研究流程适配。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

五项端到端重分析覆盖DDA/DIA蛋白质组与bulk RNA-seq；每项有记录的人类指导。样本丰度相关0.85–0.997、差异表达fold-change Spearman 0.88–0.91；共同显著特征无方向反转；肝纤维化随机效应meta分析恢复一致蛋白调控。文献级数据引用目录是描述性输出，并非准确性验证基准。

### 5.2 基线、指标与结果

五项端到端重分析覆盖DDA/DIA蛋白质组与bulk RNA-seq；每项有记录的人类指导。样本丰度相关0.85–0.997、差异表达fold-change Spearman 0.88–0.91；共同显著特征无方向反转；肝纤维化随机效应meta分析恢复一致蛋白调控。文献级数据引用目录是描述性输出，并非准确性验证基准。

### 5.3 科学贡献与证据强度

以Agent使分散于论文、补充材料和数据仓库的组学研究可检索、可重分析并可跨研究综合，提供可审计的复用框架。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与生物信息学、开放组学数据再利用和实验可复现性工作相关。相较只做文献摘要或生成分析代码的系统，ODDA实现数据查找、实际定量处理和跨研究结果综合。

## 7. 局限性与风险

依据正式全文。规模化论文索引抽取没有经准确率验证；五项再分析都有人类指导，数据和工具受可获得性、许可及逐案适配约束。作者称其为可行性演示而非完整性能基准。

## 8. 对综述写作的价值

适合展示Agent参与组学数据复现、跨研究验证及疾病机制综合，并可用于讨论人类监督与证据可审计性。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent复用与综合公开组学数据

### 9.2 速记版 pipeline

ODDA通过MCP server暴露容器化工具；Agent从全文/补充材料/代码中提取样本和参数，识别PRIDE、MassIVE、GEO、SRA等数据，下载数据并运行DIA/蛋白质组或bulk RNA-seq流程，再整合研究结果。全文强调人类指导与逐研究流程适配。

### 9.3 标注字段汇总

```text
paper_id=ASD-0895
inclusion_status=included
scientific_object_modules=06;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.02; 07.02.11
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 重分析已发表组学数据，答案可由原作者结果和数据库记录核对 | “五项端到端重分析覆盖DDA/DIA蛋白质组与bulk RNA-seq” · L89 |
| 验证强度 | V2 计算/仿真/回顾性 | 重分析与原作者数据比对，样本相关0.85–0.997，fold-change Spearman 0.88–0.91，属计算验证 | “样本丰度相关0.85–0.997、差异表达fold-change Spearman 0.88–0.91” · L61 |
| 系统自主性 | L1 任务助手 |  | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
