# ALKEMIE Agent: an autonomous platform for computational materials design

**论文信息**

- ID：ASD-0991
- 标题：ALKEMIE Agent: an autonomous platform for computational materials design
- 作者：Hongfu Huang; Yuzhe Li; Ao Xu; Bo Liu; Changrui Wang; Kan Tang; Ning Yang; Shengxian Liu; Hanyu Liu; Pengpeng Zhang; Linggang Zhu; Fengkai Liu; Yichen Lu; Tong Zhao; Naihua Miao; Jian Zhou; Zhimei Sun
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.15776
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0991.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Huang_2026_ALKEMIE_Agent_an_autonomous_platform_for_computational_materials_design_ASD0991.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | ALKEMIE Agent是计算材料设计平台，将检索增强生成、材料计算知识库、已注册技能、数据库溯源、AI结构建模、受限任务执行、工具迭代及错误诊断整合进可追踪控制环。论文展示材料推荐、结构建模、声子计算、机器学习势训练、LAMMPS、AIMC采样及主动学习筛选等任务。 | 摘要；TXT第14行；核验TXT行号 14 | Despite the powerful multi-scale modeling methods and high-throughput infrastructures established in the materials community, real material computation workflows remain fragmented and heavily manual, requiring researchers to constantly bridge software tools, data analysis, and intermediate decisions. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 研究者以自然语言提出材料计算任务，Agent借助知识库和RAG补充工具说明，选取注册技能并调用材料数据库、结构建模和计算工具。任务执行受边界约束，工具错误及输出会触发诊断和后续调用；结果、来源和步骤保存在可追踪记录中。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第17行；核验TXT行号 17 | This growing gap between methodological capability and practical execution highlights the need for a new kind of autonomous computational framework, one that can coordinate tools, knowledge, and workflows in a more unified and adaptive way. | 高（一手正文；非独立复现） |
| Agent能力与行动 | ALKEMIE Agent: an autonomous platform for computational materials design。系统角色与能力：研究者以自然语言提出材料计算任务，Agent借助知识库和RAG补充工具说明，选取注册技能并调用材料数据库、结构建模和计算工具。任务执行受边界约束，工具错误及输出会触发诊断和后续调用；结果、来源和步骤保存在可追踪记录中。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第20行；核验TXT行号 20 | Here, we introduce ALKEMIE Agent, an agentic platform in which retrieval-augmented generation, a materials-computation knowledge base, registered skills, database-supported provenance, AI-assisted structure modeling, bounded task execution, tool-calling iteration, and error-diagnostic assistance are integrated within a traceable control loop. | 高（一手正文；非独立复现） |
| 验证与结果 | 以多类材料计算应用演示平台能力，涉及材料推荐、声子、势函数训练、分子动力学、AIMC和主动学习。论文主要是平台能力展示，任务层面的科学基线和成功率应按各案例单独描述。 | 摘要；TXT第25行；核验TXT行号 25 | The capabilities of ALKEMIE Agent are demonstrated through applications including materials recommendation, structure modeling, phonon calculations, machine-learned interatomic potential training, LAMMPS simulations, Ab Initio Monte Carlo (AIMC) sampling, and active-learning-based materials screening. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 可用于综述计算材料Agent平台设计、技能管理、受限执行和来源追踪。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第29行；核验TXT行号 29 | Finally, we outline the future directions and challenges for the development of agentic platforms for computational materials design. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

ALKEMIE Agent是计算材料设计平台，将检索增强生成、材料计算知识库、已注册技能、数据库溯源、AI结构建模、受限任务执行、工具迭代及错误诊断整合进可追踪控制环。论文展示材料推荐、结构建模、声子计算、机器学习势训练、LAMMPS、AIMC采样及主动学习筛选等任务。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。ALKEMIE Agent是计算材料设计平台，将检索增强生成、材料计算知识库、已注册技能、数据库溯源、AI结构建模、受限任务执行、工具迭代及错误诊断整合进可追踪控制环。论文展示材料推荐、结构建模、声子计算、机器学习势训练、LAMMPS、AIMC采样及主动学习筛选等任务。
  - 原文位置：摘要；TXT第14行；核验TXT行号 14；引文：Despite the powerful multi-scale modeling methods and high-throughput infrastructures established in the materials community, real material computation workflows remain fragmented and heavily manual, requiring researchers to constantly bridge software tools, data analysis, and intermediate decisions.
- 多步行动过程：yes。研究者以自然语言提出材料计算任务，Agent借助知识库和RAG补充工具说明，选取注册技能并调用材料数据库、结构建模和计算工具。任务执行受边界约束，工具错误及输出会触发诊断和后续调用；结果、来源和步骤保存在可追踪记录中。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：正文；TXT第25行；核验TXT行号 25；引文：The capabilities of ALKEMIE Agent are demonstrated through applications including materials recommendation, structure modeling, phonon calculations, machine-learned interatomic potential training, LAMMPS simulations, Ab Initio Monte Carlo (AIMC) sampling, and active-learning-based materials screening.
- 至少一种Agent能力：yes。ALKEMIE Agent: an autonomous platform for computational materials design。系统角色与能力：研究者以自然语言提出材料计算任务，Agent借助知识库和RAG补充工具说明，选取注册技能并调用材料数据库、结构建模和计算工具。任务执行受边界约束，工具错误及输出会触发诊断和后续调用；结果、来源和步骤保存在可追踪记录中。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第20行；核验TXT行号 20；引文：Here, we introduce ALKEMIE Agent, an agentic platform in which retrieval-augmented generation, a materials-computation knowledge base, registered skills, database-supported provenance, AI-assisted structure modeling, bounded task execution, tool-calling iteration, and error-diagnostic assistance are integrated within a traceable control loop.
- 明确科研流程角色：yes。ALKEMIE Agent: an autonomous platform for computational materials design。系统角色与能力：研究者以自然语言提出材料计算任务，Agent借助知识库和RAG补充工具说明，选取注册技能并调用材料数据库、结构建模和计算工具。任务执行受边界约束，工具错误及输出会触发诊断和后续调用；结果、来源和步骤保存在可追踪记录中。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：正文；TXT第216行；核验TXT行号 216；引文：The layered architecture is operationalized as a bounded, human-supervised control loop in which a materials-design request

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.01 材料基础；04.02 结构材料与无机材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为计算材料设计工作流及其多个材料系统，归04.01/04.02。平台广度不代表每个案例都完成了新材料实验验证。

### 2.3 容易混淆的边界

对象为计算材料设计工作流及其多个材料系统，归04.01/04.02。平台广度不代表每个案例都完成了新材料实验验证。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

ALKEMIE Agent: an autonomous platform for computational materials design。系统角色与能力：研究者以自然语言提出材料计算任务，Agent借助知识库和RAG补充工具说明，选取注册技能并调用材料数据库、结构建模和计算工具。任务执行受边界约束，工具错误及输出会触发诊断和后续调用；结果、来源和步骤保存在可追踪记录中。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

ALKEMIE Agent: an autonomous platform for computational materials design。系统角色与能力：研究者以自然语言提出材料计算任务，Agent借助知识库和RAG补充工具说明，选取注册技能并调用材料数据库、结构建模和计算工具。任务执行受边界约束，工具错误及输出会触发诊断和后续调用；结果、来源和步骤保存在可追踪记录中。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

可用于综述计算材料Agent平台设计、技能管理、受限执行和来源追踪。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

研究者以自然语言提出材料计算任务，Agent借助知识库和RAG补充工具说明，选取注册技能并调用材料数据库、结构建模和计算工具。任务执行受边界约束，工具错误及输出会触发诊断和后续调用；结果、来源和步骤保存在可追踪记录中。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

以多类材料计算应用演示平台能力，涉及材料推荐、声子、势函数训练、分子动力学、AIMC和主动学习。论文主要是平台能力展示，任务层面的科学基线和成功率应按各案例单独描述。

### 5.2 基线、指标与结果

以多类材料计算应用演示平台能力，涉及材料推荐、声子、势函数训练、分子动力学、AIMC和主动学习。论文主要是平台能力展示，任务层面的科学基线和成功率应按各案例单独描述。

### 5.3 科学贡献与证据强度

可用于综述计算材料Agent平台设计、技能管理、受限执行和来源追踪。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

平台与材料数据库、RAG、技能式工具调用及自动化材料计算工作相关，强调来源追踪、受限执行和错误诊断的统一。

## 7. 局限性与风险

作者及读者可确认的适用边界：平台覆盖多种计算技能，但应用案例类型不一，统一的成功率或跨任务科学基线有限；单个案例结果应分别解释。

## 8. 对综述写作的价值

可用于综述计算材料Agent平台设计、技能管理、受限执行和来源追踪。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

ALKEMIE Agent是计算材料设计平台，将检索增强生成、材料计算知识库、已注册技能、数据库溯源、AI结构建模、受限任务执行、工具迭代及错误诊断整合进可追踪控制环。

### 9.2 速记版 pipeline

研究者以自然语言提出材料计算任务，Agent借助知识库和RAG补充工具说明，选取注册技能并调用材料数据库、结构建模和计算工具。任务执行受边界约束，工具错误及输出会触发诊断和后续调用；结果、来源和步骤保存在可追踪记录中。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-0991
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.01;04.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.01.04` 材料计算与材料信息学；二级：`04.01`。
- 原文位置：PDF p.2。
- 判定：材料计算平台集成结构、声子和MLIP运行与验证。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
