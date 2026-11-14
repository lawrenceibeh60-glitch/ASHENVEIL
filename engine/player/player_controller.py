"""Keyboard-driven third-person player controller."""
from math import atan2, degrees
from panda3d.core import Vec3


class PlayerController:
    """Owns player movement state; rendering and camera logic stay separate."""

    def __init__(self, app, input_manager, root, move_speed: float = 6.0,
                 jump_speed: float = 7.0, gravity: float = 20.0,
                 world_limit: float = 22.0) -> None:
        self.app = app
        self.input = input_manager
        self.root = root
        self.move_speed = move_speed
        self.jump_speed = jump_speed
        self.gravity = gravity
        self.world_limit = world_limit
        self.vertical_speed = 0.0
        self.grounded = True

    def update(self, dt: float, camera_heading: float) -> None:
        dt = min(max(dt, 0.0), 0.05)
        forward = float(self.input.is_down("move_forward")) - float(self.input.is_down("move_backward"))
        right = float(self.input.is_down("move_right")) - float(self.input.is_down("move_left"))

        from engine.player.movement_math import camera_relative_direction
        move_x, move_y = camera_relative_direction(forward, right, camera_heading)
        if move_x or move_y:
            self.root.setX(self.root.getX() + move_x * self.move_speed * dt)
            self.root.setY(self.root.getY() + move_y * self.move_speed * dt)
            self.root.setH(degrees(atan2(move_x, move_y)))

        if self.input.consume_press("jump") and self.grounded:
            self.vertical_speed = self.jump_speed
            self.grounded = False

        if not self.grounded:
            self.vertical_speed -= self.gravity * dt
            self.root.setZ(self.root.getZ() + self.vertical_speed * dt)
            if self.root.getZ() <= 0:
                self.root.setZ(0)
                self.vertical_speed = 0
                self.grounded = True

        self.root.setX(max(-self.world_limit, min(self.world_limit, self.root.getX())))
        self.root.setY(max(-self.world_limit, min(self.world_limit, self.root.getY())))
