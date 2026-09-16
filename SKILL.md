# Academic Video Skill

## Purpose

Turn an academic paper into a short, evidence-grounded research video.

The skill must preserve scholarly accuracy. It may simplify exposition, but it must never invent empirical evidence, coefficients, figures, tables, sample sizes, methods, or causal claims.

## Operating principles

1. Parse before summarizing.
2. Build an evidence map before writing narration.
3. Every empirical claim must link to a paper source.
4. Separate evidence-bearing visuals from explanatory or cinematic visuals.
5. Prefer deterministic rendering for numbers, tables, figures, methods, and equations.
6. Use generative video only for contextual, metaphorical, or non-evidence scenes.
7. Run academic QA before final export.

## Required workflow

### Stage 1 — Parse the paper
Extract:
- title
- authors
- abstract
- section hierarchy
- paragraphs with page provenance
- figures and captions
- tables and captions
- equations where available
- references where available

Preferred tools:
- Docling for structure
- PyMuPDF for page geometry, rendering, and crops

Output: `paper.json`

### Stage 2 — Build the research map
Identify:
- research question
- theoretical motivation
- data/sample
- period/population
- identification strategy / method
- main findings
- mechanisms
- heterogeneity
- robustness
- limitations
- contribution

Output: `research_map.json`

### Stage 3 — Build the evidence map
For each claim, create a stable claim ID and attach source provenance.

Claim classes:
- FACT
- METHOD
- EMPIRICAL_RESULT
- THEORETICAL_CLAIM
- INTERPRETATION
- LIMITATION
- BACKGROUND
- METAPHOR

Rules:
- EMPIRICAL_RESULT requires direct evidence.
- METHOD requires direct evidence.
- FACT should have evidence whenever paper-derived.
- METAPHOR may be unsupported but must not be presented as empirical evidence.

Each claim should specify whether generative visuals are allowed.

Output: `evidence_map.json`

### Stage 4 — Plan the narrative
Create a concise narrative appropriate for the target duration.

Default structure for a 60–120 second research video:
1. Hook / research question
2. Why the question matters
3. Data
4. Method / identification
5. Finding 1
6. Finding 2
7. Finding 3 / mechanism
8. Contribution / takeaway

Every narration unit must reference one or more claim IDs.

Output: `narrative.json`

### Stage 5 — Create the storyboard
Convert the narrative into scenes.

Each scene must include:
- scene ID
- duration
- narration
- claim IDs
- visual intent
- visual type
- required assets
- renderer

Output: `storyboard.json`

### Stage 6 — Route scenes
Allowed renderer classes:
- `paper_evidence`
- `data_visualization`
- `concept_diagram`
- `method_animation`
- `cinematic`
- `typography`

Default routing:
- empirical evidence -> deterministic renderer
- paper figures/tables -> direct asset animation
- methods/equations -> Manim or HyperFrames
- concepts/mechanisms -> HyperFrames or Manim
- contextual/metaphorical scenes -> optional generative video
- titles/takeaways -> HyperFrames

Never route an empirical coefficient, table, figure, or sample statistic to a generative video renderer.

### Stage 7 — Voice and captions
Preferred:
- Qwen3-TTS for production narration
- edge-tts as MVP fallback
- WhisperX for alignment

### Stage 8 — Compose
Preferred:
- HyperFrames for deterministic composition
- FFmpeg for normalization, muxing, encoding, and final export

### Stage 9 — Academic QA
Before final export, check:
- every empirical narration claim is supported
- numbers match source evidence
- signs/directions match
- figure/table identity matches
- no unsupported causal upgrade
- no generative visual is presented as empirical evidence
- captions are synchronized
- frames are valid
- audio exists and is intelligible

If a critical check fails, regenerate or revise the relevant scene rather than exporting the final video.

## Output structure

```text
output/
├── paper.json
├── research_map.json
├── evidence_map.json
├── narrative.json
├── storyboard.json
├── assets/
│   ├── figures/
│   ├── tables/
│   └── pages/
├── scenes/
├── audio/
├── subtitles/
├── qa/
└── final.mp4
```

## Style defaults

Visual style should be restrained, professional, and publication-adjacent rather than promotional or cyberpunk.

Prefer:
- strong typography
- clean diagrams
- readable plots
- restrained transitions
- consistent visual grammar
- visible provenance for evidence-bearing visuals

Avoid:
- fabricated dashboards
- decorative pseudo-data
- excessive cinematic effects
- illegible motion graphics
- unsupported claims added for narrative drama
