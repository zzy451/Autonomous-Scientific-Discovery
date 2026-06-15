# DrugAgent 2024

## 基本信息
- **论文**: DrugAgent: Automating AI-aided Drug Discovery Programming through LLM Multi-Agent Collaboration
- **作者**: Sizhe Liu, Yizhou Lu, Siyu Chen, Xiyang Hu, Jieyu Zhao, Tianfan Fu, Yue Zhao
- **年份**: 2024
- **来源**: arXiv:2411.15692
- **关键词**: drug-discovery, multi-agent, ML-programming, ADMET

## 核心思想
DrugAgent 用多智能体协作自动化药物发现中的机器学习编程任务。

## 方法细节
系统包含 Planner 和 Instructor 等角色，识别领域知识需求、构建工具、编码并评估模型。

## 关键结果
论文在 ADMET prediction 等任务上展示了 end-to-end ML programming pipeline。

## 局限性
主要是 ML programming 层面的药物发现辅助，不等同于真实药物发现闭环。

## 核心贡献
把药物发现中的领域知识和 ML 编程自动化结合到多智能体 workflow。

## 与综述的关联
适合放入 `X2-Y0-Z1/Z3/Z4/Z5/Z7`；它是药物发现 ML 编程的多智能体支撑系统，但不应作为搜索/演化机制主证据。

## 原文核对与分类复核
- **原文核对**：原文包含 LLM Planner 和 LLM Instructor，解决药物发现中从 theoretical ideas 到 robust ML implementation 的落地问题。
- **机制判断**：系统确实是多智能体协作，但原文摘要没有显示明确的搜索、演化或候选排序机制。
- **分类复核**：已从 `Y2` 修正为 `Y0`；`X2` 保持；`Z1,Z3,Z4,Z5,Z7` 保持。它适合作为 ASD 相关系统，而不是搜索/演化章节主证据。
- **写作用途**：放在工具/代码执行或领域知识注入，不应作为 evolutionary workflow 例子。

## 深读补充（按 MARS 标准）

### 研究问题
DrugAgent 关注药物发现中理论想法难以转化为可靠 ML 实现的问题，尤其是药物发现任务需要领域知识和高质量代码实现。

### 系统架构 / 工作流
系统由 LLM Planner 和 LLM Instructor 等角色组成。Planner 制定高层方案，Instructor 识别并整合领域知识以完成实现。

### 关键机制
核心是 multi-agent collaboration for ML programming，而不是搜索或演化。系统帮助药物发现研究者把 AI 方法落地到具体任务。

### 实验验证与证据
原文在 drug-target interaction 等药物发现任务上展示相对 ReAct 等 baseline 的性能提升。

### 局限性补充
DrugAgent 主要是 ML 编程自动化，不等于真实药物发现闭环。它缺少明确候选搜索/演化机制。

### XYZ 分类逐项解释
- `X2`：Planner / Instructor 多角色协作。
- `Y0`：没有明确搜索、演化或候选筛选。
- `Z1,Z3,Z4,Z5,Z7`：覆盖领域知识、代码设计、执行、分析和验证。

### 综述写作用法
适合第 6/8 章的领域工具和代码执行支撑，不应作为演化机制主证据。
