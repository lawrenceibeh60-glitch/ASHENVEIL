"""Panda3D application bootstrap for ASHENVEIL."""
from panda3d.core import loadPrcFileData
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText

from engine.core.config import load_json_config
from engine.input.input_manager import InputManager
from engine.scenes.player_test_scene import PlayerTestScene


class AshenveilApp(ShowBase):
    """Creates the runtime, input layer, and current development scene."""

    def __init__(self) -> None:
        self.game_config = load_json_config("game.json")
        self.graphics_config = load_json_config("graphics.json")
        self.controls_config = load_json_config("controls.json")

        window = self.game_config.get("window", {})
        width = int(window.get("width", 1280))
        height = int(window.get("height", 720))
        loadPrcFileData(
            "ASHENVEIL window configuration",
            f"win-size {width} {height}\n"
            f"window-title {self.game_config.get('title', 'ASHENVEIL')}\n"
            f"fullscreen {int(bool(window.get('fullscreen', False)))}\n"
            f"win-fixed-size {int(not bool(window.get('resizable', True)))}\n"
            "sync-video true\n"
            "audio-library-name null\n"
        )

        super().__init__()
        self.disableMouse()

        bg = self.graphics_config.get("background_color", [0.035, 0.045, 0.065, 1.0])
        self.setBackgroundColor(*bg)
        self.setFrameRateMeter(bool(self.game_config.get("runtime", {}).get("show_fps", True)))

        self.input_manager = InputManager(self.controls_config)
        self.scene = PlayerTestScene(self, self.input_manager)
        self.scene.build()

        self.title_text = OnscreenText(
            text="ASHENVEIL  |  M1 PLAYER FOUNDATION",
            pos=(0, 0.94),
            scale=0.043,
            fg=(0.88, 0.84, 0.72, 1),
            shadow=(0, 0, 0, 0.8),
            mayChange=False,
        )
        self.help_text = OnscreenText(
            text="WASD: Move   SPACE: Jump   MOUSE: Orbit camera   ESC: Exit",
            pos=(0, -0.94),
            scale=0.035,
            fg=(0.82, 0.84, 0.86, 1),
            shadow=(0, 0, 0, 0.8),
            mayChange=False,
        )
        self.accept("escape", self.userExit)

    def destroy(self) -> None:
        if hasattr(self, "scene"):
            self.scene.destroy()
        if hasattr(self, "input_manager"):
            self.input_manager.destroy()
        super().destroy()
