# Shen et al. 2025 - An industrial automated laboratory for programmable protein evolution

**论文信息**
- 标题：An industrial automated laboratory for programmable protein evolution
- 作者：Da Shen, Xin Wang, Yuan Gao, Wei Wang, Yuchao Li, He Chen, Yushuai Guo, Shuaihua Cao, Yuqing Huang, Yan Zhang, Chengzhi Wang, Shuyi Zhang
- 年份：2025
- 来源 / venue：Nature Chemical Engineering
- DOI / arXiv / URL：https://doi.org/10.1038/s44286-025-00303-w
- PDF / 本地文件路径：本轮依据 Nature publisher page、摘要与图题级材料整理，尚未取得稳定全文 PDF
- 来源状态：source_limited=yes（本轮仍以 publisher page、摘要与图题级材料为主；冻结归类稳定为 `06`，但不能表述成已完成全文核对）
- 论文类型：研究论文 / automated protein-evolution laboratory
- 当前状态：to_read / confirmed core
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | publisher abstract | iAutoEvoLab 被描述为 industrial-grade automation platform，可在 minimal human intervention 下长期运行 | 中高 |
| 科学对象归类 | 冻结为 `06`（落盘仍写作 `06.03`） | abstract | 直接对象是 programmable protein evolution、protein adaptive landscapes 与具体蛋白功能进化 | 高 |
| 方法流程 | 长程自动化实验闭环 | abstract; Fig. 1; Extended Data | 存在 dynamic scheduling、loop control、branch switching、process termination 与 error handling | 中高 |
| 实验验证 | 强 | abstract | 对 LldR、LmrA、CapT7 等蛋白系统做真实进化实验，CapT7 从 inactive precursors 演化出功能 | 中高 |
| 来源状态 | source_limited=yes | publisher page / abstract / figure-title materials | 当前仍未取得稳定全文 PDF，但页面级一手证据已足以维持冻结 `06` | 中高 |
| 边界判断 | 不转 `07` 或 `09` | object-first review | 虽有 industrial lab framing，但 automation 是手段，稳定对象仍是蛋白工程 | 高 |

## 0. 摘要翻译

这篇论文提出工业级自动化蛋白进化实验室 iAutoEvoLab，目标是把连续、可扩展、最小人工干预的 protein evolution 做成长期稳定运行的平台。系统把自动化硬件、动态调度软件、OrthoRep 连续进化回路以及针对不同蛋白功能的遗传电路整合起来，在真实实验中完成 LldR、LmrA 和 CapT7 等蛋白系统的可编程进化。就综述口径看，它的主对象始终是蛋白功能与蛋白进化，而不是实验自动化基础设施本身，因此更适合归入生命科学中的 protein engineering 支线。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：明确科研目标、长程多步行动、自动实验执行、动态调度、结果反馈与后续进化决策都已出现
- 判定置信度：中高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：未突出为软件多 Agent，但系统性调度明确存在
- 在科研流程中承担的明确角色：实验调度、进化执行、筛选控制、错误处理、流程终止/切换

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：06
- 冻结归类结论：06（生命科学）
- 二级类：06.03
- source_limited：yes
- 三级类：programmable protein evolution / protein engineering
- 四级专题：Programmable protein-evolution automated laboratories
- 四级专题是否为新增：否
- 归类理由：系统的直接研究对象是蛋白功能、蛋白进化与 adaptive landscape
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：LldR、LmrA、CapT7 等蛋白系统及其功能进化
- 最终科学问题：如何在自动化平台上长期、可编程地执行 protein evolution
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：industrial laboratory 是手段层叙述，稳定科学对象是蛋白工程而非实验室工程

### 2.3 容易混淆的边界

- 可能误归类到：07、09
- 最终判定：冻结为 06（生命科学；落盘仍写作 06.03）
- 判定理由：不是患者、疾病或药物转化，也不是工程装置本体论文
- 是否需要二次复核：是，主要为补足全文方法细节

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：否
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：否
- Robot / Embodied Agent：是
- Human-in-the-loop Agent：弱
- Hybrid Agent：是
- 其他：industrial automated evolution lab

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：否
- 科学问题提出：否
- 假设生成：部分是
- 实验设计：是
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：是
- 数据分析：是
- 结果解释：部分是
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
- 多 Agent 协作：未见稳定证据
- 环境交互：是
- 闭环实验：是

### 3.4 交叉属性标签

- 计算驱动：否
- 数据驱动：是
- 实验驱动：是
- 仿真驱动：否
- 多模态：否
- 多尺度建模：否
- 高通量筛选：是
- 知识图谱：否
- 数字孪生：否
- 机器人平台：是
- 其他：industrial-grade automation

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：连续蛋白进化要实现长期稳定运行、动态切换和最小人工干预，传统实验室很难做到
- 现有科研流程或方法的痛点：自动化硬件、进化回路和任务调度长期分离
- 核心假设或直觉：如果把 industrial automation、genetic circuits 和 dynamic scheduling 统一起来，就能实现可编程的长期 protein evolution

### 4.2 系统流程

1. 输入：目标蛋白功能与进化任务
2. 任务分解 / 规划：设定回路、调度进化阶段与分支切换
3. 工具、数据库、模型或实验平台调用：自动化实验室执行培养、筛选与控制
4. 中间结果反馈：依据结果做 loop control、error handling 和 branch switching
5. 决策或迭代：继续进化或终止流程
6. 输出：具有目标功能的演化蛋白系统

### 4.3 系统组件

- Agent 核心：iAutoEvoLab
- 工具 / API / 数据库：industrial automation hardware、OrthoRep、genetic circuits、dynamic scheduling software
- 记忆或状态模块：process state、loop state、termination state
- 规划器：dynamic scheduling / branch switching
- 评估器 / verifier：功能筛选与结果判定
- 人类反馈或专家介入：最小
- 实验平台或仿真环境：真实工业级自动化蛋白进化平台

## 5. 实验与验证

### 5.1 验证方式

- benchmark：否
- 仿真验证：否
- 高通量计算：否
- 机器人实验：是
- 湿实验：是
- 临床数据：否
- 真实场景部署：实验室真实长期运行平台
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：LldR、LmrA、CapT7 等蛋白系统
- 任务设置：programmable continuous protein evolution
- 对比基线：当前摘要未展开
- 评价指标：功能演化成功、长期运行、可靠性
- 关键结果：多个蛋白系统得到真实进化，CapT7 从 inactive precursors 演化为 functional entity
- 是否有消融实验：当前摘要未展开
- 是否有失败案例或负结果：当前摘要未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要贡献是长期蛋白进化自动化与功能获得
- 科学贡献是否经过验证：是
- 贡献强度判断：强
- 科学贡献类型：系统平台 / 实验发现
- 证据强度：高质量摘要级实验支持

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：直接执行真实长期 protein evolution
- 与已有 Agent / 科研智能系统的区别：强调 industrial-grade、长期运行、动态调度与错误处理
- 与同一科学领域其他 Agent 文献的关系：可与 0599、0618 一起构成蛋白工程自动化主线
- 主要创新点：把 programmable evolution 与工业级自治实验室整合为统一平台

## 7. 局限性与风险

- Agent 自主性不足：当前仍主要从摘要/图题确认，具体自主深度需全文补足
- 科学验证不足：全文方法和量化结果尚未完整入手
- 泛化性不足：当前案例集中在少数蛋白系统
- 工具链依赖：高度依赖专用工业级自动化实验室
- 数据泄漏或 benchmark 偏差：非主风险
- 成本、可复现性或安全风险：平台复制门槛高
- 是否仍需后续全文复核：是；当前仍以 publisher page、摘要与图题级材料为主，因此保留 source_limited=yes，但冻结 `06` 结论不变

## 8. 对综述写作的价值

- 可放入哪个章节：生命科学 / programmable protein evolution
- 可支撑哪个论点：蛋白工程方向已经出现长周期、最小人工干预的自治实验室
- 可用于哪个表格或图：protein-evolution platform comparison
- 适合作为代表性案例吗：适合
- 推荐引用强度：标准到核心之间
- 需要在正文中特别引用的页码 / 图 / 表：Fig. 1 与 extended data scheduling elements
- 需要与哪些论文并列比较：ASD-0599, ASD-0618

## 9. 总结

### 9.1 一句话概括

面向 programmable protein evolution 的工业级自治实验室。

### 9.2 速记版 pipeline

1. 设定蛋白进化任务
2. 自动化实验室持续执行进化
3. 动态调度与分支切换
4. 根据结果继续筛选/终止
5. 得到具目标功能的蛋白系统

### 9.3 标注字段汇总

```text
是否纳入：是
主类：06
二级类：06.03
三级类：programmable protein evolution / protein engineering
四级专题：Programmable protein-evolution automated laboratories
Agent 类型：Planning Agent; Tool-using Agent; Robot / Embodied Agent; Hybrid Agent
科研流程角色：experimental_design; tool_use_and_code_execution; experiment_execution; data_analysis; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; environment_interaction; closed_loop_experimentation
验证方式：robotic_experiment; wet_lab_experiment; real_world_deployment
交叉属性：data_driven; experiment_driven; high_throughput_screening; robotic_platform
科学贡献类型：system_platform; experimental_discovery
证据强度：medium_high_primary_abstract
归类置信度：高
纳入置信度：中高
推荐引用强度：standard
```
