# GPT Researcher 2024

## 基本信息
- **论文**: GPT-Researcher
- **作者**: Assaf Elovic (assafelovic) + 社区贡献者
- **年份**: 2024 (持续更新)
- **来源**: https://github.com/assafelovic/gpt-researcher
- **关键词**: 自主研究, 多智能体, 网页爬取, 深度研究, 报告生成, 开源系统

## 核心思想
GPT-Researcher 是较早开源并持续维护的深度研究智能体（截至 2026-05-30 约 27.4k GitHub stars、3.7k forks，GitHub latest release 为 v3.4.4），支持对任意主题进行 Web 与本地文档的自主研究，生成带引用的长篇事实性报告。其核心理念源自 Plan-and-Solve 与 RAG 范式，通过并行化智能体工作流缓解现有 LLM 的信息滞后、token 限制与来源偏见问题。项目由 Assaf Elovic 发起，社区活跃，已被集成为 Claude Skill 与 MCP Server。

## 方法细节
- **Planner-Executor-Publisher 三阶段架构**：Planner 根据用户查询生成研究问题集合；Execution agents 并行爬取 20+ 网页源为每个问题收集信息；Publisher 过滤、聚合汇总，生成最终研究报告。完整流水线确保从问题分解到报告输出全自动化。
- **深度研究模式（Deep Research）**：采用树状递归探索策略，支持配置深度与广度。每个分支独立管理上下文，并发处理加速；官方 README 把 “Deep Research” 描述为在几分钟内产生可附引用的研究结果，使用 o3-mini/high 时成本约 $0.40。模拟人类研究员逐层深入的搜索行为，是区别于普通 RAG 系统的关键能力。
- **多智能体辅助（Multi-Agent Assistant）**：基于 LangGraph 与 AG2 框架构建专业化智能体团队，从规划到发表协同工作。受 STORM 论文启发，单次运行可生成 5-6 页多格式（PDF/Docx/Markdown）研究报告。
- **多源融合与本地文档研究**：聚合 20+ 来源减少偏见与错误信息；支持 PDF、CSV、Excel、Markdown、PPT、Word 等本地格式；JavaScript 渲染抓取动态页面；AI 内联图片生成（Gemini Nano Banana）。
- **MCP 双向集成**：既作为 MCP Client 连接 GitHub 仓库、数据库等专业数据源，又作为 MCP Server 使 Claude Desktop 等 AI 应用获得深度研究能力。

## 与 AI Scientist 的关键差异
GPT-Researcher 是信息综合与报告生成工具，非端到端科学发现系统。它不设计新算法、不做实验、不写学术论文——而是聚焦于"对已有知识的检索、聚合、总结"，其 Deep Research 模式扩展了搜索深度而非创造新知识。与之对比，AI Scientist（Sakana AI）与 AI-Researcher（HKUDS）覆盖从创意生成到实验验证再到论文撰写的完整科研闭环。

## 关键数字
- 约 27.4k GitHub stars、3.7k forks，GitHub latest release 为 v3.4.4
- 20+ 并行网页来源，报告可超 2,000 词
- Deep Research ~5 min/次，~$0.4/次（o3-mini high）
- 支持 PDF/DOCX/CSV/MD/PPT/XLSX 等本地格式
- 前端双版本：轻量 HTML/CSS/JS + 生产级 NextJS/Tailwind

## 核心贡献
GPT Researcher 2024 的核心贡献是提供一个可分析的 agentic research system 案例，展示科学工作流中某些能力如何被组织为可执行、可组合或可验证的流程。

## 与综述的关联
- 自主研究系统的重要开源代表，与 AI-Researcher、OpenScholar 形成"信息检索-知识综合-科学发现"能力谱系。
- Planner-Executor 架构是本综述多智能体研究范式的重要实例，其并行化设计为解决大规模文献调研的效率瓶颈提供了工程参考。
- MCP 集成展示了技能生态与技术工具的融合方向——研究智能体可通过标准化协议接入数据库、代码仓库等异构数据源。

## 局限性
- 核心能力边界在"信息综合"而非"知识创造"，不适合需要原创性科学假设生成或实验验证的场景。
- 报告质量高度依赖搜索源质量；对需要领域深度推理（如数学证明）的研究任务支持有限。
- 多智能体模式仍处实验阶段，生成的"论文级"报告在学术严谨性、同行评审适应性方面未经验证。
- 基于 LLM 的 Pipeline 存在固有的非确定性——同一查询多次执行可能产生不同结果，对可复现性要求高的科学研究场景不够可靠。
- 虽声称"减少偏见"（通过多源聚合），但信息源的偏见（如特定搜索引擎的排序偏见）仍可能渗透到最终报告中，偏见的消除无形式化保证。
