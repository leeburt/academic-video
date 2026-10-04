---
name: academic-video-qa
description: Audit an academic research video for scholarly accuracy, narrative quality, visual provenance, continuity, captions, audio, and export integrity.
---

# Academic Video QA

## Purpose

Decide whether the current script or draft video is safe and strong enough to lock or export.

Inputs may include:
- `evidence_map.json`
- `narrative_plan.json`
- `script.lock.md`
- `storyboard.json`
- `manifest.json`
- `draft.mp4`

Outputs:
- `qa/script_qa.json`
- `qa/final_qa.json`
- `final.mp4` only if critical checks pass

## Script QA

### Academic accuracy

Check:
- empirical claims have claim IDs;
- numbers match the source;
- signs and directions match;
- odds, probabilities, percentages, and percentage points are not confused;
- observational associations are not upgraded to causal claims;
- author speculation is not stated as established mechanism;
- proxy measures are described with appropriate caution;
- population and time window are not silently broadened;
- material limitations are preserved.

### Narrative quality

Check:
- one clear core question;
- a concrete viewer promise;
- first meaningful value arrives early;
- each beat changes understanding;
- major findings form a chain rather than a list;
- the strongest surprise is not buried;
- method appears only when useful;
- the ending resolves the opening question.

### Anti-paper-summary

Revise if the script is basically:

```text
background → data → method → finding 1 → finding 2 → finding 3 → limitation
```

### Tonal maturity

Flag:
- childish allegory;
- invented villains;
- forced sentiment;
- promotional hype;
- abstract rhetoric without empirical cash-out;
- IP characters dominating the research.

Suggested 1–5 scores:
- tension density;
- specificity;
- cognitive progression;
- tonal maturity;
- evidence integration.

Any score below 3 requires revision.

## Final QA

### Academic

Re-check:
- spoken claims;
- on-screen numbers;
- figure/table identity;
- causal language;
- source labels;
- generated visuals not masquerading as evidence.

### Narrative

Check:
- hook and ending connect;
- viewer promise is delivered;
- no redundant middle;
- evidence appears because the viewer needs it;
- limitation protects interpretation without derailing pacing.

### Visual

Check:
- each important narration unit has a meaningful visual;
- evidence is readable;
- characters are consistent;
- characters do not block evidence;
- transitions are coherent;
- no obvious generative artifacts;
- paper graphics retain identity.

### Technical

Check:
- valid frames;
- intelligible audio;
- synchronized captions;
- correct aspect ratio;
- target duration;
- successful final encode.

## Failure handling

Critical academic or evidence failure:
- do not export;
- revise the relevant upstream stage.

Narrative weakness:
- return to script.

Visual mismatch:
- return to storyboard or production.

Technical failure:
- rerender or recompose without changing claims.

QA is a gate, not a cosmetic report.
