"""Launch a fitted Panda3D preview of the installed Greyhaven GLB.

Install the asset first:
    python tools/install_greyhaven_assets.py

Then run:
    python tools/preview_greyhaven_assets.py
"""
from __future__ import annotations

from math import radians, tan
from pathlib import Path

from direct.showbase.ShowBase import ShowBase
from panda3d.core import (
    AmbientLight,
    CardMaker,
    DirectionalLight,
    LColor,
    Point3,
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
    """Standalone visual inspection window; does not alter the player scene."""

    def __init__(self) -> None:
        loadPrcFileData(
            "ASHENVEIL Greyhaven preview",
            "window-title ASHENVEIL | Greyhaven Asset Preview\\n"
            "win-size 1280 800\\n"
            "sync-video true\\n"
            "audio-library-name null\\n",
        )
        super().__init__()
        self.disableMouse()
        self.setBackgroundColor(0.035, 0.045, 0.065, 1)
        self.setFrameRateMeter(True)

        ambient = AmbientLight("greyhaven-preview-ambient")
        ambient.setColor(LColor(0.62, 0.64, 0.69, 1))
        ambient_np = self.render.attachNewNode(ambient)
        self.render.setLight(ambient_np)

        sun = DirectionalLight("greyhaven-preview-sun")
        sun.setColor(LColor(0.95, 0.88, 0.75, 1))
        sun.setDirection(Vec3(-1, -2, -3))
        sun_np = self.render.attachNewNode(sun)
        self.render.setLight(sun_np)

        asset_path = PROJECT_ROOT / ASSET_PATH
        self.asset = load_model(self.loader, asset_path)
        self.asset.reparentTo(self.render)

        bounds = self.asset.getTightBounds()
        if not bounds:
            raise RuntimeError("The Greyhaven GLB loaded but has no renderable bounds.")

        lower, upper = bounds
        center = Point3(
            (lower.x + upper.x) * 0.5,
            (lower.y + upper.y) * 0.5,
            (lower.z + upper.z) * 0.5,
        )
        extents = upper - lower
        radius = max(extents.length() * 0.5, 1.0)

        print("Greyhaven GLB loaded in Panda3D.")
        print(f"Bounds minimum: {lower}")
        print(f"Bounds maximum: {upper}")
        print(f"Approximate diameter: {radius * 2:.2f} Panda units")

        ground_size = max(extents.x, extents.y, 12.0) * 1.6
        ground_maker = CardMaker("greyhaven-preview-ground")
        ground_maker.setFrame(
            center.x - ground_size,
            center.x + ground_size,
            center.y - ground_size,
            center.y + ground_size,
        )
        ground = self.render.attachNewNode(ground_maker.generate())
        ground.setP(-90)
        ground.setZ(lower.z - 0.06)
        ground.setColor(0.19, 0.23, 0.22, 1)
        ground.setTwoSided(True)

        vertical_fov = float(self.camLens.getFov()[1])
        distance = radius / tan(radians(vertical_fov * 0.5)) * 1.25
        view_direction = Vec3(1.0, -1.35, 0.85)
        view_direction.normalize()
        self.camera.setPos(center + view_direction * distance)
        self.camera.lookAt(center)

        self.accept("escape", self.userExit)


if __name__ == "__main__":
    GreyhavenAssetPreview().run()
