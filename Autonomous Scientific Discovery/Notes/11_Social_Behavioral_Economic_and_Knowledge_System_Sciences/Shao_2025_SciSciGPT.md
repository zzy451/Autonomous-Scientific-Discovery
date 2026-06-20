# Shao et al. 2025 - SciSciGPT: advancing human-AI collaboration in the science of science

**论文信息**
- 标题：SciSciGPT: advancing human-AI collaboration in the science of science
- 作者：Erzhuo Shao; Dashun Wang
- 年份：2025
- 来源 / venue：Nature Computational Science
- DOI / arXiv / URL：https://doi.org/10.1038/s43588-025-00906-6
- PDF / 本地文件路径：当前笔记基于期刊 research article 摘要与 reviewer 一手全文证据；Research Briefing `10.1038/s43588-025-00935-1` 不是 canonical research paper
- 论文类型：研究论文 / science-of-science AI collaborator
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Canonical metadata | 研究文与 briefing 需区分 | Nature page | Research Briefing 页面明确说明其是对研究文的 summary | 高 |
| Agent 纳入 | 是 | 摘要 / 正文 | SciSciGPT 被定义为面向 science of science 的 open-source AI collaborator | 高 |
| 科学对象归类 | `11.07` | 摘要 / 正文 | 研究对象是 science of science，而非通用 research-agent platform | 高 |
| 方法流程 | 多步 workflow | 补充材料 / 正文 | 系统自动化复杂 scholarly-data-driven workflows，支持多条分析路径与迭代澄清 | 高 |
| 数据与场景 | 强 Scholarly-data anchoring | Extended Data / supplementary | 连接 SciSciNet，案例覆盖 collaboration、disruption、team science 等典型 `11.07` 对象 | 高 |

## 0. 摘要翻译

论文提出 SciSciGPT，一个面向 science-of-science 的开源 AI collaborator，用于自动化复杂研究流程并提升可复现性。系统以 scholarly data repositories 为底座，支持多种分析路径、交互式澄清与结果生成。作者通过多个 science-of-science use cases 展示该系统在研究设计、数据分析和 workflow prototyping 上的潜力。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：面向明确 research goal，执行多步 scholarly-data workflow，具备工具调用、迭代修正和明确科研角色
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：部分是
  - 多 Agent 协作：部分是
- 在科研流程中承担的明确角色：文献与数据组织、分析设计、结果解释、迭代澄清

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：11
- 二级类：11.07
- 三级类：science-of-science workflow automation
- 四级专题：scholarly-data AI collaborator
- 四级专题是否为新增：否
- 归类理由：对象稳定落在 scientific knowledge production 与 scholarly-data-driven SciSci research
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：science of science / scientific knowledge production
- 最终科学问题：如何用 AI collaborator 加速并提高 SciSci 研究 workflow 的可复现性
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：其平台外观不能覆盖对象优先原则；它不是领域无关科研平台

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 11.07
- 判定理由：从数据仓、案例到研究问题，都稳定指向 science of science
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：部分是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：是
- Hybrid Agent：是
- 其他：science-of-science AI collaborator

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：部分是
- 假设生成：部分是
- 实验设计：否
- 仿真建模：部分是
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：部分是
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：部分是
- 多 Agent 协作：部分是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：部分是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：部分是
- 数字孪生：否
- 机器人平台：否
- 其他：scholarly data lake

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：SciSci workflow 复杂、迭代快、复现成本高
- 现有科研流程或方法的痛点：跨数据库、跨分析路径、跨问题设定的原型开发效率低
- 核心假设或直觉：如果给 AI collaborator 一个 domain-grounded scholarly-data environment，就能显著提升 SciSci 研究效率

### 4.2 系统流程

1. 输入：science-of-science research question
2. 任务分解 / 规划：拆解为数据检索、分析设计、结果解释等子任务
3. 工具、数据库、模型或实验平台调用：连接 SciSciNet 等 scholarly-data resources
4. 中间结果反馈：根据用户或内部结果做 clarification / correction
5. 决策或迭代：继续执行或修正分析路径
6. 输出：可复现实验流程与分析结果

### 4.3 系统组件

- Agent 核心：SciSciGPT
- 工具 / API / 数据库：SciSciNet 和其他 scholarly data resources
- 记忆或状态模块：任务上下文和分析状态
- 规划器：有
- 评估器 / verifier：use-case-based validation
- 人类反馈或专家介入：iterative clarification
- 实验平台或仿真环境：science-of-science analysis environment

## 5. 实验与验证

### 5.1 验证方式

- benchmark：否
- 仿真验证：部分是
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：部分是
- 专家评估：部分是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：SciSciNet 与多组 science-of-science cases
- 任务设置：collaboration, confounding, disruption, team science literature synthesis 等
- 对比基线：传统手工 workflow
- 评价指标：workflow usability、reproducibility 与分析完成情况
- 关键结果：支持复杂 SciSci workflow prototyping 与 reproducibility improvement
- 是否有消融实验：当前摘要级信息有限
- 是否有失败案例或负结果：当前笔记未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏 science-of-science research workflow acceleration
- 科学贡献是否经过验证：是
- 贡献强度判断：中高
- 科学贡献类型：system_platform
- 证据强度：中高

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：直接研究 scientific knowledge production 本身
- 与已有 Agent / 科研智能系统的区别：不是通用科研平台，而是 domain-grounded SciSci collaborator
- 与同一科学领域其他 Agent 文献的关系：可与 CiteME、citation-network simulations、peer-review agents 放在 `11.07`
- 主要创新点：把 science-of-science data environment 接到 AI collaborator

## 7. 局限性与风险

- Agent 自主性不足：仍强调 collaboration 而非完全替代研究者
- 科学验证不足：更多是 workflow 能力验证，而不是单一定量 benchmark
- 泛化性不足：主要面向 SciSci data-rich workflows
- 工具链依赖：依赖 scholarly datasets 的结构化可获得性
- 数据泄漏或 benchmark 偏差：需持续警惕
- 成本、可复现性或安全风险：主风险是 metadata/title pairing 混淆，而不是分类不稳

## 8. 对综述写作的价值

- 可放入哪个章节：`11.07` 科学系统与知识生产研究
- 可支撑哪个论点：domain-grounded scholarly AI collaborator 应进入 `11.07`，而非 `01.04`
- 可用于哪个表格或图：knowledge-production agent 样本表
- 适合作为代表性案例吗：是
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：研究文与 briefing 配对说明
- 需要与哪些论文并列比较：ASD-0629、ASD-0637、peer-review agents

## 9. 总结

### 9.1 一句话概括

面向 science-of-science 的 AI collaborator，应稳归 `11.07`。

### 9.2 速记版 pipeline

1. 读入 SciSci 研究问题  
2. 拆解数据与分析任务  
3. 调 scholarly datasets / tools  
4. 迭代澄清并输出结果

### 9.3 标注字段汇总

```text
是否纳入：是
主类：11
二级类：11.07
三级类：science-of-science workflow automation
四级专题：scholarly-data AI collaborator
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; environment_interaction
验证方式：real_world_deployment
交叉属性：computation_driven; data_driven
科学贡献类型：system_platform
证据强度：medium_high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
