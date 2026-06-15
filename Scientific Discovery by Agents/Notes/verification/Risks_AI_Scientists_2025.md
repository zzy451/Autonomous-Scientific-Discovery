# Risks AI Scientists 2025

## 基本信息
- **论文**: Risks of AI Scientists: Prioritizing Safeguarding Over Autonomy
- **作者**: Xiangru Tang, Qiao Jin, Kunlun Zhu, Tongxin Yuan, Yichi Zhang, Wangchunshu Zhou, Meng Qu, Yilun Zhao, Jian Tang, Zhuosheng Zhang, Arman Cohan, Dov Greenbaum, Zhiyong Lu, Mark Gerstein
- **年份**: 2025
- **来源**: Nature Communications, doi:10.1038/s41467-025-63913-1; arXiv:2402.04247v5 (2025-07-21)
- **关键词**: ai-scientist-safety, governance, risk-analysis, agent-alignment, scientific-tools, counterexample

## 核心思想
这篇 perspective 讨论的核心问题是：当 LLM-powered agents 被用于科学研究，并能访问专业数据库、软件工具、机器人或实验设备时，风险不再只是“模型输出有害文本”，而是扩展为 **agent action** 对现实世界造成影响。

作者把 AI scientists 定义为具备科学领域能力的自主系统，能够访问生物数据库、执行化学实验、从 in silico 分析到物理实验流程中自动规划和行动。论文主张，AI scientist 的发展不能只追求更高 autonomy，而应优先建立 safeguarding：保护人类、环境和科学系统免受误用、事故和长期副作用。

## 方法细节
论文不是实证 benchmark，也没有提出新的可运行 AI scientist 系统；它采用 perspective / scoping review 的方式，建立 AI scientist 风险分类和治理框架。

风险分析分为三条轴线，分别对应 Fig. 1 中的 user intent、scientific domain 和 environmental impact：

- **User Intent**：direct malicious intent、indirect malicious intent、unintended consequences。
- **Scientific Domain**：chemical、biological、radiological、physical、information science、emerging technology。
- **Environmental Impact**：natural environment、human health、socioeconomics。

作者还把 AI scientist 的脆弱性对应到五个 agent 模块：

- **LLMs**：事实错误、jailbreak、推理缺陷、知识过时。
- **Planning**：缺乏长期风险意识、资源浪费和死循环、多任务规划不足。
- **Action**：工具使用缺乏监督，人机交互行动规范不足。
- **External Tools**：机器人、化学分析软件、分子设计工具等可能因误用产生现实危害。
- **Memory and Knowledge**：领域安全知识不足、人类反馈有限、环境反馈不足、研究来源不可靠。

治理方案是三元框架：

1. **Human regulation**：开发者和用户培训、许可、审计、IRB/机构级监督、分层报告机制。
2. **Agent alignment**：从 LLM-level alignment 扩展到 agent-level alignment，学习专家工作流、行动序列和风险反馈，并通过 red teaming、task alignment 等方式评估安全。
3. **Agent regulation and environmental feedback**：约束工具使用、模拟环境、实时决策验证、critic models、基于 action data 的调优。

## 关键结果

这篇论文没有进行模型实验，也没有报告某个 AI scientist 的成功率或攻击成功率。它的关键贡献是风险框架和治理主张：

1. **AI scientist 风险不同于普通 LLM 风险**  
   普通 LLM 主要生成文本；AI scientist 可能调用实验工具、控制设备、执行化学/生物/物理操作，因此需要从 output safety 转向 behavioral safety。

2. **风险可来自恶意目标，也可来自良性目标的副作用**  
   作者特别强调 indirect malicious intent 和 unintended consequences：用户可以让 agent 合成看似无害的中间体，最终组合成危险目标；也可能在良性科研任务中生成危险副产物或长期环境影响。

3. **科学领域风险具有 domain specificity**  
   化学风险包括危险反应、爆炸物、有害农药等；生物风险包括病原体操作、基因编辑、生物危害；信息科学风险包括医学文献投毒、隐私泄露、错误知识传播；物理和放射性场景还涉及设备故障、泄漏、核安全等。

4. **现有安全工作不足以覆盖 AI scientists**  
   作者指出当前防护主要集中在 LLM content safety、jailbreak 防御或通用 agent monitor；针对 AI scientists 的专门机制较少。SciGuard、ChemCrow safety tool、CLAIRify 等是相关起点，但整体仍缺少行动空间约束、专门 risk-control model、领域专家知识和系统性安全 benchmark。

5. **需要从“输出是否安全”转向“行动序列是否安全”**  
   同一个工具调用在不同实验上下文中风险不同，因此不能只过滤最终文本。Agent-level safety 需要评估计划、工具选择、参数、环境反馈和长期后果。

6. **作者没有声称现有 AI scientist 系统都存在可利用漏洞**  
   Ethical and societal impact 中明确说明，论文没有开发或测试针对现有 AI scientist 的具体 exploit；其分析也不一定适用于已经具备全面安全措施和领域专家监督的 robustly designed systems。

## 与综述的关联

这篇论文是我们综述中的 **Counterexample + Boundary evidence**。它不否定 agentic scientific discovery 的价值，但直接提醒：越强调 autonomy，越需要证明系统具备安全的行动约束、环境反馈理解和人类监管机制。

在 Scientific Workflow 中，它主要约束 Experiment Design、Execution 和 Verification：任何能设计实验、调用工具或影响真实世界的 agent，都必须有 safety verification。  

在 Skill Lifecycle 中，它提示 skill 不只是“能做事”的 procedure，还必须包含：

- Representation：安全约束、许可范围、SOP、危险工具清单。
- Retrieval：检索 domain-specific safety knowledge，而不只是科研知识。
- Composition：多工具链组合前必须评估组合风险。
- Execution：关键工具调用需要权限、日志、审计和实时监控。
- Evolution：失败案例和 near-miss 需要进入长期记忆和安全训练数据。
- Verification：需要 red teaming、simulation、expert review、real-world validation。

它对综述框架的作用很关键：Skill-driven scientific discovery 不能只写 skill acquisition / composition / execution，还必须写 skill governance。否则“技能越强”可能意味着“风险表面越大”。

## 局限性

- 论文是 perspective / scoping review，不提供新 benchmark、模型实验或可复现实证数据。
- 风险分类很全面，但不同风险的概率、严重性、可检测性没有量化。
- 许多治理建议仍停留在原则层面，例如 licensing、auditing、specialized committees、critic models，具体实施成本和跨国执行机制尚不清楚。
- 论文主要讨论潜在风险，没有系统比较不同 AI scientist 系统已有安全机制的实际有效性。
- 作者明确没有开发或测试具体 exploit，因此不能把论文解读为“现有系统已经被证明不安全”。

## 核心贡献

这篇论文的核心贡献是把 AI scientists 的安全问题从 LLM 输出安全扩展到现实行动安全，并提出 human regulation、agent alignment、environmental feedback 三元治理框架，为 autonomous scientific agents 的安全边界、监管章节和反例证据提供主干文献。
