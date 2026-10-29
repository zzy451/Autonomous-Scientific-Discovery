# CFD Forge: A Physics-Constrained Agentic Framework for Autonomous CFD

**论文信息**

- ID：ASD-1045
- 标题：CFD Forge: A Physics-Constrained Agentic Framework for Autonomous CFD
- 作者：Aakash Shailesh Oza; Ryan F. Johnson; Amir Barati Farimani
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.14104
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1045.txt
- PDF / 本地文件路径：全文已缓存；PDF尚未归档，详见资料清单
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| Agent科研目标 | 将文字工程请求转换为被检查的CFD仿真。 | Abstract；核验TXT行号 297 | We present CFD Forge, an agentic framework built around OpenFOAM that carries an engineering request through case construction, meshing, solver execution, diagnostics, and reporting. | 高（一手正文；非独立复现） |
| 行动链 | 案例构建、网格、求解、诊断及报告组成多步流程。 | Abstract；核验TXT行号 297 | A large language model interprets the request, reads the simulation evidence, identifies likely causes of problems, and proposes actions from a closed set. | 高（一手正文；非独立复现） |
| 科学对象 | 验证对象包括收缩扩张喷管与二维前向台阶流。 | Abstract；核验TXT行号 297 | We demonstrate the framework on a converging–diverging nozzle and a two-dimensional forward-facing step, including geometry and operating changes requested in text. | 高（一手正文；非独立复现） |
| 评估设计 | 以36个记录状态回放并注入部分故障诊断。 | Abstract；核验TXT行号 297 | To test this separation, we replayed 36 recorded simulation states, some with deliberately altered diagnostics, through the same model in two setups. | 高（一手正文；非独立复现） |
| 接受判据 | 判定由确定性检查执行；在故障样本上未错误接受。 | Abstract / Results；核验TXT行号 297 | with CFD Forge’s checks deciding, none was accepted. | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | 喷管、前向台阶和湍流立方体用于检验CFD工程流程与数值健康验收；OpenFOAM是工具，任务对象为工程流动仿真，09.01适配。 | TXT line 297；核验TXT行号 297 | We demonstrate the framework on a converging–diverging nozzle and a two-dimensional forward-facing step, including geometry and operating changes requested in text. A turbulent cube, run outside the agent loop, shows why the checks matter: the solver completed | 高（一手正文；非独立复现） |

## 0. 摘要翻译

CFD Forge围绕OpenFOAM将文字工程请求转为可运行并可审查的流体仿真。LLM处理请求、查看仿真证据、提出下一步动作；按流型预先登记的确定性检查独立判断结果是否达标。论文展示喷管和前向台阶案例，并以扰动诊断记录检验验收机制。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是自动构造、运行并判断CFD工程仿真。
  - 原文位置：Abstract；核验TXT行号 297；引文：We present CFD Forge, an agentic framework built around OpenFOAM that carries an engineering request through case construction, meshing, solver execution, diagnostics, and reporting.
- 多步行动过程：yes。流程实际覆盖建模、网格、求解、诊断和报告多个步骤。
  - 原文位置：Abstract；核验TXT行号 297；引文：We present CFD Forge, an agentic framework built around OpenFOAM that carries an engineering request through case construction, meshing, solver execution, diagnostics, and reporting.
- 至少一种Agent能力：yes。LLM读取仿真证据、诊断故障并从受限动作集中提出处置。
  - 原文位置：Abstract；核验TXT行号 297；引文：A large language model interprets the request, reads the simulation evidence, identifies likely causes of problems, and proposes actions from a closed set.
- 明确科研流程角色：yes。Agent承担CFD仿真执行者和结果诊断者角色。
  - 原文位置：Abstract；核验TXT行号 297；引文：A large language model interprets the request, reads the simulation evidence, identifies likely causes of problems, and proposes actions from a closed set.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：09
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：09（仅归档，不覆盖其他模块）
- 模块内分类路径：09.01 工程基础
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

喷管、前向台阶和湍流立方体用于检验CFD工程流程与数值健康验收；OpenFOAM是工具，任务对象为工程流动仿真，09.01适配。

### 2.3 容易混淆的边界

喷管、前向台阶和湍流立方体用于检验CFD工程流程与数值健康验收；OpenFOAM是工具，任务对象为工程流动仿真，09.01适配。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent；Hybrid Agent

### 3.2 科研流程角色

simulation_modeling；tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

LLM工程Agent负责解释请求、构建仿真案例、执行受限动作和诊断证据；OpenFOAM及确定性验收器承担数值求解与硬判据。案例文件、模型调用和决策均保留以便审计。

### 3.3 自主能力

LLM读取仿真证据、诊断故障并从受限动作集中提出处置。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学侧展示可审计的喷管与台阶流仿真；系统侧将开放式任务执行与确定性验收分开，避免语言模型单凭单一分数判定可信度。

### 4.2 系统流程与组件

输入自然语言工程需求；解释几何与运行条件；构建案例并生成网格；调用OpenFOAM求解；分析残差和流场诊断；根据许可动作调整配置或报告；独立规则对物理/数值指标验收，模型不能自我批准。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

两个流动案例用于展示工作流；另在36个记录状态上回放并部分篡改诊断，比较模型自行判断与确定性检查。包含OpenFOAM计算与显式、按流型注册的验收标准。

### 5.2 基线、指标与结果

作者报告在未提供检查结果时模型三次重复均接受了13个可检测故障中的12个；交由CFD Forge检查判定后，故障案例均未获接受。湍流立方体展示了均值阻力稳定但侧向力振荡仍增长的拒收理由。

### 5.3 科学贡献与证据强度

科学侧展示可审计的喷管与台阶流仿真；系统侧将开放式任务执行与确定性验收分开，避免语言模型单凭单一分数判定可信度。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相比只生成CFD代码或脚本自动化，本文把请求解释、案例执行、诊断和验收串联，并保存证据链。

## 7. 局限性与风险

两个主要验证案例仍属有限流型；验收标准需针对流动类型预先登记。湍流立方体在Agent回路外运行，说明该案例是诊断示例而非自主闭环结果。

## 8. 对综述写作的价值

可用于综述工程仿真Agent如何以物理确定性判据约束LLM自主性，并报告故障验收量化结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

CFD Forge让LLM执行仿真工作、由物理检查器决定结果是否可接受。

### 9.2 速记版 pipeline

输入自然语言工程需求；解释几何与运行条件；构建案例并生成网格；调用OpenFOAM求解；分析残差和流场诊断；根据许可动作调整配置或报告；独立规则对物理/数值指标验收，模型不能自我批准。

### 9.3 标注字段汇总

```text
paper_id=ASD-1045
inclusion_status=to_read
scientific_object_modules=09
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=09
module_taxonomy_codes=09.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`09.01.02` 工程力学；二级：`09.01`。
- 原文位置：PDF p.1。
- 判定：喷管及立方体绕流CFD的确定性物理验收，属于工程力学。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
