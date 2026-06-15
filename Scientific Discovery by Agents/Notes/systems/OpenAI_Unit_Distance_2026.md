# OpenAI Unit Distance 2026

## 基本信息
- **论文**: Planar Point Sets with Many Unit Distances
- **作者**: OpenAI
- **年份**: 2026
- **来源**: OpenAI proof PDF; OpenAI remarks PDF by Noga Alon, Thomas F. Bloom, W. T. Gowers, Daniel Litt, Will Sawin, Arul Shankar, Jacob Tsimerman, Victor Wang, Melanie Matchett Wood; Nature News doi:10.1038/d41586-026-01651-0
- **关键词**: mathematical discovery, unit distance problem, Erdos conjecture, AI-generated proof, human verification, discrete geometry, number theory

## 核心思想

这项工作报告了一个 OpenAI 内部模型生成的数学反例：对平面有限点集的 unit distance problem，模型构造了无限多组点集，使 unit-distance pairs 数量达到 $n^{1+\epsilon}$ 级别，从而否定 Erdos 关于 unit distances 几乎线性的猜想。

它对本综述的重要性不在于具体数论构造本身，而在于展示了一条不同于 wet-lab 和代码 benchmark 的科学发现路径：AI 可以在开放数学问题上提出完整反例，再经由 AI grading、人类数学家、外部专家和后续 human-edited exposition 进入可验证科学记录。

## 方法细节

OpenAI proof PDF 的 AI use statement 说明，该问题首先由内部模型在完全自动方式下解决：模型收到 AI-written problem statement，输出被送入 AI grading pipeline，系统给出高置信度后，OpenAI 内部研究者和数学家才开始仔细检查。随后经过 AI-assisted verification and rewriting，草稿被送给外部数学家和 number theory experts 验证，最终形成 human-edited exposition。

论文正文的数学路线是：通过无限 unramified tower of totally real number fields with 3-power Galois groups，构造固定有理素数在塔中完全分裂的情形；再 adjoining $i$ 得到 CM fields，利用 class field tower、Golod-Shafarevich theory、bounded root discriminants 和 class number 控制，构造平面点集，使 unit-distance pairs 超过 Erdos conjecture 预期。

OpenAI remarks PDF 则给出人类数学家消化后的版本和评论。它明确说这是 OpenAI-generated counterexample 的 human-verified、简化和推广版本，并强调原 AI proof 后续经过 Codex 辅助的 exposition refinement 和专家验证。

## 关键结果

- 主定理：存在常数 $\epsilon > 0$ 和无限多正整数 $n$，使得某些 $n$ 点平面集合的 unit-distance pairs 数量至少为 $n^{1+\epsilon}$。
- 该结果否定了 Erdos 的 unit distance conjecture，即 unit distances 应为 $n^{1+o(1)}$ 级别的猜想。
- OpenAI proof PDF 声称原始解法由内部模型自动生成，之后才进入人类检查和外部专家验证流程。
- remarks PDF 中多位数学家认为该反例的重要性不仅在于结果本身，也在于它暴露了 AI 在跨领域搜索、尝试反直觉方向、提出 surprise construction 方面的潜力。

## 局限性

这项工作目前公开的是 OpenAI proof PDF、专家 remarks 和 Nature News 报道，而不是完整的系统论文。模型架构、训练方法、搜索过程、AI grading pipeline 的细节并未公开。因此它是很强的科学发现案例，但不是可复现实验系统描述。

结果经历了人类数学家的检查、重写和外部专家验证。它不能被写成“AI 输出后无需人类即可进入数学文献”。相反，它更适合作为 human-verified AI discovery 的案例：AI 产生关键反例，人类完成严格审查、整理、归因和上下文化。

remarks PDF 也提醒：该结果不能说明 AI 数学系统不会产生错误证明；许多 AI proof claims 可能更容易说服人类去检查，而不一定正确。因此对综述而言，它应与 AlphaProof Nexus 形成对照：OpenAI unit-distance 展示开放数学创意，AlphaProof Nexus 展示形式化验证闭环。

## 核心贡献

OpenAI unit-distance 工作的核心贡献是给出一个 AI-generated、human-verified 的开放数学问题反例案例，说明 autonomous discovery 不必局限于实验室或工程 benchmark，也可以发生在数学 conjecture 的探索空间中。

## 与综述的关联

在 Scientific Workflow 中，它覆盖 Hypothesis Generation、Mathematical Construction、Verification 和 Synthesis。它适合放在“mathematical discovery and verification”小节，与 AlphaProof Nexus 共同支撑数学发现线。

在 Skill Lifecycle 中，它目前只能部分映射：

- **Acquisition / Search**：模型从 problem statement 出发寻找反例路线；
- **Execution**：生成完整证明草稿；
- **Verification**：AI grading pipeline、人类数学家、外部专家；
- **Synthesis**：human-edited exposition 与专家 remarks。

Evidence Role 应标为 **Direct + Boundary**。它直接展示 AI 可以产生研究级数学发现，但边界也很清楚：系统细节不公开，验证仍高度依赖人类数学共同体。

## 可引用点

| 点 | 内容 |
|---|---|
| 结果 | 反驳 Erdos unit distance conjecture |
| 发现方式 | OpenAI internal model 自动生成原始证明，之后经 AI grading 和人类专家验证 |
| 验证形态 | human-edited proof PDF + human-verified remarks |
| 对照工作 | AlphaProof Nexus 的 Lean formal proof search |
| 综述位置 | mathematical discovery, human verification, boundary of autonomy |

## 写作时避免

- 不要写成 Meta 的工作；当前可靠来源指向 OpenAI。
- 不要写成完全无人工参与的最终发表流程；最终证明经过人类检查、重写和专家验证。
- 不要把这项工作当作可复现系统论文；公开材料缺少模型和 pipeline 细节。
- 不要把一个数学反例直接泛化为所有科学领域的 autonomous discovery 能力。
