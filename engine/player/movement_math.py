"""Small deterministic helpers for camera-relative player movement."""
from math import cos, sin, radians, hypot


def camera_relative_direction(forward: float, right: float, heading_degrees: float) -> tuple[float, float]:
    """Convert input axes into a normalized world-space X/Y direction.

    Panda3D uses +Y as forward and +X as right. Heading zero faces +Y.
    """
    magnitude = hypot(forward, right)
    if magnitude == 0:
        return 0.0, 0.0
    forward /= magnitude
    right /= magnitude
    angle = radians(heading_degrees)
    x = right * cos(angle) + forward * sin(angle)
    y = forward * cos(angle) - right * sin(angle)
    return x, y
