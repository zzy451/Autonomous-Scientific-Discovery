# Auditing Discovery Claims: A Two-Sided Criterion for Agentic Science, with the Negative Side Decidable

**论文信息**

- ID：ASD-0874
- 标题：Auditing Discovery Claims: A Two-Sided Criterion for Agentic Science, with the Negative Side Decidable
- 作者：Chen, Wenhui; Chen, Jianlin; Lin, Ziyao; Vong, Chi Man
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2608.00981
- 一手阅读来源：https://arxiv.org/abs/2608.00981
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：Auditing Discovery Claims: A Two-Sided Criterion for Agentic Science, with the Negative Side Decidable
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/2608.00981.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| RNA pseudoknot设计为具体对象。 | 系统针对crossing base-pair RNA targets。 | 全文摘要及RNA实验节 | high |
| 能力审计分为正负两侧。 | 负面界限可形式判定，正面判断需经验oracle。 | 全文贡献与方法节 | high |
| 单一oracle下43/60成功。 | 所优化预测器判定43个设计成功。 | 全文摘要及结果 | high |
| 多预测器下只有1/60通过。 | 三种预测器的交叉验证揭示oracle依赖。 | 全文摘要及结果 | high |
| 外部预测器检验弱于MFE基线。 | 同一43个目标中分别确认2与26个设计，报告p=8e-7。 | 全文配对实验 | high |
| 作者明确限制机制结论。 | 机制与迁移性未证实，panel存在预测器相关问题。 | 全文讨论 | medium |

## 0. 摘要翻译

论文提出审计AI-for-science系统能力增长的双侧标准，并以RNA pseudoknot/crossing base-pair设计检验可判定负界限和外部验证。单一优化预测器下的成功率明显高于多预测器交叉验证；作者指出评估panel相关、程序机制迁移未证实。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
Agent通过搜索生成程序、调用RNA结构预测器并依据外部反馈评估，执行多步科学序列设计与能力审计。

### 1.2 排除风险检查

具体对象为RNA序列及二级结构，建议06.01.03分子生物学。RNA对象上有设计和验证任务，不能归01.04。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不替代多模块事实）
- 模块内分类路径：06.01.03
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

优化预测器下43/60 targets成功，三个预测器下1/60；未见预测器对同一43个确认2个，MFE solver确认26个。另有951 paired units程序比较，作者称机制及迁移性尚未证明。

### 2.3 容易混淆的边界

具体对象为RNA序列及二级结构，建议06.01.03分子生物学。RNA对象上有设计和验证任务，不能归01.04。

## 3. Agent 系统与科研流程角色

Agent通过搜索生成程序、调用RNA结构预测器并依据外部反馈评估，执行多步科学序列设计与能力审计。

科研流程与自主能力以本文实际行动和工具调用为依据：

提出双侧能力审计；形式化pseudoknot-free oracle的可达目标边界；Agent搜索并生成RNA设计程序，以训练所用与外部预测器评测。

## 4. 方法设计

### 4.1 方法动机与设计

区分形式可判定的负面能力边界与需外部验证的正向能力，揭示单一预测器可能高估RNA设计成功。

### 4.2 系统流程与组件

提出双侧能力审计；形式化pseudoknot-free oracle的可达目标边界；Agent搜索并生成RNA设计程序，以训练所用与外部预测器评测。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

优化预测器下43/60 targets成功，三个预测器下1/60；未见预测器对同一43个确认2个，MFE solver确认26个。另有951 paired units程序比较，作者称机制及迁移性尚未证明。

### 5.2 基线、指标与结果

优化预测器下43/60 targets成功，三个预测器下1/60；未见预测器对同一43个确认2个，MFE solver确认26个。另有951 paired units程序比较，作者称机制及迁移性尚未证明。

### 5.3 科学贡献与证据强度

区分形式可判定的负面能力边界与需外部验证的正向能力，揭示单一预测器可能高估RNA设计成功。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与自改进科学Agent评测、oracle gaming检验及RNA结构预测基准相关。

## 7. 局限性与风险

预测器共享参数导致相关；测试split非结构独立；执行噪声与方法效应相近；search-free probe解释了大部分headline effect。

## 8. 对综述写作的价值

提供Agent发现能力的严格审计实例，适用于讨论oracle leakage与能力归因。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

以外部验证审计RNA发现主张

### 9.2 速记版 pipeline

提出双侧能力审计；形式化pseudoknot-free oracle的可达目标边界；Agent搜索并生成RNA设计程序，以训练所用与外部预测器评测。

### 9.3 标注字段汇总

```text
paper_id=ASD-0874
inclusion_status=included
scientific_object_modules=06
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.01.03
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/06_Life_Sciences/ASD-0874_Auditing_Discovery_Claims_A_Two_Sided_Criterion_for_Agentic_Science_with_the_Negative_Side_Decidable.pdf`，共51页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2608.00981
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O4 需物理检验 | 设计RNA pseudoknot序列，需预测器或实验检验 | “crossing base-pair RNA targets” · L25 |
| 验证强度 | V2 计算/仿真/回顾性 | 计算验证，但作者明确指出单一预测器可能高估成功 | “三个预测器下1/60” · L62 |
| 系统自主性 | L2 闭环执行者 | 系统优化并生成RNA设计，但在预测器指导下 | — |

- 强验证（V3–V4）：否
- 置信度：low；需全文复核：是；争议记录：无
- 复核状态：待专家复核：低置信度；需全文复核
