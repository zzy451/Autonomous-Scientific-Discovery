# Self Driving Labs ChemRev 2024

## 基本信息
- **论文**: Self-Driving Laboratories for Chemistry and Materials Science
- **作者**: Sterling G. Baird et al.
- **年份**: 2024
- **来源**: Chemical Reviews 124(16):9633-9732, doi:10.1021/acs.chemrev.4c00055 (published online 13 Aug 2024)
- **关键词**: survey, self-driving-lab, chemistry, materials-science, infrastructure

## 核心思想
Self-driving laboratory 正在成为 chemistry 和 materials science 的重要范式，但相关系统跨越硬件自动化、软件编排、优化算法、表征设备和领域应用，概念容易混用。

这篇综述要解决的问题是：如何系统梳理 SDL 的技术构成、应用领域、自动化层级和现实限制。

## 方法细节
综述从技术栈和应用场景两个维度整理 SDL：

1. **硬件层**：自动反应器、液体处理、机器人平台、分析仪器和实验室基础设施；
2. **软件层**：调度、实验控制、数据管理、设备通信；
3. **决策层**：Bayesian optimization、active learning、实验设计和约束处理；
4. **应用层**：drug discovery、materials science、genomics、chemistry 等；
5. **自动化层级**：从部分自动化到闭环自主实验。

## 关键结果

综述强调 SDL 通过 automated experimental workflows 与 autonomous experimental planning 加速科学方法。它把 SDL 理解为硬件自动化、数据基础设施、实验规划算法和表征反馈共同构成的闭环系统，而不是单独的机器人或优化器。它收集了大量真实 SDL 案例，并讨论不同领域的挑战，包括硬件集成、数据质量、算法选择、可复现性、成本和安全。原文还特别强调 enabling technologies：hardware、software 以及与 laboratory infrastructure 的集成；应用覆盖从 drug discovery、materials science 到 genomics 和 chemistry，并讨论不同 levels of automation。

## 与综述的关联

在 Scientific Workflow 中，它覆盖 Experiment Design、Execution、Result Analysis、Verification 和 Evolution。

在 Skill Lifecycle 中，它主要支撑 Representation / protocol skill、Execution / lab action、Evolution / active learning 和 Verification / real-world validation。

Evidence Role 应标为 **Infrastructure**。它不是单个 agent 系统，而是为我们理解 wet-lab / robotic lab / autonomous experimentation 提供基础分类。它也提醒我们，LLM agent 只是 self-driving science 的一部分，不能替代硬件、传感、数据和实验安全。

## 局限性

作为综述，它本身不提出新系统。由于 SDL 发展很快，2025-2026 的 Nature / Nature Communications / Nature Synthesis 新案例需要继续补充。它对 LLM skill lifecycle 的映射需要由我们在综述中完成。

## 核心贡献

这篇 Chemical Reviews 的核心贡献是提供 chemistry/materials SDL 的权威技术地图，帮助我们把 agentic scientific discovery 放回真实实验自动化基础设施中理解。
