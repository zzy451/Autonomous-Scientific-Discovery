# Agent Laboratory 2024

## 基本信息
- **论文**: Agent Laboratory: Using LLM Agents as Research Assistants
- **作者**: Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Michael Moor, Zicheng Liu, Emad Barsoum
- **年份**: 2024
- **来源**: arXiv:2501.04227
- **关键词**: autonomous-research, end-to-end-pipeline, human-in-the-loop, llm-benchmarking, agent-framework

## 核心思想
Agent Laboratory 是一个端到端的自主 LLM 研究框架，接受人类提供的研究想法，经文献综述、实验执行、报告撰写三个阶段自动产出研究论文和代码仓库。支持多种前沿 LLM 后端（o1-preview 在报告质量/有用性和 NeurIPS-style 总分上最好，o1-mini 实验质量最高），人类可在每阶段介入反馈。其 mle-solver 在 10 个 MLE-Bench 子集任务上获得的奖牌数和高于人类中位数次数均超过 MLAB/OpenHands/AIDE；gpt-4o 后端单篇成本 $2.33，较以往方法降 84%。

## 研究问题与动机
科研过程漫长昂贵，大量高质量想法因时间资源限制被搁置。现有 LLM 研究助理（ResearchAgent 自动 ideation + 迭代精炼、The AI Scientist 全自动论文生成+审稿）虽 novelty 较高，但 Si et al. (2024) 指出可行性/实施细节薄弱，Chakrabarty et al. (2024) 发现 LLM 降低创意多样性。Agent Laboratory 定位为辅助人类科学家执行其自身想法（非替代），让研究者专注于创意构思。系统为 "计算灵活" 设计——可根据 CPU/GPU/内存资源灵活分配算力。

## 方法细节
**5 种角色 Agent：PhD、Postdoc、ML Engineer、SW Engineer、Professor。**

**阶段一：文献综述**——PhD Agent 迭代执行：(1) summary：arXiv API 返回 top-20 摘要；(2) full_text：提取完整内容；(3) add_paper：纳入 curated review。多轮查询、评估相关性、精炼选择直到达 N_max。

**阶段二：实验执行**
- Plan Formulation：PhD+Postdoc 对话协作确定模型/数据集/步骤，Postdoc 提交 plan 指令
- Data Preparation：ML Engineer 用 `python` 命令和 `search_hf`（HuggingFace）准备数据，SW Engineer 经编译验证后提交，迭代至 bug-free
- Running Experiments（mle-solver 核心 5 步循环）：(A) Command Execution——从高分程序池采样，REPLACE（全新生成）或 EDIT（行级替换）修改；(B) Code Execution——编译检查，失败 max 3 次自动修复；(C) Program Scoring——LLM 奖励模型评分 0-1（类似 LLM reasoning tree search 但遍历程序空间而非推理步骤）；(D) Self-Reflection——无论成败生成反思文本；(E) Performance Stabilization——维护高分池 + 批量并行 N 修改选最优替换最低分，高熵采样平衡探索精炼
- Results Interpretation：PhD+Postdoc 讨论 mle-solver 结果，Postdoc 提交 interpretation

**阶段三：报告撰写**（paper-solver）——(A) 生成 8 标准章节 LaTeX 脚手架；(B) Arxiv 工具检索引用文献；(C) EDIT 命令逐行修改+编译验证；(D) 自动审稿评分（在 ICLR 2022 OpenReview 500 篇校准：人工准确率 65% vs 自动 66%，F1 0.49 vs 0.57）。3 审稿 Agent 模拟 NeurIPS 四维度评审（Originality/Quality/Clarity/Significance），PhD 决定定稿或回溯早期子任务重做。

**运行模式**：Autonomous（仅需初始想法，子任务依次执行） vs Co-pilot（每子任务后人类 checkpoint 审核，可提供反馈要求重新执行）。

## 关键结果
- **5 研究模板 × 3 后端 = 15 篇，10 位 PhD 评审（1-5 分制）**：
  gpt-4o：实验 2.6/5，报告 3.0/5，有用性 4.0/5
  o1-mini：实验 3.2/5（+0.6），报告 3.2/5（+0.2），有用性 4.3/5（+0.3）
  o1-preview：实验 2.9/5，报告 3.4/5（最高），有用性 4.4/5（最高）
- **主题差异极大**：词序主题报告最高 3.8/5，图像噪声 gpt-4o 1.5/5 vs o1-mini 4.0/5（差 2.5 分）
- **NeurIPS 风格评分**（人类评审，总分 10）：gpt-4o 3.5 → o1-mini 3.8 → o1-preview 4.0。NeurIPS 录取均线 5.9，尚未达标
- **自动审稿 vs 人类**：自动 6.1/10 vs 人类 3.8/10（自动高估约 +2.3），Clarity/Contribution 类似高估
- **Co-pilot > Autonomous**，参与者普遍愿意继续使用
- **成本**：gpt-4o $2.33/篇，较以往降 84%；10 个 MLE-Bench 子集任务中，mle-solver 获得 4 枚奖牌（2 金、1 银、1 铜），且 6/10 个任务超过人类中位数，高于 MLAB/OpenHands/AIDE

## 局限性
自主模式距顶会门槛仍有差距（4.0/10 vs 5.9/10）；自动审稿严重高估（+2.3）；不同主题性能差异巨大；仅 ML 领域验证；Agent 可能产生幻觉/错误引用；对人类反馈依赖未量化。

## 核心贡献
首个从人类想法到完整论文+代码的端到端自主科研流水线；o1-preview 在质量/有用性指标上最好，但最低成本口径来自 gpt-4o 单篇 $2.33（降 84%），质量距顶会仍有差距（4.0 vs 5.9）。
Pipeline：Human Idea → [Lit Review (PhD+arXiv iterative) → Experimentation (PhD+Postdoc plan → ML Engineer mle-solver: REPLACE/EDIT→compile→LLM score 0-1→reflect→stabilize) → Report Writing (paper-solver scaffold 8 sections → Arxiv cite → EDIT refine → 3-reviewer NeurIPS eval → PhD decide: revise/backtrack)] → Code Repo + Paper

## 与综述的关联
是目前最接近 "AI Agent 自主完成科学发现全流程" 的完整系统实现，为本综述提供核心案例。人机协作（Co-pilot）模式为 Agent 定位提供关键参照：Agent 做执行层，人类做创意+把关。84% 成本降低表明大规模部署可行性增强。mle-solver 的 "程序空间树搜索+LLM 自评分+反思+稳定化" 为自主实验设计提供可复用范式。自动审稿校准方法论（ICLR 2022 500 篇）也为综述评估提供参考。
