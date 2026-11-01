# SciExam for ENSO: Can AI Agents Build Climate Models?

**论文信息**

- ID：ASD-0907
- 标题：SciExam for ENSO: Can AI Agents Build Climate Models?
- 作者：Zhang, Yinling; Liu, Langchen; Xiu, Dongbin; Zou, Xueyan; Kuang, Xu; Wang, Mengdi; Liu, Shilong
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.10513
- 一手阅读来源：https://arxiv.org/abs/2610.10513
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：SciExam for ENSO: Can AI Agents Build Climate Models?
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/2610_10513.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 任务要求Agent从真实观测构建ENSO低阶随机模型，而非只回答知识题。 | 全文任务描述将输入设为观测记录，产出为可执行的时间步进模型。 | §3.1 Scientific Modeling Task | high |
| Agent具有多步、反馈驱动研究流程。 | 先处理观测、选择诊断并冻结诊断，再依据其结果构建模型。 | §3.2 Agent Workflow | high |
| 评测包含多种科学有效性检验。 | 全文列出ENSO统计特征、动力一致性/变量重建和预测能力等检验，不以单一已知答案评分。 | §3.3 Scientific Evaluation及附录C | high |
| 评测对象和比较规模明确。 | 跨12个Agent系统运行；摘要报告6个系统超过已发表参考模型。 | §3.4 Experimental Setup / §4 Results | high |
| 结果涉及气候科学争议而不只模型拟合。 | 作者分析较优模型的简化形式与ENSO暖冷不对称机制的竞争解释之间的相容性。 | §5.1 Agent-Built Models Reenact the ENSO Mechanism Debate | high |
| 作者检查了记忆污染和外部信息影响。 | 全文对观测数据污染和web access作控制分析，讨论Agent构模受信息输入影响。 | §5.2 Case Study of the Top System | high |

## 0. 摘要翻译

论文提出面向厄尔尼诺—南方涛动（ENSO）气候建模的科学评测：Agent基于真实观测构建低阶随机模型，先处理观测并编写诊断，再依据诊断反馈建模。隐藏评测检验长期统计性质、未观测变量重建和留出年份预测。摘要称测试12种Agent系统，其中6种得分超过已发表模型；较优模型与ENSO暖冷不对称的两种竞争解释相容。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
研究目标是气候科学建模与检验；系统要完成观测分析、诊断设计和模型构建等多步行动，并使用代码/实验接口及诊断反馈迭代，明确承担气候科学研究角色。

### 1.2 排除风险检查

05地球环境的气候系统对象明确。容易与01计算/AI能力评测混淆，但代码和Agent是研究工具，最终对象及验证均为ENSO气候模型，故应落05；未发现独立算法能力实验需另加01。类别风险低，核心强度仍由主控决定。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：05
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：05（仅归档，不替代多模块事实）
- 模块内分类路径：05.02.02
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

- object：ENSO（年际气候变率主模态）及低阶随机气候模型
- baselines：已发表ENSO模型；摘要未给出其题名/全部配置，笔记阶段不补写。
- metrics：长程统计特征、动力耦合/未观测变量重建、留出年份预测的综合评测；按论文附录各实验定义。
- results：摘要报告12个Agent系统中6个得分高于已发表模型，优势主要在重建和预测；不在此复述未核实的具体分数。

### 2.3 容易混淆的边界

05地球环境的气候系统对象明确。容易与01计算/AI能力评测混淆，但代码和Agent是研究工具，最终对象及验证均为ENSO气候模型，故应落05；未发现独立算法能力实验需另加01。类别风险低，核心强度仍由主控决定。

## 3. Agent 系统与科研流程角色

研究目标是气候科学建模与检验；系统要完成观测分析、诊断设计和模型构建等多步行动，并使用代码/实验接口及诊断反馈迭代，明确承担气候科学研究角色。

科研流程与自主能力以本文实际行动和工具调用为依据：

构建带时间预算的Agent建模任务；Agent读取原始观测、编写并冻结自选诊断，再输出模型实现。统一评估器在统计模拟、动力重建/一致性和预测任务中调用提交模型，并进行参考模型比较；另做输入信息与web访问控制分析。

## 4. 方法设计

### 4.1 方法动机与设计

将科学Agent评测推进到开放式气候模型构建：在没有唯一标准答案的情况下，以统计性质、动力一致性与预测能力联合检验生成模型，并分析模型是否触及ENSO科学机制问题。

### 4.2 系统流程与组件

构建带时间预算的Agent建模任务；Agent读取原始观测、编写并冻结自选诊断，再输出模型实现。统一评估器在统计模拟、动力重建/一致性和预测任务中调用提交模型，并进行参考模型比较；另做输入信息与web访问控制分析。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

- object：ENSO（年际气候变率主模态）及低阶随机气候模型
- baselines：已发表ENSO模型；摘要未给出其题名/全部配置，笔记阶段不补写。
- metrics：长程统计特征、动力耦合/未观测变量重建、留出年份预测的综合评测；按论文附录各实验定义。
- results：摘要报告12个Agent系统中6个得分高于已发表模型，优势主要在重建和预测；不在此复述未核实的具体分数。

### 5.2 基线、指标与结果

- object：ENSO（年际气候变率主模态）及低阶随机气候模型
- baselines：已发表ENSO模型；摘要未给出其题名/全部配置，笔记阶段不补写。
- metrics：长程统计特征、动力耦合/未观测变量重建、留出年份预测的综合评测；按论文附录各实验定义。
- results：摘要报告12个Agent系统中6个得分高于已发表模型，优势主要在重建和预测；不在此复述未核实的具体分数。

### 5.3 科学贡献与证据强度

将科学Agent评测推进到开放式气候模型构建：在没有唯一标准答案的情况下，以统计性质、动力一致性与预测能力联合检验生成模型，并分析模型是否触及ENSO科学机制问题。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与固定数据管线上的方程发现/气候模拟基准相关；本作强调Agent须从观测自主选择检查方式并构建模型，评测超越拟合误差。

## 7. 局限性与风险

任务使用简化低阶模型和预定义观测/运行环境；结果受时间预算、Agent harness及评测指标设定影响。单篇预印本结果不能直接证明模型机制正确或形成新气候理论。

## 8. 对综述写作的价值

适合作为Agent从数据处理、诊断到气候建模和验证的前沿案例；支持综述比较开放式模型发现与传统答案型benchmark的差异。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent从观测构建ENSO模型

### 9.2 速记版 pipeline

构建带时间预算的Agent建模任务；Agent读取原始观测、编写并冻结自选诊断，再输出模型实现。统一评估器在统计模拟、动力重建/一致性和预测任务中调用提交模型，并进行参考模型比较；另做输入信息与web访问控制分析。

### 9.3 标注字段汇总

```text
paper_id=ASD-0907
inclusion_status=included
scientific_object_modules=05
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=05
module_taxonomy_codes=05.02.02
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/05_Earth_and_Environmental_Sciences/ASD-0907_SciExam_for_ENSO_Can_AI_Agents_Build_Climate_Models.pdf`，共28页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2610.10513.pdf
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。
