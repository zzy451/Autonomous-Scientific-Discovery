# MAESTRO 2026

## 基本信息
- **论文**: Reasoning-Driven Design of Single Atom Catalysts via a Multi-Agent Large Language Model Framework
- **作者**: Dong Hyeon Mok, Seoin Back, Victor Fung, Guoxiang Hu
- **年份**: 2026
- **来源**: arXiv:2602.21533
- **关键词**: multi-agent, catalyst-discovery, reasoning-driven-design, design-history, autonomous-loop

## 核心思想
MAESTRO 关注单原子催化剂设计。论文提出，多智能体 LLM 框架可以通过推理、反思和设计历史积累来发现高性能催化剂，而不只是执行传统机器学习筛选。

## 方法细节
MAESTRO 的全称是 Multi-Agent-based Electrocatalyst Search Through Reasoning and Optimization。多个具有专门角色的 LLM agents 在 autonomous design loop 中协作：它们提出修改、反思结果、积累设计历史，并通过 in-context learning 改进后续设计。

## 关键结果
论文报告 MAESTRO 识别出 LLM 背景知识中未显式编码的 design principles，并发现打破反应中间体 conventional scaling relations 的催化剂候选。

## 局限性
MAESTRO 主要处于计算和候选发现层面，真实实验验证、长期复现和安全边界仍需要进一步确认。

## 核心贡献
MAESTRO 的核心贡献是展示多智能体推理循环可以在催化剂发现中形成设计原则并改进候选。

## 与综述的关联
该工作适合放入 `X2-Y1-Z2/Z3/Z4/Z5/Z7,Z8`，属于严格 ASD 候选。它补强多智能体反思、设计历史和科学产物迭代。

## 原文核对与分类复核
- **原文核对**：原文提出 Multi-Agent-based Electrocatalyst Search Through Reasoning and Optimization，多个专门 LLM agents 在 autonomous design loop 中 reason、propose modifications、reflect on results，并积累 design history。
- **机制判断**：它支撑催化剂设计闭环，核心是反思、结果反馈和设计历史累积。
- **分类复核**：保持 `严格 ASD`；`X2` 正确；`Y1` 正确，因为 reflection 是核心；`Z2,Z3,Z4,Z5,Z7,Z8` 正确。
- **写作用途**：适合说明 multi-agent reflection 在材料/催化剂设计中的作用。

## 深读补充（按 MARS 标准）

### 研究问题
MAESTRO 面向 single atom catalysts 设计，关注如何让 LLM agents 在材料发现中进行推理、反思和基于结果的优化。

### 系统架构 / 工作流
系统全称为 Multi-Agent-based Electrocatalyst Search Through Reasoning and Optimization。多个专门 LLM agents 在 autonomous design loop 中提出修改、分析结果、反思并累积 design history。

### 关键机制
核心是 reflection + design history。系统不是纯粹暴力搜索，而是通过多 agent 推理和结果反馈逐步改进催化剂候选。

### 实验验证与证据
原文面向 oxygen reduction reaction 的 single atom catalysts 设计，展示 LLM reasoning 与 in-context learning 在材料发现中的作用。

### 局限性补充
材料候选的真实实验可行性、DFT/模拟精度和长期稳定性仍需专家验证。

### XYZ 分类逐项解释
- `X2`：多个 specialized LLM agents 协作。
- `Y1`：reflect on results 和 design history 是核心。
- `Z2,Z3,Z4,Z5,Z7,Z8`：覆盖设计、执行、分析、验证和迭代。

### 综述写作用法
适合材料发现小节中说明 multi-agent reflection 的作用。
