"""Deterministic world-space collision and ground queries for the player/camera.

This lightweight layer deliberately avoids Panda3D dependencies so its geometry
rules can be exercised in ordinary unit tests.
"""
from dataclasses import dataclass
from math import sqrt
from typing import Iterable


@dataclass(frozen=True)
class AABB:
    """Axis-aligned obstacle bounds in world coordinates."""

    min_x: float
    max_x: float
    min_y: float
    max_y: float
    min_z: float
    max_z: float

    def __post_init__(self) -> None:
        if self.min_x > self.max_x or self.min_y > self.max_y or self.min_z > self.max_z:
            raise ValueError("AABB minimum bounds must not exceed maximum bounds")

    def expanded(self, amount: float) -> "AABB":
        return AABB(
            self.min_x - amount, self.max_x + amount,
            self.min_y - amount, self.max_y + amount,
            self.min_z - amount, self.max_z + amount,
        )


@dataclass(frozen=True)
class GroundSurface:
    """A rectangular walkable surface whose top is at height."""

    min_x: float
    max_x: float
    min_y: float
    max_y: float
    height: float

    def contains(self, x: float, y: float) -> bool:
        return self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y


class CollisionWorld:
    """Small AABB collision world with sliding, ground queries and camera clipping."""

    def __init__(
        self,
        obstacles: Iterable[AABB] = (),
        surfaces: Iterable[GroundSurface] = (),
        world_limit: float = 22.0,
        default_ground_height: float = 0.0,
    ) -> None:
        if world_limit <= 0:
            raise ValueError("world_limit must be positive")
        self.obstacles = tuple(obstacles)
        self.surfaces = tuple(surfaces)
        self.world_limit = float(world_limit)
        self.default_ground_height = float(default_ground_height)

    def ground_height_at(self, x: float, y: float) -> float:
        """Return the highest walkable surface beneath the supplied X/Y point."""
        heights = [
            surface.height for surface in self.surfaces
            if surface.contains(x, y)
        ]
        return max([self.default_ground_height, *heights])

    @staticmethod
    def _vertical_overlap(z: float, body_height: float, obstacle: AABB) -> bool:
        return z < obstacle.max_z and z + body_height > obstacle.min_z

    def _move_axis(
        self,
        position: float,
        target: float,
        cross_position: float,
        z: float,
        body_height: float,
        radius: float,
        axis: str,
        grounded: bool,
        max_step_height: float,
    ) -> float:
        result = target
        for obstacle in self.obstacles:
            if not self._vertical_overlap(z, body_height, obstacle):
                continue

            if axis == "x":
                cross_min, cross_max = obstacle.min_y - radius, obstacle.max_y + radius
                near, far = obstacle.min_x - radius, obstacle.max_x + radius
            else:
                cross_min, cross_max = obstacle.min_x - radius, obstacle.max_x + radius
                near, far = obstacle.min_y - radius, obstacle.max_y + radius

            if not cross_min <= cross_position <= cross_max:
                continue

            if target > position and position <= near < result:
                result = near
            elif target < position and position >= far > result:
                result = far

        if grounded:
            if axis == "x":
                next_ground = self.ground_height_at(result, cross_position)
            else:
                next_ground = self.ground_height_at(cross_position, result)
            if next_ground > z + max_step_height:
                result = position

        limit = self.world_limit - radius
        return max(-limit, min(limit, result))

    def move_horizontal(
        self,
        x: float,
        y: float,
        z: float,
        dx: float,
        dy: float,
        radius: float = 0.42,
        body_height: float = 1.8,
        grounded: bool = True,
        max_step_height: float = 0.35,
    ) -> tuple[float, float]:
        """Move on X then Y, stopping at obstacles while preserving wall sliding."""
        if radius < 0 or body_height <= 0:
            raise ValueError("radius must be non-negative and body_height positive")
        next_x = self._move_axis(
            x, x + dx, y, z, body_height, radius, "x",
            grounded, max_step_height,
        )
        next_y = self._move_axis(
            y, y + dy, next_x, z, body_height, radius, "y",
            grounded, max_step_height,
        )
        return next_x, next_y

    @staticmethod
    def _segment_aabb_fraction(
        start: tuple[float, float, float],
        end: tuple[float, float, float],
        bounds: AABB,
    ) -> float | None:
        """Return the first segment fraction inside bounds, or None."""
        t_min, t_max = 0.0, 1.0
        for origin, destination, low, high in (
            (start[0], end[0], bounds.min_x, bounds.max_x),
            (start[1], end[1], bounds.min_y, bounds.max_y),
            (start[2], end[2], bounds.min_z, bounds.max_z),
        ):
            delta = destination - origin
            if abs(delta) < 1e-9:
                if origin < low or origin > high:
                    return None
                continue
            first = (low - origin) / delta
            second = (high - origin) / delta
            if first > second:
                first, second = second, first
            t_min = max(t_min, first)
            t_max = min(t_max, second)
            if t_min > t_max:
                return None
        return t_min if 0.0 <= t_min <= 1.0 else None

    def resolve_camera_position(
        self,
        target: tuple[float, float, float],
        desired: tuple[float, float, float],
        radius: float = 0.22,
        clearance: float = 0.12,
    ) -> tuple[float, float, float]:
        """Pull the camera forward when an obstacle blocks its target-to-camera ray."""
        nearest: float | None = None
        for obstacle in self.obstacles:
            fraction = self._segment_aabb_fraction(
                target, desired, obstacle.expanded(radius)
            )
            if fraction is not None and (nearest is None or fraction < nearest):
                nearest = fraction

        if nearest is None:
            return desired

        dx = desired[0] - target[0]
        dy = desired[1] - target[1]
        dz = desired[2] - target[2]
        length = sqrt(dx * dx + dy * dy + dz * dz)
        fraction = max(0.0, nearest - (clearance / length if length else 0.0))
        return (
            target[0] + dx * fraction,
            target[1] + dy * fraction,
            target[2] + dz * fraction,
        )
