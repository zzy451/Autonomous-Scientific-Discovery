# Ji et al. 2025 - Leveraging LLM-based agents for social science research: insights from citation network simulations

**论文信息**
- 标题：Leveraging LLM-based agents for social science research: insights from citation network simulations
- 作者：Jiarui Ji; Runlin Lei; Xuchen Pan; Zhewei Wei; Hao Sun; Yankai Lin; Xu Chen; Yongzheng Yang; Yaliang Li; Bolin Ding; Ji-Rong Wen
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2511.03758
- PDF / 本地文件路径：`Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Unknown_2025_Citation_Network_Simulations.pdf`（当前归档文件名沿用旧占位符）；本轮已基于本地归档 arXiv PDF 全文复核
- 论文类型：预印本 / citation-network simulation agents
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

## Reaudit Update (2026-07-05)

- `scientific_object_modules`: `11`
- `primary_module_for_filing`: `11`
- `source_limited`: `no`
- `first_hand_sources_checked`: local archived arXiv PDF full text
- `pdf_status`: local archived PDF `Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Unknown_2025_Citation_Network_Simulations.pdf`
- `final_note_classification`: stable `11.07` landing; note filing path is convenience only, not classification authority.
- `metadata_refresh`: visible authors corrected from placeholder `Unknown`; archive filename is intentionally unchanged.

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | 本地归档 PDF 第 1-2 页；正文 | 提出 CiteAgent 以 author / paper agents 模拟 citation-network formation | 高 |
| 科学对象归类 | `11.07` | 本地归档 PDF 第 1-2 页 | 对象是 citation networks、reference behavior、academic environments 与 science of science 研究 | 高 |
| 方法流程 | 多步 agent simulation | 本地归档 PDF 第 2 页；framework section | 包含 Initialization / Socialization / Creation 等阶段 | 高 |
| 验证内容 | science-of-science patterns | 本地归档 PDF 第 1 页摘要；results | 验证 power-law、citational distortion、shrinking diameter | 高 |
| 边界风险 | 标题误导 | 本地归档 PDF 第 1-2 页 | 虽写 social science research，但正文明确把对象锚定到 science-of-science citation-network simulation | 高 |

## 0. 摘要翻译

论文提出一个基于 LLM agents 的 citation-network simulation framework，用来模拟作者与论文的互动，并研究引用网络形成中的关键规律。作者用该系统考察 power-law、citational distortion、network diameter 变化等 science-of-science 现象，并分析 academic environments 如何影响引用行为。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统通过多步 author-agent simulation、协作、决策与引用生成来完成研究任务
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：部分是
  - 工具调用：部分是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：模拟科学共同体行为、分析引用网络、解释 academic patterns

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：11
- 二级类：11.07
- 三级类：citation-network simulation and science-of-science analysis
- 四级专题：academic citation behavior agents
- 四级专题是否为新增：否
- 归类理由：最终研究对象是 scientific knowledge production 中的 citation network 与引文行为
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：citation networks, referencing behavior, academic environments
- 最终科学问题：如何用 agent simulation 解释和研究 scientific citation behavior
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：尽管标题写 social science research，但对象并非一般社会系统，而是 academic citation networks

### 2.3 容易混淆的边界

- 可能误归类到：11.02
- 最终判定：保留 11.07
- 判定理由：正文明确将其界定为 science-of-science 子问题
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：部分是
- Tool-using Agent：部分是
- Retrieval-augmented Agent：否
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：author / paper simulation agents

### 3.2 科研流程角色

- 文献检索与阅读：部分是
- 知识抽取与组织：部分是
- 科学问题提出：否
- 假设生成：部分是
- 实验设计：是
- 仿真建模：是
- 工具调用与代码执行：部分是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：部分是
- 计划生成：部分是
- 工具调用：部分是
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
- 仿真驱动：是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：academic environment simulation

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：传统 citation-network analysis 难以直接检验不同 academic environments 下的引文决策机制
- 现有科研流程或方法的痛点：缺少可控、可解释的 academic-behavior simulation sandbox
- 核心假设或直觉：用 LLM agents 模拟作者与论文互动，可帮助研究科学共同体中的引文现象

### 4.2 系统流程

1. 输入：初始 academic environment 与 agent settings
2. 任务分解 / 规划：初始化 author / paper entities
3. 工具、数据库、模型或实验平台调用：进行 socialization、creation 与 citation decisions
4. 中间结果反馈：形成并更新 citation network
5. 决策或迭代：继续多轮 academic interaction
6. 输出：citation network statistics 与 science-of-science insights

### 4.3 系统组件

- Agent 核心：CiteAgent framework
- 工具 / API / 数据库：current visible evidence limited
- 记忆或状态模块：agent memory / paper history
- 规划器：multi-stage simulation logic
- 评估器 / verifier：network-pattern analysis
- 人类反馈或专家介入：环境设定
- 实验平台或仿真环境：academic citation-network simulation

## 5. 实验与验证

### 5.1 验证方式

- benchmark：否
- 仿真验证：是
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：citation-network simulation outputs
- 任务设置：academic citation behavior simulation
- 对比基线：known network regularities / counterfactual environments
- 评价指标：power-law, citational distortion, shrinking diameter 等
- 关键结果：系统可重现多个典型 citation-network phenomena
- 是否有消融实验：当前笔记未展开
- 是否有失败案例或负结果：当前笔记未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏 science-of-science simulation framework
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system_platform
- 证据强度：中高

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：对象是 academic citation behavior，不是自然科学对象
- 与已有 Agent / 科研智能系统的区别：通过 agent simulation 研究 science-of-science phenomena
- 与同一科学领域其他 Agent 文献的关系：可与 SciSciGPT、CiteME 放在 `11.07` 体系内比较
- 主要创新点：把 citation-network theory 与 LLM agent simulation 结合

## 7. 局限性与风险

- Agent 自主性不足：系统主要用于模拟与解释引文行为，而非直接执行现实科研闭环
- 科学验证不足：主要依赖 simulation
- 泛化性不足：对真实学术生态的映射仍有限
- 工具链依赖：依赖环境设定与 simulation assumptions
- 数据泄漏或 benchmark 偏差：simulation assumptions 需要继续注意
- 成本、可复现性或安全风险：主风险是标题容易把它误带到一般 social science

## 8. 对综述写作的价值

- 可放入哪个章节：`11.07` 中的 academic-network agents
- 可支撑哪个论点：部分标题写 social science 的论文，最终对象仍可能是 science-of-science
- 可用于哪个表格或图：citation-network simulation agents 对比
- 适合作为代表性案例吗：可作为边界样本
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：framework stages 与 network-phenomena results
- 需要与哪些论文并列比较：ASD-0624、ASD-0629

## 9. 总结

### 9.1 一句话概括

用 LLM agents 模拟作者与论文互动，研究 citation-network 规律。

### 9.2 速记版 pipeline

1. 初始化作者与论文 agent  
2. 让它们互动与写作  
3. 形成引用网络  
4. 分析学术网络规律

### 9.3 标注字段汇总

```text
是否纳入：是
主类：11
二级类：11.07
三级类：citation-network simulation and science-of-science analysis
四级专题：academic citation behavior agents
Agent 类型：LLM Agent; Multi-Agent System; Hybrid Agent
科研流程角色：experimental_design; simulation_modeling; data_analysis; result_interpretation; evidence_assessment_and_validation
自主能力：memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：simulation_validation
交叉属性：computation_driven; data_driven; simulation_driven
科学贡献类型：system_platform
证据强度：medium_high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
