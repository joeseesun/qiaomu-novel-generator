# qiaomu-novel-generator

> 把一句主题、人物设定、梗概或已有片段，变成原创、完整、强钩子、高张力的中文短篇小说。
> Turn one story idea into a complete, gripping Chinese short story with a reusable narrative craft workflow.

[![Install](https://img.shields.io/badge/install-npx%20skills%20add-0f766e)](#安装)
[![License](https://img.shields.io/github/license/joeseesun/qiaomu-novel-generator)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/joeseesun/qiaomu-novel-generator)](https://github.com/joeseesun/qiaomu-novel-generator/commits/main)
[![Stars](https://img.shields.io/github/stars/joeseesun/qiaomu-novel-generator?style=social)](https://github.com/joeseesun/qiaomu-novel-generator)

```bash
npx skills add joeseesun/qiaomu-novel-generator
```

很多 AI 小说写得平，不是因为词不够华丽，而是因为故事缺少发动机：主角没有明确欲望，冲突不升级，场景只在解释，结尾没有余味。这个 skill 把“优秀作家的可泛化叙事技法”整理成可复用流程，用来生成完整中文短篇，或把一个疲软片段改成更有钩子、更有压迫感、更有反转余味的故事。

## 真实输出预览

| 输入类型 | 生成物 |
|---|---|
| 江湖悬疑、命运压力、交易与误判 | [《雨夜验剑》](examples/sample-01-wuxia-suspense.md) |
| 近未来科幻、记忆交易、身份反转 | [《第七枚记忆》](examples/sample-02-sci-fi-memory.md) |

这个 skill 不复刻受版权保护文本，不复制名场面、签名句、人物设定或可识别情节链；如果用户提到某位作家，会把它转换成悬念、留白、对白张力、命运感、类型爽点、心理压迫、结构反转和意象控制等通用技法。

## 安装

前置条件：

- [ ] 已安装 Node.js，并能运行 `node -v`
- [ ] 已安装 npm/npx，并能运行 `npx --version`
- [ ] 使用的 Agent 支持本地 skills，或支持通过 `npx skills add` 安装 GitHub skill

安装：

```bash
npx skills add joeseesun/qiaomu-novel-generator
```

验证可发现：

```bash
npx skills add joeseesun/qiaomu-novel-generator --list
```

## 你可以这样说

- “用 qiaomu-novel-generator，写一个不会武功的书生误入江湖死局的完整短篇。”
- “这个小说开篇太平了，强化钩子、人物欲望、冲突升级和结尾余味。”
- “科幻悬疑：人可以出售记忆，但主角发现自己卖掉了谋杀证据。”
- “参考武侠的命运感、悬疑的信息差和短篇小说的留白，写成原创故事，不要仿写具体作者。”

## 它会做什么

1. 识别输入类型、目标题材、读者期待和隐含限制。
2. 提炼主角欲望、可见障碍、隐藏压力、道德代价和结尾余味。
3. 选择 3-5 个叙事技法引擎，而不是拼贴某个作家的表面腔调。
4. 设计开篇扰动、三次以上冲突升级、关键反转和回响式结尾。
5. 生成原创、完整的中文短篇小说。
6. 在样例或评测场景中，从开篇钩子、人物欲望、冲突升级、对白张力、画面感、反转/悬念、结尾余味七项自检。
7. 遇到用户反馈时，先归因失败模式，再决定是局部重写，还是沉淀为可迁移规则。

## 适合场景

- 从一句梗概生成完整短篇
- 把已有片段改成更抓人的开篇
- 强化主角动机、爽点、打脸、悬疑、反转和结尾余味
- 写武侠、修仙、都市职场、科幻悬疑、奇幻、现实题材等中文故事样章
- 把一次创作反馈沉淀为可持续优化的写作流程

## 质量边界

- 允许借鉴通用技法：悬念、留白、命运压力、类型承诺、心理压迫、对白张力、结构反转。
- 不复制受版权保护文本、名场面、人物、地名、招式、签名句或可识别情节链。
- 不直接模仿在世作者的完整个人风格。
- 如果用户要求敏感题材，优先做虚构化、非指导性、以人物选择为中心的处理。

## 开发与验证

```bash
cd ~/.agents/skills/qiaomu-novel-generator
python3 scripts/validate_skill.py
python3 /Users/joe/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
python3 scripts/evaluate_story.py examples/sample-01-wuxia-suspense.md
python3 scripts/evaluate_story.py examples/sample-02-sci-fi-memory.md
```

包结构：

```text
SKILL.md
README.md
manifest.json
agents/interface.yaml
agents/openai.yaml
references/technique-matrix.md
references/output-contract.md
references/quality-checklist.md
references/genre-quality-rubric.md
references/evolution-loop.md
examples/sample-01-wuxia-suspense.md
examples/sample-02-sci-fi-memory.md
scripts/validate_skill.py
scripts/evaluate_story.py
```

## Troubleshooting

| 问题 | 常见原因 | 处理方式 |
|---|---|---|
| `npx skills add` 找不到 skill | `SKILL.md` frontmatter 解析失败，或仓库未发布到默认分支 | 先运行 `npx skills add joeseesun/qiaomu-novel-generator --list`，确认能看到 `qiaomu-novel-generator` |
| 已安装但没有自动触发 | 当前 Agent 不支持隐式 skill 调用，或输入没有命中小说/故事类触发词 | 明确说“用 qiaomu-novel-generator 写……” |
| 故事变成设定说明 | 输入里没有主角欲望、代价或危险 | 追加“主角想要什么、失去什么、谁在阻止他” |
| 想模仿某位作家 | 直接仿写在世作者风格或复制经典段落不合适 | 改成“使用悬念、留白、对白张力、命运压力等通用技法” |

## Author

Copyright (c) 向阳乔木

- X: https://x.com/vista8
- GitHub: https://github.com/joeseesun/

## License

MIT. See [LICENSE](LICENSE).

---

<a name="english"></a>

## English

`qiaomu-novel-generator` is an agent skill for generating original Chinese short fiction from a theme, character setup, synopsis, trope, or draft excerpt. It focuses on narrative craft rather than style cloning: hook, desire, escalation, tense dialogue, concrete imagery, reversal, suspense, and an ending that echoes.

Install:

```bash
npx skills add joeseesun/qiaomu-novel-generator
```

Try:

- "Use qiaomu-novel-generator to write a complete Chinese short story from this wuxia suspense idea."
- "Rewrite this flat opening with a stronger hook, clearer desire, escalating conflict, and a lingering ending."
- "Sci-fi suspense: people can sell memories, and the protagonist discovers they sold the evidence of a murder."

This skill does not copy protected text, famous scenes, signature lines, unique characters, or recognizable plot chains, and it does not directly imitate a living author's distinctive style.
