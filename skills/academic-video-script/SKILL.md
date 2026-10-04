---
name: academic-video-script
description: Turn an evidence map into a concise, mature, high-retention academic video narrative and lock the final spoken script.
---

# Academic Video Script

## Purpose

Answer one question:

> **How should this paper be told so that the viewer keeps learning and keeps watching?**

Inputs:
- `paper.json`
- `evidence_map.json`

Outputs:
- `narrative_plan.json`
- `script.md`
- `script.lock.md`
- `qa/script_qa.json`

## Core rules

1. Evidence decides what can be said.
2. The viewer's active question decides when it should be said.
3. The paper's native tension comes before an invented story.
4. A script is not a compressed abstract.
5. Academic accuracy preserves meaning, not academic wording.

## Content budget

For 60–120 seconds, default to:
- one core audience question;
- one core tension;
- two or three major findings;
- at most one method explanation;
- at most one mechanism;
- two to four spoken numbers;
- one necessary limitation;
- one final takeaway.

Treat these as upper bounds, not targets.

## Step 1 — Find the paper's native tension

Test for:

- **Expectation reversal**: we expect A, but observe B.
- **Outcome contradiction**: two outcomes coexist although intuition predicts otherwise.
- **Unequal conversion**: similar or greater input produces unequal return.
- **Puzzle escalation**: each result makes the initial puzzle harder.
- **Mechanism puzzle**: the obvious explanation does not fully account for the result.

If the native tension is already strong, do not invent a fictional story.

## Step 2 — Define four anchors

Write explicitly:

- **Audience Question** — what a non-specialist naturally wants to know.
- **Viewer Promise** — what the viewer will understand by the end.
- **Core Surprise** — the finding that most changes prior expectations.
- **Final Takeaway** — the revised understanding that remains after the video.

These are not interchangeable.

## Step 3 — Build an expectation–surprise ladder

For each major beat:

```text
Question
→ Expected answer
→ Actual finding
→ Surprise / correction
→ New question
```

Major findings must form a chain, not a list.

Bad:
```text
finding 1
finding 2
finding 3
```

Better:
```text
finding
→ puzzle
→ deeper finding
→ explanation or revised understanding
```

## Step 4 — Design beats

A beat is the smallest unit in which the viewer's understanding changes.

For each beat record:
- viewer state before;
- active question;
- new information;
- viewer state after;
- surprise / correction;
- next question;
- supporting claim IDs.

If understanding does not change, merge or delete the beat.

Typical 60–120 second video: 6–10 meaningful beats.

## Step 5 — Choose the hook

Compare several hook types:
- counterintuitive finding;
- expectation reversal;
- unresolved question;
- result first;
- concrete real example;
- contrast case;
- abnormal number;
- fictional story.

Priority:
```text
paper-native tension
> real concrete example
> explanatory story
> pure fictional story
```

The first valuable idea should arrive early. Do not hide the strongest result behind long setup.

## Story necessity test

Use a fictional story only if it:
- materially reduces abstraction;
- creates a question the paper later answers;
- provides a stable explanatory model;
- is needed because the paper lacks a sufficiently strong native tension.

Otherwise, skip it.

## Anti-fable rule

Never use a fictional person's intentional behavior to stand in for an unverified social mechanism.

For example, if a paper shows lower uptake of one group's innovation, do not depict another person deliberately rejecting it unless the paper directly identifies that mechanism.

Characters may represent intuition or questions; they may not invent causality.

## Metaphor cash-out rule

Metaphor is allowed, but it must quickly resolve into a measurable research object.

Example:

> "Which innovations are remembered by science?"

Then clarify:

> "Here, 'remembered' means that a newly introduced concept link is reused in later papers."

Avoid long chains of empty phrases such as "seen", "caught", "opened a door", "left a mark" without empirical translation.

## Method placement

Do not insert methods because the paper has a Methods section.

Use method explanation when:
- it answers viewer skepticism ("could this just be...?"); or
- the method itself is the paper's contribution.

Method should earn its place.

## Character IP: 勤劳牛 / 发疯马

Use them as cognitive interfaces.

- 发疯马: intuition, haste, common misconception, skepticism.
- 勤劳牛: anomaly detection, evidence, correction, cautious explanation.

Good:
> 马：既然更创新，不应该更容易成功吗？  
> 牛：问题就在这里，结果恰恰相反。

Bad:
> 马 deliberately suppresses 牛's innovation, when the paper never identified such a mechanism.

They do not need to appear in every beat.

## Spoken style

Prefer:
- short sentences;
- concrete nouns;
- one main idea per sentence;
- explicit contrast;
- spoken Chinese rather than journal prose.

Avoid repetitive academic scaffolding:
- "研究结果表明……"
- "进一步分析发现……"
- "研究还发现……"
- "综上所述……"

Use questions and contrasts where they genuinely advance cognition.

## Anti-paper-summary test

If the video can be relabeled as:

```text
background → data → method → finding 1 → finding 2 → finding 3 → limitation
```

the narrative is not ready.

Scene logic should instead follow the viewer's questions.

## Script QA

Evaluate:

### Academic accuracy
- every empirical statement has supporting claim IDs;
- numbers and directions match;
- causal language stays within evidence;
- proxy variables are not overstated;
- limitations that materially change interpretation are preserved.

### Narrative quality
- the hook creates a real question or expectation gap;
- the viewer promise is clear;
- each beat changes understanding;
- findings escalate or explain one another;
- methods appear when needed;
- the ending answers the opening question.

### Tonal maturity
Reject:
- childish allegory used in place of mechanism;
- invented villains;
- forced sentiment;
- promotional language;
- abstract rhetoric without evidence;
- character antics that dominate the science.

Score 1–5:
- tension density;
- specificity;
- cognitive progression;
- tonal maturity;
- evidence integration.

Any score below 3 requires revision.

## Locking

When QA passes, copy the final narration/dialogue into `script.lock.md`.

All downstream TTS, captions, storyboard, and prompts must use the locked script. If the script changes, downstream artifacts become stale.
