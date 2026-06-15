# Anthropic Skills Spec 2025

## 基本信息
- **论文**: Anthropic Agent Skills 仓库与规范
- **作者**: Anthropic
- **年份**: 2025
- **来源**: https://github.com/anthropics/skills
- **关键词**: Skills 规范, 技能系统, SKILL.md, 渐进式披露, 可复用指令, Claude Code

## 核心思想
Anthropic 发布的 Agent Skills 官方实现仓库，包含示例技能、规范文档入口与技能模板。Skills 是自包含的"指令+脚本+资源"文件夹，Claude 按需动态加载以提升特定任务表现。仓库中部分技能为开源（Apache 2.0），同时包含了驱动 Claude 文档创建与编辑功能的 DOCX/PDF/PPTX/XLSX 技能（源码可用但非开源）。此仓库是 Anthropic 对 Agent Skills 格式的具体实现；GitHub star 数会持续变化，不适合作为论文笔记中的稳定事实。

## 方法细节
- **SKILL.md 格式**：每个技能是以 YAML frontmatter + Markdown 指令构成的文件夹。仅需两个必填字段：`name`（小写/数字/连字符，唯一标识）和 `description`（完整功能描述与使用场景）。正文包含具体指令、示例与指南。
- **渐进式披露（Progressive Disclosure）**：三级加载机制——元数据（~100 tokens）在启动时加载到系统提示，完整指令（< 5000 tokens）在技能被触发时加载，脚本/参考文件按需加载。此设计最大化节省上下文窗口，使 Claude 可同时"知晓"数百技能而不耗尽 token 配额。
- **发现性/可组合性/可移植性（Discoverable/Composable/Portable）**：技能通过规范化的目录结构与元数据实现自动发现；多个技能可组合编排应对复杂任务；Anthropic 官方仓库说明中支持在 Claude Code、Claude.ai 和 Claude API 场景中使用，但不同渠道的安装、权限和运行时行为不完全相同。
- **三种使用渠道**：(1) Claude Code 插件市场——`/plugin marketplace add anthropics/skills` 一键安装；(2) Claude.ai 付费计划——内置可用；(3) Claude API——通过 Skills API 上传自定义技能。
- **技能分类**：创意与设计（艺术、音乐、设计）、开发与技术（Web 测试、MCP Server 生成）、企业工作流（沟通、品牌规范）、文档技能（DOCX/PDF/PPTX/XLSX）四大类。

## 关键结果
- `./skills/`：四大类技能示例——Creative & Design（艺术、音乐、设计）、Development & Technical（Web 测试、MCP Server 生成）、Enterprise & Communication（沟通、品牌规范）、Document Skills（DOCX/PDF/PPTX/XLSX，Source Available）。
- `./spec/`：原 Agent Skills 规范所在地，已独立迁移至 agentskills.io。
- `./template/`：Starter template，社区可基于此创建自定义技能；仓库本身同时可作为 Claude Code plugin marketplace 注册。
- 示例技能涵盖：PDF 表单提取、PPT 生成、XLSX 数据分析、品牌写作、前端测试、MCP Server 生成、设计咨询等。
- **Partner Skills**：Notion 等合作伙伴已发布基于此规范的技能（如 Notion Skills for Claude），展示了技能生态的外部扩展性。

## 设计哲学
Anthropic 在工程博客 "Equipping agents for the real world with Agent Skills" 中阐述了三大设计原则：
- **可发现性（Discoverable）**：通过 YAML frontmatter 中的 `description` 字段，Claude 可在会话启动时自动识别适用技能，无需用户手动指定。技能路由基于用户意图与技能描述的语义匹配。
- **可组合性（Composable）**：技能通过标准化接口可被编排为多步工作流——例如 PDF 技能 + 分析技能 + 报告技能组合完成文档审查任务。SKILL.md 的 Markdown 格式使技能间引用变得自然。
- **可移植性（Portable）**：技能格式强调文件夹、SKILL.md、脚本和资源的可迁移包装。Anthropic 官方仓库展示的是 Claude 生态内的实现；跨平台可移植性需要依赖 Agent Skills Spec 与各客户端适配，不能直接推断为所有平台行为一致。

## 与综述的关联
- 科学发现智能体的"技能生态"基础设施——Skills 提供了规范化、可共享、可组合的智能体能力扩展机制，使文献检索、数据分析、实验设计等科研技能可被标准化封装。
- 渐进式披露设计为科学发现系统中处理大规模领域知识提供了架构参考——在有限上下文内高效编排多个专业化学术技能（如领域检索器、统计检验器、引用验证器）。
- 与 Agent Skills Spec、SkillsBench、GStack、Osmani Agent Skills 共同构成本综述的 Skills 生态系统维度，代表了从"一次性提示词"到"可复用工具包"的范式转变。

## 局限性
- 当前实现深度绑定 Claude 生态，跨平台可移植性尚需社区适配验证——Agent Skills Spec 的目标正是解决这一问题。
- 文档技能（DOCX/PDF/PPTX/XLSX）为 Source Available 而非开源，限制了对复杂技能实现原理的学习与二次开发。
- 技能质量高度依赖人类编写者——SkillsBench 研究表明模型难以自主生成有效技能，Anthropic 当前的技能库规模仍有限（几十个），远未覆盖科学发现所需的数千个领域特定技能。

## 核心贡献
Anthropic Skills 仓库的核心贡献是给出了 Agent Skills 的官方工程实现和可运行样例，证明“技能”可以被封装为指令、脚本和资源的自包含目录，并由模型按需加载和组合。
