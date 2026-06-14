# Prewrite Interview

Use this before drafting a new story.

The goal is to make the user feel the story is being designed with them, not dumped at them. A good novel request should pass through story strategy and outline confirmation before the full draft, unless the user explicitly says to skip discussion and write directly.

When the user gives a plot idea, do not only ask generic options. First offer classic beat inspirations from `references/inspiration-remix-playbook.md`, then let the user choose or combine.

When the user says to search first or names a specific reference whose context matters, use `references/source-research-remix.md` before this interview. Summarize only reusable craft signals and sources, then ask the user to choose a bridge combination.

## When The Request Is Vague

If the user only says things like `帮我生成一个小说`, `写一篇小说`, `来个修仙打脸`, or gives only a broad genre/trope, do not start the full story.

Give a short default plan plus numbered choices. Use the Qiaomu goal-skill pattern: recommended defaults first, short reason, compact options, and a reply shortcut.

Choose options from `references/story-engine-library.md`. Do not keep reusing the same修仙拍卖 default unless the user signals that genre.
If the user names a work, trope, or author, use `references/inspiration-remix-playbook.md` to translate it into reusable functions and craft sliders.
If the user also asks for search, include 3-5 source-informed functions before the options.

Output shape:

```text
我先帮你把故事方向定住。默认我会选：[情绪承诺] + [高压关系] + [冲突场] + [2-3 个剧情引擎]。

默认选择理由：[一句话，说明为什么这个方向最容易出钩子、冲突和爽点。]

可选调整
1. 主情绪：A [默认：爽/燃/甜/惊等] / B [替代情绪] / C [更暗或更慢热]
2. 高压关系：A [默认关系] / B [更亲密更痛] / C [更对抗更刺激]
3. 冲突场：A [默认公开场] / B [更危险场] / C [更现实场]
4. 剧情引擎：A [默认 2-3 个引擎] / B [更反转] / C [更成长]
5. 升级节奏：A [默认：小压迫→小反击→大陷害→大翻盘] / B [悬疑层层揭露] / C [短剧式强钩子]
6. 结尾味道：A [默认：爽完留钩子] / B [收束干净] / C [黑色反转]

你可以直接回复：按默认，或回复类似 `1B 2A 3C`。
```

Keep choices short. Do not ask a long questionnaire. The user should be able to answer in one line.

## When The Request Has Enough Premise

If the user already gives a theme, protagonist, core conflict, or desired trope, do not immediately draft the full story. First provide a strategy sheet and outline.

Output shape:

```text
## 经典桥段启发

1. A [经典信号]：[可复用功能]，适合做[效果]
2. B [经典信号]：[可复用功能]，适合做[效果]
3. C [经典信号]：[可复用功能]，适合做[效果]

我建议组合：[A + C + 反向处理]。

## 小说如何吸引人

- 读者承诺：
- 经典桥段重构：
- 风格技法转译：
- 主爽点/主情绪：
- 高压关系：
- 剧情引擎：
- 开篇钩子：
- 主角欲望：
- 隐藏压力：
- 冲突升级：
- 章节/场景钩子：
- 爽点/反转：
- 语言处理：
- 结尾余味：

## 大纲

1. [开篇扰动]
2. [主角主动选择]
3. [第一次升级]
4. [第二次升级]
5. [公开或情感反转]
6. [结尾回响]

确认后我再写正文。你可以回复：按这个写 / 加强打脸 / 更悬疑 / 更现实 / 更狠。
```

## When To Draft

Draft the full story only when:

- the user confirms the outline with `按这个写`, `开始写`, `就这样`, `按默认`, or equivalent;
- the user explicitly says `别问，直接写`, `不用讨论`, or `按默认直接写`;
- the user is asking to revise an existing full draft and the needed direction is already clear.

If drafting directly because the user explicitly asked to skip discussion, still do the strategy and outline internally before writing.

## Strategy Requirements

The strategy must explain how the story will become attractive in reader-effect terms:

- What question makes the reader continue?
- What does the protagonist visibly want right now?
- What primary emotional payoff is promised: 爽、甜、虐、恨、惊、燃、怕、痛, or治愈?
- Which high-pressure relationship makes the conflict hard to escape?
- Which 2-4 story engines from `story-engine-library.md` are carrying the plot?
- Which famous beat cards or style signals are being remixed, and what elements are changed?
- Where will the protagonist be publicly underestimated, trapped, or forced to choose?
- Which safe option will close first?
- What information will reverse its meaning later?
- What final image will echo the opening?

Avoid abstract promises such as `更有张力` unless paired with a concrete move.
