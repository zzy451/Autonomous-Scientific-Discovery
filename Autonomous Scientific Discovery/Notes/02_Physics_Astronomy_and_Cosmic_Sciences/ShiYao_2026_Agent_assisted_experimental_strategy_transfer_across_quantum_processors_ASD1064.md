# Agent-assisted experimental strategy transfer across quantum processors

**论文信息**

- ID：ASD-1064
- 标题：Agent-assisted experimental strategy transfer across quantum processors
- 作者：Hou, Shi-Yao; Wu, Zipeng; Zhang, Chao; Feng, Guanru; Li, Keren; Xiang, Jingen
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.21047
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1064.txt
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/ShiYao_2026_Agent_assisted_experimental_strategy_transfer_across_quantum_processors_ASD1064.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 目标与对象 | 五台三量子比特NMR处理器执行Grover态制备。 | TXT line 278；核验TXT行号 278 | Nuclear magnetic resonance (NMR) provides an established setting for quantum control and computation 19, including experimental polynomial optimization on a four-qubit processor 20. Here we evaluate an agent-assisted experimental strategy on five three-qubit NMR processors, using three-qubit Grover target-state preparation as a common experimental task 21, 22. The processors shared a common experimental interface but differed in Hamiltonian parameters, spectral structure and operating conditions. The strategy was developed under human supervision on one processor and applied sequentially to four others. Each deployment involved local calibration and measurement, together with device-specific control-pulse optimization using gradient ascent pulse engineering (GRAPE) 23. Across the four deployment processors, the marked-state populations of the reconstructed dominant eigenstates ranged from 0.9100.910 to 0.9590.959, with relative deviations below 3.8%3.8\% from the ideal value of 0.9450.945. | 高（一手正文；非独立复现） |
| Agent行动 | 工具用于表征、控制合成、测量和重建。 | TXT line 308；核验TXT行号 308 | In T2E, the agent invokes and coordinates deterministic tools to characterize the processor, synthesize controls, acquire measurements and reconstruct experimental outputs. It uses the resulting evidence to select subsequent actions and adapt the experimental procedure. Operators retain responsibility for instrument preparation, physical adjustment, safety and procedural authorization. The agent therefore coordinates decisions at a higher level than a conventional controller, while numerical calculations remain assigned to deterministic tools and physical interventions to operators. | 高（一手正文；非独立复现） |
| 迁移 | 策略在一台开发后部署到四台设备。 | TXT line 241；核验TXT行号 241 | Progress in quantum hardware requires a growing volume of experiments across diverse devices, straining the capacity of human experts. Automation remains challenging because device differences and drift can render workflows developed on one processor unsuitable for another. Here we present an agent-assisted experimental strategy for conducting experiments across three-qubit nuclear magnetic resonance processors. Developed on one processor and applied sequentially to four others, the strategy uses an agent to assess experimental evidence, select subsequent measurements and adapt procedures, with operators providing instrument preparation and physical intervention. | 高（一手正文；非独立复现） |
| 定量验证 | 迁移设备结果接近理想标记态布居。 | TXT line 243；核验TXT行号 243 | The experimental strategy was refined through sequential deployment, and all four processors ultimately produced outputs dominated by their respective marked states. The marked-state populations of the reconstructed dominant eigenstates ranged from 0.9100.910 to 0.9590.959, with relative deviations below 3.8%3.8\% from the ideal value of 0.945. These results demonstrate that an agent-assisted experimental strategy can be reused and refined across processors to realize a common quantum task, providing a basis for scaling experimental practice beyond individual devices. | 高（一手正文；非独立复现） |
| 工具 | 基于GPT-5的Codex使用Python和SpinQLink。 | TXT line 528；核验TXT行号 528 | The agent, identified in the Q0 manifest as Codex based on GPT-5, used Python experimental tools and a locally bundled spinqlink instrument interface. Its policy linked observations and quality checks to action selection, tool outputs and human interventions. Transfer context admitted generic policies and tools but excluded development-device numerical parameters, waveforms and reference shapes. These were procedural restrictions; automatic context isolation was not established. Configuration records, decision examples and the incomplete Q3 entry-context evidence are described in Supplementary Sec. S2. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出跨三量子比特NMR处理器迁移的Agent辅助实验策略。策略在Q0开发，之后部署到四台处理器，以Grover标记态制备为共同任务。Agent依据本地实验数据选择测量并适配程序，操作者负责准备与物理干预。 本记录依据全文摘要、方法、实验、结果和局限段落整理，具体依据与引用定位见上列证据日志。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。在量子硬件上执行Grover态制备任务。
  - 原文位置：TXT line 278；核验TXT行号 278；引文：Nuclear magnetic resonance (NMR) provides an established setting for quantum control and computation 19, including experimental polynomial optimization on a four-qubit processor 20. Here we evaluate an agent-assisted experimental strategy on five three-qubit NMR processors, using three-qubit Grover target-state preparation as a common experimental task 21, 22. The processors shared a common experimental interface but differed in Hamiltonian parameters, spectral structure and operating conditions. The strategy was developed under human supervision on one processor and applied sequentially to four others. Each deployment involved local calibration and measurement, together with device-specific control-pulse optimization using gradient ascent pulse engineering (GRAPE) 23. Across the four deployment processors, the marked-state populations of the reconstructed dominant eigenstates ranged from 0.9100.910 to 0.9590.959, with relative deviations below 3.8%3.8\% from the ideal value of 0.9450.945.
- 多步行动过程：yes。Agent表征设备、合成控制、采集并重建结果。
  - 原文位置：TXT line 308；核验TXT行号 308；引文：In T2E, the agent invokes and coordinates deterministic tools to characterize the processor, synthesize controls, acquire measurements and reconstruct experimental outputs. It uses the resulting evidence to select subsequent actions and adapt the experimental procedure. Operators retain responsibility for instrument preparation, physical adjustment, safety and procedural authorization. The agent therefore coordinates decisions at a higher level than a conventional controller, while numerical calculations remain assigned to deterministic tools and physical interventions to operators.
- 至少一种Agent能力：yes。Agent依据证据选择测量并适配实验程序。
  - 原文位置：TXT line 241；核验TXT行号 241；引文：Progress in quantum hardware requires a growing volume of experiments across diverse devices, straining the capacity of human experts. Automation remains challenging because device differences and drift can render workflows developed on one processor unsuitable for another. Here we present an agent-assisted experimental strategy for conducting experiments across three-qubit nuclear magnetic resonance processors. Developed on one processor and applied sequentially to four others, the strategy uses an agent to assess experimental evidence, select subsequent measurements and adapt procedures, with operators providing instrument preparation and physical intervention.
- 明确科研流程角色：yes。Agent参与跨设备实验策略迁移和任务验证。
  - 原文位置：TXT line 528；核验TXT行号 528；引文：The agent, identified in the Q0 manifest as Codex based on GPT-5, used Python experimental tools and a locally bundled spinqlink instrument interface. Its policy linked observations and quality checks to action selection, tool outputs and human interventions. Transfer context admitted generic policies and tools but excluded development-device numerical parameters, waveforms and reference shapes. These were procedural restrictions; automatic context isolation was not established. Configuration records, decision examples and the incomplete Q3 entry-context evidence are described in Supplementary Sec. S2.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：02
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：02（仅归档，不覆盖其他模块）
- 模块内分类路径：02.02 物理学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为量子硬件实验任务，归入物理科学02，而非单纯软件或抽象算法。

### 2.3 容易混淆的边界

对象为量子硬件实验任务，归入物理科学02，而非单纯软件或抽象算法。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

tool_augmented_llm

### 3.2 科研流程角色

experiment_planning；instrument_operation；cross_device_transfer

基于GPT-5的Codex调用Python实验工具和SpinQLink接口，协调表征、控制合成、采集和重建。

### 3.3 自主能力

Agent依据证据选择测量并适配实验程序。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是展示跨处理器实现共同量子实验任务；系统贡献是基于证据选择行动并迁移策略的Agent流程。

### 4.2 系统流程与组件

Agent读取谱线和校准证据，判断是否需更多测量，调用GRAPE生成设备专属控制脉冲并采集层析数据，之后继续或请求人工处理；策略从Q0迁移至四台处理器。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

五台三量子比特液态NMR处理器执行共同Grover任务；以局部Hamiltonian拟合、响应矩阵、七测量基层析及理想态布居验证。

### 5.2 基线、指标与结果

作者报告四台迁移设备主特征态标记态布居为0.910至0.959，相对理想0.945偏差低于3.8%。

### 5.3 科学贡献与证据强度

科学贡献是展示跨处理器实现共同量子实验任务；系统贡献是基于证据选择行动并迁移策略的Agent流程。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

区别于只做校准或接口兼容，本研究重建本地模型并实现共同多量子比特任务。

## 7. 局限性与风险

- author_stated：操作人员仍负责安全、设备准备和物理干预；跨平台需要适配本地模型与工具。
- reviewer_inference：目前只在同类NMR设备验证，不能直接外推其他量子硬件。

## 8. 对综述写作的价值

可讨论实验Agent策略迁移依赖本地校准及人类物理参与。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Agent辅助策略经本地适配，在四台额外NMR设备上实现Grover实验任务。

### 9.2 速记版 pipeline

Agent读取谱线和校准证据，判断是否需更多测量，调用GRAPE生成设备专属控制脉冲并采集层析数据，之后继续或请求人工处理；策略从Q0迁移至四台处理器。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1064
inclusion_status=to_read
scientific_object_modules=02
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=02
module_taxonomy_codes=02.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`02.02.06` 量子力学；二级：`02.02`。
- 原文位置：PDF p.2。
- 判定：三量子位NMR处理器量子态及Grover实验，量子力学。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
