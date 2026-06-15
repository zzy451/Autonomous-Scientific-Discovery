# ToolUniverse 2025

## 基本信息
- **论文**: Democratizing AI scientists using ToolUniverse
- **作者**: Shanghua Gao, Richard Zhu, Pengwei Sui, Zhenglun Kong, Sufian Aldogom, Yepeng Huang, Ayush Noori, Reza Shamji, Krishna Parvataneni, Theodoros Tsiligkaridis, Marinka Zitnik
- **年份**: 2025
- **来源**: arXiv:2509.23426
- **关键词**: scientific-tools, AI-scientist, tool-ecosystem, agentic-workflow

## 核心思想
ToolUniverse 提供构建 AI scientist 的统一科学工具生态，降低 bespoke scientific agents 的构建成本。

## 方法细节
系统整合 600+ 科学工具，提供 Find Tool 和 Call Tool 等标准化交互协议，并可优化工具说明和组合 agentic workflows。

## 关键结果
论文展示 ToolUniverse 可用于构建 AI scientist，并在高胆固醇血症案例中识别潜在药物 analog。

## 局限性
更偏 infrastructure，不是单一完整发现系统。

## 核心贡献
把 scientific tool ecosystem 作为 AI scientist 的基础设施。

## 与综述的关联
适合放入 `X0-Y5-Z1/Z3/Z4,Z5,Z7,Z8`，支撑 harness / capability evolution。

## 原文核对与分类复核
- **原文核对**：原文提出 AI scientists 的工具生态，包含 600+ models、datasets、APIs、scientific packages，并支持 tool interface refinement、new tool generation、tool composition。
- **机制判断**：它不是单个 ASD 闭环系统，但强烈支撑 agentic harness / capability evolution。
- **分类复核**：保持 `ASD 相关系统`；`X0` 正确；`Y5` 正确；`Z1,Z3,Z4,Z5,Z7,Z8` 正确。
- **写作用途**：适合作为“工具基础设施如何让 ASD 从原型走向工作台”的核心材料。

## 深读补充（按 MARS 标准）

### 研究问题
ToolUniverse 关注 AI scientists 难以构建的原因：工具、数据、模型和分析环境分散，缺少统一可调用、可组合、可优化的科学工具生态。

### 系统架构 / 工作流
系统提供 600+ models、datasets、APIs 和 scientific packages，支持工具识别、调用、接口优化、新工具生成和 agentic workflow composition。

### 关键机制
核心是 scientific tool ecosystem 和 tool interface refinement。它让 AI scientist 从临时工具调用走向标准化工具宇宙。

### 实验验证与证据
原文以 hypercholesterolemia case study 展示 ToolUniverse 构建 AI scientist 并识别具有良好预测性质的药物 analog。

### 局限性补充
ToolUniverse 是基础设施，不是单个发现闭环。工具质量、权限、安全和错误传播需要治理。

### XYZ 分类逐项解释
- `X0`：不是固定多智能体系统。
- `Y5`：工具接口优化、新工具生成和 workflow composition 属于 capability / harness evolution。
- `Z1,Z3,Z4,Z5,Z7,Z8`：覆盖知识、工具设计、执行、分析、验证和迭代。

### 综述写作用法
适合基础设施章节，也是 harness evolution 的强证据。
