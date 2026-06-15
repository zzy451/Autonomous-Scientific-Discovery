# ChemCost 2026

## 基本信息
- **论文**: Can Agents Price a Reaction? Evaluating LLMs on Chemical Cost Reasoning
- **作者**: Yuyang Wu et al.
- **年份**: 2026
- **来源**: arXiv:2605.07251
- **关键词**: benchmark, chemistry, scientific-tool-use, counterexample, cost-reasoning

## 核心思想
ChemCost 评测 LLM agent 是否能从化学反应描述出发，完成采购成本估计。这个任务看似比合成规划简单，但要求 agent 同时做好化学实体 grounding、供应商报价检索、包装规格选择、数量归一化和算术计算。

## 评测目标
ChemCost 评测 LLM agent 是否能从化学反应描述出发，完成采购成本估计。这个任务看似比合成规划简单，但要求 agent 同时做好化学实体 grounding、供应商报价检索、包装规格选择、数量归一化和算术计算。

论文要回答的问题是：科学工具访问是否足以让 agent 可靠完成化学领域的资源约束推理。

## 基准设计
ChemCost 构造了一个 judge-free benchmark，避免依赖专家主观评价或 LLM-as-judge。

- **任务输入**：化学反应描述。
- **任务目标**：估计采购成本。
- **核心步骤**：
  1. grounding chemical identities；
  2. retrieve supplier quotes；
  3. select valid purchasable packs；
  4. normalize quantities；
  5. compute total cost。
- **诊断维度**：grounding、retrieval、procurement 和 arithmetic。
- **鲁棒性测试**：加入 controlled noise，包括化学别名、数量表达、缺失字段和格式扰动。

## 关键数字

| 指标 | 数值 |
|---|---:|
| 可评测反应数 | 1,427 |
| 化学品数量 | 2,261 |
| 供应商报价数量 | 230,775 |
| 最强 agent 在 clean inputs 上 25% relative error 内准确率 | 50.6% |
| 人类参考 CTA@25 / CTA@10 | 66.9% / 57.0% |
| 最强 agent 在 clean inputs 上 10% relative error 内准确率 | 37.0% |

## 设计哲学

ChemCost 的设计哲学是用有精确答案的真实化学采购任务检验 agent。它把“科学工具使用”拆成可定位的失败阶段，避免只看最终文本是否像专家回答。

这使 ChemCost 成为一个强反例：科学 agent 即使可以调用工具，也可能因为解析脆弱、证据整合差、包装选择无效或工具调用不收敛而失败。

## 局限性

ChemCost 只覆盖化学采购成本估计，不覆盖合成路线是否可行、反应是否成功、实验安全或真实实验执行。它评测的是资源约束下的化学推理和工具使用，而不是完整化学发现。

## 核心贡献
ChemCost 2026 的核心贡献是把化学采购成本估计转化为 judge-free、可阶段诊断的 agent 评测任务，证明工具访问虽然必要，但不足以保证科学场景中的实体 grounding、报价检索、包装选择和数值聚合可靠完成。

## 与综述的关联

在 Scientific Workflow 中，ChemCost 覆盖 Knowledge Grounding、Result Analysis 和 Verification，尤其对应 resource planning 和 cost reasoning。

在 Skill Lifecycle 中，它对应：

- Retrieval：供应商报价和化学实体检索；
- Execution：工具调用和数值计算；
- Verification：阶段级错误诊断；
- Boundary：验证 tool access 的不足。

Evidence Role 应标为 **Counterexample + Boundary**。它直接约束“有工具的 agent 就能做科学任务”的说法。对我们的综述来说，ChemCost 很适合放在 scientific tool-use 和 resource-aware skill 的局限性部分。

## 论证级补充

### 方法流程细化

1. 输入是化学反应描述，系统需要识别反应物、试剂、用量和采购需求。
2. Agent 需要完成 chemical identity grounding，再检索供应商报价和可购买包装规格。
3. 系统将包装规格、价格和所需用量归一化，并计算采购总成本。
4. Benchmark 按 grounding、retrieval、procurement 和 arithmetic 拆解错误来源，避免只看最终答案。

### 关键数字核对

| 指标 | 数值 | 原文位置/表格 | 可用于正文的说法 |
|---|---:|---|---|
| 可评测反应数 | 1,427 | benchmark 数据集描述 | ChemCost 用 1,427 个真实化学成本估计任务评估 resource-aware reasoning。 |
| 化学品数量 | 2,261 | benchmark 数据集描述 | 任务需要对大量化学实体进行 grounding。 |
| 供应商报价数量 | 230,775 | benchmark 数据集描述 | 报价规模说明该任务不是简单算术，而是检索、选择和归一化链条。 |
| 最强 agent clean inputs 25% relative error 内准确率 | 50.6% | model evaluation | 即使在 clean inputs 下，最佳 agent 也只有约一半样本进入 25% 相对误差范围。 |
| 人类参考 clean inputs 25% relative error 内准确率 | 66.9% | Table 1 | 最强 agent 与人类参考仍有明显差距。 |
| DeepSeek V4 Pro clean inputs 10% relative error 内准确率 | 37.0% | Table 1 | 严格误差阈值下，agent 的可靠数值准确率进一步下降。 |

### 可支撑的论点

- 科学工具访问本身不足以保证可靠 scientific reasoning；资源推理会在实体对齐、检索、采购选择和算术环节逐步出错。
- Resource planning 是科学工作流中的独立能力，不应被简单归入“工具调用”。
- 阶段级诊断比总分更适合分析 scientific agent 的失败机制。

### 不能支撑的过度结论

- 不能把 ChemCost 的失败结果推广为“LLM agent 不适合所有化学任务”。
- 不能把成本估计失败等同于合成规划或实验执行失败。
- 不能忽略 benchmark 的供应商数据、价格时效性和采购场景对结果的影响。

### 与其他 anchor papers 的关系

- 反例：与 SciAgentGym 一起说明 tool-use skill 的边界，区别在于 ChemCost 有明确数值答案和阶段级错误诊断。
- 对照：与 MOSAIC 相比，ChemCost 不评估合成协议成功率，而评估实验前资源与采购约束；与 tool-free baseline 的对比还说明 ReAct + 工具显著优于纯 prompt，但仍远未解决任务。
- 补充：与 RoboChem-Flex 共同支撑“真实科学执行需要考虑成本、设备和资源条件”。

### 框架映射

| 维度 | 标签 |
|---|---|
| Scientific Workflow | Knowledge Grounding; Experiment Design; Verification |
| Skill Lifecycle | Retrieval; Execution; Verification |
| Evidence Role | Counterexample; Boundary |
| Cross-cutting Constraints | resource awareness; price grounding; arithmetic reliability; tool-use brittleness |
