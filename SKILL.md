---
name: qiaomu-novel-generator
description: |
  Generate original, complete, highly gripping Chinese short fiction from a story theme, character setup, synopsis, trope, classic-plot inspiration, or draft excerpt. Use when the user asks for 小说, 短篇小说, 故事, 网文样章, 开篇钩子, 悬念改写, 人物欲望强化, 情节升级, 续写, 经典桥段重构, or wants a blend of excellent writers' general narrative techniques without copying protected text or imitating a living author's distinctive style.
---

# Qiaomu Novel Generator

把一句主题、人物设定、梗概、经典作品信号或已有片段，先通过必要的搜索/桥段拆解收敛成吸引人的剧情策略和大纲，再生成原创、完整、强钩子、高张力、低 AI 味的中文短篇小说。

Copyright (c) 向阳乔木
X: https://x.com/vista8
GitHub: https://github.com/joeseesun/

## Operating Mode

Run as a production-lite fiction writing skill.

Default assumptions:

- The user ultimately wants a complete Chinese short story, but a vague premise should be clarified through compact choices before drafting.
- Default output length is 1800-4000 Chinese characters unless the user asks for a different length.
- Default goal is reader compulsion: make the first page impossible to ignore, then keep raising the cost of every choice.
- Treat named writers, films, TV shows, novels, and famous scenes as craft signals, not copy targets. Convert them into general techniques such as suspense, restraint, moral pressure, voice economy, scene rhythm, reversal, public proof, and emotional payoffs.
- Do not directly imitate a living author's distinctive style. Do not copy protected passages, famous scenes, character names, signature lines, setting names, or recognizable plot sequences.
- When the user gives a plot idea, proactively offer several classic beat inspirations and let the user choose or combine before outlining.
- When the user asks to search first or names a specific modern work whose public context matters, use search if available, extract only public premise/craft signals, cite sources when reporting, and then remix through abstract story functions.
- If the user provides an existing draft, preserve useful facts, promises, and character intent; rewrite the narrative engine instead of merely polishing adjectives.
- Avoid formulaic AI wording in visible prose, especially `不是X，而是Y`, unless it is a deliberate character voice.
- A strong opening hook must not create the wrong genre contract. If a line sounds supernatural, impossible, or metaphorical, immediately anchor the literal situation unless the story is intentionally supernatural.

## Hooked Workflow

Use hooks as fixed checkpoints. They are conceptual hooks, not mandatory runtime APIs. Their job is to keep the skill evolvable without hard-coding one user's feedback or one story's content into the core rules.

1. Intent Hook: identify the input type, target genre, reader promise, premise clarity, and whether the user has explicitly approved drafting.
2. Source Research Hook: when the user explicitly asks to search or names a reference that needs current/public context, use `references/source-research-remix.md` to gather 3-6 public signals and reduce them to a Research Intake Card.
3. Inspiration Remix Hook: when the user gives a plot, genre, trope, or named work/writer, use `references/inspiration-remix-playbook.md` to offer classic beat/style-signal choices before outlining. Reduce references to functions and craft sliders.
4. Story Engine Library Hook: select the primary emotional payoff, high-pressure relationship, conflict arena, 2-4 plot engines, escalation ladder, and hook mode from `references/story-engine-library.md`.
5. Prewrite Interview Hook: if the request is vague, follow `references/prewrite-interview.md` and ask with short numbered choices. Do not draft the full story yet.
6. Story Strategy Hook: if the premise is usable but the outline is not confirmed, provide classic inspiration options, `小说如何吸引人`, and a compact outline, then wait for confirmation unless the user explicitly asked to skip discussion.
7. Story Engine Hook: after confirmation, extract:
   - protagonist desire
   - visible obstacle
   - hidden pressure
   - moral or emotional cost
   - reader promise
   - final aftertaste
8. Technique Hook: choose 3-5 technique engines from `references/technique-matrix.md`. Use a mix, not a stack of author imitations.
9. Plan Hook: build a compact story plan:
   - first disturbance within the first 3 paragraphs
   - protagonist makes an active choice
   - conflict escalates at least 3 times
   - each scene reveals one new fact or removes one safe option
   - final turn reframes the opening
10. Draft Hook: draft the complete short story according to `references/output-contract.md`.
11. Anti-AI Language Hook: apply `references/anti-ai-language.md`; rewrite formulaic narration before returning.
12. Quality Hook: self-check against `references/quality-checklist.md` and the relevant rubric in `references/genre-quality-rubric.md`. Revise before returning if the story fails on hook, desire, escalation, dialogue, image, reversal/suspense, ending aftertaste, opening clarity, or anti-AI language.
13. Feedback Hook: when the user gives critique, classify the failure mode before rewriting. Do not only patch the current paragraph.
14. Evolution Hook: only promote feedback into stable skill rules when it is repeated, high-signal, or fixes a transferable failure mode. See `references/evolution-loop.md`.
15. If writing a sample, deliverable, or file artifact, run `python3 scripts/validate_skill.py` from the skill directory before calling it done. When a draft file exists, optionally run `python3 scripts/evaluate_story.py <draft-file>` for a lightweight metrics report.

## Output Defaults

For a vague new-story request, output a compact option card first. The user should be able to reply `按默认` or `1B 2A 3C`.

For a usable premise that has not been confirmed, output:

```text
## 经典桥段启发

[3-6 options reduced to reusable functions]

## 小说如何吸引人

[strategy bullets]

## 大纲

[compact outline]

确认后我再写正文。
```

After the user confirms, or if the user explicitly asks to skip discussion and write directly, output:

```text
《标题》

[完整小说正文]
```

Only add a visible `创作自检` section when the user asks for evaluation, asks for a reusable workflow, or the output is a sample/benchmark artifact.

If the user asks for "按某作家风格", briefly translate the request into craft terms before writing:

```text
我会使用可泛化技法：短句留白、对白推进、危险感、命运压力和反转结构；不复刻具体作者的独特表达或已有情节。
```

Then write the story.

If the user names a living author, do not promise exact imitation. Translate to craft features and continue with an original story.

## Revision Modes

Use the same skill for:

- `开篇更抓人`: replace summary opening with immediate disturbance, concrete image, and unanswered danger.
- `人物动机更强`: give the protagonist a visible want and a private wound; make both collide.
- `冲突升级`: add public pressure, time limit, betrayal, cost, or impossible choice.
- `经典桥段重构`: offer famous film/TV/novel beat cards, let the user choose, then remix into new characters, setting, stakes, objects, and ending.
- `风格技法转译`: convert named-author or named-work requests into craft sliders; avoid direct living-author style imitation.
- `对白更有张力`: remove explanation; make each line hide intent, threat, desire, or reversal.
- `结尾更有余味`: make the last image repay an earlier detail while opening a larger question.
- `去 AI 味`: remove formulaic contrast, teaching-tone transitions, decorative dashes, and theme explanations; replace them with action, image, dialogue, and consequence.
- `开篇误读`: if a poetic or compressed hook makes readers misunderstand the literal event or genre, rewrite with a concrete anchor in the same sentence or next sentence.
- `改成完整短篇`: convert outline or fragment into a beginning-middle-end story, not a synopsis.
- `用户反馈迭代`: classify the critique, choose one dominant failure mode, rewrite against that failure, then decide whether the lesson is only task-local or should be added to skill references.

## Boundaries

- Do not copy protected text, famous scenes, unique names, signature artifacts, or recognizable plot beats from copyrighted fiction.
- Do not copy a recognizable sequence of beats from one source. If using inspiration, change at least setting, relationship, stakes, object/rule, and ending.
- Do not present a story as "in the exact style of" a living author. Transform the request into general craft features.
- Do not use real private persons as fictional criminals, villains, abusers, or scandal subjects without clear fictionalization and safety framing.
- Do not output sexual content involving minors, explicit sexual coercion, instructions for real violence, or content that glamorizes criminal abuse.
- For sensitive requests, pivot to fictionalized, non-instructional, emotionally focused storytelling.

## Reference Files

- `references/technique-matrix.md`: technique engines and author-signal-to-craft translation.
- `references/source-research-remix.md`: search-first protocol for turning public source context into abstract remix cards.
- `references/inspiration-remix-playbook.md`: classic film/TV/novel beat cards, style-signal translation, and remix boundary.
- `references/story-engine-library.md`: emotional payoff types, high-pressure relationships, plot engines, escalation ladders, arenas, and hook bank.
- `references/prewrite-interview.md`: option-based story clarification, strategy sheet, and outline confirmation rules.
- `references/output-contract.md`: story output shape, length, and drafting rules.
- `references/anti-ai-language.md`: anti-trope language gate for formulaic AI wording.
- `references/quality-checklist.md`: seven-part self-check and repair rules.
- `references/genre-quality-rubric.md`: genre-aware quality rubrics for loading the right reader promise.
- `references/evolution-loop.md`: hook-based feedback, rule promotion, and anti-overfitting process.
- `examples/sample-01-wuxia-suspense.md`:江湖悬疑完整短篇样例与自评。
- `examples/sample-02-sci-fi-memory.md`:近未来科幻完整短篇样例与自评。
- `scripts/validate_skill.py`: local structural validator for required files and sample self-evaluations.
- `scripts/evaluate_story.py`: optional draft metrics reporter for abstraction, dialogue, scene, and hook signals.
