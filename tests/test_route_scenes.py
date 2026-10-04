import pytest

from scripts.route_scenes import Claim, assert_route_safe, choose_renderer


def test_empirical_claim_routes_to_deterministic_renderer():
    claims = [
        Claim(
            claim_id="C001",
            type="EMPIRICAL_RESULT",
            generative_visual_allowed=False,
        )
    ]
    assert choose_renderer("data_visualization", claims) == "hyperframes"


def test_method_animation_routes_to_manim():
    claims = [
        Claim(
            claim_id="C002",
            type="METHOD",
            generative_visual_allowed=False,
        )
    ]
    assert choose_renderer("method_animation", claims) == "manim"


def test_contextual_claim_can_route_to_video_model():
    claims = [
        Claim(
            claim_id="C003",
            type="METAPHOR",
            generative_visual_allowed=True,
        )
    ]
    assert choose_renderer("cinematic", claims) == "video_model"


def test_fail_closed_when_evidence_is_sent_to_video_model():
    claims = [
        Claim(
            claim_id="C004",
            type="EMPIRICAL_RESULT",
            generative_visual_allowed=False,
        )
    ]
    with pytest.raises(ValueError):
        assert_route_safe("video_model", claims)
