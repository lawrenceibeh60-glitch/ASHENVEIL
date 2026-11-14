"""Panda3D application bootstrap for ASHENVEIL."""
from panda3d.core import loadPrcFileData
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText

from engine.core.config import load_json_config
from engine.scenes.bootstrap import BootstrapScene


class AshenveilApp(ShowBase):
    """Creates the initial window, renderer, scene, and runtime controls."""

    def __init__(self) -> None:
        self.game_config = load_json_config("game.json")
        self.graphics_config = load_json_config("graphics.json")

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

        self.scene = BootstrapScene(self)
        self.scene.build()

        self.title_text = OnscreenText(
            text="ASHENVEIL  |  FOUNDATION TEST SCENE",
            pos=(0, 0.92),
            scale=0.045,
            fg=(0.88, 0.84, 0.72, 1),
            shadow=(0, 0, 0, 0.8),
            mayChange=False,
        )
        self.accept("escape", self.userExit)
