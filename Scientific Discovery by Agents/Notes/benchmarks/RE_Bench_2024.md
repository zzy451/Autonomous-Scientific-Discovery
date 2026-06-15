# RE Bench 2024

## 基本信息
- **论文**: RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts
- **作者**: Hjalmar Wijk, Tao Lin, Joel Becker, Sami Jawhar, Neev Parikh, Thomas Broadley, Lawrence Chan, Michael Chen, Josh Clymer, Jai Dhyani, Elena Ericheva, Katharyn Garcia, Brian Goodrich, Nikola Jurkovic, Holden Karnofsky, Megan Kinniment, Aron Lajko, Seraphina Nix, Lucas Sato, William Saunders, Maksym Taran, Ben West, Elizabeth Barnes
- **年份**: 2024
- **来源**: arXiv:2411.15114
- **关键词**: benchmark, ML R&D, human baseline, frontier AI, Triton kernel, AI safety

## 核心思想
该文提出 RE-Bench（Research Engineering Benchmark V1），包含 7 个开放式的 ML 研究工程环境，并收集了 61 位人类专家在 8 小时内完成的 71 次尝试数据。在每环境 2 小时的条件下，最佳 AI 智能体得分比人类专家高 4 倍；但在 8 小时总时长条件下，人类以微弱优势超越 AI；在 32 小时的总尝试聚合下，人类得分达到 AI 的 2 倍。定性发现：现代 AI 智能体在诸多 ML 课题上展现出显著专长——例如某智能体写出了比所有人类专家更快的 Triton 核函数。AI 生成和测试方案的速度是人类十倍以上，成本远低于人类。所有环境、人类数据、分析代码和智能体轨迹均已开源。

## 评测目标
评测前沿 AI 智能体在开放式 ML 研究工程（AI R&D）任务上的真实能力，直接对标人类专家以评估 AI R&D 自动化风险。这是 AI 安全治理的关键需求——多个 AI 开发者和政府将"AI 自动化 AI 研究"列为需要预警的关键能力。现有基准的不足：(1) MLE-bench 等将人类 Kaggle 成绩与 AI 在不同条件下对比，条件不等价；(2) GPQA、SciCode 等无人类基线或仅短期人类数据；(3) 缺少在同一受控环境下 AI 智能体与人类专家直接对比的数据。RE-Bench 核心创新在于提供了这种等价条件下的人机对比。

## 基准设计
- **题目数量/来源/难度分级**：7 个手工设计的开放式 ML 研究工程环境：(1) Optimize LLM Foundry（优化微调脚本运行时间）、(2) Optimize a Kernel（为 GPU 前缀和写 Triton 内核）、(3) Fix Embedding（修复被破坏的词嵌入矩阵）、(4) Scaling Law Experiment（在小规模实验中预测最优架构-训练步骤权衡）、(5) Restricted Architecture MLM（用有限 PyTorch 原语构建掩码语言模型）、(6) Finetune GPT-2 for QA（微调小模型为聊天机器人）、(7) Scaffolding for Rust Codecontests（为 GPT-3.5 构建 Rust 竞赛编程脚手架）。覆盖预训练、后训练、脚手架、性能工程、调试等 AI R&D 子领域。
- **评分方式**：每个环境定义评分函数和起始方案（得分 = 0）与参考方案（得分 = 1），通过线性归一化使跨任务可比。允许智能体随时运行评分函数获取反馈（Scaling Law Experiment 除外，需保持实验外推性）。评估基于运行期间最高得分。
- **人类基线 vs AI 基线**：61 位人类专家（来自 METR 职业网络 43 人、招聘流程 11 人、研究生外展 7 人）在等价条件下完成 71 次 8h 尝试。82% 的尝试获得非零分数，24% 达到或超过参考方案。专家来源差异大：职业网络均分 0.96，招聘申请者均分 0.46。AI 2h 预算下可得分数为人类 4x，但 8h 人类微弱领先，32h 总预算人类达 AI 2x。最佳 AI 配置（o1-preview + AIDE 或 Claude 3.5 Sonnet + Modular）匹配人类第 36-37 百分位。
- **设计原则**：(i) 可行性——70%+ 人类专家可在 8h 内取得进展；(ii) 生态效度——与真实 AI R&D 高度相关，环境设计对齐 Epoch AI 的 AI R&D 自动化技能分类；(iii) 抗饱和——环境有高天花板，顶尖人类分数之上仍有 >15% 提升空间；(iv) 覆盖多样性——不同反馈周期长度（40s ~ 2.5h）、代码量（218 ~ 1392 行）和创新性各异。

## 关键数字
| 指标 | 值 |
|------|-----|
| 任务环境数 | 7 |
| 人类专家数 | 61（71 次 8h 尝试）|
| 人类非零分比例 | 82% |
| 人类达到/超过参考方案比例 | 24% |
| AI 2h 预算 vs 人类 2h | AI 约 4x 高于人类 |
| 人类 8h vs AI 8h | 人类微弱领先 |
| 人类 32h 聚合 vs AI 32h 聚合 | 人类约 2x 于 AI |
| AI 最佳百分位匹配 | 人类第 36-37 百分位 |
| AI 速度优势 | 生成和测试方案约 10x 快于人类 |
| 人类/AI 可用 GPU | 0-6 × H100（按任务而异）|
| AI 评估采样 | 16h 总预算下 Claude 3.5 Sonnet + Modular: 30min@32；o1-preview + AIDE: 2h@8 |
| 丢弃的规格数 | >12（至少 5 个已完成实现因质量不达标被弃）|

## 设计哲学
- **等价条件人机对比**：这是 RE-Bench 最核心的哲学——人类和 AI 使用完全相同的虚拟机、时间预算、GPU 资源。由此建立了直接逻辑链：如果 AI 在相同条件下显著弱于人类专家，则不可能以经济有效的方式自动化这些专家的研究工作。
- **时间扩展曲线而非单点对比**：通过多时间预算（30min / 2h / 8h / 32h 聚合）、多采样策略（k 次短运行 vs 单次长运行），揭示 AI 和人类有本质不同的时间扩展特征——AI 初期快但不持续进步，人类慢启动但持续加速。这种多维度对比远超传统 pass@k 评估。
- **"天花板高 + 可进展"双重验证**：确保环境同时满足两个条件——人类 8h 内可稳定取得进展（避免操作困难），且评分天花板远高于顶级人类（避免饱和）。创建过程中丢弃了大量不达标的规格和完整实现。
- **安全治理导向**：明确将 RE-Bench 定位为"早期预警评估"，为 AI 研发者提供安全缓冲——在模型真正能自动化 AI R&D 之前就捕捉到接近信号。

## 局限性
- 仅 7 个环境，覆盖面有限。缺少：组织分布式训练、设定研究方向、创建数据集、硬件问题调查、技术架构设计、有挑战的数学/理论工作、重叠/模糊约束的目标定义、大规模工程复杂性。
- 人类专家群体来源不均（职业网络专家平均分远高于招聘申请者），自选参与可能导致选择偏差，不宜仅对比人类均值。
- Finetune GPT-2 for QA 环境得分离散度大（起始方案方差大），评估信噪比受影响。
- 主要评估产出结果而非研究过程的洞察质量。
- 2h 条件下的对比可能低估人类的规划能力（人类在长时程更优），短期评估可能给出过度乐观的 AI 进展图景。
- 成本维度未充分优化——AI token 成本远低于人类劳动力，暗示通过更多 token 预算和更优脚手架可进一步提升 AI 表现。

## 核心贡献
RE Bench 2024 的核心贡献是构造 7 个开放式 ML research engineering 环境，并在完全等价的计算环境和时间预算下收集人类专家基线，使 frontier AI agent 的 AI R&D 自动化能力可以与真实专家在短时、长时和 best-of-k 设置下直接比较。

## 与综述的关联
RE-Bench 是评估 AI 智能体在 ML 研究工程领域最具人本主义色彩的基准——其核心贡献在于大规模收集了人类专家在完全相同任务上的受控数据，使人机对比不再是印象式的。在本综述 benchmark 章节中，它与 MLE-Bench 形成"工程 vs 研究"的轴：MLE-Bench 侧重竞赛式 ML 工程，RE-Bench 侧重开放式研究探索。同时，RE-Bench 与 ScienceAgentBench 形成"ML 研究 vs 跨学科科学"的互补——前者聚焦 ML 领域内的 R&D，后者横跨多个科学学科。其 AI 安全治理导向也是该基准的独特价值。
