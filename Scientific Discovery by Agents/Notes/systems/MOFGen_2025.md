# MOFGen 2025

## 基本信息
- **论文**: System of Agentic AI for the Discovery of Metal-Organic Frameworks
- **作者**: Theo Jaffrelot Inizan, Sherry Yang, Aaron Kaplan, Yen-hsu Lin, Jian Yin, Saber Mirzaei, Mona Abdelgaid, Ali H. Alawadhi, KwangHwan Cho, Zhiling Zheng, Ekin Dogus Cubuk, Christian Borgs, Jennifer T. Chayes, Kristin A. Persson, Omar M. Yaghi
- **年份**: 2025
- **来源**: arXiv:2504.14110
- **关键词**: MOF, materials-discovery, agentic-ai, candidate-generation, synthesis-validation

## 核心思想
MOFGen 面向 metal-organic frameworks 的自动化发现。论文指出，材料生成模型需要同时满足性能、结构可行性和合成可行性，因此不能只依赖单一生成模型，而需要多个专门模块协作。

## 方法细节
MOFGen 由多个 interconnected agents / modules 组成，包括提出 novel MOF compositions 的 LLM、生成 crystal structures 的 diffusion model、优化和筛选候选的 quantum mechanical agents，以及由专家规则和机器学习引导的 synthetic-feasibility agents。

## 关键结果
系统生成了大量 novel MOF structures 和 synthesizable organic linkers，并通过 high-throughput experiments 和成功合成 5 个 AI-dreamt MOFs 进行验证。

## 局限性
MOFGen 的“agentic”更多体现为异质科学能力和模型模块协同，而不是自然语言多角色 agents。其流程面向特定材料类别，迁移到其他科学领域仍需要重新设计。

## 核心贡献
MOFGen 的核心贡献是将生成、量子力学筛选、合成可行性判断和实验验证连接成 MOF 发现工作流。

## 与综述的关联
该工作适合放入 `X2-Y2-Z2/Z3/Z4/Z5/Z7/Z8`，属于严格 ASD 候选。它支持本文关于“多”的能力之多：多智能体不只是多个 LLM，也可以是 LLM、扩散模型、计算代理、合成可行性代理和实验验证的组合。

## 原文核对与分类复核
- **原文核对**：原文提出 Agentic AI system for MOF discovery，包括 LLM composition proposer、diffusion structure generator、quantum mechanical agents 和 synthetic-feasibility agents。
- **机制判断**：它生成大量 novel MOF structures / linkers，并通过高通量实验和专家规则/模型进行验证。
- **分类复核**：保持 `严格 ASD`；`X2` 正确；`Y2` 正确，因为核心是候选生成、过滤和验证；`Z2,Z3,Z4,Z5,Z7,Z8` 正确。
- **写作用途**：适合作为多能力 agent 组合发现材料结构的核心例子。

## 深读补充（按 MARS 标准）

### 研究问题
MOFGen 关注 MOF 发现中化学空间巨大、结构生成与可合成性难以同时保证的问题。

### 系统架构 / 工作流
系统由 LLM composition proposer、diffusion structure generator、quantum mechanical agents 和 synthetic-feasibility agents 组成，形成多能力 agentic AI system。

### 关键机制
核心是多模型/多 agent 协同：LLM 提出组成，diffusion model 生成结构，量子力学 agents 优化与过滤，synthetic feasibility agents 判断可合成性。

### 实验验证与证据
原文报告生成大量 novel MOF structures 和 synthesizable linkers，并通过 high-throughput experiments 及相关计算/规则验证。

### 局限性补充
生成空间、可合成性模型和数据库偏差会影响结果。真实合成与长期性能仍需要进一步验证。

### XYZ 分类逐项解释
- `X2`：多个明确能力模块/agents 协同。
- `Y2`：候选组成、结构和 linker 被生成、过滤、选择。
- `Z2,Z3,Z4,Z5,Z7,Z8`：覆盖候选设计、结构生成、计算执行、分析、验证和迭代。

### 综述写作用法
适合材料发现严格 ASD 小节，说明多智能体可以组织 LLM、diffusion、QM 和 feasibility checking。
