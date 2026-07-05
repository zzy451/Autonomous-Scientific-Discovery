# Unknown 2026 - AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation

**论文信息**
- 标题：AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation
- 作者：Unknown
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2605.28655
- PDF / 本地文件路径：未见本地归档 PDF；本轮核对 arXiv abstract、arXiv HTML full text v1，并确认可用 PDF `https://arxiv.org/pdf/2605.28655.pdf`
- 论文类型：系统论文 / 多 Agent 科研系统
- 当前状态：已读；已按 relaxed multi-module 口径完成复核
- 阅读日期：2026-06-23
- 笔记作者：Codex

## Evidence Log

### 2026-07-05 wording harmonization

- Active source-state wording for this note is now: local archived PDF exists at `Reference_PDF/01_Formal_Information_and_Computational_Sciences/Unknown_2026_AutoScientists.pdf`.
- Active landed classification wording remains `scientific_object_modules=01;06;07`, `object_coverage_mode=multi_module`, and `primary_module_for_filing=06`.
- The current note path under `01` should be read as historical filing residue only; it is not active evidence for a `01.04`-style or `01`-primary reading.

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract；HTML full text v1 | 系统强调 self-organizing agent teams、长期实验、记忆与失败回顾，满足多步 Agent 标准 | 高 |
| 科学对象归类 | `01;06;07` | abstract；task coverage section | 既有 formal / computational research tasks，也有生命科学与药物发现任务，因此不能保留为独立 `01.04` | 高 |
| `01` 证据 | 是 | LM-training optimization coverage | 形式/计算对象来自 LM training 与相关 formal-computational research tasks | 中高 |
| `06` 与 `07` 证据 | 是 | BioML-Bench；ProteinGym；biomedical imaging；single-cell omics；drug-discovery tasks | 生命科学与医学对象覆盖明确存在 | 高 |
| 边界裁决 | 不进入 `01.04` | full-text task description | 当前文件留在 `01` 文件夹只是历史落盘便利；权威分类事实应记录为 `01;06;07`，`primary_module_for_filing=06` | 高 |

## 0. 摘要翻译

AutoScientists 描述了一组可自组织的 Agent 团队，用于长程科研实验与持续迭代。系统不仅展示一般性的科研协同能力，还在 LM training、ProteinGym、BioML-Bench、biomedical imaging、single-cell omics 和 drug-discovery 等对象上给出可识别任务覆盖。因此本轮不再接受旧的 `01.04` only 读法，而采用 `01;06;07` 的多模块记录。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：面向明确科研目标；强调长期实验；具备任务分工、记忆、反馈与多 Agent 协作
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：hypothesis generation；workflow orchestration；feedback iteration；tool use and code execution

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`01;06;07`
- 覆盖模式：多模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：`06`
- Primary module for filing 说明：用于展示和后续归档便利；当前 note 位于 `01` 文件夹不代表分类 authority
- 主展示模块一级类：`06` 生命科学
- 主展示模块二级类：生物任务 benchmark / case coverage
- 主展示模块三级类：暂不细分
- 主展示模块四级专题：long-running scientific experimentation teams with life / biomedical coverage
- 其他覆盖模块及对应层级路径：`01` 形式、信息与计算科学；`07` 医学与健康科学
- 四级专题是否为新增：否
- 是否进入独立 `01.04` 存放区：否
- 每个模块的对象实验证据：
  - `01`：LM-training optimization / formal-computational tasks
  - `06`：ProteinGym、BioML-Bench、single-cell omics、protein engineering
  - `07`：drug-discovery 与 biomedical imaging 任务
- 归类理由：对象级任务覆盖已经跨越计算、生命与医学三侧，平台外观不足以把它收回 `01.04`
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：论文中实际评测的计算任务、生命科学任务和医学 / 药物发现任务
- 最终科学问题：如何让自组织 Agent 团队持续推进长程科研实验
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：通用 team architecture 是实现方式，不是主分类依据

### 2.3 容易混淆的边界

- 可能误归类到：独立 `01.04`
- 最终判定：不进入 `01.04`；记录为 `01;06;07`
- 判定理由：论文已报告具体对象任务覆盖，不满足 `01.04` 的“无具体对象实验”条件
- 多模块覆盖说明：生命与医学任务虽服务于通用团队架构展示，但在 relaxed rule 下仍应记为对象模块
- 01.04 判定说明：否
- 是否需要二次复核：否；当前 abstract + HTML full text v1 已足以稳定支持本轮归类

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：部分是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：未强调
- Hybrid Agent：是
- 其他：self-organizing long-running research team

### 3.2 科研流程角色

- 文献检索与阅读：部分是
- 知识抽取与组织：是
- 科学问题提出：是
- 假设生成：是
- 实验设计：部分是
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
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：部分是
- 多模态：未强调
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：未强调
- 数字孪生：否
- 机器人平台：否
- 其他：long-running memory and failure-recovery loop

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：构建可持续、可恢复、可长期迭代的科研团队式 Agent
- 现有科研流程或方法的痛点：短链条助手难以支持长程实验、失败记忆与持续优化
- 核心假设或直觉：自组织团队、长程记忆与失败回顾可改善科研实验推进能力

### 4.2 系统流程

1. 输入：科研目标与任务约束
2. 任务分解 / 规划：自组织 Agent 团队分工
3. 工具、数据库、模型或实验平台调用：按任务需要调用外部资源
4. 中间结果反馈：记录失败、回顾轨迹、调整策略
5. 决策或迭代：继续推进长期实验
6. 输出：稳定的研究结论、候选方案或实验结果

### 4.3 系统组件

- Agent 核心：self-organizing agent teams
- 工具 / API / 数据库：多类科研工具
- 记忆或状态模块：有
- 规划器：有
- 评估器 / verifier：有
- 人类反馈或专家介入：未突出为本轮分类关键
- 实验平台或仿真环境：与具体任务共同出现

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：部分是
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：未强调

### 5.2 数据、任务与指标

- 数据集 / 实验对象：LM training cases；BioML-Bench；ProteinGym；biomedical imaging；single-cell omics；drug-discovery tasks
- 任务设置：长程 scientific experimentation
- 对比基线：论文原文设置
- 评价指标：任务能力与系统表现
- 关键结果：跨 `01;06;07` 的对象任务均有可识别覆盖
- 是否有消融实验：有部分分析
- 是否有失败案例或负结果：有失败记忆 / 回顾机制相关描述

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏科研系统平台，但具备 concrete task coverage
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system platform；benchmark
- 证据强度：一手 abstract + HTML full text；source_limited=no

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单步模型，而是长程团队式 Agent
- 与已有 Agent / 科研智能系统的区别：强调 self-organizing teams 与 long-running experimentation
- 与同一科学领域其他 Agent 文献的关系：是典型“平台感强但已有 concrete object coverage”的 relaxed-rule 样本
- 主要创新点：把长期实验、失败记忆与团队协作整合到同一科研 Agent 架构

## 7. 局限性与风险

- Agent 自主性不足：实际科研落地强度仍需继续观察
- 科学验证不足：主要依赖 benchmark / task coverage
- 泛化性不足：跨任务成功不等于真实科研闭环全部成熟
- 工具链依赖：高
- 数据泄漏或 benchmark 偏差：需警惕
- 成本、可复现性或安全风险：长程多 Agent 成本较高
- 是否仍需进一步全文复核：否；本轮一手 HTML 全文已足够支持当前模块结论，仅缺本地 PDF 归档

## 8. 对综述写作的价值

- 可放入哪个章节：多模块科研 Agent；`01.04` 边界纠偏案例
- 可支撑哪个论点：通用 team architecture 一旦出现具体对象任务覆盖，就不应继续写成 `01.04` only
- 可用于哪个表格或图：multi-module object coverage 表；general-method boundary 表
- 适合作为代表性案例吗：适合
- 推荐引用强度：core
- 需要在正文中特别引用的页码 / 图 / 表：task coverage 与 long-running experimentation 相关部分
- 需要与哪些论文并列比较：AutoSci；AutoResearchClaw；其他 long-running scientific-agent systems

## 9. 总结

### 9.1 一句话概括

自组织长程科研 Agent 团队，且已覆盖计算、生命与医学对象任务。

### 9.2 速记版 pipeline

1. 接收科研目标
2. 组织 Agent 团队分工
3. 调用工具推进长期实验
4. 记忆失败并持续迭代
5. 输出研究结果

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：01;06;07
覆盖模式：multi_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：06
是否进入 01.04 存放区：否
主展示模块一级类：06
主展示模块二级类：生命科学任务覆盖
主展示模块三级类：暂不细分
主展示模块四级专题：long-running scientific experimentation teams with life / biomedical coverage
其他覆盖模块及对应层级路径：01;07
module_assignment_evidence：LM training -> 01；ProteinGym/BioML-Bench/single-cell omics -> 06；drug discovery/biomedical imaging -> 07
multi_module_object_coverage_note：当前 note 路径仅是历史落盘；权威分类为 01;06;07
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Hybrid Agent
科研流程角色：hypothesis_generation; workflow_orchestration; feedback_iteration; tool_use_and_code_execution
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark
交叉属性：computation_driven; data_driven
科学贡献类型：system_platform; benchmark
证据强度：first_hand_full_text
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
