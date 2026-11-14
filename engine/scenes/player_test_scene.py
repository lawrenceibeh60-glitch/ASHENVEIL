"""Greybox arena for validating M1 player movement and camera behaviour."""
from panda3d.core import AmbientLight, CardMaker, ClockObject, DirectionalLight, LColor

from engine.player.player_controller import PlayerController
from engine.camera.third_person_camera import ThirdPersonCamera


class PlayerTestScene:
    def __init__(self, app, input_manager) -> None:
        self.app = app
        self.input = input_manager
        self.root = app.render.attachNewNode("ashenveil-m1-player-test")
        self.player = None
        self.camera = None

    def build(self) -> None:
        self._build_lighting()
        self._build_ground()
        self._build_obstacles()
        self._build_player()
        self.camera = ThirdPersonCamera(self.app, self.player)
        self.app.taskMgr.add(self._update, "ashenveil-m1-player-update")

    def _build_lighting(self) -> None:
        ambient = AmbientLight("m1-ambient")
        ambient.setColor(LColor(0.42, 0.45, 0.52, 1))
        ambient_node = self.root.attachNewNode(ambient)
        self.app.render.setLight(ambient_node)
        sun = DirectionalLight("m1-sun")
        sun.setColor(LColor(0.9, 0.84, 0.72, 1))
        sun_node = self.root.attachNewNode(sun)
        self.app.render.setLight(sun_node)

    def _build_ground(self) -> None:
        maker = CardMaker("m1-ground")
        maker.setFrame(-24, 24, -24, 24)
        ground = self.root.attachNewNode(maker.generate())
        ground.setP(-90)
        ground.setZ(-0.02)
        ground.setColor(0.19, 0.23, 0.22, 1)
        ground.setTwoSided(True)

    def _box(self, name, position, scale, color):
        model = self.app.loader.loadModel("models/box")
        model.reparentTo(self.root)
        model.setName(name)
        model.setPos(*position)
        model.setScale(*scale)
        model.setColor(*color)
        return model

    def _build_obstacles(self) -> None:
        self._box("m1-obstacle-west", (-7, 5, 1, ), (1.5, 1.5, 1), (0.36, 0.39, 0.44, 1))
        self._box("m1-obstacle-east", (7, 8, 1.5), (1.5, 1.5, 1.5), (0.48, 0.34, 0.25, 1))
        self._box("m1-platform", (0, 13, 0.5), (5, 2, 0.5), (0.39, 0.40, 0.36, 1))

    def _build_player(self) -> None:
        self.player = self.root.attachNewNode("ashenveil-player")
        body = self.app.loader.loadModel("models/box")
        body.reparentTo(self.player)
        body.setScale(0.45, 0.35, 0.9)
        body.setZ(0.9)
        body.setColor(0.72, 0.70, 0.61, 1)
        self.controller = PlayerController(self.app, self.input, self.player)

    def _update(self, task):
        dt = ClockObject.getGlobalClock().getDt()
        self.controller.update(dt, self.camera.heading)
        self.camera.update()
        return task.cont

    def destroy(self) -> None:
        self.app.taskMgr.remove("ashenveil-m1-player-update")
        self.root.removeNode()
