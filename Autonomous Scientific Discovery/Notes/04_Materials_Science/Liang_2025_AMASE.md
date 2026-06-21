# Liang et al. 2025 - Real-time experiment-theory closed-loop interaction for autonomous materials science

**论文信息**
- 标题：Real-time experiment-theory closed-loop interaction for autonomous materials science
- 作者：Liang et al.
- 年份：2025
- 来源 / venue：Science Advances
- DOI / arXiv / URL：https://doi.org/10.1126/sciadv.adu7426
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Liang_2025_AMASE.pdf（arXiv PDF 已归档）
- 论文类型：研究论文 / autonomous materials science system
- 当前状态：to_read / confirmed core
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv PDF abstract | `AMASE` 执行 self-driving cyclical interaction of experiments and computational predictions | 高 |
| 多步行动 | 是 | arXiv PDF abstract | real-time、autonomous、continuous closed-loop | 高 |
| 科学对象归类 | `04` 材料科学 | arXiv PDF abstract | 任务是 temperature-composition phase diagram mapping | 高 |
| 实验验证 | 强 | arXiv PDF abstract | 在 Sn-Bi binary thin-film system 中验证，并把所需实验数降低约 6 倍 | 高 |
| 边界判断 | 不应转 `01.04` | 对象证据 | 虽有 experiment-theory platform 外观，但最终对象是具体材料 phase diagram exploration | 高 |

## 0. 摘要翻译

论文提出 `AMASE`，用于实现实验与理论预测之间的实时闭环互动。系统在材料实验与 computational predictions 之间持续循环，在较少实验次数下完成 temperature-composition phase diagram 探索，并在 Sn-Bi binary thin-film system 上验证。虽然论文带有强 platform / experiment-theory integration 气质，但其稳定研究对象是材料相图与材料发现问题，因此主类应保留在 `04`。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统执行自主实验选择、理论预测整合、结果反馈与下一轮决策
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：未见明确证据
- 在科研流程中承担的明确角色：实验设计、实验执行、理论-实验联动、材料发现

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：04
- 二级类：04.04
- 三级类：phase-diagram-driven materials discovery
- 四级专题：Closed-loop autonomous materials science
- 四级专题是否为新增：否
- 归类理由：系统直接服务于材料相图探索与材料发现
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：temperature-composition phase diagram / thin-film material system
- 最终科学问题：如何以更少实验探索材料相图并加速材料发现
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：experiment-theory workflow 是实现手段，不是主对象

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 04
- 判定理由：贡献明确收口到材料 phase space 探索
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：否
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：未见明确证据
- Robot / Embodied Agent：部分是
- Human-in-the-loop Agent：未见明确证据
- Hybrid Agent：是
- 其他：experiment-theory loop controller

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：否
- 科学问题提出：弱
- 假设生成：部分是
- 实验设计：是
- 仿真建模：是
- 工具调用与代码执行：是
- 实验执行：是
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：部分是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：未见明确证据
- 环境交互：是
- 闭环实验：是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：是
- 仿真驱动：是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：部分是
- 知识图谱：否
- 数字孪生：否
- 机器人平台：部分是
- 其他：experiment-theory coupling

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：减少材料探索中昂贵且缓慢的人工实验迭代
- 现有科研流程或方法的痛点：实验与理论预测脱节、探索效率低
- 核心假设或直觉：实时闭环的 experiment-theory coupling 能更快锁定关键 phase space

### 4.2 系统流程

1. 输入：材料体系与待探索 phase space
2. 任务分解 / 规划：系统选择下一批实验点
3. 工具、数据库、模型或实验平台调用：执行实验并计算预测
4. 中间结果反馈：实验与理论结果并入状态
5. 决策或迭代：更新搜索方向
6. 输出：更完整的相图理解与材料发现结果

### 4.3 系统组件

- Agent 核心：AMASE closed-loop controller
- 工具 / API / 数据库：实验平台 + computational prediction stack
- 记忆或状态模块：phase-space state
- 规划器：active experiment selector
- 评估器 / verifier：实验-理论一致性与 discovery objective
- 人类反馈或专家介入：摘要未强调
- 实验平台或仿真环境：thin-film materials system

## 5. 实验与验证

### 5.1 验证方式

- benchmark：否
- 仿真验证：是
- 高通量计算：部分是
- 机器人实验：部分是
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：未见明确证据

### 5.2 数据、任务与指标

- 数据集 / 实验对象：Sn-Bi binary thin-film system
- 任务设置：phase diagram mapping
- 对比基线：摘要未细述
- 评价指标：所需实验数与探索效率
- 关键结果：仅覆盖整个组成-温度相空间的一小部分即可准确确定 Sn-Bi 共晶相图，并实现约 6 倍实验数缩减
- 是否有消融实验：摘要未细述
- 是否有失败案例或负结果：摘要未细述

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：有材料 phase-space discovery contribution
- 科学贡献是否经过验证：是
- 贡献强度判断：强
- 科学贡献类型：实验发现 / 系统平台
- 证据强度：实验验证

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：直接嵌入真实实验循环，而非离线预测
- 与已有 Agent / 科研智能系统的区别：突出实时 experiment-theory closed loop
- 与同一科学领域其他 Agent 文献的关系：与 `ASD-0410`、`ASD-0379`、`ASD-0417` 同属强材料 SDL 样本
- 主要创新点：实时联动实验与理论、显著降低相图探索成本

## 7. 局限性与风险

- Agent 自主性不足：摘要未细述 planner 内部结构
- 科学验证不足：跨材料体系泛化仍待全文
- 泛化性不足：当前证据集中在特定二元薄膜体系
- 工具链依赖：依赖实验-计算集成
- 数据泄漏或 benchmark 偏差：不是主风险
- 成本、可复现性或安全风险：实验平台门槛较高

## 8. 对综述写作的价值

- 可放入哪个章节：材料科学中的 phase-diagram self-driving discovery
- 可支撑哪个论点：Agent 可把实验和理论预测整合成连续闭环
- 可用于哪个表格或图：materials SDL representative systems
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：待全文
- 需要与哪些论文并列比较：`ASD-0410`、`ASD-0379`

## 9. 总结

### 9.1 一句话概括

实时实验-理论闭环系统高效探索材料相图。

### 9.2 速记版 pipeline

1. 选择材料空间
2. 系统挑下一轮实验
3. 实验与理论并行更新
4. 反馈进搜索状态
5. 收敛到关键 phase diagram

### 9.3 标注字段汇总

```text
是否纳入：是
主类：04
二级类：04.04
三级类：phase-diagram-driven materials discovery
四级专题：Closed-loop autonomous materials science
Agent 类型：Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：hypothesis_generation; experimental_design; simulation_modeling; experiment_execution; data_analysis; evidence_assessment_and_validation
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction; closed_loop_experimentation
验证方式：simulation_validation; closed_loop_experiment
交叉属性：computation_driven; data_driven; experiment_driven; simulation_driven
科学贡献类型：experimental_discovery; system_platform
证据强度：experimentally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：core
```

