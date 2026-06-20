# Tosh et al. 2025 - A Bayesian active learning platform for scalable combination drug screens

**论文信息**
- 标题：A Bayesian active learning platform for scalable combination drug screens
- 作者：Tosh et al.
- 年份：2025
- 来源 / venue：Nature Communications
- DOI / arXiv / URL：https://doi.org/10.1038/s41467-024-55287-7
- PDF / 本地文件路径：未保存本地 PDF；本笔记基于 Nature Communications 正式页面与 reviewer 一手证据
- 论文类型：research paper / classical active-learning experimental design platform
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是，但 agenticity 偏 classical | Nature abstract / results | BATCHIE 动态分批设计实验并基于上一轮结果选择下一轮药筛 | 高 |
| 科学对象归类 | `07.04` | Nature abstract / introduction | 论文围绕组合药筛、癌症细胞系和 Ewing sarcoma follow-up validation | 高 |
| 方法流程 | 贝叶斯主动学习闭环 | Results / Fig. 2-related text | 初始 batch -> 模型更新 -> 选下一批 plate -> 再实验 | 高 |
| 实验验证 | 强 | abstract / results | 只探索约 4% 的组合空间就定位高价值组合，并做前瞻性验证 | 高 |
| 边界判断 | 不应退回 `01.04` | abstract / introduction | 这是 concrete biomedical object paper；剩余风险在 core-strength 而非对象分类 | 高 |

## 0. 摘要翻译

论文提出 `BATCHIE`，用贝叶斯主动学习在批次级动态设计组合药筛实验。系统在每一轮根据已有结果选择信息量最大的下一批实验，并在大规模回顾性与前瞻性癌症药筛中证明，相比固定设计能更快发现有效且协同的药物组合。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具备明确科研目标、多轮实验设计、模型更新、反馈驱动的下一轮决策
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：部分是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：实验设计、候选优先级排序、数据分析、证据评估

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除，但应注明这是 classical active-learning agent

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：07
- 二级类：07.04
- 三级类：
- 四级专题：Active-learning platforms for combination drug screens
- 四级专题是否为新增：否
- 归类理由：直接对象是组合药物筛选、癌症药物组合发现与验证
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：癌症组合药筛与协同药物组合
- 最终科学问题：如何在极大组合空间中高效找到有效药物组合
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：贝叶斯主动学习只是手段，真正对象是组合药筛与治疗候选发现

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 07.04
- 判定理由：论文并非通用科研平台，而是具体 biomedical screening workflow
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：否
- Planning Agent：是
- Tool-using Agent：部分是
- Retrieval-augmented Agent：否
- Multi-Agent System：否
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：Bayesian active-learning controller

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：否
- 科学问题提出：否
- 假设生成：是
- 实验设计：是
- 仿真建模：是
- 工具调用与代码执行：部分是
- 实验执行：部分是
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：否
- 计划生成：是
- 工具调用：部分是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：否
- 环境交互：是
- 闭环实验：是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：是
- 仿真驱动：是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：是
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：sequential experimental design

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：组合药筛空间过大，穷举成本极高
- 现有科研流程或方法的痛点：固定设计浪费实验预算，难以快速定位高价值组合
- 核心假设或直觉：主动学习可以在有限实验预算下更快锁定协同组合

### 4.2 系统流程

1. 输入：药物集合、细胞系、初始实验批次
2. 任务分解 / 规划：用贝叶斯模型估计不确定性与价值
3. 工具、数据库、模型或实验平台调用：组合药筛实验与模型更新
4. 中间结果反馈：收集当前批次实验结果
5. 决策或迭代：选择下一批最有价值的组合
6. 输出：高价值组合候选与验证结果

### 4.3 系统组件

- Agent 核心：Bayesian active-learning planner
- 工具 / API / 数据库：combination screening data
- 记忆或状态模块：历史药筛结果
- 规划器：posterior-guided batch selection
- 评估器 / verifier：前瞻性药筛与 follow-up validation
- 人类反馈或专家介入：研究者设定实验边界
- 实验平台或仿真环境：drug-combination screening workflow

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：是
- 高通量计算：否
- 机器人实验：否
- 湿实验：是
- 临床数据：否
- 真实场景部署：否
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：206 drugs、16 cancer cell lines 等组合药筛任务
- 任务设置：动态批次实验设计与组合优选
- 对比基线：固定设计或非主动策略
- 评价指标：探索效率、hit recovery、组合发现质量
- 关键结果：仅探索约 4% 的组合空间就发现高价值组合，并对 Ewing sarcoma 做进一步验证
- 是否有消融实验：部分有
- 是否有失败案例或负结果：未重点展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是，发现高价值组合候选
- 科学贡献是否经过验证：是
- 贡献强度判断：强
- 科学贡献类型：实验发现；系统平台
- 证据强度：实验验证

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不仅做预测，还动态决定下一轮实验
- 与已有 Agent / 科研智能系统的区别：是非 LLM、classical active-learning 样式的 biomedical experimental agent
- 与同一科学领域其他 Agent 文献的关系：可作为 `07` 中 agenticity 偏 classical 但对象很稳的样本
- 主要创新点：把主动学习直接用于大规模组合药筛的 sequential experiment design

## 7. 局限性与风险

- Agent 自主性不足：比多工具 LLM agent 更窄
- 科学验证不足：否
- 泛化性不足：当前主要验证在特定 cancer screening 场景
- 工具链依赖：依赖药筛平台与模型设定
- 数据泄漏或 benchmark 偏差：需要继续关注
- 成本、可复现性或安全风险：大规模药筛成本高

## 8. 对综述写作的价值

- 可放入哪个章节：07 医疗与健康科学 / drug discovery agents
- 可支撑哪个论点：并非所有核心 biomedical agent 都是 LLM；classical active-learning controller 也可满足 Agent 最低标准
- 可用于哪个表格或图：biomedical closed-loop design systems
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：abstract、adaptive design 结果部分
- 需要与哪些论文并列比较：drug-combination / DMTA / biomedical screening agents

## 9. 总结

### 9.1 一句话概括

贝叶斯主动学习闭环加速组合药筛发现。

### 9.2 速记版 pipeline

1. 做初始组合药筛
2. 更新贝叶斯模型
3. 选下一批最值钱实验
4. 再做实验并反馈
5. 找到高价值组合

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：07
二级类：07.04
三级类：
四级专题：Active-learning platforms for combination drug screens
Agent 类型：Planning Agent; Hybrid Agent
科研流程角色：hypothesis_generation; experimental_design; data_analysis; evidence_assessment_and_validation; feedback_iteration
自主能力：planning; feedback_iteration; autonomous_decision_making; closed_loop_experimentation
验证方式：closed_loop_experiment; wet_lab_experiment; simulation_validation
交叉属性：computation_driven; data_driven; experiment_driven; high_throughput_screening
科学贡献类型：experimental_discovery; system_platform
证据强度：experimentally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```

