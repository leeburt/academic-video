# Architecture Reference

## Design rule

Use a specialist skill when the work requires a distinct reasoning mode. Use a reference file when the content is a shared convention. Use an executable script when the task is deterministic execution.

## Repository responsibilities

### Orchestrator
`/SKILL.md`
- stage order
- stage gates
- handoffs
- top-level safety rules

### Specialist skills
`/skills/*/SKILL.md`
- paper evidence reasoning
- narrative/script reasoning
- storyboard reasoning
- production decisions
- QA decisions

### References
`/references/`
- stable conventions
- visual style
- IP definitions
- architecture notes

### Schemas
`/schemas/`
- machine-readable contracts
- not prose reasoning

### Scripts
`/scripts/`
- deterministic execution
- routing
- rendering helpers
- validation
- composition

## Avoid over-fragmentation

Do not create separate skills for:
- hooks;
- beats;
- TTS;
- captions;
- Seedance;
- manifest writing.

These are subroutines inside the five specialist domains.

## Invalidation rule

```text
evidence changes → narrative + script + storyboard + production become stale
script changes → storyboard + production become stale
storyboard changes → affected production assets become stale
production-only changes → evidence/script remain valid
```

The manifest should make this dependency chain auditable.
