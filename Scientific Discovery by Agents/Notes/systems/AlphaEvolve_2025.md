# AlphaEvolve 2025

## 基本信息
- **论文**: AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery
- **作者**: Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex Davies, Sebastian Nowozin, Pushmeet Kohli, Matej Balog
- **年份**: 2025
- **来源**: arXiv:2506.13131
- **关键词**: system, coding-agent, scientific-discovery, algorithmic-discovery, verification

## 核心思想
很多科学和算法发现可以被表达为“提出候选程序、运行 evaluator、保留更优版本”的搜索问题。传统 LLM 代码生成能提出候选，但缺乏系统化的长程进化、自动评估和保留改进机制。

AlphaEvolve 要解决的问题是：能否用 coding agent 在自动 evaluator 约束下进行科学和算法 discovery。

## 方法细节
AlphaEvolve 使用 evolutionary generate-test-refine loop：LLM autonomous pipeline 直接修改候选算法代码，并从一个或多个 automated evaluators 接收反馈。

核心流程是：

1. 给定问题、约束和 evaluator；
2. LLM 生成候选代码或算法；
3. 系统运行自动评估器测试候选；
4. 根据结果选择、修改和进化候选；
5. 多轮搜索后得到更高性能或新发现；公开的 `google-deepmind/alphaevolve_results` 仓库只包含数学发现结果与正确性验证 notebook，不包含运行 AlphaEvolve 的系统代码。

这种形式把“发现”转化为可执行 artifact 的优化。

## 关键结果

1. AlphaEvolve 被用于优化 Google 大规模计算栈中的关键组件，包括 data center scheduling、hardware accelerator circuit simplification，以及加速训练支撑 AlphaEvolve 的 LLM。
2. 在数学和计算机科学问题上，AlphaEvolve 发现了新的、可证明正确的算法，扩展了 prior automated discovery methods 的适用范围。
3. 一个代表性结果是发现了用 **48 次 scalar multiplications** 计算两个 `4 x 4` complex-valued matrices 相乘的过程，这是该设置中 56 年来对 Strassen 算法后的首次改进。

## 与综述的关联

在 Scientific Workflow 中，它覆盖 Hypothesis Generation、Execution 和 Verification。

在 Skill Lifecycle 中，它对应 Representation / code skill、Execution / code run、Evolution / iterative refinement 和 Verification / automated evaluator。

Evidence Role 应标为 **Indirect + Direct**。它对自然科学发现不是直接湿实验样本，但对“可验证 discovery loop”非常关键：只有当候选可以被自动 evaluator 检验时，agentic discovery 才能稳定迭代。

## 局限性

AlphaEvolve 更适合可形式化、可自动评估的任务。许多科学假设没有快速 evaluator，湿实验和临床验证也不能像代码测试一样廉价运行。

公开材料主要是 white paper 和结果验证 notebook，而不是完整可运行系统；因此复现实验发现流程本身需要额外系统实现和计算资源。

## 核心贡献

AlphaEvolve 的核心贡献是把 discovery 组织为 code artifact generation、automated evaluation 和 evolutionary refinement，为可验证 scientific skill evolution 提供强机制样本。
