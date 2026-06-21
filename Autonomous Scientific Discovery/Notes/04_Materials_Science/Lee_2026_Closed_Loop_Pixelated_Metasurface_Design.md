# Lee and Kim 2026 - Closed-loop experimental AI for pixelated metasurface design

**论文信息**
- 标题：Closed-loop experimental AI for pixelated metasurface design
- 作者：Jeong-Min Lee; Sun-Kyung Kim
- 年份：2026
- 来源 / venue：Photonic and Phononic Properties of Engineered Nanostructures XVI (Proc. SPIE)
- DOI / arXiv / URL：https://doi.org/10.1117/12.3091089
- PDF / 本地文件路径：未保存本地 PDF；本笔记主要基于 Crossref 与 SPIE 页面摘要片段
- 论文类型：conference research paper / weak-evidence closed-loop experimental system
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

## Round-2 Relaxed Multi-Module Update (2026-06-21)

- `scientific_object_modules`: `04`
- `object_coverage_mode`: `single_module`
- `primary_module_for_filing`: `04`
- `general_method_bucket`: `none`
- `first_hand_sources_checked`: Crossref DOI record `10.1117/12.3091089`; DOI resolver / official SPIE landing URL
- `classification_evidence_source_level`: `source_limited`
- `note_revision_required`: `no`

This note no longer treats the record as an unresolved `04 / 09` expansion candidate. The currently accessible first-hand evidence is source-limited, because the SPIE abstract/full text is still access-blocked in the current environment, but it is already sufficient for the narrow boundary decision: the stable object remains pixelated metasurface / engineered nanostructure design, so the paper stays in `04`, and no independent engineering-system or process object is strong enough to add `09`.

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Crossref DOI record; SPIE snippet | 题名与摘要片段都显示这是 experiment-driven、machine-learning-guided closed-loop framework | 中 |
| 科学对象归类 | `04.04` 暂保留 | SPIE snippet | 对象是 pixelated metasurfaces / engineered nanostructures，而不是通用科研平台 | 中 |
| 方法流程 | 制备-测量-优化闭环 | SPIE snippet | 片段明确提到 closes the loop between fabrication, measurement, and optimization | 中 |
| 实验验证 | 有真实实验闭环，但细节不足 | SPIE snippet | 可确认有 experimental AI，但缺少完整实验设置、指标与结果表 | 低 |
| 边界判断 | 更像 `04 / 09`，不是 `01.04` | venue + snippet | 研究对象是 metasurface 结构本体；真正压力在 materials vs engineering，而不是通用平台 | 中 |

## 0. 摘要翻译

目前能稳定获得的 SPIE 摘要片段显示，论文提出一个实验驱动、机器学习引导的闭环框架，把像素化超表面的制备、测量与优化连接起来，用于像素化超表面设计。由于官方全文与完整摘要当前不可稳定访问，本笔记仅能做片段级判断。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：倾向是
- 判断依据：存在明确科研目标、闭环实验流程、机器学习驱动的下一轮优化决策
- 判定置信度：中
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：部分是
  - 工具调用：部分是
  - 反馈迭代：是
  - 自主决策：部分是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：实验设计、实验执行衔接、结果反馈、优化迭代

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除，但证据仍偏弱

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：04
- 二级类：04.04
- 三级类：
- 四级专题：Closed-loop metasurface design systems
- 四级专题是否为新增：否
- 归类理由：被设计、制备与优化的最终对象是 pixelated metasurface / engineered nanostructure
- 归类置信度：中

### 2.2 对象优先判定

- 最终科学研究对象：像素化超表面与其结构-性能设计空间
- 最终科学问题：如何通过闭环实验更快找到满足目标性能的超表面结构
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：机器学习与实验闭环只是手段，真正被优化的是超表面结构对象

### 2.3 容易混淆的边界

- 可能误归类到：09；01.04
- 最终判定：暂保留 04.04
- 判定理由：当前对象首先是超表面/纳米结构本体；如果后续全文显示论文核心其实是器件级工程系统而非材料对象，再复核 `04 / 09`
- 是否需要二次复核：是

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：否
- Planning Agent：部分是
- Tool-using Agent：部分是
- Retrieval-augmented Agent：否
- Multi-Agent System：否
- Robot / Embodied Agent：未明确
- Human-in-the-loop Agent：未明确
- Hybrid Agent：是
- 其他：machine-learning-guided experimental optimizer

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：否
- 科学问题提出：否
- 假设生成：否
- 实验设计：是
- 仿真建模：部分是
- 工具调用与代码执行：部分是
- 实验执行：是
- 数据分析：是
- 结果解释：部分是
- 证据评估与验证：部分是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：未明确
- 计划生成：部分是
- 工具调用：部分是
- 记忆与状态维护：未明确
- 反馈迭代：是
- 自主决策：部分是
- 多 Agent 协作：否
- 环境交互：是
- 闭环实验：是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：是
- 仿真驱动：部分是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：未明确
- 知识图谱：否
- 数字孪生：否
- 机器人平台：未明确
- 其他：metasurface optimization

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：希望把像素化超表面设计从手工试错推进到实验闭环优化
- 现有科研流程或方法的痛点：设计空间离散、制备和测量成本高、人工迭代慢
- 核心假设或直觉：将 fabrication、measurement、optimization 连成闭环，可以更高效逼近目标结构

### 4.2 系统流程

1. 输入：目标超表面结构/性能设计任务
2. 任务分解 / 规划：基于已有实验结果选择下一轮候选
3. 工具、数据库、模型或实验平台调用：制备与测量链路，外加机器学习优化器
4. 中间结果反馈：返回实验测量结果
5. 决策或迭代：更新模型并提出下一轮结构/参数
6. 输出：更优的像素化超表面设计

### 4.3 系统组件

- Agent 核心：machine-learning-guided closed-loop controller
- 工具 / API / 数据库：SPIE 摘要片段未给出完整细节
- 记忆或状态模块：实验历史数据
- 规划器：未明确
- 评估器 / verifier：实验测量结果
- 人类反馈或专家介入：未明确
- 实验平台或仿真环境：fabrication-measurement loop

## 5. 实验与验证

### 5.1 验证方式

- benchmark：否
- 仿真验证：未明确
- 高通量计算：否
- 机器人实验：未明确
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：pixelated metasurfaces
- 任务设置：闭环设计、制备、测量与优化
- 对比基线：未明确
- 评价指标：未完整公开
- 关键结果：可确认存在实验闭环，但结果细节不足
- 是否有消融实验：未明确
- 是否有失败案例或负结果：未明确

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：可能有更优超表面设计结果
- 科学贡献是否经过验证：有实验闭环迹象，但证据不完整
- 贡献强度判断：中
- 科学贡献类型：设计；系统平台
- 证据强度：摘要片段支持

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是离线预测，而是实验闭环优化
- 与已有 Agent / 科研智能系统的区别：面向具体 metasurface 对象，不是通用 research-agent 平台
- 与同一科学领域其他 Agent 文献的关系：可作为 `04 / 09` 边界上的弱证据样本
- 主要创新点：把实验驱动超表面设计与机器学习闭环结合

## 7. 局限性与风险

- Agent 自主性不足：当前公开证据不足以判断完整自主程度
- 科学验证不足：是
- 泛化性不足：未知
- 工具链依赖：强
- 数据泄漏或 benchmark 偏差：未知
- 成本、可复现性或安全风险：最大风险是全文与完整实验信息缺失

## 8. 对综述写作的价值

- 可放入哪个章节：04 材料科学 / 光学材料与超表面设计
- 可支撑哪个论点：有些非化学 closed-loop experimental AI 仍应按具体材料对象归类
- 可用于哪个表格或图：弱证据边界样本表
- 适合作为代表性案例吗：暂不适合
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：当前仅能引用摘要片段
- 需要与哪些论文并列比较：metamaterial / photonics SDL records

## 9. 总结

### 9.1 一句话概括

弱证据但倾向归入材料超表面闭环设计。

### 9.2 速记版 pipeline

1. 设定超表面设计目标
2. 制备并测量样本
3. 机器学习更新优化器
4. 提出下一轮实验
5. 闭环迭代到更优设计

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：04
二级类：04.04
三级类：
四级专题：Closed-loop metasurface design systems
Agent 类型：Planning Agent; Hybrid Agent
科研流程角色：experimental_design; experiment_execution; data_analysis; feedback_iteration
自主能力：feedback_iteration; autonomous_decision_making; environment_interaction; closed_loop_experimentation
验证方式：closed_loop_experiment
交叉属性：computation_driven; data_driven; experiment_driven
科学贡献类型：design; system_platform
证据强度：medium_metadata_only
归类置信度：中
纳入置信度：中
推荐引用强度：普通引用
```
