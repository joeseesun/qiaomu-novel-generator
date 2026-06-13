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


def count_terms(text: str, terms: list[str]) -> int:
    return sum(text.count(term) for term in terms)


def count_dialogue_lines(text: str) -> int:
    return sum(1 for line in text.splitlines() if "“" in line and "”" in line)


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

    report = [
        f"file: {path}",
        f"chars_no_space: {chars}",
        f"dialogue_lines: {dialogue_lines}",
        f"abstract_term_hits: {abstract_hits} ({hits_per_100(abstract_hits, chars):.2f} per 100 chars)",
        f"scene_marker_hits: {scene_hits}",
        f"first_3_paragraph_hook_hits: {hook_hits}",
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
