"""Launch a lightweight Panda3D preview of the installed Greyhaven GLB.

Install the asset first with:
    python tools/install_greyhaven_assets.py

Then run:
    python tools/preview_greyhaven_assets.py
"""
from __future__ import annotations

from pathlib import Path

from direct.showbase.ShowBase import ShowBase
from panda3d.core import (
    AmbientLight,
    CardMaker,
    DirectionalLight,
    LColor,
    Vec3,
    loadPrcFileData,
)

from engine.assets.model_loader import load_model

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ASSET_PATH = (
    "assets/environments/greyhaven/"
    "building_pack_free_low-poly_3d_model_in_fbx.glb"
)


class GreyhavenAssetPreview(ShowBase):
    """Standalone visual inspection window; does not alter the game scene."""

    def __init__(self) -> None:
        loadPrcFileData(
            "ASHENVEIL Greyhaven preview",
            "window-title ASHENVEIL | Greyhaven Asset Preview\n"
            "win-size 1280 800\n"
            "sync-video true\n"
            "audio-library-name null\n",
        )
        super().__init__()
        self.disableMouse()
        self.setBackgroundColor(0.055, 0.065, 0.08, 1)
        self.setFrameRateMeter(True)

        ambient = AmbientLight("greyhaven-preview-ambient")
        ambient.setColor(LColor(0.52, 0.55, 0.62, 1))
        ambient_np = self.render.attachNewNode(ambient)
        self.render.setLight(ambient_np)

        sun = DirectionalLight("greyhaven-preview-sun")
        sun.setColor(LColor(0.95, 0.88, 0.75, 1))
        sun.setDirection(Vec3(-1, -2, -3))
        sun_np = self.render.attachNewNode(sun)
        self.render.setLight(sun_np)

        ground_maker = CardMaker("greyhaven-preview-ground")
        ground_maker.setFrame(-18, 18, -18, 18)
        ground = self.render.attachNewNode(ground_maker.generate())
        ground.setP(-90)
        ground.setZ(-0.04)
        ground.setColor(0.22, 0.25, 0.24, 1)
        ground.setTwoSided(True)

        asset_path = PROJECT_ROOT / ASSET_PATH
        self.asset = load_model(self.loader, asset_path)
        self.asset.reparentTo(self.render)
        self.asset.setPos(0, 0, 0)
        self.asset.setScale(1.0)

        self.camera.setPos(11, -16, 10)
        self.camera.lookAt(0, 0, 1.5)
        self.accept("escape", self.userExit)


if __name__ == "__main__":
    GreyhavenAssetPreview().run()
