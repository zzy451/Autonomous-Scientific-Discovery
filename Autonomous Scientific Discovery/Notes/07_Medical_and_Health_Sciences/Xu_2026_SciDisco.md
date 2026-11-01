# Scaling Scientific Discovery Environments for Turn-Level Agentic RL

**论文信息**

- ID：ASD-0919
- 标题：Scaling Scientific Discovery Environments for Turn-Level Agentic RL
- 作者：Xu, Yucheng; Zhang, Keyi; Yu, Yuyang; Zhang, Min; Meng, Shiyuan; Chu, Pei; Tu, Zhongying
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2607.28990
- 一手阅读来源：https://arxiv.org/abs/2607.28990
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：Scaling Scientific Discovery Environments for Turn-Level Agentic RL
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/source_F/2607.28990.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 任务定义 | 任务要求针对数据评价科学假设、形成统计发现并用可执行分析支撑主张。 | §3 Problem Formulation | high |
| 环境 | 环境包含假设、数据、hidden evidence graph、代码沙盒和自动verifier。 | §4.1 SciThèque；Appendix B | high |
| 多步训练 | 用DAG生成并过滤多轮轨迹；DiscoPO按轮次奖励产生可验证证据的动作。 | §4.2–4.3 | high |
| 对象覆盖 | 数据领域分布由economics、medicine、biology和earth science领头。 | Appendix A；Table 5 | high |
| 主结果 | 作者报告SciDisco-14B在假设驱动科学数据分析benchmark达到SOTA。 | Abstract；§5.4 | high |
| 分类依据 | 任务在具体领域数据上进行分析与主张验证，属于科学对象benchmark，而非纯通用Agent能力测试。 | Appendix task examples | high |
| 对象数据来源支持模块内细分 | FRED 151个环境；UniProt 114、STRING yeast 34；CDC FluView 65、CDC PLACES 36；USGS water data 41。分别支持经济、蛋白、水文与流行病学分析对象。 | Appendix A，Table 6及对应参考文献 | high |
| 具体公共卫生任务的多步分析轨迹 | CDC FluView的年龄组ILI计数是否在lag 1 Granger-cause总ILI；示例1379行、12列，轨迹10次分析行动加最终提交。 | Appendix示例任务，Tables 14–15 | high |

## 0. 摘要翻译

SciDisco构建包含开放科学数据、研究假设、隐藏证据DAG、代码沙盒和verifier的交互环境，训练Agent逐轮执行可验证的科学数据分析。数据覆盖经济、医学、生物和地球科学等领域。作者报告SciDisco-14B在假设驱动科学数据分析benchmark上达到SOTA，并用逐轮credit奖励产生可验证证据的动作。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
Agent通过多轮环境互动读取数据、执行统计分析、沿证据图验证科学主张并依据每轮反馈改进；全文已给出经济、医学、生物和地球科学等具体对象类别，不能自动归01.04。

### 1.2 排除风险检查

主控追加核对Appendix A Tables 5–6及14–15：FRED经济数据→11.01，UniProt/STRING蛋白对象→06.03.06，USGS water data→05.02.07，CDC FluView与PLACES→07.03.01。不是01.04；不因采用RL和Python就追加01。Table 5另列127个工程域环境，但具体工程对象尚未核清，暂不追加09。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：05;06;07;11
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：07（仅归档，不替代多模块事实）
- 模块内分类路径：05.02.07; 06.03.06; 07.03.01; 11.01
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

对象为真实经济、医学、生物和地球科学数据上的假设驱动分析。基线包括既有scientific analysis agents及SFT/RL训练变体。指标包括假设证据支持、过程和终局验证、benchmark performance。作者报告SciDisco-14B达到SOTA；消融表明SFT提供主要首阶段收益，DiscoPO再有提升。具体分值未在此转录。

### 2.3 容易混淆的边界

主控追加核对Appendix A Tables 5–6及14–15：FRED经济数据→11.01，UniProt/STRING蛋白对象→06.03.06，USGS water data→05.02.07，CDC FluView与PLACES→07.03.01。不是01.04；不因采用RL和Python就追加01。Table 5另列127个工程域环境，但具体工程对象尚未核清，暂不追加09。

## 3. Agent 系统与科研流程角色

Agent通过多轮环境互动读取数据、执行统计分析、沿证据图验证科学主张并依据每轮反馈改进；全文已给出经济、医学、生物和地球科学等具体对象类别，不能自动归01.04。

科研流程与自主能力以本文实际行动和工具调用为依据：

SciThèque把假设、数据、隐藏证据图和verifier编译为任务；从DAG合成并筛选多轮演示；DiscoPO按轮次奖励产生可验证分析证据的动作。

## 4. 方法设计

### 4.1 方法动机与设计

提出规模化、过程可验证的科学数据发现环境，并将训练credit从单一终局结果细化至每轮可验证证据贡献。

### 4.2 系统流程与组件

SciThèque把假设、数据、隐藏证据图和verifier编译为任务；从DAG合成并筛选多轮演示；DiscoPO按轮次奖励产生可验证分析证据的动作。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

对象为真实经济、医学、生物和地球科学数据上的假设驱动分析。基线包括既有scientific analysis agents及SFT/RL训练变体。指标包括假设证据支持、过程和终局验证、benchmark performance。作者报告SciDisco-14B达到SOTA；消融表明SFT提供主要首阶段收益，DiscoPO再有提升。具体分值未在此转录。

### 5.2 基线、指标与结果

对象为真实经济、医学、生物和地球科学数据上的假设驱动分析。基线包括既有scientific analysis agents及SFT/RL训练变体。指标包括假设证据支持、过程和终局验证、benchmark performance。作者报告SciDisco-14B达到SOTA；消融表明SFT提供主要首阶段收益，DiscoPO再有提升。具体分值未在此转录。

### 5.3 科学贡献与证据强度

提出规模化、过程可验证的科学数据发现环境，并将训练credit从单一终局结果细化至每轮可验证证据贡献。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

连接数据科学Agent、科学发现benchmark、ReAct以及turn-level RL和过程监督研究。

## 7. 局限性与风险

任务集中于可计算开放数据分析，并不等同于自动实验执行；other类别及个别task的具体对象仍需查看任务目录。

## 8. 对综述写作的价值

展示科学数据Agent环境、过程验证和逐轮RL信号的结合，是对象多模块与通用方法边界样本。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

以逐轮证据训练科学数据Agent

### 9.2 速记版 pipeline

SciThèque把假设、数据、隐藏证据图和verifier编译为任务；从DAG合成并筛选多轮演示；DiscoPO按轮次奖励产生可验证分析证据的动作。

### 9.3 标注字段汇总

```text
paper_id=ASD-0919
inclusion_status=included
scientific_object_modules=05;06;07;11
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=07
module_taxonomy_codes=05.02.07; 06.03.06; 07.03.01; 11.01
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/07_Medical_and_Health_Sciences/ASD-0919_Scaling_Scientific_Discovery_Environments_for_Turn_Level_Agentic_RL.pdf`，共19页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2607.28990v1
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。
