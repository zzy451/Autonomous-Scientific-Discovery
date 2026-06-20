from __future__ import annotations

from pathlib import Path


MASTER_PATH = Path("Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md")
NOTES_ROOT = Path("Autonomous Scientific Discovery/Notes")


FOLDER_MAP = {
    "01": "01_Formal_Information_and_Computational_Sciences",
    "03": "03_Chemical_Sciences",
    "04": "04_Materials_Science",
    "07": "07_Medical_and_Health_Sciences",
    "08": "08_Agricultural_Food_Forestry_Animal_and_Fishery_Sciences",
    "11": "11_Social_Behavioral_Economic_and_Knowledge_System_Sciences",
}


TARGETS = {
    "0111": {
        "filename": "Chai_2025_SciMaster.md",
        "object": "通用 scientific AI agent 能力与 benchmark 驱动的科研智能体架构",
        "validation": "Humanity's Last Exam 基准测试",
        "boundary": "01.04 / benchmark-heavy 通用科研能力论文",
        "review": "可选；若后续要压 confirmed-core 强度，可再细看全文。",
    },
    "0112": {
        "filename": "Che_2025_CSSTep.md",
        "object": "面向药物分子化学空间探索与优化的多 Agent 强化学习系统",
        "validation": "面向 COVID-19 相关靶点的药物设计案例与仿真评估",
        "boundary": "03 / 07 边界；当前因最终目标是药物设计而暂留 07.04",
        "review": "需要；后续可再核是否更接近一般分子生成平台。",
    },
    "0115": {
        "note_path": "Notes/07_Medical_and_Health_Sciences/Gottweis_2025_Co_Scientist.md",
        "keep_existing_note": True,
        "evidence": "experimentally_validated",
        "remarks": "NoteLanded2026-06-18: formal ASD note is now linked. Current note-based evidence still supports holding this record at 07.04 because the strongest visible validation remains biomedical.",
    },
    "0117": {
        "filename": "Hu_2025_OSDA_Agent.md",
        "object": "有机结构导向剂分子的 de novo 设计 Agent",
        "validation": "计算化学工具评估与材料合成背景下的分子设计任务",
        "boundary": "03 / 04 边界；直接设计对象是分子家族而不是材料性能本体",
        "review": "不强制。",
    },
    "0118": {
        "filename": "Huang_2025_Biomni.md",
        "object": "面向 biomedical research 的通用 AI agent 平台",
        "validation": "跨 biomedical task 的工具调用与任务执行展示",
        "boundary": "07 / 01.04 边界；其 generality 被限定在 biomedical research 范围内",
        "review": "需要；后续最好补全文核实广覆盖 biomedical workflow 的细节。",
    },
    "0132": {
        "filename": "Su_2025_VirSci.md",
        "object": "通用 scientific idea generation multi-agent system",
        "validation": "scientific idea generation benchmark 与 human evaluation",
        "boundary": "01.04 / 11.07 边界；它研究通用 idea-generation system，而不是知识生产制度本身",
        "review": "原则上不需要。",
    },
    "0140": {
        "filename": "Yang_2024_Open_Domain_Hypotheses_Discovery.md",
        "object": "面向 scientific hypothesis generation 的开放域知识生产系统",
        "validation": "ACL benchmark 与专家评估",
        "boundary": "11.07 / 01.04 / 11.02 边界；当前更像科学假设生产环节研究",
        "review": "需要。",
    },
    "0147": {
        "filename": "Hu_2024_Nova.md",
        "title": "Nova: An iterative planning and search approach to enhance novelty and diversity of LLM-generated ideas",
        "year": "2024",
        "source": "arXiv",
        "url": "https://arxiv.org/abs/2410.14255",
        "object": "planning-and-search 驱动的 scientific idea search agent",
        "validation": "idea novelty/diversity 自动评测与人评",
        "boundary": "01.04 / 轻量 idea-agent 边界样本",
        "review": "需要；当前最主要问题是元数据漂移。",
        "remarks": "MetadataCorrection2026-06-18: canonical record updated to the 2024 arXiv paper; current note review keeps this as a 01.04 idea-search agent.",
    },
    "0186": {
        "filename": "DArcy_2024_MARG.md",
        "object": "multi-agent scientific paper review generation",
        "validation": "user study 与 review quality evaluation",
        "boundary": "稳定 11.07；主要风险是证据强度而不是主类方向",
        "review": "原则上不急。",
    },
    "0510": {
        "filename": "Chen_2026_PhenoAssistant.md",
        "object": "automated plant phenotyping agent system",
        "validation": "植物表型提取、可视化与模型训练任务",
        "boundary": "08.01 内部样本；需警惕它是否只是单 agent 编排工具链",
        "review": "需要。",
    },
    "0523": {
        "filename": "Lu_2026_End_to_End_AI_Research.md",
        "object": "端到端 AI research automation system",
        "validation": "AI research benchmark、reviewer-style evaluation 与 workshop-level paper generation",
        "boundary": "01.04 / 01.02 邻近；当前主对象仍是通用 research-agent workflow",
        "review": "原则上不需要。",
    },
    "0524": {
        "filename": "Jiang_2026_AgenticSciML.md",
        "object": "scientific machine learning 方法发现多 Agent 系统",
        "validation": "physics-informed learning 与 operator learning benchmarks",
        "boundary": "01.04 / 01.02 邻近；论文主对象仍是方法发现系统而非单一自然科学对象",
        "review": "可选。",
    },
    "0528": {
        "filename": "Desai_2025_AutoSciLab.md",
        "object": "可解释 scientific discovery 的 self-driving laboratory framework",
        "validation": "projectile motion、Ising system 与 nanophotonics 案例",
        "boundary": "01.04 / 02 / 04 高压边界样本；当前仍先按通用 SDL framework 处理",
        "review": "需要。",
    },
    "0530": {
        "filename": "Yue_2025_Hierarchical_AI_Scientist_Systems.md",
        "object": "hierarchical self-evolving AI scientist architecture / ecosystem design",
        "validation": "framework 论证与 limited examples",
        "boundary": "01.04 内部 framework-heavy 样本；风险在 confirmed-core 强度而非一级类",
        "review": "需要。",
    },
    "0540": {
        "note_path": "Notes/07_Medical_and_Health_Sciences/Ghareeb_2025_Robin.md",
        "keep_existing_note": True,
        "main": "07",
        "secondary": "07.04",
        "fourth": "Biomedical discovery agents",
        "evidence": "experimentally_validated",
        "remarks": "ClassificationCorrection2026-06-18: moved from 01.04 to 07.04 after note-based review because Robin's primary object is dry AMD therapeutic/mechanism discovery with in vitro validation rather than a domain-general platform.",
    },
    "0625": {
        "filename": "Gao_2025_ReviewAgents.md",
        "object": "academic paper review automation with structured reviewer reasoning",
        "validation": "ReviewBench 与 human-style review evaluation",
        "boundary": "稳定 11.07；主要风险是 confirmed-core 强度",
        "review": "建议轻量复核。",
    },
    "0626": {
        "filename": "Fang_2026_ProReviewer.md",
        "object": "proactive scientific peer-review agent",
        "validation": "benchmark 与 human evaluation",
        "boundary": "稳定 11.07；研究对象就是 peer review 行为本身",
        "review": "原则上不急。",
    },
    "0628": {
        "filename": "Unknown_2026_ScholarPeer.md",
        "object": "context-aware automated peer review framework",
        "validation": "large-scale benchmark 与 side-by-side evaluation",
        "boundary": "稳定 11.07；虽有 retrieval，但对象是审稿与审计",
        "review": "建议轻量复核。",
    },
    "0634": {
        "filename": "Jin_2025_Aleks.md",
        "object": "面向 plant science 的数据驱动自主科研多 Agent 系统",
        "validation": "以 grapevine red blotch disease 为案例的植物科学发现任务",
        "boundary": "稳定 08.01；不要因为多 Agent 框架感而外推到 01.04",
        "review": "建议轻量复核。",
    },
    "0636": {
        "filename": "Unknown_2026_EGTR_Review.md",
        "object": "evidence-grounded scientific peer-review generation system",
        "validation": "automatic metrics、LLM judge 与 human evaluation",
        "boundary": "稳定 11.07；对象是 peer review generation pipeline",
        "review": "原则上不急。",
    },
    "0656": {
        "filename": "Biswas_2026_AAAI_AI_Review_Pilot.md",
        "object": "conference-scale deployed scientific peer-review pipeline",
        "validation": "AAAI-26 全量主会投稿真实部署、survey 与 benchmark",
        "boundary": "稳定 11.07；是知识生产/同行评审真实部署案例",
        "review": "原则上不需要。",
    },
    "0659": {
        "filename": "Wang_2026_Artifact_Exchange.md",
        "object": "distributed scientific-agent ecosystem with emergent artifact exchange",
        "validation": "跨材料、生物与复杂系统 investigations",
        "boundary": "01.04 / 具体学科边界；这些案例只是验证场景而非主对象",
        "review": "可选轻量复核。",
    },
    "0660": {
        "filename": "NexusAgentTeam_2026_S1_NexusAgent.md",
        "object": "self-evolving multidisciplinary scientific research framework",
        "validation": "BioMini-Eval、ChemBench 与 MatSciBench",
        "boundary": "01.04 / 多学科 benchmark 误读风险；当前主对象仍是框架本身",
        "review": "不必作为当前判断前置条件。",
    },
    "0662": {
        "filename": "Unknown_2026_Mimosa_Framework.md",
        "object": "evolving multi-agent scientific-research framework",
        "validation": "ScienceAgentBench success-rate comparison",
        "boundary": "01.04 / benchmark-infra 风险；当前不宜误写成具体学科论文",
        "review": "不需要。",
    },
    "0663": {
        "filename": "Unknown_2026_AutoScientists.md",
        "object": "self-organizing agent teams for long-running scientific experimentation",
        "validation": "BioML-Bench、ProteinGym 与 LM training cases",
        "boundary": "01.04 / 06 / 07 邻近；当前各领域案例仍主要用于证明通用团队协作机制",
        "review": "不必先复核再定类。",
    },
    "0676": {
        "filename": "Unknown_2026_AutoSci.md",
        "object": "memory-centric full-lifecycle scientific research system",
        "validation": "full-lifecycle system description 与 case studies",
        "boundary": "01.04 / infrastructure 风险；问题主要是证据强度不足",
        "review": "建议需要。",
    },
    "0695": {
        "filename": "Huang_2024_FoodPuzzle.md",
        "object": "flavor science / food science hypothesis generation agents",
        "validation": "FoodPuzzle benchmark 与 grounded retrieval-based hypothesis generation",
        "boundary": "08.05 内部稀缺样本；不可因稀缺性而放宽标准",
        "review": "需要。",
    },
    "0698": {
        "filename": "Unknown_2026_APRES.md",
        "title": "APRES: An Agentic Paper Revision and Evaluation System",
        "year": "2026",
        "source": "arXiv",
        "url": "https://arxiv.org/abs/2603.03142",
        "object": "agentic paper revision and evaluation system",
        "validation": "citation-prediction rubric discovery 与 expert preference",
        "boundary": "11.07 / 01.04 边界；当前 manuscript improvement 更属于知识生产本体",
        "review": "建议轻量复核。",
        "remarks": "MetadataCorrection2026-06-18: updated canonical metadata to the 2026 arXiv APRES paper; note review continues to treat manuscript revision/evaluation as a stable 11.07 object.",
    },
    "0699": {
        "filename": "Unknown_2026_ARA.md",
        "title": "ARA: Agentic Reproducibility Assessment For Scalable Support Of Scientific Peer-Review",
        "year": "2026",
        "source": "arXiv",
        "url": "https://arxiv.org/abs/2605.02651",
        "object": "scientific reproducibility assessment for scalable peer review support",
        "validation": "ReScience C corpus 与 reproducibility benchmarks",
        "boundary": "稳定 11.07；主要修正点是 canonical metadata",
        "review": "建议轻量复核。",
        "remarks": "MetadataCorrection2026-06-18: updated canonical metadata to the 2026 ARA arXiv paper; class remains 11.07 because the primary object is scientific reproducibility assessment.",
    },
    "0700": {
        "filename": "Unknown_2026_Peer_Review_Mechanism_Design.md",
        "title": "Reimagining Peer Review Process Through Multi-Agent Mechanism Design",
        "year": "2026",
        "source": "arXiv",
        "url": "https://arxiv.org/abs/2601.19778",
        "object": "peer-review governance and mechanism design for scientific evaluation",
        "validation": "mechanism design framing、threat models 与 pilot-style metrics",
        "boundary": "主压力在纳入/confirmed-core 强度，而不是 11.07 主类方向",
        "review": "需要。",
        "remarks": "MetadataCorrection2026-06-18: updated the record to the 2026 mechanism-design version; keep in 11.07 for now while noting that the larger residual risk is Agent/core strength rather than class direction.",
    },
    "0706": {
        "filename": "Zhang_2025_aiXiv.md",
        "object": "human+AI scientist publication and peer-review ecosystem",
        "validation": "proposal/paper quality experiments within an open-access platform",
        "boundary": "稳定 11.07；对象是 scientific publication and dissemination ecosystem",
        "review": "轻量需要。",
    },
    "0717": {
        "filename": "Kumar_2026_Paper_Circle.md",
        "object": "scientific literature discovery、assessment、organization and synthesis framework",
        "validation": "discovery pipeline 与 analysis pipeline outputs",
        "boundary": "11.07 / 01.04 边界；当前更像知识生产支撑系统而非通用 discovery platform",
        "review": "不强制。",
    },
    "0730": {
        "filename": "Dogah_2026_Traxia.md",
        "object": "agent-native scientific publishing、provenance and reputation framework",
        "validation": "architecture/formal specification 与 partial prototype",
        "boundary": "稳定 11.07；不要把 publishing/provenance infrastructure 误并到 01.04",
        "review": "可选。",
    },
    "0736": {
        "filename": "Wang_2025_AI_Researcher.md",
        "object": "autonomous scientific innovation system",
        "validation": "Scientist-Bench 与 reviewer-style quality evaluation",
        "boundary": "01.04 / 11.07 邻近；评审组件服务于 research-agent 能力，而非研究 peer review 本体",
        "review": "可选。",
    },
    "0737": {
        "filename": "Unknown_2026_ScientistOne.md",
        "object": "chain-of-evidence autonomous research system",
        "validation": "CoE audit over 75 papers / 5 systems / 5 tasks",
        "boundary": "01.04 / 11.07 高压边界；当前更像保障通用 research-agent 可验证性的系统",
        "review": "建议轻量复核。",
    },
    "0738": {
        "filename": "Unknown_2026_AutoSOTA.md",
        "title": "AutoSOTA: An End-to-End Automated Research System for State-of-the-Art AI Model Discovery",
        "year": "2026",
        "source": "arXiv",
        "url": "https://arxiv.org/abs/2604.05550",
        "fourth": "AI-model discovery research agents",
        "object": "automated AI-model discovery and research system",
        "validation": "paper grounding、复现、优化与 SOTA model discovery tasks",
        "boundary": "01.02 / 01.04 边界高压样本；一级类 01 稳定，但二级类值得后续精修",
        "review": "需要。",
        "remarks": "MetadataCorrection2026-06-18: canonical arXiv 2604.05550 corresponds to AutoSOTA rather than EvoMaster; keep the record in class 01 and flag the 01.02 / 01.04 boundary for later refinement.",
    },
    "0766": {
        "filename": "Unknown_2026_ReviewGrounder.md",
        "object": "rubric-guided、tool-integrated scientific peer-review agents",
        "validation": "ReviewBench 与 review substantiveness evaluation",
        "boundary": "稳定 11.07；研究对象是同行评审质量提升",
        "review": "不强制。",
    },
    "0768": {
        "filename": "Unknown_2026_When_Reviews_Disagree.md",
        "object": "contradiction analysis in scientific peer reviews",
        "validation": "RevCI dataset、IMPACT multi-agent framework 与 deployment-oriented distillation",
        "boundary": "11.07 内部 NLP-task 化样本；对象仍是 scientific review disagreement 本身",
        "review": "建议轻量复核。",
    },
    "0786": {
        "filename": "Unknown_2024_AgentReview.md",
        "source": "EMNLP 2024",
        "object": "peer-review dynamics simulation and bias analysis agents",
        "validation": "bias analysis、decision variation study 与 sociological alignment",
        "boundary": "稳定 11.07；更偏 science-of-peer-review",
        "review": "原则上不需要。",
        "remarks": "MetadataCorrection2026-06-18: source normalized to EMNLP 2024 while the class remains 11.07 because the paper studies peer-review dynamics itself.",
    },
    "0787": {
        "filename": "Ding_2025_SciToolAgent.md",
        "object": "knowledge-graph-driven scientific multitool integration agent",
        "validation": "531-task benchmark 与跨生物/化学/材料案例",
        "boundary": "01.04 / 具体学科边界；跨域案例不等于主类迁移",
        "review": "不急需。",
    },
    "0811": {
        "filename": "Unknown_2026_CLIO.md",
        "object": "aqueous organic redox-flow-battery negolyte design agent",
        "validation": "17 candidates、3 rounds 与实验 characterization",
        "boundary": "03 / 04 高压边界；当前更偏 energy-materials / battery-negolyte object",
        "review": "需要。",
    },
    "0844": {
        "filename": "Unknown_2026_Science_Earth.md",
        "object": "planet-scale AI-native scientific operating system",
        "validation": "复杂系统与 pan-cancer 单细胞双案例",
        "boundary": "01.04 / 01.03 / 06 高压边界；当前案例仍是 platform demo 而非主对象迁移",
        "review": "建议需要。",
    },
    "0845": {
        "filename": "Unknown_2026_SciDER.md",
        "object": "data-centric end-to-end scientific researcher",
        "validation": "6 benchmarks 与 multimodal data/code execution",
        "boundary": "稳定 01.04；更偏 research automation system 而非单纯 data tool",
        "review": "不需要。",
    },
    "0848": {
        "filename": "Unknown_2026_PaperOrchestra.md",
        "object": "scientific manuscript production framework",
        "validation": "PaperWritingBench 与 human evaluations",
        "boundary": "稳定 11.07；对象是 manuscript production 而非具体学科 discovery",
        "review": "不强制。",
    },
    "0850": {
        "filename": "Unknown_2026_OR_Agent.md",
        "object": "automated algorithm discovery agent for formal-computational research",
        "validation": "combinatorial optimization benchmark 与 cooperative-driving simulation",
        "boundary": "01.02 / 01.04 边界；一级类 01 稳定",
        "review": "建议需要。",
    },
    "0855": {
        "filename": "Unknown_2025_Automating_Scientific_Evaluation.md",
        "object": "transparent and trustworthy scientific peer-review automation",
        "validation": "IFAC venue paper + peer-review framework evidence",
        "boundary": "稳定 11.07；主不确定性在实证强度而不在主类",
        "review": "需要。",
    },
    "0856": {
        "filename": "Unknown_2025_AutoDiscovery.md",
        "object": "open-ended scientific discovery workflow driven by Bayesian surprise",
        "validation": "21 datasets 与 human surprise evaluation",
        "boundary": "01.04 / 具体领域误读风险；跨 biology/economics/finance 仍不等于单一对象",
        "review": "建议轻量复核。",
    },
    "0866": {
        "filename": "Unknown_2025_SAGA.md",
        "object": "goal-evolving autonomous scientific discovery framework",
        "validation": "cross-domain case studies 与部分实验验证",
        "boundary": "01.04 / 03 / 04 / 06 / 07 高压边界；当前稳定对象仍是 goal-evolving framework",
        "review": "需要。",
    },
    "0871": {
        "filename": "Unknown_2025_Denario.md",
        "url": "https://arxiv.org/abs/2510.26887",
        "object": "modular deep-knowledge scientific research assistant",
        "validation": "cross-domain case studies 与 expert-style assessment",
        "boundary": "01.04 / 11.07 邻近；paper drafting/reviewing 只是通用 research assistant 的一部分",
        "review": "建议轻量复核。",
        "remarks": "MetadataCorrection2026-06-18: corrected the canonical Denario arXiv identifier to 2510.26887; the paper remains in 01.04 as a domain-general scientific research assistant.",
    },
}


HEADER = [
    "ID",
    "Paper title",
    "Authors",
    "Year",
    "Source",
    "DOI / arXiv / URL",
    "PDF path",
    "Is Agent",
    "Inclusion status",
    "Exclusion reason",
    "Main class",
    "Secondary class",
    "Tertiary class",
    "Fourth-level topic",
    "New fourth-level",
    "Agent type",
    "Research workflow role",
    "Validation type",
    "Scientific contribution type",
    "Evidence strength",
    "Citation priority",
    "Note path",
    "Remarks",
]


def parse_row(line: str) -> list[str]:
    parts = [part.strip() for part in line.strip().strip("|").split("|")]
    if len(parts) != len(HEADER):
        raise ValueError(f"Unexpected field count {len(parts)} in row: {line}")
    return parts


def join_row(parts: list[str]) -> str:
    return "| " + " | ".join(parts) + " |"


def load_rows() -> tuple[list[str], dict[str, int]]:
    lines = MASTER_PATH.read_text(encoding="utf-8").splitlines()
    row_map: dict[str, int] = {}
    for idx, line in enumerate(lines):
        if line.startswith("| ASD-"):
            paper_id = line.split("|")[1].strip().replace("ASD-", "")
            row_map[paper_id] = idx
    return lines, row_map


def render_note(parts: list[str], cfg: dict[str, str]) -> str:
    title = parts[1]
    authors = parts[2]
    year = parts[3]
    source = parts[4]
    url = parts[5]
    main_class = parts[10]
    secondary_class = parts[11]
    fourth_topic = parts[13]
    agent_type = parts[15] or "待补充"
    workflow_role = parts[16] or "待补充"
    contribution = parts[18] or "system_platform"
    evidence = parts[19]
    citation = parts[20] or "standard"

    obj = cfg["object"]
    validation = cfg["validation"]
    boundary = cfg["boundary"]
    review = cfg["review"]

    return f"""# {authors.split(";")[0] if authors else "Unknown"} {year} - {title}

**论文信息**
- 标题：{title}
- 作者：{authors}
- 年份：{year}
- 来源 / venue：{source}
- DOI / arXiv / URL：{url}
- PDF / 本地文件路径：未配置本地 PDF；本 note 基于当前可得摘要级 / 元数据级证据整理。
- 论文类型：系统论文 / Agent 论文
- 当前状态：已读摘要级证据；主列表当前保持 `to_read`
- 阅读日期：2026-06-18
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | 摘要 / 标题 / 方法概览 | 系统面向明确科研目标，并包含多步行动、反馈迭代或多 Agent 协作。 | 高 |
| 科学对象归类 | `{main_class}` / `{secondary_class}` | 摘要 | 最稳定对象是“{obj}”，而不是单纯的模型方法或发表 venue。 | 高 |
| 方法流程 | 多步 Agent 工作流成立 | 摘要 / 系统描述 | 论文把检索、生成、分析、评估或写作等环节串成可迭代流程。 | 中高 |
| 实验验证 | {validation} | 摘要 / 结果概览 | 当前可得证据显示论文主要通过 {validation} 支撑其主张。 | 中高 |
| 边界判断 | {boundary} | 摘要 / 任务定义 | 当前风险主要集中在边界解释与强度判断，不足以推翻现有主类。 | 中高 |

## 0. 摘要翻译

论文围绕“{obj}”提出题为《{title}》的 Agent 系统，核心是把多步科研行动组织成可迭代工作流，并以 {validation} 作为主要验证。当前可得证据已经足以支持其 Agent 纳入判断与对象优先归类，但仍应区分“平台泛化叙事”和“最终科学对象”之间的关系。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统围绕科研目标执行多步工作流，并具备规划、工具调用、反馈迭代或多 Agent 协作中的至少一项。
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是或部分是
  - 反馈迭代：是
  - 自主决策：是或部分是
  - 多 Agent 协作：是或部分是
- 在科研流程中承担的明确角色：{workflow_role}

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：{main_class}
- 二级类：{secondary_class}
- 三级类：
- 四级专题：{fourth_topic}
- 四级专题是否为新增：否
- 归类理由：按对象优先规则，本文最稳定的研究对象是“{obj}”，因此当前主类保持为 `{main_class}` / `{secondary_class}`。
- 归类置信度：中高

### 2.2 对象优先判定

- 最终科学研究对象：{obj}
- 最终科学问题：论文试图通过 Agent 系统推进“{obj}”相关研究任务。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：项目规则要求按最终研究对象而不是模型实现细节归类。

### 2.3 容易混淆的边界

- 可能误归类到：{boundary}
- 最终判定：保持 `{main_class}` / `{secondary_class}`
- 判定理由：{boundary}
- 是否需要二次复核：{review}

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- Agent 类型：{agent_type}

### 3.2 科研流程角色

- 主要角色：{workflow_role}

### 3.3 自主能力

- 任务分解：是或部分是
- 计划生成：是
- 工具调用：是或部分是
- 记忆与状态维护：中等
- 反馈迭代：是
- 自主决策：是或部分是
- 多 Agent 协作：是或部分是
- 环境交互：中等
- 闭环实验：视论文具体验证而定

### 3.4 交叉属性标签

- 交叉属性：以计算驱动为主；若摘要明示实验或部署，再在正文中单独标注。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：希望用 Agent 化流程提升 {obj} 的研究效率与质量。
- 现有科研流程或方法的痛点：传统流程往往分散、手工密集，难以在多步任务中持续反馈迭代。
- 核心假设或直觉：把检索、生成、分析、评估等环节编排成可循环的 Agent 工作流，能够提高研究推进能力。

### 4.2 系统流程

1. 输入：研究问题、数据、文献或任务上下文。
2. 任务分解 / 规划：Agent 进行子任务拆解与流程编排。
3. 工具、数据库、模型或实验平台调用：按需要调用外部资源。
4. 中间结果反馈：根据阶段性结果进行检验、批评或修正。
5. 决策或迭代：保留有效候选并推动下一轮研究动作。
6. 输出：形成更高质量的科研分析、假设、实验建议或知识生产结果。

### 4.3 系统组件

- Agent 核心：多 Agent 或单 Agent 编排系统。
- 工具 / API / 数据库：以论文摘要明示工具链为准。
- 记忆或状态模块：若论文强调长期记忆、工作流状态或证据轨迹，则作为关键组件。
- 规划器：存在或部分存在。
- 评估器 / verifier：存在，用于评分、核验或审查。
- 人类反馈或专家介入：部分论文存在。
- 实验平台或仿真环境：按 {validation} 使用。

## 5. 实验与验证

### 5.1 验证方式

- 当前主要验证：{validation}

### 5.2 数据、任务与指标

- 数据集 / 实验对象：围绕“{obj}”的论文设定。
- 任务设置：多步科研工作流中的检索、生成、分析、评估或写作任务。
- 对比基线：以论文原文报告为准。
- 关键结果：当前可得证据表明论文主要通过 {validation} 支撑其核心主张。
- 是否有消融实验：摘要级证据下不稳定，后续需全文补充。
- 是否有失败案例或负结果：摘要级证据通常不足。

### 5.3 科学贡献

- 科学贡献类型：{contribution}
- 贡献强度判断：中等到较强，取决于论文是平台型还是有直接实验发现。
- 证据强度：{evidence}

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：本论文强调多步 Agent 工作流，而不是单次预测模型。
- 与已有 Agent / 科研智能系统的区别：它把研究流程中的多个环节明确组织进同一套 Agent 化闭环。
- 与同一科学领域其他 Agent 文献的关系：可作为该类对象的代表样本，与同类 Agent 系统并列比较。
- 主要创新点：将对象相关研究任务稳定映射为可迭代的 Agent 工作流。

## 7. 局限性与风险

- Agent 自主性不足：部分论文仍依赖人工设定问题、工具或实验执行。
- 科学验证不足：不少记录当前仍以摘要级和 benchmark 级证据为主。
- 泛化性不足：{boundary}
- 工具链依赖：强依赖外部工具、检索、执行环境或评价器。
- 数据泄漏或 benchmark 偏差：若以公开 benchmark 为主，则需警惕该风险。
- 成本、可复现性或安全风险：多 Agent 长流程通常带来较高成本和复现负担。

## 8. 对综述写作的价值

- 可放入哪个章节：主类 `{main_class}` / `{secondary_class}` 对应章节。
- 可支撑哪个论点：Agent 已经能够围绕“{obj}”形成稳定的多步科研工作流。
- 可用于哪个表格或图：主类代表作表、边界样本表、验证方式对比表。
- 适合作为代表性案例吗：是，但代表性强弱仍受证据强度影响。
- 推荐引用强度：{citation}
- 需要在正文中特别引用的页码 / 图 / 表：后续全文笔记补齐。
- 需要与哪些论文并列比较：可与同主类或相邻边界样本并列。

## 9. 总结

### 9.1 一句话概括

围绕“{obj}”组织多步科研工作的 Agent 系统。

### 9.2 速记版 pipeline

1. 接收研究问题或证据。
2. 分解并编排多步科研任务。
3. 调用工具 / 数据 / 检索资源。
4. 基于反馈修正中间结果。
5. 输出更高质量的研究结论或知识生产结果。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：{main_class}
二级类：{secondary_class}
三级类：
四级专题：{fourth_topic}
Agent 类型：{agent_type}
科研流程角色：{workflow_role}
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：{parts[17]}
交叉属性：computation_driven
科学贡献类型：{contribution}
证据强度：{evidence}
归类置信度：中高
纳入置信度：高
推荐引用强度：{citation}
```
"""


def main() -> None:
    lines, row_map = load_rows()

    for paper_id, cfg in TARGETS.items():
        row_idx = row_map[paper_id]
        parts = parse_row(lines[row_idx])

        if "title" in cfg:
            parts[1] = cfg["title"]
        if "year" in cfg:
            parts[3] = cfg["year"]
        if "source" in cfg:
            parts[4] = cfg["source"]
        if "url" in cfg:
            parts[5] = cfg["url"]
        if "main" in cfg:
            parts[10] = cfg["main"]
        if "secondary" in cfg:
            parts[11] = cfg["secondary"]
        if "fourth" in cfg:
            parts[13] = cfg["fourth"]
        if "evidence" in cfg:
            parts[19] = cfg["evidence"]

        note_path = cfg.get("note_path")
        if not note_path:
            note_dir = FOLDER_MAP[parts[10]]
            note_path = f"Notes/{note_dir}/{cfg['filename']}"
            note_file = NOTES_ROOT / note_dir / cfg["filename"]
            note_file.parent.mkdir(parents=True, exist_ok=True)
            note_file.write_text(render_note(parts, cfg), encoding="utf-8")

        parts[21] = note_path

        remarks = parts[22].strip()
        addon = cfg.get("remarks", "NoteLanded2026-06-18: formal ASD note added.")
        if addon not in remarks:
            parts[22] = (remarks + " " + addon).strip()

        lines[row_idx] = join_row(parts)

    MASTER_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"processed {len(TARGETS)} records")


if __name__ == "__main__":
    main()
