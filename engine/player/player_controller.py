"""Collision-aware third-person player movement and simple grounded traversal."""
from math import atan2, degrees

from engine.physics.collision_world import CollisionWorld


class PlayerController:
    """Owns player movement, jumping and support-surface state."""

    def __init__(
        self,
        app,
        input_manager,
        root,
        move_speed: float = 6.0,
        jump_speed: float = 7.0,
        gravity: float = 20.0,
        world_limit: float = 22.0,
        collision_world: CollisionWorld | None = None,
        player_radius: float = 0.42,
        body_height: float = 1.8,
        step_height: float = 0.35,
    ) -> None:
        self.app = app
        self.input = input_manager
        self.root = root
        self.move_speed = move_speed
        self.jump_speed = jump_speed
        self.gravity = gravity
        self.world_limit = world_limit
        self.collision_world = collision_world or CollisionWorld(
            world_limit=world_limit
        )
        self.player_radius = player_radius
        self.body_height = body_height
        self.step_height = step_height
        self.vertical_speed = 0.0
        self.grounded = True

    def update(self, dt: float, camera_heading: float) -> None:
        dt = min(max(dt, 0.0), 0.05)

        if self.input.consume_press("jump") and self.grounded:
            self.vertical_speed = self.jump_speed
            self.grounded = False

        forward = float(self.input.is_down("move_forward")) - float(
            self.input.is_down("move_backward")
        )
        right = float(self.input.is_down("move_right")) - float(
            self.input.is_down("move_left")
        )

        from engine.player.movement_math import camera_relative_direction

        move_x, move_y = camera_relative_direction(forward, right, camera_heading)
        current_z = self.root.getZ()
        next_x, next_y = self.collision_world.move_horizontal(
            self.root.getX(),
            self.root.getY(),
            current_z,
            move_x * self.move_speed * dt,
            move_y * self.move_speed * dt,
            radius=self.player_radius,
            body_height=self.body_height,
            grounded=self.grounded,
            max_step_height=self.step_height,
        )
        self.root.setX(next_x)
        self.root.setY(next_y)

        if move_x or move_y:
            self.root.setH(degrees(atan2(move_x, move_y)))

        if self.grounded:
            support_height = self.collision_world.ground_height_at(next_x, next_y)
            if support_height < current_z - 1e-4:
                self.grounded = False
                self.vertical_speed = 0.0
            else:
                self.root.setZ(support_height)

        if not self.grounded:
            previous_z = self.root.getZ()
            self.vertical_speed -= self.gravity * dt
            next_z = previous_z + self.vertical_speed * dt
            support_height = self.collision_world.ground_height_at(next_x, next_y)

            if (
                self.vertical_speed <= 0
                and previous_z >= support_height
                and next_z <= support_height
            ):
                self.root.setZ(support_height)
                self.vertical_speed = 0.0
                self.grounded = True
            else:
                self.root.setZ(next_z)
