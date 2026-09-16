# Academic Video

**Evidence-grounded agentic workflow for turning academic papers into research videos.**

Academic Video is an experimental open-source project for converting academic papers into short, accurate, visually clear research videos. The project is designed around a simple principle:

> Generative models may explain the evidence, but they must not invent the evidence.

Instead of treating paper-to-video as a single summarization prompt, Academic Video separates the workflow into structured stages:

1. **Paper parsing** — extract sections, figures, tables, equations, and page-level provenance.
2. **Research mapping** — identify research questions, data, methods, findings, contributions, and limitations.
3. **Evidence mapping** — link every empirical claim to its source in the paper.
4. **Narrative planning** — convert the research structure into a concise video narrative.
5. **Scene routing** — choose the appropriate renderer for each scene.
6. **Rendering** — combine deterministic motion graphics, academic animation, and optional generative video.
7. **Voice and captions** — synthesize narration and align subtitles.
8. **Academic QA** — verify claims, numbers, directions, figures, and audiovisual integrity.

## Core design

```text
paper.pdf
   |
   v
Paper Parser
   |
   v
Research Map + Evidence Map
   |
   v
Narrative Planner
   |
   v
Storyboard
   |
   v
Scene Router
   |-----------------------------|
   |              |              |
   v              v              v
Evidence       Diagram        Cinematic
Scenes         Scenes         Scenes
   |              |              |
HyperFrames    Manim          Video model
   |              |              |
   |--------------|--------------|
                  v
               Composer
                  |
                  v
              Academic QA
                  |
                  v
              final.mp4
```

## Rendering policy

Empirical evidence should use deterministic renderers whenever possible.

| Scene type | Preferred renderer |
|---|---|
| Paper figure/table | HyperFrames / direct asset animation |
| Numeric result | HyperFrames |
| DID / event study / DAG / equations | Manim or HyperFrames |
| Conceptual mechanism | HyperFrames / Manim |
| Contextual or metaphorical scene | Generative video model |
| Titles / takeaways / typography | HyperFrames |

Generative video must **not** be used to fabricate regression coefficients, tables, empirical figures, sample sizes, or other evidence-bearing visuals.

## Planned open-source stack

- **Docling** — document structure extraction
- **PyMuPDF** — precise page rendering and figure/table crops
- **HyperFrames** — deterministic motion graphics and composition
- **Manim Community** — academic and methodological animations
- **Qwen3-TTS / edge-tts** — narration
- **WhisperX** — word-level alignment and subtitles
- **FFmpeg** — composition and encoding
- Optional video backends: Seedance, Veo, Runway, Wan/ComfyUI

## Development roadmap

### V0 — End-to-end prototype
PDF → extracted assets → narration → simple storyboard → deterministic render → MP4.

### V1 — Evidence grounding
Introduce claim IDs, evidence IDs, source provenance, and restrictions on generative visuals.

### V2 — Scene router + social-science templates
Add reusable templates for figures, tables, coefficients, DID, event studies, mechanisms, timelines, and takeaways.

### V3 — Manim renderer
Add methodological and mathematical animation support.

### V4 — Generative video router
Add provider adapters for contextual/cinematic scenes while preserving evidence restrictions.

### V5 — Academic QA + regeneration
Check claim support, numeric consistency, direction consistency, visual provenance, timing, captions, and rendering quality.

## Repository status

Early-stage scaffold. The first implementation focuses on the evidence schema and routing logic before adding expensive video-generation backends.

## License

License to be selected before the first public release.
