"""Tests for player collision, terrain support and camera obstruction."""
import pytest

from engine.physics.collision_world import AABB, CollisionWorld, GroundSurface


def make_world():
    return CollisionWorld(
        obstacles=[AABB(-1, 1, 2, 4, 0, 2)],
        world_limit=10,
    )


def test_player_stops_before_obstacle():
    world = make_world()
    x, y = world.move_horizontal(0, 0, 0, 0, 5, radius=0.5)
    assert x == pytest.approx(0)
    assert y == pytest.approx(1.5)


def test_player_can_pass_over_obstacle_when_body_is_above_it():
    world = make_world()
    x, y = world.move_horizontal(0, 0, 2.1, 0, 5, radius=0.5)
    assert x == pytest.approx(0)
    assert y == pytest.approx(5)


def test_world_bounds_include_player_radius():
    world = make_world()
    x, y = world.move_horizontal(0, 0, 0, 50, 0, radius=0.5)
    assert x == pytest.approx(9.5)
    assert y == pytest.approx(0)


def test_raised_surface_blocks_walking_but_is_reachable_by_jump():
    world = CollisionWorld(
        surfaces=[GroundSurface(-2, 2, 2, 5, 1.0)],
        world_limit=10,
    )
    x, y = world.move_horizontal(
        0, 0, 0, 0, 4, grounded=True, max_step_height=0.35
    )
    assert y == pytest.approx(0)

    x, y = world.move_horizontal(
        0, 0, 0, 0, 4, grounded=False, max_step_height=0.35
    )
    assert y == pytest.approx(4)
    assert world.ground_height_at(x, y) == pytest.approx(1.0)


def test_ground_query_uses_highest_surface_under_player():
    world = CollisionWorld(
        surfaces=[
            GroundSurface(-5, 5, -5, 5, 0.4),
            GroundSurface(-1, 1, -1, 1, 1.2),
        ]
    )
    assert world.ground_height_at(0, 0) == pytest.approx(1.2)
    assert world.ground_height_at(3, 3) == pytest.approx(0.4)


def test_camera_is_pulled_forward_before_obstacle():
    world = make_world()
    position = world.resolve_camera_position((0, 0, 1), (0, 6, 1))
    assert position[1] < 2
    assert position[1] > 1


def test_camera_position_is_unchanged_without_obstruction():
    world = make_world()
    desired = (5, 0, 3)
    assert world.resolve_camera_position((0, 0, 1), desired) == desired


def test_invalid_world_limit_is_rejected():
    with pytest.raises(ValueError):
        CollisionWorld(world_limit=0)
