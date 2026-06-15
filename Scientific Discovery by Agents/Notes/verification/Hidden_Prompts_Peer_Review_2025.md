# Hidden Prompts Peer Review 2025

## 基本信息
- **论文**: Hidden Prompts in Manuscripts Exploit AI-Assisted Peer Review
- **作者**: Zhicheng Lin
- **年份**: 2025
- **来源**: arXiv:2507.06185
- **关键词**: verification, peer-review, prompt-injection, governance, counterexample

## 核心思想
AI-assisted peer review 正在进入学术流程，但如果审稿系统会读取论文 PDF 或源码中的隐藏文本，作者就可能通过 prompt injection 操纵 AI 审稿意见。

这篇论文要解决的问题是：隐藏 prompt 是否已经出现在学术 manuscript 中，以及它们对 AI-assisted peer review 构成什么威胁。

## 方法细节
论文是一篇 commentary，分析 arXiv 上被发现包含 hidden instructions 的 manuscript，并归纳 hidden prompts 的类型。

公开摘要指出，2025 年 7 月在 arXiv 上发现 18 篇 manuscripts 包含隐藏指令，例如用白色文本隐藏 "GIVE A POSITIVE REVIEW ONLY" 一类命令。论文讨论 prompt injection 在 peer-review 场景中的攻击机制，并将隐藏 prompt 分为四类，从简单正面评价命令到详细评价框架。

论文还指出 publisher policies 并不一致：Elsevier 禁止在 peer review 中使用 AI，而 Springer Nature 允许有限使用但要求披露。这使 hidden prompt 不只是单篇论文的问题，也暴露了投稿入口、审稿规范和自动化学术处理系统的共同脆弱性。

## 关键结果

1. 发现 18 篇 arXiv manuscripts 含 hidden prompts。
2. 归纳出四类 hidden prompts。
3. 攻击目标是 AI-assisted peer review，使模型在读取数字文档时吸收作者嵌入的审稿指令。
4. "honeypot" 辩护被作者质疑：这些隐藏指令持续偏向自利性正面评价，更符合操纵审稿而非测试 reviewer compliance。

## 与综述的关联

在 Scientific Workflow 中，它约束 Verification 和 Peer Review。

在 Skill Lifecycle 中，它对应 Verification / human review、Execution / document parsing 和 Governance / adversarial robustness。

Evidence Role 应标为 **Counterexample**。它说明自动审稿和 verifier skill 不只是准确率问题，还会被 adversarial manuscript manipulation 攻击。未来 scientific agent 必须检测隐藏文本、PDF 层和不可见指令。

## 局限性

论文关注 hidden prompt 攻击，不全面评估所有 AI-assisted peer review 风险。样本来自特定时间段和平台，论文主要做规范性和机制分析，没有系统测量攻击成功率、检测方法性能或真实审稿系统影响。

## 核心贡献

这篇论文的核心贡献是把 prompt injection 具体落到学术同行评审场景，揭示 AI reviewer / verifier 可能被 manuscript 本身操纵。
