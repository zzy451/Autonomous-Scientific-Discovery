# Curie 2025

## 基本信息
- **论文**: Curie: Toward Rigorous and Automated Scientific Experimentation with AI Agents
- **作者**: Patrick Tser Jern Kon, Jiachen Liu, Qiuyi Ding, Yiming Qiu, Zhenning Yang, Yibo Huang, Jayanth Srinivasa, Myungjin Lee, Mosharaf Chowdhury, Ang Chen
- **年份**: 2025
- **来源**: arXiv:2502.16069
- **关键词**: experimentation, rigor, AI-agents, reproducibility

## 核心思想
Curie 关注自动科学实验中的 rigor，试图让 agentic experimentation 更可靠、可控和可解释。

## 方法细节
系统包含 intra-agent rigor、inter-agent rigor 和 experiment knowledge modules，用于约束实验设计和执行。

## 关键结果
论文报告 Curie 在实验问题回答上相对强基线有 3.4 倍提升。

## 局限性
主要面向计算机科学实验，不是通用科学发现系统。

## 核心贡献
把 rigor 作为自动实验 agent 的一等设计目标。

## 与综述的关联
适合放入 `X2-Y1-Z2/Z3/Z4/Z5/Z7`，支撑实验执行和验证边界。

## 原文核对与分类复核
- **原文核对**：原文针对 rigorous automated scientific experimentation，提出 intra-agent rigor、inter-agent rigor 和 experiment knowledge module。
- **机制判断**：它支撑实验自动化中的可靠性、控制性和可解释性，不是完整科学发现系统，但对 ASD 的实验执行与验证非常关键。
- **分类复核**：保持 `ASD 相关系统`；`X2` 正确，因原文有 inter-agent rigor；`Y1` 正确，因核心是实验反馈、修正和严谨性控制；`Z2,Z3,Z4,Z5,Z7` 正确。
- **写作用途**：适合放在 experiment / execution rigor 和 multi-agent risk mitigation 小节。

## 深读补充（按 MARS 标准）

### 研究问题
Curie 关注自动科学实验中的 rigorous experimentation。LLM 可以自动化许多环节，但如果缺少可靠性、控制性和可解释性，实验结论就很难可信。

### 系统架构 / 工作流
系统包含 intra-agent rigor module、inter-agent rigor module 和 experiment knowledge module，用于提升实验设计、执行和解释的严谨性。

### 关键机制
核心是把 rigor 嵌入 agent workflow。intra-agent 模块提升单 agent 可靠性，inter-agent 模块维持方法控制，knowledge module 增强可解释性。

### 实验验证与证据
原文构建 46 个跨四个计算机科学领域的 experimental benchmark，报告相对强 baseline 有明显提升。

### 局限性补充
Curie 重点是科学实验 rigor，不是完整发现闭环；并且 benchmark 主要来自计算机科学实验问题。

### XYZ 分类逐项解释
- `X2`：inter-agent rigor 明确涉及多智能体。
- `Y1`：通过实验反馈和严谨性检查修正流程。
- `Z2,Z3,Z4,Z5,Z7`：覆盖问题、实验设计、执行、分析和验证。

### 综述写作用法
适合 verification / execution rigor 小节，也可作为多智能体风险控制案例。
