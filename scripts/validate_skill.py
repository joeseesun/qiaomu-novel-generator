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
    "references/source-research-remix.md",
    "references/inspiration-remix-playbook.md",
    "references/story-engine-library.md",
    "references/prewrite-interview.md",
    "references/output-contract.md",
    "references/anti-ai-language.md",
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
    for term in ["Source Research Hook", "Inspiration Remix Hook", "Story Engine Library Hook", "Prewrite Interview Hook", "Anti-AI Language Hook"]:
        if term not in skill_text:
            fail(f"SKILL.md missing new workflow hook: {term}")
    source_research = read("references/source-research-remix.md")
    for term in ["When To Search", "Research Intake Card", "Search-To-Remix Output", "Modern Organization Beat Cards"]:
        if term not in source_research:
            fail(f"source-research-remix.md missing required section: {term}")
    evolution = read("references/evolution-loop.md")
    for term in ["Do Not Overfit", "Rule Promotion", "Failure Taxonomy"]:
        if term not in evolution:
            fail(f"evolution-loop.md missing section: {term}")
    rubric = read("references/genre-quality-rubric.md")
    for term in ["Reader Promise", "Universal Rubric", "Anti-Exposition Check"]:
        if term not in rubric:
            fail(f"genre-quality-rubric.md missing section: {term}")
    engine_library = read("references/story-engine-library.md")
    for term in ["Emotional Payoff Types", "High-Pressure Relationship Bank", "Core Plot Engines", "Escalation Ladders", "Chapter Or Episode Hook Bank"]:
        if term not in engine_library:
            fail(f"story-engine-library.md missing required section: {term}")
    remix = read("references/inspiration-remix-playbook.md")
    for term in ["Classic Beat Cards", "Style Signal Translation", "Remix Boundary", "马伯庸式", "食神式"]:
        if term not in remix:
            fail(f"inspiration-remix-playbook.md missing required term: {term}")
    prewrite = read("references/prewrite-interview.md")
    for term in ["可选调整", "你可以直接回复", "经典桥段启发", "小说如何吸引人", "确认后我再写正文"]:
        if term not in prewrite:
            fail(f"prewrite-interview.md missing required term: {term}")
    anti_ai = read("references/anti-ai-language.md")
    for term in ["不是X，而是Y", "Target: zero", "Replace explanation with action"]:
        if term not in anti_ai:
            fail(f"anti-ai-language.md missing required term: {term}")


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
