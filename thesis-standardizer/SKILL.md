---
name: thesis-standardizer
description: Standardize and draft undergraduate thesis or graduation-design papers from source code, school templates, task books, drafts, screenshots, databases, APIs, experiments, PDF literature, and test evidence. Use when the user asks to write, generate, refactor, check, or package a thesis; turn a program into thesis chapters; create thesis specs, figure registries, draw.io diagrams, evidence indexes, PDF reference extraction, or citation cross-reference maps; or enforce school thesis rules before drafting.
---

# Thesis Standardizer

## Operating Model

Treat a thesis as an evidence-driven project. Do not start from prose. Start from standards, facts, and evidence.

Layering:

1. `SKILL.md`: routing, guardrails, and quality gates.
2. `references/`: detailed workflows loaded only when needed.
3. `scripts/`: deterministic extraction and initialization helpers.
4. `assets/thesis-ai-standard/`: portable project templates copied into the user's workspace.
5. user's materials: school template, source code, PDFs, screenshots, data, tests, and drafts.

## Decision Tree

- New thesis workspace or missing templates: run `scripts/init_thesis_workspace.py <target-dir>`.
- Program/source-code thesis: read `references/source-to-thesis-workflow.md`; run `scripts/build_project_evidence.py <project-dir> --out paper-context/evidence`.
- PDF literature, related work, or citations: read `references/literature-and-pdf-workflow.md`; run the PDF extraction and citation cross-reference scripts.
- Existing draft or Word-format-sensitive work: use this skill for standards/evidence, then use `thesis-docx`/`docx` for Word layout and PDF review.
- Before final delivery: read `references/quality-gates.md` and run the applicable checks.

## Required Read Order

When `thesis-ai-standard/` exists, read:

1. `thesis-ai-standard/README.md`
2. the public-standards guide in `thesis-ai-standard/`
3. `thesis-ai-standard/templates/standard-profile.yaml`
4. `thesis-ai-standard/templates/thesis-ai-spec.yaml`
5. `thesis-ai-standard/templates/figure-registry.yaml`

If those files do not exist, bootstrap them from `assets/thesis-ai-standard/`.

## Core Workflow

1. Collect standards: school template, advisor instructions, task book, proposal.
2. Collect evidence: source code, database schema, API docs, screenshots, test reports, data, experiment logs, PDFs, existing drafts.
3. Fill `standard-profile.yaml` before interpreting formatting rules.
4. Fill `thesis-ai-spec.yaml` before drafting chapters.
5. Fill `figure-registry.yaml` before generating diagrams or screenshots.
6. Stop and list missing materials when a claim lacks evidence.
7. Draft chapter by chapter using `chapter-section-template.md`.
8. Review with `ai-review-rubric.json` and the quality gates.

## Thesis Type Selection

Use the closest `type_profile`:

- `system_design`: software, app, mini program, website, management system, IoT, embedded system.
- `empirical_research`: experiment, algorithm/model evaluation, engineering test, statistical result.
- `survey_analysis`: questionnaire, interview, case study, user or industry analysis.
- `engineering_design`: engineering plan, product design, structure/process design, prototype validation.
- `literature_review`: literature matrix, topic comparison, method review, research trend.

Do not force non-software papers into the system-design chapter structure.

## Non-Negotiable Rules

- School and advisor rules override bundled defaults.
- Never invent functions, fields, API paths, tests, experiment data, samples, citations, DOI values, or school requirements.
- Never expose AI workflow language in thesis body text.
- Every figure/table/equation/screenshot must have source, ID, title, first mention, and status.
- PDF reference extraction creates candidates only; verify bibliography before final writing.
- Claim completion only after running relevant script validation or clearly stating what could not be verified.

## Bundled References

- `references/source-to-thesis-workflow.md`: program/source-code to thesis evidence workflow.
- `references/literature-and-pdf-workflow.md`: PDF reference extraction and citation cross-reference workflow.
- `references/rapid-thesis-workflow.md`: short path for common thesis package tasks.
- `references/quality-gates.md`: final validation checklist.

## Bundled Scripts

- `scripts/init_thesis_workspace.py`: copy `assets/thesis-ai-standard/` into a project.
- `scripts/build_project_evidence.py`: create source-code evidence files for system-design papers.
- `scripts/extract_pdf_references.py`: extract candidate reference sections from PDFs.
- `scripts/build_literature_crossrefs.py`: map extracted references to thesis topics or chapter claims.
