# Unknown 2026 - Collective intelligence for AI-assisted chemical synthesis

**论文信息**
- 标题：Collective intelligence for AI-assisted chemical synthesis
- 作者：Unknown
- 年份：2026
- 来源 / venue：Nature
- DOI / arXiv / URL：https://doi.org/10.1038/s41586-026-10131-4
- PDF / 本地文件路径：未保存本地 PDF；本笔记基于 Nature 正式页面与 reviewer 一手证据
- 来源状态：source_limited=yes（当前未取得稳定全文 PDF；冻结归类已确定落在 `03`，但细节仍需后续全文补足）
- 论文类型：research paper / collective-intelligence chemistry system
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Nature abstract / figures | MOSAIC 基于 Llama-3.1 和大量 specialist chemical experts 生成可执行合成协议 | 高 |
| 科学对象归类 | 冻结为 `03`（落盘仍写作 `03.03`） | abstract / validation summary | 核心验证是 chemical synthesis、new compounds 和 reaction methods，因此按对象优先落在化学科学 | 中 |
| 方法流程 | 专家路由 + 协议生成 | abstract / framework figure | 系统从反应知识中调用专家并输出 executable experimental protocols | 中 |
| 实验验证 | 强，但当前本地证据仍以摘要层为主 | abstract / validation summary | 报告 71% success rate 与 35+ new compounds | 中 |
| 来源状态 | source_limited=yes | Nature page / reviewer evidence | 当前证据足以支持冻结 `03` 结论，但尚未取得稳定全文 PDF，因此保留全文补核需求 | 高 |
| 边界判断 | `03 / 01.04` 压力高 | abstract last sentence | 作者主动把方法上升到一般化 discovery strategy，因此仍需后续全文复核 | 中 |

## 0. 摘要翻译

作者提出 MOSAIC，一个以集体智能为核心的化学合成系统。它基于 Llama-3.1-8B-Instruct，将庞大的化学反应空间拆分为 2,498 个专业化学专家区域，从而生成可复现、可执行并带置信度指标的实验协议。论文报告系统以约 71% 的成功率实现 35 余个新化合物，并声称能支持超出训练分布的新反应方法发现。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在明确科研目标、多步协议生成、专家调用与实验实现验证
- 判定置信度：中高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：部分是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：知识调用、协议生成、实验方案建议与可执行性输出

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除，但需注明边界压力大

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：03
- 冻结归类结论：03（化学科学）
- 二级类：03.03
- source_limited：yes
- 三级类：
- 四级专题：Collective-intelligence chemical synthesis systems
- 四级专题是否为新增：否
- 归类理由：尽管平台与 general discovery 叙事很强，但当前可见核心验证仍集中在 chemical synthesis protocol 与新化合物实现，因此按对象优先落在 `03`
- 归类置信度：中

### 2.2 对象优先判定

- 最终科学研究对象：可执行化学合成协议、复杂合成与新化合物
- 最终科学问题：如何把海量反应知识转成成功率更高的可执行化学合成方案
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：虽然框架具有一般化表述，但当前实证对象仍是 chemistry synthesis

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：冻结为 03（化学科学；落盘仍写作 03.03）
- 判定理由：作者虽声称可推广到更广泛 discovery 场景，但当前强验证仍是化学合成；本项目据此在 `03 / 01.04` 压力下仍保持 chemistry-object landing
- 是否需要二次复核：是

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：部分是
- Multi-Agent System：是
- Robot / Embodied Agent：部分是
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：specialist-expert collective intelligence framework

### 3.2 科研流程角色

- 文献检索与阅读：部分是
- 知识抽取与组织：是
- 科学问题提出：否
- 假设生成：部分是
- 实验设计：是
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：是
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：部分是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：部分是
- 闭环实验：部分是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：是
- 仿真驱动：否
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：部分是
- 其他：specialist routing

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：化学反应知识增长过快，人类难以高效转译为可执行实验协议
- 现有科研流程或方法的痛点：单一模型难以覆盖广阔反应空间
- 核心假设或直觉：把化学知识拆成大量专家区域并协同调用，能提高合成成功率

### 4.2 系统流程

1. 输入：目标化合物或合成任务
2. 任务分解 / 规划：在专家空间中路由问题
3. 工具、数据库、模型或实验平台调用：specialist experts 与协议生成模块
4. 中间结果反馈：返回候选协议与置信度
5. 决策或迭代：选择更优协议并执行验证
6. 输出：可执行化学合成方案与新化合物

### 4.3 系统组件

- Agent 核心：MOSAIC
- 工具 / API / 数据库：specialist chemical experts
- 记忆或状态模块：reaction knowledge partition
- 规划器：expert routing
- 评估器 / verifier：success rate 与实验成功结果
- 人类反馈或专家介入：仍存在
- 实验平台或仿真环境：化学合成验证流程

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：未明确
- 湿实验：是
- 临床数据：否
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：chemical reaction protocols / new compounds
- 任务设置：生成可执行合成协议并验证成功率
- 对比基线：单模型或非专家路由方法
- 评价指标：success rate、新化合物数量等
- 关键结果：约 71% success rate；35+ new compounds
- 是否有消融实验：未完整获取
- 是否有失败案例或负结果：未完整获取

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是
- 科学贡献是否经过验证：是
- 贡献强度判断：强
- 科学贡献类型：experimental_discovery; system_platform
- 证据强度：实验验证

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不只是离线模型，而是面向可执行合成协议的 expert-routing system
- 与已有 Agent / 科研智能系统的区别：强调 collective intelligence 与 specialist partitioning
- 与同一科学领域其他 Agent 文献的关系：和 ChemCrow / Chemputer / synthesis engine 形成高平台感 chemistry-agent 谱系
- 主要创新点：以大量专门化学专家协同生成可执行协议

## 7. 局限性与风险

- Agent 自主性不足：仍需更完整全文判断
- 科学验证不足：当前本地证据仍偏摘要层
- 泛化性不足：虽声称可广泛推广，但当前证据主要来自化学合成
- 工具链依赖：强
- 数据泄漏或 benchmark 偏差：需要继续关注
- 成本、可复现性或安全风险：实验实现成本高
- 是否仍需后续全文复核：是；当前问题主要是 source completeness，而不是冻结 `03` 结论本身不稳

## 8. 对综述写作的价值

- 可放入哪个章节：03 化学科学 / AI-assisted synthesis
- 可支撑哪个论点：平台感很强的系统，也可能因为 concrete chemistry validation 而保持在 03
- 可用于哪个表格或图：03/01.04 高压力边界案例表
- 适合作为代表性案例吗：可以，但需标注边界压力
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：abstract、framework figure、validation summary
- 需要与哪些论文并列比较：ChemCrow、MOOSE-Chem、Chemputer lineage

## 9. 总结

### 9.1 一句话概括

集体智能系统生成并验证可执行化学合成协议。

### 9.2 速记版 pipeline

1. 输入化学合成任务
2. 路由到专业化学专家
3. 生成可执行协议
4. 验证成功率与新化合物
5. 迭代改进方案

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：03
二级类：03.03
三级类：
四级专题：Collective-intelligence chemical synthesis systems
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; experimental_design; tool_use_and_code_execution; experiment_execution; evidence_assessment_and_validation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; wet_lab_experiment; expert_evaluation
交叉属性：computation_driven; data_driven; experiment_driven
科学贡献类型：experimental_discovery; system_platform
证据强度：medium_pending_full_text
归类置信度：中
纳入置信度：中高
推荐引用强度：普通引用
```
