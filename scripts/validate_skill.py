#!/usr/bin/env python3
"""Validate qiaomu-novel-generator structure and sample evidence."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "manifest.json",
    "agents/interface.yaml",
    "agents/openai.yaml",
    "references/technique-matrix.md",
    "references/output-contract.md",
    "references/quality-checklist.md",
    "references/genre-quality-rubric.md",
    "references/evolution-loop.md",
    "examples/sample-01-wuxia-suspense.md",
    "examples/sample-02-sci-fi-memory.md",
    "scripts/evaluate_story.py",
]

SELF_EVAL_ITEMS = [
    "开篇钩子",
    "人物欲望",
    "冲突升级",
    "对白张力",
    "画面感",
    "反转/悬念",
    "结尾余味",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}", file=sys.stderr)
    sys.exit(1)


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.exists():
        fail(f"missing required file: {relative}")
    return path.read_text(encoding="utf-8")


def validate_skill_md() -> None:
    text = read("SKILL.md")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        fail("SKILL.md frontmatter is not closed")
    frontmatter = parts[1]
    if "name: qiaomu-novel-generator" not in frontmatter:
        fail("SKILL.md frontmatter must contain the skill name")
    if "description:" not in frontmatter:
        fail("SKILL.md frontmatter must contain description")
    unresolved_markers = ["[TO" + "DO", "TO" + "DO:"]
    if any(marker in text for marker in unresolved_markers):
        fail("SKILL.md still contains unresolved template markers")


def validate_manifest() -> None:
    data = json.loads(read("manifest.json"))
    if data.get("name") != "qiaomu-novel-generator":
        fail("manifest.json has wrong name")
    for item in data.get("resources", []):
        if not (ROOT / item).exists():
            fail(f"manifest resource does not exist: {item}")
    for item in data.get("scripts", []):
        if not (ROOT / item).exists():
            fail(f"manifest script does not exist: {item}")


def validate_yaml_like(relative: str, required_terms: list[str]) -> None:
    text = read(relative)
    for term in required_terms:
        if term not in text:
            fail(f"{relative} missing required term: {term}")
    if "\t" in text:
        fail(f"{relative} contains tab indentation")


def validate_examples() -> None:
    for relative in [
        "examples/sample-01-wuxia-suspense.md",
        "examples/sample-02-sci-fi-memory.md",
    ]:
        text = read(relative)
        for heading in ["## 输入", "## 技法组合", "## 小说正文", "## 创作自评"]:
            if heading not in text:
                fail(f"{relative} missing heading: {heading}")
        for item in SELF_EVAL_ITEMS:
            if item not in text:
                fail(f"{relative} missing self-eval item: {item}")
        story_part = text.split("## 小说正文", 1)[1].split("## 创作自评", 1)[0]
        if len(story_part.strip()) < 1200:
            fail(f"{relative} story sample is too short to prove a complete short story")


def validate_evolution_docs() -> None:
    skill_text = read("SKILL.md")
    for term in ["Intent Hook", "Quality Hook", "Feedback Hook", "Evolution Hook"]:
        if term not in skill_text:
            fail(f"SKILL.md missing hook term: {term}")
    evolution = read("references/evolution-loop.md")
    for term in ["Do Not Overfit", "Rule Promotion", "Failure Taxonomy"]:
        if term not in evolution:
            fail(f"evolution-loop.md missing section: {term}")
    rubric = read("references/genre-quality-rubric.md")
    for term in ["Reader Promise", "Universal Rubric", "Anti-Exposition Check"]:
        if term not in rubric:
            fail(f"genre-quality-rubric.md missing section: {term}")


def main() -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            fail(f"missing required file: {relative}")

    validate_skill_md()
    validate_manifest()
    validate_yaml_like("agents/interface.yaml", ["triggers:", "quality_gates:", "resources:"])
    validate_yaml_like("agents/openai.yaml", ["interface:", "default_prompt:", "allow_implicit_invocation:"])
    validate_examples()
    validate_evolution_docs()
    print("[OK] qiaomu-novel-generator structure and samples validated")


if __name__ == "__main__":
    main()
