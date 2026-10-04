---
name: academic-video-storyboard
description: Convert a locked academic-video script into a shot-level visual plan with evidence-safe rendering, timing, prompts, and continuity.
---

# Academic Video Storyboard

## Purpose

Answer one question:

> **How should each locked line of narration become a clear, continuous, evidence-safe visual sequence?**

Inputs:
- `script.lock.md`
- `evidence_map.json`
- optional IP references

Output:
- `storyboard.json`

## Timing first

Generate draft TTS or otherwise estimate real spoken duration before final shot timing.

Do not create fixed-duration shots and then force narration into them.

## Object model

Keep three levels distinct:

- **Scene** — narrative unit.
- **Shot** — timeline / generation unit.
- **Asset** — concrete media file.

A scene may contain multiple shots. A shot may use multiple assets.

## Shot requirements

Each shot should record:
- `shot_id`
- `beat_id`
- duration
- purpose: evidence / explanation / story / transition
- narration or dialogue
- claim IDs
- visual intent
- visual type
- characters
- assets
- `entry_state`
- `exit_state`
- `continuity_in`
- `continuity_out`
- `transition_type`
- renderer
- fallback renderer
- image prompt if relevant
- video prompt if relevant

## Visual types

- `paper_evidence`
- `data_visualization`
- `concept_diagram`
- `method_animation`
- `cinematic`
- `typography`

## Rendering policy

### Evidence
Use source-faithful or deterministic representation for:
- paper figures;
- paper tables;
- coefficients;
- sample statistics;
- empirical percentages;
- axes and scales;
- formulas used as evidence.

### Explanation
Use deterministic diagrams for:
- mechanisms;
- timelines;
- causal structures;
- research design;
- concept relationships.

### Generative video
Use for:
- context;
- character performance;
- metaphor;
- non-evidence transitions.

Never ask a generative video model to draw a real paper figure, regression coefficient, sample statistic, or empirical chart.

## Continuity

Adjacent shots must share at least one:
- action;
- gaze;
- object;
- composition;
- color logic;
- sound;
- narration semantics.

Prefer visual bridges when changing modes:
- an object becomes a chart;
- a whiteboard sketch becomes a paper figure;
- a character points toward a real evidence graphic;
- a repeated shape or phrase carries the transition.

Do not rely on hard cuts for every transition.

## IP continuity

If using fixed characters, read the project character bible and use the same references across shots.

Characters may:
- ask;
- react;
- point;
- compare;
- explain.

They must not:
- cover key evidence;
- become the evidence;
- embody an unverified causal mechanism.

## Evidence entrance and exit

When a paper figure or numeric result appears:
- introduce why the viewer is seeing it;
- visually highlight only the relevant part;
- exit the evidence with a clear interpretive transition.

Avoid dumping full paper pages without guidance.

## Prompt rule

Prompts describe composition, action, and camera movement. They must not invent empirical content.

Keep paper text, labels, exact numbers, and figures as post-production overlays or deterministic elements.

Use `schemas/storyboard.schema.json` as the machine-readable contract.
