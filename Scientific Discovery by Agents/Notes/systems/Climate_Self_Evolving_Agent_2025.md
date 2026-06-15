# Climate Self Evolving Agent 2025

## 基本信息
- **论文**: A Self-Evolving AI Agent System for Climate Science
- **作者**: Zijie Guo, Jiong Wang, Fenghua Ling, Wangxu Wei, Xiaoyu Yue, Zhe Jiang, Wanghan Xu, Jing-Jia Luo, Lijing Cheng, Yoo-Geun Ham, Fengfei Song, Pierre Gentine, Toshio Yamagata, Ben Fei, Wenlong Zhang, Xinyu Gu, Chao Li, Yaqiang Wang, Tao Chen, Wanli Ouyang, Bowen Zhou, Lei Bai
- **年份**: 2025
- **来源**: arXiv:2507.17311
- **关键词**: system, climate-science, self-evolving-agent, data-analysis

## 核心思想
Climate science 涉及多源数据、物理机制、统计分析和复杂可视化。通用 agent 容易执行单次分析，但难以在长程任务中积累经验、更新策略并形成可复用流程。

这篇论文要解决的问题是：如何让 climate science agent 在任务执行中自我演化，逐步改进数据分析和物理推理能力。

## 方法细节
系统 EarthLink 被设计为 self-evolving AI agent for climate science，定位是面向 Earth scientists 的 interactive copilot。

核心流程包括：

1. 规划气候科学分析任务；
2. 执行代码和数据处理；
3. 生成物理解释和可视化；
4. 根据失败和反馈更新内部策略；
5. 在后续任务中复用改进后的 analysis procedure。

按官方项目页描述，EarthLink 的实现包括 Planning Module、Scientific Diagnosis / Self-Evolving Scientific Lab 和 Multi-Scenario Analysis 等模块，并依托 Knowledge Library、Data Library 和 Tool Library 组织文献、气候数据与诊断工具。

## 关键结果

1. EarthLink 将 planning、code execution、data analysis 和 physical reasoning 集成到统一流程中，面向 large-scale climate tasks 自动执行研究分析。
2. 专家评估显示，EarthLink 在 model-observation comparison 和 climate change understanding 等核心气候任务上达到接近 junior researcher 的 proficiency。
3. 在 Atlantic Niño precursors 这一开放科学问题中，EarthLink 自主制定研究策略、识别 predictability sources、用可用数据验证假设，并提出 physically consistent mechanism。

## 与综述的关联

在 Scientific Workflow 中，它覆盖 Knowledge Grounding、Result Analysis、Hypothesis Generation 和 Evolution。

在 Skill Lifecycle 中，它对应 Execution / code run、Evolution / reflection 和 memory-like skill update。

Evidence Role 应标为 **Direct + Boundary**。它补足我们框架中 climate science 和 long-horizon self-evolution 的交叉区域，同时需要把“自我演化”限定为用户交互、错误修正与成功代码/结果复用驱动的工作流改进。

## 局限性

该工作仍是 arXiv 候选，Atlantic Niño 案例主要展示系统在已有数据上的机制分析能力。其发现是否会被独立气候学研究进一步确认、self-evolving 机制是否显著超越普通 memory/reflection，还需要后续外部验证。

## 核心贡献

这篇论文的核心贡献是把 climate science analysis 建模为可自我演化的 agent workflow，展示 agentic science 不限于生物医学和材料化学。
