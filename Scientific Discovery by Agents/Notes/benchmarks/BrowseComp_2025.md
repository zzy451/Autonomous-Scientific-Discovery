# BrowseComp 2025

## 基本信息
- **论文**: BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents
- **作者**: Jason Wei, Zhiqing Sun, Spencer Papay, Scott McKinney, Jeffrey Han, Isa Fulford, Hyung Won Chung, Alex Tachard Passos, William Fedus, Amelia Glaese
- **年份**: 2025
- **来源**: arXiv:2504.12516
- **关键词**: benchmark, web browsing, persistent search, information retrieval, AI agent, Deep Research

## 核心思想
该文提出 BrowseComp（Browsing Competition），一个简单但极具挑战性的网页浏览智能体基准。BrowseComp 包含 1,266 个需要持续、深度浏览互联网以寻找难以发现的纠缠信息的问题。这些问题由人类训练师以"逆向构建"方式创建：从已知事实出发，反向设计需要大量搜索才能找到答案的问题（如"1990-1994 年间，哪场足球赛有巴西裁判、4 张黄牌、4 次换人、其中一次是因伤在 25 分钟内换人？"）。尽管难度极高，BrowseComp 设计简洁——预期答案是短字符串、易于自动验证。最佳模型 Deep Research 达到 51.5% 准确率，GPT-4o 仅 0.6%，GPT-4o with browsing 仅 1.9%。人类训练师（同一群体但非问题创建者）在 2 小时内解决了 29.2% 的问题。BrowseComp 与编程竞赛基准的类比——衡量的是核心能力的不完全但有用的代理指标。

## 评测目标
评测 AI 智能体在互联网上持续、深入、创造性地寻找难以发现的事实信息的能力。常见问答基准（TriviaQA、Natural Questions）已饱和，现有检索基准聚焦"一次搜索即可找到"的信息。BrowseComp 专门测"需要浏览大量网页、综合多条线索、进行创造性搜索策略"的深度浏览能力。这种能力与科学发现高度相关：文献检索、假设验证、跨领域关联发现等都依赖类似的深度信息检索能力。

## 基准设计
- **题目数量/来源/难度分级**：1,266 个问题（原始 1,287，排除 21 个标签答案有误的问题）。完全由人类训练师基于个人兴趣领域创建。主题分布：TV shows & movies 16.2%、Science & technology 13.7%、Art 10.0%、History 9.9%、Sports 9.7%、Music 9.2%、Video games 5.6%、Geography 5.5%、Politics 4.7%、Other 15.6%。三重难度检验：(1) 现有模型（GPT-4o with/without browsing, o1, Deep Research 早期版本）无法解决；(2) 5 次简单 Google 搜索无法在结果首页找到答案；(3) 另一训练师 10 分钟内无法解决（若解决率 >40% 则修改问题）。
- **评分方式**：使用与 Humanity's Last Exam 相同的 grading prompt（LLM 判断预测答案与参考答案是否语义等价）。所有参考答案为短字符串。同时测量校准度（Calibration Error）——模型置信度与实际准确率的匹配程度。要求模型输出 answer + confidence score。
- **人类基线 vs AI 基线**：人类训练师（非问题创建者，无 AI 辅助）2 小时内解决 29.2%（367/1255），答案与参考答案一致率 86.4%。模型：GPT-4o 0.6%、GPT-4o w/ browsing 1.9%、GPT-4.5 0.9%、OpenAI o1 9.9%、Deep Research 51.5%。论文图示中 Best-of-64（基于置信度选优）将 Deep Research 提升到约 75%。Calibration Error：Deep Research 91%（最高）、GPT-4o w/ browsing 82%、GPT-4o 69%。
- **设计原则**：(i) "easy to verify, hard to solve"的逆向构建范式；(ii) 领域多样性通过训练师个人兴趣自然达成；(iii) 防泄漏——包含 canary string、禁止公开发布示例；(iv) 测试时计算扩展——通过 Best-of-N 和投票策略展示性能随计算量平滑扩展。

## 关键数字
| 指标 | 值 |
|------|-----|
| 问题总数 | 1,266 |
| 原始问题数 | 1,287（移除 21 个标签错误）|
| 人类 2h 内解决率 | 29.2%（367/1255）|
| 人类答案一致率 | 86.4% |
| GPT-4o 准确率 | 0.6% |
| GPT-4o w/ browsing | 1.9% |
| GPT-4.5 准确率 | 0.9% |
| OpenAI o1 准确率 | 9.9% |
| Deep Research 准确率 | 51.5% |
| Deep Research Best-of-64 | 图示约 75% |
| GPT-4o Calibration Error | 69% |
| Deep Research Calibration Error | 91% |
| 彻底解决的任务（pass@64=100%）| 16% |
| 完全失败的任务（pass@64=0%）| 14% |
| 最佳聚合策略 | Best-of-N（基于置信度）|

## 设计哲学
- **"逆向构建"方法论创新**：训练师从已确认事实出发反向设计问题，确保 (a) 100% 存在正确答案、(b) 答案简单可验证、(c) 搜索空间极大。这规避了传统 QA 基准"正问题容易、反问题无法构建"的困境。
- **"编程竞赛类比"框架**：明确将 BrowseComp 类比为编程竞赛——衡量的是核心能力的不完全但有用的代理指标。这种诚实定位避免了过度宣称。
- **校准度作为伴随评估**：具备浏览能力的模型在该任务上出现更高校准误差（Deep Research Calibration Error 91%，GPT-4o w/ browsing 82%），说明工具访问可能放大错误答案中的过度自信。反映了对"智能体应知其所不知"的重视。
- **测试时计算扩展的系统分析**：通过 Best-of-N 和投票策略展示性能随计算量平滑扩展，暗示浏览能力可通过工程手段显著改善，不单纯依赖模型能力提升。

## 局限性
- 仅测"找到单一精确答案"的能力，不测长回答、消歧、多模态信息检索（图像、视频、音频、交互式网页）。
- 无法保证参考答案是唯一正确答案（逆向构建的固有局限），尽管通过训练师领域熟悉度和多约束条件降低多解风险。
- 人类基线来自训练师群体（对数据集创建有一定熟悉度），不适合作为"普通人类"参考标准。2 小时限制可能导致可解决问题被放弃。
- 论文脚注说明 Deep Research 接触过专门训练其完成 BrowseComp 类任务的数据，因此与其他模型的横向比较可能存在训练目标差异。
- 高度专业化的领域问题可能无法推广到通用科学信息检索场景；网页内容可能随时间变化或消失。

## 核心贡献
BrowseComp 2025 的核心贡献是把"持续、深入、创造性网页浏览"这一 agent 能力转化为短答案、易验证、难求解的评测任务，并展示了浏览工具、推理策略、测试时计算和校准误差之间的关系。

## 与综述的关联
BrowseComp 测量的是科学发现工作流中的核心能力——深度信息检索与综合。科学发现始于对已有知识的大范围搜索和交叉验证，这正是 BrowseComp 所测的技能。它与 SimpleQA 同属 OpenAI simple-evals 系列——SimpleQA 测"模型是否知道事实"，BrowseComp 测"模型是否能找到事实"。在本综述中，BrowseComp 代表"科学文献/信息检索能力"这一评估维度，与 CORE-Bench（代码复现中的信息检索）和 AutoSurvey（文献综述生成中的检索环节）形成技术共鸣。
