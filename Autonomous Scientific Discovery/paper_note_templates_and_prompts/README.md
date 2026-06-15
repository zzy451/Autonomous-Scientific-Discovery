# Paper Note Templates and Prompts

本目录用于收录 `LLM Survey` 项目中已经验证过的论文阅读格式、提示词格式和综述组织格式，并在此基础上改造成适合 `Autonomous Scientific Discovery` 综述的工作模板。

## 一、目录结构

- `original_prompts/`：从 `LLM Survey` 复制来的原始论文阅读提示词。
- `original_format_examples/`：从 `LLM Survey` 复制来的代表性论文笔记、论文清单、章节草稿和覆盖检查样例。
- `ASD_single_paper_note_template.md`：后续记录每篇 Agent 文献的主模板。
- `ASD_survey_paper_note_template.md`：记录相关综述、taxonomy、benchmark 论文的模板。
- `ASD_paper_reading_prompt.md`：给模型或人工读论文时使用的 ASD 专用提示词。
- `ASD_survey_reading_prompt.md`：读综述论文、领域报告、benchmark paper 时使用的提示词。
- `ASD_paper_list_template.md`：维护候选文献池和纳入状态的表格模板。
- `ASD_section_scratch_template.md`：把大量论文笔记汇总为章节草稿时使用的模板。
- `ASD_coverage_check_template.md`：检查文献清单、笔记、分类和正文引用是否一致。
- `ASD_annotation_schema.md`：统一纳入状态、Agent 标签、科研流程角色、验证方式、证据强度和文件命名规则。

## 二、使用原则

1. 先判断论文是否属于 Agent 文献，不满足 Agent 纳入标准则不进入正式笔记库。
2. 主分类按科学研究对象归入封闭的 `01–11` 科学对象体系。
3. Agent 类型、科研流程角色、自主能力、验证方式和交叉属性只作为副标签。
4. 如果论文有具体科学对象，即使提出通用 ASD 系统，也按具体科学对象归类。
5. 领域无关型科研智能系统归入 `01.04`；科学系统与知识生产研究归入 `11.07`。

## 三、工作目录

项目根目录已经建立以下工作目录：

```text
Notes/
  01_Formal_Information_and_Computational_Sciences/
  02_Physics_Astronomy_and_Cosmic_Sciences/
  03_Chemical_Sciences/
  04_Materials_Science/
  05_Earth_and_Environmental_Sciences/
  06_Life_Sciences/
  07_Medical_and_Health_Sciences/
  08_Agricultural_Food_Forestry_Animal_and_Fishery_Sciences/
  09_Engineering_and_Industrial_Technology_Sciences/
  10_Aerospace_Marine_and_Transportation_Sciences/
  11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/
Paper_Lists/
Section_Scratch/
Coverage_Check/
Reference_PDF/
```

后续开始正式收集文献时，直接在这些目录下创建清单、笔记、章节草稿和覆盖检查报告。
