# Sun et al. 2026 - TeLLAgent: a dual-agent framework for reliable scientific discovery with tool-enhanced LLMs

**论文信息**
- 标题：TeLLAgent: a dual-agent framework for reliable scientific discovery with tool-enhanced LLMs
- 作者：Sun et al.
- 年份：2026
- 来源 / venue：Chemical Science
- DOI / arXiv / URL：https://doi.org/10.1039/d5sc09883a
- PDF / 本地文件路径：本轮基于 RSC publisher abstract 与 reviewer 一手证据；未保存本地 PDF
- 论文类型：系统论文 / general scientific-discovery agent framework
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | RSC publisher abstract | supervisor-executor dual-agent framework + self-correction loop | 高 |
| 科学对象归类 | `01.04` | RSC publisher abstract | 贡献中心是可迁移 scientific-discovery framework | 高 |
| 方法流程 | 规划-执行-纠错 | RSC publisher abstract | global planning agent, local execution agent, 30 tools | 高 |
| 实验验证 | benchmark + cross-domain demo | RSC publisher abstract | benchmark against GPT-5 and other frameworks | 高 |
| 边界判断 | 应离开 `03` | object-first reading | organic solar cell demo 不足以压过通用框架属性 | 高 |

## 0. 摘要翻译

本文提出 TeLLAgent，一个由 supervisor 与 executor 组成的双 Agent 科学发现框架，通过 30 个专用工具、自纠错回路和多步科研任务编排，提高 tool-enhanced LLM 在 scientific discovery 中的可靠性，并在 benchmark 与有机太阳能材料发现中验证。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具备多步规划、执行、工具调用、自纠错和科研工作流角色承担
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：任务分解、工具调用、知识检索、结果整合、端到端科研执行

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不适用

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：01
- 二级类：01.04
- 三级类：通用科研 Agent / 科学发现平台
- 四级专题：Dual-agent scientific discovery framework
- 四级专题是否为新增：否
- 归类理由：主贡献是领域可迁移的科研 Agent 架构，而非单一化学对象研究
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：general scientific-discovery capability
- 最终科学问题：如何提高 tool-enhanced LLM scientific-discovery workflows 的可靠性
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：化学 venue 与单个 organic solar cell demo 都不足以改变其通用框架属性

### 2.3 容易混淆的边界

- 可能误归类到：03 / 04
- 最终判定：改到 01.04
- 判定理由：organic solar cell 和 drug-discovery 扩展示例反而说明其跨领域平台属性
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Multi-Agent System：是
- Tool-using Agent：是
- Hybrid Agent：是

### 3.2 科研流程角色

- 知识抽取与组织：是
- 假设生成：是
- 工具调用与代码执行：是
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 多模态：是

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：降低 tool-augmented scientific-discovery tasks 中的幻觉和流程失稳
- 现有科研流程或方法的痛点：单 Agent 在复杂科研任务中的可靠性不足
- 核心假设或直觉：将全局规划与局部执行拆开，并加入自纠错回路，可显著提升可靠性

### 4.2 系统流程

1. 输入：科研问题与任务目标。
2. 任务分解 / 规划：supervisor 生成全局计划。
3. 工具、数据库、模型或实验平台调用：executor 调用专用工具执行子任务。
4. 中间结果反馈：结果返回给 supervisor 做校验。
5. 决策或迭代：通过 self-correction loop 修正错误并继续执行。
6. 输出：更可靠的 scientific-discovery workflow 结果。

### 4.3 系统组件

- Agent 核心：supervisor + executor dual-agent system
- 工具 / API / 数据库：30 specialized tools
- 记忆或状态模块：任务状态与执行上下文
- 规划器：global planning agent
- 评估器 / verifier：self-correction / reliability checks

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：benchmark tasks + organic solar cell materials discovery demo
- 任务设置：与 GPT-5 及其他框架比较科学任务完成质量
- 评价指标：reliability / recovery / task performance
- 关键结果：双 Agent 框架在可靠性上优于比较对象

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：核心是科研工作流能力与框架提升
- 科学贡献是否经过验证：是
- 贡献强度判断：中到强
- 科学贡献类型：system_platform; benchmark
- 证据强度：expert_confirmed

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：关注的是科研 Agent workflow 本身而非单学科模型
- 与已有 Agent / 科研智能系统的区别：强调 dual-agent reliability design
- 与同一科学领域其他 Agent 文献的关系：可与 Agent Laboratory、CodeScientist、InternAgent 并列
- 主要创新点：用 planning / execution 分离和自纠错回路稳定科学任务执行

## 7. 局限性与风险

- 当前总结主要基于 publisher abstract
- 虽有具体 demo，但仍应避免把跨领域平台强行压入化学或材料主类
- 是否仍需进一步全文复核：否，改类到 01.04 的依据已足够强

## 8. 对综述写作的价值

- 可放入哪个章节：01.04 通用科研智能系统
- 可支撑哪个论点：单个具体 demo 不应掩盖通用科研 Agent 架构属性
- 适合作为代表性案例吗：适合
- 推荐引用强度：core

## 9. 总结

### 9.1 一句话概括

双 Agent 科学发现框架以自纠错提升科研任务可靠性。

### 9.2 速记版 pipeline

1. supervisor 规划
2. executor 调工具
3. 返回中间结果
4. 自纠错修正
5. 输出科研结果

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：01
二级类：01.04
三级类：通用科研 Agent / 科学发现平台
四级专题：Dual-agent scientific discovery framework
Agent 类型：LLM Agent; Multi-Agent System; Tool-using Agent; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark
交叉属性：computation_driven; data_driven; multimodal
科学贡献类型：system_platform; benchmark
证据强度：expert_confirmed
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
