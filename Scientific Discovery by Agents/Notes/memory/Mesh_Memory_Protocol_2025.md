# Mesh Memory Protocol 2026

## 基本信息
- **论文**: Mesh Memory Protocol: Semantic Infrastructure for Multi-Agent LLM Systems
- **作者**: Hongwei Xu
- **年份**: 2026
- **来源**: arXiv:2604.19540
- **关键词**: memory

## 核心思想
提出 Mesh Memory Protocol（MMP），面向多 LLM Agent 跨会话、长时间认知协作的语义基础设施协议。识别"跨会话 Agent 间认知协作"这一新型交互模式——Agent 团队在数天/数周的数据生成冲刺、迭代产品评审中持续协作。协议解决三个核心问题：P1-每个 Agent 按字段选择性接受同伴贡献而非全盘接受；P2-每条主张可追溯至来源，使返回的主张能被识别为接收方自身先前推理的回声；P3-跨会话重启后存活的记忆因其存储方式（写入时过滤）而非检索方式而具有相关性。定义四个可组合原语：CAT7（七字段认知记忆块固定模式）、SVAF（按字段对照接收者角色索引锚点评估）、Agent 间谱系（内容哈希 DAG 追踪）、remix（仅存储接收者经角色评估的理解，永不存储原始同伴信号）。已发布规范（CC BY 4.0），并报告三种参考部署/第一方运营观察。

## 研究问题与动机
Cemri et al. (2025) 从 1,600+ 多 Agent 轨迹中编目 14 种系统化失败模式，分布在系统设计缺陷、Agent 间失准、任务验证三类。Riedl (2025) 表明 prompt 级干预可在单会话内引导协作，但无法跨会话扩展。现有协议栈（MCP、A2A）解决工具访问和任务路由，AutoGen/MetaGPT 解决任务级编排——但都未解决语义层问题：当多个并行 Agent 必须共同演化认知状态时，如何在字段粒度上同意或不同意彼此的贡献？如何追踪返回的声明来自哪里？如何从"按角色评估后过滤"的记忆中恢复而非从原始信号重放？这三个问题对消息传递透明、对编排不可见、在模型层结构上不可达。

## 方法细节
MMP 为 8 层协议（L0-L7），本文贡献聚焦 L3-L4 的四个语义基础设施原语：

**CAT7（L3 记忆层）**：每条认知记忆块（CMB）由 7 个固定类型字段组成——focus、issue、intent、motivation、commitment、perspective、mood。CMB = (H, B)，H 为 7 字段 header（每字段含文本 tf + 单位归一化嵌入 vf ∈ R^d；Listing 1 的线框示例为 32 维），B 为可选任务特定 body（⊥ 为常见情况）。mood 字段额外携带 (valence, arousal) ∈ [-1,1]^2 情感坐标。7 字段跨所有领域固定不变，领域语义体现在字段文本中而非字段名——以 schema 灵活性换取通用互操作性。

**SVAF（L4 耦合层）**：Symbolic-Vector Attention Fusion，对每个 CMB 的 7 个字段计算余弦距离 δf = 1 - cos(ˆvf, v_new)，融合锚点 ˆvf 由角色权重 αf、相似度、时间衰减 e^(-λ(t-τj))、置信度 Cj 加权。闭式默认阈值将信号分为 redundant（max δf < 0.10）、aligned（δtotal ≤ 0.25）、guarded（δtotal ≤ 0.50）、rejected（otherwise）；神经 gate 变体可像 Listing 1 那样准入高新颖性、低 gate value 的信号，而非简单按 drift 阈值过滤。不同接收者因 αf 不同而对同一 CMB 产生不同准入判定——实现协议层角色专业化。在 237K 样本上训练，三分类准确率 78.7%。mood 字段经无监督训练发现为最高权重字段。

**谱系（Lineage）**：每条 remix CMB 携带 parents 和 ancestors 的 DAG 链接。回声检测实现为 ancestors(cin) ∩ Kself ≠ ∅ 的 O(1) 哈希集合操作。无活后代节点的 CMB 过期，有活后代的 ancestors 受保护——基于证明价值而非年龄的自我剪枝。

**Remix**：写入时过滤不变式——∀c ∈ Mi: c = remix(cin, i) with κ(cin, i) ∈ {aligned, guarded}。接收者的记忆存储仅包含自己的 remix，从不存储原始同伴信号。跨会话重启时恢复的是经角色评估的理解，而非原始转录。这与 RAG/checkpoint 等读取时过滤形成范畴性反转。

四个原语双重集成：垂直（将记忆提升为认知，写入从被动追加变为评估性行为）和水平（跨 Agent 跨会话携带已评估认知状态）。

## 关键结果
- **Table 1 审计**：对 8 种现有记忆基板（MemGPT、Mem0、A-MEM、AWM、Reflexion、CoALA、Voyager、Collaborative Memory）进行 P1/P2/P3 + 多 Agent 优先支持审计。联合交集 P1+P2+P3+Multi-agent 在所有 8 种基板中均为空白——Collaborative Memory 最接近但准入是访问控制粒度而非接收者角色语义评估。
- **Listing 1 真实跨平台 CMB**：2026-04-20 Mac↔Windows mesh 采集的 CMB，SVAF 神经评估结果：6 个内容字段 drift 在 0.84-0.99（高新颖性），对应的 gate values 0.0003-0.0009（低门值 = 通过准入），mood drift 0.0899（gate 0.1785）。展示了带通准入机制而非简单阈值。
- **三种参考部署/证据**：sym-mesh-channel（Claude Code plugin）通过 Anthropic Claude Plugin Directory submission review；MeloTune iOS 作为跨域 mesh agent 使用 CAT7/mood 调整播放；一人 AI startup 的日常运营 mesh 中报告 14 波训练数据生成冲刺。跨平台 Mac↔Windows CMB 是线框互操作样例，不是单独的第三个部署。

## 局限性
- CAT7 的 7 字段固定 schema 可能限制某些高度专业化科学领域特殊数据结构的表达——body schema 虽可扩展但 header 不可变。
- 实证部署是 N=3、Mac↔Windows LAN、同一 Claude Opus 4.7 家族、单团队/作者运营场景；N≥10 收敛、多组织部署和跨提供商异质性（Claude/GPT/Gemini/开源模型）仍未验证。
- Remix 机制不把原始同伴信号写入接收者记忆；在需要审计原始记录的合规场景中，需要额外的原始日志/签名层配合。
- SVAF 的 αf 角色权重当前为静态分配，动态话题依赖调整列为开放问题。
- CAT7+SVAF+lineage+remix 是否为满足 P1-P3 的最小/唯一充分集——形式化证明缺失。

## 核心贡献
**一句话**：MMP 是首个为多 LLM Agent 提供"语义基础设施"的生产级协议——通过 CAT7 固定 7 字段 schema + SVAF 按角色字段级评估 + DAG 谱系 O(1) 回声检测 + remix 写入时过滤，使 Agent 间跨会话认知状态交换成为可能。
**Pipeline 速记**：Agent-A 发射 CAT7 CMB（7 字段 header + 可选 body）→ 接收者 SVAF 逐字段计算余弦 drift × 角色权重 → 带通分类（redundant/aligned/guarded/rejected）→ 准入信号经 remix 生成新 CMB 并记录谱系 parents/ancestors → 仅 remix 存储，原始信号不落盘 → 跨会话恢复时直接加载已评估理解。

## 与综述的关联
MMP 是科学发现多 Agent 系统"如何对话与记忆"的协议层答案。科学发现需要理论家、实验家、数据分析师等多个角色 Agent 在数周内持续协作，MMP 的 P1（按字段选择性接受）防止错误假设在 Agent 间传播，P2（谱系追踪）确保每条科学推断可追溯至原始证据或推理步骤，P3（写入时过滤）保证每个 Agent 恢复的是经自身角色评估的科学理解。与 A-MEM（单 Agent 记忆演化）、MIRIX（多类型记忆组织）、Intrinsic Memory Agents（异质角色记忆）形成互补——MMP 位于协议层，定义 Agent 间如何交换，而其他框架定义 Agent 内如何存储。
