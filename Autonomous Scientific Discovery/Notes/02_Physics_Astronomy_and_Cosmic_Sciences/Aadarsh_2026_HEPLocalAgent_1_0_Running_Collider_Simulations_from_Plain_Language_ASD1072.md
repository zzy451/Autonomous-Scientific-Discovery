# HEPLocalAgent 1.0: Running Collider Simulations from Plain-Language Requests on Your Own Computer

**论文信息**

- ID：ASD-1072
- 标题：HEPLocalAgent 1.0: Running Collider Simulations from Plain-Language Requests on Your Own Computer
- 作者：Singh, Aadarsh; Vempati, Sudhir K.
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.28244
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1072.txt
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Aadarsh_2026_HEPLocalAgent_1_0_Running_Collider_Simulations_from_Plain_Language_ASD1072.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科研任务 | 从自然语言请求构造对撞机模拟工作流。 | TXT lines 10-12；核验TXT行号 10 | We present HEPLocalAgent, an open-source local interface for constructing a bounded class of collider-simulation workflows from natural-language requests. A locally served lan- guage model proposes a typed workflow representation, while deterministic software restores | 高（一手正文；非独立复现） |
| 方法流程 | 模型提出类型化表示，确定性软件恢复参数并建输入。 | TXT lines 11-14；核验TXT行号 11 | class of collider-simulation workflows from natural-language requests. A locally served lan- guage model proposes a typed workflow representation, while deterministic software restores recognized user-stated quantities, constructs the HEP-tool inputs, validates the supported workflow, and presents the resulting artifacts for approval before execution. | 高（一手正文；非独立复现） |
| 基准结果 | 完整确定性管线比初始提议通过更多案例。 | TXT lines 16-19；核验TXT行号 16 | response comparison on 47 evaluable model–request cases, the first structured proposal pro- duced 7 unmodified artifacts satisfying the external benchmark scorer, compared with 19 after the complete deterministic pipeline. After applying the benchmark’s fixed representa- tion normalization, the corresponding counts were 11 and 43. The direction of improvement | 高（一手正文；非独立复现） |
| 执行验证 | 四个经批准工作流执行完成且重复截面一致。 | TXT lines 22-24；核验TXT行号 22 | trol lines, and the output-directory name), not on physics content. Four of seven approved workflows executed to completion on the managed local software stack with cross sections consistent between repeats. In a separate challenge set, 57 of 96 problematic requests nev- | 高（一手正文；非独立复现） |
| 限制 | 挑战集中57/96有问题请求仍到审批阶段。 | TXT lines 24-27；核验TXT行号 24 | consistent between repeats. In a separate challenge set, 57 of 96 problematic requests nev- ertheless reached the approval stage after part of the request had been dropped, defaulted, or reinterpreted. No tested unsafe payload was retained in an executable artifact before the approval gate, but this does not establish operating-system-level containment. The deter- | 高（一手正文；非独立复现） |

## 0. 摘要翻译

HEPLocalAgent从自然语言请求构造受限类别的对撞机模拟工作流。语言模型提出类型化表示，确定性软件恢复用户参数、生成工具输入并验证工作流，最终交用户批准执行。47个案例中完整管线比初始结构化提议通过更多外部评分；挑战请求显示系统仍可能丢失或改写用户意图，故需专家审批。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。构造并运行粒子对撞机模拟工作流。
  - 原文位置：TXT lines 10-12；核验TXT行号 10；引文：We present HEPLocalAgent, an open-source local interface for constructing a bounded class of collider-simulation workflows from natural-language requests. A locally served lan- guage model proposes a typed workflow representation, while deterministic software restores
- 多步行动过程：yes。自然语言解释后确定性构造输入、验证并等待批准执行。
  - 原文位置：TXT lines 11-14；核验TXT行号 11；引文：class of collider-simulation workflows from natural-language requests. A locally served lan- guage model proposes a typed workflow representation, while deterministic software restores recognized user-stated quantities, constructs the HEP-tool inputs, validates the supported workflow, and presents the resulting artifacts for approval before execution.
- 至少一种Agent能力：yes。Agent解析用户请求并委托确定性后端构造模拟工件。
  - 原文位置：TXT lines 866-869；核验TXT行号 866；引文：HEPLocalAgent implements the central architectural lesson of HEPToolBench: a language model interprets the user’s request, while deterministic software restores recognized user-stated facts, constructs the corresponding workflow, and checks it before execution. In the 47-case same-response comparison, the unmodified structured artifacts pass the external scorer in 7
- 明确科研流程角色：yes。生成对撞机模拟输入及分析工作流，执行前要求审批。
  - 原文位置：TXT lines 22-24；核验TXT行号 22；引文：trol lines, and the output-directory name), not on physics content. Four of seven approved workflows executed to completion on the managed local software stack with cross sections consistent between repeats. In a separate challenge set, 57 of 96 problematic requests nev-

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：02
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：02（仅归档，不覆盖其他模块）
- 模块内分类路径：02.02 物理学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

粒子碰撞模拟属于02物理科学；此文主要是科学软件与流程可靠性评估。

### 2.3 容易混淆的边界

粒子碰撞模拟属于02物理科学；此文主要是科学软件与流程可靠性评估。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

local_llm_workflow_agent

### 3.2 科研流程角色

simulation_workflow_construction；human_approval

本地运行LLM解释需求，确定性后端生成MadGraph、Pythia8、Delphes等工具工件并校验；执行前由用户批准。

### 3.3 自主能力

Agent解析用户请求并委托确定性后端构造模拟工件。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

系统贡献是本地、可检查且验证门控的HEP流程构建；科学贡献限于支持既定碰撞模拟，未报告新物理发现。

### 4.2 系统流程与组件

输入自然语言模拟请求；LLM形成类型化工作流表示，后端恢复已识别的物理参数、生成输入文件并校验支持范围，将工件交用户审查批准后执行；完成后比较截面及基准评分。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

47个模型-请求对照案例、96个问题请求挑战集、批准工作流本地执行和重复截面一致性测试。

### 5.2 基线、指标与结果

作者报告完整流程外部评分通过工件由7增至19；规范化评分由11增至43；4/7批准工作流成功完成。

### 5.3 科学贡献与证据强度

系统贡献是本地、可检查且验证门控的HEP流程构建；科学贡献限于支持既定碰撞模拟，未报告新物理发现。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

实现HEPToolBench提出的模型解释与确定性工作流构造分离原则。

## 7. 局限性与风险

- author_stated：不是自主或自验证Agent；57/96问题请求仍到审批阶段，且可能改变原意；无操作系统级隔离证明。
- reviewer_inference：软件基准合规不等于物理问题设置一定符合用户本意。

## 8. 对综述写作的价值

可讨论科学模拟Agent的人类审批门控及语义保持风险。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

HEPLocalAgent以确定性后端构造并验证本地对撞机模拟工作流。

### 9.2 速记版 pipeline

输入自然语言模拟请求；LLM形成类型化工作流表示，后端恢复已识别的物理参数、生成输入文件并校验支持范围，将工件交用户审查批准后执行；完成后比较截面及基准评分。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1072
inclusion_status=to_read
scientific_object_modules=02
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=02
module_taxonomy_codes=02.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`02.02.14` 粒子物理学；二级：`02.02`。
- 原文位置：PDF p.15。
- 判定：对撞机截面及事件模拟研究，归粒子物理。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
