# MIRIX 2025

## 基本信息
- **论文**: MIRIX: Multi-Agent Memory System for LLM-Based Agents
- **作者**: Yu Wang, Xi Chen
- **年份**: 2025
- **来源**: arXiv:2507.07957
- **关键词**: memory

## 核心思想
提出 MIRIX，一个模块化多智能体记忆系统，旨在解决"让语言模型真正记住"这一核心挑战。系统包含六种精心设计的记忆类型——Core Memory、Episodic Memory、Semantic Memory、Procedural Memory、Resource Memory 和 Knowledge Vault——由多智能体架构（6 个 Memory Manager + Meta Memory Manager + Chat Agent = 8 个 Agent）协调动态更新和检索控制。在 ScreenshotVQA（多模态，每序列近 20,000 张高分辨率截图）上比 RAG 基线准确率提升 35%、存储需求降低 99.9%；在 LOCOMO（长文本对话）上以 85.4% 达到 SOTA。配套发布跨平台个人助手应用，支持实时屏幕监控、个性化记忆构建和可视化。

## 研究问题与动机
现有 Agent 记忆系统面临三大瓶颈：(1) **缺乏组合式记忆结构**：大多数方案将所有历史数据存放在单一扁平存储中，不做类型路由（程序性 vs 情景性 vs 语义性），导致检索低效且不准——你无法用同一方式查找"如何安装软件"和"上周三午饭吃了什么"。(2) **多模态支持差**：文本中心记忆机制在非语言输入（截图、界面布局、地图）占主导时完全失效。(3) **扩展性与抽象不足**：直接存储原始输入（尤其是图像）导致存储需求爆炸性增长，且缺乏有效抽象层来总结和保留关键信息。根本痛点：人类记忆是多类型、多模态、层次化的，但 Agent 记忆系统仍然是扁平、单模态、非层次化的。

## 方法细节
**六种记忆类型（层次化内部结构）**：
- **Core Memory**：高优先级持久信息，分 persona block（Agent 身份/语调）和 human block（用户姓名、偏好等），容量达 90% 触发受控重写压缩。
- **Episodic Memory**：带时间戳的事件日志，字段包括 event_type、summary、details、actor、timestamp。支持时间索引和行为追踪。
- **Semantic Memory**：独立于时间的抽象知识（概念、实体、关系），字段包括 name、summary、details、source。以树状层级结构组织（如 Favorites > Sports/Pets/Music）。
- **Procedural Memory**：结构化操作流程（workflow/guide/script 类型），字段包括 entry_type、description、steps（可为 JSON 或其他结构化步骤列表）。
- **Resource Memory**：文档/文件/多模态资源存储，字段包括 title、summary、resource_type（doc/markdown/pdf_text/image/voice_transcript）、content。支持上下文连续性。
- **Knowledge Vault**：敏感信息的安全存储（凭证、地址、API key），按 sensitivity 级别（low/medium/high）分级访问控制，高敏感条目排除在常规检索之外。

**多智能体协调架构（8 Agent）**：Meta Memory Manager 负责分析输入内容、决定路由到哪些 Memory Manager；6 个 Memory Manager 并行更新各自记忆类型；Chat Agent 管理自然语言交互。Memory Update 流程：用户输入 → 记忆库自动搜索 → Meta Memory Manager 分析 → 路由到相关 Memory Managers 并行更新 → 返回确认。检索流程：用户查询 → Active Retrieval（Agent 先生成 topic → topic 检索 6 个记忆组件各 top-10 → 带来源标签注入 system prompt）→ Chat Agent 综合分析 → 生成回复。支持 multiple retrieval functions（embedding_match、bm25_match、string_match），Agent 根据上下文选择最合适的方式。

**应用层面**：React-Electron 跨平台应用，每 1.5 秒截图一次，视觉相似度 > 0.99 去重。每累积 20 张独特截图（约 60 秒）触发记忆更新。利用 Gemini API 的 Google Cloud URL 加载图片，端到端延迟从 GPT-4 的 ~50 秒降至 < 5 秒。

## 关键结果
- **ScreenshotVQA**：11+21+55=87 问题，3 名 PhD 学生，5,000-20,000 张截图。MIRIX 总体准确率 59.5% vs SigLIP@50 44.1%（+35%），vs Gemini long-context 11.7%（+410%）。存储：MIRIX 15.89MB vs SigLIP 15.07GB（99.9% 降低），vs Gemini 236.70MB（93.3% 降低）。
- **LOCOMO**（10 个对话，每对话 600 轮、26K tokens 平均，~200 问题/对话）：MIRIX 总体 85.38%，超过最强开源基线 LangMem 78.05%（+8.3 点），超过 Zep 79.09%（+6.3 点）。Multi-Hop 类别：MIRIX 83.70% vs Zep 69.16%（+24.5 点），远超所有基线。对比 Full-Context 上界 87.52%，MIRIX 在 Multi-Hop 上反超（83.70% vs 77.70%），因为 MIRIX 在记忆阶段已显式合并事件（如"Caroline 4 年前从家乡瑞典搬家"），避免了 Full-Context 需要多步推理拼接。
- **关键分析**：Single-Hop 的微弱差距（MIRIX 85.11% vs Full-Context 88.53%；Temporal 为 88.39% vs 92.70%）部分源于数据集歧义问题——"Melanie 什么时候露营？"在对话中既有计划时间（五月说下月 = 六月）也有实际发生时间（十月提及），MIRIX 优先存储确认事件导致与期望答案偏离。
- **效率**：Gemini backbone（gemini-2.5-flash-preview-04-17），Google Cloud 异步上传/检索；GPT-4.1-mini 用于 LOCOMO（函数调用能力强，Multi-turn ACC 29.75 vs GPT-4o-mini 22.12）。

## 局限性
- 六种记忆类型在复杂科学场景中边界可能模糊——"实验步骤"既是 Procedural 也是 Episodic，"文献综述"既是 Resource 也是 Semantic。
- 多 Agent 协调（8 Agent × 多轮 LLM 调用）的推理开销未量化——虽报告了延迟降低但总计算成本未系统分析。
- 仅评估了截图和文本模态，未覆盖结构化数据（表格、JSON）、数值数据（传感器读数）、音频——这些在科学发现中极为常见。
- Active Retrieval 的 topic 生成质量直接影响检索精度——topic 生成错误可能导致级联检索失败，对此缺乏鲁棒性分析。
- Agent Memory Marketplace 和可穿戴设备场景（第 2 节）与核心实验贡献关联较松散。

## 核心贡献
**一句话**：MIRIX 用 6 种专门化记忆类型 × 8 个协调 Agent 实现了多模态、层次化、SOTA 的 Agent 记忆系统——在 20K 截图问答上比 RAG 准 35% 且省 99.9% 存储，在长对话上达到 85.4% 总体准确。
**Pipeline 速记**：多模态输入（截图/文本）→ 去重 → 累积批次触发 → Meta Memory Manager 分析路由 → 6 个 Memory Managers 并行更新各自记忆类型（带层次化字段）→ 用户查询 → Active Retrieval（生成 topic → 并行检索 6 记忆各 top-10 → 带来源标签注入 prompt）→ Chat Agent 综合生成回复。

## 与综述的关联
科学发现涉及高度异质的信息类型——实验方案（Procedural）、观察记录（Episodic）、文献知识与概念关系（Semantic）、数据集和图表（Resource）、敏感凭证或受控资源信息（Knowledge Vault）——MIRIX 的六类型记忆架构为科学发现 Agent 提供了最直接的知识组织蓝图。其多模态能力（原生处理截图）对于自动化实验监控、仪器读数捕获等场景具有直接应用价值。Active Retrieval 的"先推断主题再检索"策略对科学发现中"从模糊问题到精确检索"的泛化需求也特别契合。但 MIRIX 缺乏研究领域特定的记忆 schema（如实验条件、p 值、置信度等科学元数据字段），需要领域适配才能充分发挥作用。
