# CoScientist 2026

## 基本信息
- **论文**: Accelerating scientific discovery with Co-Scientist
- **作者**: Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Anil Palepu, Petar Sirkovic, Artiom Myaskovsky, Felix Weissenberger, Keran Rong, Ryutaro Tanno, Khaled Saab, Dan Popovici, Jacob Blum, Fan Zhang, Katherine Chou, Avinatan Hassidim, Burak Gokturk, Amin Vahdat, Pushmeet Kohli, Yossi Matias, Andrew Carroll, Kavita Kulkarni, Nenad Tomasev, Yuan Guan, Vikram Dhillon, Eeshit Dhaval Vaishnav, Byron Lee, Tiago R. D. Costa, Jose R. Penades, Gary Peltz, Yunhan Xu, Annalisa Pawlosky, Alan Karthikesalingam, Vivek Natarajan
- **年份**: 2026
- **来源**: Nature, doi:10.1038/s41586-026-10644-y; arXiv:2502.18864
- **关键词**: autonomous-science, co-scientist, multi-agent, biomedical-discovery, hypothesis-generation, wet-lab-validation

## 核心思想
这篇论文要解决的是：科学发现中最耗费专家精力的部分往往不是简单文献总结，而是提出新颖、可检验、和已有证据相容的研究假设。现有“deep research”类工具主要擅长检索和综合信息，但通常不能持续生成、批判、排序和演化假设，也缺少真实湿实验验证。

作者提出 AI Co-Scientist 的目标不是完全替代科学家，而是在科学家给定研究目标、偏好和约束后，帮助生成可实验验证的研究假设和研究方案。论文明确把系统定位为 scientist-in-the-loop 的协作系统，最终实验选择和科学判断仍由专家负责。

## 方法细节
AI Co-Scientist 是一个基于 Gemini 2.0 的多智能体系统，核心机制可以概括为“generate, debate, evolve”。

系统首先把科学家用自然语言描述的研究目标解析为 research plan configuration，其中包括目标、约束、偏好、评价标准等。默认评价标准包括 alignment、plausibility、novelty、testability 和 safety。

系统包含四类基础组件：

- 自然语言交互界面：科学家可输入研究目标、修改约束、补充反馈、审阅假设。
- 异步任务框架：Supervisor agent 管理任务队列、分配 worker、调度各类专门 agent，并支持 test-time compute scaling。
- 专门 agent 群：Generation、Reflection、Ranking、Proximity、Evolution、Meta-review 分别负责生成、批判、Elo tournament 排序、相似性聚类/去重、假设改写演化、以及综合反馈。
- Context memory：保存系统状态、agent 中间结果、tournament 进度和统计信息，支持长时程迭代和失败后重启。

关键机制是 Elo-based tournament。系统让不同研究假设进行成对比较和模拟科学辩论，由 Ranking agent 维护 Elo 排名；Evolution agent 根据高排名假设继续综合、类比、扩展或简化；Meta-review agent 汇总各轮 review 和 debate 中反复出现的问题，把反馈追加到后续 agent prompt 中。作者强调这种学习不依赖 fine-tuning 或 reinforcement learning，而是通过长上下文反馈实现迭代改进。

## 关键结果

1. **Elo 自动评价与 GPQA 正确率相关**  
   作者把 GPQA diamond 问题转成研究目标，比较 Co-Scientist 输出的 Elo rating 与正确率。选取每个问题最高 Elo 的结果时，Co-Scientist 在 GPQA diamond 上达到 **78.4% top-1 accuracy**。作者同时提醒，Elo 是系统内部自动评价指标，不是 ground truth。

2. **test-time compute scaling 提升假设质量**  
   在截至 2025-02-03 的 **203 个研究目标**上，作者把生成过程分成 10 个时间 bucket，观察 best Elo 和 top-10 average Elo。两项指标均随迭代推进上升，说明更多 test-time compute 与更高自动评价质量相关。

3. **专家评价中 Co-Scientist 输出更受偏好**  
   在 **15 个生物医学专家策划的困难研究目标**上，系统与 Gemini 2.0、OpenAI o1/o3-mini-high、DeepSeek R1、以及专家 best guess 进行比较。Elo 指标显示 Co-Scientist 随计算扩展超过其他模型和专家 best guess。  
   在其中 **11 个研究目标**上，专家进行人工偏好评估：Co-Scientist 平均偏好排名为 **2.36**，novelty 为 **3.64/5**，impact 为 **3.09/5**。作者强调这些是主观专家评价，不是客观真值。

4. **安全红队测试初步通过**  
   作者用 frontier LLMs 构造 **1200 个 adversarial research goals**，覆盖 **40 个生物医学和科学主题**，用于测试系统是否拒绝危险研究目标。论文报告系统通过了全部检查，但数据因敏感性未公开。

5. **AML 药物重定位验证**  
   系统先在 **2300 个已批准药物**和 **33 种癌症类型**构成的空间中生成候选。六位血液学/肿瘤学专家审阅了 **78 个 NIH Specific Aims 格式**的药物重定位方案。  
   对 AML，专家从 top-ranked hypotheses 中选择候选做体外实验。已有一定证据的 5 个候选中，Binimetinib、Pacritinib、Cerivastatin 抑制 MOLM-13 细胞活性；Binimetinib 的 IC50 最低达到 **7 nM**。  
   对没有 AML 既有临床/临床前证据的 3 个 novel candidates，KIRA6 在 KG-1、MOLM-13、HL-60 三种 AML 细胞系中均显示 nM 级抑制，IC50 分别为 **13 nM、517 nM、817 nM**。作者明确说这些结果只是早期体外 biological reality check，不等同于临床有效性。

6. **肝纤维化靶点发现**  
   专家从 **15 个 top-ranked hypotheses** 中选择 3 个研究方案。Co-Scientist 提出 3 个新的 epigenetic modifiers，并建议可由现有药物靶向。实验显示，针对其中 2 个 epigenetic modifiers 的药物在 human hepatic organoids 中具有显著 anti-fibrotic activity，且未造成细胞毒性；其中一个药物已被 FDA 批准用于其他适应症。

7. **抗菌耐药机制复现**  
   在 cf-PICIs 跨菌种传播机制问题上，研究者给系统一页背景材料和两篇相关论文。Co-Scientist 在 **2 天**内把“cf-PICIs 与不同 helper phage tails 相互作用以扩展宿主范围”列为 top-ranked hypothesis。该假设与独立研究团队多年实验得到、当时尚未公开的发现相吻合。作者也说明系统是在开放文献和多年领域知识基础上推理，不是凭空发现。

## 与综述的关联

这篇论文是“Agentic Autonomous Scientific Discovery”方向的核心新增文献，但它对我们的框架更准确的作用是：证明 agent 可以参与真实科学发现中的假设生成、排序、实验设计和早期验证，而不是证明科学全流程已经自动化。

在 Scientific Workflow 上，它覆盖 Knowledge Grounding、Hypothesis Generation、Experiment Design、Verification 和 Evolution，尤其强在 hypothesis generation 与 wet-lab validation 的连接。

在 Skill Lifecycle 上，它对应：

- Representation：研究目标、研究方案、Specific Aims、实验 proposal 可视为 workflow/protocol skill 的雏形。
- Acquisition：主要来自文献检索、科学辩论、专家输入和系统迭代。
- Retrieval：依赖 web search、文献探索、proximity graph 和 context memory。
- Composition：多个专门 agent 通过 Supervisor 和 tournament 组合。
- Evolution：通过 Elo tournament、Reflection、Evolution、Meta-review 持续改写和提升假设。
- Verification：包括专家审阅、GPQA、体外实验、肝类器官实验、安全红队测试。

Evidence Role 应标为 **Indirect + Boundary**。它不是一篇显式研究 skill library 的论文，但它提供了强烈的间接证据：科学发现 agent 的关键能力可以被组织成可生成、可批判、可排序、可演化、可验证的 procedure。同时它也给出边界：真实发现仍需要专家选择、湿实验资源、后续临床/机制验证和安全治理。

与 AI Scientist 相比，Co-Scientist 更强调人类科学家协作和真实生物医学验证；AI Scientist 更强调端到端生成机器学习论文。与 self-driving lab 文献相比，Co-Scientist 还没有形成自动实验闭环，实验执行仍由人类专家和实验室完成。

## 局限性

- 系统依赖开放文献和 web search，不能访问全部付费文献，也可能漏掉关键 prior work。
- 负结果和失败实验通常不发表，因此系统缺少专家经验中很重要的 negative evidence。
- LLM 的 factuality、hallucination、bias 可能被系统继承和放大。
- 现有系统主要处理文本；作者承认尚未充分利用论文图表、大型多组学数据集、知识图谱和专业数据库。
- Elo 是内部自动评价指标，可能偏好系统自身容易奖励的输出属性，不能完全代表科学家偏好或真实正确性。
- 专家评价规模较小，11 或 15 个研究目标不足以证明跨领域泛化。
- 湿实验验证主要是早期体外验证；AML 药物重定位结果不等于 in vivo 有效，也不等于临床成功。
- 系统当前没有设计完整临床试验方案，也没有充分处理药物递送、生物利用度、药代动力学、复杂药物相互作用和患者异质性。
- 安全评估仍是初步的；1200 个 adversarial goals 没有公开，外部无法复核其覆盖度。
- 论文明确要求持续 human expert oversight，最终科学决策仍由人类专家完成。

## 核心贡献

AI Co-Scientist 的核心贡献是把“文献驱动的假设生成”推进到多智能体辩论、Elo tournament 演化和真实生物医学湿实验初步验证的层面，展示了 scientist-in-the-loop agent 系统可以在药物重定位、靶点发现和机制解释中产生可检验的科学假设。

## 论证级补充

### 方法流程细化

1. **输入**：科学家给定研究目标、偏好、约束和评价标准，系统解析为 research plan configuration。
2. **生成**：Generation agent 根据文献和上下文提出多个候选假设。
3. **批判与排序**：Reflection agent 批判假设，Ranking agent 通过成对比较和 Elo tournament 排序。
4. **演化**：Evolution agent 对高排名假设进行综合、扩展、类比或简化，Meta-review agent 把跨轮反馈写回后续 prompt。
5. **人工选择与实验**：专家审阅 top hypotheses，并选择候选进入 AML、肝纤维化和 cf-PICI 等验证场景。
6. **反馈边界**：实验结果用于证明候选假设有 early biological plausibility，但不是自动湿实验闭环。

### 关键数字核对

| 指标 | 数值 | 可用于正文的说法 |
|---|---:|---|
| GPQA diamond top-1 accuracy | 78.4% | 内部 Elo 排名和科学推理表现相关，但 Elo 不是 ground truth |
| research goals for test-time scaling | 203 | 更多 test-time compute 与更高自动评价质量相关 |
| expert-curated hard biomedical goals | 15 | 专家目标上的表现支持 scientist-in-the-loop ideation |
| human preference evaluated goals | 11 | 专家偏好评估规模有限 |
| adversarial research goals | 1,200 | 安全红队测试有初步结果，但数据未公开 |
| drug repurposing search space | 2,300 drugs × 33 cancers | 系统可在大候选空间中提出可实验检验假设 |
| AML KIRA6 IC50 | 13 nM / 517 nM / 817 nM | novel candidate 有早期体外活性，不等于临床有效 |

### 可支撑的论点

- Hypothesis generation 可以被组织成 generate-critique-rank-evolve 的 agentic procedure。
- 科学假设 skill 需要专家偏好、文献 grounding、安全过滤和实验验证共同约束。
- Co-Scientist 是 scientist-in-the-loop discovery，而不是 fully autonomous science。

### 不能支撑的过度结论

- 不能说系统已经自动完成完整生物医学发现。
- 不能把 AML 和肝纤维化体外结果写成临床发现。
- 不能把 Elo 排名等同于科学真值。
- 不能说安全性已被充分外部审计，因为 adversarial goals 未公开。

### 与其他 anchor papers 的关系

- **互补 Robin**：Co-Scientist 更强在开放式假设辩论；Robin 更强在实验数据分析反馈到下一轮候选。
- **互补 CRISPR-GPT**：Co-Scientist 生成可检验假设；CRISPR-GPT 封装具体 gene-editing protocol skill。
- **对照 A-Lab / RoboChem-Flex**：Co-Scientist 没有机器人实验闭环，physical grounding 依赖外部人类实验室。
- **受 SPOT-a / SafeScientist 约束**：co-scientist 输出必须接受错误检测和风险审查。

### 框架映射

| 维度 | 标签 |
|---|---|
| Scientific Workflow | Knowledge Grounding; Hypothesis Generation; Experiment Design; Verification; Evolution |
| Skill Lifecycle | Acquisition / literature-derived; Composition / multi-agent; Evolution / reflection; Verification / human and wet-lab review |
| Evidence Role | Indirect; Boundary |
| Cross-cutting Constraints | Human Oversight; Auditability; limited Physical Grounding |
