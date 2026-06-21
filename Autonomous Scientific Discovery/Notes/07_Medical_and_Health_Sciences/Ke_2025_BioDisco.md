# Ke et al. 2025 - BioDisco: Multi-agent hypothesis generation with dual-mode evidence, iterative feedback and temporal evaluation

## 2026-06-21 relaxed round-2 boundary closure

- `scientific_object_modules`: `07;06`
- `object_coverage_mode`: `multi_module`
- `primary_module_for_filing`: `07`
- `general_method_bucket`: `none`
- `first_hand_sources_checked`: arXiv abstract / version page `2508.01285`; ar5iv full text `2508.01285v2`; official GitHub `yujingke/BioDisco`; official PyPI `biodisco`
- `classification_evidence_source_level`: `first_hand_full_text`
- `note_revision_required`: `no`

This round closes the `07 / 06` boundary as `07;06`. `07` remains primary because BioDisco is explicitly framed as biomedical hypothesis generation and its strongest evaluation domains are cardiovascular medicine and NSCLC immunotherapy. At the same time, the full text also exposes independent life-science object coverage through genes, proteins, biological pathways, gene-gene / disease-gene / chemical-gene benchmark relations, vascular smooth muscle cells, macrophages, CD8+ T-cell exhaustion, and explicit biological-mechanism / interaction prompts. Under the current relaxed object-coverage rule, that is enough to add `06`.

**论文信息**
- 标题：BioDisco: Multi-agent hypothesis generation with dual-mode evidence, iterative feedback and temporal evaluation
- 作者：Yujing Ke; Kevin George; Kathan Pandya; David Blumenthal; Maximilian Sprang; Gerrit Grossmann; Sebastian Vollmer; David Antony Selby
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2508.01285
- PDF / 本地文件路径：当前笔记基于 arXiv HTML / PDF 全文
- 论文类型：系统论文 / biomedical hypothesis-generation agents
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv HTML 摘要与 Figure 1 | 系统由多个 agents 结合知识图谱、文献检索、internal scoring 与 feedback loop 生成并修正 biomedical hypotheses | 高 |
| 科学对象归类 | `07.04` | 任务定义、评测与案例 | 任务、评测与案例都锚定在疾病、免疫学、心血管与治疗靶点相关 biomedical questions | 高 |
| 方法流程 | 多步闭环 | 系统流程描述 | planner 统筹 graph / literature evidence retrieval、hypothesis generation、critic scoring 与 refinement | 高 |
| 边界判断 | 不退回 `01.04` | 贡献与案例 | 虽有 framework 形态，但直接对象是 biomedical hypothesis discovery，而非通用科研平台 | 高 |
| 验证方式 | temporal + expert evaluation | 评测部分 | 通过时间切分评测、人类专家评估和 Bradley-Terry 对比验证假设质量 | 中高 |

## 0. 摘要翻译

论文提出 BioDisco，一个面向生物医学假设生成的多 Agent 框架。系统同时利用文献检索与生物医学知识图谱这两类证据源，通过内部评分与反馈循环迭代优化假设，并使用时间切分评测、人类专家评估和 Bradley-Terry 模型验证所生成假设的新颖性与重要性。它的重点不是通用科研能力平台，而是围绕疾病机制、免疫学和治疗靶点的 biomedical hypothesis discovery。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具有明确科研目标、多 Agent 分工、检索增强、反馈迭代、自主筛选与修正
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：假设生成、文献检索与阅读、证据评估与验证、反馈迭代

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：07
- 二级类：07.04
- 三级类：biomedical hypothesis discovery
- 四级专题：therapeutic-target and disease-mechanism hypothesis agents
- 四级专题是否为新增：否
- 归类理由：具体任务、评测与专家评价都锚定在疾病、免疫、心血管与治疗靶点相关 biomedical questions，而不是领域无关研究平台
- 归类置信度：中高

### 2.2 对象优先判定

- 最终科学研究对象：疾病机制、免疫学与治疗靶点相关的 biomedical hypotheses
- 最终科学问题：如何在 biomedical evidence space 中自动生成、评分并迭代修正高价值假设
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：framework 形态只是实现方式，最终对象仍是 biomedical hypothesis discovery

### 2.3 容易混淆的边界

- 可能误归类到：06.03；01.04
- 最终判定：暂保持 07.04
- 判定理由：最强案例与评测都偏 disease / therapeutic target / health relevance，而不是纯基础生命机制或通用 scientific-agent substrate
- 是否需要二次复核：是

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：biomedical KG + literature dual-evidence agents

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：部分是
- 假设生成：是
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：部分是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：部分是
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
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：是
- 数字孪生：否
- 机器人平台：否
- 其他：literature-grounded hypothesis discovery

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：biomedical hypothesis discovery 依赖异构证据整合，人工探索成本高
- 现有科研流程或方法的痛点：知识图谱与文献各自不完整，单一路径难以稳定生成高质量 hypotheses
- 核心假设或直觉：双模证据 + multi-agent critic loop 能提升 biomedical hypothesis generation 的质量与新颖性

### 4.2 系统流程

1. 输入：biomedical research topic / hypothesis goal
2. 任务分解 / 规划：planner 组织 evidence construction
3. 工具、数据库、模型或实验平台调用：knowledge graph retrieval、literature retrieval、hypothesis generation、critic scoring
4. 中间结果反馈：根据 internal scoring 决定 refined or discarded
5. 决策或迭代：持续修正 hypothesis
6. 输出：具有新颖性与重要性评分的 biomedical hypotheses

### 4.3 系统组件

- Agent 核心：planner + hypothesis generators + critics
- 工具 / API / 数据库：biomedical knowledge graphs、literature retrieval tools
- 记忆或状态模块：evidence context 与 scoring history
- 规划器：有
- 评估器 / verifier：critic / Bradley-Terry / expert evaluation
- 人类反馈或专家介入：用于最终质量评估
- 实验平台或仿真环境：temporal split evaluation

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：unseen biomedical findings；TruthHypo 中的 chemical-gene、gene-gene、gene-disease 关系
- 任务设置：根据双模证据生成并比较 biomedical hypotheses
- 对比基线：paired comparison / Bradley-Terry ranking
- 评价指标：新颖性、重要性、专家偏好
- 关键结果：在 temporal evaluation 与 human expert evaluation 中表现稳定
- 是否有消融实验：当前笔记未细化
- 是否有失败案例或负结果：当前笔记未细化

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：能提出高质量 biomedical hypotheses，但直接实验确认仍弱
- 科学贡献是否经过验证：部分是
- 贡献强度判断：中
- 科学贡献类型：假设 / 系统平台
- 证据强度：专家确认

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单次 hypothesis generation，而是 dual-evidence + critic feedback 的多 Agent 流程
- 与已有 Agent / 科研智能系统的区别：对象更聚焦于 biomedical hypothesis discovery，而非通用 scientific workflow
- 与同一科学领域其他 Agent 文献的关系：可与 CAR-T、drug-discovery、virtual-pharma 类 `07.04` 记录并列，也可作为 `07.04 / 06.03` 边界样本
- 主要创新点：文献与知识图谱双模证据驱动的迭代式假设发现

## 7. 局限性与风险

- Agent 自主性不足：仍依赖外部知识图谱和文献检索质量
- 科学验证不足：主要是 temporal / expert evaluation，缺少实验性 biomedical validation
- 泛化性不足：framework 色彩较强，存在 `07.04 / 06.03 / 01.04` 边界压力
- 工具链依赖：强依赖 KG 与 literature stack
- 数据泄漏或 benchmark 偏差：需后续核查 temporal split 设置
- 成本、可复现性或安全风险：专家评估成本较高

## 8. 对综述写作的价值

- 可放入哪个章节：07.04 生物医药 / 药学中的 hypothesis-generation agents
- 可支撑哪个论点：Agent 已开始承担 biomedical hypothesis discovery 与 evidence refinement
- 可用于哪个表格或图：07 类边界样本对照表
- 适合作为代表性案例吗：可作为边界代表样本
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：Figure 1；immunology 与 cardiovascular case studies
- 需要与哪些论文并列比较：ASD-0716；ASD-0113；ASD-0126

## 9. 总结

### 9.1 一句话概括

结合知识图谱与文献证据的 biomedical hypothesis-generation 多 Agent 系统。

### 9.2 速记版 pipeline

1. 构建 biomedical 背景
2. 检索知识图谱与文献
3. 生成候选假设
4. critic 评分并迭代修正
5. 输出高价值 biomedical hypotheses

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：07
二级类：07.04
三级类：biomedical hypothesis discovery
四级专题：therapeutic-target and disease-mechanism hypothesis agents
Agent 类型：LLM Agent; Multi-Agent System; Retrieval-augmented Agent; Hybrid Agent
科研流程角色：hypothesis_generation; literature_search_and_reading; evidence_assessment_and_validation; feedback_iteration
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven; knowledge_graph
科学贡献类型：hypothesis; system_platform
证据强度：high_primary_pdf
归类置信度：中高
纳入置信度：高
推荐引用强度：standard
```
