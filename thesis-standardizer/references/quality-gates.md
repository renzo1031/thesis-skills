# Quality Gates

Use before saying a thesis package, chapter draft, or review is complete.

## Gate 1: Standards

- `standard-profile.yaml` exists and identifies school/advisor rules.
- Reference style version is explicit.
- Bundled defaults are marked as fallback, not school requirements.
- Word/PDF layout-sensitive items are not claimed verified unless they were checked.

## Gate 2: Evidence

- `thesis-ai-spec.yaml` contains the thesis type and real facts.
- `figure-registry.yaml` lists each figure, table, equation, screenshot, and source.
- Claimed functions map to code, screenshots, tests, or user-provided materials.
- Claimed tests or experiments map to reports, logs, tables, or screenshots.

## Gate 3: Academic Integrity

- No fabricated references, DOI values, years, journals, APIs, fields, test results, samples, or metrics.
- No AI workflow leakage in body text.
- PDF reference extraction is treated as candidate evidence until verified.
- Private data, tokens, account names, phone numbers, and keys are not exposed in screenshots or prose.

## Gate 4: Structure

- Chapter structure matches `type_profile`.
- Chapter titles and numbering are continuous.
- Introduction does not promise work absent from later chapters.
- Conclusion summarizes completed work only.

## Gate 5: Figures, Tables, Equations

- Figure captions are below figures unless school rules differ.
- Table captions are above tables unless school rules differ.
- Every figure/table/equation is mentioned in text before or near placement.
- Structural diagrams have editable sources.
- Formula variables and units are explained.

## Gate 6: Script Validation

Run applicable checks:

```powershell
python C:\Users\Lenovo\.codex\skills\.system\skill-creator\scripts\quick_validate.py .\thesis-standardizer
python -m py_compile .\thesis-standardizer\scripts\*.py
```

For generated thesis workspaces:

```powershell
python - <<'PY'
import json, yaml
from pathlib import Path
base = Path('thesis-ai-standard/templates')
for name in ['standard-profile.yaml', 'thesis-ai-spec.yaml', 'figure-registry.yaml']:
    yaml.safe_load((base / name).read_text(encoding='utf-8'))
json.loads((base / 'ai-review-rubric.json').read_text(encoding='utf-8'))
print('OK')
PY
```

On Windows PowerShell, use a here-string piped into Python if shell heredoc is unavailable.

## Completion Language

Report:

- what was generated or changed
- what was verified
- what still needs human/school-template review
- which evidence is missing, if any
