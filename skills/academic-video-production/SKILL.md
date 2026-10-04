---
name: academic-video-production
description: Produce assets, voice, captions, rendered clips, and the composed draft from an approved academic-video storyboard.
---

# Academic Video Production

## Purpose

Execute an approved storyboard without changing the paper's claims or rewriting the locked script.

Inputs:
- `script.lock.md`
- `storyboard.json`
- evidence assets
- optional IP assets

Outputs:
- `assets/`
- `audio/`
- `subtitles/`
- `manifest.json`
- `draft.mp4`

## Non-negotiable rule

Production may change **how** a claim is visualized, but not **what** the locked script says.

If a production constraint would require rewriting a claim, return to the script stage.

## Asset source classes

Use:
- `EXTRACT` — paper-derived source material;
- `DRAW` — deterministic charts, diagrams, typography, animation;
- `GENERATE` — generative image/video for non-evidence content.

Evidence-bearing material should normally be EXTRACT or DRAW.

## Renderer routing

Keep `scripts/route_scenes.py` as the fail-closed routing layer.

Default:
- paper evidence → direct asset / HyperFrames;
- numeric findings → HyperFrames;
- methods/equations → Manim or HyperFrames;
- concepts/mechanisms → deterministic diagram;
- cinematic/contextual scene → video model;
- typography → HyperFrames.

## Generative video

If Seedance is configured and available, prefer it for:
- character acting;
- contextual scenes;
- non-evidence transitions;
- metaphorical footage.

Before use, check:
- model identifier;
- API key presence;
- base URL;
- account permission;
- quota / availability.

If unavailable:
1. use another configured video backend;
2. use deterministic animation;
3. use static keyframes with voice/captions.

Never allow a failure to silently drop a required shot.

## Voice

Preferred production voice:
- Qwen3-TTS.

Fallback:
- edge-tts.

Use draft speech early for timing and final speech for delivery.

Character dialogue must preserve speaker identity and voice consistency.

## Captions

Captions must be derived from the final audio / locked text, not from an obsolete script draft.

WhisperX may be used for alignment.

## Composition

Use:
- HyperFrames for deterministic composition;
- FFmpeg for normalization, muxing, encoding, and final export.

All shots belong on one timeline.

Do not splice a separately produced story intro onto an unrelated old paper video.

## Manifest

Record for each shot and asset:
- shot ID;
- beat ID;
- claim IDs;
- script version;
- prompt hash;
- reference images;
- source class;
- renderer;
- model;
- task ID when applicable;
- actual duration;
- resolution;
- creation time;
- status;
- fallback reason.

This allows downstream invalidation when the script changes.
