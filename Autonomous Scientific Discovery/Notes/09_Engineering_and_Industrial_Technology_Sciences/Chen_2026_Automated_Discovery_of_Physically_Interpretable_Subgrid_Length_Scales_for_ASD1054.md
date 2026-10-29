# Automated Discovery of Physically Interpretable Subgrid Length Scales for Detached Eddy Simulation via Agentic AI

**论文信息**

- ID：ASD-1054
- 标题：Automated Discovery of Physically Interpretable Subgrid Length Scales for Detached Eddy Simulation via Agentic AI
- 作者：Jiawei Chen; Xiang I. A. Yang; Ping He
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.29850
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1054.txt
- PDF / 本地文件路径：Reference_PDF/09_Engineering_and_Industrial_Technology_Sciences/Chen_2026_Automated_Discovery_of_Physically_Interpretable_Subgrid_Length_Scales_for_ASD1054.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学问题 | DEScover搜索DES模型的subgrid length scale表达式。 | Abstract；核验TXT行号 15 | Four large language model (LLM) agents then propose, review, implement, and evaluate candidate formulations and generate scripts for CFD simulations. | 高（一手正文；非独立复现） |
| 多Agent过程 | 四个LLM代理提出、审阅、实现并评估候选公式。 | Abstract；核验TXT行号 14 | The user provides only a modeling idea: the length scale is the grid width normal to the local vortex axis. | 高（一手正文；非独立复现） |
| 评测对象 | 候选在平板、后向台阶、自由剪切层和结冰翼型上测试。 | Abstract；核验TXT行号 18 | The candidates are tested on four cases spanning canonical and engineering flows: a flat plate, a backward-facing step, a free shear layer, and an iced airfoil. | 高（一手正文；非独立复现） |
| 效果比较 | 最佳候选在四类测试中优于最大网格尺度基线。 | Abstract；核验TXT行号 19 | For all test cases, the best candidate consistently outperforms the standard length scale based on the maximum cell size. | 高（一手正文；非独立复现） |
| 工作量 | 单次Agent发现流程平均约25分钟，不含CFD仿真。 | Abstract；核验TXT行号 22 | discovery run takes about 25 minutes on average, excluding the CFD simulations. | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | DES亚格子尺度在平板、后向台阶、自由剪切层和结冰翼型流场上检验，既涉及流体力学对象也服务CFD工程建模；建议补02.02.03经典力学。 | TXT line 18；核验TXT行号 18 | four cases spanning canonical and engineering flows: a flat plate, a backward-facing step, a free shear layer, and an iced airfoil. For all test cases, the best candidate consistently outperforms the standard length scale based on the maximum cell size. Its ac | 高（一手正文；非独立复现） |

## 0. 摘要翻译

DEScover用多Agent发现可解释的Detached Eddy Simulation亚格子长度尺度。研究者只提供基于局部涡轴法向网格宽度的建模想法，Agent提出、评审、编码和评估候选表达式，并通过工程与典型流动CFD案例检验。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是发现DES湍流模型可解释的亚格子长度尺度。
  - 原文位置：Abstract；核验TXT行号 15；引文：Four large language model (LLM) agents then propose, review, implement, and evaluate candidate formulations and generate scripts for CFD simulations.
- 多步行动过程：yes。多个Agent依次提出、审查、实现并评估候选闭合表达式。
  - 原文位置：Abstract；核验TXT行号 14；引文：The user provides only a modeling idea: the length scale is the grid width normal to the local vortex axis.
- 至少一种Agent能力：yes。多Agent从用户概念生成可运行代码并利用CFD结果择优。
  - 原文位置：Abstract；核验TXT行号 14；引文：The user provides only a modeling idea: the length scale is the grid width normal to the local vortex axis.
- 明确科研流程角色：yes。Agent承担工程湍流模型假设生成、仿真测试和筛选。
  - 原文位置：Abstract；核验TXT行号 18；引文：The candidates are tested on four cases spanning canonical and engineering flows: a flat plate, a backward-facing step, a free shear layer, and an iced airfoil.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：02;09
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：09（仅归档，不覆盖其他模块）
- 模块内分类路径：02.02.03 经典力学；09.01 工程基础
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

DES亚格子尺度在平板、后向台阶、自由剪切层和结冰翼型流场上检验，既涉及流体力学对象也服务CFD工程建模；建议补02.02.03经典力学。

### 2.3 容易混淆的边界

DES亚格子尺度在平板、后向台阶、自由剪切层和结冰翼型流场上检验，既涉及流体力学对象也服务CFD工程建模；建议补02.02.03经典力学。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Multi-Agent System；Tool-using Agent

### 3.2 科研流程角色

hypothesis_generation；simulation_modeling；tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

LLM代理分担发现、批判审查、公式实现和评估；CFD求解器计算候选闭合在流场上的表现，研究者给定初始物理想法，最终候选是可独立使用的湍流模型项。

### 3.3 自主能力

多Agent从用户概念生成可运行代码并利用CFD结果择优。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

流体工程侧提出并验证新的物理可解释DES长度尺度；系统侧显示多Agent可把建模直觉转为候选闭合、代码与仿真评估。

### 4.2 系统流程与组件

输入物理建模想法；发现Agent从涡识别器推断涡轴并提出尺度形式；评审Agent检查物理可解释性；编码Agent生成并执行CFD脚本；评估Agent对多个流态比较标准尺度和候选结果；保留表现稳健者。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

四种流动案例：平板、后向台阶、自由剪切层和结冰翼型。比较最大单元尺度基线及专家设计的剪切层适配尺度，借CFD数值结果评估。

### 5.2 基线、指标与结果

作者报告最佳候选在所有测试案例上均优于最大单元尺寸基线；相对专家设计剪切层尺度准确度相近或略好。Agent发现过程平均约25分钟，不含求解时间。

### 5.3 科学贡献与证据强度

流体工程侧提出并验证新的物理可解释DES长度尺度；系统侧显示多Agent可把建模直觉转为候选闭合、代码与仿真评估。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与只做CFD设定自动化的Agent相比，DEScover直接搜索湍流模型结构；与纯数据拟合闭合相比，候选由物理想法约束且形式可读。

## 7. 局限性与风险

四个案例支持的流态范围仍有限，候选尺度需在更宽Re数、网格及复杂几何中继续评估；报告的发现耗时不含昂贵CFD运行。

## 8. 对综述写作的价值

可用于综述Agent提出物理可解释工程模型并以多案例求解验证的代表工作。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

DEScover由多Agent提出并通过CFD测试新的可解释湍流长度尺度。

### 9.2 速记版 pipeline

输入物理建模想法；发现Agent从涡识别器推断涡轴并提出尺度形式；评审Agent检查物理可解释性；编码Agent生成并执行CFD脚本；评估Agent对多个流态比较标准尺度和候选结果；保留表现稳健者。

### 9.3 标注字段汇总

```text
paper_id=ASD-1054
inclusion_status=to_read
scientific_object_modules=02;09
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=09
module_taxonomy_codes=02.02.03;09.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`09.01.02` 工程力学；二级：`09.01`。
- 原文位置：PDF p.1。
- 判定：脱体涡模拟亚格子闭合与流动实验，工程流体力学。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
