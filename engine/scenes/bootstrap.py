"""A lightweight procedural scene used to verify the M0 runtime."""
from panda3d.core import (
    AmbientLight,
    CardMaker,
    DirectionalLight,
    LColor,
    Vec3,
)


class BootstrapScene:
    """Builds a simple lit test environment without external assets."""

    def __init__(self, app) -> None:
        self.app = app
        self.root = app.render.attachNewNode("ashenveil-bootstrap-scene")

    def build(self) -> None:
        self._build_lighting()
        self._build_ground()
        self._build_landmarks()
        self.app.camera.setPos(0, -18, 11)
        self.app.camera.lookAt(0, 0, 1.2)

    def _build_lighting(self) -> None:
        ambient = AmbientLight("ashenveil-ambient")
        ambient.setColor(LColor(0.34, 0.38, 0.48, 1))
        ambient_node = self.root.attachNewNode(ambient)
        self.app.render.setLight(ambient_node)

        sun = DirectionalLight("ashenveil-key-light")
        sun.setColor(LColor(0.95, 0.82, 0.62, 1))
        sun.setDirection(Vec3(-1, 1, -2))
        sun_node = self.root.attachNewNode(sun)
        self.app.render.setLight(sun_node)

    def _build_ground(self) -> None:
        maker = CardMaker("test-ground")
        maker.setFrame(-24, 24, -24, 24)
        ground = self.root.attachNewNode(maker.generate())
        ground.setP(-90)
        ground.setZ(-0.05)
        ground.setColor(0.16, 0.20, 0.19, 1)
        ground.setTwoSided(True)

    def _build_landmarks(self) -> None:
        # Panda3D's bundled box model gives us a dependency-free test landmark.
        for x, y, z, scale, color in (
            (-3.0, 2.0, 1.0, 1.0, (0.34, 0.39, 0.46, 1)),
            (3.0, 3.0, 1.5, 1.5, (0.48, 0.34, 0.25, 1)),
            (0.0, 7.0, 2.0, 2.0, (0.42, 0.39, 0.31, 1)),
        ):
            landmark = self.app.loader.loadModel("models/box")
            landmark.reparentTo(self.root)
            landmark.setPos(x, y, z)
            landmark.setScale(scale)
            landmark.setColor(*color)
