# Jin et al. 2025 - BioLab: End-to-End Autonomous Life Sciences Research with Multi-Agents System Integrating Biological Foundation Models

## 2026-06-20 relaxed multi-module revision

```text
scientific_object_modules: 06;07
object_coverage_mode: multi_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 06
first_hand_sources_checked: bioRxiv DOI landing / abstract-level first-hand page
classification_evidence_source_level: first_hand_abstract_or_landing_page
module_assignment_evidence: 06 is supported by DNA/RNA/protein/cell life-science tasks and biological-foundation-model tool use. 07 is supported by macrophage-targeting antibody design, PD-1 / pembrolizumab optimization, IC50 assays, and therapeutic validation.
multi_module_object_coverage_note: BioLab is still filed primarily under life sciences, but therapeutic antibody optimization and assay evidence are concrete biomedical object coverage, so 07 is added.
```

**论文信息**
- 标题：BioLab: End-to-End Autonomous Life Sciences Research with Multi-Agents System Integrating Biological Foundation Models
- 作者：Ruofan Jin; Yucheng Guo; Yuanhao Qu; Ming Yang; Chun Shang; Qirong Yang; Linlin Chao; Yi Zhou; Ruilai Xu; Ziyao Xu; Ruhong Zhou; Zaixi Zhang; Mengdi Wang; Xiaoming Zhang; Le Cong
- 年份：2025
- 来源 / venue：bioRxiv
- DOI / arXiv / URL：https://doi.org/10.1101/2025.09.03.674085
- PDF / 本地文件路径：当前笔记基于 bioRxiv / Semantic Scholar 检索页与 reviewer 一手证据；本地未保存 PDF
- 论文类型：研究论文 / end-to-end life-science multi-agent system
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | bioRxiv snippet / reviewer evidence | 论文明确把 `BioLab` 描述为 multi-agent system for end-to-end biological research | 高 |
| 科学对象归类 | `06.03` | abstract summary / reviewer evidence | 虽然任务范围宽，但对象始终在 life-science discovery across DNA/RNA/protein/cell/chemical scales | 高 |
| 方法流程 | planner/reasoner/critic/memory + 219 xBio tools | reviewer evidence | 八个 agents 协作调用 biological foundation models 和工具链 | 高 |
| 边界判断 | 不应改到 `01.04` | object-first rule | 覆盖面广不等于领域无关；论文的任务、工具和实验验证都在生命科学内部 | 高 |
| 实验验证 | antibody design pipeline + validation | reviewer evidence | 从 target mining 到 multi-objective optimization，再到 biological validation | 高 |

## 0. 摘要翻译

`BioLab` 是一个面向生命科学研究的 end-to-end multi-agent system。它把八个不同职责的 agents 与大量 biological foundation models 和 xBio tools 组合起来，覆盖从目标挖掘、推理、优化到结果验证的完整研究流程。虽然它呈现出很强的平台感，而且任务横跨 DNA、RNA、蛋白、细胞和化学多个尺度，但这些任务都仍属于 concrete life-science discovery，因此主类应维持在 `06.03`，而不是回退到 `01.04`。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在多 Agent 协作、工具调用、规划、批评/修正和端到端生命科学研究流程
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：目标挖掘、研究规划、模型调用、优化、验证

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：06
- 二级类：06.03
- 三级类：end-to-end life-science discovery workflow
- 四级专题：End-to-end autonomous life-science research systems
- 四级专题是否为新增：否
- 归类理由：尽管系统覆盖范围广，但工具链、任务集和实验验证都稳定落在生命科学内部
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：DNA/RNA/protein/cell/chemical-scale life-science tasks
- 最终科学问题：如何把 biological foundation models 和 multi-agent workflow 组合成端到端生命科学研究系统
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：多 Agent 平台结构只是手段，稳定对象仍是生命科学研究问题

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保持 06.03
- 判定理由：如果一个系统既不依赖 biological tools，也没有 biological validation，才更像 `01.04`；而 BioLab 恰恰相反
- 是否需要二次复核：对 top-level class 不需要

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：部分是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：biological foundation-model orchestration system

### 3.2 科研流程角色

- 文献检索与阅读：部分是
- 知识抽取与组织：是
- 科学问题提出：是
- 假设生成：是
- 实验设计：是
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
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：部分是
- 闭环实验：部分是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：部分是
- 仿真驱动：部分是
- 多模态：是
- 多尺度建模：是
- 高通量筛选：部分是
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：biological foundation models

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：实现从目标定义到验证的端到端生命科学研究自动化
- 现有科研流程或方法的痛点：生命科学工具分散，多尺度任务间切换成本高
- 核心假设或直觉：如果把生物基础模型和多 Agent 系统统一起来，就能构建更完整的 life-science research loop

### 4.2 系统流程

1. 输入：life-science research task
2. 任务分解 / 规划：Planner、Reasoner、Critic、Memory 等 agents 协作分解任务
3. 工具、数据库、模型或实验平台调用：调用 219 个 xBio tools across biological scales
4. 中间结果反馈：Critic / Memory 等模块检查并保留状态
5. 决策或迭代：继续优化研究方案和候选
6. 输出：完成的生命科学研究 workflow 与优化结果

### 4.3 系统组件

- Agent 核心：BioLab
- 工具 / API / 数据库：219 xBio-Tools + biological foundation models
- 记忆或状态模块：Memory Agent
- 规划器：Planner Agent
- 评估器 / verifier：Critic Agent and biological validation
- 人类反馈或专家介入：当前公开证据未完全展开
- 实验平台或仿真环境：multi-scale biological research environment

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：部分是
- 高通量计算：否
- 机器人实验：否
- 湿实验：部分是
- 临床数据：否
- 真实场景部署：否
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：DNA/RNA/protein/cell/chemical scale life-science tasks
- 任务设置：end-to-end autonomous biological research
- 对比基线：current public evidence not fully expanded
- 评价指标：workflow completion, design quality, biological task performance
- 关键结果：在 antibody-design pipeline 上实现从 target mining 到 multi-objective optimization 并报告 improved PD-1 antibody performance
- 是否有消融实验：当前笔记未展开
- 是否有失败案例或负结果：未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：具备较强 life-science discovery orientation
- 科学贡献是否经过验证：是
- 贡献强度判断：中高
- 科学贡献类型：system_platform; bioinformatics_discovery
- 证据强度：medium_high_preprint

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单一 biological model，而是端到端生命科学 research system
- 与已有 Agent / 科研智能系统的区别：更强调多尺度 biological foundation model integration
- 与同一科学领域其他 Agent 文献的关系：可与 VenusFactory2、BioGAIP、CellForge 共同构成 `06 / 01.04` 边界核心样本
- 主要创新点：把端到端 autonomous life-science research 放到一个统一多 Agent 系统中

## 7. 局限性与风险

- Agent 自主性不足：当前主要证据仍依赖摘要和 reviewer evidence
- 科学验证不足：需要全文确认多尺度任务是否都达到与 antibody case 同等深度
- 泛化性不足：不同 biological scales 上的一致性仍需观察
- 工具链依赖：高度依赖 xBio tools 和 foundation models
- 数据泄漏或 benchmark 偏差：当前证据不足以细评
- 成本、可复现性或安全风险：工具栈复杂，复现成本较高

## 8. 对综述写作的价值

- 可放入哪个章节：06 生命科学中的 end-to-end autonomous research systems
- 可支撑哪个论点：即使系统覆盖多尺度生命科学，只要对象稳定在生命科学内部，仍不应退回 `01.04`
- 可用于哪个表格或图：`06.03 / 01.04` 边界案例表
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：后续全文补充
- 需要与哪些论文并列比较：Tan_2026_Protein_Discovery_Directed_Evolution; BioGAIP; Jin_2025_BioLab_Life_Sciences

## 9. 总结

### 9.1 一句话概括

多 Agent 系统整合 biological foundation models 做端到端生命科学研究。

### 9.2 速记版 pipeline

1. 接收生命科学任务
2. 多 Agent 分解并调度 biological tools
3. 迭代优化与验证
4. 输出 research result

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：06
二级类：06.03
三级类：end-to-end life-science discovery workflow
四级专题：End-to-end autonomous life-science research systems
Agent 类型：LLM Agent; Multi-Agent System; Tool-using Agent; Hybrid Agent
科研流程角色：hypothesis_generation; tool_use_and_code_execution; workflow_orchestration; evidence_assessment_and_validation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; computational_validation
交叉属性：computation_driven; data_driven; multimodal; multi_scale_modeling
科学贡献类型：system_platform; bioinformatics_discovery
证据强度：medium_high_preprint
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
