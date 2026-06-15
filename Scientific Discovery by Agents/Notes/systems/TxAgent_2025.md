# TxAgent 2025

## 基本信息
- **论文**: TxAgent: An AI Agent for Therapeutic Reasoning Across a Universe of Tools
- **作者**: Shanghua Gao, Richard Zhu, Zhenglun Kong, Ayush Noori, Xiaorui Su, Curtis Ginder, Theodoros Tsiligkaridis, Marinka Zitnik
- **年份**: 2025
- **来源**: arXiv:2503.10970
- **关键词**: therapeutic-reasoning, biomedical-tools, tool-use, drug-interaction

## 核心思想
TxAgent 使用多步推理和实时生物医学工具调用来支持治疗推理。

## 方法细节
系统连接 211 个工具，执行药物相互作用、禁忌症和个体化治疗建议相关任务。

## 关键结果
论文报告 TxAgent 在多个 drug reasoning benchmarks 上优于 LLM 和 tool-use baselines。

## 局限性
偏临床/治疗推理，不是完整新药发现闭环。

## 核心贡献
展示 scientific tool-use agent 如何在高风险生物医学任务中进行跨源验证。

## 与综述的关联
适合放入 `X0-Y1-Z1/Z3/Z4,Z5,Z7`。

## 原文核对与分类复核
- **原文核对**：原文提出 therapeutic reasoning agent across a universe of tools，围绕生物医学/治疗学工具调用和推理。
- **机制判断**：它支撑生物医学 ASD 的工具使用、数据分析和验证环节，但不是完整发现闭环。
- **分类复核**：保持 `ASD 相关系统`；`X0` 正确；`Y1` 可保留为工具调用后的推理和修正；`Z1,Z3,Z4,Z5,Z7` 正确。
- **写作用途**：适合放在 biomedical tool-use infrastructure，而非 multi-agent 主证据。

## 深读补充（按 MARS 标准）

### 研究问题
TxAgent 关注 therapeutic reasoning 需要跨大量工具、数据和模型进行推理的问题。单一 LLM 难以可靠完成复杂治疗学任务。

### 系统架构 / 工作流
系统作为 AI agent across a universe of tools，围绕治疗学问题调用多种工具，进行知识检索、分析、推理和结果解释。

### 关键机制
核心是 tool-use reasoning。它将生物医学工具生态接入 agent workflow。

### 实验验证与证据
原文在治疗学推理相关任务中评估系统，展示跨工具推理能力。

### 局限性补充
TxAgent 是 biomedical tool-use agent，不是完整 drug discovery 或 clinical validation 系统。安全和临床可靠性需要严格验证。

### XYZ 分类逐项解释
- `X0`：非显式多智能体。
- `Y1`：工具调用后的推理和修正。
- `Z1,Z3,Z4,Z5,Z7`：覆盖知识、方案、执行、分析和验证。

### 综述写作用法
适合 biomedical tool-use infrastructure，不应作为多智能体主证据。
