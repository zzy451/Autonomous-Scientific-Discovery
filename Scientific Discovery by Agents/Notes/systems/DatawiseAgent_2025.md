# DatawiseAgent 2025

## 基本信息
- **论文**: DatawiseAgent: A Notebook-Centric LLM Agent Framework for Adaptive and Robust Data Science Automation
- **作者**: Ziming You, Yumiao Zhang, Dexuan Xu, Yiwei Lou, Yandong Yan, Wei Wang, Huamin Zhang, Yu Huang
- **年份**: 2025
- **来源**: EMNLP 2025 Main Conference camera-ready; arXiv:2503.07044v2
- **关键词**: system, data-science-agent, notebook, code-execution

## 核心思想
数据科学和科学分析通常发生在 notebook 中：研究者逐步读取数据、写代码、检查输出、修改分析路径。许多 agent 系统把数据分析视为一次性代码生成，忽略了 notebook 的交互式和可追踪特征。

DatawiseAgent 要解决的问题是：如何把 notebook 作为 LLM agent 自动数据分析的核心执行载体。

## 方法细节
DatawiseAgent 是 notebook-centric framework。论文引入 unified interaction representation，并用基于 finite-state transducers 的多阶段架构组织长程规划、渐进式求解和执行失败恢复。

核心流程是：

1. 接收自然语言数据分析任务；
2. 将任务分解为 notebook cells；
3. 生成代码、运行 cell、读取输出；
4. 根据错误和结果调整下一步分析；
5. 在 notebook 中保留可检查的执行轨迹和结果。

Notebook cells 在这里不仅是输出格式，也是 agent 的 execution substrate。

## 关键结果

1. 论文在 **data analysis、scientific visualization、predictive modeling** 三类场景上评测，覆盖 InfiAgent-DABench、MatplotBench 和 DSBench。
2. DatawiseAgent 超过 ReAct、MatplotAgent、AutoGen、TaskWeaver、Data Interpreter 等强基线，显示出更好的 effectiveness 和 adaptability。
3. 在 DSBench data modeling benchmark 上，DatawiseAgent 在所有测试 LLM 上都达到 **90%+** task success 和 **40+** Relative Performance Gap（RPG），包括使用 GPT-4o mini 时也超过此前 SOTA。
4. 在较弱或较小模型上，系统表现为 graceful performance degradation，说明 notebook-centric workflow 和 FST 控制结构提升了鲁棒性与可扩展性。

## 与综述的关联

在 Scientific Workflow 中，它覆盖 Execution、Result Analysis 和 Synthesis。

在 Skill Lifecycle 中，它对应 Representation / code skill、Execution / code run、Verification / runtime feedback 和 Composition / sequential notebook workflow。

Evidence Role 应标为 **Direct + Infrastructure**。它补足科研 agent 的一个现实基础：大量科学发现先发生在 notebook 分析中，而不是直接在论文或湿实验里。

## 局限性

DatawiseAgent 是通用数据科学 agent，不是特定科学发现系统。它的科学有效性取决于数据、任务和领域工具。自动 notebook 运行也可能产生错误解释或表面上可执行但统计上不合理的分析。

## 核心贡献

DatawiseAgent 的核心贡献是把 notebook 从展示结果的容器变成 agent 执行、调试和记录数据科学 workflow 的核心环境。
