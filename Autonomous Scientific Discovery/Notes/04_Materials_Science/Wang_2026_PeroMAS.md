# Wang 2026 - PeroMAS: A Multi-agent System of Perovskite Material Discovery

**论文信息**
- 标题：PeroMAS: A Multi-agent System of Perovskite Material Discovery
- 作者：Yishu Wang; Wei Liu; Yifan Li; Shengxiang Xu; Xujie Yuan; Ran Li; Yuyu Luo; Jia Zhu; Shimin Di; Min-Ling Zhang; Guixiang Li
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2602.13312
- PDF / 本地文件路径：本轮笔记基于 arXiv abstract 整理；未确认本地归档 PDF
- 论文类型：系统论文 / materials discovery agent
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract L38-L41 | 系统把 perovskite-specific tools 封装为 MCPs，由多 Agent 规划与调用 | 高 |
| 科学对象归类 | `04.04` | arXiv abstract L38-L41 | 直接对象是 perovskite solar-cell materials，而非通用工作流本体 | 高 |
| 方法流程 | 端到端材料发现 | arXiv abstract L38-L40 | 从 literature retrieval、data extraction 到 property prediction、mechanism analysis 构成闭环 | 高 |
| 实验验证 | 有真实合成验证 | arXiv abstract L40-L41 | 论文明确说通过 real synthesis experiments 验证有效性 | 高 |
| 边界判断 | 不回到 `01.04` | arXiv abstract L38-L41 | 工具虽平台化，但研究目标稳定锁定在 perovskite material discovery | 高 |

## 0. 摘要翻译

论文指出，钙钛矿太阳能电池是第三代光伏革命的重要方向，但其开发流程复杂，涉及文献检索、数据整合、实验设计和合成等闭环步骤。作者提出 PeroMAS，把一组 perovskite-specific tools 封装为 MCPs，由多 Agent 进行规划和调用，以支持多目标约束下的钙钛矿材料设计，并覆盖从文献检索、数据抽取到性质预测和机理分析的全过程。论文还构建了由人类专家参与的评测基准，并通过真实合成实验验证了系统有效性。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：有明确材料发现目标；多步工作流；多 Agent 协作与工具调用显式存在
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：文献整合、数据提取、性质预测、机理分析、候选设计

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：04
- 二级类：04.04
- 三级类：
- 四级专题：Perovskite-discovery multi-agent systems
- 四级专题是否为新增：否
- 归类理由：系统直接服务于 perovskite materials discovery，输出对象是具体材料候选
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：perovskite solar-cell materials
- 最终科学问题：如何在多目标约束下发现更优的钙钛矿材料候选
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：MCP 和 multi-agent 只是手段；研究对象始终是钙钛矿材料

### 2.3 容易混淆的边界

- 可能误归类到：01.04；07
- 最终判定：保留 04.04
- 判定理由：既不是通用科学平台，也不是药物/生医研究；应用场景稳定落在光伏材料
- 是否需要二次复核：否，主类方向较稳

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是（专家评测）
- Hybrid Agent：是
- 其他：MCP-based materials workflow

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：部分是
- 假设生成：是
- 实验设计：部分是
- 仿真建模：部分是
- 工具调用与代码执行：是
- 实验执行：部分是
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：未明确
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：部分是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：是
- 仿真驱动：部分是
- 多模态：未明确
- 多尺度建模：否
- 高通量筛选：部分是
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：MCP tool integration

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：钙钛矿开发流程环节多、物理约束传播难、单模型难以端到端优化
- 现有科研流程或方法的痛点：离散模型割裂了材料发现全链条
- 核心假设或直觉：多 Agent 通过 perovskite-specific tools 协同，可以把多目标材料发现流程打通

### 4.2 系统流程

1. 输入：perovskite material discovery objective
2. 任务分解 / 规划：多 Agent 组织目标、约束与搜索路线
3. 工具、数据库、模型或实验平台调用：调用 perovskite-specific MCP tools
4. 中间结果反馈：融合检索、抽取、预测与机理分析结果
5. 决策或迭代：在多目标约束下继续筛选与设计
6. 输出：满足约束的候选材料与分析结论

### 4.3 系统组件

- Agent 核心：PeroMAS multi-agent controller
- 工具 / API / 数据库：perovskite-specific MCP tools
- 记忆或状态模块：摘要未完全展开
- 规划器：存在
- 评估器 / verifier：human-expert benchmark 与真实合成验证
- 人类反馈或专家介入：存在专家评测
- 实验平台或仿真环境：真实 synthesis experiments

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：部分是
- 高通量计算：部分是
- 机器人实验：否
- 湿实验：是
- 临床数据：否
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：perovskite materials / PSCs
- 任务设置：多目标约束下的材料设计与发现
- 对比基线：single LLM 与 traditional search strategies
- 评价指标：discovery efficiency、候选质量、真实合成效果
- 关键结果：显著提高发现效率，找到满足多目标约束的候选，并完成真实合成验证
- 是否有消融实验：摘要未明确
- 是否有失败案例或负结果：摘要未明确

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是，属于材料候选发现与真实验证
- 科学贡献是否经过验证：是
- 贡献强度判断：强
- 科学贡献类型：system_platform; materials_discovery
- 证据强度：medium_high_primary_abstract

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单一 predictor，而是端到端多 Agent 材料发现系统
- 与已有 Agent / 科研智能系统的区别：围绕 perovskite-specific MCP 工具构造完整 workflow
- 与同一科学领域其他 Agent 文献的关系：可与 LLMatDesign、GraphAgents、A-Lab 系列形成 04 类材料 Agent 谱系
- 主要创新点：把 perovskite 开发全流程打通，并落到真实合成验证

## 7. 局限性与风险

- Agent 自主性不足：摘要未完全展示长期记忆和失败恢复细节
- 科学验证不足：已有真实合成，但仍建议阅读全文确认基线与实验规模
- 泛化性不足：当前集中在 perovskite family
- 工具链依赖：强依赖 perovskite-specific MCP ecosystem
- 数据泄漏或 benchmark 偏差：专家基准需全文核实设计细节
- 成本、可复现性或安全风险：材料实验复现成本较高
- 是否仍需进一步全文复核：建议后续补核全文；本轮仅核对 arXiv abstract，未确认本地归档 PDF，但主类和纳入判断已经较稳

## 8. 对综述写作的价值

- 可放入哪个章节：04.04 能源 / 光伏材料 Agent
- 可支撑哪个论点：具体材料对象上的多 Agent workflow 已能连接检索、预测与真实合成
- 可用于哪个表格或图：材料发现闭环强度比较表；MCP-based workflows 对比表
- 适合作为代表性案例吗：是
- 推荐引用强度：core
- 需要在正文中特别引用的页码 / 图 / 表：multi-objective constraints、human-expert benchmark、real synthesis
- 需要与哪些论文并列比较：GraphAgents、A-Lab、Agentic LLM Reasoning in a Self-Driving Laboratory

## 9. 总结

### 9.1 一句话概括

把钙钛矿材料发现流程做成多 Agent 闭环系统。

### 9.2 速记版 pipeline

1. 设定钙钛矿材料目标
2. 多 Agent 规划与调用 MCP 工具
3. 检索抽取并做预测分析
4. 生成并筛选候选
5. 通过真实合成验证

### 9.3 标注字段汇总

```text
是否纳入：是
主类：04
二级类：04.04
三级类：
四级专题：Perovskite-discovery multi-agent systems
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Hybrid Agent
科研流程角色：literature_search_and_reading; data_analysis; workflow_orchestration; feedback_iteration; evidence_assessment_and_validation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; wet_lab_experiment; expert_evaluation; computational_validation
交叉属性：computation_driven; data_driven; experiment_driven
科学贡献类型：system_platform; materials_discovery
证据强度：medium_high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
