# Zhao et al. 2026 - OpenEarth-Agent: From Tool Calling to Tool Creation for Open-Environment Earth Observation

**论文信息**
- 标题：OpenEarth-Agent: From Tool Calling to Tool Creation for Open-Environment Earth Observation
- 作者：Sijie Zhao; Feng Liu; Xueliang Zhang; Hao Chen; Xinyu Gu; Zhe Jiang; Fenghua Ling; Ben Fei; Wenlong Zhang; Junjue Wang; Weihao Xuan; Pengfeng Xiao; Naoto Yokoya; Lei Bai
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2603.22148
- PDF / 本地文件路径：当前笔记基于 arXiv abstract / HTML 与官方 GitHub
- 论文类型：预印本 / Earth observation agent system
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract | 系统具备 adaptive workflow planning 与 tool creation，不是单轮 EO 问答 | 高 |
| 科学对象归类 | `05.04` | abstract / HTML | 论文对象明确是 open-environment Earth observation | 高 |
| 方法流程 | 多 Agent 闭环 | HTML | Data Summary、Planning、Workflow、Coding、Checking 五类 agents 协同完成任务 | 高 |
| 工具与对象绑定 | 很强 | HTML / GitHub | GEE、gdal、rasterio、geopandas、PySAL 与多源遥感数据深度绑定 EO 分析 | 高 |
| 实验验证 | benchmark + cross-benchmark | abstract / HTML | OpenEarth-Bench 有 596 个真实案例，并在 Earth-Bench 上与大量专用工具系统对比 | 高 |

## 0. 摘要翻译

论文提出 OpenEarth-Agent，一个面向 open-environment Earth observation 的多 Agent 系统。与只会调固定工具的系统不同，它能根据任务需要创建新工具，并将多源数据探索、任务 DAG 化、代码执行与结果检查串成闭环。作者构建了 OpenEarth-Bench，并展示该系统在 urban、agriculture、vegetation、water bodies、soil、economy 与 snow 等 Earth observation 场景中的泛化能力。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统具备规划、工具创建、执行、检查反馈和多步闭环
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：数据获取、预处理、分析执行、结果校验、工具构造

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：05
- 二级类：05.04
- 三级类：Earth observation 与地理空间分析
- 四级专题：open-environment EO tool-creation agents
- 四级专题是否为新增：否
- 归类理由：虽然方法论有较强平台感，但 benchmark、工具、任务和验证都深度绑定 EO 与地理空间分析
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：open-environment Earth observation workflows
- 最终科学问题：如何在复杂 EO 场景下让 Agent 自主完成多源数据探索、分析和结果校验
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：tool creation 只是方法创新，稳定对象仍是 EO scientific workflows

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 05.04
- 判定理由：OpenEarth-Bench、Earth-Bench、EO tools 与任务定义都不是领域无关平台证据
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：部分是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：tool-creation EO workflow agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与知识组织：部分是
- 科学问题提出：否
- 假设生成：否
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与假设验证：是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：是
- 多尺度建模：部分是
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：geospatial analysis

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：开放环境中的 EO 任务远比固定 benchmark 更复杂，固定工具箱难以泛化
- 现有科研流程或方法的痛点：只会 tool calling 的系统很难适应 unseen EO data and tasks
- 核心假设或直觉：如果 Agent 能把任务结构化并在需要时创建新工具，就能更稳地执行 full-pipeline EO analysis

### 4.2 系统流程

1. 输入：Earth observation 自然语言任务
2. 任务分解 / 规划：先做多源数据概览，再把任务拆成 DAG
3. 工具、数据库、模型或实验平台调用：调用或创建 EO tools，访问多源遥感数据
4. 中间结果反馈：Checking agent 对结果有效性和地学合理性做检查
5. 决策或迭代：修正工具或 workflow
6. 输出：可执行的 EO analysis result

### 4.3 系统组件

- Agent 核心：OpenEarth-Agent multi-agent workflow
- 工具 / API / 数据库：GEE、gdal、rasterio、geopandas、PySAL 等
- 记忆或状态模块：任务 DAG 与中间执行状态
- 规划器：Planning / Workflow agents
- 评估器 / verifier：Checking agent
- 人类反馈或专家介入：无强制 HITL
- 实验平台或仿真环境：OpenEarth-Bench / Earth-Bench

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：部分是
- 专家评估：部分是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：OpenEarth-Bench 596 个真实 EO full-pipeline cases
- 任务设置：urban、agriculture、vegetation、water、soil、economy、snow 等跨域 EO tasks
- 对比基线：Earth-Bench 上的已有 remote-sensing agents / tool systems
- 评价指标：任务完成率、跨环境泛化与 cross-benchmark 表现
- 关键结果：仅用少量 essential pretrained models 也能接近依赖大量 specialized tools 的系统
- 是否有消融实验：摘要级证据有限
- 是否有失败案例或负结果：当前证据未详细展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏 EO workflow 平台能力
- 科学贡献是否经过验证：是
- 贡献强度判断：中高
- 科学贡献类型：系统平台
- 证据强度：以一手 abstract / HTML 为主

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：关键不是普通 EO 多模态问答，而是能主动创建工具的 workflow agent
- 与已有 Agent / 科研智能系统的区别：强调从 tool calling 走向 tool creation
- 与同一科学领域其他 Agent 文献的关系：可与 Earth-Agent、CMIP-Forge、EarthLink 一起构成 `05` 类平台感较强但对象明确的样本
- 主要创新点：在 EO 场景中把 workflow planning、tool creation 和 geoscientific checking 统一起来

## 7. 局限性与风险

- Agent 自主性不足：仍需依赖底层 LLM 与外部 EO 工具链质量
- 科学验证不足：当前证据主要来自 abstract / HTML / repo
- 泛化性不足：虽强调 open-environment，但实际泛化边界仍需持续观察
- 工具链依赖：高度依赖地理空间工具生态
- 数据泄漏或 benchmark 偏差：benchmark 构建方式会影响结论
- 成本、可复现性或安全风险：跨数据源和动态建工具的复现实践成本较高
- 是否仍需进一步全文复核：否

## 8. 对综述写作的价值

- 可放入哪个章节：Earth observation agent systems
- 可支撑哪个论点：即使系统看起来像通用平台，只要对象和验证深度绑定 EO，主类仍应是 `05`
- 可用于哪个表格或图：`05 / 01.04` 边界压测表
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：多 Agent 架构与 OpenEarth-Bench 说明
- 需要与哪些论文并列比较：ASD-0653、ASD-0632、ASD-0851

## 9. 总结

### 9.1 一句话概括

面向开放 EO 环境的多 Agent 工具创建系统。

### 9.2 速记版 pipeline

1. 汇总多源 EO 数据
2. 把任务拆成 DAG
3. 调工具或创建新工具
4. 检查并修正分析结果

### 9.3 标注字段汇总

```text
是否纳入：是
主类：05
二级类：05.04
三级类：Earth observation 与地理空间分析
四级专题：open-environment EO tool-creation agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven; multimodal
科学贡献类型：system_platform
证据强度：medium_high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
