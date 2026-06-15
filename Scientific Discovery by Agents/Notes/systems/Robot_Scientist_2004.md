# Robot Scientist 2004

## 基本信息
- **论文**: Functional Genomic Hypothesis Generation and Experimentation by a Robot Scientist
- **作者**: Ross D. King et al.
- **年份**: 2004
- **来源**: Nature, doi:10.1038/nature02236
- **关键词**: system, robot-scientist, functional-genomics, closed-loop-discovery, classic

## 核心思想
在 LLM 出现之前，科学发现自动化已经有核心问题：机器能否不仅执行实验，还能生成假设、选择实验、解释结果并更新下一轮计划。

Robot Scientist 要解决的问题是：能否在 functional genomics 中让机器自动形成假设、设计实验、执行实验并根据结果改进知识。

## 方法细节
论文中的 Robot Scientist 使用 inductive logic programming、主动实验选择和自动化实验结合，目标任务是酵母芳香族氨基酸生物合成中的 gene-function assignment。

核心流程包括：

1. 根据已有 functional genomic knowledge 生成关于 yeast gene function 的假设；
2. 选择最有信息量的实验；
3. 自动执行实验；
4. 将结果与假设比较；
5. 更新知识库并进入下一轮实验。

这个系统不是 LLM agent，但具备现代 autonomous scientific discovery 的基本闭环。

## 关键结果

论文展示 Robot Scientist 能在 functional genomics 任务中自动生成并测试假设。相较随机实验选择和穷举实验设计，作者报告其用更少实验成本确定 gene function；这一优势来自主动选择信息量更高的实验，而不是通用自然语言推理能力。它是早期将 hypothesis generation、experiment selection 和 robotic experimentation 结合的代表性工作。

## 与综述的关联

在 Scientific Workflow 中，它覆盖 Hypothesis Generation、Experiment Design、Execution、Verification 和 Evolution。

在 Skill Lifecycle 中，它对应 Representation / hypothesis rule、Execution / lab action、Verification / experimental test 和 Evolution / knowledge update。

Evidence Role 应标为 **Infrastructure + Historical Baseline**。它提醒我们 autonomous scientific discovery 不是 LLM 之后才出现；LLM agents 应该被放在更长的 robot scientist / closed-loop experimentation 脉络中理解。

## 局限性

系统依赖特定 functional genomics 问题和规则化表示，不具备通用自然语言推理或跨领域迁移能力。实验范围也远小于现代自动化平台。

## 核心贡献

Robot Scientist 的核心贡献是早在 2004 年就展示了假设生成、实验选择、机器人执行和知识更新的完整科学发现闭环，是 agentic autonomous scientific discovery 的历史基线。
