# Human-agent discovery of reconfigurable in-plane ferroelectric superdomain control

**论文信息**

- ID：ASD-1003
- 标题：Human-agent discovery of reconfigurable in-plane ferroelectric superdomain control
- 作者：Yu Liu; Boris Slautin; Ching-Che Lin; Jaegyu Kim; Lane W. Martin; Sergei V. Kalinin
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.06887
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1003.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Liu_2026_Human_agent_discovery_of_reconfigurable_in_plane_ferroelectric_superdomain_ASD1003.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | SPARC让编码Agent和人类操作员共享显微镜、笔记本及持久记忆文件，在未预先定义全部变量和动作的探索阶段协作。论文将其用于重构(111)取向PbZr0.2Ti0.8O3薄膜的面内铁电超畴方向；Agent分析旧测量、定义实验状态并设计交替极性脉冲晶格，后续Agent控制实验验证方向选择规律。 | 摘要；TXT第27行；核验TXT行号 27 | Automated experimentation is most effective when the observables, available actions, and objective are defined before the experiment starts, as is the case for Bayesian optimization. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 操作员监督的首轮活动中，Agent重分析历史测量、建立状态表示并提出脉冲实验设计；人类结合仪器知识审阅并执行/监督。后续控制阶段，系统将PITFALLS记忆编译成写入前检查，再由Agent生成控制程序执行脉冲与扫描，读取畴方向变化并验证假设。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第31行；核验TXT行号 31 | Here we introduce the Scanning Probe Agentic Research Cycle (SPARC) framework, in which a coding agent and a human operator share one microscope, one notebook, and two persistent memory files. | 高（一手正文；非独立复现） |
| Agent能力与行动 | Human-agent discovery of reconfigurable in-plane ferroelectric superdomain control。系统角色与能力：操作员监督的首轮活动中，Agent重分析历史测量、建立状态表示并提出脉冲实验设计；人类结合仪器知识审阅并执行/监督。后续控制阶段，系统将PITFALLS记忆编译成写入前检查，再由Agent生成控制程序执行脉冲与扫描，读取畴方向变化并验证假设。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第35行；核验TXT行号 35 | In an operator-supervised campaign, the agent reanalyzed earlier manual measurements, defined the experimental state, and developed an oriented lattice of stationary bias pulses with alternating polarity between rows to reconfigure the superdomain direction. | 高（一手正文；非独立复现） |
| 验证与结果 | 实验表明空间极性反转比脉冲晶格周期与畴条纹周期精确匹配更能决定方向选择；组合栅格扫描和掩膜脉冲将“UTK”写入超畴方向。作者强调执行物理验证、记忆有效范围、观测量验证和鲁棒控制仍是必要要求。 | 正文；TXT第39行；核验TXT行号 39 | The experiments showed that spatial polarity alternation, instead of the exact matching between the lattice and lamellar periods, determines directional selection. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 交互记录和错误日志揭示实验Agent在探索性测量中的要求与限制，相关结果仍以人类监督的实验过程为边界。 | 摘要；TXT第39行；核验TXT行号 127 | The interaction record and error logs also reveal the requirements and present limitations of a reliable experimental agent. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

SPARC让编码Agent和人类操作员共享显微镜、笔记本及持久记忆文件，在未预先定义全部变量和动作的探索阶段协作。论文将其用于重构(111)取向PbZr0.2Ti0.8O3薄膜的面内铁电超畴方向；Agent分析旧测量、定义实验状态并设计交替极性脉冲晶格，后续Agent控制实验验证方向选择规律。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。SPARC让编码Agent和人类操作员共享显微镜、笔记本及持久记忆文件，在未预先定义全部变量和动作的探索阶段协作。论文将其用于重构(111)取向PbZr0.2Ti0.8O3薄膜的面内铁电超畴方向；Agent分析旧测量、定义实验状态并设计交替极性脉冲晶格，后续Agent控制实验验证方向选择规律。
  - 原文位置：摘要；TXT第27行；核验TXT行号 27；引文：Automated experimentation is most effective when the observables, available actions, and objective are defined before the experiment starts, as is the case for Bayesian optimization.
- 多步行动过程：yes。操作员监督的首轮活动中，Agent重分析历史测量、建立状态表示并提出脉冲实验设计；人类结合仪器知识审阅并执行/监督。后续控制阶段，系统将PITFALLS记忆编译成写入前检查，再由Agent生成控制程序执行脉冲与扫描，读取畴方向变化并验证假设。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第31行；核验TXT行号 31；引文：Here we introduce the Scanning Probe Agentic Research Cycle (SPARC) framework, in which a coding agent and a human operator share one microscope, one notebook, and two persistent memory files.
- 至少一种Agent能力：yes。Human-agent discovery of reconfigurable in-plane ferroelectric superdomain control。系统角色与能力：操作员监督的首轮活动中，Agent重分析历史测量、建立状态表示并提出脉冲实验设计；人类结合仪器知识审阅并执行/监督。后续控制阶段，系统将PITFALLS记忆编译成写入前检查，再由Agent生成控制程序执行脉冲与扫描，读取畴方向变化并验证假设。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第35行；核验TXT行号 35；引文：In an operator-supervised campaign, the agent reanalyzed earlier manual measurements, defined the experimental state, and developed an oriented lattice of stationary bias pulses with alternating polarity between rows to reconfigure the superdomain direction.
- 明确科研流程角色：yes。实验表明空间极性反转比脉冲晶格周期与畴条纹周期精确匹配更能决定方向选择；组合栅格扫描和掩膜脉冲将“UTK”写入超畴方向。作者强调执行物理验证、记忆有效范围、观测量验证和鲁棒控制仍是必要要求。
  - 原文位置：正文；TXT第39行；核验TXT行号 39；引文：The experiments showed that spatial polarity alternation, instead of the exact matching between the lattice and lamellar periods, determines directional selection.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.03 软物质与功能材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为铁电薄膜超畴控制和扫描探针实验，归04.03。属于人机共同发现，Agent不是独立自主系统；物理写入是否成功需读回验证。

### 2.3 容易混淆的边界

对象为铁电薄膜超畴控制和扫描探针实验，归04.03。属于人机共同发现，Agent不是独立自主系统；物理写入是否成功需读回验证。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

实验设计与执行

Human-agent discovery of reconfigurable in-plane ferroelectric superdomain control。系统角色与能力：操作员监督的首轮活动中，Agent重分析历史测量、建立状态表示并提出脉冲实验设计；人类结合仪器知识审阅并执行/监督。后续控制阶段，系统将PITFALLS记忆编译成写入前检查，再由Agent生成控制程序执行脉冲与扫描，读取畴方向变化并验证假设。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

Human-agent discovery of reconfigurable in-plane ferroelectric superdomain control。系统角色与能力：操作员监督的首轮活动中，Agent重分析历史测量、建立状态表示并提出脉冲实验设计；人类结合仪器知识审阅并执行/监督。后续控制阶段，系统将PITFALLS记忆编译成写入前检查，再由Agent生成控制程序执行脉冲与扫描，读取畴方向变化并验证假设。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

可支持综述讨论开放式实验探索中人机互补、持久记忆及物理执行核验。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

操作员监督的首轮活动中，Agent重分析历史测量、建立状态表示并提出脉冲实验设计；人类结合仪器知识审阅并执行/监督。后续控制阶段，系统将PITFALLS记忆编译成写入前检查，再由Agent生成控制程序执行脉冲与扫描，读取畴方向变化并验证假设。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

实验表明空间极性反转比脉冲晶格周期与畴条纹周期精确匹配更能决定方向选择；组合栅格扫描和掩膜脉冲将“UTK”写入超畴方向。作者强调执行物理验证、记忆有效范围、观测量验证和鲁棒控制仍是必要要求。

### 5.2 基线、指标与结果

实验表明空间极性反转比脉冲晶格周期与畴条纹周期精确匹配更能决定方向选择；组合栅格扫描和掩膜脉冲将“UTK”写入超畴方向。作者强调执行物理验证、记忆有效范围、观测量验证和鲁棒控制仍是必要要求。

### 5.3 科学贡献与证据强度

可支持综述讨论开放式实验探索中人机互补、持久记忆及物理执行核验。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

作者把Agent定位为传统贝叶斯优化尚未适用的开放实验探索推理层，强调人类实验知识、共享记忆与显式物理验证的互补。

## 7. 局限性与风险

作者及读者可确认的适用边界：实证是围绕单一PbZr0.2Ti0.8O3薄膜的监督式和后续Agent控制活动；作者强调仪器执行读回、记忆有效条件和测量有效性仍需显式核验。

## 8. 对综述写作的价值

可支持综述讨论开放式实验探索中人机互补、持久记忆及物理执行核验。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

SPARC让编码Agent和人类操作员共享显微镜、笔记本及持久记忆文件，在未预先定义全部变量和动作的探索阶段协作。

### 9.2 速记版 pipeline

操作员监督的首轮活动中，Agent重分析历史测量、建立状态表示并提出脉冲实验设计；人类结合仪器知识审阅并执行/监督。后续控制阶段，系统将PITFALLS记忆编译成写入前检查，再由Agent生成控制程序执行脉冲与扫描，读取畴方向变化并验证假设。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-1003
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.03
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.03.04` 智能材料；二级：`04.03`。
- 原文位置：PDF p.4。
- 判定：PZT铁电薄膜超畴翻转写入，归智能材料。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
