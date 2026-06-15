# Collaborative Memory 2025

## 基本信息
- **论文**: Collaborative Memory: Multi-User Memory Sharing in LLM Agents with Dynamic Access Control
- **作者**: Alireza Rezazadeh, Zichao Li, Ange Lou, Yuying Zhao, Wei Wei, Yujia Bao
- **年份**: 2025
- **来源**: arXiv:2505.18279
- **关键词**: memory, multi-agent, access-control, collaboration, knowledge-sharing, provenance

## 核心思想
复杂任务日益委托给专业 LLM Agent 集成体，这些 Agent 相互推理、沟通和协调，同时与外部工具、API 和数据库交互。持久化记忆虽已证明能提升单 Agent 性能，大多数方法假设单用户单 Agent 范式——忽略了多用户间动态、非对称权限下的知识传递需求与挑战。本文提出 Collaborative Memory 框架，面向多用户多 Agent 环境，将非对称时变访问控制编码为连接用户、Agent 和资源的二分图。双层记忆：(1) 私有记忆仅对创建用户可见；(2) 共享记忆选择性跨用户共享。每条记忆片段携带不可变溯源属性（贡献 Agent、访问资源和时间戳），支持追溯权限检查。细粒度读策略按当前用户-Agent-资源约束投影过滤视图；写策略通过上下文感知转换管理保留与共享。实现安全、高效、可解释的跨用户知识共享，具有可证明的非对称时变策略遵守性和完整的记忆操作可审计性。

## 研究问题与动机
现有记忆系统（MemGPT/MemTree/GraphRAG/HippoRAG）均假设单用户单 Agent、全局可见记忆。但在真实多用户多 Agent 场景（企业协作助手、多用户生产力平台、分布式工作流系统）中存在两个核心挑战：(1) 信息非对称——不同用户访问不同 Agent，不同 Agent 连接不同资源（工具/API/知识库），必须防止未经授权的信息泄露；(2) 动态访问模式——权限随时间变化（角色变更、入职/离职、政策调整），系统必须在权限变更后即时调整可访问的信息范围。核心问题：如何在不违反访问约束的前提下最大化集体记忆的效用？本文从分布式认知理论（Distributed Cognition, Hutchins 1995）出发，将多 Agent 系统视为统一认知实体，强调跨主体知识传递必须受权限约束且可追溯审计。

## 方法细节
### 动态二分图建模
每个时间步 t 的访问权限由两个二分图捕获——G_UA(t) ⊆ U × A（用户→Agent 可调用关系）和 G_AR(t) ⊆ A × R（Agent→资源可访问关系）。图随时间演化以反映用户增删、角色变更和资源权限调整。由此推导出 A(u,t) = {a | (u,a) ∈ G_UA(t)} 即 u 在 t 时刻可调用的 Agent 集合，以及 R(a,t) = {r | (a,r) ∈ G_AR(t)} 即 a 在 t 时刻可访问的资源集合。

### 双层记忆与不可变溯源
M = M_private ∪ M_shared，每片段 m 携带不可变溯源属性：
- T(m)：创建时间 | U(m)：贡献用户 | A(m)：贡献 Agent 集合 | R(m)：创建时访问的资源集合
Agent a 服务用户 u 时可访问的完整记忆集：M(u,a,t) = {m | A(m) ⊆ A(u,t) ∧ R(m) ⊆ R(a,t)}
此公式自动包含三类子集：(i) u 历史中与其他可用 Agent 的交互记录；(ii) Agent a 为其他用户创建的记忆片段；(iii) 其他用户通过 u 可调用的 Agent 所创建的片段。通过 Agent 级和资源级约束叠加，即使允许跨用户共享，也确保不泄露超出权限的信息。

### 细粒度读写策略
Read Policy Π_read：将 M(u,a,t) 投影为过滤/转换后的视图（可限制片段数量、关键词过滤、匿名化或改写），配置粒度为 {全局共享、按用户、按 Agent、随时间变化} 四维度。
Write Policy 分 Π_write/private 和 Π_write/shared 两路——可执行实体匿名化、敏感信息脱敏、内容审核等上下文感知转换。从直接 embedding 存储到接入 MemTree 等复杂记忆结构均可兼容。实验提供两种实例化：Simple（读不修改+写不修改）和 Transformation（LLM 在读写前后做脱敏/匿名/改写——实验采用 Transformation 写 + Simple 读的组合）。

### 实现全栈
全 gpt-4o + text-embedding-3-large。Coordinator 接收 (i) 用户查询、(ii) 各 Agent 专长字符串、(iii) 对话历史，输出 JSON `{"agent":ID,"subquery":...}` 或 `{"stop":true}`。Domain Agents 通过 OpenAI function-calling 调用 Python callable 资源（如知识库搜索 query→top_k_results）。Memory Encoder 将对话轨迹映射为 LLM 生成的 key-value 片段并标注溯源。Memory Retrieval：余弦相似度取 top-k_user（用户私有层）+ top-k_cross（满足溯源约束的跨用户层）。Response Aggregator 接收 (subquery, response) 列表合成最终答案。

### 评估指标
三个指标：Accuracy（LLM-judge 评估回答与 ground truth 的一致性，0-1 归一化）、Agent Utilization（每查询平均调用的不同 Agent 数量，反映协调开销）、Resource Utilization（每查询平均知识库/API 调用次数，代理系统效率）。

## 关键结果
- **Scenario 1（完全协作）**——MultiHop-RAG 数据集：609 篇新闻跨 6 领域（科技/娱乐/体育/科学/商业/健康）、2556 个多跳问题（需要推理/比较/时间推理）、6 个领域专家 Agent（各独占一个 KB）、5 用户全权限。KMeans 10 簇聚类模拟真实多用户查询重叠。协作记忆准确率维持 > 0.90（隔离记忆略低）。资源利用率：50% 查询重叠率下降低高达 61%，75% 重叠率下降低 59%（相比隔离记忆配置）。
- **Scenario 2（非对称协作）**——200 个合成商业项目查询（从 "Identify high-demand skincare markets in Europe" 到 "Craft a strategic growth plan for smart home devices in privacy-regulated markets"）、4 种用户角色（Market Researcher/Financial Analyst/Logistics Lead/Strategy Director）、4 专业 Agent（各自独占市场 DB/财务预测/物流对比器/战略计算资源），仅 Strategy Director 可访问全部 Agent。即使部分权限共享，各角色资源调用次数均显著低于完全隔离配置。Strategy Director 汇总时大量冗余已被消除。
- **Scenario 3（动态演化）**——SciQAG 科学问答数据集：5 科学领域（化学分析/能源燃料/陶瓷材料/纸木材料/物理数学）、5 RAG Agent（各覆盖一个领域语料）、5 用户（每用户 4 查询/领域，共 100 查询）、9 个时间点 t₀-t₈（每个时间点 100 查询）。t₀ 从 5 条用户-Agent 边的稀疏图开始，t₁ 至 t₄ 逐步授予边（Bernoulli trials，边数增至 10/15/20/25）→ t₅ 至 t₈ 逐步撤销边（降至 20/15/10/5）。准确率随权限授予上升、随撤销下降（展示强耦合）。平均查询资源数随时间推移下降——记忆机制复用已检索信息的直接证据。访问矩阵验证严格权限遵守——用户仅访问二分图显式授权的 Agent 和资源，黄色矩形标记允许访问区域，数值表示实际调用次数。

## 局限性
实验依赖现有基准（MultiHop-RAG/SciQAG）和合成查询，尚缺乏专用多用户协作记忆基准。
尚未在真实企业级多用户场景中验证（受监管和隐私障碍限制）；当前环境用户和 Agent 数量可控（5 用户/5-6 Agent），大规模高并发场景（角色频繁变更、海量并发请求）未探索；LLM 随机性可能导致偶发幻觉或策略违反，尽管有 enforcement 机制；实际生产环境 API 延迟波动 5-30 分钟，仅以资源调用次数为效率代理指标；未与 RBAC/ABAC 等成熟工业安全框架进行深度集成和对比评估；Transformation 写策略的脱敏/匿名化质量未量化。
此外，协同记忆的冷启动问题（新用户无历史记忆时如何快速融入协作）未被研究。

## 核心贡献
首个在 LLM Agent 记忆系统中显式建模多用户/非对称/时变访问控制的框架，资源利用率降低高达 61%，具备可证明策略遵守性和完整审计能力。
Pipeline：User Query → Coordinator (assign subqueries per G_UA(t)) → [Per Agent a: Read (Π_read filters M(u,a,t) = {m | A(m) ⊆ A(u,t) ∧ R(m) ⊆ R(a,t)} by provenance & current permissions) → Generate (a(query, filtered_memory, R(a,t))) → Write (Π_write/private + Π_write/shared with context-aware transformations)] → Aggregator (synthesize from all agent outputs) → Final Response + Immutable Audit Trail

## 与综述的关联
科学发现日益依赖多研究者、多 Agent 协作——跨实验室的数据共享、联合实验、文献协同分析等场景中，如何在保护知识产权和隐私的同时实现高效知识共享是关键难题。Collaborative Memory 为此提供了形式化框架：二分图访问控制 + 不可变溯源 + 独立读写策略。它与 MemGPT（单 Agent 内存管理和上下文扩展）和 Generative Agents（反思式记忆与知识提炼）共同构成本综述记忆维度的三个支柱，分别覆盖"如何扩展上下文容量"、"如何从记忆中提炼知识"、"如何在多主体间安全共享知识"三个递进层次。在科学发现的多实验室、多角色协作场景中，该框架可确保实验数据、假设验证和最终结论在正确权限约束下流动，为构建安全可信的多人协作科学发现 Agent 系统提供了关键基础设施。
