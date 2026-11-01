# SQD-Agent: LLM-driven agentic framework for Quantum Chemistry workflows

**论文信息**

- ID：ASD-0888
- 标题：SQD-Agent: LLM-driven agentic framework for Quantum Chemistry workflows
- 作者：Tiwari, Kislaya; Ray, Anupama
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.39302
- 一手阅读来源：https://arxiv.org/html/2609.39302v2
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：SQD-Agent: LLM-driven agentic framework for Quantum Chemistry workflows
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/2609.39302.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| Agent分工 | lead orchestrator路由给化学设置、SQD执行、硬件、mitigation、profiling、debug和reporting专员。 | §I, Fig. 1; §II | high |
| 确定性工具执行 | Agent规划和选择配置；固定库例程执行电路、量子采样、子空间对角化和后处理。 | §II-A Architecture | high |
| 自然语言工作流 | 甲醛STO-3G请求触发分子识别、ansatz配置、执行、工件保存和报告生成。 | §III-B | high |
| 模拟对象验证 | N2与CH2O结果和CASCI、CCSD等经典参考比较。 | §III-C; Table II | high |
| 硬件验证及限制 | N2/LUCJ在156-qubit ibm_kingston上执行；全文说明硬件验证仅一个分子和后端，不代表广泛化学benchmark。 | Hardware results; §IV | high |

## 0. 摘要翻译

已获取v2全文。SQD-Agent把自然语言科研意图转为可执行混合量子-经典工作流，是面向Sample-Based Quantum Diagonalization量子化学的LLM多Agent系统。编排Agent解析目标并路由给化学设置、SQD执行、硬件提交、误差缓解、分析和报告Agent。Simulator任务以甲醛为例自动选STO-3G并比较ansatz；N2、CH2O与CASCI/CCSD参考比较。N2/LUCJ在156-qubit IBM硬件上执行，结果在化学精度内复现FCI。全文将其限制为SQD算法下的分子基态估计，不主张量子优势。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
摘要明确多Agent生成并执行面向具体量子化学对象的多步工作流，工具协调与硬件反馈科研角色清晰。

### 1.2 排除风险检查

研究对象为N2/CH2O分子电子结构，归03.02；量子计算设备和采样算法是执行工具，不据此归02或01。
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

自然语言验证任务要求对甲醛STO-3G运行SQD能量估计并比较ansatz；Agent识别分子和基组并执行，生成比较表、线路指标及收敛轨迹。模拟实验将N2与CH2O和CASCI/CCSD参考比较。N2/LUCJ在ibm_kingston 156-qubit硬件运行；该设置下测试的误差缓解策略相对FCI误差在10^-3 mHa以内，未缓解baseline运行时间最短。此硬件实验用于验证系统能力，不是广泛化学性能benchmark。

### 2.3 容易混淆的边界

研究对象为N2/CH2O分子电子结构，归03.02；量子计算设备和采样算法是执行工具，不据此归02或01。

## 3. Agent 系统与科研流程角色

摘要明确多Agent生成并执行面向具体量子化学对象的多步工作流，工具协调与硬件反馈科研角色清晰。

科研流程与自主能力以本文实际行动和工具调用为依据：

模块化Python执行引擎接收Agent工作流规格，确定性例程执行电路构造、量子采样、子空间对角化和后处理。编排Agent将自然语言任务分派给化学设置、SQD执行、硬件、误差缓解、profiling、debug和报告专员。系统记录运行规格、命令、环境、线路指标、收敛轨迹与工件；支持模拟器和IBM Quantum后端。硬件Agent可按线路深度、门数、shots和目标建议误差缓解策略。

## 4. 方法设计

### 4.1 方法动机与设计

提供量子化学SQD任务的自然语言到执行工件工作流，把多Agent规划、经典化学前处理、量子硬件提交、缓解比较和复现日志接在一起。

### 4.2 系统流程与组件

模块化Python执行引擎接收Agent工作流规格，确定性例程执行电路构造、量子采样、子空间对角化和后处理。编排Agent将自然语言任务分派给化学设置、SQD执行、硬件、误差缓解、profiling、debug和报告专员。系统记录运行规格、命令、环境、线路指标、收敛轨迹与工件；支持模拟器和IBM Quantum后端。硬件Agent可按线路深度、门数、shots和目标建议误差缓解策略。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

自然语言验证任务要求对甲醛STO-3G运行SQD能量估计并比较ansatz；Agent识别分子和基组并执行，生成比较表、线路指标及收敛轨迹。模拟实验将N2与CH2O和CASCI/CCSD参考比较。N2/LUCJ在ibm_kingston 156-qubit硬件运行；该设置下测试的误差缓解策略相对FCI误差在10^-3 mHa以内，未缓解baseline运行时间最短。此硬件实验用于验证系统能力，不是广泛化学性能benchmark。

### 5.2 基线、指标与结果

自然语言验证任务要求对甲醛STO-3G运行SQD能量估计并比较ansatz；Agent识别分子和基组并执行，生成比较表、线路指标及收敛轨迹。模拟实验将N2与CH2O和CASCI/CCSD参考比较。N2/LUCJ在ibm_kingston 156-qubit硬件运行；该设置下测试的误差缓解策略相对FCI误差在10^-3 mHa以内，未缓解baseline运行时间最短。此硬件实验用于验证系统能力，不是广泛化学性能benchmark。

### 5.3 科学贡献与证据强度

提供量子化学SQD任务的自然语言到执行工件工作流，把多Agent规划、经典化学前处理、量子硬件提交、缓解比较和复现日志接在一起。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与ASD-0010 El Agente、ASD-0061 xchemagents相邻；本文专注SQD算法族的混合量子经典执行和真实硬件协调。

## 7. 局限性与风险

当前只覆盖SQD一种算法族和分子基态估计一个任务；硬件实验仅N2、一个ansatz和一个IBM后端。用户监督持续存在，几何选择、硬件提交、shots等安全关键决策不完全自主；作者不主张量子优势。

## 8. 对综述写作的价值

提供量子硬件Agent运行证据，并界定系统验证与化学发现、量子优势之间的差距。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent协调量子化学对角化流程

### 9.2 速记版 pipeline

模块化Python执行引擎接收Agent工作流规格，确定性例程执行电路构造、量子采样、子空间对角化和后处理。编排Agent将自然语言任务分派给化学设置、SQD执行、硬件、误差缓解、profiling、debug和报告专员。系统记录运行规格、命令、环境、线路指标、收敛轨迹与工件；支持模拟器和IBM Quantum后端。硬件Agent可按线路深度、门数、shots和目标建议误差缓解策略。

### 9.3 标注字段汇总

```text
paper_id=ASD-0888
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

- 本地PDF：`Reference_PDF/03_Chemical_Sciences/ASD-0888_SQD_Agent_LLM_driven_agentic_framework_for_Quantum_Chemistry_workflows.pdf`，共11页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2609.39302
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。
