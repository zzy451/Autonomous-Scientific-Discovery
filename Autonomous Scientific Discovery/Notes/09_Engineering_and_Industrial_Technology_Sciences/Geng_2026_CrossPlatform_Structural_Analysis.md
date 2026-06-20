# Geng et al. 2026 - Automating Structural Analysis Across Multiple Software Platforms Using Large Language Models

**论文信息**
- 标题：Automating Structural Analysis Across Multiple Software Platforms Using Large Language Models
- 作者：Ziheng Geng; Jiachen Liu; Ian Franklin; Ran Cao; Dan M. Frangopol; Minghui Cheng
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2604.09866
- PDF / 本地文件路径：当前笔记基于 arXiv abstract / PDF
- 论文类型：研究论文 / cross-platform structural-analysis multi-agent system
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract | 明确是 two-stage multi-agent architecture | 高 |
| 多步行动 | 是 | PDF §3.1-§3.2 | Stage 1 做 structured reasoning 与 JSON 抽取，Stage 2 并行翻译到多软件脚本 | 高 |
| 工具调用 | 是 | PDF §3.2-§3.3 | 面向 ETABS、SAP2000、OpenSees 生成可执行脚本 | 高 |
| 科学对象归类 | `09.05` | intro / abstract | 全文围绕 frame structural analysis、geometry、support、load、material、internal force diagrams | 高 |
| 边界判断 | 不转 `01.04` | methods / abstract | JSON 和 code translation 只是服务于结构分析对象 | 高 |
| 主要剩余风险 | core-strength risk | results | 重点仍是 workflow acceleration 与软件适配，而非更强 discovery contribution | 中高 |

## 0. 摘要翻译

本文研究如何让 LLM 以多 Agent 方式自动完成跨软件平台的结构分析。系统先从自然语言结构描述中提取几何、材料、边界与荷载信息，形成统一 JSON，再并行翻译为 ETABS、SAP2000 与 OpenSees 的可执行脚本。作者在 20 个代表性的 frame structural analysis 问题上进行了 10 次重复试验，报告系统在三种平台上都能达到 90% 以上准确率。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在明确目标、多阶段 multi-agent workflow、外部工程软件调用和可执行脚本生成
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：部分是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：结构分析、建模、脚本生成、平台适配、结果验证

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：09
- 二级类：09.05
- 三级类：跨平台结构分析与 FEA 建模
- 四级专题：Cross-platform structural-analysis agents
- 四级专题是否为新增：否
- 归类理由：最终对象始终是 frame structural analysis，而不是通用 multi-agent substrate
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：frame structural analysis、FEA modeling、跨 ETABS / SAP2000 / OpenSees workflow
- 最终科学问题：如何让 Agent 稳定完成跨软件平台的结构分析
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：统一 JSON 与并行 code translation 只是实现路径，不改变对象归属

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保持 09.05
- 判定理由：输入、输出、benchmark 和 evaluation 全部围绕结构分析对象
- 是否需要二次复核：建议

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：cross-platform code-translation agents

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：是
- 科学问题提出：否
- 假设生成：否
- 实验设计：否
- 仿真建模：是
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：部分是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：部分是
- 反馈迭代：是
- 自主决策：部分是
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：否
- 实验驱动：否
- 仿真驱动：是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：multi-software structural workflow

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：解决现有工作多局限在单一结构分析软件的问题
- 现有科研流程或方法的痛点：工程师往往需要跨 ETABS / SAP2000 / OpenSees 切换，人工成本高
- 核心假设或直觉：先统一结构语义，再并行翻译到多个软件平台，可以增强实用性与部署性

### 4.2 系统流程

1. 输入：自然语言结构分析问题
2. 任务分解 / 规划：agents 做 geometry / material / boundary / load inference
3. 工具、数据库、模型或实验平台调用：生成 JSON，再并行转成 ETABS / SAP2000 / OpenSees scripts
4. 中间结果反馈：检查多平台脚本的一致性与正确性
5. 决策或迭代：修正翻译或结构推理链
6. 输出：可执行多平台结构分析脚本

### 4.3 系统组件

- Agent 核心：two-stage multi-agent architecture
- 工具 / API / 数据库：ETABS；SAP2000；OpenSees
- 记忆或状态模块：shared JSON representation
- 规划器：Stage 1 structured reasoning agents
- 评估器 / verifier：multi-platform execution and accuracy checks
- 人类反馈或专家介入：未作为主流程核心
- 实验平台或仿真环境：20 representative frame problems

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：是
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：未明确

### 5.2 数据、任务与指标

- 数据集 / 实验对象：20 representative frame problems
- 任务设置：跨平台结构分析脚本生成
- 对比基线：多软件人工流程 / 非 agentic pipelines
- 评价指标：accuracy across repeated trials
- 关键结果：三平台准确率均超过 90%
- 是否有消融实验：摘要未充分展开
- 是否有失败案例或负结果：需全文继续核

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏结构分析自动化
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：系统平台 / 工程分析
- 证据强度：benchmark + 仿真验证

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单平台脚本生成，而是跨平台结构分析 workflow
- 与已有 Agent / 科研智能系统的区别：突出 unified JSON + parallel code-translation architecture
- 与同一科学领域其他 Agent 文献的关系：可与 0752 / 0753 / 0754 / 0756 构成 structural-analysis family
- 主要创新点：跨多个常用工程软件完成统一结构语义推理与脚本自动化

## 7. 局限性与风险

- Agent 自主性不足：更像工程分析 workflow acceleration
- 科学验证不足：仍以 benchmark 和 repeated trials 为主
- 泛化性不足：主要针对 frame structural analysis
- 工具链依赖：依赖各平台固定语法和建模逻辑
- 数据泄漏或 benchmark 偏差：需后续核
- 成本、可复现性或安全风险：多平台稳定部署仍需继续验证

## 8. 对综述写作的价值

- 可放入哪个章节：09 工程与工业技术科学中的结构分析 agents
- 可支撑哪个论点：Agent 已从单平台分析走向跨平台 engineering workflow
- 可用于哪个表格或图：structural-analysis family table；`09 / 01.04` 边界说明
- 适合作为代表性案例吗：可作为工程 workflow 样本
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：two-stage architecture；accuracy summary
- 需要与哪些论文并列比较：Liang_2025_MASSE_Structural_Engineering; Liang_2025_Automated_Structural_Analysis; Geng_2026_Agentic_3D_Frame_Analysis

## 9. 总结

### 9.1 一句话概括

跨 ETABS / SAP2000 / OpenSees 自动做结构分析。

### 9.2 速记版 pipeline

1. 读结构题
2. 抽统一 JSON
3. 并行翻译多平台脚本
4. 做结构分析
5. 输出结果

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：09
二级类：09.05
三级类：跨平台结构分析与 FEA 建模
四级专题：Cross-platform structural-analysis agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; simulation_modeling; tool_use_and_code_execution; data_analysis; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; multi_agent_collaboration; environment_interaction
验证方式：benchmark; simulation_validation
交叉属性：computation_driven; simulation_driven
科学贡献类型：system_platform
证据强度：simulation_supported
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
