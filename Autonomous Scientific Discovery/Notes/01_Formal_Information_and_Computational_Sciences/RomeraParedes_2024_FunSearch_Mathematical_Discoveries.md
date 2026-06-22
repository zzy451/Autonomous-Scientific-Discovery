# Romera-Paredes et al. 2024 - Mathematical discoveries from program search with large language models

**论文信息**
- 标题：Mathematical discoveries from program search with large language models
- 作者：Bernardino Romera-Paredes et al.
- 年份：2024
- 来源 / venue：Nature
- DOI / arXiv / URL：https://doi.org/10.1038/s41586-023-06924-6
- PDF / 本地文件路径：本轮未新增本地 PDF；已核对 Nature article page 与 publisher PDF，当前 note 不补写不存在的本地归档路径
- 论文类型：系统论文 / mathematical discovery
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Nature article / PDF | LLM 生成程序，evaluator 打分，程序库回灌，形成闭环 | 高 |
| 多步行动 | 是 | Nature article / PDF | prompt 组装、生成、评估、存储、再采样迭代 | 高 |
| 科学对象归类 | `01` | Nature article / PDF | 头号发现落在 extremal combinatorics 的 cap set problem，属于具体数学对象研究 | 高 |
| 不是 `01.04` | 是 | Nature article / PDF | 已对具体数学对象产出新可验证知识，因此不再适用 general-method bucket | 高 |
| 数学贡献 | 强 | Nature article / PDF | 改进 cap set lower bound；给出更优构造 | 高 |

## 0. 摘要翻译

论文提出 FunSearch，把 pretrained LLM 与 evaluator 结合，在程序空间中迭代搜索。系统不是直接输出答案，而是生成可执行程序并由 evaluator 打分筛选。最重要的新结果出现在极值组合数学中的 cap set problem，作者报告发现超过既有最优结果的新构造，并改进相关下界；online bin packing 主要作为泛化展示。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具备明确科研目标、多步程序生成与评估循环、工具调用与反馈迭代
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：不突出
- 在科研流程中承担的明确角色：假设生成、程序搜索、证据评估与验证

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- scientific_object_modules：`01`
- object_coverage_mode：`single_module`
- has_concrete_object_experiments：yes
- general_method_bucket：none
- primary_module_for_filing：`01`
- 一级类：01
- 二级类：01.01
- 三级类：extremal combinatorics
- 四级专题：Program-search mathematical discovery
- 四级专题是否为新增：否
- 归类理由：最强、最核心的新知识贡献稳定落在数学对象本身
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：cap set problem 等数学对象
- 最终科学问题：如何通过程序搜索发现新的数学构造与下界
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：program search 是方法，数学对象才是主类依据

### 2.3 容易混淆的边界

- 可能误归类到：01.04 或 01.02
- 最终判定：01.01
- 判定理由：online bin packing 只是泛化展示；headline discovery 是具体数学对象
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Tool-using Agent：是
- Hybrid Agent：是

### 3.2 科研流程角色

- 假设生成：是
- 工具调用与代码执行：是
- 证据评估与验证：是
- 结果解释：是

### 3.3 自主能力

- 任务分解：部分
- 计划生成：是
- 工具调用：是
- 反馈迭代：是
- 自主决策：是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：否
- 实验驱动：否

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：扩展 LLM 在数学与算法发现中的能力
- 现有科研流程或方法的痛点：手工搜索与构造效率有限
- 核心假设或直觉：LLM 生成程序 + evaluator 反馈可形成有效发现循环

### 4.2 系统流程

1. 输入：问题描述与已有程序库
2. 任务分解 / 规划：prompt 组装与程序生成
3. 工具、数据库、模型或实验平台调用：执行程序并用 evaluator 打分
4. 中间结果反馈：高分程序回灌到程序库
5. 决策或迭代：继续再采样搜索
6. 输出：更优数学构造与可验证结果

### 4.3 系统组件

- Agent 核心：FunSearch
- 工具 / API / 数据库：program database, evaluator
- 评估器 / verifier：formal / computational evaluator
- 实验平台或仿真环境：程序执行环境

## 5. 实验与验证

### 5.1 验证方式

- benchmark：有泛化展示
- 计算验证：是
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：cap set problem；online bin packing
- 任务设置：生成可执行程序并搜索更优解
- 对比基线：既有最优结果与其他方法
- 评价指标：构造质量、下界改进等
- 关键结果：得到更优 cap set 构造并改进 lower bound

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是，发现新的数学结果
- 科学贡献是否经过验证：是
- 贡献强度判断：强
- 科学贡献类型：knowledge_discovery
- 证据强度：computationally_validated

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：是面向正式数学对象的发现闭环
- 与已有 Agent / 科研智能系统的区别：不是通用 research-agent platform，而是 concrete mathematical discovery
- 与同一科学领域其他 Agent 文献的关系：是 `01.01 / 01.04 / 01.02` 边界的强锚点
- 主要创新点：把 LLM 程序搜索与 evaluator 闭环结合起来用于数学发现

## 7. 局限性与风险

- Agent 自主性不足：不突出多 Agent 协作
- 科学验证不足：对数学对象已足够强
- 泛化性不足：online bin packing 只是辅助展示

## 8. 对综述写作的价值

- 可放入哪个章节：01 形式、信息与计算科学
- 可支撑哪个论点：只要产出稳定具体数学对象知识，就应离开 `01.04`
- 可用于哪个表格或图：`01.01 / 01.04 / 01.02` 边界案例表
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用

## 9. 总结

### 9.1 一句话概括

围绕具体数学对象的程序搜索发现系统。

### 9.2 速记版 pipeline

1. LLM 生成候选程序
2. evaluator 运行并打分
3. 高分程序回灌
4. 继续迭代搜索
5. 输出更优数学结果

### 9.3 标注字段汇总

```text
是否纳入：to_read
scientific_object_modules：01
object_coverage_mode：single_module
has_concrete_object_experiments：yes
general_method_bucket：none
primary_module_for_filing：01
first_hand_sources_checked：Nature article page; publisher PDF
classification_evidence_source_level：first_hand_full_text
主类：01
二级类：01.01
三级类：extremal combinatorics
四级专题：Program-search mathematical discovery
Agent 类型：LLM Agent; Tool-using Agent; Hybrid Agent
科研流程角色：hypothesis_generation; tool_use_and_code_execution; evidence_assessment_and_validation; result_interpretation
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making
验证方式：computational_validation; expert_evaluation
交叉属性：computation_driven
科学贡献类型：knowledge_discovery
证据强度：computationally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
