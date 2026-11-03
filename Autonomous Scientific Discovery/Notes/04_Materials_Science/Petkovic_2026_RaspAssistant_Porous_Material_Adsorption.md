# RaspAssistant as an Agentic Framework for Automating Adsorption Simulation Research in Porous Materials

**论文信息**

- ID：ASD-0889
- 标题：RaspAssistant as an Agentic Framework for Automating Adsorption Simulation Research in Porous Materials
- 作者：Petković, Marko; Gooijer, Susanne; Vicent-Luna, José Manuel; Menkovski, Vlado; Calero, Sofía
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.27572
- 一手阅读来源：https://arxiv.org/html/2610.27572
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：RaspAssistant as an Agentic Framework for Automating Adsorption Simulation Research in Porous Materials
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/2610.27572.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 工作流 | 从力场准备、模拟、验证延伸到分离分析。 | Abstract | high |
| Agent分工 | Supervisor分解目标并协调检索、力场、模拟及分析专家；高层Agent规划、执行、验证、修订。 | Methods §4 | high |
| 工具 | 调用RASPA 2.0.47与RUPTURA；模拟输出转换为结构化JSON。 | Methods §4 | high |
| 验证基准 | 四项吸附/分离研究，各三次multi-agent复现，共12次；均分9.13/10。 | Results §2.1 | high |
| 对象结果 | 力场诊断修订；CO2力场经MFI实验验证后筛选197种纯硅沸石。 | Abstract/Results | high |

## 0. 摘要翻译

RaspAssistant是层级多Agent框架，将多孔材料吸附研究从力场准备延伸至验证及下游分离分析。Supervisor分解自然语言目标并协调文献检索、力场准备、模拟设置/执行和分析专家；上层Agent计划、执行、验证、修订，使用RASPA和RUPTURA。评测含4项已发表研究的12次多Agent复现运行，平均综合分9.13/10；另有8例力场提取基准。在开放研究中诊断并修改乙炔力场，验证CO2力场后筛查197种纯硅沸石。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
全文显示多Agent分解任务、调用模拟工具、验证结果并迭代修订，承担吸附/分离计算研究角色且有明确多孔材料对象。

### 1.2 排除风险检查

MOF/沸石是多孔功能材料，直接研究孔结构和吸附/分离功能，归04.03；吸附质是探针，未以反应或合成为研究对象，不加03。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不替代多模块事实）
- 模块内分类路径：04.03
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

四项研究：TAMOF-1 CO2/N2、开放金属位MOF乙炔分离、M-MOF-74金属中心效应、离子交换沸石烯烃/烷烃分离；12次multi-agent复现评分8.50–10.00/10，均分9.13；力场提取benchmark均分0.967；CO2力场对MFI实验验证后筛197种纯硅沸石。

### 2.3 容易混淆的边界

MOF/沸石是多孔功能材料，直接研究孔结构和吸附/分离功能，归04.03；吸附质是探针，未以反应或合成为研究对象，不加03。

## 3. Agent 系统与科研流程角色

全文显示多Agent分解任务、调用模拟工具、验证结果并迭代修订，承担吸附/分离计算研究角色且有明确多孔材料对象。

科研流程与自主能力以本文实际行动和工具调用为依据：

Supervisor接收自然语言目标和结构/实验/力场文件；协调检索、力场准备、RASPA模拟、输出转换和分析；下级Agent可编辑文件、运行计算、验证并重做；RUPTURA处理混合物和突破分析；共享记忆保存上下文。

## 4. 方法设计

### 4.1 方法动机与设计

自动协调吸附模拟全流程，并将力场诊断、实验校验和分离分析纳入科研工作流。

### 4.2 系统流程与组件

Supervisor接收自然语言目标和结构/实验/力场文件；协调检索、力场准备、RASPA模拟、输出转换和分析；下级Agent可编辑文件、运行计算、验证并重做；RUPTURA处理混合物和突破分析；共享记忆保存上下文。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

四项研究：TAMOF-1 CO2/N2、开放金属位MOF乙炔分离、M-MOF-74金属中心效应、离子交换沸石烯烃/烷烃分离；12次multi-agent复现评分8.50–10.00/10，均分9.13；力场提取benchmark均分0.967；CO2力场对MFI实验验证后筛197种纯硅沸石。

### 5.2 基线、指标与结果

四项研究：TAMOF-1 CO2/N2、开放金属位MOF乙炔分离、M-MOF-74金属中心效应、离子交换沸石烯烃/烷烃分离；12次multi-agent复现评分8.50–10.00/10，均分9.13；力场提取benchmark均分0.967；CO2力场对MFI实验验证后筛197种纯硅沸石。

### 5.3 科学贡献与证据强度

自动协调吸附模拟全流程，并将力场诊断、实验校验和分离分析纳入科研工作流。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与通用材料模拟Agent相邻；本篇对象为MOF和沸石孔材料的吸附/分离性能。

## 7. 局限性与风险

研究人员仍需提供目标/输入并评估物理模型和结论；存在归一化错误、收敛证据不足及重复计算；分数由单一人工评审者给出。

## 8. 对综述写作的价值

压测多孔材料、吸附/混合物分离与模拟Agent分类边界。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent执行多孔材料吸附模拟

### 9.2 速记版 pipeline

Supervisor接收自然语言目标和结构/实验/力场文件；协调检索、力场准备、RASPA模拟、输出转换和分析；下级Agent可编辑文件、运行计算、验证并重做；RUPTURA处理混合物和突破分析；共享记忆保存上下文。

### 9.3 标注字段汇总

```text
paper_id=ASD-0889
inclusion_status=included
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.03
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/04_Materials_Science/ASD-0889_RaspAssistant_as_an_Agentic_Framework_for_Automating_Adsorption_Simulation_Research_in_Porous_Materials.pdf`，共50页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2610.27572
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 执行多孔材料吸附模拟并筛选沸石，答案可由模拟核对 | “CO2力场对MFI实验验证后筛197种纯硅沸石” · L61 |
| 验证强度 | V2 计算/仿真/回顾性 | 计算验证，12次复现均分9.13/10 | “12次multi-agent复现评分8.50–10.00/10，均分9.13” · L61 |
| 系统自主性 | L2 闭环执行者 | 系统协调从力场准备到分离分析的全流程 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
