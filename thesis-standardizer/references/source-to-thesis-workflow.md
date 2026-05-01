# Source To Thesis Workflow

Use this reference when the user gives a program, repository, database, API, screenshots, or test reports and wants a thesis.

## Goal

Turn implementation evidence into thesis-ready facts before writing prose.

## Inputs

Preferred inputs:

- source repository or project folder
- school template or formatting guide
- task book, proposal, advisor notes
- database schema or migration files
- API docs or route definitions
- screenshots and test reports
- deployment or run instructions

## Bootstrap Evidence

Run:

```powershell
python C:\Users\Lenovo\.codex\skills\thesis-standardizer\scripts\build_project_evidence.py . --out .\paper-context\evidence
```

Outputs:

```text
paper-context/evidence/
  project-evidence.json
  code-structure.md
  tech-stack.md
  api-list.md
  database-schema.md
  test-results.md
```

The script is a first pass. Read the outputs, then inspect source files before making important claims.

## Evidence To Thesis Mapping

| Evidence | Thesis Use |
|----------|------------|
| directory tree | system composition, frontend/backend split, module boundaries |
| package files | technology stack and development environment |
| routes/controllers | API design and detailed implementation |
| SQL/migrations/entities | database design and ER diagrams |
| tests/reports | testing chapter and result credibility |
| screenshots | detailed implementation and testing figures |

## Draft Order For System Papers

1. Related technology and development environment.
2. Requirement analysis.
3. Overall design.
4. Database/API/module design.
5. Detailed implementation.
6. Testing.
7. Introduction and conclusion last.

Introduction is easier and less fake after the real contribution is known.

## Stop Conditions

Do not draft final prose if these are missing:

- no school template or standard profile for layout-sensitive delivery
- no code evidence for claimed modules
- no schema/API evidence for database or interface claims
- no screenshots or run evidence for UI claims
- no test evidence for "tested", "stable", "passed", or "effective" claims

Return a missing-material list instead.

## Figure Planning

Create or update `figure-registry.yaml` before drawing:

- system architecture: based on real directory and deployment structure
- module diagram: based on real feature/module boundaries
- business flow: based on actual user/admin workflow
- ER diagram: based on schema/entities
- sequence diagram: based on controller/service/API flow
- screenshots: based on actual running pages or reports

Do not create decorative diagrams that cannot be traced to code or evidence.
