# Generative Adversarial Reviews 2024

## 基本信息
- **论文**: Generative Adversarial Reviews: When LLMs Become the Critic
- **作者**: Nicolas Bougie, Narimasa Watanabe
- **年份**: 2024
- **来源**: arXiv:2412.10415
- **关键词**: peer-review, reviewer-agents, meta-review, manuscript-graph

## 核心思想
该工作用 LLM-powered reviewer agents 模拟科学论文审稿和 meta-review。

## 方法细节
系统使用 reviewer personas、manuscript graph、external knowledge 和 multi-round assessment，最后由 meta-reviewer 聚合结果。

## 关键结果
论文报告 GAR 在反馈质量和论文 outcome prediction 上接近人类 reviewer。

## 局限性
自动审稿不等于科学真值验证，仍存在偏差和责任问题。

## 核心贡献
展示 reviewer-agent architecture 可以服务科学评审流程。

## 与综述的关联
适合放入 `X2-Y1-Z7`，支撑多智能体 review / critique。

## 原文核对与分类复核
- **原文核对**：题名和摘要显示该工作关注 LLM 作为 critic 的 adversarial / review 场景。
- **机制判断**：它支撑多智能体审稿、批评和 meta-review，但不是完整科学发现闭环。
- **分类复核**：保持 `ASD 相关系统`；`X2` 正确；`Y1` 正确；`Z7` 正确。
- **写作用途**：适合放在 critique / review / verifier agents 小节。

## 深读补充（按 MARS 标准）

### 研究问题
Generative Adversarial Reviews 关注如何让 LLM 扮演 critic，产生更有用的评审和反驳，从而改善科学写作或研究想法。

### 系统架构 / 工作流
系统以 reviewer / critic 角色组织评审过程，并通过 adversarial review 思路暴露论文或想法中的弱点。

### 关键机制
核心是 adversarial critique。它不生成科学发现本身，而是支撑 reviewer / verifier agent。

### 实验验证与证据
原文评估 LLM critic 在 review 场景中的表现，展示自动批评对研究评估的潜力。

### 局限性补充
自动 critique 可能生成看似严厉但不 grounded 的意见，需要 CLAIMCHECK 这类 claim-level 检查。

### XYZ 分类逐项解释
- `X2`：reviewer / meta-reviewer 等角色化评审。
- `Y1`：批评和修正属于反思机制。
- `Z7`：主要支撑 review / validation。

### 综述写作用法
适合 critique / review agents 小节，但要和 grounded verification 区分。
