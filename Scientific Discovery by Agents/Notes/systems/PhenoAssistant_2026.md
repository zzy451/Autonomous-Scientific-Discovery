# PhenoAssistant 2026

## 基本信息

- **论文**: A conversational multi-agent AI system for automated plant phenotyping / PhenoAssistant
- **年份**: 2026
- **来源**: Nature Communications, doi:10.1038/s41467-026-71090-y; arXiv:2504.19818
- **系统名称**: PhenoAssistant
- **关键词**: plant phenotyping, central manager agent, vision model zoo, coding agent, data visualization

## 一句话总结

PhenoAssistant 用 central manager agent 编排 plant phenotyping 工具、vision model zoo、coding/data visualization agents 和分析模块，让研究者通过自然语言完成表型提取、统计分析和可复现工作流。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X4` | GitHub/论文描述 central manager agent 编排专门工具和 agents |
| Y | `Y0` | 主要证据是 central manager 编排工具、模型和数据分析 agents；未见明确反思、自我修正、搜索或演化机制 |
| Z | `Z3,Z4,Z5,Z7` | 覆盖分析设计、执行、结果分析和 case/evaluation 验证；复现支持不等同于长周期 discovery iteration |

## 对综述的价值

它补植物科学 execution substrate，支撑“多智能体如何组织实验数据分析和可复现 pipeline”。
