# CrossAudit: A Git-Native, Cross-Vendor Audit Loop for Agentic Science

**论文信息**

- ID：ASD-0879
- 标题：CrossAudit: A Git-Native, Cross-Vendor Audit Loop for Agentic Science
- 作者：Dong, Zhaohe; Chen, Yuhao
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2608.28631
- 一手阅读来源：https://arxiv.org/abs/2608.28631
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：CrossAudit: A Git-Native, Cross-Vendor Audit Loop for Agentic Science
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/2608.28631.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 审计逐个科研工作增量进行。 | 异供应商Agent按人工版本化规则检查增量。 | 全文摘要及§2 | high |
| Git保存审计轨迹。 | 报告、裁决、争议以commit记录。 | 全文协议 | high |
| 确定性检查先于模型。 | Agent不得豁免脚本确认的硬失败。 | 全文协议不变量 | high |
| 参考实现含GitHub Actions。 | 实现使用GitHub Actions及数百行Python。 | 全文implementation | high |
| 注入缺陷试验有43个缺陷。 | 30个增量、43个seeded defects，每配置运行一次。 | 全文trial方法与结果 | high |
| 作者拒绝宣称厂商优劣。 | 结果显示规则解读不同，不证明某供应商更好。 | 全文摘要和讨论 | medium |

## 0. 摘要翻译

CrossAudit提出科研流水线持续审计协议：异供应商Agent按人工版本化规则检查每个增量，审查轨迹以Git保存，确定性检查优先，有限修订失败后升级人工。作者实现GitHub Actions方案，并报告化学计算管线部署和注入缺陷试验，但不据此声称供应商优劣。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
CrossAudit要求审计Agent读取规则、检查科研工作增量、指出违反规则之处并触发有限修订循环，属于持续科研流水线监督，不是单轮文本标签任务。

### 1.2 排除风险检查

倾向11.07：审计对象为科研流水线、科学主张和科研质量治理过程。若全文证实协议完全通用且未实际核验科研主张，可改为01.04。计算化学只是部署场景，没有分子/反应实验，不能据此分03。 主控与独立审稿复核§3.1、§3.4、§4.2：多Agent生成、异厂商审计、修订及升级流程满足科研角色；以科学记录和主张审计为实际验证对象，采用11.07。perovskite additive仅部署语境，无添加剂对象结果，暂不加03/04。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：11
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：11（仅归档，不替代多模块事实）
- 模块内分类路径：11.07
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

GitHub Actions/Python参考实现；closely related variant部署于计算化学流水线；注入缺陷实验含30个增量与43个缺陷，每配置一次。作者称结果不能证明任何供应商优越。

### 2.3 容易混淆的边界

倾向11.07：审计对象为科研流水线、科学主张和科研质量治理过程。若全文证实协议完全通用且未实际核验科研主张，可改为01.04。计算化学只是部署场景，没有分子/反应实验，不能据此分03。 主控与独立审稿复核§3.1、§3.4、§4.2：多Agent生成、异厂商审计、修订及升级流程满足科研角色；以科学记录和主张审计为实际验证对象，采用11.07。perovskite additive仅部署语境，无添加剂对象结果，暂不加03/04。

## 3. Agent 系统与科研流程角色

CrossAudit要求审计Agent读取规则、检查科研工作增量、指出违反规则之处并触发有限修订循环，属于持续科研流水线监督，不是单轮文本标签任务。

科研流程与自主能力以本文实际行动和工具调用为依据：

跨供应商审查；人工版本化规则；Git提交保存审计轨迹；确定性脚本先运行；Agent只能引用规则提出阻塞；限定修订轮次后升级人工。

## 4. 方法设计

### 4.1 方法动机与设计

将异厂商Agent审计、可回放记录、确定性规则优先和人工升级组成科研流水线监督协议。

### 4.2 系统流程与组件

跨供应商审查；人工版本化规则；Git提交保存审计轨迹；确定性脚本先运行；Agent只能引用规则提出阻塞；限定修订轮次后升级人工。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

GitHub Actions/Python参考实现；closely related variant部署于计算化学流水线；注入缺陷实验含30个增量与43个缺陷，每配置一次。作者称结果不能证明任何供应商优越。

### 5.2 基线、指标与结果

GitHub Actions/Python参考实现；closely related variant部署于计算化学流水线；注入缺陷实验含30个增量与43个缺陷，每配置一次。作者称结果不能证明任何供应商优越。

### 5.3 科学贡献与证据强度

将异厂商Agent审计、可回放记录、确定性规则优先和人工升级组成科研流水线监督协议。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与AI scientist、多Agent科研流水线、LLM-as-a-judge及软件持续集成审计相关。

## 7. 局限性与风险

每配置仅一次；自有仓库审计破坏盲法；共同语料中的错误会导致审查者共同出错；部署为相近变体且未保存原始模型对话。

## 8. 对综述写作的价值

压力测试11.07是否涵盖科学研究流程治理，以及何时应放入01.04通用方法。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

跨厂商Agent审计科学记录

### 9.2 速记版 pipeline

跨供应商审查；人工版本化规则；Git提交保存审计轨迹；确定性脚本先运行；Agent只能引用规则提出阻塞；限定修订轮次后升级人工。

### 9.3 标注字段汇总

```text
paper_id=ASD-0879
inclusion_status=included
scientific_object_modules=11
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=11
module_taxonomy_codes=11.07
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/ASD-0879_CrossAudit_A_Git_Native_Cross_Vendor_Audit_Loop_for_Agentic_Science.pdf`，共19页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2608.28631
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 在注入缺陷实验的30个增量和43个缺陷上评测审计能力，属于预定义测试 | “30个增量、43个seeded defects” · L29 |
| 验证强度 | V2 计算/仿真/回顾性 | 通过GitHub Actions实现和注入缺陷试验验证，但仅一次配置 | “每配置运行一次” · L29 |
| 系统自主性 | L1 任务助手 | 系统按人工版本化规则检查科研增量，但主要是审计监督而非研究执行 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
