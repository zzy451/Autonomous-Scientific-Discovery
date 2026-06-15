# GStack 2025

## 基本信息
- **论文**: GStack: Virtual Engineering Team for Claude Code
- **作者**: Garry Tan (Y Combinator President & CEO)
- **年份**: 2025-2026 (持续更新)
- **来源**: https://github.com/garrytan/gstack (MIT License; README/self-reported metrics)
- **关键词**: AI工程团队, 技能编排, 并行开发, 冲刺工作流, YC方法论, Claude Code

## 核心思想
GStack 是 Y Combinator CEO Garry Tan 打造的开源工具集，将 Claude Code 转化为"虚拟工程团队"。仓库 README 将其组织为 23 个 specialists 与 8 个 power tools，围绕 Think → Plan → Build → Review → Test → Ship → Reflect 的冲刺工作流运转。Tan 在 README 中自称 2026 年逻辑代码产出速度是 2013 年的约 810 倍（11,417 vs 14 逻辑行/天），且与 Conductor 配合支持 10-15 个并行冲刺。MIT 协议开源，README 称 setup 支持 Claude Code 以及 OpenAI Codex CLI、Cursor、OpenCode 等 10 个 AI coding agents。

## 方法细节
每个技能是工作流中的一个节点，输出自动馈入下游，无信息遗漏：
- **Think（思考）**：`/office-hours`——YC 风格产品质问，6 个强制问题重新框定需求，输出设计文档馈入所有下游技能。
- **Plan（规划）**：`/plan-ceo-review`（CEO/创始人视角，4 种范围模式挑战战略）、`/plan-eng-review`（架构锁定 + ASCII 图 + 边界情况 + 测试计划）、`/plan-design-review`（设计维度 0-10 评分 + AI Slop 检测）、`/plan-devex-review`（开发者体验审查，20-45 个强制问题）。
- **Build（构建）**：`/design-consultation`（从零建立设计系统）、`/design-shotgun`（生成 4-6 个 AI 样机变体 + 对比看板 + 品味记忆学习）、`/design-html`（Pretext 计算布局，30KB 零依赖生产级 HTML/CSS）、`/autoplan`（自动执行 CEO→设计→工程/DX 评审链）、`/spec`（五阶段规格生成与质量门禁）。
- **Review（评审）**：`/review`（高级工程师级代码审查，自动修复明显问题）、`/codex`（OpenAI Codex 独立第二意见，跨模型交叉分析）、`/design-review`（设计审计 + 原子提交修复）、`/devex-review`（实际开发者体验测试，对比计划评分）。
- **Test（测试）**：`/qa`（真实 Chromium 浏览器点击测试 + Bug 修复 + 回归测试生成）、`/qa-only`（纯 Bug 报告不修改代码）、`/investigate`（系统根因排查，铁律——无调查不修复）、`/benchmark`（页面性能和 Core Web Vitals 基线）。
- **Ship（发布）**：`/ship`（同步 main、运行测试、审计覆盖率、推送、开 PR，自动引导测试框架）、`/land-and-deploy`（合并 PR → 等待 CI 部署 → 验证生产健康）、`/canary`（部署后 SRE 监控循环）。
- **Reflect（反思）**：`/retro`（团队感知的每周回顾，按人分解、发布趋势、测试健康）、`/document-release`（自动更新所有项目文档，Diataxis 覆盖图）、`/document-generate`（从零生成缺失文档）、`/learn`（跨会话项目模式、偏好和教训管理）。

## 关键结果
- **并行冲刺 + Conductor**：与 Conductor 配合，每个 Claude Code session 隔离工作区，一个规划、一个评审、多个实现、一个 QA；10-15 个并行冲刺是 Tan 在 README 中描述的个人实践上限。
- **跨智能体协作**：`/pair-agent` 使 Claude Code、OpenClaw、Hermes、Codex 等共享浏览器，隔离 Tab + 作用域 Token + 频率限制。
- **安全护栏**：`/careful`（破坏性命令前警告）、`/freeze`（锁定编辑至单目录）、`/guard`（full safe 模式）、`/cso`（OWASP Top 10 + STRIDE + 17 项误报排除）。
- **提示注入防御**：浏览器侧栏内置 22MB ML 分类器 + Claude Haiku 转录检查 + 金丝雀 Token + 双分类器共识判决。
- **持续检查点模式**：技能自动提交 `WIP:` 提交，`/context-restore` 重建会话状态，`/ship` 在 PR 前压缩 WIP 提交。

## 与科学工作流的映射
GStack 的冲刺结构可以类比到科研软件工作流：Think（问题重构/假设形成）→ Plan（实验或实现方案）→ Build（代码实现）→ Review（代码/设计审查）→ Test（运行验证）→ Ship（发布）→ Reflect（回顾改进）。但这种映射主要适用于科研代码、数据产品和工程化研究流程，不能直接等同于湿实验、材料合成或临床验证。

## 核心贡献
GStack 2025 的核心贡献是展示了一套可复用的 agentic software engineering 技能编排范式：用 slash-command skills、角色化审查、浏览器 QA、安全护栏、发布流程和并行 workspace，把单一 coding agent 组织成接近工程团队的工作流。

## 与综述的关联
- 科学发现智能体的"工程编排"参考实现——GStack 的多智能体协调与质量关卡机制可迁移到 AI-Researcher 等系统的实验代码生成与验证，但需要重新定义科学领域的 QA、统计检验和复现实验技能。
- 与 Addy Osmani Agent Skills、Anthropic Skills 共同展示技能生态如何从"单技能"走向"多技能编排+跨智能体协作"。
- Garry Tan 的 810x 生产力声明可作为一个公开自测案例，而不能作为独立验证的普遍生产力结论。

## 局限性
- 深度绑定 Claude Code 生态与特定基础设施（Playwright、Bun、Conductor），独立运行的门槛较高。虽支持多种 AI coding agents，但核心功能在非 Claude Code 环境中的可用性参差不齐。
- 810x 生产力声明基于个人测量，控制变量（经验增长、项目复杂度变化、工具之外的效率提升）难以完全分离——虽提供了复现脚本与详细方法论（docs/ON_THE_LOC_CONTROVERSY.md），但外部独立验证缺乏。
- 科学实验场景的适配尚需领域特化——GStack 的 QA 测试（浏览器点击）、安全审计（OWASP/STRIDE）直接适用于 Web 应用，但科研领域的实验验证（如统计检验的正确性、数据处理的合规性）需要全新的技能模块。
- 并行冲刺的上限（10-15）由 Conductor 的工作区隔离能力决定，扩展到更大规模（如自动运行数百个实验变体）需额外的资源编排与冲突解决机制。
