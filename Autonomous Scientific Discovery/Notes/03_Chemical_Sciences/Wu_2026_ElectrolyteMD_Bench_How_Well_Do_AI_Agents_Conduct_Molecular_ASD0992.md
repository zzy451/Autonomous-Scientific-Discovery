# ElectrolyteMD-Bench: How Well Do AI Agents Conduct Molecular Dynamics Studies across Electrolyte Solvation Regimes?

**论文信息**

- ID：ASD-0992
- 标题：ElectrolyteMD-Bench: How Well Do AI Agents Conduct Molecular Dynamics Studies across Electrolyte Solvation Regimes?
- 作者：Shukai Wu; Shuo Niu; Zhaoming Xu; Yan Luo; Wentao Lin
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.31743
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0992.txt
- PDF / 本地文件路径：Reference_PDF/03_Chemical_Sciences/Wu_2026_ElectrolyteMD_Bench_How_Well_Do_AI_Agents_Conduct_Molecular_ASD0992.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | ElectrolyteMD-Bench评估AI Agent能否可靠开展不同溶剂化区间的电解液分子动力学研究。基准覆盖稀溶、高浓及局部高浓电解液，把局部配位、离子缔合、单粒子动力学和集体输运组织为连续研究流程，并按模拟有效性、分析有效性、证据完整性和结论校准审计。 | 摘要；TXT第272行；核验TXT行号 272 | AI agents are advancing the automation of molecular dynamics (MD) research, with the potential to accelerate discovery and design of lithium-battery electrolytes. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | Agent接收电解液体系与研究问题，构建模拟盒并执行平衡、生产采样、性质分析和跨体系解释；每阶段根据误差和采样充分性决定修正、延长采样或停止。基准同时保留模拟轨迹与证据，审查Agent最终结论是否由计算支持。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第272行；核验TXT行号 272 | We introduce ElectrolyteMD-Bench, which unifies dilute, high-concentration, and localized high-concentration electrolytes in a comparative study across distinct solvation regimes. | 高（一手正文；非独立复现） |
| Agent能力与行动 | ElectrolyteMD-Bench: How Well Do AI Agents Conduct Molecular Dynamics Studies across Electrolyte Solvation Regimes?。系统角色与能力：Agent接收电解液体系与研究问题，构建模拟盒并执行平衡、生产采样、性质分析和跨体系解释；每阶段根据误差和采样充分性决定修正、延长采样或停止。基准同时保留模拟轨迹与证据，审查Agent最终结论是否由计算支持。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第272行；核验TXT行号 272 | Agents autonomously perform system construction, equilibration, production sampling, property analysis, and cross-system interpretation, while deciding whether to correct errors, continue sampling, or stop. | 高（一手正文；非独立复现） |
| 验证与结果 | 八种模型—harness配置共完成24个体系运行，均获得有效生产轨迹，但没有一项研究满足全部科学要求。失败包括漏分析、物理定义或数值实现错误、统计支持不足及结论与证据不符。 | 摘要；TXT第272行；核验TXT行号 272 | Across eight model–harness configurations, all 24 system runs produced valid production trajectories, yet none of the eight studies satisfied all scientific requirements. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 支持综述论证“工作流成功运行”与“科学研究可靠完成”之间仍有显著差距。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第272行；核验TXT行号 272 | Failures included missing analyses, incorrect physical definitions or numerical implementations, insufficient statistical support, and completion claims inconsistent with retained evidence. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

ElectrolyteMD-Bench评估AI Agent能否可靠开展不同溶剂化区间的电解液分子动力学研究。基准覆盖稀溶、高浓及局部高浓电解液，把局部配位、离子缔合、单粒子动力学和集体输运组织为连续研究流程，并按模拟有效性、分析有效性、证据完整性和结论校准审计。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。ElectrolyteMD-Bench评估AI Agent能否可靠开展不同溶剂化区间的电解液分子动力学研究。基准覆盖稀溶、高浓及局部高浓电解液，把局部配位、离子缔合、单粒子动力学和集体输运组织为连续研究流程，并按模拟有效性、分析有效性、证据完整性和结论校准审计。
  - 原文位置：摘要；TXT第272行；核验TXT行号 272；引文：AI agents are advancing the automation of molecular dynamics (MD) research, with the potential to accelerate discovery and design of lithium-battery electrolytes.
- 多步行动过程：yes。Agent接收电解液体系与研究问题，构建模拟盒并执行平衡、生产采样、性质分析和跨体系解释；每阶段根据误差和采样充分性决定修正、延长采样或停止。基准同时保留模拟轨迹与证据，审查Agent最终结论是否由计算支持。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第272行；核验TXT行号 272；引文：We introduce ElectrolyteMD-Bench, which unifies dilute, high-concentration, and localized high-concentration electrolytes in a comparative study across distinct solvation regimes.
- 至少一种Agent能力：yes。ElectrolyteMD-Bench: How Well Do AI Agents Conduct Molecular Dynamics Studies across Electrolyte Solvation Regimes?。系统角色与能力：Agent接收电解液体系与研究问题，构建模拟盒并执行平衡、生产采样、性质分析和跨体系解释；每阶段根据误差和采样充分性决定修正、延长采样或停止。基准同时保留模拟轨迹与证据，审查Agent最终结论是否由计算支持。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第272行；核验TXT行号 272；引文：Agents autonomously perform system construction, equilibration, production sampling, property analysis, and cross-system interpretation, while deciding whether to correct errors, continue sampling, or stop.
- 明确科研流程角色：yes。八种模型—harness配置共完成24个体系运行，均获得有效生产轨迹，但没有一项研究满足全部科学要求。失败包括漏分析、物理定义或数值实现错误、统计支持不足及结论与证据不符。
  - 原文位置：摘要；TXT第272行；核验TXT行号 272；引文：Across eight model–harness configurations, all 24 system runs produced valid production trajectories, yet none of the eight studies satisfied all scientific requirements.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：03;04
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：03（仅归档，不覆盖其他模块）
- 模块内分类路径：03.02 基础化学；04.04 能源、电子与器件材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象是锂电池电解液溶剂化和MD研究任务，涵盖03.02分子模拟科学问题及04.04研究流程评估。Agent能力评估基准不等同于本文发现新电解液。

### 2.3 容易混淆的边界

对象是锂电池电解液溶剂化和MD研究任务，涵盖03.02分子模拟科学问题及04.04研究流程评估。Agent能力评估基准不等同于本文发现新电解液。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

ElectrolyteMD-Bench: How Well Do AI Agents Conduct Molecular Dynamics Studies across Electrolyte Solvation Regimes?。系统角色与能力：Agent接收电解液体系与研究问题，构建模拟盒并执行平衡、生产采样、性质分析和跨体系解释；每阶段根据误差和采样充分性决定修正、延长采样或停止。基准同时保留模拟轨迹与证据，审查Agent最终结论是否由计算支持。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

ElectrolyteMD-Bench: How Well Do AI Agents Conduct Molecular Dynamics Studies across Electrolyte Solvation Regimes?。系统角色与能力：Agent接收电解液体系与研究问题，构建模拟盒并执行平衡、生产采样、性质分析和跨体系解释；每阶段根据误差和采样充分性决定修正、延长采样或停止。基准同时保留模拟轨迹与证据，审查Agent最终结论是否由计算支持。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

支持综述论证“工作流成功运行”与“科学研究可靠完成”之间仍有显著差距。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

Agent接收电解液体系与研究问题，构建模拟盒并执行平衡、生产采样、性质分析和跨体系解释；每阶段根据误差和采样充分性决定修正、延长采样或停止。基准同时保留模拟轨迹与证据，审查Agent最终结论是否由计算支持。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

八种模型—harness配置共完成24个体系运行，均获得有效生产轨迹，但没有一项研究满足全部科学要求。失败包括漏分析、物理定义或数值实现错误、统计支持不足及结论与证据不符。

### 5.2 基线、指标与结果

八种模型—harness配置共完成24个体系运行，均获得有效生产轨迹，但没有一项研究满足全部科学要求。失败包括漏分析、物理定义或数值实现错误、统计支持不足及结论与证据不符。

### 5.3 科学贡献与证据强度

支持综述论证“工作流成功运行”与“科学研究可靠完成”之间仍有显著差距。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

本文补足常见Agent benchmark只测代码或单项任务的不足，将电解液研究组织为含统计充分性、物理定义和证据一致性的完整MD研究评估。

## 7. 局限性与风险

作者及读者可确认的适用边界：基准明确显示所有配置虽能生成有效生产轨迹，却没有研究满足全部科学要求；基准任务与电解液体系仍是有限覆盖。

## 8. 对综述写作的价值

支持综述论证“工作流成功运行”与“科学研究可靠完成”之间仍有显著差距。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

ElectrolyteMD-Bench评估AI Agent能否可靠开展不同溶剂化区间的电解液分子动力学研究。

### 9.2 速记版 pipeline

Agent接收电解液体系与研究问题，构建模拟盒并执行平衡、生产采样、性质分析和跨体系解释；每阶段根据误差和采样充分性决定修正、延长采样或停止。基准同时保留模拟轨迹与证据，审查Agent最终结论是否由计算支持。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-0992
inclusion_status=to_read
scientific_object_modules=03;04
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=03
module_taxonomy_codes=03.02;04.04
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`03.02.04` 物理化学；二级：`03.02`。
- 原文位置：PDF p.3。
- 判定：电解液溶剂化、输运及分子动力学直接支持物理化学；电化学可作交叉候选。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
