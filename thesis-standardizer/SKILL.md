---
name: thesis-standardizer
description: Standardize and draft undergraduate thesis or graduation-design papers from source code, school templates, task books, drafts, screenshots, databases, APIs, experiments, and test evidence. Use when the user asks to write, generate, refactor, check, or package a thesis; build a thesis workflow from a program; create thesis chapters, figures, tables, evidence indexes, draw.io diagrams, or AI-readable thesis specs; or quickly turn a project into a standards-driven thesis deliverable.
---

# Thesis Standardizer

## Core Rule

Treat the thesis as an evidence-driven project, not a text-generation task. Read standards first, facts second, evidence third, then write. Never invent functions, database fields, API paths, tests, experiment data, citations, DOI values, or school rules.

## Fast Workflow

1. Find or create the thesis workspace.
   - If no `thesis-ai-standard/` exists, run `scripts/init_thesis_workspace.py <target-dir>`.
   - If one exists, reuse it and update only the missing fields.
2. Read in this order:
   - `thesis-ai-standard/README.md`
   - the public-standards guide in `thesis-ai-standard/`
   - `thesis-ai-standard/templates/standard-profile.yaml`
   - `thesis-ai-standard/templates/thesis-ai-spec.yaml`
   - `thesis-ai-standard/templates/figure-registry.yaml`
3. Build context from the user's materials:
   - school template, task book, proposal, existing draft
   - source code, database schema, API docs, screenshots, test reports
   - data files, experiment records, questionnaire/interview materials
   - PDF papers and downloaded literature when doing literature review or related work
4. Fill or update:
   - `standard-profile.yaml`: school rules, advisor rules, reference standard version
   - `thesis-ai-spec.yaml`: thesis facts, type profile, chapters, evidence index
   - `figure-registry.yaml`: figures, tables, equations, screenshots, source files
5. Stop before drafting if required evidence is missing. Output a missing-material list with exact file types needed.
6. Draft chapter by chapter using `templates/chapter-section-template.md`.
7. Generate editable diagrams with draw.io/Mermaid when evidence supports the nodes and relationships.
8. For literature-heavy work, extract PDF reference sections first, then build a citation map before drafting.
9. Review with `templates/ai-review-rubric.json`.
10. For Word layout-sensitive work, use the existing `thesis-docx`/`docx` skills and verify in Word/PDF when available.

## Thesis Type Selection

Choose the closest `type_profile` in `thesis-ai-spec.yaml`:

- `system_design`: software, app, mini program, website, management system, IoT, embedded system.
- `empirical_research`: experiment, algorithm/model evaluation, engineering test, statistical result.
- `survey_analysis`: questionnaire, interview, case study, user or industry analysis.
- `engineering_design`: engineering plan, product design, structure/process design, prototype validation.
- `literature_review`: literature matrix, topic comparison, method review, research trend.

Do not force all papers into the software-system structure. For non-system papers, replace "requirement/design/implementation/test" language with "research design/process/results/discussion" language.

## Standards Policy

Always enforce this priority:

1. School or college official template.
2. Advisor/task-book requirements.
3. Education-ministry sampling and academic-integrity requirements.
4. School-specified national standards.
5. The bundled default rules.

As of 2026-05-01, `GB/T 7713.1-2025` is implemented. `GB/T 7714-2025` is published and takes effect on 2026-07-01; reference style still follows the school notice during the transition.

## Drafting Rules

- Write in normal thesis voice: use academic Chinese prose such as "This paper designs...", "The system...", "The experiment results...".
- Do not mention AI, prompt use, source feeding, or "based on user-provided code" in body text.
- Every chapter must have a purpose, inputs, evidence, suggested figures/tables, and self-check items.
- Every figure/table/equation must have an ID, title, source, first mention, and status.
- Screenshots must be clear, cropped, relevant, and free of secrets or private data.
- Conclusions summarize completed work only; future work must remain future work.

## Literature And PDF Workflow

Use this when the user gives PDF papers, asks for literature review, related work, references, citation cross-references, or reference cleanup.

1. Run `scripts/extract_pdf_references.py <pdf-dir> --out <output-dir>` to extract text and likely reference sections from PDFs.
2. Read the generated `reference-extraction.json` and `reference-extraction.md`.
3. Run `scripts/build_literature_crossrefs.py <reference-json> --topics <topics-file> --out <output-md>` when a topic/chapter outline is available.
4. Use AI judgment to verify extraction quality. PDF extraction is a candidate list, not ground truth.
5. Create citation cross-reference entries only where the paper's title, keywords, abstract, or reference text genuinely matches a chapter claim.
6. Do not fabricate missing bibliographic fields. Mark uncertain author, title, year, DOI, or venue values as `unknown` or `needs_check`.

## Bundled Resources

- `assets/thesis-ai-standard/`: portable template package copied into new projects.
- `references/rapid-thesis-workflow.md`: quick operating guide for common requests.
- `references/literature-and-pdf-workflow.md`: PDF reference extraction and citation cross-reference guide.
- `scripts/init_thesis_workspace.py`: copy the bundled template package into a target project.
- `scripts/extract_pdf_references.py`: extract likely references from PDF files.
- `scripts/build_literature_crossrefs.py`: create chapter/topic citation cross-reference indexes from extracted references.

Load reference files only when needed. Prefer the script for bootstrapping instead of manually recreating the folder tree.
