---
name: academic-paper-evidence
description: Parse an academic paper, reconstruct its research design, and build a traceable evidence map for downstream video writing.
---

# Academic Paper Evidence

## Purpose

Answer one question:

> **What does the paper actually establish, and where is the evidence?**

Do not optimize for entertainment here. Optimize for scholarly fidelity and traceability.

## Inputs

- paper PDF / DOCX / extracted text
- optional user notes about the paper

## Outputs

- `paper.json`
- `evidence_map.json`

## Paper extraction

Capture when available:
- title and authors;
- abstract;
- section hierarchy;
- paragraphs with page provenance;
- figures and captions;
- tables and captions;
- equations;
- appendix material;
- references.

Preferred tools:
- Docling for document structure;
- PyMuPDF for page geometry, rendering, and crops.

## Research structure

Identify:
- research question;
- theoretical motivation;
- unit of analysis;
- population and period;
- data and sample;
- treatment/exposure/key predictors;
- outcomes;
- method / identification strategy;
- main findings;
- mechanisms;
- heterogeneity;
- robustness;
- limitations;
- contribution.

Separate clearly:
- what the authors measure;
- what they estimate;
- what they infer;
- what they speculate.

## Claim classes

Use stable claim IDs such as `C001`.

Allowed classes:
- `FACT`
- `METHOD`
- `EMPIRICAL_RESULT`
- `THEORETICAL_CLAIM`
- `INTERPRETATION`
- `LIMITATION`
- `BACKGROUND`
- `METAPHOR`

## Evidence rules

### EMPIRICAL_RESULT
Must have direct provenance. Preserve:
- direction;
- scale;
- uncertainty when material;
- subgroup / model / specification;
- exact unit of the statistic.

Do not silently convert:
- odds to probability;
- percent to percentage points;
- association to causation;
- conditional estimates to population-wide statements.

### METHOD
Must have direct paper support. Record enough detail to prevent later scripts from inventing identification strength.

### INTERPRETATION
Mark whether it is:
- explicitly stated by the authors;
- a cautious synthesis of paper evidence;
- a video-side explanatory gloss.

### METAPHOR
May lack paper evidence but must never be presented as an empirical result.

## Generative-visual policy

For each claim, record whether generative visuals are allowed.

Default:
- METHOD → false
- EMPIRICAL_RESULT → false
- paper-derived FACT with exact visual identity → false
- metaphor / context → may be true

## Narrative role hint

Evidence extraction may optionally assign:
- `setup`
- `surprise`
- `proof`
- `escalation`
- `explanation`
- `qualification`
- `payoff`

This is a hint only; final narrative decisions belong to the script skill.

## Completion criteria

Evidence work is ready for script writing when:
- the core research question is clear;
- all candidate major findings have claim IDs;
- methods and limitations are represented;
- high-value numeric claims are traceable;
- causal language boundaries are explicit;
- important ambiguities are surfaced rather than guessed.

Use `schemas/evidence.schema.json` as the machine-readable contract.
