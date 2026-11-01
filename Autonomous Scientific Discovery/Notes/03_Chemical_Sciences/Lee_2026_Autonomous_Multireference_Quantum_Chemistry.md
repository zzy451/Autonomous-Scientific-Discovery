# Can Autonomous LLM Agents Execute Multireference Quantum Chemistry Calculations?

**论文信息**

- ID：ASD-0880
- 标题：Can Autonomous LLM Agents Execute Multireference Quantum Chemistry Calculations?
- 作者：Lee, Victor Chang; Rondinelli, James M.
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.13357
- 一手阅读来源：https://arxiv.org/html/2609.13357
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：Can Autonomous LLM Agents Execute Multireference Quantum Chemistry Calculations?
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/2609.13357.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 科研任务 | Agent自主完成活性空间选择、态平均、收敛恢复和态识别。 | Abstract | high |
| 多步执行 | 生成、提交ORCA作业并解析输出；记录推理日志。 | Abstract; Methods | high |
| 对象/基准 | 以QUESTDB分子垂直跃迁能比较三种知识条件。 | Results IV.1 | high |
| 效果指标 | 决策梯使覆盖率24.9%升至44.1%，MAE 0.373降至0.339 eV；复现MAE 23 meV。 | Abstract; Conclusions | high |
| 适用边界 | 过渡金属体系仍困难，需专门活性空间和态跟踪方法。 | Conclusions | high |

## 0. 摘要翻译

本文评估自主LLM Agent能否独立完成多参考电子结构计算中的活性空间选择、态平均、收敛恢复与电子态识别。Agent检索文献类比或记录化学推理，生成并提交ORCA计算、分析输出并保留审计日志。以QUESTDB垂直激发能为基准，结构化决策梯使覆盖率由24.9%升至44.1%，MAE由0.373降至0.339 eV；信息充分时复现MAE为23 meV。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
全文记录Agent自主选择计算设置、调用ORCA、分析结果及恢复收敛，承担电子结构计算研究角色；有明确分子对象和基准验证。

### 1.2 排除风险检查

对象是分子电子结构与跃迁能，归化学03.02；不因作者机构或计算方法归材料04/计算科学。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：03
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：03（仅归档，不替代多模块事实）
- 模块内分类路径：03.02
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

84个分子、558个QUESTDB垂直激发能；比较baseline、decision-ladder、replication三种信息条件；报告coverage和MAE，复现任务七次内解决75%目标构型。

### 2.3 容易混淆的边界

对象是分子电子结构与跃迁能，归化学03.02；不因作者机构或计算方法归材料04/计算科学。

## 3. Agent 系统与科研流程角色

全文记录Agent自主选择计算设置、调用ORCA、分析结果及恢复收敛，承担电子结构计算研究角色；有明确分子对象和基准验证。

科研流程与自主能力以本文实际行动和工具调用为依据：

Claude Opus 5 Agent结合ORCA 6.1；以文献检索/类比决定活性空间与态选择，生成并提交输入，解析输出并恢复收敛；使用CASSCF/SC-NEVPT2、aug-cc-pVTZ和RIJCOSX。

## 4. 方法设计

### 4.1 方法动机与设计

展示Agent执行多参考量子化学工作流的能力，并说明结构化程序规则可提高覆盖率并降低误差。

### 4.2 系统流程与组件

Claude Opus 5 Agent结合ORCA 6.1；以文献检索/类比决定活性空间与态选择，生成并提交输入，解析输出并恢复收敛；使用CASSCF/SC-NEVPT2、aug-cc-pVTZ和RIJCOSX。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

84个分子、558个QUESTDB垂直激发能；比较baseline、decision-ladder、replication三种信息条件；报告coverage和MAE，复现任务七次内解决75%目标构型。

### 5.2 基线、指标与结果

84个分子、558个QUESTDB垂直激发能；比较baseline、decision-ladder、replication三种信息条件；报告coverage和MAE，复现任务七次内解决75%目标构型。

### 5.3 科学贡献与证据强度

展示Agent执行多参考量子化学工作流的能力，并说明结构化程序规则可提高覆盖率并降低误差。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与ASD-0010 El Agente、ASD-0061 xchemagents、ASD-0217 Aitomia主题相邻；本文具体关注多参考活性空间、态指认和QUESTDB复现。

## 7. 局限性与风险

过渡金属体系仍困难；性能依赖任务上下文和专家知识；完整上下文复现代表性能上界。

## 8. 对综述写作的价值

为Agent自主计算化学、工具调用及可重复性提供量化证据。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

自主执行多参考量子化学流程

### 9.2 速记版 pipeline

Claude Opus 5 Agent结合ORCA 6.1；以文献检索/类比决定活性空间与态选择，生成并提交输入，解析输出并恢复收敛；使用CASSCF/SC-NEVPT2、aug-cc-pVTZ和RIJCOSX。

### 9.3 标注字段汇总

```text
paper_id=ASD-0880
inclusion_status=included
scientific_object_modules=03
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=03
module_taxonomy_codes=03.02
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/03_Chemical_Sciences/ASD-0880_Can_Autonomous_LLM_Agents_Execute_Multireference_Quantum_Chemistry_Calculations.pdf`，共16页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2609.13357
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。
