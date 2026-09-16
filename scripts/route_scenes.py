from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


EVIDENCE_TYPES = {"EMPIRICAL_RESULT", "METHOD"}


@dataclass(frozen=True)
class Claim:
    claim_id: str
    type: str
    generative_visual_allowed: bool


def choose_renderer(visual_type: str, claims: Iterable[Claim]) -> str:
    """Route a scene to a renderer while enforcing evidence safety rules."""
    claims = list(claims)

    if any(c.type in EVIDENCE_TYPES for c in claims):
        if visual_type == "method_animation":
            return "manim"
        return "hyperframes"

    if not all(c.generative_visual_allowed for c in claims):
        if visual_type == "method_animation":
            return "manim"
        return "hyperframes"

    if visual_type == "cinematic":
        return "video_model"
    if visual_type == "method_animation":
        return "manim"
    if visual_type in {"paper_evidence", "data_visualization", "concept_diagram", "typography"}:
        return "hyperframes"

    raise ValueError(f"Unknown visual_type: {visual_type}")


def assert_route_safe(renderer: str, claims: Iterable[Claim]) -> None:
    """Fail closed if evidence-bearing claims are accidentally sent to a generative renderer."""
    claims = list(claims)
    if renderer == "video_model" and any(
        c.type in EVIDENCE_TYPES or not c.generative_visual_allowed for c in claims
    ):
        raise ValueError("Evidence-bearing scene cannot be routed to a generative video renderer.")
