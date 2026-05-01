# Literature And PDF Workflow

Use this reference when a thesis needs literature review, related work, citation cleanup, citation placement, or reference extraction from PDF papers.

## Inputs

Preferred inputs:

- PDF papers in one folder
- thesis title, abstract, keywords, chapter outline, or `thesis-ai-spec.yaml`
- school reference style requirement
- existing reference list, if any

## PDF Reference Extraction

Run:

```powershell
python C:\Users\Lenovo\.codex\skills\thesis-standardizer\scripts\extract_pdf_references.py .\papers --out .\paper-context\literature
```

Outputs:

```text
paper-context/literature/
  reference-extraction.json
  reference-extraction.md
```

The script extracts candidate reference sections. Treat output as raw evidence. Verify bibliographic fields manually or with trusted sources before final formatting.

## Citation Cross-References

If a topic outline exists, create a citation cross-reference index:

```powershell
python C:\Users\Lenovo\.codex\skills\thesis-standardizer\scripts\build_literature_crossrefs.py .\paper-context\literature\reference-extraction.json --topics .\paper-context\topics.md --out .\paper-context\literature\citation-crossrefs.md
```

Cross-reference rules:

- Match references to claims by overlap with topic terms, methods, domain words, and known acronyms.
- Prefer recent and directly relevant papers for research status sections.
- Prefer method papers for method/theory sections.
- Prefer system/application papers for design comparison sections.
- Do not cite a paper merely because a keyword appears once.
- Mark weak matches as `needs_check`.

## Writing Literature Review

Structure by theme, not by one-paper-per-paragraph:

1. Define the research or engineering problem.
2. Group literature into 2-4 themes.
3. Compare methods, data, systems, or conclusions.
4. Identify the gap that the thesis addresses.
5. Connect the gap to the thesis work.

Avoid:

- fabricated author/year/venue
- references not cited in body text
- body citations missing from final reference list
- DOI or URL hallucination
- "AI found" or "the uploaded paper says" wording

## Final Checks

- Every cited source appears in the reference list.
- Every reference-list item is cited, unless school rules allow uncited background references.
- Reference format follows `standard-profile.yaml`.
- Extraction uncertainty is resolved before final submission.
