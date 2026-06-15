# AI Researcher HKU 2025

## 基本信息
- **论文**: AI-Researcher: Autonomous Scientific Innovation
- **作者**: Jiabin Tang, Lianghao Xia, Zhonghang Li, Chao Huang (HKUDS, 香港大学)
- **年份**: 2025
- **来源**: https://github.com/HKUDS/AI-Researcher; arXiv: 2505.18705
- **关键词**: 自主科学发现, 端到端研究, 文献综述, 算法设计, 论文生成, 多智能体

## 核心思想
AI-Researcher 是香港大学 HKUDS 团队开发的端到端自主科学研究自动化系统。该系统覆盖从文献综述到论文撰写的完整研究生命周期，旨在"重塑传统研究范式"——从概念到发表全自动化。用户仅需提供参考文献列表或详细研究思路，系统即可自主完成创意生成、算法实现、实验验证与学术手稿撰写。

## 方法细节
- **三阶段全流程自动化**：
  (1) 文献综述与创意生成——Resource Collector 从 arXiv、IEEE Xplore、ACM DL、GitHub 等多源自动收集论文与代码，Resource Filter 按引用量、代码维护状态等维度筛选高质量资源，Idea Generator 分析现有方法局限、识别新兴趋势、提出新颖研究方向。
  (2) 算法设计、实现与验证——在 Docker 容器化环境中执行"设计-实现-验证-精化"迭代循环。设计阶段确立理论基础；实现阶段产出功能模块；验证阶段开展系统实验收集指标；精化阶段识别性能瓶颈并迭代优化。
  (3) 论文撰写——Writer Agent 采用分层写作方法，整合研究动机、算法框架与实验验证结果，自动生成完整学术手稿。
- **双智能体架构**：research_agent 处理创意生成与实验验证（支持 GPU Docker 环境），paper_agent 负责论文生成。通过 LiteLLM 支持 Claude、OpenAI、DeepSeek 等多模型后端。
- **双输入模式**：Level 1——用户提供详细研究思路，系统据此设计实现；Level 2——用户仅提交参考文献，系统自动分析提出创新概念并实现。后者降低了对用户领域专长的要求。
- **多维评估基准**：覆盖 CV、NLP、数据挖掘、信息检索四领域，以人类专家论文为 Ground Truth，从新颖性、实验全面性、理论基础、结果分析、写作质量五个维度评估。

## 关键结果
- arXiv 版本提出 Scientist-Bench，覆盖 Diffusion Models、Vector Quantization、Graph Neural Networks、Recommendation Systems 四类 AI 研究任务，而不是泛称 CV/NLP/DM/IR。
- Scientist-Bench 含 22 篇 2022-2024 年发表论文构造的任务；主评估使用 5 篇 ground-truth 论文进行自动生成论文与人类论文的比较。
- 提供 7 个完整示例（VQ、GNN、推荐系统、扩散模型等），每个示例包含全自动生成的论文 PDF + 代码工作区
- 支持 Gradio Web GUI，生产版上线 novix.science/chat
- 多 LLM 提供商支持（Claude, OpenAI, DeepSeek 等）

## 核心贡献
AI Researcher HKU 2025 的核心贡献是提供一个可分析的 agentic research system 案例，展示科学工作流中某些能力如何被组织为可执行、可组合或可验证的流程。

## 与综述的关联
- 端到端科学发现智能体的代表性工作，直接对应本综述"Scientific Discovery by Agents"核心主题——从"辅助检索"到"自主创造"的范式跃迁。
- 其三阶段流水线（综述-实验-写作）为理解科学发现智能体的功能边界提供了架构蓝图。
- 与 GPT-Researcher（信息综合）、OpenScholar（文献检索验证）、AI Scientist（Sakana）共同构成研究自动化的能力谱系。

## 局限性
- 论文级成果的学术质量尚未经过独立同行评审验证——系统自动生成的论文可能包含幻觉引用、不严谨推理或对已有工作的非故意抄袭。
- 当前示例集中在 CV/ML 等计算密集型领域（向量量化、图神经网络、推荐系统、扩散模型），向实验科学（生物、化学、物理）扩展需解决物理实验自动化、湿实验室操作的根本性挑战。
- 完整的论文原文（arXiv: 2505.18705）需下载阅读以获取每个领域的详细实验结果与人类评估数据。
- 系统在 Level 2 模式（仅给参考文献）下的创意质量与原创性尚未与人类研究者进行大规模盲法比较——"看起来合理"与"真正新颖"之间存在重要差距。
- 系统的评估指标（新颖性、实验全面性、理论基础、结果分析、写作质量）依赖 Evaluator Agent 自动评分，这些 AI 评估器的校准信度与人类专家的一致性尚未在论文中独立验证。
