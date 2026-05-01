# Workflow State Management

Use this reference when a thesis project needs persistent progress tracking, step-by-step execution records, or a clear "where are we now" state.

## Goal

Create a thesis workbench under `paper-context/workflow/` so the agent can resume work without guessing.

## Bootstrap

Run:

```powershell
python C:\Users\Lenovo\.codex\skills\thesis-standardizer\scripts\init_workflow_logs.py .
```

`init_thesis_workspace.py` runs this automatically unless `--no-workflow-logs` is used.

## Generated Files

| File | Purpose |
| --- | --- |
| `workflow-status.md` | Current stage, next action, overall status |
| `step-plan.md` | Step-by-step task board with dependencies |
| `progress-log.md` | Chronological work-session log |
| `material-inventory.md` | School, project, evidence, and literature inventory |
| `evidence-gaps.md` | Unsupported claims and missing materials |
| `chapter-progress.md` | Chapter-level drafting/review status |
| `revision-log.md` | All changes from comments, AIGC pass, standards, figures, and final review |

## Update Rules

At the start of a thesis task:

1. Read `workflow-status.md`.
2. Read `step-plan.md`.
3. Read the module-specific files for the user's request.
4. Update current stage and next action before doing substantial work.

At the end of a thesis task:

1. Append an entry to `progress-log.md`.
2. Update `step-plan.md` statuses.
3. Update `chapter-progress.md` if chapter work changed.
4. Add unresolved materials to `evidence-gaps.md`.
5. Add actual edits to `revision-log.md`.

## Status Vocabulary

Use these values consistently:

- `pending`: not started
- `in_progress`: currently being worked on
- `blocked`: cannot proceed without material or decision
- `needs_review`: generated but needs human/school/template review
- `done`: verified enough for the current stage
- `deprecated`: no longer used

## Non-Negotiable Rule

Do not silently skip log updates after changing thesis content or workflow state. The workbench is the memory of the thesis project.
