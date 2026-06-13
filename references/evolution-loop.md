# Evolution Loop

Use this file when the user critiques a story, asks why an output failed, or wants the skill to improve over time.

The goal is to learn transferable craft rules without hard-coding one draft, one user phrase, one genre, or one story premise into the skill.

## Hook Pipeline

```text
User request
-> Intent Hook: identify genre, reader promise, output shape, and key risk
-> Draft Hook: write one complete story or revision
-> Quality Hook: check generic and genre-specific failure modes
-> Rewrite Hook: fix the most damaging failure first
-> Feedback Hook: classify user critique into reusable failure types
-> Evolution Hook: decide whether to store as task-local note, eval case, or stable rule
```

## Failure Taxonomy

Classify feedback before rewriting.

| Feedback symptom | Transferable failure type | Rewrite direction |
|---|---|---|
| boring, flat, no hook | weak disturbance or weak reader promise | start closer to danger, shame, desire, or irreversible loss |
| feels like an essay, report, lesson, recap, tutorial | exposition dominance | replace explanation with scene, action, conflict, object, and dialogue |
| too much jargon or abstract language | abstraction overload | translate terms into human stakes and concrete events |
| not satisfying, not爽 | missing public reversal or payoff | build a visible arena where the protagonist's value is proven |
| protagonist feels weak or wrong | misframed character competence | distinguish true incompetence from unfamiliar rules, hidden skill, or blocked expression |
| conflict does not escalate | flat obstacle chain | close a safe option, add time pressure, raise cost, or expose a secret |
| ending has no aftertaste | missing image return | make the final image repay an earlier detail with changed meaning |
| genre feels wrong | reader promise mismatch | load the genre-specific rubric before rewriting |

## Rule Promotion

Do not update core rules after every critique. Promote feedback in layers:

1. Task-local fix: use when the feedback only applies to the current draft.
2. Candidate lesson: store mentally or in an iteration note when it may recur.
3. Eval case: create an example when the failure is useful for future testing.
4. Stable rule: update `quality-checklist.md`, `genre-quality-rubric.md`, or `output-contract.md` only when the lesson is repeated, high-signal, and genre-transferable.

## Do Not Overfit

- Do not add a rule that names one draft's characters, objects, company, setting, or plot.
- Do not turn one user's word choice into a universal ban.
- Do not make a genre-specific rule global unless it also improves other genres.
- Do not preserve a bad output as a positive example. Use it only as a failure case if needed.
- Do not let metrics replace taste. Metrics are smoke alarms, not judges.

## Feedback Hook Procedure

When the user critiques an output:

1. Restate the likely failure mode in one short sentence.
2. Identify whether it is task-local, genre-level, or global craft-level.
3. Rewrite the story or relevant section against the dominant failure.
4. If updating the skill, write an abstract rule and place it in the narrowest useful reference file.
5. Run `scripts/validate_skill.py` after editing the skill.

## Evolution Hook Procedure

When updating the skill:

1. Prefer references over bloating `SKILL.md`.
2. Keep rules phrased as reader-effect and craft behavior, not one-off content.
3. Add scripts only for repeatable checks that are cheap and non-authoritative.
4. Validate structure and any changed scripts.
5. If a rule starts hurting good outputs, loosen it or move it from hard rule to diagnostic.
