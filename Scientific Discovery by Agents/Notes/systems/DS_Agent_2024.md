# DS-Agent 2024

## 基本信息
- **论文**: DS-Agent: Automated Data Science by Empowering Large Language Models with Case-Based Reasoning
- **作者**: Siyuan Guo, Cheng Deng, Ying Wen, Hechang Chen, Yi Chang, Jun Wang
- **年份**: 2024
- **来源**: arXiv:2402.17453; ICML 2024
- **关键词**: data-science, case-based-reasoning, automatic-iteration, code-generation

## 核心思想
DS-Agent 用 case-based reasoning 支撑自动数据科学任务，从需求理解到模型训练。

## 方法细节
系统在 development stage 中通过反馈机制迭代调整方案，并在 deployment stage 复用成功案例生成代码。

## 关键结果
论文报告 GPT-4 配合 DS-Agent 在 development stage 达到 100% success rate。

## 局限性
主要面向数据科学任务，不专门处理科学假设或实验设计。

## 核心贡献
将案例记忆和反馈循环引入数据科学 agent。

## 与综述的关联
适合放入 `X0-Y5-Z3/Z4/Z5,Z7,Z8`，支撑 harness/memory evolution。

## 原文核对与分类复核
- **原文核对**：原文提出 DS-Agent，通过 case-based reasoning 构造 automatic iteration pipeline，并利用 Kaggle expert knowledge 与 feedback mechanism。
- **机制判断**：它支撑自动数据科学，重点是案例记忆和部署阶段复用，不是多智能体系统。
- **分类复核**：保持 `ASD 相关系统`；`X0` 正确；`Y5` 正确，因为 case memory / CBR 属于 harness capability reuse；`Z3,Z4,Z5,Z7,Z8` 正确。
- **写作用途**：适合基础设施和 harness evolution 小节。

## 深读补充（按 MARS 标准）

### 研究问题
DS-Agent 关注自动数据科学任务中 LLM agents 容易生成不合理实验计划、难以稳定构建高质量模型的问题。

### 系统架构 / 工作流
系统结合 LLM agent 和 case-based reasoning。开发阶段通过自动迭代 pipeline 利用 Kaggle expert knowledge；部署阶段用简化 CBR 复用过去成功方案。

### 关键机制
核心是案例记忆和反馈驱动的自动迭代。系统把历史任务经验转化为可复用解决方案。

### 实验验证与证据
原文报告 DS-Agent 在开发阶段达到高成功率，并在部署阶段显著提升 one-pass rate，同时降低运行成本。

### 局限性补充
它主要是自动数据科学系统，科学发现意义取决于数据任务本身；不处理实验室验证或科学机制解释。

### XYZ 分类逐项解释
- `X0`：非显式多智能体。
- `Y5`：case memory / CBR 属于 harness capability reuse。
- `Z3,Z4,Z5,Z7,Z8`：覆盖方案、执行、分析、验证和迭代。

### 综述写作用法
适合作为 harness evolution 和 case-based workflow reuse 的支撑案例。
