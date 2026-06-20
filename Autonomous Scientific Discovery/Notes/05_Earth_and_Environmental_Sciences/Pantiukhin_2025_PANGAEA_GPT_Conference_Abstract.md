# Pantiukhin et al. 2025 - PANGAEA GPT: A Coordinated Multi-Agent Architecture for Earth System Data Discovery and Analysis

**论文信息**
- 标题：PANGAEA GPT: A Coordinated Multi-Agent Architecture for Earth System Data Discovery and Analysis
- 作者：Pantiukhin et al.
- 年份：2025
- 来源 / venue：EGU General Assembly / EGUsphere
- DOI / arXiv / URL：https://doi.org/10.5194/egusphere-egu25-13656
- PDF / 本地文件路径：本轮基于 Copernicus abstract page 与 reviewer 一手证据；未保存本地 PDF
- 论文类型：conference abstract / lineage record
- 当前状态：background_only
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Copernicus abstract page | Supervisor / Task / Data Agents 明确存在 | 高 |
| 科学对象归类 | `05.04` | abstract page | Earth system data discovery and analysis via PANGAEA archive | 高 |
| 文献类型 | conference abstract | venue metadata | 会议摘要而非完整方法论文 | 高 |
| confirmed-core 风险 | 应降级 | lineage comparison | 与 `ASD-0546` 存在明显 companion / fuller-record 关系 | 高 |
| 边界判断 | 不需改到 `01.04` | object-first reading | 场景和对象都稳定锚定地球系统数据 | 高 |

## 0. 摘要翻译

PANGAEA GPT 是一个面向地球系统数据发现与分析的多智能体框架，旨在帮助地学研究者处理和解释 PANGAEA 档案中的 Earth system datasets。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具备多 Agent 分工、数据分析、可视化与文档生成能力
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：部分
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：查询解析、任务分派、数据分析、结果解释

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除，但应从 confirmed core 降到 background_only

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：05
- 二级类：05.04
- 三级类：地球系统数据发现
- 四级专题：Earth-system data-discovery and analysis agents
- 四级专题是否为新增：否
- 归类理由：对象是地球系统数据资源和地学分析工作流
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：Earth system datasets in PANGAEA
- 最终科学问题：如何用协调式多 Agent 改善地学数据发现与分析
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：虽然是通用 LLM 架构，但任务场景并不跨域，而是稳定服务地学数据

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保持 05.04，但降为 background_only
- 判定理由：主要问题是会议摘要谱系重复，不是对象归类错误
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Multi-Agent System：是
- Hybrid Agent：是

### 3.2 科研流程角色

- 知识抽取与组织：是
- 数据分析：是
- 结果解释：是

### 3.3 自主能力

- 计划生成：是
- 工具调用：是
- 反馈迭代：是
- 多 Agent 协作：是

### 3.4 交叉属性标签

- 数据驱动：是

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：降低地学数据档案使用门槛
- 现有科研流程或方法的痛点：异构数据资源难检索、难分析
- 核心假设或直觉：分层 Agent 能更好组织地学数据发现任务

### 4.2 系统流程

1. 输入：地学研究者的问题。
2. 任务分解 / 规划：Supervisor Agent 分派任务。
3. 工具、数据库、模型或实验平台调用：Task / Data Agents 访问 PANGAEA 与分析环境。
4. 中间结果反馈：数据处理与可视化结果回流。
5. 决策或迭代：继续细化分析。
6. 输出：地学数据解释和文档化结果。

### 4.3 系统组件

- Agent 核心：Supervisor + Task Agents + Data Agents
- 工具 / API / 数据库：PANGAEA archive, Python environment
- 评估器 / verifier：摘要层未展开

## 5. 实验与验证

### 5.1 验证方式

- benchmark：否
- 真实场景部署：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：Earth system datasets
- 任务设置：数据发现、分析、可视化、文档生成
- 关键结果：展示 coordinated multi-agent workflow

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要是系统概念展示
- 科学贡献是否经过验证：摘要层有限
- 贡献强度判断：弱到中
- 科学贡献类型：system_platform; lineage_record
- 证据强度：benchmark_only

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：是明确的多 Agent 地学数据系统
- 与已有 Agent / 科研智能系统的区别：更适合作为 `ASD-0546` 的 companion abstract
- 与同一科学领域其他 Agent 文献的关系：应与 fuller earth-science MAS record 一并看待
- 主要创新点：此条本身的主要价值在谱系定位

## 7. 局限性与风险

- 只是 conference abstract
- 与 fuller record 的谱系重复明显
- 是否仍需进一步全文复核：否

## 8. 对综述写作的价值

- 可放入哪个章节：05 背景 / 谱系补充
- 可支撑哪个论点：说明地学多 Agent 系统的早期公开形态
- 适合作为代表性案例吗：不适合
- 推荐引用强度：background

## 9. 总结

### 9.1 一句话概括

地学多 Agent 会议摘要，更适合转为背景谱系条目。

### 9.2 速记版 pipeline

1. 研究者提问
2. 多 Agent 分派任务
3. 检索地学数据
4. 分析与可视化
5. 输出解释

### 9.3 标注字段汇总

```text
是否纳入：background_only
主类：05
二级类：05.04
三级类：地球系统数据发现
四级专题：Earth-system data-discovery and analysis agents
Agent 类型：LLM Agent; Multi-Agent System; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; data_analysis; result_interpretation
自主能力：planning; tool_use; feedback_iteration; multi_agent_collaboration
验证方式：
交叉属性：data_driven
科学贡献类型：system_platform; lineage_record
证据强度：benchmark_only
归类置信度：高
纳入置信度：高
推荐引用强度：background
```
