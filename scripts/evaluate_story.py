#!/usr/bin/env python3
"""Lightweight story diagnostics for qiaomu-novel-generator.

This script is intentionally non-authoritative. It reports smoke-test metrics
that help spot abstraction overload, weak scene density, or missing dialogue.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ABSTRACT_TERMS = [
    "需求",
    "流程",
    "系统",
    "规范",
    "策略",
    "机制",
    "能力",
    "价值",
    "痛点",
    "闭环",
    "效率",
    "协同",
    "模型",
    "方案",
    "架构",
    "规则",
]

SCENE_MARKERS = [
    "会议室",
    "门口",
    "窗",
    "雨",
    "灯",
    "桌",
    "屏幕",
    "手机",
    "街",
    "车",
    "手",
    "眼",
    "血",
    "杯",
    "纸",
    "门",
    "椅",
    "走廊",
]

HOOK_MARKERS = [
    "死",
    "血",
    "笑",
    "哭",
    "错",
    "债",
    "骂",
    "停",
    "断",
    "丢",
    "骗",
    "杀",
    "输",
    "滚",
    "赔",
    "取消",
]

AIISH_PATTERNS = [
    ("not_x_but_y", r"不是[^。！？\n]{0,40}而是"),
    ("not_about_but_about", r"不在于[^。！？\n]{0,40}在于"),
    ("summary_ending", r"总之|综上所述|总而言之"),
    ("teaching_transition", r"关键在于|值得注意的是|让我们|想象一个世界"),
    ("not_only_more", r"这不仅[^。！？\n]{0,40}更是"),
    ("meaning_slogan", r"这就是[^。！？\n]{0,30}的意义"),
]

AMBIGUOUS_OPENING_PATTERNS = [
    ("dead_person_walking", r"死人[^。！？\n]{0,12}(走|进|来|到)"),
    ("corpse_walking", r"尸体[^。！？\n]{0,12}(走|进|来|到)"),
    ("dead_speaking", r"(死人|死者|尸体)[^。！？\n]{0,12}(说|问|喊|开口)"),
]


def count_terms(text: str, terms: list[str]) -> int:
    return sum(text.count(term) for term in terms)


def count_dialogue_lines(text: str) -> int:
    return sum(1 for line in text.splitlines() if "“" in line and "”" in line)


def count_aiish_patterns(text: str) -> dict[str, int]:
    return {name: len(re.findall(pattern, text)) for name, pattern in AIISH_PATTERNS}


def count_ambiguous_opening_patterns(text: str) -> dict[str, int]:
    opening = first_paragraphs(text)
    return {
        name: len(re.findall(pattern, opening))
        for name, pattern in AMBIGUOUS_OPENING_PATTERNS
    }


def first_paragraphs(text: str, count: int = 3) -> str:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    return "\n".join(paragraphs[:count])


def hits_per_100(part: int, chars: int) -> float:
    return 0.0 if chars <= 0 else part / chars * 100


def evaluate(path: Path) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    compact = re.sub(r"\s+", "", text)
    chars = len(compact)
    abstract_hits = count_terms(text, ABSTRACT_TERMS)
    scene_hits = count_terms(text, SCENE_MARKERS)
    dialogue_lines = count_dialogue_lines(text)
    hook_hits = count_terms(first_paragraphs(text), HOOK_MARKERS)
    dash_hits = text.count("——")
    aiish_hits = count_aiish_patterns(text)
    ambiguous_opening_hits = count_ambiguous_opening_patterns(text)
    aiish_total = sum(aiish_hits.values())
    ambiguous_opening_total = sum(ambiguous_opening_hits.values())

    report = [
        f"file: {path}",
        f"chars_no_space: {chars}",
        f"dialogue_lines: {dialogue_lines}",
        f"abstract_term_hits: {abstract_hits} ({hits_per_100(abstract_hits, chars):.2f} per 100 chars)",
        f"scene_marker_hits: {scene_hits}",
        f"first_3_paragraph_hook_hits: {hook_hits}",
        f"dash_hits: {dash_hits}",
        "aiish_pattern_hits: "
        + ", ".join(f"{name}={count}" for name, count in aiish_hits.items()),
        "ambiguous_opening_hits: "
        + ", ".join(f"{name}={count}" for name, count in ambiguous_opening_hits.items()),
    ]

    warnings = []
    if chars < 800:
        warnings.append("draft may be too short to judge as a complete short story")
    if dialogue_lines < 4:
        warnings.append("low dialogue count; check whether the draft is explaining instead of dramatizing")
    if abstract_hits > scene_hits * 2 and abstract_hits > 12:
        warnings.append("abstract language may dominate concrete scene work")
    if scene_hits < 8:
        warnings.append("low concrete scene marker count; add people, objects, places, or actions")
    if hook_hits == 0:
        warnings.append("first three paragraphs may lack immediate disturbance")
    if aiish_hits.get("not_x_but_y", 0) > 0:
        warnings.append("AI-ish contrast pattern found: rewrite '不是X，而是Y' unless it is deliberate dialogue")
    if aiish_total > aiish_hits.get("not_x_but_y", 0):
        warnings.append("AI-ish explanatory phrasing found; replace lesson voice with action, image, dialogue, or consequence")
    if dash_hits > 3:
        warnings.append("too many decorative dashes; replace most with comma, period, colon, or scene action")
    if ambiguous_opening_total > 0:
        warnings.append(
            "opening may create a false supernatural or impossible-action reading; add an immediate literal anchor or rewrite the hook"
        )

    return report, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Report lightweight story quality diagnostics.")
    parser.add_argument("story_file", type=Path)
    parser.add_argument("--fail-on-warning", action="store_true")
    args = parser.parse_args()

    if not args.story_file.exists():
        print(f"[FAIL] file not found: {args.story_file}", file=sys.stderr)
        return 1

    report, warnings = evaluate(args.story_file)
    for line in report:
        print(line)
    if warnings:
        print("warnings:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("warnings: none")

    return 1 if warnings and args.fail_on_warning else 0


if __name__ == "__main__":
    raise SystemExit(main())
