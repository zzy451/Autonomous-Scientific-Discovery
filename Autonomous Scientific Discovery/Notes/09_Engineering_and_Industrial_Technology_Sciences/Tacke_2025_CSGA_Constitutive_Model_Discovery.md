# Tacke et al. 2025 - Constitutive scientific generative agent (CSGA): Leveraging large language models for automated constitutive model discovery

**论文信息**
- 标题：Constitutive scientific generative agent (CSGA): Leveraging large language models for automated constitutive model discovery
- 作者：Tacke et al.
- 年份：2025
- 来源 / venue：Machine Learning for Computational Science and Engineering
- DOI / arXiv / URL：https://doi.org/10.1007/s44379-025-00022-2
- PDF / 本地文件路径：本轮基于 publisher abstract 与 reviewer 一手证据；未保存本地 PDF
- 论文类型：方法论文 / constitutive-model discovery agent
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 暂保留 | publisher abstract | LLM covers model selection; outer generation + inner optimization | 中高 |
| 科学对象归类 | `09.01` | publisher abstract | constitutive models for mechanical response under load | 高 |
| 方法流程 | 生成-优化-比较 | publisher abstract | SGA / CSGA 自动产生并评估模型候选 | 高 |
| 实验验证 | benchmark problems | publisher abstract | 三类 benchmark problems 下比较 stress-response prediction | 中 |
| 边界判断 | 不应移到 `01.04` | object-first reading | 对象是明确的工程 / 计算力学建模任务 | 高 |

## 0. 摘要翻译

本文提出 CSGA，把 LLM-based scientific generative agent 与材料理论知识结合起来，用于自动发现可解释的 constitutive models，并在多个力学 benchmark 问题上与 CANN、SGA 比较。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：暂保留为是
- 判断依据：存在模型候选生成、理论约束注入、参数优化和比较流程
- 判定置信度：中高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：待确认
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：模型生成、参数优化、结果比较

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：边界较近
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：不缺，但 discovery loop 主要发生在建模层
- 若排除，排除理由：当前不排除，但 confirmed-core 强度仍需注意

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：09
- 二级类：09.01
- 三级类：constitutive modeling / computational mechanics
- 四级专题：Constitutive-model discovery agents
- 四级专题是否为新增：否
- 归类理由：直接对象是材料受载力学响应的 constitutive model discovery
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：constitutive models for mechanical response
- 最终科学问题：如何自动发现更可解释、表现更优的 constitutive models
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：LLM 是生成工具，稳定对象是工程 / 力学建模任务

### 2.3 容易混淆的边界

- 可能误归类到：01.04 / 04
- 最终判定：保持 09.01
- 判定理由：它既不是通用科研平台，也不是具体材料家族发现，而是工程力学模型发现
- 是否需要二次复核：是

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Tool-using Agent：是
- Hybrid Agent：是

### 3.2 科研流程角色

- 假设生成：是
- 仿真建模：是
- 工具调用与代码执行：是
- 证据评估与验证：是

### 3.3 自主能力

- 计划生成：是
- 工具调用：是
- 反馈迭代：是

### 3.4 交叉属性标签

- 计算驱动：是
- 仿真驱动：是

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：降低 constitutive-model discovery 对人工专家选择的依赖
- 现有科研流程或方法的痛点：模型空间大，人工选择与优化效率低
- 核心假设或直觉：LLM 生成候选与下层优化结合可更快搜索可解释模型

### 4.2 系统流程

1. 输入：力学 benchmark 问题与材料理论约束。
2. 任务分解 / 规划：外层生成模型候选。
3. 工具、数据库、模型或实验平台调用：内层优化器估计参数并计算响应。
4. 中间结果反馈：stress-response error 回流。
5. 决策或迭代：生成和比较新候选。
6. 输出：更优 constitutive model。

### 4.3 系统组件

- Agent 核心：CSGA
- 工具 / API / 数据库：优化器、benchmark problems
- 规划器：LLM-based candidate generation
- 评估器 / verifier：stress-response prediction comparison

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：three benchmark constitutive-model problems
- 任务设置：与 CANN、SGA 对比模型发现效果
- 评价指标：prediction quality / interpretability
- 关键结果：CSGA 在多个问题上提升自动发现能力

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：提供自动 constitutive-model discovery 策略
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：knowledge_discovery; model_discovery
- 证据强度：simulation_supported

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：围绕模型发现闭环而非单次预测
- 与已有 Agent / 科研智能系统的区别：聚焦 engineering constitutive modeling
- 与同一科学领域其他 Agent 文献的关系：可与 FEM / structural-analysis agents 对照
- 主要创新点：把 LLM 生成与理论约束优化合并到统一发现循环中

## 7. 局限性与风险

- 当前验证更像建模 benchmark，不是实体实验闭环
- confirmed-core 风险高于主类风险
- 是否仍需进一步全文复核：是

## 8. 对综述写作的价值

- 可放入哪个章节：09 工程与工业技术科学
- 可支撑哪个论点：Agent 已进入工程建模与理论发现任务
- 适合作为代表性案例吗：可作为边界样本
- 推荐引用强度：standard

## 9. 总结

### 9.1 一句话概括

LLM 生成与优化结合自动发现力学本构模型。

### 9.2 速记版 pipeline

1. 生成模型候选
2. 优化参数
3. 评估响应误差
4. 回流更新
5. 选出更优模型

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：09
二级类：09.01
三级类：constitutive modeling / computational mechanics
四级专题：Constitutive-model discovery agents
Agent 类型：LLM Agent; Tool-using Agent; Hybrid Agent
科研流程角色：hypothesis_generation; simulation_modeling; tool_use_and_code_execution; evidence_assessment_and_validation
自主能力：planning; tool_use; feedback_iteration
验证方式：benchmark; simulation_validation
交叉属性：computation_driven; simulation_driven
科学贡献类型：knowledge_discovery; model_discovery
证据强度：simulation_supported
归类置信度：高
纳入置信度：中高
推荐引用强度：standard
```
