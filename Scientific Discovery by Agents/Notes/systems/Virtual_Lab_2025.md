# Virtual Lab 2025

## 基本信息
- **论文**: The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies
- **作者**: Kyle Swanson, Wesley Wu, Nash L. Bulaong, John E. Pak, James Zou
- **年份**: 2025
- **来源**: Nature, doi:10.1038/s41586-025-09442-9
- **关键词**: autonomous-science, virtual-lab, multi-agent, protein-design, nanobody, wet-lab-validation

## 核心思想
这篇论文要解决的问题是：复杂的跨学科科研项目通常需要免疫学、机器学习、计算生物学和实验生物学等多个领域专家协作，但很多研究者并不容易获得这样一支专家团队。现有 LLM 多用于回答具体科学问题、总结论文或写代码，较少用于执行开放式、跨学科、需要真实实验验证的研究项目。

作者提出 Virtual Lab，目标是用一个由 LLM Principal Investigator 和多个 LLM scientist agents 组成的虚拟科研团队，在人类研究者高层指导下完成复杂科研任务。论文用 SARS-CoV-2 新变体 nanobody 设计作为示范任务。

## 方法细节
Virtual Lab 的核心不是单个 agent，而是一组通过会议机制协作的角色化 agent。每个 agent 由四个字段定义：Title、Expertise、Goal、Role。人类研究者先定义 Principal Investigator（PI）和 Scientific Critic，然后 PI 根据项目描述自动创建具体 scientist agents。

在本文的 nanobody 设计项目中，PI 创建了三个 scientist agents：

- Immunologist
- Machine Learning Specialist
- Computational Biologist

Virtual Lab 通过两类会议推进研究：

- **Team meeting**：所有 agent 讨论高层研究问题，PI 负责引导、综合和总结，Scientific Critic 负责指出局限。
- **Individual meeting**：单个 scientist agent 处理具体任务，例如写 ESM、AlphaFold-Multimer 或 Rosetta 的代码，Scientific Critic 可参与批评和改进。

同一会议也可以并行运行多次：高温度生成多个回答，再用低温度 merge meeting 汇总，从而兼顾创造性和稳定性。

本文的 nanobody 项目分五个阶段：

1. Team selection：PI 选择 Immunologist、Machine Learning Specialist、Computational Biologist。
2. Project specification：决定设计 nanobody 而非标准 antibody，并选择修改已有 nanobody 而非 de novo design。
3. Tools selection：选择 ESM、AlphaFold-Multimer、Rosetta。
4. Tools implementation：由 agent 写 ESM LLR、AlphaFold-Multimer ipLDDT、Rosetta dG 相关代码。
5. Workflow design：组合工具形成多轮 mutation-selection pipeline。

计算 pipeline 从四个已有 SARS-CoV-2 Wuhan strain RBD nanobodies 出发：Ty1、H11-D4、Nb21、VHH-72。Round 1 先用 ESM 计算所有单点突变的 log-likelihood ratio（ESM LLR），保留 top 20；round 2-4 则从上一轮 top 5 输入序列分别扩展，每轮形成 100 个候选。候选再用 AlphaFold-Multimer 预测 nanobody-spike complex 并计算 AF ipLDDT，最后用 Rosetta relax 结构并计算 binding energy（RS dG）。三者合成 weighted score：

`WS = 0.2 * ESM LLR + 0.5 * AF ipLDDT - 0.3 * RS dG`

每轮按 WS 保留 top 5 进入下一轮，共迭代 4 轮，最多引入 4 个突变。最终跨不同突变轮数比较时，系统改用相对于 wild type 的 ESM LLRWT 计算 WSWT，并为每个起始 nanobody 选择 23 个突变体，共 92 个 mutant nanobodies 进入实验验证。

## 关键结果

1. **Virtual Lab 设计出 92 个新 nanobodies**  
   系统从 Ty1、H11-D4、Nb21、VHH-72 四个已有 nanobody 出发，每个生成 23 个突变体，总共 **92 个**设计进入实验验证。

2. **计算指标显示突变体整体优于 wild type**  
   所有 92 个突变体都有正 ESM LLR，说明 ESM 相比 wild type 更偏好这些序列。**78/92（85%）** 的突变体 AF ipLDDT 高于对应 wild type；**32/92（35%）** 的 AF ipLDDT ≥ 80；**60/92（65%）** 的 Rosetta dG 优于对应 wild type；**23/92（25%）** 的 RS dG ≤ -50。

3. **表达与可溶性较好**  
   实验表达显示 **35/92（38%）** 的设计每升细胞培养物中可获得超过 25 mg soluble periplasmic nanobody；只有 **6/92（6.5%）** 低于 5 mg/l。作者据此认为 Virtual Lab 引入的突变整体没有造成大规模 misfolding 或 aggregation。

4. **大部分 H11-D4 和 Nb21 突变体保留 Wuhan RBD binding**  
   ELISA 测试 96 个 nanobodies（92 个突变体 + 4 个 wild type）对多个 spike RBD 的结合。在 H11-D4 和 Nb21 系列中，**44/46（96%）** 突变体保留 Wuhan RBD binding。Ty1 系列表现较差，只有 **10/23** 保留 Wuhan RBD binding；VHH-72 系列中 **13/22** 保留接近 wild type 的 Wuhan RBD binding。

5. **两个突变体显示对新变体的改进 binding profile**  
   Nb21(I77V/L59E/Q87A/R37Q) 对 JN.1 RBD 显示 ELISA binding，且对 MERS-CoV RBD 和 BSA 无明显非特异结合。其 JN.1 RBD 的 EC50 约 **2.0 ng/ml**，弱于 Wuhan RBD 的 **0.2 ng/ml**，但 wild-type Nb21 对 JN.1 RBD binding 很低，因此突变体有改进。该突变体还提高了 KP.3 RBD binding，平均 intensity 为 **3.5**，而其他 Nb21 mutants 平均为 **0.06 ± 0.09（n=22）**，unmutated sequence 为 **0.1**。  
   Ty1(V32F/G59D/N54S/F32S) 则提升了 Wuhan RBD binding，并获得中等 JN.1 RBD binding，而 unmutated Ty1 没有可见 JN.1 RBD binding。

6. **人类输入量较少，但不是零**  
   Virtual Lab 的会议阶段每次会议或并行会议约需 **5-10 分钟**，GPT-4o token 成本约 **1-2 美元**；全部会议阶段约 **1-2 小时**、**10-20 美元**。考虑 prompt 调整、审阅和调试 agent 写的代码，workflow 设计耗时数天；计算 pipeline 运行约一周，nanobody 合成约六周，binding 实验约两周。  
   人类研究者在所有阶段共写 **1596 words**，约占 Virtual Lab 总文字量 **1.3%**；LLM agents 写 **122462 words**，占 **98.7%**。ESM、AlphaFold-Multimer 和 Rosetta 脚本由 agent 从头写成，但部分数据整理和 job scheduling 脚本由人类研究者补充。

## 与综述的关联

Virtual Lab 是“skill-driven scientific discovery”非常重要的间接证据。它没有显式称自己为 skill system，但它清楚展示了科研能力如何被拆成角色、会议、工具实现和 workflow design 几类可复用程序单元。

在 Scientific Workflow 上，它覆盖：

- Hypothesis / project specification：决定 nanobody vs antibody、modify existing vs de novo。
- Experiment Design：选择起始 nanobody、设计计算筛选流程。
- Execution：调用 ESM、AlphaFold-Multimer、Rosetta，生成并运行代码。
- Verification：表达实验、ELISA binding、RBD panel 实验。
- Synthesis：PI agent 总结会议，形成研究决策。

在 Skill Lifecycle 上，它对应：

- Representation：agent role prompt、meeting agenda、tool scripts、weighted scoring workflow。
- Acquisition：通过多 agent 讨论、Scientific Critic 反馈和人类高层约束形成方案。
- Composition：team meeting + individual meeting + parallel/merge meeting 构成层级式组合。
- Execution：代码生成、计算工具调用和 wet-lab validation。
- Evolution：多轮 mutation-selection pipeline，以及会议中的批评-改进循环。
- Verification：结构模型指标、表达量、ELISA binding、非特异 binding 检查。

Evidence Role 应标为 **Indirect + Infrastructure**。它证明多 agent 角色协作可以生成可执行科研 workflow 和代码，并产出经实验验证的蛋白设计候选；但它不是完整自动实验室，合成和实验仍由人类完成。

与 Co-Scientist 相比，Virtual Lab 更强调“虚拟跨学科团队”和会议协议；Co-Scientist 更强调 hypothesis tournament 和生物医学假设排序。与 Robin 相比，Virtual Lab 更偏工具链构建和 protein design，Robin 更偏实验数据分析反馈循环。

## 局限性

- 人类研究者仍然提供高层目标、会议 agenda、prompt 调整、代码审阅、调试和部分数据/job 脚本，不是完全自主系统。
- 实验验证仍由人类生物学家完成，Virtual Lab 不控制机器人实验设备。
- 研究只在 SARS-CoV-2 nanobody design 一个任务中验证，跨科学领域泛化仍是推断。
- 系统依赖 GPT-4o 知识和生成能力；knowledge cutoff 可能导致不了解最新工具或文献，例如作者提到 AlphaFold 3 与 AlphaFold-Multimer 的例子。
- prompt engineering 仍然重要；没有合适 agenda 时，agent 可能给出空泛回答。
- LLM 可能产生幻觉、错误科学事实或错误引用，仍需人类基于可信来源核查关键事实和决策。
- Ty1 系列出现较差 Wuhan RBD binding，H11-D4 系列中也有 3 个突变体对 BSA 和全部 RBD 高非特异结合，说明 pipeline 仍会产生有问题设计。
- 当前实验主要是 binding profile，没有证明 neutralization、体内效果或临床可用性。

## 核心贡献

Virtual Lab 的核心贡献是把多 agent 会议机制用于真实跨学科科研项目，自动设计并实现 ESM + AlphaFold-Multimer + Rosetta 的 nanobody design workflow，最终产生 92 个经实验验证的 SARS-CoV-2 nanobody 突变体，其中两个显示对 JN.1 或 KP.3 等新变体的改进 binding profile。
