# Cakir and Yerlikaya 2026 - From Experimental Limits to Physical Insight: A Retrieval-Augmented Multi-Agent Framework for Interpreting Searches Beyond the Standard Model

**论文信息**
- 标题：From Experimental Limits to Physical Insight: A Retrieval-Augmented Multi-Agent Framework for Interpreting Searches Beyond the Standard Model
- 作者：Altan Cakir; Ayca Yerlikaya
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2605.02491
- PDF / 本地文件路径：已核对 arXiv PDF 全文，并参考 arXiv 页面元数据
- 论文类型：系统论文 / particle-physics interpretation agent
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Abstract | retrieval-augmented multi-agent AI framework for exploration and interpretation of HEP literature | 高 |
| 科学对象归类 | `02.02` | Title; Abstract | 对象是 BSM collider searches、HEPData、exclusion limits 与 particle-physics constraints | 高 |
| 多步行动流程 | 明确存在 | Sec. 3; Fig. 1 | query interpretation、retrieval、planning/reasoning、synthesis 构成可迭代工作流 | 高 |
| 工具调用 | 明确存在 | Abstract; Sec. 3 | 调用 publications、HEPData、plots reconstruction 等外部证据源 | 高 |
| 验证方式 | case study / computational | Sec. 5.4 | 使用 recent CMS searches 做案例，重建 exclusion limits 并跨论文比较 constraints | 中高 |
| 边界判断 | 不应移入 `01.04` | Introduction; Sec. 2.6 | 系统虽有平台外观，但实验、案例和贡献都绑定高能粒子物理对象 | 高 |

## 0. 摘要翻译

现代超越标准模型搜索产生了快速增长且异构的文献，包括文本分析、数值数据集和图形排除极限。整合这些分散来源通常既耗时又依赖人工。本文提出 HEP-CoPilot，一个 retrieval-augmented multi-agent AI framework，用于高能粒子物理文献的探索与解释。系统统一整合论文文本、HEPData 结构化实验数据和重建物理图像，并通过 coordinated agent workflows 实现对实验分析的 evidence-grounded reasoning 和 collider 结果的结构化解释。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统有明确科研目标、多步检索与解释流程、外部证据调用、综合推理与结果输出
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：部分是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：文献检索与阅读、证据评估与验证、工具调用与代码执行、结果解释

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：02
- 二级类：02.02
- 三级类：高能粒子物理实验结果解释
- 四级专题：BSM search interpretation agents
- 四级专题是否为新增：否
- 归类理由：系统直接服务于 collider search interpretation，而非领域无关 research-agent substrate
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：BSM 搜索结果、HEPData、排除极限与粒子物理约束
- 最终科学问题：如何让 Agent 自动整合分散证据并解释高能物理实验约束
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：RAG 和 multi-agent 只是方法，主对象仍是高能粒子物理

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保持 02.02
- 判定理由：任务、数据源、案例和贡献都直接绑定 HEP 对象与 CMS analyses
- 是否需要二次复核：否，主类判断已较稳

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
- 其他：Particle-physics literature interpretation agent

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：否
- 假设生成：否
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
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
- 记忆与状态维护：是
- 反馈迭代：部分是
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
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：HEPData / plot reconstruction

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：BSM 搜索文献和数据来源快速增长，人工整合成本高
- 现有科研流程或方法的痛点：需要跨论文、跨数据表和图形手工比较实验约束
- 核心假设或直觉：RAG 与多 Agent 工作流可以把异构粒子物理证据整合成 physics-aware interpretation

### 4.2 系统流程

1. 输入：高能粒子物理查询或待解释的 BSM 搜索问题
2. 任务分解 / 规划：Mission Control / Router 解析查询并分发子任务
3. 工具、数据库、模型或实验平台调用：调用 publications、HEPData、plots reconstruction
4. 中间结果反馈：返回检索结果、重建约束与跨论文比较信息
5. 决策或迭代：综合物理证据形成解释
6. 输出：physics-aware explanation 与 constraint comparison

### 4.3 系统组件

- Agent 核心：Mission Control / specialized agents
- 工具 / API / 数据库：论文文本; HEPData; plot reconstruction
- 记忆或状态模块：任务上下文
- 规划器：有
- 评估器 / verifier：evidence-grounded synthesis
- 人类反馈或专家介入：低
- 实验平台或仿真环境：粒子物理文献与数据环境

## 5. 实验与验证

### 5.1 验证方式

- benchmark：否
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：部分是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：recent CMS BSM searches
- 任务设置：检索测量、重建 exclusion limits、跨论文比较 constraints
- 对比基线：人工整合流程
- 评价指标：case-study usefulness 与解释能力
- 关键结果：能够从 HEPData 重建限制并支持跨论文一致比较
- 是否有消融实验：当前笔记未完整确认
- 是否有失败案例或负结果：作者承认评估规模仍小

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏粒子物理证据整合与解释，而非直接新物理发现
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：explanation / system_platform
- 证据强度：计算验证

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单次高能物理问答，而是多步证据整合与结果解释
- 与已有 Agent / 科研智能系统的区别：对象稳定落在 HEP experiment interpretation
- 与同一科学领域其他 Agent 文献的关系：可与量子实验、多信使天文学 Agent 形成 class-02 样本群
- 主要创新点：整合 publications、HEPData 和 plots 的 evidence-grounded multi-agent interpretation

## 7. 局限性与风险

- Agent 自主性不足：仍主要是解释与比较，不是自主实验设计
- 科学验证不足：案例规模有限
- 泛化性不足：当前主要围绕 CMS analyses
- 工具链依赖：强依赖 HEPData 和本地数据重建
- 数据泄漏或 benchmark 偏差：当前未见明确数据泄漏讨论，主要风险仍是案例规模有限与跨搜索泛化证据不足
- 成本、可复现性或安全风险：核心风险是 core-strength，而非主类方向

## 8. 对综述写作的价值

- 可放入哪个章节：02 物理学中的 high-energy physics interpretation agents
- 可支撑哪个论点：看似通用的 research co-pilot 仍可能因对象稳定而应留在具体物理类
- 可用于哪个表格或图：02 / 01.04 边界表；证据整合型 Agent 对照表
- 适合作为代表性案例吗：适合
- 推荐引用强度：standard
- 需要在正文中特别引用的页码 / 图 / 表：Fig. 1; Sec. 5.4
- 需要与哪些论文并列比较：accelerator experiment agent、AI-Mandel、GW-Eyes

## 9. 总结

### 9.1 一句话概括

高能物理实验约束解释多 Agent。

### 9.2 速记版 pipeline

1. 解析粒子物理查询
2. 检索论文与 HEPData
3. 重建排除极限
4. 跨论文比较约束
5. 输出物理解释

### 9.3 标注字段汇总

```text
是否纳入：是
主类：02
二级类：02.02
三级类：高能粒子物理实验结果解释
四级专题：BSM search interpretation agents
Agent 类型：LLM Agent; Multi-Agent System; Retrieval-augmented Agent; Hybrid Agent
科研流程角色：literature_search_and_reading; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation
自主能力：task_decomposition; planning; tool_use; autonomous_decision_making; multi_agent_collaboration
验证方式：computational_validation
交叉属性：computation_driven; data_driven; multimodal
科学贡献类型：explanation; system_platform
证据强度：computationally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
