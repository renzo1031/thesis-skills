# Thesis Skills

一个面向本科毕业论文/毕业设计的 Codex skill。目标是把“程序源码 + 学校模板 + 证据材料”整理成 AI 可执行的论文写作流程，让 AI 先建立标准、事实和证据索引，再按章节写论文。

核心 skill：`thesis-standardizer`

## 能做什么

- 根据学校论文模板、任务书、源码、数据库、接口、截图、测试报告生成论文资料包。
- 自动初始化 `thesis-ai-standard/`，包含标准配置、论文事实模板、图表登记表、评分表和 draw.io 图模板。
- 支持系统设计与实现、实验研究、调查分析、工程设计、文献综述等本科论文类型。
- 从 PDF 论文中抽取候选参考文献段落。
- 建立“章节论点 ↔ 可引用文献 ↔ PDF 来源”的文献交叉引用索引。
- 约束 AI 不编造功能、字段、接口、实验数据、测试结果、参考文献和学校规则。

## 安装

把 `thesis-standardizer/` 复制到 Codex skills 目录：

```powershell
Copy-Item -Recurse .\thesis-standardizer $env:USERPROFILE\.codex\skills\thesis-standardizer
```

重新打开 Codex 会话后，可以这样调用：

```text
Use $thesis-standardizer，根据我的程序源码和学校模板，先生成论文资料包，再规划本科论文目录。
```

## 快速初始化论文项目

在你的论文项目目录运行：

```powershell
python $env:USERPROFILE\.codex\skills\thesis-standardizer\scripts\init_thesis_workspace.py .
```

会生成：

```text
thesis-ai-standard/
  README.md
  01-本科论文标准化最佳实践.md
  02-公开标准与高校规范来源.md
  templates/
    standard-profile.yaml
    thesis-ai-spec.yaml
    figure-registry.yaml
    literature-review-matrix.yaml
    chapter-section-template.md
    ai-prompts.md
    ai-review-rubric.json
  drawio/
    system-architecture-template.drawio
    backend-layered-architecture-template.drawio
    business-flow-template.drawio
    er-diagram-template.drawio
    algorithm-workflow-template.drawio
    sequence-diagram-template.drawio
```

## 推荐工作流

1. 上传学校模板、任务书、开题报告或导师要求。
2. 上传程序源码、数据库结构、接口文档、运行截图、测试报告。
3. 让 AI 先填写 `standard-profile.yaml`，明确学校规则和参考文献版本。
4. 让 AI 再填写 `thesis-ai-spec.yaml`，抽取真实论文事实。
5. 让 AI 填写 `figure-registry.yaml`，规划图、表、公式和截图。
6. 按章节写正文，证据不足时先补材料。
7. 用 `ai-review-rubric.json` 做终稿审查。
8. 最后进入 Word/PDF 排版检查。

## PDF 文献交叉引用

把 PDF 文献放到 `papers/` 后运行：

```powershell
python $env:USERPROFILE\.codex\skills\thesis-standardizer\scripts\extract_pdf_references.py .\papers --out .\paper-context\literature
```

生成：

```text
paper-context/literature/reference-extraction.json
paper-context/literature/reference-extraction.md
```

如果已经有章节主题或论文提纲，例如 `paper-context/topics.md`：

```powershell
python $env:USERPROFILE\.codex\skills\thesis-standardizer\scripts\build_literature_crossrefs.py .\paper-context\literature\reference-extraction.json --topics .\paper-context\topics.md --out .\paper-context\literature\citation-crossrefs.md
```

这会生成文献交叉引用索引。注意：PDF 抽取结果只是候选证据，最终作者、年份、题名、期刊、DOI、引用格式必须核验。

## 规则

- 学校/学院正式模板优先。
- 导师、任务书和开题要求优先。
- 教育部抽检、学术规范和学位论文作假处理要求是底线。
- 国家标准作为学校未细化时的参考。
- 本仓库默认规则只作为可替换默认值。
- AI 不得编造功能、字段、接口、实验数据、测试结果、参考文献和 DOI。
- AI 不得在论文正文中写“根据用户提供材料”“通过分析代码”“让 AI 生成”等工作流痕迹。
- 每张图、表、公式、截图都必须有来源、编号、标题和正文引用位置。

## 仓库内容边界

本仓库只包含通用 skill、模板、脚本和说明文档。不包含任何具体学生论文、学校私有模板、源码项目、截图、PDF 文献或个人资料。
