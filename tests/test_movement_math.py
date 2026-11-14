"""Tests for camera-relative player movement math."""
import math

import pytest

from engine.player.movement_math import camera_relative_direction


def test_forward_at_zero_heading_points_along_positive_y():
    assert camera_relative_direction(1, 0, 0) == pytest.approx((0, 1))


def test_right_at_zero_heading_points_along_positive_x():
    assert camera_relative_direction(0, 1, 0) == pytest.approx((1, 0))


def test_forward_rotates_with_camera_heading():
    assert camera_relative_direction(1, 0, 90) == pytest.approx((1, 0), abs=1e-7)


def test_backward_is_opposite_forward():
    assert camera_relative_direction(-1, 0, 0) == pytest.approx((0, -1))


def test_diagonal_input_is_normalized():
    x, y = camera_relative_direction(1, 1, 0)
    assert math.hypot(x, y) == pytest.approx(1.0)


def test_idle_input_returns_zero_vector():
    assert camera_relative_direction(0, 0, 45) == (0, 0)
