# Notes 目录说明

## 笔记模板

本目录的论文笔记格式仿照 `LLM Survey/Notes`：不使用 YAML frontmatter，而是在文档开头使用一级标题和“基本信息”块。正文标题应尽量简洁、语义化，不使用 `0. / 1. / 2.` 这类顶层编号。

### 模板 A：系统/方法论文

```markdown
# {论文简称或核心题名}

## 基本信息
- **论文**: {论文标题}
- **作者**: {作者}
- **年份**: {年份}
- **来源**: {arXiv ID、会议或 DOI}
- **关键词**: {标签}

## 核心思想
这篇论文要解决什么问题？为什么之前的方法不够？

## 方法细节
提出了什么方案？核心机制是什么？workflow 如何运行？

## 关键结果
最重要的实验结果是什么？关键数字是什么？

## 局限性
作者承认的局限，以及我们需要注意的边界。

## 核心贡献
一句话说明这篇论文最不可忽视的贡献。

## 与综述的关联
这个工作在我们的框架中处于什么位置？和哪些其他论文互补、对照或构成边界？
```

### 模板 B：基准/评测论文

```markdown
# {基准简称}

## 基本信息
- **论文**: {论文标题}
- **作者**: {作者}
- **年份**: {年份}
- **来源**: {arXiv ID、会议或 DOI}
- **关键词**: benchmark, {其他标签}

## 核心思想
这个基准为什么被提出？它试图补上什么评测空白？

## 评测目标
这个基准测什么能力？

## 基准设计
- 题目数量/来源/难度分级
- 评分方式
- 人类基线 vs AI 基线

## 关键数字
| 指标 | 数值 |
|---|---:|
| ... | ... |

## 设计哲学
这个基准的独特设计选择反映了什么价值观？

## 局限性
什么重要能力没有被测到？

## 与综述的关联
它支撑、约束或反驳综述中的哪个论点？
```

## 子目录说明

| 目录 | 内容 |
|------|------|
| `systems/` | ARA, SkillOS, SSL, AI Scientist 等核心系统 |
| `benchmarks/` | PaperBench, GAIA, MLE-Bench 等基准测试 |
| `memory/` | MemGPT, Collaborative Memory 等记忆系统 |
| `skills-ecosystem/` | Voyager, AWM, Reflexion 等 Skill 生态论文 |
| `verification/` | OpenScholar, LLM-as-a-Verifier 等验证系统 |
| `surveys/` | CUHK-Shenzhen Survey 等相关综述 |
| `cognitive-architectures/` | 认知姿态、推理框架、多智能体辩论 |
| `infrastructure/` | W3C PROV, RO-Crate, MLflow 等标准与基础设施 |

## 命名规范

每篇论文一个文件：`{Author}_{Year}_{ShortName}.md`
- 示例：`Shazeer_2020_SwiGLU.md`
- 示例：`Mialon_2023_GAIA.md`
