# GeneAgent 2025

## 基本信息
- **论文**: GeneAgent: Self-Verification Language Agent for Gene Set Knowledge Discovery Using Domain Databases
- **作者**: Zhizheng Wang, Qiao Jin, Chih-Hsuan Wei, Shubo Tian, Po-Ting Lai, Qingqing Zhu, Chi-Ping Day, Christina Ross, Zhiyong Lu
- **年份**: 2025
- **来源**: Nature Methods, doi:10.1038/s41592-025-02748-6; arXiv:2405.16205
- **关键词**: gene-set-analysis, self-verification, biomedical-agent, domain-database, hallucination-reduction

## 核心思想
GeneAgent 要解决的是 gene set knowledge discovery 中 LLM 生成生物过程解释时的可靠性问题。传统 GSEA 依赖已知数据库中的 enrichment terms，适合解释与既有功能强重叠的 gene sets；而对边缘重叠、较少研究的 gene sets，研究者希望发现新的潜在功能。标准 GPT-4 虽能生成 biological process name 和解释文本，但容易出现幻觉、不可控错误和不可复核的叙述。

论文的目标是把 LLM 的生成能力与专家策划数据库的事实验证结合起来，使 gene set 分析不仅能生成解释，还能通过数据库证据自我校验和修正。

## 方法细节
GeneAgent 是基于 GPT-4 的 self-verification language agent，核心工作流包含四步：

1. **Generation**：输入 gene set，先生成 biological process name 和 analytical narratives。
2. **Self-verification**：启动 selfVeri-Agent，从生成内容中抽取 claims，并用 gene names 调用生物医学数据库 Web APIs 获取参考功能。
3. **Modification**：根据 verification report 保留或修改 process name 与分析文本。
4. **Summarization**：汇总中间验证报告，输出最终 biological process name 和 gene-function narratives。

selfVeri-Agent 会优先验证 process name，再验证 analytical narratives，并在修改后的分析文本基础上再次检查 process name。论文称这种 cascade structure 相比普通 CoT 更强调 inference process 的可验证性。

GeneAgent 使用 **18 个 biomedical databases**，通过 **4 个 Web APIs** 访问，包括：

- g:Profiler / g:GOSt，用于 GO、KEGG、Reactome 等 enrichment terms；
- Enrichr，用于 pathway analysis；
- E-utils，用于 NCBI Gene 和 PubMed；
- CustomAPI，用于 gene-disease、gene-domain、PPI、gene-complex 等数据库。

评测时作者使用 masking strategy，避免某个数据集自己的数据库被直接用于验证自己的 gene sets。

## 关键结果

1. **1,106 个 gene sets 基准评测**  
   评测集来自三类来源：Gene Ontology **1,000** 个、NeST **50** 个、MSigDB **56** 个；gene set 大小从 **3 到 456**，平均 **50.67** 个 genes，reference terms 平均 **4.50** 个词。

2. **ROUGE 和语义相似度均优于 GPT-4**  
   在 MsigDB 上，GeneAgent 将 Rouge-L / Rouge-1 从 GPT-4 的 **23.9%** 提高到 **31.0%**，Rouge-2 从 **7.4%** 提高到 **15.5%**。MedCPT 语义相似度在三个数据集上分别达到 **0.705、0.761、0.736**，相对 GPT-4 有统计显著提升（p < 0.05）。

3. **高相似结果更多**  
   GeneAgent 生成相似度超过 90% 的结果有 **170** 个，GPT-4 为 **104** 个；超过 70% 的结果 GeneAgent 为 **614** 个，GPT-4 为 **545** 个。完全 100% 相似的结果 GeneAgent 为 **15** 个，GPT-4 为 **3** 个。

4. **背景分布 percentile 更高**  
   在 12,320 个背景 terms 中，GeneAgent 有 **76.9%（850/1106）** 的生成名称超过 90th percentile，GPT-4 为 **74.5%**；超过 98th percentile 的 gene sets，GeneAgent 超过 **675** 个，GPT-4 为 **598** 个；100th percentile 的结果 GeneAgent 为 **82** 个，GPT-4 为 **43** 个。

5. **verification report 可作为更好的 gene-function synopsis**  
   在 MSigDB 56 个 gene sets 上，用 GeneAgent verification reports 作为 synopsis 时，LLM 生成的 enrichment terms 中 **80.7%（296/367）** 与 g:Profiler 显著 enrichment terms 精确匹配；使用 SPINDOCTOR ontological synopsis 为 **68.8%（282/410）**，无 synopsis 为 **56.0%（195/348）**。作者将未匹配项视为潜在 hallucination，因此 GeneAgent 未匹配比例为 **19.3%**。

6. **self-verification 覆盖大部分 claims**  
   GeneAgent 生成 **15,903** 个 claims，其中 **15,848（99.6%）** 成功验证：**84% supported**、**1% partially supported**、**8% refuted**、**7% unknown**。未被支持的 claims 占 **16%**，分布在 **794** 个 gene sets 中，其中 **703（88.5%）** 后续被修改。

7. **人工核查 self-verification 决策**  
   作者随机选取 NeST 中 **10** 个 gene sets，共 **132** 个 claims 进行人工检查；GeneAgent 给出的 132 个决策中，人工确认 **92%（122）** 正确。

8. **B2905 melanoma case study**  
   作者将 GeneAgent 应用于 mouse B2905 melanoma cell lines 的 **7** 个 novel gene sets，gene 数为 **19 到 49**。专家评价显示 GeneAgent 在 process names 和 analytical narratives 上优于 GPT-4，并能给出与 mitochondrial respiratory chain complexes、neurodegeneration 等相关的更细粒度解释。

## 与综述的关联

GeneAgent 是科学发现 Agent 中 **Knowledge Grounding + Verification** 的直接证据。它不是完整自动科研系统，但它清楚展示了 biomedical agent 如何通过 domain databases 验证 LLM 生成的科学解释，并把幻觉检测嵌入生成-修改-总结流程。

在 Scientific Workflow 中，它覆盖 Knowledge Grounding、Result Analysis、Verification，并间接支持 Hypothesis Generation，因为 gene set 功能解释本身就是机制假设的前置步骤。

在 Skill Lifecycle 中，它对应：

- Representation：claims、process names、analytical narratives 是可验证的知识单元。
- Retrieval：通过 g:Profiler、Enrichr、E-utils、CustomAPI 检索 curated biomedical knowledge。
- Composition：generation -> verification -> modification -> summarization 的级联工作流。
- Execution：自动调用 Web APIs 与后端数据库。
- Evolution：unsupported claims 被用于修改输出，形成局部自我修正。
- Verification：数据库证据、人工核查、masking strategy 和 case study。

Evidence Role 应标为 **Direct**。它直接支持“scientific agent 的可靠性来自可追溯证据和领域数据库，而不是单纯 LLM 自信输出”这一点。

## 局限性

- 只使用 GPT-4 作为 backbone，未系统评估 GPT-3.5、Gemini、Llama 等模型在同一 agent 框架下的表现。
- 虽然 self-verification 有效，GeneAgent 仍可能生成与 reference terms 差异较大的 process names。
- 错误分析显示，失败主要来自错误拒绝正确 process name，或错误支持本来不相似的 process name；作者认为可通过更多相关数据库和更有效的 modification prompts 缓解。
- 系统没有预处理 gene set，例如去除与其他 genes 不一致的 outlier genes。
- 任务仍是 gene set interpretation，不等同于湿实验验证或完整机制发现。

## 核心贡献

GeneAgent 的核心贡献是把 gene set 功能解释变成一个可检索、可验证、可修正的 agent workflow，用 18 个生物医学数据库和 self-verification 机制显著降低标准 GPT-4 在基因集分析中的幻觉风险。
