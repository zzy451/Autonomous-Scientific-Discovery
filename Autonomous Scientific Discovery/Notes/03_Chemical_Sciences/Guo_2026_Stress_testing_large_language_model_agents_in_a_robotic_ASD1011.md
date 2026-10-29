# Stress-testing large language model agents in a robotic chemistry laboratory

**论文信息**

- ID：ASD-1011
- 标题：Stress-testing large language model agents in a robotic chemistry laboratory
- 作者：Lulu Guo; Yingkai Sun; Xiaobo Li; Luyao Ge; Ziming Wang; Haitao Zheng; Jingyu Li; Huijuan Zhang; Bingxu Chen; Daobin Liu; Yuebo Liu; Jie Li; Xiaohui Li; Linjiang Chen; Yi Luo; Jun Jiang
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2607.23045
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1011.txt
- PDF / 本地文件路径：Reference_PDF/03_Chemical_Sciences/Guo_2026_Stress_testing_large_language_model_agents_in_a_robotic_ASD1011.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| scientific object/task | 研究对象是LLM Agent在机器人化学实验室中把科研意图转成实体实验行动的能力；该文通过物理执行评估科研自主性。 | Full text, extracted character offset 1010；核验TXT行号 14 | Here, we use a robotic chemistry laboratory as a physical-world testbed to make scientific agency measurable | 高（一手正文；非独立复现） |
| method or agent workflow | Agent需在设备、参数、样品和容器约束下形成连贯计划，并根据连续实验轮次调整行动，属于多步实验闭环。 | Full text, extracted character offset 2177；核验TXT行号 27 | Agents must produce executable actions that respect constraints imposed by instruments, operating parameters, samples and vessels, while maintaining coherent plans and adapting across successive experimental rounds | 高（一手正文；非独立复现） |
| evaluation design | 评估在45个模块化工作站上运行4,608次试验，按实验室约束检查生成流程是否可执行。 | 本地原文 TXT 第15行 | Its 45 modular workstations exposed as machine-readable skills enabled 4,608 trials. | 高（一手正文；非独立复现） |
| reported result | 结果显示只有少数试验产生经专家判定可执行的工作流，量化了当前实体实验执行能力的边界。 | Full text, extracted character offset 1207；核验TXT行号 16 | Only 3.3% of trials produced expert-assessed executable workflows | 高（一手正文；非独立复现） |
| limitation / boundary | 五轮实验中反馈仅带来局部调整，未触发工作流级重规划或分析方法重设计，说明闭环适应仍有限。 | Full text, extracted character offset 1498；核验TXT行号 19 | experimental feedback prompted local adjustments but no workflow-level replanning | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文以机器人化学实验室检验大语言模型Agent能否把化学研究意图转成受实验室约束的实际操作。45个模块化工作站以机器可读技能开放，研究共执行4,608次试验，并按物理可执行性、问题覆盖和流程完整性等维度由专家评估。仅3.3%的试验产生完整可执行流程，最佳系统的可执行率为28.1%；多轮实验反馈也未促成流程级重规划。该研究提供了Agent物理执行能力的压力测试，而非某个特定反应的新发现。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究目标是实测语言模型Agent在机器人化学实验中将科学意图落实为物理行动的能力。
  - 原文位置：Full text, extracted character offset 1010；核验TXT行号 14；引文：Here, we use a robotic chemistry laboratory as a physical-world testbed to make scientific agency measurable
- 多步行动过程：yes。研究要求Agent在多项实验室约束下维持计划，并随连续轮次适应实验反馈，符合多步行动。
  - 原文位置：Full text, extracted character offset 2177；核验TXT行号 27；引文：Agents must produce executable actions that respect constraints imposed by instruments, operating parameters, samples and vessels, while maintaining coherent plans and adapting across successive experimental rounds
- 至少一种Agent能力：yes。Agent生成受设备、参数、样品及容器约束的可执行流程；研究直接以实体试验检验该能力。
  - 原文位置：Full text, extracted character offset 2177；核验TXT行号 27；引文：Agents must produce executable actions that respect constraints imposed by instruments, operating parameters, samples and vessels, while maintaining coherent plans and adapting across successive experimental rounds
- 明确科研流程角色：yes。Agent参与流程规划、执行及实验适应；论文以机器人化学实验室中的实际试验评估这一科研角色。
  - 原文位置：Full text, extracted character offset 1128；核验TXT行号 15；引文：modular workstations exposed as machine-readable skills enabled

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：03
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：03（仅归档，不覆盖其他模块）
- 模块内分类路径：03.01 化学总论与化学方法
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归入01.04通用科研Agent方法；对象是化学实验室操作工作流，但论文核心是Agent能力压力测试，没有以具体反应发现作为主要科学结果。

### 2.3 容易混淆的边界

归入01.04通用科研Agent方法；对象是化学实验室操作工作流，但论文核心是Agent能力压力测试，没有以具体反应发现作为主要科学结果。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

研究以45个可机器读取技能模块连接LLM Agent和机器人化学实验室，考查从研究意图转成物理操作、应对状态反馈和完成多步实验流程的可靠性。

### 3.3 自主能力

Agent生成受设备、参数、样品及容器约束的可执行流程；研究直接以实体试验检验该能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是把化学实验Agent的物理行动、流程覆盖和执行完整性变成可量化压力测试，并公开机器人技能接口支持重复评估。

### 4.2 系统流程与组件

作者开展4,608次试验，观察不同模型产生的操作/计划在实验室约束下能否执行，并以六项维度标记物理可执行性、问题覆盖和工作流完整性；另分析多轮规划中错误是否累积。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

验证来自真实机器人实验室任务和专家评估的试验标签，并对多个模型进行比较；报告成功比例及规划轨迹变化。它检验可执行与完整程度，不等于化学反应产率或新反应发现验证。

### 5.2 基线、指标与结果

总体只有3.3%的试验获得专家评定的完整成功；表现较好的系统在可执行标签上仍只达到28.1%，长流程规划中会遗漏步骤或偏离任务。结果揭示语言计划转成物理操作的显著落差。

### 5.3 科学贡献与证据强度

贡献是把化学实验Agent的物理行动、流程覆盖和执行完整性变成可量化压力测试，并公开机器人技能接口支持重复评估。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较知识问答或代码执行基准，该工作在真实机器人实验室检查动作可行性和长流程完整性；论文强调计划质量不能替代物理执行证据。

## 7. 局限性与风险

实验室技能和任务范围限定了可测能力，专家评分具有操作化定义；低成功率反映当前系统在该测试床的表现，不能直接推断所有机器人实验室场景。

## 8. 对综述写作的价值

可用于衡量化学Agent从语言计划到机器人实际动作的可靠性，并讨论实验流程完整性的操作化。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

作者在45个机器人工作站上对化学实验Agent进行4,608次压力测试，重点评估计划能否转为可执行动作及是否覆盖完整流程。完整成功比例仅3.3%，显示自然语言推理尚不能替代可靠的实体实验执行。

### 9.2 速记版 pipeline

作者开展4,608次试验，观察不同模型产生的操作/计划在实验室约束下能否执行，并以六项维度标记物理可执行性、问题覆盖和工作流完整性；另分析多轮规划中错误是否累积。

### 9.3 标注字段汇总

```text
paper_id=ASD-1011
inclusion_status=to_read
scientific_object_modules=03
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=03
module_taxonomy_codes=03.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`03.03.03` 催化化学；二级：`03.03`。
- 原文位置：PDF pp.5。
- 判定：Concrete experiment/task evidence supports 03.03.03 (催化化学). h that a task had started or completed. We collected 32 research tasks from domain experts, with eight tasks in each of four catalysis domains (Fig. 2B, note 4 of the supplementary text, and table S8). Together, these tasks formed a test suite for general catalysis research spanning electrocatalysis, electrochemical materials and testing, photocatalysis and thermal catalysis. Electrocatalysis tasks covered the oxygen
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
