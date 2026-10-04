---
name: academic-video
description: Orchestrate an evidence-grounded workflow for turning academic papers into short research videos. Delegate paper analysis, script writing, storyboard design, production, and QA to specialist skills.
---

# Academic Video Orchestrator

## Goal

Turn an academic paper into an accurate, clear, engaging research video without flattening it into a paper summary.

The orchestrator owns workflow order and handoffs. Specialist skills own domain-specific reasoning.

## Highest-priority rules

1. **Evidence decides what can be said.**
2. **The viewer's question decides when it should be said.**
3. **Use the paper's native tension before inventing a story.**
4. **Never use generative video to fabricate empirical evidence.**
5. **Do not begin expensive rendering before the script is locked.**

## Default workflow

```text
Paper
  ↓
1. Paper & Evidence
  ↓
2. Narrative & Script
  ↓
3. Storyboard
  ↓
4. Production
  ↓
5. QA & Export
```

## Specialist skills

Use the relevant specialist when entering each stage:

- `skills/academic-paper-evidence/SKILL.md`
- `skills/academic-video-script/SKILL.md`
- `skills/academic-video-storyboard/SKILL.md`
- `skills/academic-video-production/SKILL.md`
- `skills/academic-video-qa/SKILL.md`

Shared schemas and design references live in `schemas/` and `references/`.

## Stage gates

### Gate 1 — Evidence ready
Do not write the final narration until:
- core research question is identified;
- major empirical claims have stable claim IDs;
- empirical results and methods have direct provenance;
- causal strength and limitations are known.

Expected outputs:
- `paper.json`
- `evidence_map.json`

### Gate 2 — Script ready
Do not storyboard until:
- one core audience question is chosen;
- the viewer promise is explicit;
- the paper's native tension has been tested;
- findings form a progressive argument rather than a list;
- script QA passes;
- `script.lock.md` exists.

Expected outputs:
- `narrative_plan.json`
- `script.md`
- `script.lock.md`

### Gate 3 — Storyboard ready
Do not batch-render until:
- narration timing is based on draft TTS or measured speech;
- evidence-bearing shots use deterministic or source-faithful visuals;
- scene/shot continuity is specified;
- generative-video shots contain no empirical numbers, tables, or paper figures.

Expected output:
- `storyboard.json`

### Gate 4 — Production ready
Production may generate:
- paper crops and extracted figures;
- deterministic diagrams and charts;
- method animation;
- voice and captions;
- contextual or metaphorical generative footage.

Expected outputs:
- `assets/`
- `manifest.json`
- `draft.mp4`

### Gate 5 — Final QA
Export `final.mp4` only after academic, narrative, visual, and technical checks pass.

## Default content budget for 60–120 seconds

Use as a constraint, not a quota:

- 1 core question
- 1 core tension
- 2–3 major findings
- 0–1 method explanation
- 0–1 mechanism
- 2–4 spoken numbers
- 1 necessary limitation
- 1 final takeaway

## Default narrative policy

Do not mechanically map paper sections into video sections.

Avoid:
```text
background → data → method → finding 1 → finding 2 → finding 3 → limitation
```

Prefer:
```text
question → expected answer → finding → surprise → new question → deeper finding → revised understanding
```

If a paper already contains a strong empirical paradox, expectation reversal, unequal conversion, or escalating puzzle, use that as the narrative engine.

## Story policy

`story_mode` is conditional, not required.

A fictional story is justified only when it materially reduces abstraction or creates a question the paper later answers.

Never use a fictional character's intentional action to stand in for a social mechanism the paper did not identify.

## Default character IP

If the project uses 勤劳牛 / 发疯马, treat them as cognitive interfaces rather than story protagonists:

- 发疯马: ordinary intuition, fast judgment, common misunderstanding, skepticism.
- 勤劳牛: evidence, anomaly detection, correction, cautious interpretation.

They may ask, challenge, point, or explain. They must not replace evidence or embody an unverified causal mechanism.

## Rendering policy

Evidence-bearing content:
- paper figure/table → source asset or deterministic animation;
- coefficients/numbers → deterministic typography/chart;
- methods/equations → deterministic animation;
- concepts/mechanisms → deterministic diagram unless clearly metaphorical.

Generative video:
- context;
- character performance;
- metaphor;
- non-evidence transitions.

Never generate fake empirical charts, regression coefficients, sample statistics, or paper figures.

## Core outputs

```text
output/
├── paper.json
├── evidence_map.json
├── narrative_plan.json
├── script.md
├── script.lock.md
├── storyboard.json
├── manifest.json
├── assets/
├── audio/
├── subtitles/
├── qa/
│   ├── script_qa.json
│   └── final_qa.json
├── draft.mp4
└── final.mp4
```

## When the user asks for only part of the workflow

Do not force the full pipeline.

Examples:
- "只写脚本" → run evidence + script stages only.
- "只做分镜" → require or recover a locked script, then run storyboard.
- "检查这版视频" → run QA only.
- "从论文做完整视频" → run the full workflow.

Keep the orchestrator short. Put detailed reasoning rules in the specialist skills and shared references.
