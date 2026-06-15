# AlphaProof Nexus 2026

## 基本信息
- **论文**: Advancing Mathematics Research with AI-Driven Formal Proof Search
- **作者**: George Tsoukalas, Anton Kovsharov, Sergey Shirobokov, Anja Surina, Moritz Firsching, Gergely Berczi, Francisco J. R. Ruiz, Arun Suggala, Adam Zsolt Wagner, Eric Wieser, Lei Yu, Aja Huang, Miklos Z. Horvath, Andrew Ferrauiolo, Henryk Michalewski, Codrut Grosu, Thomas Hubert, Matej Balog, Pushmeet Kohli, Swarat Chaudhuri
- **年份**: 2026
- **来源**: arXiv:2605.22763v1; code/results: https://github.com/google-deepmind/alphaproof-nexus-results
- **关键词**: mathematical discovery, formal proof search, Lean, multi-agent, evolutionary search, AlphaProof, Erdos problems, Google DeepMind

## 核心思想

AlphaProof Nexus 要解决的问题是：LLM 已经能做复杂数学推理，但自然语言证明容易包含细微错误，难以直接进入研究级数学工作。作者提出用 Lean 这样的形式化证明语言把数学发现转化为“生成可验证代码”的问题，由 Lean compiler 对每一步进行机械验证。

论文的核心主张不是“LLM 能写出漂亮自然语言证明”，而是：当问题可以被形式化为 Lean theorem sketch 时，agent 可以在 LLM 生成、Lean 验证、证明草图改写、工具调用和演化式搜索之间形成闭环，从而在开放研究问题上产生可机器验证的证明 artifact。

## 方法细节

AlphaProof Nexus 是一个面向 LLM-aided proof generation 的框架。输入是 Lean 文件：包含目标 theorem、依赖定义和 imports，证明部分用 `sorry` 占位；用户可额外提供自然语言上下文和 Lean 编码的领域知识。系统只允许 agent 修改 `EVOLVE-BLOCK` 和 `EVOLVE-VALUE` 标记包围的代码片段。成功输出是无 `sorry` 且能通过 Lean 编译的证明。

论文比较了四类 agent 配置：

- **Agent A basic**：多个 prover subagents 独立运行。每个 subagent 执行多轮 LLM 推理和 search-and-replace 修改，每轮后调用 Lean 编译器检查，错误信息反馈到下一轮。
- **Agent B basic + AlphaProof**：在 basic loop 中允许调用 AlphaProof 作为 focused proof tool，AlphaProof 可返回 proof、disproof 或 failure message。
- **Agent C evolutionary**：受 AlphaEvolve 启发，prover subagents 从共享 population database 中采样并写回 proof sketches；rating agents 用 plausibility、clarity、novelty 等维度做相对比较，并聚合成 Elo rating，再用 P-UCB 采样驱动搜索。
- **Agent D full-featured**：结合 AlphaProof 工具调用和 evolutionary population database，是论文探索 open research problems 的主配置。

这个系统很适合本综述的 multi-agent / evolutionary 主题：它不是单个 proof model 一次性输出答案，而是由 prover subagents、rating agents、Lean validator、AlphaProof tool 和 population database 共同构成的搜索-验证-演化系统。

## 关键结果

- 在 Formal Conjectures 中可用的 **353 个 Erdos open problems Lean statements** 上，full-featured agent 解决 **9/353** 个问题。作者称其中包含两个已开放 **56 年**的问题。
- 在 OEIS 任务中，系统从 492 个 autoformalized open questions 中证明 **44/492** 个 conjectures；作者要求先证明 test lemmas 来缓解 misformalization 风险。
- 系统还解决或推进了多个研究级方向：代数几何中约 **15 年**的 Hilbert functions open question、凸优化中更强的 Anchored GDA 收敛界、图论重构相关变体、Ben Green list 中的 additive combinatorics 问题、量子光学构造问题等。
- 成本上，摘要称 full-featured agent 解决 Erdos 问题的 inference cost 为每题 **a few hundred dollars**；正文和补充材料显示成本和 wall-clock time 方差较大。
- 后验分析显示，basic agent 也能复现 9 个 Erdos 成功，但在困难问题上成本更高；带 AlphaProof 或 full-featured 配置在部分困难问题上更有效。
- 单独把 AlphaProof 作为 tree-search baseline，在 9 个 Erdos 问题上即使用约 **64 v6e TPU hours per problem** 的预算也没有解决这些问题。这说明成功不只是底层 theorem prover 的结果，而是 agentic loop、上下文改写和搜索策略的组合效果。

## 局限性

AlphaProof Nexus 的强验证能力建立在 Lean formalization 之上。只有被形式化为 Lean theorem sketch 的问题才能进入这个闭环；Erdos evaluation 的 353 个问题来自开源 Formal Conjectures 仓库，天然偏向更容易形式化的问题，而不是全部 1200+ Erdos problem catalog 的无偏样本。

系统仍需要人类数学家提供或确认形式化目标，并在 solved 后验证 Lean statement 是否忠实表达原始问题。论文还报告了 misformalization 和 hallucinated established lemma 等失败模式，说明形式验证能检查 proof，但不能自动保证 problem statement、背景假设和自然语言解释完全正确。

演化式配置也不总是最优。论文的对比显示，basic / AlphaProof-equipped agents 在一些问题上成本更低；full-featured agent 在困难问题上更强，但计算开销、方差和系统复杂度都更高。

## 核心贡献

AlphaProof Nexus 的核心贡献是把数学发现组织成可机器验证的多智能体演化搜索：LLM prover 生成和改写 Lean proof sketches，Lean compiler 提供硬验证，AlphaProof 作为 focused proof tool，rating agents 和 population database 支撑跨尝试的演化式复用。

## 与综述的关联

在 Scientific Workflow 中，AlphaProof Nexus 覆盖 Hypothesis/Proof Search、Execution、Verification 和 Evolution。它展示了一个与 wet-lab discovery 不同但同样重要的“形式化科学发现”路径：当领域存在形式验证器时，agentic discovery 可以把 output 直接变成可审计、可复现、可机器检查的 artifact。

在 Skill Lifecycle 中，它对应：

- **Representation**：Lean theorem sketch、proof sketch、`EVOLVE-BLOCK` / `EVOLVE-VALUE`；
- **Execution**：LLM subagent 修改 Lean code，调用 Lean compiler 和 AlphaProof；
- **Composition**：prover subagents、rating agents、validator、AlphaProof tool 的组合；
- **Evolution**：population database、Elo rating、P-UCB sampling；
- **Verification**：sorry-free Lean proof compilation。

Evidence Role 应标为 **Direct + Boundary**。它直接支撑 multi-agent/evolutionary workflow，但同时也给出边界：形式化数学中的强验证不能直接泛化到自然语言论文、湿实验或开放式科学假设。

## 可引用点

| 点 | 内容 |
|---|---|
| 最强数字 | 9/353 Erdos problems；44/492 OEIS conjectures |
| 核心机制 | LLM prover subagents + Lean compiler feedback + optional AlphaProof + evolutionary population database |
| 验证方式 | 输出必须是 sorry-free Lean proof，并通过 compiler |
| 人类角色 | 提供/确认 formalization，检查 Lean statement 是否忠实表达原始问题 |
| 综述位置 | formal verification / mathematical discovery / evolutionary multi-agent workflow |

## 写作时避免

- 不能写成“Google solved all Erdos problems”；论文只报告 353 个已形式化问题中的 9 个。
- 不能写成“AlphaProof 单独解决了这些问题”；论文明确显示 standalone AlphaProof baseline 未解决 9 个 Erdos problems。
- 不能把 Lean proof 通过等同于自然语言科学解释完全正确；statement fidelity 仍需人类检查。
- 不能把 formal proof search 的成功泛化为所有科学领域都有同等强验证闭环。
