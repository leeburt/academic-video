# Academic Video

**Evidence-grounded, narrative-first workflow for turning academic papers into research videos.**

Academic Video is an experimental open-source project for converting academic papers into short research videos that are both **scholarly accurate** and **worth watching**.

The project follows four principles:

> **Evidence decides what can be said.**  
> **The viewer's question decides when it should be said.**  
> **The paper's native tension comes before an invented story.**  
> **Generative models may explain evidence, but must not invent it.**

## Why the repository is modular

Paper analysis, script writing, storyboard design, rendering, and QA are different reasoning tasks. Instead of putting every rule into one giant prompt, the repository uses a small orchestrator plus specialist skills.

```text
academic-video
│
├── SKILL.md                           # workflow orchestrator
├── skills/
│   ├── academic-paper-evidence/       # paper parsing + evidence map
│   ├── academic-video-script/         # narrative + script
│   ├── academic-video-storyboard/     # scene/shot visual design
│   ├── academic-video-production/     # rendering, TTS, captions, compose
│   └── academic-video-qa/             # academic + narrative + AV QA
├── references/                        # shared design rules
├── schemas/                           # machine-readable contracts
├── scripts/                           # executable helpers
└── examples/
```

This keeps the main skill small and lets each specialist focus on one job.

## Core workflow

```text
paper.pdf
   ↓
Paper & Evidence
   ↓
Narrative & Script
   ↓
Storyboard
   ↓
Production
   ↓
Final QA
   ↓
final.mp4
```

### 1. Paper & Evidence

Extract the research structure and create stable claim IDs with provenance.

Outputs:
- `paper.json`
- `evidence_map.json`

### 2. Narrative & Script

Choose the core audience question, identify the paper's native tension, build an expectation–surprise progression, and write a concise spoken script.

Outputs:
- `narrative_plan.json`
- `script.md`
- `script.lock.md`

### 3. Storyboard

Translate the locked script into scenes and shots. Evidence visuals are source-faithful or deterministic; generative visuals are reserved for context and metaphor.

Output:
- `storyboard.json`

### 4. Production

Generate or extract assets, synthesize speech, align captions, render shots, and compose the draft.

Outputs:
- `assets/`
- `manifest.json`
- `draft.mp4`

### 5. QA

Check academic accuracy, narrative progression, visual provenance, continuity, captions, audio, and final encoding.

Outputs:
- `qa/script_qa.json`
- `qa/final_qa.json`
- `final.mp4`

## Narrative design

The project explicitly avoids turning a paper into a section-by-section summary.

Avoid:

```text
background → data → method → finding 1 → finding 2 → finding 3 → limitation
```

Prefer:

```text
question
→ expected answer
→ actual finding
→ surprise
→ new question
→ deeper finding
→ revised understanding
```

A fictional story is optional. If the paper already contains a strong paradox or expectation reversal, that should drive the video.

## Evidence policy

Empirical claims must be traceable to the source paper.

| Content | Preferred representation |
|---|---|
| Paper figure/table | Original asset or faithful animation |
| Numeric result | Deterministic typography / chart |
| DID / event study / equation | Manim / HyperFrames |
| Conceptual mechanism | Deterministic diagram |
| Context / metaphor / character acting | Generative video allowed |
| Titles / takeaways | Deterministic typography |

Generative video must **not** fabricate regression coefficients, tables, empirical figures, sample sizes, or other evidence-bearing visuals.

## Existing executable safety rule

`scripts/route_scenes.py` fails closed when evidence-bearing claims are accidentally routed to a generative video renderer.

## Planned / compatible stack

- **Docling** — document structure extraction
- **PyMuPDF** — page rendering and crops
- **HyperFrames** — deterministic motion graphics
- **Manim Community** — methods and mathematical animation
- **Qwen3-TTS / edge-tts** — narration
- **WhisperX** — alignment and subtitles
- **FFmpeg** — composition and encoding
- Optional video backends: Seedance, Veo, Runway, Wan/ComfyUI

## Repository status

Early-stage scaffold. The current architecture prioritizes evidence contracts and narrative quality before expensive rendering backends.

## License

License to be selected before the first public release.
