#!/usr/bin/env python3
"""Build a citation cross-reference index from extracted PDF references."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "this",
    "that",
    "研究",
    "系统",
    "方法",
    "设计",
    "实现",
    "分析",
    "基于",
    "本文",
    "论文",
}


def tokenize(text: str) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9_+-]{2,}|[\u4e00-\u9fff]{2,}", text.lower())
    return [word for word in words if word not in STOPWORDS]


def topic_blocks(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    blocks: list[dict[str, str]] = []
    current_title = "General"
    current_lines: list[str] = []

    for line in text.splitlines():
        if line.startswith("#"):
            if current_lines:
                blocks.append({"topic": current_title, "text": "\n".join(current_lines)})
                current_lines = []
            current_title = line.lstrip("#").strip() or "Untitled"
        else:
            current_lines.append(line)
    if current_lines:
        blocks.append({"topic": current_title, "text": "\n".join(current_lines)})
    if not blocks:
        blocks.append({"topic": "General", "text": text})
    return blocks


def load_references(path: Path) -> list[dict[str, str]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    refs: list[dict[str, str]] = []
    for result in payload.get("results", []):
        title = result.get("title_guess", "")
        pdf = result.get("pdf", "")
        for ref in result.get("references", []):
            refs.append({"source_pdf": pdf, "source_title": title, "reference": ref})
    return refs


def score(topic_text: str, reference: str) -> tuple[int, list[str]]:
    topic_counts = Counter(tokenize(topic_text))
    ref_tokens = tokenize(reference)
    overlaps = []
    total = 0
    for token in ref_tokens:
        if token in topic_counts:
            total += topic_counts[token]
            if token not in overlaps:
                overlaps.append(token)
    year_bonus = 1 if re.search(r"\b20[0-2]\d\b", reference) else 0
    return total + year_bonus, overlaps[:10]


def write_crossrefs(refs: list[dict[str, str]], topics: list[dict[str, str]], out: Path) -> None:
    lines = ["# Citation Cross-Reference Index", ""]
    if not refs:
        lines.append("No extracted references available. Run extract_pdf_references.py first.")
        out.write_text("\n".join(lines), encoding="utf-8")
        return

    for topic in topics:
        ranked = []
        for ref in refs:
            value, overlaps = score(topic["text"] + " " + topic["topic"], ref["reference"])
            if value > 0:
                ranked.append((value, overlaps, ref))
        ranked.sort(key=lambda item: item[0], reverse=True)

        lines.extend([f"## {topic['topic']}", ""])
        if not ranked:
            lines.append("- No strong match. Needs AI/human review.")
            lines.append("")
            continue

        for value, overlaps, ref in ranked[:8]:
            confidence = "strong" if value >= 4 else "needs_check"
            lines.append(f"- Confidence: `{confidence}`; score: `{value}`")
            lines.append(f"  - Matched terms: {', '.join(overlaps) if overlaps else 'year/recentness only'}")
            lines.append(f"  - Reference: {ref['reference']}")
            lines.append(f"  - Source PDF: `{ref['source_pdf']}`")
        lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build citation cross-references by keyword overlap.")
    parser.add_argument("reference_json", help="reference-extraction.json from extract_pdf_references.py")
    parser.add_argument("--topics", required=True, help="Markdown file containing thesis topics or chapter outline.")
    parser.add_argument("--out", default="citation-crossrefs.md", help="Output markdown file.")
    args = parser.parse_args()

    refs = load_references(Path(args.reference_json))
    topics = topic_blocks(Path(args.topics))
    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    write_crossrefs(refs, topics, out)
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
