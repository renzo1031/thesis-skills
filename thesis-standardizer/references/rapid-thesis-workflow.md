# Rapid Thesis Workflow

Use this reference when the user wants to quickly turn a program, experiment, or existing draft into a thesis package.

## Intake Checklist

Collect what exists before drafting:

- school template or formatting guide
- task book, proposal, advisor notes
- source code or project folder
- database schema, API docs, test reports
- screenshots or experiment outputs
- existing thesis draft, if any
- reference list or required citation style

If school rules are missing, use bundled defaults but mark them as replaceable.

## Bootstrap

Run:

```powershell
python C:\Users\Lenovo\.codex\skills\thesis-standardizer\scripts\init_thesis_workspace.py .
```

Then fill:

```text
thesis-ai-standard/templates/standard-profile.yaml
thesis-ai-standard/templates/thesis-ai-spec.yaml
thesis-ai-standard/templates/figure-registry.yaml
```

## From Program To Thesis

For software/system projects:

1. Read repository structure and identify frontend, backend, database, external services, and test assets.
2. Extract real facts into `thesis-ai-spec.yaml`.
3. Create a figure plan in `figure-registry.yaml`:
   - system architecture
   - module diagram
   - business flow
   - ER diagram or data model
   - key sequence diagrams
   - screenshots and test result figures
4. Draft chapters in this order:
   - related technology
   - requirement analysis
   - overall design
   - detailed implementation
   - testing
   - introduction and conclusion last

## From Experiment Or Survey To Thesis

For research/data papers:

1. Identify research question, objects, variables, data source, method, and limitations.
2. Use `type_profile: empirical_research` or `survey_analysis`.
3. Build tables before prose:
   - variable definition table
   - sample/data source table
   - method or model table
   - result table
4. Draft results only from provided data.

## Stop Conditions

Do not draft final prose when these are missing:

- school template for layout-sensitive delivery
- source evidence for claimed functions or experiments
- test/experiment result records
- database/API facts for system papers
- reference list for literature review and citations

Instead output an exact missing-material list.

## Review

Before final response, run or perform:

- YAML parse for standard/spec/registry files
- JSON parse for review rubric
- XML parse for draw.io templates if modified
- scan for project-specific leftovers when creating a generic package
- review for AI-workflow leakage in thesis prose
